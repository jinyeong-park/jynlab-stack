# 04 · Higgsfield prompts (website hero image + website video loops)

Higgsfield generates the **static hero image** and **short looping video assets** for the website. Nothing else. The VSL is filmed by the operator (see `03-vsl-script.md`). Higgsfield does not touch the VSL.

## What Higgsfield does

Higgsfield is character-consistent AI image and video generation. The operator pastes a prompt, picks a style, gets back an image (or a short looping video clip). Output is photorealistic by default.

The prompts in this reference are paste-ready. Jude fills in the operator-specific bracketed variables before handing them over.

## Where Higgsfield assets live in the funnel

| Asset | Where it appears | Format |
|---|---|---|
| Hero image | `/squeeze` and/or `/` hero section | Static PNG, ~1920x1080 |
| Hero loop (optional) | Same place, replaces static if the operator wants subtle motion | MP4, 4 to 8 sec, no audio, looping |
| Section atmosphere shot (optional) | Backdrop for the "actual problem" or "offer" section | Static PNG |
| Mobile fallback for 3D scene | Used when `prefers-reduced-motion` or low-end device | Static PNG |

That is it. No VSL beats. No Higgsfield in the video.

## Variables Jude fills in

Pull these from `business.md` before writing the prompts. **All five are required.** Do not default. If `business.md` lacks any of them, stop and ask the operator.

- `[aesthetic]`: the operator's visual aesthetic, in 3 to 5 keywords. Examples (any one of these is valid, none is the default):
  - `Caravaggio dark, painterly, single-key chiaroscuro`
  - `clean Scandinavian minimal, soft daylight, matte`
  - `brutalist, hard light, high contrast, concrete textures`
  - `editorial soft, golden hour, shallow depth of field`
  - `90s-film analog, warm grain, slight halation`
  - `clinical, neutral lab, even fluorescent, sharp focus`
  - `cinematic anamorphic, deep blacks, volumetric haze`
- `[archetype]`: what the operator (or their subject) looks like at work. e.g. "solo founder at a laptop", "fitness coach mid-rep", "agency owner at whiteboard", "surgeon in OR scrubs"
- `[setting]`: where the operator works. e.g. "Chilliwack home office at dawn", "open studio with rubber flooring", "minimalist lab with white walls", "warehouse loft with concrete floor"
- `[primary object]`: the operator's main work-tool object. e.g. "open terminal on a laptop", "kettlebell on rubber floor", "stack of contracts on a desk", "stethoscope on white tile"
- `[accent color]`: the operator's brand accent, hex required. Pulled from `business.md`.

## Hero image (3 framing options)

Pick the FRAMING that fits the operator's offer (character / workspace / environment), then inject the operator's `[aesthetic]` keywords. The framing is structural; the aesthetic is brand.

### Option A · Character framing

Best when the operator IS the brand (solo founder, coach, consultant). Faces convert.

```
Portrait of a [archetype], [aesthetic], 35mm lens, photorealistic,
[accent color] subtle accent in the frame (vignette, reflection, or
highlight as the aesthetic allows), no logos, no text, no watermarks,
4k resolution, sharp focus on eyes
```

### Option B · Workspace framing

Best for craft-led brands (developer, writer, designer, maker). Object intimacy.

```
Overhead shot of [primary object] on the surface that fits [setting],
[aesthetic], 35mm lens, photorealistic, [accent color] subtle accent
in the frame, no logos, no text, no watermarks, 4k resolution, ambient
depth of field
```

### Option C · Environment framing

Best when the SETTING is the proof (gym, studio, agency, retail, lab).

```
Wide environmental shot of [setting], [aesthetic], 35mm lens,
photorealistic, [accent color] subtle accent in the frame, no logos,
no text, no watermarks, 4k resolution
```

### Worked example (one operator, "Caravaggio dark" aesthetic, only ONE example)

Aesthetic input: `Caravaggio dark, painterly, single-key chiaroscuro`
Archetype: `solo founder at a laptop`
Accent: `#DB011C`

Renders as Option A:

```
Portrait of a solo founder at a laptop, Caravaggio dark, painterly,
single-key chiaroscuro, 35mm lens, photorealistic, #DB011C subtle
accent in the frame (vignette, reflection, or highlight as the
aesthetic allows), no logos, no text, no watermarks, 4k resolution,
sharp focus on eyes
```

A different operator with `clean Scandinavian minimal, soft daylight, matte` aesthetic + `warm ochre #CB8E2E` accent on the same Option A framing produces an entirely different hero image. Same template, different brand.

## Hero loop video (optional)

Use only if the operator wants subtle motion in the hero. Short loops, no audio.

### Loop A · Slow push-in (matches Option A above)

```
Source frame: [hero image option A render]
Motion: 6-second slow push-in on the operator's face, no camera shake,
ambient breathing motion only, eyes hold direct, depth-of-field blur on
background remains constant. Loop seamlessly from end frame back to start frame.
```

### Loop B · Workspace drift (matches Option B above)

