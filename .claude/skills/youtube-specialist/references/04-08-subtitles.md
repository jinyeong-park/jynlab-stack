## Step 6: Sentence-aware subtitles

### 6a. Re-transcribe final cut

```bash
python3 {EDIT_DIR}/retranscribe.py {EDIT_DIR}/final_cut.mp4 {EDIT_DIR}/transcript_final.json
```

### 6b. Build subtitle cards (SINGLE LINE ONLY)

**CRITICAL: Subtitles are SINGLE LINE ONLY. Never wrap to 2 rows.** If a card would exceed the max char limit, split it into multiple cards. never let ASS auto-wrap.

Use WORD-LEVEL data with `punctuated_word` from Deepgram to build cards. Break rules:

1. **MAX 38 characters per card** (hard limit, enforces single line)
2. **Break at sentence boundaries** (. ? !). NEVER mid-sentence when possible
3. **Break at strong commas** if card approaches the 38-char limit
4. **Break at natural pauses** if sentence is too long for one card
5. **Merge cards shorter than 0.5s** with adjacent card
6. **ASS file uses `WrapStyle: 2`** (no automatic wrapping) with `MarginL=80, MarginR=80`
7. **Verify every card**: after building, check that no card exceeds 38 chars. Fail loudly if any does.

**BAD card breaks (NEVER DO THIS):**
```
"do. But first, let me tell you what I wouldn't do. I"   ← crosses 3 sentences
"Customer the world split in two people being replaced"   ← crosses 2 sentences
"If I had to start over from zero today here's what"     ← > 38 chars, would wrap
```

**GOOD card breaks:**
```
"If I had to start over from zero,"        ← 32 chars
"here's exactly what I'd do."               ← 27 chars
"But first, let me tell you"                ← 26 chars
"what I wouldn't do."                       ← 19 chars
```

### 6c. Correct text against script

Fix ALL Deepgram mishears by comparing against the script:

**Common mishears (fix these every time):**
- "clothecode"/"closed code"/"cloud code"/"Clotheco" → "Claude Code"
- "comment" (typing context) → "command"
- "ASO founders" → "AI solo founders"
- "cookie" → "Kooky", "rifa" → "Refa", "Chiliwa"/"Chilliwok" → "Chilliwack"
- "scrapping" → "scripting", "scraps" → "scrapes"
- "antigravity" → "Antigravity"
- "epify" → "Apify", "bursal" → "Vercel"
- "$9.97" → "$997", "1,414,000" → "14,000"

**Capitalization (fix ALL):**
- `I` standalone. ALWAYS capitalize
- `AI`, `ROI`, `MCP`, `API`, `YouTube`. always uppercase
- Product names: Claude Code, Apify, Stripe, Perplexity, Instantly, Vercel, Cursor
- Person names: Daniel, Kooky, Maria, Steven, Refa, Sandy, Hormozi
- Framework names: Value Equation, AI Learning Addiction, Dopamine Ladder
- Skill names: /find-niche, /build-offer, /build-pipeline, /yt-cut-edit

**Punctuation:** periods at sentence ends, commas for pauses, question marks.

**Numbers:** cross-check ALL dollar amounts, percentages, counts against script.

**General mishear pass:** After applying the known fixes above, do a FINAL pass comparing each subtitle card against the nearest script line. Fix ANY remaining word that doesn't match what the script says. The fixed list above covers common Agent Founders vocabulary, but every video will have unique mishears. Compare against script, not just the list.

### 6d. Generate ASS and SRT files

**ASS header MUST include `WrapStyle: 2`** (no automatic wrapping). Without this, long lines will wrap to 2 rows regardless of the 38-char limit.

```
[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Inter Medium,62,&H00FFFFFF,&H000000FF,&H19000000,&H19000000,0,0,0,0,100,100,0.5,0,3,10,0,2,80,80,80,1
```

Key parameters:
- `WrapStyle: 2`. **DISABLE auto-wrapping. Forces single line.**
- Font: Inter Medium, 62px
- BorderStyle=3, Outline=10 (wide pill padding left/right)
- MarginL=80, MarginR=80 (screen edge padding)
- MarginV=80 (bottom margin)
- BackColour=&H19000000 (semi-transparent black)

Write `{EDIT_DIR}/captions.ass` and `{EDIT_DIR}/captions.srt`.

**Verification after writing:** Check every card in captions.srt is ≤ 38 chars. If any exceed, split and re-write before burning.

### 6e. Burn subtitles (libx264, constant 30fps)

**Use libx264, NOT hevc_videotoolbox.** Same reason as Step 5d. videotoolbox breaks constant fps.

```bash
ffmpeg -y -i {EDIT_DIR}/final_cut.mp4 \
  -vf "ass='{EDIT_DIR}/captions.ass',fps=30" \
  -r 30 -vsync cfr \
  -c:v libx264 -preset fast -crf 18 \
  -pix_fmt yuv420p \
  -c:a aac -b:a 192k \
  -movflags +faststart \
  {EDIT_DIR}/final_with_subs.mp4
```

This produces the SUBBED version. For /yt-assemble to work correctly, keep `final_cut.mp4` (no subs) as the main deliverable. /yt-assemble will burn subtitles at the end of its own overlay chain using the captions.ass file.

---

