---
name: youtube
description: Your complete YouTube pipeline in one skill. One-time setup, research viral topics, build the Hook/Problem/Solution/Results/Outro outline, write the teleprompter script, cut-edit the talking head footage, and generate the full publish package (title, thumbnail brief, description, pinned comment, community post). 80% of YouTube production from one command.
argument-hint: "[step: 'setup', 'research', 'outline', 'script', 'cut-edit', 'publish', or blank for full pipeline]"
user-invocable: true
---

# /youtube: your complete YouTube pipeline

**Purpose:** One skill runs your entire YouTube production. One-time setup of the local tools, research a viral topic, build an outline in the proven 5-section structure, write a word-for-word teleprompter script, cut-edit your talking head footage, and generate the full publish package. You film for 1 hour. This skill handles the other 90%.

**Required MCP:** YouTube (search, analytics, transcript, publish), Apify (trend research, competitor scraping)

## How this skill works

You can run the full pipeline step by step, or jump to a specific step:

- `/youtube setup`. one-time install of ffmpeg, Python 3.10+, and your Deepgram API key (run once per machine before your first video)
- `/youtube research`. start with topic research
- `/youtube outline`. build the 5-section outline from a topic
- `/youtube script`. write the teleprompter script from an outline
- `/youtube cut-edit`. edit your raw talking head footage
- `/youtube publish`. generate the full publish package

Each step reads the output of the previous step. Run them in order for a new video. The `setup` step is one-time only.

---

## Step 0: One-time local setup (run once per machine)

**Load [references/00-setup.md](references/00-setup.md)** for the full one-time setup workflow.

