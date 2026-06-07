# Transcribe footage with Deepgram (Step 2)

Transcribes original footage to JSON via Deepgram Nova-3. Outputs `transcript_original.json` with utterances and word-level timestamps.

## Substitute these template variables before writing the script

- `{footage_path}` → absolute path from Step 1
- `{edit_dir}` → absolute path from Step 1
- `{api_key}` → DEEPGRAM_API_KEY (loaded from .env or environment)
- `{source_duration}` → float from ffprobe result

Use Python f-strings or `.replace()` to do the substitution when writing the file. Never save the raw template to disk.

## transcribe.py (one-shot for original footage)

```python
#!/usr/bin/env python3
import subprocess, requests, json, os, sys

FOOTAGE = "{footage_path}"
OUT_DIR = "{edit_dir}"
API_KEY = os.environ.get("DEEPGRAM_API_KEY", "{api_key}")
SOURCE_DURATION = {source_duration}

audio_path = os.path.join(OUT_DIR, "audio.wav")
print("Extracting audio...")
r = subprocess.run([
    "ffmpeg", "-y", "-i", FOOTAGE, "-t", str(SOURCE_DURATION),
    "-vn", "-ar", "16000", "-ac", "1",
    "-af", "highpass=f=200,lowpass=f=3000,afftdn=nf=-25,loudnorm",
    audio_path
], capture_output=True, text=True)
if r.returncode != 0:
    print("Error:", r.stderr[-500:]); sys.exit(1)

print("Transcribing with Deepgram Nova-3...")
with open(audio_path, "rb") as f:
    audio = f.read()

resp = requests.post(
    "https://api.deepgram.com/v1/listen",
    headers={"Authorization": f"Token {API_KEY}", "Content-Type": "audio/wav"},
    params={
        "model": "nova-3", "language": "en", "smart_format": "true",
        "punctuate": "true", "utterances": "true",
        "words": "true", "filler_words": "true"
    },
    data=audio, timeout=600
)
if resp.status_code != 200:
    print(f"Deepgram error {resp.status_code}:", resp.text[:500]); sys.exit(1)

dg = resp.json()
out = os.path.join(OUT_DIR, "transcript_original.json")
with open(out, "w") as f:
    json.dump(dg, f, indent=2)

utts = dg["results"]["utterances"]
if len(utts) == 0:
    print("ERROR: Deepgram returned 0 utterances. Check audio quality."); sys.exit(1)
print(f"✓ {len(utts)} utterances → {out}")
```

## retranscribe.py (reusable for passes 2-3)

```python
#!/usr/bin/env python3
"""Re-transcribe a cut video. Usage: retranscribe.py video.mp4 out.json"""
import subprocess, requests, json, os, sys

VIDEO = sys.argv[1]
OUT_JSON = sys.argv[2]
API_KEY = os.environ.get("DEEPGRAM_API_KEY", "{api_key}")

dur = subprocess.run(
    ["ffprobe","-v","quiet","-show_entries","format=duration","-of","csv=p=0", VIDEO],
    capture_output=True, text=True
).stdout.strip()
print(f"Video: {float(dur):.1f}s")

audio_path = OUT_JSON.replace('.json', '.wav')
print("Extracting audio...")
r = subprocess.run([
    "ffmpeg", "-y", "-i", VIDEO,
    "-vn", "-ar", "16000", "-ac", "1",
    "-af", "highpass=f=200,lowpass=f=3000,afftdn=nf=-25,loudnorm",
    audio_path
], capture_output=True, text=True)
if r.returncode != 0:
    print("Error:", r.stderr[-500:]); sys.exit(1)

print("Transcribing...")
with open(audio_path, "rb") as f:
    audio = f.read()

resp = requests.post(
    "https://api.deepgram.com/v1/listen",
    headers={"Authorization": f"Token {API_KEY}", "Content-Type": "audio/wav"},
    params={
        "model": "nova-3", "language": "en", "smart_format": "true",
        "punctuate": "true", "utterances": "true",
        "words": "true", "filler_words": "true"
    },
    data=audio, timeout=600
)
if resp.status_code != 200:
    print(f"Error {resp.status_code}:", resp.text[:500]); sys.exit(1)

dg = resp.json()
with open(OUT_JSON, "w") as f:
    json.dump(dg, f, indent=2)

utts = dg["results"]["utterances"]
if len(utts) == 0:
    print("ERROR: 0 utterances. Check audio."); sys.exit(1)
for i, u in enumerate(utts):
    print(f"[{i}] {u['start']:.1f}-{u['end']:.1f}s: {u['transcript']}")
print(f"\n✓ {len(utts)} utterances → {OUT_JSON}")
```

## Verification gate

After running, verify:
- `transcript_original.json` exists and has `results.utterances` with > 0 entries
- Total transcript text > 50 characters
- If empty: STOP. Check audio quality, Deepgram API key, video has audio track

## Audio preprocessing notes

The `-af "highpass=f=200,lowpass=f=3000,afftdn=nf=-25,loudnorm"` chain:
- highpass at 200 Hz removes low rumble (mic stand, AC)
- lowpass at 3000 Hz removes high hiss
- afftdn FFT-based denoise at -25 noise floor
- loudnorm EBU R128 normalization

This dramatically improves Deepgram accuracy on noisy mic recordings.