```
Source frame: [hero image option B render]
Motion: 8-second slow drift across the desk left to right, paper or surface
texture catches subtle light shift, shallow depth of field, no other motion.
Loop seamlessly.
```

### Loop C · Environmental light shift (matches Option C above)

```
Source frame: [hero image option C render]
Motion: 8-second slow rack focus from foreground to background detail,
ambient light intensifies subtly across the duration, no camera move beyond
focus pull. Loop seamlessly.
```

## Section atmosphere shots (optional, only when needed)

For the "actual problem" or "offer" section if the operator wants visual depth there.

### Loop graveyard atmosphere (for "actual problem" section)

```
Image:
Overhead shot of a desk with stacks of unopened books, half-finished
notebooks scattered, course completion certificates printed and crumpled,
half-empty coffee cup, hard side lighting, painterly Caravaggio shadow,
photorealistic, 35mm lens, no logos, no readable text, 4k resolution
```

### Roadmap focus shot (for "offer / commitment" section)

```
Image:
Tablet on dark wooden surface showing a roadmap timeline UI with numbered
tiles in weekly clusters, glowing [accent color] accent lines, dark UI,
painterly bokeh background, single overhead pendant light, photorealistic,
35mm lens, sharp focus on the tablet, no logos
```

## Universal prompt rules

- **Always include "no logos, no text, no watermarks".** Higgsfield sometimes hallucinates fake brand text.
- **Always specify the lens.** "35mm lens" reads as photographic. Without it the model defaults to amateur compositions.
- **Always specify the color grade direction.** "dark muted color grade with subtle [accent color] vignette" gives the operator's brand a thread through every image.
- **Always specify "no readable text" if text appears in frame.** Otherwise Higgsfield fills with gibberish that ruins the shot.
- **Always cap motion duration on loops.** 4 to 10 seconds. Longer loops cost more credits and rarely improve.
- **Always loop seamlessly.** "Loop seamlessly from end frame back to start frame" in the video prompt.

## Style consistency

To make every Higgsfield asset on the website feel like the same brand, hold these constant across every render:

1. **Same lens.** Pick once (e.g. 35mm), use everywhere unless a shot demands different focal length.
2. **Same `[aesthetic]` keywords.** Whatever the operator's `business.md` specifies . Caravaggio dark / Scandinavian minimal / brutalist / editorial / 90s analog / clinical / cinematic, paste the SAME keywords into every prompt.
3. **Same accent color.** The operator's brand hex appears as a subtle accent in every shot.
4. **Same negative-space rule.** If the aesthetic is dark, every shot is dark. If bright, every shot is bright. Do not mix.
5. **Same color grade direction.** Pull from the aesthetic. Do not vary across shots.

## What Jude hands the operator

Drop a single Markdown file at the project root or in `prompts/higgsfield-prompts.md`:

```
# Higgsfield prompts for [operator's brand name]

## Hero image (pick one)
[Option A, B, or C with operator variables filled in]

## Hero loop (optional, if motion is wanted)
[Loop A, B, or C matching the chosen hero image option]

## Section atmosphere shots (optional)
[Graveyard, roadmap, etc., only the ones the operator wants]

## How to render

1. Open Higgsfield image-gen
2. Paste the prompt
3. Pick "photorealistic" style
4. Generate 4 variants per prompt
5. Pick the strongest, download the PNG
6. Drop into /public/images/ on this project

For loops:
7. Switch to Higgsfield video-gen
8. Upload the chosen image as source frame
9. Paste the motion prompt
10. Set duration (4 to 10 seconds)
11. Generate, download MP4
12. Drop into /public/videos/ on this project
```

## Common mistakes

**The hero image looks generic.** Almost always means the prompt did not specify lens, lighting, and color grade. Re-render with all three.

**The hero loop drifts off-loop.** Higgsfield clips longer than 10 seconds drift into hallucination. Cut to 6 to 8 seconds and add "loop seamlessly from end frame back to start frame".

**Faces look uncanny.** Caravaggio half-lit composition usually fixes this. If still uncanny, try "painterly oil-paint texture" weight up or shift to Option B (workspace shot, no face).

**Text appears in frame and looks garbled.** Add "no logos, no readable text, no watermarks" to every prompt.

**Brand color does not appear.** "[accent color] subtle vignette in corners" usually fixes it. If still missing, add "[accent color] reflection on glass surfaces" or "[accent color] pixel highlights".

## Re-render budget

The operator should expect to re-render 30 to 50 percent of the assets to get keepers. Budget Higgsfield credits accordingly. The hero image is the single most important shot. Spend more renders to get it right.

## What Higgsfield does NOT do

- **VSL talking-head footage.** The operator films themselves. See `03-vsl-script.md`.
- **VSL B-roll.** The operator captures real screen recordings, real desktop scrolls, real workflow. No AI-generated VSL content.
- **Logos or wordmarks.** Use a vector tool (Figma, Affinity, Illustrator) for logos. AI tools hallucinate them.
- **Avatars or AI presenters.** Faces in the VSL must be human.
- **Voiceover.** The operator's voice. AI voiceover reads as fake.
