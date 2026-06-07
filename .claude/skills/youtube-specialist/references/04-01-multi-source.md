# Multi-source detection and normalization (Step 1.5)

When `FOOTAGE_DIR` has 2+ `.mp4` files (e.g. talking head + screen recording), normalize each to constant 30fps 1920x1080 BEFORE any cuts. Then run Pass 1 on each separately and combine in script zone order.

## Detect

```python
import glob
mp4s = sorted(glob.glob(os.path.join(FOOTAGE_DIR, "*.mp4")))
if not mp4s:
    print(f"ERROR: no .mp4 files found in {FOOTAGE_DIR}")
    sys.exit(1)

MULTI_SOURCE = len(mp4s) >= 2
print(f"Found {len(mp4s)} source file(s): {[os.path.basename(m) for m in mp4s]}")
print(f"Mode: {'MULTI-SOURCE' if MULTI_SOURCE else 'SINGLE-SOURCE'}")
```

If single-source, skip to Step 2 with that one file.

## Identify files

- `V{N} Video*.mp4` or `*_talking*.mp4` → talking head
- `V{N} Screen*.mp4` or `*_screen*.mp4` → screen recording
- Fallback: shorter file (~5-15 min) = talking head, longer file (~20-40 min) = screen

## Normalize each source

Critical: V1 talking head was 23.976fps. Many cameras output non-30fps. Always normalize.

```bash
EDIT="{video_dir}/assets/edit"
mkdir -p "$EDIT"

for src in V1_talking_head.mp4 V1_Screen.mp4; do
  ffmpeg -y -i "assets/talking_head/$src" \
    -vf "fps=30,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2" \
    -r 30 -vsync cfr \
    -c:v libx264 -preset fast -crf 18 \
    -pix_fmt yuv420p \
    -c:a aac -b:a 192k \
    "$EDIT/${src%.mp4}_norm.mp4"
done
```

Save normalized outputs to `{EDIT_DIR}/`, NOT `talking_head/` (read-only).

## After normalization

1. **Run Pass 1 (Steps 2-3) on EACH normalized file separately.** Outputs: `pass1_talking_head.mp4`, `pass1_screen.mp4`.

2. **Combine in script zone order via concat demuxer:**

```python
with open(f"{EDIT_DIR}/concat_list.txt", "w") as f:
    f.write(f"file 'pass1_talking_head.mp4'\n")  # Zone A
    f.write(f"file 'pass1_screen.mp4'\n")         # Zone B
    f.write(f"file 'pass1_talking_head.mp4'\n")   # Zone C. use inpoint/outpoint if needed

subprocess.run([
    "ffmpeg", "-y", "-f", "concat", "-safe", "0",
    "-i", f"{EDIT_DIR}/concat_list.txt",
    "-r", "30", "-vsync", "cfr",
    "-c:v", "libx264", "-preset", "fast", "-crf", "18",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k",
    f"{EDIT_DIR}/combined.mp4"
], check=True)
```

3. **Continue Pass 2 (auto-detect retakes) on `combined.mp4`.**
4. **Pass 3 (silence polish) on Pass 2 output.**
5. **Step 5d (speed + final 30fps) on Pass 3 output.**

## Audio gotcha (V1 lesson)

V1 talking head was stereo (2 channels), V1 screen recording was mono (1 channel). The first concat demuxer attempt **silently dropped the talking head audio for Zone C** because channel mismatch. Result: 180+ seconds of missing audio.

**Fix**: force `-ac 2` on both normalized outputs OR use concat filter (not demuxer) when channel layouts differ:

```bash
ffmpeg -y \
  -i pass1_talking_head.mp4 \
  -i pass1_screen.mp4 \
  -filter_complex "[0:v][0:a][1:v][1:a][0:v][0:a]concat=n=3:v=1:a=1[v][a]" \
  -map "[v]" -map "[a]" \
  -r 30 -vsync cfr \
  -c:v libx264 -preset fast -crf 18 -pix_fmt yuv420p \
  -c:a aac -b:a 192k -ac 2 \
  combined.mp4
```

Verify after combine: audio waveform sample at start/middle/end of each zone. If silence anywhere, channel mismatch is the cause.

## Critical rule

**Do NOT overlay B-roll or infographics on top of the Zone B screen recording in /yt-assemble.** The screen IS the visual. /yt-assemble Rule 9 enforces this downstream. don't undermine it by normalizing the visual distinction away.

---

## V6 lesson: VFR source audio drift (CRITICAL)

**V6 symptom**: Subtitles burned onto final cut were ~6 seconds out of sync by the end of a 22-minute video. Chris reported the same sync problem on every iteration.

