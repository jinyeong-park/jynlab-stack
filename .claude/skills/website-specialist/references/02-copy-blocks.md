# 02 · Copy blocks

Patterns for every text block on the funnel. Pain-led, anti-AI-slop, humanizer-clean. Each pattern has a template, an example, and a rule.

**Read this first.** All examples in this file come from one operator (executionsquad.co). They show the PATTERN, not the voice. The operator's voice, accent color, typography, and specific phrasings come from their own `business.md`. Do not copy the example phrases. Copy the structure.

Examples like "Stop learning AI / Start Executing it", "You are not behind / You are addicted", "Close the tabs / Open the folder" are the Execution Squad's voice. Different operators land on different lines. A fitness coach might write "Stop researching workouts / Start lifting", a SaaS founder might write "Stop watching demos / Start shipping", a B2B agency might write a more measured "Most playbooks are theater / Ours runs in production". The pain-led-inversion STRUCTURE is universal; the words are not.

## The voice

- **First-person singular for the operator's voice.** "I", not "we". Trust comes from one human, not a committee.
- **"You" for the reader.** Direct address. Accusation when the pain block lands.
- **Short, then long, then short.** Sentence variety reads as human. Uniform cadence reads as AI.
- **One opinion per section minimum.** Take a side. The reader feels the spine.

## Banned words and phrases

These are AI tells. Strip them on sight.

**Banned vocabulary** (Tier 1, never use): delve, tapestry, multifaceted, landscape, leverage, robust, testament, pivotal, underscore, encompass, realm, embark, interplay, intricate, nuance, garner, paramount, commendable, meticulous, showcase, symphony, beacon, indelible, bustling, vibrant, enigma, unwavering, nestled, annals, bespoke.

**Banned vocabulary** (Tier 2, avoid): elevate, navigate, harness, unlock, foster, bolster, captivate, comprehensive, cutting-edge, groundbreaking, seamless, holistic, transformative, pioneering, trailblazing, streamline, innovative, revolutionary, supercharge, reimagine, orchestrate, synergy, align, dynamic, profound, esteemed, whimsical, burgeon, aptly, poised.

**Banned phrases**: "in today's fast-paced world", "in the realm of", "when it comes to", "it's worth noting that", "stands as a testament", "plays a vital role", "paving the way", "at the forefront of", "game-changer", "best-in-class", "the future looks bright", "only time will tell", "unleash the power of".

**Banned formatting**: em dashes (use period, comma, parens), Title Case headings (use sentence case), decorative emoji in body text, the "**Bold term:** explanation" pattern in bullet lists.

Run `/humanizer-check` after writing any block. The skill catches these automatically.

## Hero block

The first thing the visitor sees. Two-line H1, one paragraph subhead, optional CTA below.

### Pattern

```
H1 line 1 (white): [Pain command, imperative verb]
H1 line 2 (italic + accent): [Inversion or alternative]
Subhead (zinc-300/400, max-w-xl): [Promise + specifics, 3-4 short clauses]
```

### Examples

**Squeeze page (lead magnet)**
```
Execute,
don't learn.

Free. The roadmap plus Jude. Install tonight. No more AI tutorials.
```

**Long-form landing**
```
Stop learning AI.
Start Executing it.

Twelve Claude Code agents. One folder on your machine. Your business runs from there. No new tutorial. No new tool to chase tomorrow.
```

### Rules

- **Pain-led, not feature-led.** Never "Build websites in 5 minutes." Always "Stop renting your stack."
- **Two lines maximum.** Three lines reads as a paragraph, not a hero.
- **Second line italic.** Inverts the first line. Different color (accent).
- **Subhead is short clauses, not one long sentence.** Period-separated rhythm reads punchy.
- **No subhead highlight clutter.** Maximum one phrase highlighted in white. Default is zero highlights.

## Subhead block (general body paragraph)

Used in every section after the heading.

### Pattern

```
[Specific claim] [Concrete proof] [Implication for reader].
```

### Example

> Three specialists release per week. Mon, Wed, Fri. Each launch ships an agent file, a base skill, a video walkthrough, and a live build call. Sunday May 24 is the orchestrator reveal.

### Rules

- **Lead with the specific.** Numbers, dates, names.
- **One sentence per beat.** Mix lengths inside the paragraph.
- **End on the reader's stake.** What does this mean for them?

## Problem block (agitation)

The "why you bought another tutorial last week" section. First-person from the operator. "You" accusation. Unflinching.

