## Step 5: PASS 3. Silence polish and final check

### 5a. Re-transcribe pass 2 result

```bash
python3 {EDIT_DIR}/retranscribe.py {EDIT_DIR}/pass2.mp4 {EDIT_DIR}/transcript_pass3.json
```

### 5b. Check for any remaining doubles

```python
# Auto-detect repeated consecutive words
for i, u in enumerate(utts):
    words = u['transcript'].lower().split()
    for j in range(len(words)-1):
        if words[j] == words[j+1] and words[j] not in ('a','the','to','in','no','not','100'):
            print(f'REPEAT [{i}]: {u["transcript"]}')
```

Fix any remaining issues with targeted cuts.

### 5c. Trim silences > 0.5s

Write `{EDIT_DIR}/pass3_silence.py`:

```python
#!/usr/bin/env python3
import subprocess, re, json, sys

VIDEO = "{edit_dir}/pass2.mp4"
OUT = "{edit_dir}/final_cut.mp4"
SILENCE_MIN = 0.5  # trim any silence > 0.5s
NOISE_FLOOR = -30  # dB

SOURCE_DUR = float(subprocess.run(
    ["ffprobe","-v","quiet","-show_entries","format=duration","-of","csv=p=0", VIDEO],
    capture_output=True, text=True
).stdout.strip())

# Detect silences > 0.5s at -30dB noise floor
cmd = ["ffmpeg","-i",VIDEO,
       "-af",f"silencedetect=noise={NOISE_FLOOR}dB:duration={SILENCE_MIN}",
       "-f","null","/dev/null"]
r = subprocess.run(cmd, capture_output=True, text=True)
ss = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", r.stderr)]
se = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", r.stderr)]
silences = list(zip(ss, se))

# Trim each silence to 0.2s (keep 0.1s at each end for natural breath)
trim_zones = []
for s_start, s_end in silences:
    trim_start = s_start + 0.1
    trim_end = s_end - 0.1
    if trim_end > trim_start:
        trim_zones.append((trim_start, trim_end))

# Build keep segments
keep = [(0, SOURCE_DUR)]
for cs, ce in trim_zones:
    new_keep = []
    for ks, ke in keep:
        if ce <= ks or cs >= ke: new_keep.append((ks, ke))
        elif cs <= ks and ce >= ke: pass
        elif cs > ks and ce < ke: new_keep.extend([(ks, cs), (ce, ke)])
        elif cs <= ks: new_keep.append((ce, ke))
        else: new_keep.append((ks, cs))
    keep = [(s, e) for s, e in new_keep if e - s > 0.03]

total_trimmed = sum(ce - cs for cs, ce in trim_zones)
print(f"Trimmed {len(trim_zones)} silence gaps, {total_trimmed:.1f}s removed")

with open("{edit_dir}/pass3_segments.json", "w") as f:
    json.dump(keep, f)
subprocess.run(["python3", "{edit_dir}/render_cuts.py", VIDEO,
    "{edit_dir}/pass3_segments.json", OUT])
```

**Silence threshold = 0.5s.** Any silence longer than 0.5s gets trimmed. Silences under 0.5s are natural breathing pauses. leave them alone.

Output: `{EDIT_DIR}/final_cut.mp4`

Print: `Pass 3: Trimmed {N} silence gaps ({TOTAL}s removed), final: {DURATION}s`

---

