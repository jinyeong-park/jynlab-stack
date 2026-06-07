## Step 3: PASS 1. Cut retake blocks

**This is you (Claude Code) working directly.**

### 3a. Read transcript and script

1. List all utterances from `transcript_original.json`
2. Read the script file
3. Map script sections to utterance ranges

### 3b. Identify retake blocks

Walk through the script line by line. For each scripted line, find ALL takes in the transcript. Keep the BEST (usually last clean) take. Mark everything else as a cut block.

**What to cut (BLOCKS only, not individual words):**
- Retake blocks: same scripted line recorded multiple times → **always keep the LAST clean version**, cut all earlier takes as ONE block
- Sentence restarts: speaker bails on a sentence partway through and starts the same sentence over → cut from the start of the failed attempt to the start of the successful one. The speaker almost always restarts at the beginning of the sentence, not mid-sentence.
- Practice attempts: speaker repeating a word 3+ times (e.g., "wouldn't" x5) → cut entire practice block
- Directions to self: "one more", "delete that section", "let me try again"
- Dead air between takes (gaps > 3s with no speech)

**What to KEEP:**
- Everything that matches the script (100%)
- Improvised additions (the ~2% extra)
- Natural pauses between sentences (< 1s)
- Breaths. NEVER cut at breaths

**CRITICAL RULES:**
- Cut as BLOCKS with start/end timestamps, NOT individual utterances
- Never cut within a sentence. only between takes
- Never cut at a breath or short pause
- If in doubt, KEEP it

### 3c. Define KEEP ranges (preferred) or CUT_ZONES

**Preferred: KEEP ranges.** Map each script line to its best take. More accurate than defining what to cut.

```python
KEEP = [
    (start_sec, end_sec),  # Script line: "..."
    ...
]
```

Alternative: CUT_ZONES if easier for the specific recording.
```python
CUT_ZONES = [
    (start_sec, end_sec),  # description
    ...
]
```

### 3d. Render Pass 1

Write and run `{EDIT_DIR}/pass1_cut.py` with this structure:

```python
#!/usr/bin/env python3
import json, subprocess, re, os, sys

FOOTAGE = "{footage_path}"
OUT_DIR = "{edit_dir}"
TRANSCRIPT = OUT_DIR + "/transcript_original.json"
SPEED = {speed}
SILENCE_MIN = 3.0
SILENCE_NOISE = -35

# Load transcript
with open(TRANSCRIPT) as f:
    dg = json.load(f)
words = dg["results"]["channels"][0]["alternatives"][0]["words"]
utts = dg["results"]["utterances"]

# Get source duration
SOURCE_DUR = float(subprocess.run(
    ["ffprobe","-v","quiet","-show_entries","format=duration","-of","csv=p=0", FOOTAGE],
    capture_output=True, text=True
).stdout.strip())
print(f"Source: {SOURCE_DUR:.1f}s ({SOURCE_DUR/60:.1f} min)")

def detect_silences(video_path, duration):
    cmd = ["ffmpeg","-i",video_path,"-t",str(duration),
           "-af",f"silencedetect=noise={SILENCE_NOISE}dB:duration={SILENCE_MIN}",
           "-f","null","/dev/null"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    ss = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", r.stderr)]
    se = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", r.stderr)]
    return list(zip(ss, se))

CUT_ZONES = [
    # paste your cut zones here. (start_sec, end_sec) tuples
]

# Sort and merge overlapping zones
CUT_ZONES.sort()
merged = []
for cs, ce in CUT_ZONES:
    if merged and cs <= merged[-1][1]:
        merged[-1] = (merged[-1][0], max(merged[-1][1], ce))
    else:
        merged.append((cs, ce))

total_cut = sum(ce-cs for cs,ce in merged)
print(f"{len(merged)} cut zones, {total_cut:.1f}s retake time")

# Build keep segments
first_word = words[0]['start'] if words else 0
full_range = [(max(0, first_word - 0.2), SOURCE_DUR)]

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
    return [(s, e) for s, e in result if e - s > 0.1]

keep = subtract_zones(full_range, merged)

# Trim long silences (>3s). keep 0.5s
silences = detect_silences(FOOTAGE, SOURCE_DUR)
silence_trims = []
for ss, se in silences:
    if se - ss > SILENCE_MIN:
        trim_start = ss + 0.5
        trim_end = se - 0.3
        if trim_end > trim_start:
            silence_trims.append((trim_start, trim_end))
if silence_trims:
    keep = subtract_zones(keep, silence_trims)
    print(f"Trimmed {len(silence_trims)} long silence gaps")

total_keep = sum(e-s for s,e in keep)
print(f"Keep: {len(keep)} segments, {total_keep:.1f}s -> {total_keep/SPEED:.1f}s at {SPEED}x")

# Save segments and render using render_cuts.py
segments_path = OUT_DIR + "/pass1_segments.json"
with open(segments_path, "w") as f:
    json.dump(keep, f)

out_path = OUT_DIR + "/pass1.mp4"
r = subprocess.run(["python3", OUT_DIR + "/render_cuts.py", FOOTAGE, segments_path, out_path])
if r.returncode != 0: sys.exit(1)
```

