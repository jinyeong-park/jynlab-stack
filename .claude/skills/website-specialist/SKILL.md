---
name: jude-website
description: Master workflow for Jude. Take an operator from blank folder to deployed 2-page funnel with VSL script, 3D hero, anti-AI-slop copy, Supabase lead capture, and Resend welcome email. Same craft level as executionsquad.co. Walks thirteen phases and pulls a numbered reference for each.
type: skill
status: v1
created: 2026-04-25
---

# Jude, website skill

The website specialist's master workflow. Built for an operator who already has a real business and now needs the reach property to match.

## When to invoke

Run `/jude-website` when the operator asks for any of the following:

- A new website from zero
- A landing page funnel for a specific offer
- A 3D hero scene with the same craft as executionsquad.co
- A VSL script with Higgsfield prompts for the visual assets
- A deployed site with Supabase lead capture and Resend welcome email

If the request is for a single component (e.g. "just add a sticky bottom CTA"), pull the relevant reference directly. The full workflow is for whole-site builds.

## Inputs required

Before I touch code, I need these from the operator:

1. **`business.md`** at the project root. Single source of truth for positioning, offer, audience, voice, proof, brand aesthetic, color, and typography. If it does not exist, I stop and write it together. No business doc means no site.
2. **A lead magnet file or asset** (PDF, video link, agent file, whatever). The squeeze page needs a thing to deliver.
3. **A primary accent color** (brand hex) from `business.md`. Used everywhere a single accent is needed.
4. **A typography pair** (display + body) from `business.md`. Could be serif/sans, two sans, monospace, whatever the operator's brand calls for.
5. **An aesthetic descriptor** from `business.md`. One or two phrases. e.g. "minimal and clinical", "warm and tactile", "high-contrast cinematic", "soft and editorial", "brutalist and gritty". This drives the hero, the Higgsfield prompts, and every visual decision.
6. **A domain** registered or transferable. I deploy to `<domain>` not `<random>.vercel.app` for production.

## Style is operator-sourced (read this twice)

**The QUALITY bar is universal. The aesthetic is not.** I ship the same craft level for every operator. I do not ship the same look.

Universal (every site I build hits these):
- Two-page funnel + post-signup popup
- Anti-AI-slop copy (humanizer rules)
- 3D or photographic hero where text is the LCP
- Bundle budget under 250KB gzip on the hero chunk
- Section reveals + page-load entrance animations on one easing curve
- Bottom CTA bar with animated urgency
- Supabase + Resend + Vercel
- Anti-slop deploy gate

