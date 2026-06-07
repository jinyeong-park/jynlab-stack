---
name: business
description: Day 2 master compile. Produces a complete business.md through Socratic interview backed by real data. Scrapes Reddit + YouTube comments + Perplexity to validate the operator's winning niche (/20 scoring), auto-recommends offer + pricing + guarantee from competitor gaps, and writes 5 warm conversation starters. Every other Squad skill reads business.md. Use on Day 2 of Month 1, or whenever the operator says "build my business.md", "compile my business doc", or "find my niche" with rough niche ideas.
argument-hint: "[optional: rough niche idea, e.g. 'dental clinics Austin' or 'AI service business']"
user-invocable: true
---

# /business: your complete business file in one conversation

One command produces a complete `business.md` through a guided conversation backed by real data. This is the single source of truth every other skill reads. The skill interviews you (Socratic, one question at a time), scrapes the market (Reddit, YouTube, Perplexity), validates your niche (/20), auto-recommends offer and price from competitor gaps, writes 5 warm conversation starters. You walk out with a locked niche, a locked offer, and 5 people to message today.

**Required MCP:** Perplexity (research), Apify (Reddit), YouTube (comments + search suggestions). Gmail optional (warm outreach).

## Input

- Read existing `business.md` if it exists (update mode)
- Read `.claude/rules/humanizer.md` for writing rules
- $ARGUMENTS (optional): rough niche idea

## Step 1: Detect mode

1. Check if `business.md` exists.
2. If exists with a niche defined: UPDATE MODE. Show section summary, ask what changed, only re-interview changed sections. If updating niche, re-run scraping.
3. Otherwise: NEW MODE (Phase 1-10).

---

## Phase 1: Socratic questions (understand the person)

One question at a time. Wait for the answer before the next.

**Warm-up:**
1. "What work have you done in the last 5 years? Not job titles. What did you actually DO?"
2. "Who did you help, and what specific problem did you solve?"
3. "What result did they get? Numbers if you have them."
4. "If you charged for that, what would someone pay?"

**Vision + Mission:**
5. "What's the world you want to build? Not your business goal. The world."
6. "What's the biggest thing you could accomplish with this?"

Vision detector: if generic ("help people succeed"), push back: "That could be anyone's vision. What's specific to YOU?"

**Who I am:**
7. "What's your background? What pushed you to go solo?"

Goal: the full arc, not a resume. Where they started, what broke, why they are here now.

**Network size:**
8. "How many people could you text right now and get a reply? Friends, family, ex-coworkers, college classmates, neighbors. Not LinkedIn connections you never talk to. Rough number."

- 50+: LARGE warm base.
- 10-50: MEDIUM. Enough for the 5-Person Test with room.
- Under 10: SMALL. Still run the 5-Person Test. If warm cannot produce 5, cold dashboard is the fallback.

---

## Phase 2: Niche candidate generation + data scraping

From the Socratic answers, generate 2-3 candidate niches. Present them:

```
Based on your background, here are 3 niche candidates:
1. [Candidate 1] - because [reason from their answers]
2. [Candidate 2] - because [reason]
3. [Candidate 3] - because [reason]

I'm going to scrape Reddit, YouTube, and competitor data for each one. Give me a minute.
```

Load `references/03-niche-data-collection.md` for the full scraping workflow.

Per candidate:
1. Reddit scrape via Apify (target subreddits, 20-50 results)
2. YouTube comment scraping (2-3 competitor videos, 20-30 comments each)
3. YouTube search suggestions (3 keywords)
4. Perplexity validation (3 queries: market size, competitor deep dive, positioning gaps)
5. Score /20 (demand, competition, willingness to pay, reachability)

Present:

```
--- NICHE SCORECARD ---
[Candidate 1]: [score]/20 - [one-line summary]
[Candidate 2]: [score]/20 - [one-line summary]
[Candidate 3]: [score]/20 - [one-line summary]

Recommended: [Candidate X] because [data-backed reason].
Do you agree, or want to go with a different one?
```

If all score below 13: back to Phase 1 and explore a different direction.

Save scrape data to `temp/{YYYY-MM-DD}_niche-prospects-{niche-keyword}.json`.

---

## Phase 3: 5-Person Test + Lock

Once the winning niche is agreed:

Ask: "Name 5 real humans you could text right now who either have this problem OR know someone who does. Friends, family, ex-coworkers, classmates, neighbors. Not past clients. Not industry contacts. Not LinkedIn 2nd-degree. People who know you as a person."

These 5 are the niche discovery engine, not a pitch list. First conversations tell you if the problem is real, how they describe it, what they would pay. The niche sharpens from there.

If they cannot name 5: the niche is too vague or pulled too far from who they actually know. Help narrow or shift. Repeat until 5.

If they can: those 5 become Day 1 warm conversation starters. Save them.

**7-Day Lock:** "This niche is locked for 7 days. You do not switch until you have talked to real people for a full week."

---

## Phase 4: Beliefs + Enemy

**Beliefs (5-7 distinct):**
1. "What do you believe about your industry that most people disagree with?"
2. "What's a common piece of advice in your space that you think is dead wrong?"
3. "What do your future clients believe right now that's holding them back?"

Platitude detector: if "hard work pays off" or "quality matters," push back: "Nobody would argue with that. What do you believe that would make someone push back?"

**The enemy:**
1. "What's the specific pattern your audience is stuck in?"
2. "If you had to name that pattern like a character, what would you call it?"

Enemy detector: if vague ("lack of knowledge"), push back: "That's a problem, not an enemy. The enemy is an identity. Who is your client right now that's holding them back?"

**Three-layer problem:**
3. "What's the practical day-to-day problem?" (external)
4. "How does that make them feel?" (internal)
5. "Why is it wrong that this problem exists?" (philosophical)