### Pattern

```
[Section eyebrow]: The actual problem
[H2]: [Pain reframe, two lines, second italic accent]

[P1] [Concrete pattern the reader recognizes]. [P2] [Why it is not their fault]. [P3] [Operator's own version of this pain]. [P4 (white text, the answer)] [What stopped it]. [P5] [The product is the exit, not another tool].
```

### Example (from `executionsquad.co`)

```
THE ACTUAL PROBLEM

You are not behind.
You are addicted.

You bookmarked the tutorial. Bought the course. Signed up for the new tool. A new model shipped. You started over.

This is not learning. This is chasing. Every tool sells a chase dressed up as a tool. Every model release resets your stack. Every guru sells you a course about the thing you have not used yet.

You are not lazy. You are not slow. You are addicted because someone built a business out of selling you the next thing.

I lived in that loop for years. Twenty tabs open. Three half-finished platforms. A Notion graveyard. The shame of paying for something I already owned.

Here is what stopped it. Everything on my own machine. One folder. Claude Code as the brain. My platform on the front. Twelve specialists I built once that keep running.

The Squad is not another tool. It is the exit from the chase. Sovereignty is what shows up after.
```

### Rules

- **The pain has to be specific.** "Twenty tabs open" not "feeling overwhelmed." Specifics convert.
- **Operator's own pain matters.** The reader buys from someone who lived it.
- **The white-text paragraph is the answer.** Make it visible. Bold weight or full white.
- **Last line is the product reframe.** "Not another tool. The exit."

## Roster block (character select)

Used when the offer is a list of N items. Specialists, modules, week-by-week deliverables, team members, frameworks. See `06-character-select.md` for the component.

### Copy pattern (eyebrow + heading + intro paragraph)

```
[Eyebrow]: The roster
[H2]: [Name of the collection. (italic) [What they share]].

[Intro paragraph]: [How many] [items]. [Sequencing rule]. [What each one ships]. [Closing line].
```

### Example

```
THE ROSTER

Twelve specialists.
One business.

Each specialist is a Claude Code agent with a defined role, a base skill, a reference, and a 30+ minute video walkthrough. Three release per week until Sunday May 24.
```

### Rules

- **The inversion happens on the second H2 line.** "One business" lands harder than "for your team."
- **Intro paragraph is structural.** What is each item, how often does it ship, when does it end.

## Offer block (the commitment)

The biggest, most detailed section on the page. The visitor watched the VSL. Now the rational read.

### Block order inside the offer section

