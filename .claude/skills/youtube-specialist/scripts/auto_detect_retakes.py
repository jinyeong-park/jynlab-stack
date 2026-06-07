#!/usr/bin/env python3
"""Aggressive retake detector.

Walks the transcript and finds:
- Single-word repeats: "but but", "I I", "the the" (with tiny gap)
- 2/3/4/5-word phrase repeats within 3 seconds
- For each detected retake, the cut zone is from the START of the first
  instance to the START of the second (clean) instance.

Protected pairs: never split between Claude and Code, etc.
"""
import json, sys, re

TRANSCRIPT_PATH = sys.argv[1]
OUTPUT_JSON = sys.argv[2]

with open(TRANSCRIPT_PATH) as f:
    dg = json.load(f)
words = dg["results"]["channels"][0]["alternatives"][0]["words"]

# Normalize: get clean lowercase word + start/end + sentence-end flag
norm = []
for w in words:
    clean = w["word"].lower().strip(".,!?\"'")
    pw = w.get("punctuated_word", w["word"])
    sentence_end = pw.rstrip().endswith((".", "!", "?"))
    norm.append({"w": clean, "s": w["start"], "e": w["end"], "raw": w["word"], "pw": pw, "se": sentence_end})

# Protected multi-word units. never cut between these tokens
PROTECTED_PAIRS = {
    ("claude", "code"),
    ("clothecode", "code"),
    ("model", "context"),
    ("context", "protocol"),
    ("agent", "founders"),
    ("liam", "ottley"),
    ("liam", "oddly"),
    ("liam", "oderley"),
    ("nate", "hirk"),
    ("nate", "herc"),
    ("nate", "hark"),
    ("google", "antigravity"),
    ("google", "calendar"),
    ("find", "niche"),
    ("build", "offer"),
    ("build", "landing"),
    ("outreach", "engine"),
    ("close", "deal"),
    ("mission", "control"),
    ("skill", "eval"),
    ("skill", "improve"),
    ("yt", "cut"),
    ("cut", "edit"),
    ("youtube", "cut"),
}

# Words that are allowed to repeat naturally (don't flag)
ALLOWED_REPEATS = {
    "no",   # "no, no, no" emphasis
    "yes",
    "very",
    "so",
    "really",
    "ha",  # laughter
    "ok",
    "okay",
}

# Filler words. single-word repeats among these are common natural speech;
# only flag if exact same token repeats with very small gap (< 0.4s)
COMMON_SHORT = {"i", "a", "the", "to", "in", "of", "and", "is", "it", "but",
                "or", "you", "me", "we", "he", "she", "they", "this", "that",
                "for", "on", "at", "by", "as", "be", "do", "if", "an", "my",
                "your", "his", "her", "our", "all"}

cut_zones = []
debug = []

def is_protected(i):
    """Check if position i forms a protected pair with i+1 or i-1."""
    if i + 1 < len(norm):
        if (norm[i]["w"], norm[i+1]["w"]) in PROTECTED_PAIRS:
            return True
    if i > 0:
        if (norm[i-1]["w"], norm[i]["w"]) in PROTECTED_PAIRS:
            return True
    return False

# Strategy: for each position, check if the next N words match the next-next N words
# Try N from 5 down to 1 (prefer longer matches first)
covered = set()  # word indices already covered by a cut

def already_covered(start_i, end_i):
    return any(i in covered for i in range(start_i, end_i + 1))

i = 0
while i < len(norm) - 1:
    if i in covered:
        i += 1
        continue

    found = False
    # Try N=5 down to 1
    for n in (5, 4, 3, 2, 1):
        if i + 2 * n > len(norm):
            continue

        seg_a = [norm[i + k]["w"] for k in range(n)]
        seg_b = [norm[i + n + k]["w"] for k in range(n)]

        # Exact match required, OR prefix-match for N>=3
        # (same first N-1 words, last word differs but is similar)
        is_exact = seg_a == seg_b
        is_prefix = (
            n >= 3
            and seg_a[:-1] == seg_b[:-1]
            and seg_a[-1] != seg_b[-1]
            and (seg_a[-1].startswith(seg_b[-1])
                 or seg_b[-1].startswith(seg_a[-1])
                 or len(seg_a[-1]) <= 2
                 or len(seg_b[-1]) <= 2)
        )
        if not (is_exact or is_prefix):
            continue

        # Check time gap between end of A and start of B
        gap = norm[i + n]["s"] - norm[i + n - 1]["e"]
        # Allow up to 2.5s gap for retake detection
        if gap > 2.5:
            continue

        # SENTENCE BOUNDARY PROTECTION:
        # If the LAST word of the first instance ends a sentence (. ! ?),
        # this is two separate sentences, not a retake.
        # Example: "like this. This is what..." or "phase five. Phase five competition"
        if norm[i + n - 1]["se"]:
            continue

        # For single-word repeats, be stricter
        if n == 1:
            word = seg_a[0]
            # Skip allowed natural repeats
            if word in ALLOWED_REPEATS:
                continue
            # For very common short words, only count if super tight gap
            if word in COMMON_SHORT and gap > 0.6:
                continue
            # Skip if word is too short (likely artifact)
            if len(word) <= 1 and word not in ("i", "a"):
                continue

        # Check protected pairs - don't cut into a protected unit
        # Cut would be: from norm[i]["s"] to norm[i+n]["s"]
        # That removes words [i .. i+n-1]
        # We need to verify words i-1+i and i+n-1+i+n don't form protected pairs across the cut
        skip = False
        for k in range(n):
            if is_protected(i + k):
                skip = True
                break
        if skip:
            continue

        # Don't include this if any of the words is already covered
        if already_covered(i, i + n - 1):
            continue

        # Record cut zone: from start of first instance to start of second instance
        cut_start = norm[i]["s"] - 0.05  # tiny lead-in
        cut_end = norm[i + n]["s"] - 0.02  # stop just before second instance starts

        if cut_end <= cut_start:
            continue
        if cut_end - cut_start < 0.05:
            continue

        cut_zones.append((cut_start, cut_end))
        debug.append({
            "n": n,
            "phrase": " ".join(seg_a),
            "first_at": norm[i]["s"],
            "second_at": norm[i + n]["s"],
            "gap": gap,
            "cut": (cut_start, cut_end),
        })
        # Mark first instance words as covered
        for k in range(n):
            covered.add(i + k)
        found = True
        i = i + n  # skip past first instance
        break

    if not found:
        i += 1

print(f"Found {len(cut_zones)} retakes")
print()
print("--- Top 30 retakes by length (all phrases listed) ---")
debug.sort(key=lambda x: (-x["n"], x["first_at"]))
for d in debug[:30]:
    print(f"  N={d['n']} at {d['first_at']:7.2f}s gap={d['gap']:.2f}s: \"{d['phrase']}\" (cut {d['cut'][0]:.2f}-{d['cut'][1]:.2f})")

if len(debug) > 30:
    print(f"  ... and {len(debug) - 30} more")

# Save
with open(OUTPUT_JSON, "w") as f:
    json.dump({
        "cuts": cut_zones,
        "debug": debug,
    }, f, indent=2)

print(f"\nSaved to {OUTPUT_JSON}")
print(f"Total cut time: {sum(e - s for s, e in cut_zones):.1f}s")