**What it does:**
1. Detects the student's operating system (macOS, Linux, Windows)
2. Installs `ffmpeg` via the correct package manager (Homebrew on Mac, apt on Linux, manual installer walkthrough on Windows)
3. Verifies or installs Python 3.10 or newer
4. Installs the Python libraries the cut-edit pass needs (`deepgram-sdk`, `pydub`, `numpy`)
5. Walks the student through creating a free [Deepgram](https://console.deepgram.com/signup) account and collects the API key
6. Saves `DEEPGRAM_API_KEY` to `./.env`

**When to run it:** the first time the student wants to make a video. After the first successful run, `/youtube cut-edit` just works and this step is never needed again.

**Your job:** one question at a time, no shell commands visible to the student, no jargon.

---

## Step 1: Research viral topics

**Load [references/01-research.md](references/01-research.md)** for the full research workflow.

**What it does:**
1. Search YouTube for top-performing videos in your niche (last 30-90 days, sorted by views)
2. Search X/Twitter for trending AI topics via Apify
3. Pull transcripts from the top 3-5 videos to extract hook patterns and title structures
4. Identify which topics have high views but low competition (the gap)
5. Present 5-10 topic candidates with view counts, channel sizes, and viral ratios

**Output:** `01_RESEARCH.md` with topic candidates ranked by potential.

**Your job:** Pick one topic from the list.

---

## Step 2: Build the outline

**Load [references/02-outline.md](references/02-outline.md)** for the outline structure and rules.

**What it does:**
1. Read business.md for your niche, voice, enemy, and offer
2. Build a 5-section outline using the proven structure:

```
HOOK (0:00 - 0:15)
  → Result claim or surprising stat. Open 1-2 curiosity loops.

PROBLEM (0:15 - 2:00)  
  → "Tell me if this sounds like you." Paint the viewer's pain.
  → Name the enemy (AI Tourist, Course Collector, Feature Addict, etc.)
  → Loss aversion: what they are losing every day they don't act.

SOLUTION (2:00 - 9:00)
  → Show your invention/build/system on screen.
  → Walk through it section by section.
  → Micro-payoffs every 90 seconds ("think about that").
  → This is 50%+ of the video runtime.

RESULTS (9:00 - 11:00)
  → Your numbers + 2-3 student/client results with names.
  → "Same person. Different system."

OUTRO (11:00 - 11:30)
  → CTA to your lead magnet or landing page.
  → Identity bridge: "where [enemy] becomes [hero identity]."
  → "I built this for the person I used to be."
```

3. Generate 3 title options (Claude Code in first half, specific number, under 58 chars)
4. Generate thumbnail direction (face + 2 text elements + dark background)

**Output:** `02_OUTLINE.md` with the full 5-section outline, 3 titles, thumbnail spec.

**Your job:** Review the outline. Approve or request changes.

---

## Step 3: Write the teleprompter script

**Load [references/03-script.md](references/03-script.md)** for script writing rules.

**What it does:**
1. Read the approved outline from `02_OUTLINE.md`
2. Read business.md for voice and tribal vocabulary
3. Read `.claude/rules/humanizer.md` for banned words
4. Expand each section into word-for-word spoken lines
5. Apply psychology techniques:
   - Open loops in the first 30 seconds
   - Loss aversion framing in Problem
   - "I was that person" confession with every enemy mention
   - Micro-payoffs every 90 seconds in Solution
   - Authority stacking sequence (0:30 result, 2:00 failure story, 5:00 demo, 8:00 student result)
   - Identity-based CTA in Outro

**Output:** `03_SCRIPT.md`. pure teleprompter. Every word is the word you read into the camera.

**Your job:** Read it out loud once. Flag any line that doesn't sound like you. Rewrite those lines.

**Then film.** Talking head. Direct to camera. One take or two. Do not film 10 takes. The cut-edit step handles retakes.

---

## Step 4: Cut-edit your footage

**Load [references/04-cut-edit.md](references/04-cut-edit.md)** for the full editing workflow.

**What it does:**
1. **VFR drift check**: screen recorders (OBS, Zoom, Cap) produce variable framerate that ruins subtitle sync. The skill checks and re-encodes to constant 30fps if needed.
2. **Transcribe**: calls Deepgram API for word-level timestamps.
3. **Pass 1. Retake removal**: uses the script as ground truth. Identifies blocks where you restarted a sentence and cuts them.
4. **Pass 2. Phrase repeat detection**: N-gram analysis catches "so so", "um the um the", repeated phrases. Removes them.
5. **Pass 3. Silence polish**: any silence over 0.5 seconds gets trimmed to 0.2 seconds.
6. **Subtitle generation**: creates .ass subtitle file (single-line, 38-char cards).
7. **Final render**: outputs CFR 30fps mp4 via libx264.

**Output:** `final_cut.mp4` + `transcript_final.json` + `captions.ass`

**Your job:** Watch the cut once. Flag any bad edits. The skill fixes them.

**Requires:** ffmpeg installed, Deepgram API key in .env, Python 3.10+ for the retake detection script.

---

## Step 5: Publish package

**Load [references/05-publish.md](references/05-publish.md)** for the publish workflow.

**What it does:**
1. Read business.md for positioning and CTA links
2. Read the script for content context
3. Generate the full publish package:

```
TITLE: [final title, Claude Code in first half, under 58 chars]

THUMBNAIL BRIEF:
  - Face position, text elements, accent color, dark background
  - 3 alternate concepts for A/B testing

YOUTUBE DESCRIPTION:
  - One-line hook
  - CTA links (lead magnet + main site)
  - Timestamps from the script sections
  - Hashtags (5-7)
  - Tags (15-20 search keywords)

PINNED COMMENT:
  - CTA to lead magnet
  - "Drop a comment if you have questions. I read every one."

YOUTUBE COMMUNITY POST:
  - 4-5 lines. Hook + what the video covers + "link in comments"

UPLOAD SETTINGS:
  - Category, language, end screen placement, card placement
```

4. Optionally upload via YouTube MCP if connected

**Output:** `04_PUBLISH.md` with the complete package ready to copy-paste.

**Your job:** Review titles. Pick the thumbnail concept. Copy-paste description and pinned comment. Publish.

---

## What this skill does NOT handle

The 5-step pipeline covers 80% of production. The other 20% is visual polish that your video editor handles faster than automation for now:

- **B-roll insertion and timeline planning**. picking clips, timing them, placing them.
- **Music and sound mix**. background music, ducking, levels.
- **Motion graphics and animated infographics**. animated text, data diagrams, transitions.
- **Final render with overlays**. combining talking head, B-roll, captions, and music.

**For your first 10 videos, ship clean talking head with captions.** Add visual polish after you have proof the content works. Your energy is better spent on hook + script + distribution than on motion graphics.

---

## Self-check before finishing each step

### After research:
- [ ] 5-10 topic candidates with view counts and viral ratios
- [ ] At least 2 topics with low competition (few videos, high views)
- [ ] Research saved to 01_RESEARCH.md

### After outline:
- [ ] 5 sections present: Hook, Problem, Solution, Results, Outro
- [ ] Enemy named in Problem section
- [ ] Solution section has the invention/build as the core
- [ ] 3 title options generated
- [ ] Outline saved to 02_OUTLINE.md

### After script:
- [ ] Pure teleprompter format (no scene directions in the script)
- [ ] No em dashes
- [ ] No Tier 1/2 banned words
- [ ] Open loops in first 30 seconds
- [ ] Micro-payoffs every 90 seconds in Solution
- [ ] "I was that person" with every enemy mention
- [ ] Script saved to 03_SCRIPT.md

### After cut-edit:
- [ ] VFR drift checked and fixed if needed
- [ ] Retakes removed
- [ ] Phrase repeats removed
- [ ] Silences polished
- [ ] Subtitles generated
- [ ] Final cut rendered at CFR 30fps

### After publish:
- [ ] Title under 58 chars with Claude Code in first half
- [ ] Thumbnail brief with face + 2 text elements
- [ ] Description with timestamps and CTA links
- [ ] Pinned comment with lead magnet link
- [ ] Community post drafted
- [ ] Package saved to 04_PUBLISH.md

## Reference library

| File | When to load |
|---|---|
| [references/00-setup.md](references/00-setup.md) | Step 0. One-time local setup. ffmpeg, Python 3.10+, Deepgram key. Run once per machine before the student's first video. |
| [references/01-research.md](references/01-research.md) | Step 1. Viral topic research workflow. YouTube + X scraping. |
| [references/02-outline.md](references/02-outline.md) | Step 2. The 5-section outline structure. Hook/Problem/Solution/Results/Outro rules. |
| [references/03-script.md](references/03-script.md) | Step 3. Script writing rules. Psychology techniques. Humanizer rules. |
| [references/04-01-multi-source.md](references/04-01-multi-source.md) | Step 4. Handling multiple source files (talking head + screen recording). |
| [references/04-02-transcribe.md](references/04-02-transcribe.md) | Step 4. Deepgram transcription setup and word-level timestamp extraction. |
| [references/04-03-render-cuts.md](references/04-03-render-cuts.md) | Step 4. ffmpeg cut commands and render patterns. |
| [references/04-04-pass1-cut-retakes.md](references/04-04-pass1-cut-retakes.md) | Step 4 Pass 1. Script-faithful retake block removal logic. |
| [references/04-05-pass2-auto-detect.md](references/04-05-pass2-auto-detect.md) | Step 4 Pass 2. N-gram phrase repeat auto-detection and removal. |
| [references/04-06-pass3-silence.md](references/04-06-pass3-silence.md) | Step 4 Pass 3. Silence trimming rules. |
| [references/04-07-speed-30fps.md](references/04-07-speed-30fps.md) | Step 4. Constant framerate enforcement and VFR drift fix. |
| [references/04-08-subtitles.md](references/04-08-subtitles.md) | Step 4. .ass subtitle generation rules (38-char, single-line). |
| [references/04-09-verify-report.md](references/04-09-verify-report.md) | Step 4. Post-edit verification checklist. |
| [references/04-10-critical-rules.md](references/04-10-critical-rules.md) | Step 4. Critical rules from real production bugs (must read). |
| [references/05-publish.md](references/05-publish.md) | Step 5. Publish package. Title, thumbnail, description, comment, community post. |

## Change log

| Date | Changes |
|---|---|
| 2026-04-10 | v1: Unified `/youtube` skill with 5 steps and 14 reference files. Core pipeline: research → outline → script → cut-edit → publish. Visual polish features deferred to a later version. |
| 2026-04-11 | Cleaned dispatcher copy: removed internal skill names from the "what is NOT handled" section so students see capabilities, not legacy skill plumbing. |
| 2026-04-11 | Added Step 0 (`/youtube setup`) to the pipeline. Previously a standalone `/youtube-setup` skill, now folded into this dispatcher as reference 00-setup.md to match the existing 5-step reference pattern. One-time local install of ffmpeg, Python 3.10+, and Deepgram API key via natural-language delegation. |