1. **Eyebrow:** `Founding [Role] · The commitment` (or whatever the operator's tier name is + "The commitment")
2. **Title (centered):** Price line, two lines, first part italic accent. e.g. "$997. / Locked for life."
3. **Subtitle:** "One commitment. One year of [thing]. [Onboarding promise]."
4. **Two hero deliverable cards** (side by side):
   - Left card (accent border): immediate deliverable (e.g. 1-on-1 onboarding call within 48 hours)
   - Right card (zinc border): ongoing deliverable (e.g. 12 months of access)
5. **The roadmap** (week-by-week timeline if applicable). See pattern below.
6. **Also included** (secondary 2-column list of smaller deliverables)
7. **Guarantee** (its own bordered card with title + paragraph)
8. **Animated seats progress bar** (urgency, only if there is a real cap)
9. **Claim CTA button**

### Title pattern

```
[Eyebrow uppercase, tracking-wide]: [Tier name] · The commitment
[H2 centered, big serif]:
  <span italic accent>$997</span>.
  Locked for life.
[Subtitle centered, zinc-400]: One commitment. One year of full execution. [Onboarding line].
```

### Hero deliverable card pattern

```
[Tag, accent + dot]: Within 48 hours
[H3 italic serif]: One-on-one onboarding with [operator name]
[P zinc-300]: 60-minute strategy call. We open your folder, lock your niche, and pick the first [thing] that ships your first move. You leave with a 30-day execution plan.
```

The right card mirrors the structure with a different tag (e.g. "12 months") and a different deliverable (e.g. the full library + every new release).

### Roadmap row pattern (week-by-week timeline)

```
Per week:
- Week label (accent, uppercase, tracked): "Week 1 · [Theme]"
- Date range: "Apr 27 to May 1"
- Per item in the week:
  - Number badge (48px, accent border + tint, tabular-nums)
  - Italic serif name + small uppercase role tag inline
  - One-line description (zinc-300, 14-15px)
  - Bordered date pill (zinc, uppercase tracking-wide)
```

### Item description rules

- **One sentence each.** Two short ones max.
- **Concrete deliverable + tone.** "3D landing pages and funnels, scaffolded from empty folders. Caravaggio not Vegas."
- **No marketing fluff.** "Builds new specialists. Ships 72-hour MVPs. The rock that grows the squad."

### Guarantee pattern

```
[Eyebrow]: The 90-day guarantee
[H3]: [Outcome] live in 90 days.
[P]: [Specific deliverables, 3-4 items, period-separated]. If any of those is not live in 90 days, I keep working with you free until [outcome].
```

### Example

```
THE 90-DAY GUARANTEE

Sovereign business live in 90 days.

One owned domain. One owned platform. One paying client. One launched specialist that serves that client. If any of those four is not live in 90 days, I keep working with you free until all four are.
```

### Rules for guarantee

- **Specific outcomes, not vague promises.** "First paying client" not "results."
- **First-person commitment.** "I keep working with you free."
- **No fine print.** The guarantee is the trust. Hedging kills it.

## Final CTA block (close)

Last section before footer. Pain-led close mirroring the hero pattern.

### Pattern

```
[H2 centered, two lines]:
  [Pain command]
  <span italic accent>[Action invitation]</span>
[Tagline below, uppercase tracking-wide, 14px]: Shut up and execute. (or operator's own version)
[Single claim button, accent bg]
```

### Example

```
Close the tabs.
Open the folder.

SHUT UP AND EXECUTE.

[Claim your seat →]
```

### Rules

- **Two lines maximum.** Same structure as hero.
- **Second line italic accent.** Visual rhyme with the hero binds the page.
- **Tagline is a one-liner, not a paragraph.** Operator's house phrase.
- **One CTA button.** No "or learn more" secondary. The page already taught.

## VSL placeholder block (when video is not yet recorded)

Used in the VSL section until the operator records.

### Pattern

```
[Aspect-video card, bg-zinc-950, border]:
  Centered:
    [Pulsing red dot] [Eyebrow]: Coming [Date]
    [Italic serif heading]: The walkthrough drops next week.

[Below the card, centered, zinc-400]:
  We email you the moment it lands.
```

### Example

```
● COMING MON APR 27

The walkthrough drops next week.

We email you the moment it lands.
```

## Form consent line (under email field)

The operator must include this. CASL/CAN-SPAM compliance + reader trust.

### Pattern

```
Click to get [the lead magnet], [operator name], and follow-up emails. Unsubscribe anytime.
```

### Example

```
Click to get the roadmap, Jude, and follow-up emails. Unsubscribe anytime.
```

### Rules

- **Be honest about follow-up.** Do not hide that you will send more emails.
- **Always include "Unsubscribe anytime."** Trust signal + legal cover.
- **Place under the form field.** 11-12px text, muted color.

## Footer block

Minimal. Wordmark, contact, location, legal links.

### Pattern

```
[Left]: [accent dot] + [Brand wordmark]
[Right]: [email] · [city, region] · [Privacy] [Terms]
```

### Example

```
● The Execution Squad

hi@aichrislee.com · Chilliwack, BC · Privacy · Terms
```

### Rules

- **No logo soup.** No "trusted by" strip.
- **No social icons in footer.** They drain attention.
- **Single line on desktop.** Two stacked rows on mobile.

## How to adapt these to the operator's `business.md`

When pulling from `business.md`:

1. **Find the operator's pain frame.** It usually sits in a "the disease" or "what is broken" section.
2. **Find their inversion.** What does the operator do that competitors do not.
3. **Find their proof.** Specific numbers, dates, names. If the operator has none, the copy will be vague. Push them to add real numbers before you write.
4. **Find their voice.** Read aloud the most authentic paragraph in `business.md`. Match that cadence.
5. **Find their accent color and serif.** Use those everywhere a single accent or display face is needed.

If `business.md` is too thin to write from, stop and tell the operator. Bad input means bad copy. The skill is not magic.

## Final pass

Before deploy, every text block runs `/humanizer-check`. The skill scans for:

- Banned vocabulary (Tier 1 + 2)
- Banned phrases
- Em dashes
- Decorative emoji in body
- Title Case headings
- Sentence-length variance (flag if too uniform)
- Formulaic openings ("In the realm of...")
- Formulaic closings ("Only time will tell...")

If anything fails, fix and re-run. Do not deploy until clean.
