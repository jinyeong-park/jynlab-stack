# business.md output schema

The single source of truth for an operator's strategy, identity, sales infra, and active weekly state. One file at the root of the Squad folder. No intermediate files in foundation/, offers/, outreach/templates, or marketing/communities. Those folders and files do not exist in the Starter Kit any more.

Four blocks, ordered by how often they change.

```markdown
# A. Identity & Positioning (Day 2, mostly static)

## Past Self
[Bucket sentence (1 line). Then 6 verbatim phrases the bucket uses about their pain, in their own words. Pulled from the Day 2 interview.]

## 30 Names
[30 real humans from the Past Self interview. Each line: Name · source tag (past-me / past-clients / past-colleagues) · 1-line context · channel I will reach them on. This list seeds the Squad CRM Sheet on Day 4.]

## Niches
[3 niches inside the bucket. A = priority. B, C = backup. Each: 2-3 sentence definition + why this slice.]

## Shape
[Agency / Consulting / Software / SaaS. Default Agency in Month 1. 65/20/10/5 allocation reasoning if shape pick is non-default.]

## Vision
[The specific world the operator wants to build. Personal, not generic.]

## Mission
[One sentence. Uncomfortably big.]

## Who I am
[Full arc: where they started, what happened, what broke, what they learned, why they are here now. 3-6 sentences. First person.]

## Beliefs
[5-7 numbered beliefs. Each should make someone disagree. Format: **Bold statement.** 1-2 sentence explanation.]

## The enemy
[Named identity. Bold the name. Then 2-3 paragraphs describing the pattern, why it traps people, what the exit looks like.]

## The problem (three layers)
**External (practical):** [Observable, day-to-day problem]
**Internal (emotional):** [How it feels to be stuck]
**Philosophical (why it is wrong):** [Why the world should not work this way]

## Ideal client
[Vivid portrait. Name, age, situation. What they do at 9pm on a Tuesday. What they have tried. What broke. 4-6 sentences.]

## Voice and brand
[Tone, words to use, words to avoid. Written as direct instructions for Claude.]

## Identity

### Tribal vocabulary
| Term | Meaning | How it sounds |
|------|---------|---------------|
[Minimum 5 terms with definitions and example usage]

### Rituals
[Minimum 3 rituals. Format: **Name (frequency).** Description.]

## Competition

### Tier 1: Direct competitors
| Creator | Subs | Offer | Price | Platform | Promise |
|---------|------|-------|-------|----------|---------|
[Real data from Perplexity research. Not guesses.]

### Tier 2: Adjacent
| Creator | Subs | Offer | Price | Focus |
|---------|------|-------|-------|-------|
[Real data from Perplexity research.]

### What makes us different
[3-5 specific differentiators. How we are different, not "we are better."]

### Price positioning
| Tier | Who | Price |
|------|-----|-------|
| Budget | [names] | [prices] |
| **Ours** | **[name]** | **[price]** |
| Premium | [names] | [prices] |

**Why this price:** [rationale]
**Why not lower:** [rationale]
**Why not higher:** [rationale]

---

# B. Sales Infra (Day 3-13)

## Sales Skeleton
[5-step call structure from Day 4. Opener / Diagnose / Stakes / Solution / Close.]

## Message Templates
[4 templates: inner-circle / coworker / cold-warm / cold-cold. Each: hook + case study line + ask + friction reducer.]

## Communities
[3 communities operator joined on Day 3. Each: name + platform + bucket relevance + post cadence.]

## Offers
[Up to 6 offers from Day 13. Each: name + deliverable + price + first result + guarantee.]

## Cold Email
[Strategy note: which niche is winning, which sequence pulls. Bodies live in Instantly, not here. One paragraph.]

## Proof and results
[Clients, testimonials, case studies. Or "No clients yet. Building proof through first 3 engagements."]

---

# C. Active State (updates weekly)

## Hypothesis (this week)
[Single sentence. XYZ frame from Pre-Program. At least X% of Y will Z within 7 days. Updated every Sunday.]

## Current Build (this week)
[The product being built Mon-Tue 48hr. One line. Updated every Sunday.]

## Patterns
[Retro headlines accumulated. Each line: Date · 1-sentence insight from the retro. Full retro text lives in `retros/`. This is the actionable distillation.]

## Numbers right now
[Current revenue, clients, pipeline. Real numbers. If zero, say zero. **Squad CRM Sheet URL goes here.**]

## Goals
[1-week, 1-month, 6-month targets. Specific numbers.]

## Weekly targets
[Messages, calls, content pieces. Specific numbers per week.]

## Month 1 Decision
[Day 30 output: Scale / Pivot / Kill. Seeds Month 2 first Hypothesis. Only filled on Day 30.]

---

# D. Operating manual (one-time)

## Rules for Claude
[Specific guardrails. Minimum 5 rules. "Never say X." "Always reference Y." "When writing outreach, lead with Z."]
```

## Writing rules for the business.md itself

- No marketing-speak anywhere. Every sentence should be plain English.
- Use the operator's actual words where possible, cleaned up for clarity.
- No filler. If a section has one sentence of real content, that is fine. Do not pad.
- Numbers are concrete. "$8,500 retainer" not "competitive pricing."
- The 4 MVP Lines (inside Offers) must be completable in one breath. If any line is longer than 10 words, trim.
- All text must pass humanizer rules. No banned words, no banned phrases, no em dashes.
- First person for "Who I am." Third person nowhere.
- Beliefs should read like convictions, not corporate values.
- The enemy section should feel like a story, not a definition.

## How sections get filled

| Section | Card / Skill | Day |
|---|---|---|
| Past Self · 30 Names | `mine-past-self` (interview) | Day 2 |
| Niches | `niche-selector` | Day 2 |
| Shape | `compile-business-md` confirms | Day 2 |
| Vision · Mission · Who I am · Beliefs · Enemy · Problem · Ideal client · Voice · Identity · Competition | `compile-business-md` (drafts), operator refines | Day 2 |
| Sales Skeleton | `sales-skeleton` | Day 4 |
| Message Templates | `message-template-builder` | Day 3 |
| Communities | `community-finder` | Day 3 |
| Offers | `offer-builder` | Day 13 |
| Cold Email | `cold-sequence-writer` writes the note here; bodies into Instantly | Day 16, 29 |
| Proof and results | manual + `case-study-builder` | Day 2 onward |
| Hypothesis · Current Build | operator writes Sunday, `month-1-retro-decide` confirms | Every Sunday |
| Patterns | every retro skill appends 1 line | Day 7, 10, 11, 16, 17, 18, 21, 24, 28 |
| Numbers · Goals · Weekly targets | operator writes Day 2, updates each Sunday | Day 2 + weekly |
| Month 1 Decision | `month-1-retro-decide` | Day 30 |
| Rules for Claude | operator writes Day 2 | Day 2 |
