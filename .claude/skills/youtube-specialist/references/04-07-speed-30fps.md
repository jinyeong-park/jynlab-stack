## Step 5d: Apply speed + force constant 30fps (global, one-time)

**CRITICAL: Speed is applied ONCE here, AFTER all cuts are done.** Never apply speed per-segment during concat. that causes audio/video drift over time.

**CRITICAL: Output MUST be constant 30fps via libx264, NOT hevc_videotoolbox.** Videotoolbox silently ignores the `fps=30` filter on macOS and produces VFR (variable framerate) output. This breaks /yt-assemble downstream, causing the base video to have a mismatched fps (e.g., 27.58fps) which compounds into A/V drift during overlay rendering. V0 final_assembled_v4 had 1.88s drift due to this bug. Use libx264 for reliable constant fps.

```bash
ffmpeg -y -i {EDIT_DIR}/final_cut.mp4 \
  -filter_complex "[0:v]setpts={1/SPEED}*PTS,fps=30[v];[0:a]atempo={SPEED},asetpts=PTS-STARTPTS[a]" \
  -map "[v]" -map "[a]" \
  -r 30 -vsync cfr \
  -c:v libx264 -preset fast -crf 18 \
  -pix_fmt yuv420p \
  -c:a aac -b:a 192k \
  -movflags +faststart \
  {EDIT_DIR}/final_speed.mp4
```

Key flags:
- `fps=30` in filter. resamples video to 30fps after speed change
- `-r 30 -vsync cfr` output. enforces constant 30fps in output
- `libx264 -preset fast -crf 18`. reliable encoder that respects the filter graph
- `-pix_fmt yuv420p`. broad compatibility
- `-movflags +faststart`. fast streaming start for web playback

This processes the entire video as one unit, keeping audio and video perfectly synced at constant 30fps.

**Mandatory verification after render:**
```bash
ffprobe -v quiet -select_streams v:0 -show_entries stream=r_frame_rate,duration -of csv=p=0 {EDIT_DIR}/final_speed.mp4
ffprobe -v quiet -select_streams a:0 -show_entries stream=duration -of csv=p=0 {EDIT_DIR}/final_speed.mp4
```

Check:
- `r_frame_rate == "30/1"` exactly. If not, the render failed the fps check. redo with explicit `-r 30` flag.
- Video duration and audio duration should be within 0.1s of each other. Small diff (< 0.8s) is OK because /yt-assemble will tpad the video to match audio in Step 2 of the overlay render.

Rename: `final_speed.mp4` → `final_cut.mp4` (replace the pre-speed version).

Print: `Speed: {SPEED}x applied globally ({before}s → {after}s), fps: 30/1 constant`

---

