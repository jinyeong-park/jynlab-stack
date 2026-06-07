## Step 4: PASS 2. Auto-detect retakes and detail cuts

**CRITICAL: Do NOT rely on manual transcript review for retakes. Use the auto-detector below. It catches every phrase repeat and stutter automatically, including ones you'd miss reading the transcript.**

### 4a. Re-transcribe pass 1 result

```bash
python3 {EDIT_DIR}/retranscribe.py {EDIT_DIR}/pass1.mp4 {EDIT_DIR}/transcript_pass2.json
```

### 4b. Run the auto-retake detector

Write and run `{EDIT_DIR}/auto_detect_retakes.py`. This script walks the transcript with N-gram phrase repeat detection, respects sentence boundaries, and protects multi-word names.

```python
#!/usr/bin/env python3
"""Auto-detect retakes: any N-gram phrase said twice within 2.5s of each other.

Rules:
- N=5 → 1, check each position for phrase repeats
- For N>=3, also check prefix retakes: first N-1 words match, last word differs
  (catches "what do you" → "what do your")
- Sentence boundary protection (Pass A/B only): if first instance ends with . ! ?
  (from Deepgram's punctuated_word field), treat as two separate sentences and skip
  in Pass A/B. These cases are caught by Pass C instead.
- Pass C: sentence-restart detection. Speakers usually restart at sentence
  boundaries. When two adjacent sentences begin with the same first 2-3 words
  and the gap between them is < 2.5s, the first is a failed take. Cut the
  entire first sentence and keep the LAST attempt.
- Multi-word name protection: never cut inside protected phrases
- Single-word repeats: only flagged with tight gap (<0.6s) or non-trivial words
- Outputs JSON list of cut zones for apply_retake_cuts.py
"""
import json, sys

TRANSCRIPT = sys.argv[1]
OUTPUT = sys.argv[2]
MAX_GAP = 2.5  # max seconds between first and second instance
TIGHT_GAP = 0.6  # for single-word repeats

# Never cut inside these multi-word names
PROTECTED_PAIRS = [
    ("claude", "code"),
    ("model", "context"),
    ("agent", "founders"),
    ("google", "antigravity"),
    ("liam", "ottley"),
    ("nate", "hirk"),
    ("nick", "saraev"),
    ("outreach", "engine"),
    ("skill", "eval"),
    ("mission", "control"),
    ("find", "niche"),
    ("build", "offer"),
    ("build", "pipeline"),
    ("build", "landing"),
    ("build", "delivery"),
    ("close", "deal"),
    ("yt", "cut"),
    ("yt", "research"),
    ("yt", "script"),
    ("business", "md"),
    ("mcp", "server"),
    ("agent", "sdk"),
    ("value", "equation"),
    ("dopamine", "ladder"),
    ("ai", "learning"),
    ("deepgram", "nova"),
    ("anthropic", "claude"),
    ("build", "eval"),
]

# Trivial single-word repeats to skip unless tight gap
TRIVIAL = {
    "a", "the", "to", "in", "on", "of", "and", "or", "but", "so",
    "no", "not", "yes", "it", "is", "as", "at", "if", "be", "do",
    "i", "you", "we", "he", "she", "they", "this", "that", "an",
}

with open(TRANSCRIPT) as f:
    dg = json.load(f)
words = dg["results"]["channels"][0]["alternatives"][0]["words"]

def word_text(w):
    """Get lowercase text, stripped of punctuation."""
    return w.get("word", "").lower().strip(".,!?\"'")

def is_sentence_end(w):
    """Check if punctuated_word ends with sentence terminator."""
    pw = w.get("punctuated_word", w.get("word", ""))
    return any(pw.rstrip().endswith(p) for p in (".", "!", "?"))

def is_protected_split(w1, w2):
    """True if w1/w2 are a protected multi-word pair."""
    t1 = word_text(w1)
    t2 = word_text(w2)
    for p1, p2 in PROTECTED_PAIRS:
        if t1 == p1 and t2 == p2:
            return True
    return False

def ngram_at(pos, n):
    """Get list of n word texts starting at position."""
    if pos + n > len(words):
        return None
    return [word_text(words[pos + i]) for i in range(n)]

cuts = []
used_positions = set()

# Pass A: N-gram repeat detection (N=5 down to 2)
for n in range(5, 1, -1):
    for i in range(len(words) - 2 * n):
        if i in used_positions:
            continue
        ngram1 = ngram_at(i, n)
        if not ngram1 or any(not t for t in ngram1):
            continue

        # Check exact repeat at next position
        j = i + n
        ngram2 = ngram_at(j, n)

        # Also check prefix retake for N>=3: first N-1 words match, last differs
        prefix_retake = False
        if not ngram2 or ngram1 != ngram2:
            if n >= 3:
                prefix1 = ngram1[:-1]
                prefix2 = ngram_at(j, n - 1)
                if prefix2 and prefix1 == prefix2:
                    # Also check the word AFTER j+n-1 exists (the "real" version)
                    if j + n - 1 < len(words):
                        prefix_retake = True
                        ngram2 = prefix2 + [word_text(words[j + n - 1])]
            if not prefix_retake:
                continue

        # Gap check
        gap = words[j]["start"] - words[i + n - 1]["end"]
        if gap > MAX_GAP:
            continue

        # Sentence boundary protection
        if is_sentence_end(words[i + n - 1]):
            continue

        # Multi-word name protection: check if cut would split a protected pair
        # Cut zone would be from words[i].start to words[j].start
        cut_start = words[i]["start"]
        cut_end = words[j]["start"]
        split_protected = False
        for k in range(i, j):
            if k + 1 < len(words):
                if is_protected_split(words[k], words[k + 1]):
                    # Cut only OK if the protected pair is fully inside or fully outside
                    w_mid = words[k + 1]["start"]
                    if cut_start < w_mid < cut_end and not (cut_start < words[k]["start"]):
                        split_protected = True
                        break
        if split_protected:
            continue

        phrase = " ".join(ngram1)
        cuts.append({
            "start": cut_start,
            "end": cut_end,
            "n": n,
            "phrase": phrase,
            "type": "prefix" if prefix_retake else "exact",
        })
        for k in range(i, j):
            used_positions.add(k)
        break

# Pass B: Single-word stutters (tight gap OR non-trivial word)
for i in range(len(words) - 1):
    if i in used_positions:
        continue
    t1 = word_text(words[i])
    t2 = word_text(words[i + 1])
    if not t1 or t1 != t2:
        continue
    gap = words[i + 1]["start"] - words[i]["end"]
    # Skip trivial words unless very tight
    if t1 in TRIVIAL and gap > TIGHT_GAP:
        continue
    # Skip if protected
    if is_protected_split(words[i], words[i + 1]):
        continue
    # Skip if sentence end
    if is_sentence_end(words[i]):
        continue
    cuts.append({
        "start": words[i]["start"],
        "end": words[i + 1]["start"],
        "n": 1,
        "phrase": t1,
        "type": "stutter",
    })
    used_positions.add(i)

# Pass C: Sentence-restart detection
# Speakers usually restart at sentence boundaries. If two adjacent sentences
# begin with the same first 2-3 words and the gap between them is < 2.5s,
# treat the first as a failed take and cut the entire first sentence.
# Always keep the LAST attempt.
SENTENCE_OPEN_N = 3       # compare first 3 words
SENTENCE_OPEN_MIN = 2     # but accept a 2-word match if 3rd doesn't exist
SENTENCE_RESTART_GAP = 2.5

# Build sentence list: each = (start_idx, end_idx_inclusive)
sentences = []
sent_start = 0
for k, w in enumerate(words):
    if is_sentence_end(w):
        sentences.append((sent_start, k))
        sent_start = k + 1
if sent_start < len(words):
    sentences.append((sent_start, len(words) - 1))

def sentence_opening(s_start, s_end):
    """First N non-trivial-position words of a sentence (lowercased)."""
    n = min(SENTENCE_OPEN_N, s_end - s_start + 1)
    return [word_text(words[s_start + i]) for i in range(n)]

for idx in range(len(sentences) - 1):
    s1_start, s1_end = sentences[idx]
    s2_start, s2_end = sentences[idx + 1]

    # Skip if any word in s1 already cut
    if any(p in used_positions for p in range(s1_start, s1_end + 1)):
        continue

    # Gap between sentence end and next sentence start
    gap = words[s2_start]["start"] - words[s1_end]["end"]
    if gap > SENTENCE_RESTART_GAP:
        continue

    open1 = sentence_opening(s1_start, s1_end)
    open2 = sentence_opening(s2_start, s2_end)
    if not open1 or not open2:
        continue

    # Need at least SENTENCE_OPEN_MIN matching opening words
    match_len = 0
    for a, b in zip(open1, open2):
        if a and a == b:
            match_len += 1
        else:
            break
    if match_len < SENTENCE_OPEN_MIN:
        continue

    # Don't cut if the failed sentence is suspiciously long (>12 words). that
    # would suggest two real sentences that happen to share an opening
    if (s1_end - s1_start + 1) > 12:
        continue

    # Multi-word name protection: don't split a protected pair
    cut_start = words[s1_start]["start"]
    cut_end = words[s2_start]["start"]
    split_protected = False
    for k in range(s1_start, s2_start):
        if k + 1 < len(words) and is_protected_split(words[k], words[k + 1]):
            w_mid = words[k + 1]["start"]
            if cut_start < w_mid < cut_end and not (cut_start < words[k]["start"]):
                split_protected = True
                break
    if split_protected:
        continue

    phrase = " ".join(open1[:match_len])
    cuts.append({
        "start": cut_start,
        "end": cut_end,
        "n": match_len,
        "phrase": f"sentence-restart: {phrase}...",
        "type": "sentence_restart",
    })
    for k in range(s1_start, s1_end + 1):
        used_positions.add(k)

# Merge overlapping cuts
cuts.sort(key=lambda c: c["start"])
merged = []
for c in cuts:
    if merged and c["start"] <= merged[-1]["end"]:
        merged[-1]["end"] = max(merged[-1]["end"], c["end"])
        merged[-1]["phrase"] += f" + {c['phrase']}"
    else:
        merged.append(dict(c))

total_cut = sum(c["end"] - c["start"] for c in merged)
print(f"Found {len(merged)} retakes ({total_cut:.1f}s total)")
for c in merged[:20]:
    print(f"  {c['start']:.1f}-{c['end']:.1f}s ({c['n']}-gram {c['type']}): \"{c['phrase']}\"")
if len(merged) > 20:
    print(f"  ... and {len(merged) - 20} more")

with open(OUTPUT, "w") as f:
    json.dump(merged, f, indent=2)
print(f"✓ {OUTPUT}")
```

