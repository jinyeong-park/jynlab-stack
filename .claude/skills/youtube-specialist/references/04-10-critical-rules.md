## Critical rules (from production experience)

1. **Script-faithful**: the speaker follows the script 100%. Keep everything that matches. Only cut clear retakes.
2. **No micro-cutting**: NEVER cut at breaths, short pauses, or within sentences. Cut whole retake BLOCKS.
3. **KEEP ranges, not CUT zones**: Define what to KEEP from the original, not what to cut. Map each script line to its best take. This is more accurate.
4. **Word-level precision**: For within-utterance doubles (e.g., "They shipped it six. They shipped it 74%"), use word-level timestamps from `dg["results"]["channels"][0]["alternatives"][0]["words"]` to cut at exact word boundaries.
5. **2x consecutive CLEAN before subtitles**: Re-transcribe from the video file. Check for repeats. If clean, re-transcribe AGAIN. Only proceed to subtitles after 2 consecutive clean transcriptions. Never skip this.
6. **After ANY cut, old transcripts are INVALID**: Timestamps shift after every cut. NEVER reuse a transcript from a previous version of the video for subtitles. Always re-transcribe the CURRENT video file. This is the #1 cause of subtitle desync.
7. **Don't touch originals**: `talking_head/` is read-only. All output to `edit/`.
8. **Silence threshold = 0.5s**: Trim any silence > 0.5s down to ~0.2s (0.1s kept at each end). Silences under 0.5s are natural breathing pauses. leave them. Longer dead air kills pacing.
9. **Speed applied globally ONCE**: All cuts render at native speed (1.0x). Speed (e.g., 1.15x) is applied as ONE global step after ALL cuts, before subtitles. Never per-segment.
10. **One-shot build from original**: Do all cuts in ONE pass from the original footage using KEEP ranges. Don't cut → re-cut → re-cut iteratively on the output. Each re-encoding degrades sync. If issues found after verification, update the KEEP ranges and rebuild from original.
11. **Sentence-aware subtitles**: Each card is a complete phrase. Never split mid-sentence.
12. **자막 스펠링 더블체크 필수**: 자막 빌드 후 반드시 스크립트(03_SCRIPT.md)와 대조. Deepgram 오인식(ChatGPT→chatgpt, Kooky→cookie, Chilliwack→Chiliwa 등)은 물론이고 모든 고유명사, 숫자, 스킬명(/find-niche 등) 스펠링 확인. 스크립트에 없는 추가 발언은 OK, 스펠링 틀리는 건 NOT OK.
12. **B-roll uses overlay, not concat**: B-roll clips overlay ON TOP of the talking head using ffmpeg `overlay` filter with `enable='between(t,start,end)'`. Audio stays from talking head via `-map 0:a -c:a copy`. Never concat B-roll segments (causes audio drift).
13. **B-roll minimum 3 seconds**: No rapid 1-2s cuts. Each B-roll clip must stay at least 3 seconds so the viewer can understand what they're seeing. B-roll must contextually match what's being said.
14. **Auto-detect retakes (never manual-only)**: Use `auto_detect_retakes.py` from Step 4b. It walks N-grams 5→1 (Pass A), catches prefix retakes (first N-1 words match, last differs. "what do you" → "what do your"), runs single-word stutter detection (Pass B), and runs sentence-restart detection (Pass C). Loop: re-transcribe → detect → cut until 0 retakes remain. Manual transcript review alone WILL miss retakes. always run the detector.

14a. **Last-take rule (sentence restarts)**: The speaker restarts at SENTENCE boundaries. when a sentence goes wrong partway through, they stop and start that sentence over from the beginning. ALWAYS keep the LAST attempt and cut everything before it. Pass C of the auto-detector handles this: when two adjacent sentences begin with the same first 2-3 words and the gap between them is < 2.5s, the first sentence is cut entirely. Do NOT skip Pass C. the older sentence-boundary protection in Pass A/B was the reason sentence-level retakes were being left in.

15. **Multi-word name protection (CRITICAL)**: Never cut inside "Claude Code", "/find-niche", "Model Context", "Liam Ottley", "Nate Hirk", "Google Antigravity", "Agent Founders", "Outreach Engine", "Skill Eval", "Mission Control", etc. The auto-detector's `PROTECTED_PAIRS` list handles this. keep it updated with new brand/skill names. Check every cut zone against the list before applying. One bad cut turns "Claude Code" into "Clothe". unrecoverable without going back to source.

16. **Single-line subtitles only**: MAX 38 characters per card, hard limit. ASS file must include `WrapStyle: 2` in the header. Never let subtitles wrap to 2 rows. If a sentence is too long, split into multiple cards. Verify every card against the 38-char limit before burning.
17. **build_subs.py takes transcript file as CLI argument**: `python3 build_subs.py {transcript}.json`. NEVER hardcode the transcript path. This prevents using the wrong transcript for a different video.

18. **Subtitle spelling verification gate**: After building subtitles, grep the .srt file for known Deepgram mishears (cloth, chatty, Chili, scrapping, 1,414, etc.). Fix ALL before burning. Use `\b` word boundaries in regex fixes. never substring match (`"clo" → "Claude"` would turn "close" into "Claudese").

19. **Multi-source videos**: When a video has both talking head and screen recording (two source files), transcribe and cut each separately through Pass 1. Then combine in script zone order (Zone A talking head → Zone B screen → Zone C talking head) via ffmpeg concat into `combined.mp4`. Run Pass 2 (auto-detect retakes) on the combined file. Run Pass 3 (silence polish) on the output of Pass 2.

20. **Final output MUST be constant 30fps via libx264**: Never use `hevc_videotoolbox` for the final `final_cut.mp4` render. Videotoolbox silently ignores the `fps=30` filter on macOS and produces VFR output, which breaks /yt-assemble downstream (causes A/V drift during overlay rendering). V0 final_assembled_v4 had 1.88s drift because of this. Always use `libx264 -preset fast -crf 18` with output flags `-r 30 -vsync cfr -pix_fmt yuv420p` for the final `final_cut.mp4`. Verify after render: `ffprobe -select_streams v:0 -show_entries stream=r_frame_rate` must return `30/1` exactly.

21. **V/A stream duration can differ by up to 0.8s**: Even after correct 30fps encode, the video stream and audio stream in `final_cut.mp4` may differ by a small amount (e.g., 863.8s vs 864.6s). This is fine. /yt-assemble handles it via `tpad=stop_mode=clone:stop_duration={pad}` which clones the last video frame to match audio duration. Just verify the diff is < 1s.

**Recovery when V/A diff > 1s after Step 5d render:**
1. Check source file: `ffprobe -v quiet -select_streams v:0 -show_entries stream=r_frame_rate,nb_frames,duration -of csv=p=0 final_cut.mp4`
2. If `nb_frames / 30 != duration`, the render didn't produce CFR despite the flags. Re-encode with explicit `-r 30 -fps_mode cfr` (modern ffmpeg) or `-vsync cfr` (older).
3. If source has dropped frames (nb_frames < expected), use `fps=30:round=near` filter instead of just `fps=30`.
4. Last resort: manually pad video with `tpad=stop_mode=clone:stop_duration={diff}` to match audio duration.
5. If drift persists, check for corrupt source: `ffmpeg -v error -i final_cut.mp4 -f null -` (prints nothing if clean, errors if corrupt).

---