**Root cause**: Some source recordings (especially screen recorders like OBS/Riverside/Cap) write VFR (variable frame rate) video with constant-rate audio. The MP4 container reports duration based on video stream PTS, but the actual audio samples extend past that duration. Example: a "52:50" file had 3169.756s video but 3198.131s audio samples. **+28.374s drift**.

When you concat segments from VFR sources using `atrim`/`trim` with filter_complex, the audio samples get included faithfully but video frames get CFR-aligned. Deepgram reads the resulting audio stream and sees the extra samples. returning timestamps that are systematically higher than video wall-clock time. Burning those timestamps onto video = late subtitles.

**Diagnostic**: Before doing anything else, check every source file for A/V drift:

```bash
check_drift() {
  local f="$1"
  local cdur=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$f")
  ffmpeg -y -i "$f" -vn -ar 48000 -ac 2 -c:a pcm_s16le /tmp/check.wav 2>/dev/null
  local wdur=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 /tmp/check.wav)
  local delta=$(python3 -c "print(f'{$wdur - $cdur:+.3f}')")
  printf "%-50s container=%s wav=%s delta=%s\n" "$(basename $f)" "$cdur" "$wdur" "$delta"
  rm -f /tmp/check.wav
}

for src in "$FOOTAGE_DIR"/*.mp4; do check_drift "$src"; done
```

- **delta < 0.1s**: CFR-clean, proceed normally
- **delta > 0.1s**: VFR source, MUST re-encode to CFR before anything else

**Fix (mandatory for VFR sources)**:

```bash
# Re-encode source to CFR 30fps with proper audio resampling.
# The -af "aresample=async=1:first_pts=0" forces audio to track video wall-clock.
ffmpeg -y -i "$VFR_SOURCE" \
  -c:v libx264 -preset medium -crf 18 -r 30 -vsync cfr -pix_fmt yuv420p \
  -c:a aac -b:a 192k -ar 48000 -ac 2 \
  -af "aresample=async=1:first_pts=0" \
  -movflags +faststart \
  "${VFR_SOURCE%.mp4}_cfr.mp4"
```

Verify drift on the _cfr.mp4 output. Should be <0.1s. Then use the _cfr.mp4 as the source for all subsequent cuts/concats.

**Why `-preset medium` not `fast`**: The re-encode is heavy (5-10 min for a 50-min source), but sync accuracy requires proper DCT/bitrate allocation. Don't cheap out here.

**Why `aresample=async=1:first_pts=0`**: Forces audio to start at PTS 0 and stretch/compress to match video timing. Without this, audio drift persists.

**Verification after assembly**: Extract WAV from the final file and compare to video duration. Delta should be < 0.1s. If >1s, something is still VFR in your chain.

**Skipping this step wastes hours**. Chris went through 5 versions of the same video before the root cause was identified. Always check source drift first.

---

## V6 lesson: burning captions without re-encoding audio

When burning subtitles with `ffmpeg -vf "ass=captions.ass"`, do NOT re-encode audio:

```bash
# CORRECT. copy audio, re-encode video only
ffmpeg -y -i final_cut.mp4 \
  -vf "ass=captions.ass" \
  -c:v libx264 -preset fast -crf 18 -pix_fmt yuv420p \
  -c:a copy \
  -movflags +faststart \
  final_with_subs.mp4
```

```bash
# WRONG. re-encoding audio adds AAC priming samples, introduces ~0.04s drift per encode
ffmpeg -y -i final_cut.mp4 \
  -vf "ass=captions.ass,fps=30" \      # don't add fps filter either
  -r 30 -vsync cfr \
  -c:v libx264 -preset fast -crf 18 \
  -c:a aac -b:a 192k \                 # <-- this adds priming samples
  final_with_subs.mp4
```

The `fps=30` filter in `-vf` is also unnecessary when the input is already CFR 30fps. Removing it eliminates another drift source.

---

## V6 lesson: transcribe via clean WAV with duration cap

When re-transcribing for captions, extract audio with `-t ${video_duration}` to prevent Deepgram from seeing AAC padding samples that extend past video end:

```python
dur = float(subprocess.run(
    ["ffprobe","-v","quiet","-show_entries","format=duration","-of","csv=p=0", VIDEO],
    capture_output=True, text=True
).stdout.strip())

subprocess.run([
    "ffmpeg", "-y", "-i", VIDEO,
    "-vn",
    "-t", f"{dur:.3f}",      # force audio to exact video duration
    "-ar", "48000", "-ac", "2",
    "-c:a", "pcm_s16le",     # raw PCM. no encoder priming
    # NO audio filters (no loudnorm, no highpass/lowpass). those alter timing
    audio_path
])
```

Do NOT use `-af "loudnorm"` or other dynamic filters on audio being sent to Deepgram. They shift timing subtly.