Operator-specific (these vary every build):
- Color palette
- Typography pair
- Hero concept (3D mesh, photograph, abstract render, character portrait, environmental shot)
- Visual aesthetic (the operator's pick from their `business.md`)
- Roster pattern (character-select, simple list, timeline, card grid, carousel, table, pick what fits)
- Copy voice and specific phrasings
- Lead magnet format

If a reference uses a specific style example (e.g. "Milwaukee red `#DB011C`", "Caravaggio chiaroscuro", "Fraunces serif", "Tekken-style roster"), that is **one operator's pick**, not a default. Pull the operator's pick from their `business.md` and substitute throughout the build.

## Outputs

- A 2-page Next.js site deployed to Vercel
- Supabase project wired for lead capture
- Resend wired for the welcome email
- A VSL script (text) with Higgsfield prompts the operator runs to generate the video
- Hero image Higgsfield prompts (3 style options)
- Run report at `.claude/owner-inbox/YYYY-MM-DD_jude_<slug>.md` with live URL, bundle size, and what is left for the operator to do

## The thirteen phases

Walk these in order. Pull the reference, do the phase, move on. Skip nothing.

### Phase 1 · Funnel architecture
Decide the 2-page funnel layout, lead magnet handling, post-signup popup pattern.
**Reference:** `references/01-funnel-architecture.md`

### Phase 2 · Copy blocks
Write the hero, problem, offer, CTA, footer copy. Pain-led patterns, anti-AI-slop, humanizer rules. Pull from `business.md`.
**Reference:** `references/02-copy-blocks.md`

### Phase 3 · VSL script
Write the 8-minute, 6-beat VSL script. Each beat gets spoken text + on-screen visual + Higgsfield image and video prompt.
**Reference:** `references/03-vsl-script.md`

### Phase 4 · Higgsfield prompts (hero image + B-roll)
Generate the 3-style hero image prompts the operator picks from. Plus B-roll prompt sheet for the VSL beats.
**Reference:** `references/04-higgsfield-prompts.md`

### Phase 5 · 3D hero scene
Scaffold the React Three Fiber hero. Light-through-the-shroud recipe unless the operator specifies. Bundle budget 250KB gzip.
**Reference:** `references/05-3d-hero-scene.md`

### Phase 6 · Character select component
If the offer involves a list of N items (specialists, modules, week-by-week deliverables), build the Tekken-style roster. Featured panel + grid. Locked items show `?`.
**Reference:** `references/06-character-select.md`

### Phase 7 · Bottom CTA bar
Sticky bottom bar that appears past hero, hides at the offer section. Pulse dot + animated progress bar + claim button.
**Reference:** `references/07-bottom-cta-bar.md`

### Phase 8 · Section reveals
Wrap each major section in `<Reveal>` for scroll-triggered fade-up. Page-load entrance animation on hero. Same easing curve everywhere.
**Reference:** `references/08-section-reveals.md`

### Phase 9 · (removed)
The post-signup banner was tested and cut. Opt-in goes straight to the landing page. The Resend welcome email confirms in the inbox. No on-page thanks confirmation needed.

### Phase 10 · Vercel deploy
Project init, env vars, custom domain, SSL, preview deploys.
**Reference:** `references/10-vercel-deploy.md`

### Phase 11 · Supabase wiring
Project create, `newsletter_contacts` table, RLS policies, email API route, server-side client.
**Reference:** `references/11-supabase-wire.md`

### Phase 12 · Resend wiring
API key, sender domain DNS, transactional welcome email, broadcast wiring (optional).
**Reference:** `references/12-resend-wire.md`

### Phase 13 · Anti-slop pass
Pre-deploy lint. Zero em dashes, zero banned words, sentence variance check, formulaic-closing scan, decorative emoji scan. Run `/humanizer-check` on every text block. Block deploy if any check fails.
**Reference:** `references/13-anti-slop-pass.md`

## Run order

1. Phases 1, 2, 3, 4 produce the brief and copy. Do these first, dry, before touching code.
2. Phases 5, 6, 7, 8 build the site. Code happens here.
3. Phases 10, 11, 12 wire infrastructure. Site goes live.
4. Phase 13 is the gate. Nothing ships without a clean anti-slop pass.

## Review loop (locked)

After every phase, pause. Present the deliverable to the operator. Ask explicitly: "approve, or fix what?"

Wait for the response before proceeding. Acceptable responses:
- "Approve" or "next" → move to the next phase
- A specific fix instruction → apply the fix, present again, ask again
- "Skip" → mark the phase as skipped (only for Phase 6 roster, when single-offer)

Never run all 13 phases without checkpoints. The operator is the manager. The agent reports. Treat each phase like a junior dev presenting a PR for review, not like an autonomous bot.

This rhythm is what keeps the operator in control and prevents AI-slop from sneaking through. Lose the rhythm, lose the craft.

## Defaults

- **Funnel:** 2 pages (`/squeeze` + `/`). The operator can add `/about`, `/pricing` later.
- **VSL length:** 8 minutes. Cold traffic prefers 5 to 8 min.
- **Stack:** Next.js 16 + Tailwind 4 + R3F 9 + Drei 10 + Three r171 + Supabase + Resend + Vercel. Locked. Do not negotiate.
- **Accent color:** pulled from operator's `business.md`. No fallback. Stop and ask if missing.
- **Typography:** pulled from operator's `business.md`. No fallback.
- **Aesthetic:** pulled from operator's `business.md`. Drives Higgsfield prompts, hero concept, Tailwind colors, type weights.
- **Hero concept:** the operator's aesthetic decides. Could be a 3D mesh, a photograph, a video loop, an abstract shader, a character portrait. See `references/05-3d-hero-scene.md` for stack, but the concept is brand-led.
- **Roster pattern:** pulled from the operator's offer shape. See `references/06-character-select.md` for the gate (when to use which pattern).

## Failure modes

**The site looks AI-generated.** Almost always means I skipped Phase 13. Run it. Cut everything that fails. Rewrite the cuts. Do not negotiate with the humanizer rules.

**The 3D hero blocks LCP.** I forgot `dynamic` import with `ssr: false`. Fix at `app/page.tsx`. The headline must paint first.

**The bundle exceeds 250KB.** I overbuilt. Cut the scene. Drop a shader. Lower triangle count. Use a poster image fallback on mobile.

**The form does not submit.** Supabase env vars wrong, or the API route reads the wrong table. Re-run Phase 11.


## Handoff template

When the build is done, drop the run report at `.claude/owner-inbox/YYYY-MM-DD_jude_<slug>.md`:

```
# Jude build report · <date>

## Live URL
https://<domain>

## Pages shipped
- /squeeze (lead magnet)
- / (long-form landing)

## Bundle stats
- Hero chunk: <X>KB gzip
- Total LCP: <Y>ms (mobile)

## VSL
Script: <link to script file>
Higgsfield prompts: <link to prompt sheet>
Status: not yet recorded / placeholder live

## What is left for the operator
- [ ] Render Higgsfield assets (hero image + 6 VSL beats)
- [ ] Drop assets into `/public/`
- [ ] Replace VSL placeholder with embedded video
- [ ] Verify Resend domain DNS
- [ ] Test the full funnel end to end

## Anti-slop pass
- Em dashes: 0
- Banned words: 0
- Humanizer-check: passed on all blocks
```

## Related skills

- `/humanizer-check`: runs on any copy block before it ships. Invoke after writing each text block.