Print: `Pass 1: {SOURCE}s → {RESULT}s ({N} segments, {CUT}s removed)`

**If pass1_cut.py fails:** check ffmpeg is installed, check segment count isn't > 500 (ffmpeg concat limit), check FOOTAGE path exists.

### 3e. MANDATORY verification gate

**Do NOT proceed to Pass 2 until this passes.**

1. Re-transcribe: `python3 retranscribe.py pass1.mp4 transcript_pass1_verify.json`
2. Run `verify_cuts.py` (see template below)
3. Read EVERY utterance against the script. is any line missing?
4. If issues found: fix and re-verify. Repeat until clean.
5. Do at least 2 re-transcribe+check cycles even if you think it's clean.

Write `{EDIT_DIR}/verify_cuts.py`:

```python
#!/usr/bin/env python3
"""Thorough verification of cut video against script."""
import json, sys

TRANSCRIPT = sys.argv[1]  # transcript JSON path

with open(TRANSCRIPT) as f:
    dg = json.load(f)
words = dg["results"]["channels"][0]["alternatives"][0]["words"]
utts = dg["results"]["utterances"]

print(f"=== VERIFICATION ({len(utts)} utterances, {len(words)} words) ===\n")

# 1. Word-level consecutive repeats
skip = {'a','the','to','in','no','not','i','and','you','of','it','is','on','or','at','for','my','me','so','do','be','if','up','we','he','an','as','all','our'}
print("1. WORD REPEATS:")
found = 0
for i in range(1, len(words)):
    w1 = words[i]['word'].lower().strip('.,!?"')
    w0 = words[i-1]['word'].lower().strip('.,!?"')
    if w1 == w0 and w1 not in skip and len(w1) > 1:
        print(f"   '{w1}' x2 at {words[i-1]['start']:.1f}s")
        found += 1
print(f"   {'CLEAN' if found == 0 else f'{found} ISSUES'}\n")

# 2. Phrase repeats (2-3 word phrases)
print("2. PHRASE REPEATS:")
all_text = ' '.join(u['transcript'].lower() for u in utts)
all_words = all_text.split()
phrase_issues = 0
seen_phrases = set()
for length in [3, 2]:
    for i in range(len(all_words) - length):
        phrase = ' '.join(all_words[i:i+length])
        if phrase in seen_phrases or len(phrase) < 6:
            continue
        rest = ' '.join(all_words[i+length:])
        if phrase in rest:
            # Skip common intentional repeats
            common = {'of the','in the','on the','for the','to the','and the','at the',
                      'you can','is the','of my','i was','a month','if you','on one',
                      'no fine','the end','i know','for this','on day','you type',
                      'i wouldn','not not','each one','can do','do it','it from',
                      'end of','have a','plus the','these are','day one','gives you',
                      'ninety days','you already','already know','not sign',
                      'not followers','not sounds'}
            if phrase not in common:
                print(f"   '{phrase}' appears 2+ times")
                phrase_issues += 1
                seen_phrases.add(phrase)
print(f"   {'CLEAN' if phrase_issues == 0 else f'{phrase_issues} ISSUES'}\n")

# 3. Gaps > 0.3s between words
print("3. GAPS > 0.3s:")
gap_count = 0
for i in range(len(words)-1):
    gap = words[i+1]['start'] - words[i]['end']
    if gap > 0.3:
        print(f"   {gap:.2f}s at {words[i]['end']:.1f}s: '{words[i]['word']}' ... '{words[i+1]['word']}'")
        gap_count += 1
print(f"   {gap_count} gaps found\n")

# 4. Numbers found (for manual cross-check against script)
print("4. NUMBERS (cross-check against script):")
for w in words:
    if any(c.isdigit() for c in w['word']) or w['word'].startswith('$'):
        print(f"   {w['start']:.1f}s: {w['word']}")

total = "PASS" if found == 0 and phrase_issues == 0 else "FAIL"
print(f"\n=== RESULT: {total} ===")
```

---

