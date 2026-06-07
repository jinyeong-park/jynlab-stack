# render_cuts.py. render keep-segments at native speed (1.0x)

Reusable Python script that renders a list of `[start, end]` keep-ranges into a cut video. Used by all 3 passes.

## CRITICAL: libx264 only

**Do NOT use `hevc_videotoolbox` for intermediate renders.** Videotoolbox on macOS silently ignores fps filters and produces VFR (variable framerate) output. This propagates VFR through pass1/pass2/pass3 and forces Step 5d to "fix" it later, introducing drift.

V0 final_assembled_v4 had **1.88s A/V drift** because of this bug. V5 fixed it with libx264. Always libx264 with explicit `-r 30 -vsync cfr`.

## Speed = 1.0x always at this stage

render_cuts.py always renders at 1.0x (native speed). Speed (1.15x or whatever) is applied as ONE global step in Step 5d AFTER all 3 passes. This prevents per-segment audio drift.

## Template

```python
#!/usr/bin/env python3
"""Render keep-segments into a cut video at NATIVE SPEED.
Usage: python3 render_cuts.py input.mp4 segments.json output.mp4
segments.json = list of [start, end] pairs to KEEP.
Speed is NOT applied here. do it as a separate final step.
"""
import json, subprocess, sys, os, tempfile

VIDEO = sys.argv[1]
SEGMENTS = sys.argv[2]
OUTPUT = sys.argv[3]

with open(SEGMENTS) as f:
    keep = json.load(f)

total = sum(e - s for s, e in keep)
print(f"Rendering {len(keep)} segments, {total:.1f}s at native speed")

n = len(keep)
fp = []
for i, (s, e) in enumerate(keep):
    fp.append(f"[0:v]trim=start={s:.4f}:end={e:.4f},setpts=PTS-STARTPTS[v{i}];")
    fp.append(f"[0:a]atrim=start={s:.4f}:end={e:.4f},asetpts=PTS-STARTPTS[a{i}];")
fp.append("".join(f"[v{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=0[vout];")
fp.append("".join(f"[a{i}]" for i in range(n)) + f"concat=n={n}:v=0:a=1[aout]")

ff = tempfile.mktemp(suffix='.txt')
with open(ff, "w") as f:
    f.write("\n".join(fp))

# CRITICAL: libx264 only. NEVER hevc_videotoolbox. -r 30 -vsync cfr forces CFR.
r = subprocess.run([
    "ffmpeg", "-y", "-i", VIDEO, "-filter_complex_script", ff,
    "-map", "[vout]", "-map", "[aout]",
    "-r", "30", "-vsync", "cfr",
    "-c:v", "libx264", "-preset", "fast", "-crf", "18",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", OUTPUT
], capture_output=True, text=True)
if r.returncode != 0:
    print("ERROR:", r.stderr[-2000:]); sys.exit(1)

dur = subprocess.run(
    ["ffprobe", "-v", "quiet", "-show_entries", "format=duration", "-of", "csv=p=0", OUTPUT],
    capture_output=True, text=True
).stdout.strip()
os.remove(ff)
print(f"✓ {OUTPUT} ({float(dur):.1f}s)")
```

## Why filter_complex_script vs inline

ffmpeg has a command-line length limit. For videos with 100+ keep segments, the inline filter graph exceeds it. Writing the filter graph to a temp file and using `-filter_complex_script` avoids this.

## Verification after render

```bash
ffprobe -v quiet -select_streams v:0 -show_entries stream=r_frame_rate,duration -of csv=p=0 output.mp4
# Should show: 30/1,{duration}
```

If `r_frame_rate` is anything other than `30/1`, the render produced VFR. Re-encode with explicit `-r 30 -fps_mode cfr` flags.