Run it:

```bash
python3 {EDIT_DIR}/auto_detect_retakes.py \
    {EDIT_DIR}/transcript_pass2.json \
    {EDIT_DIR}/pass2_retakes.json
```

### 4c. Apply cuts

Write `{EDIT_DIR}/apply_retake_cuts.py`:

```python
#!/usr/bin/env python3
"""Apply retake cuts JSON to a video via render_cuts.py."""
import json, subprocess, sys, os

VIDEO = sys.argv[1]
RETAKES_JSON = sys.argv[2]
OUTPUT = sys.argv[3]

SOURCE_DUR = float(subprocess.run(
    ["ffprobe","-v","quiet","-show_entries","format=duration","-of","csv=p=0", VIDEO],
    capture_output=True, text=True
).stdout.strip())

with open(RETAKES_JSON) as f:
    cuts = json.load(f)

# Build keep segments
def subtract_zones(segs, zones):
    result = []
    for ks, ke in segs:
        parts = [(ks, ke)]
        for zs, ze in zones:
            new_parts = []
            for s, e in parts:
                if ze <= s or zs >= e: new_parts.append((s, e))
                elif zs <= s and ze >= e: pass
                elif zs > s and ze < e: new_parts.extend([(s, zs), (ze, e)])
                elif zs <= s: new_parts.append((ze, e))
                else: new_parts.append((s, zs))
            parts = new_parts
        result.extend(parts)
    return [(s, e) for s, e in result if e - s > 0.03]

zones = [(c["start"], c["end"]) for c in cuts]
keep = subtract_zones([(0, SOURCE_DUR)], zones)

segs_path = OUTPUT.replace(".mp4", "_segments.json")
with open(segs_path, "w") as f:
    json.dump(keep, f)

edit_dir = os.path.dirname(VIDEO)
subprocess.run(["python3", os.path.join(edit_dir, "render_cuts.py"),
                VIDEO, segs_path, OUTPUT])
```

Apply:

```bash
python3 {EDIT_DIR}/apply_retake_cuts.py \
    {EDIT_DIR}/pass1.mp4 \
    {EDIT_DIR}/pass2_retakes.json \
    {EDIT_DIR}/pass2.mp4
```

**If detector finds 0 retakes:** copy pass1.mp4 to pass2.mp4 and continue.

Output: `{EDIT_DIR}/pass2.mp4`

Print: `Pass 2: {N} retakes auto-detected, {INPUT}s → {OUTPUT}s`

### 4d. MANDATORY iterative verification

1. Re-transcribe pass2.mp4 → transcript_pass2_verify.json
2. Run auto_detect_retakes.py on the new transcript
3. If ANY retakes remain, apply them and re-check
4. **Loop until detector finds 0 retakes.** The detector should converge in 1-2 iterations. If it doesn't, check for sentence-boundary false positives.
5. After 0 retakes, also run `verify_cuts.py` for phrase repeats, word repeats, gaps, and numbers.

---