---

## Phase 5: Offer + Price + Guarantee (data-informed)

Auto-recommend from competitor gaps in Phase 2:

```
Based on the competitor data:
- [Competitor A] charges $[X] for [what]
- [Competitor B] charges $[Y] for [what]
- Gap: nobody offers [specific gap]

Recommended offer: [deliverable] for [niche] at $[price]/month.
Delivery: [model]. Timeline: [first result in X days].
Does this feel right, or do you want to adjust?
```

Marketing-speak detector: if "comprehensive solutions" or "AI-powered optimization," stop: "That sounds like a LinkedIn headline. What do you actually do?"

Price enforcement: if they give a range, force one number: "Pick one. You can change it after 10 conversations."

**Guarantee:** "What can you guarantee?" Build stacked guarantee if possible: risk reversal + overdelivery promise.

**4 MVP Lines:**
```
Line 1 (Niche): I serve [who] who [situation].
Line 2 (Offer): I give them [what] so they [result].
Line 3 (Price): $[amount]/month. [ROI math.]
Line 4 (Delivery): Week 1: [action]. Week 2: [action]. Week 3: [first result].
```

---

## Phase 6: Ideal client + Voice + Identity

**Ideal client:**
1. "Describe your perfect client. Not demographics. A real person. Name, age, what they do at 9pm on a Tuesday."
2. "What have they already tried that didn't work?"
3. "What's the moment they realize they need you?"

**Voice:**
4. "How do you actually talk? Read me a message you'd send to a friend about what you do."

Voice detector: if their natural voice is casual but "brand voice" sounds corporate: "You just described your service casually and it sounded great. Which one is really you?"

**Identity (tribal vocabulary):**
5. "What do your members call themselves?"
6. "What's the daily ritual?"
7. "What are the milestones?"

Goal: 5 tribal terms + 3 rituals minimum. If early, help create them from niche + enemy.

---

## Phase 7: Competition table + Price rationale

Already have competitor data from Phase 2. Enrich with Perplexity if needed.

Price positioning table: budget tier, your tier, premium tier.

"Why this price? Why not lower? Why not higher?"

---

## Phase 8: Numbers, goals, rules for Claude

1. "Where are you right now? Revenue, clients, pipeline."
2. "1-week goal? 1-month? 6-month?"
3. "What do you do every week? Messages, calls, content."
4. "What should Claude never do?"
5. "Hard rules? Pricing floors, industries to avoid?"

---

## Phase 9: Generate warm conversation starters

Using the 5 people from Phase 3, generate one personalized message each. Not pitches. Conversation starters. Goal: learn, not sell.

Under 80 words. Casual. Sounds like a text to a friend, because it is.

Vary by relationship:
- Close friend or family: reference something specific from your shared life, ask if they or anyone they know hits this problem
- Ex-coworker: reference a real moment from when you worked together, ask if their current role has this pain
- College classmate or neighbor: reference the last time you talked, ask a genuine question about their world
- Referrer type (someone connected to many): ask if they know anyone who fits the problem

Every message ends with a question. Never a sales ask. The goal is a reply.

Present all 5: "Send these now? [Yes / Pick 3 / Pick 1]"

---

## Phase 10: Review + Save

1. Generate one-liner: "I help [who] get [result] in [time] without [pain], and I guarantee [risk reversal]."
2. Generate positioning statement.
3. Show complete `business.md` for approval.
4. Save to project root.
5. Next actions:

```
NEXT ACTIONS:
1. Send your 5 messages NOW. Not tomorrow. Now.
2. The Day 8 apify-pipeline-setup skill automates outreach at scale.
3. 7-Day Lock: do not switch niches for 7 days. Talk to people.

business.md saved. Scrape saved to: temp/{date}_{file}.json
```

---

## Overthinking check

If the operator wants to restart, test 3+ niches, or debates between similar options for 2+ messages:

"You're researching instead of shipping. Pick one. The 7-Day Lock means you test for a full week before switching. Pick the one that felt most natural."

---

## Self-check before finishing

1. All sections filled (or explicitly marked "to be filled")
2. No marketing-speak ("comprehensive", "solutions", "optimize", "holistic")
3. Price is a single number
4. 4 MVP Lines each under 10 words
5. Voice reflects how the operator actually talks
6. Rules for Claude has 5+ specific guardrails
7. Operator explicitly approved
8. File saved as `business.md` at project root
9. Niche validated with data (Reddit + YouTube + Perplexity, scored /20)
10. Competitor table has real data, not guesses
11. 5 warm messages are personalized
12. No em dashes anywhere
13. No Tier 1/2 banned words
14. Vision and mission are specific (not "change the world")
15. Enemy is named and specific (identity, not problem)
16. Three-layer problem covers external, internal, philosophical
17. Scrape results saved to `temp/`

## Reference library

| File | When to load |
|---|---|
| `references/01-business-md-schema.md` | Phase 10, writing the final `business.md`. Full 21-section schema. |
| `references/02-edge-cases.md` | When conversation stalls. 10 edge cases + 10 style rules. |
| `references/03-niche-data-collection.md` | Phase 2, during niche scraping. Full Reddit/YouTube/Perplexity workflow with subreddit targets, scoring bands, error handling. |

## Change log

| Date | Changes |
|---|---|
| 2026-04-10 | v3: Merged /find-niche into /business. Added Phase 2 (candidate generation + Reddit/YouTube/Perplexity scraping + /20 scoring). Added Phase 9 (5 warm outreach messages). Offer in Phase 5 auto-recommended from competitor data. |
| 2026-03-30 | v2: 7 phases, 21 sections, detectors, Perplexity competitor research. |
| 2026-03-30 | v1: 5-phase Socratic interview. |
