---
name: month-1-retro-decide
description: Runs the Day 30 closing retrospective and the Scale / Pivot / Kill decision gate for Month 1. Reads every weekly retro, the Squad CRM Sheet, business.md ## Offers, business.md ## Niches, and pulls hard numbers (messages, replies, calls, proposals, closes, revenue). Diagnoses bucket fit, channel ROI, sales-process drop stages, and Anchors discipline. Forces one explicit Scale / Pivot / Kill. Writes the Month 2 hypothesis to business.md ## Hypothesis, saves the full retro to retros/month-1.md, and drafts a public Squad post. Use on Day 30 of Month 1, or whenever the operator says "run the month 1 retro" or "make the scale/pivot/kill call."
---

# Month 1 Retro + Decide

Day 30. The operator ran one full Flywheel turn at month scale. Now they call it: Scale, Pivot, or Kill. Three options. No middle. The Rule says they decide today, not tomorrow.

This retro is more thorough than any weekly. It locks the Month 2 hypothesis. The Rule applies after: no more changes until Day 60.

## What to do

1. Read the data:
   - `business.md ## Past Self` (bucket, case studies)
   - `business.md ## Niches` (3 niches tested)
   - `business.md ## Offers` (6 offers)
   - `business.md ## Numbers right now` plus the Squad CRM Sheet
   - All weekly retros: `retros/message-retro-week-1.md` through `retros/message-retro-week-3.md`, `retros/community-post-retro-week-*.md`, `retros/calls-retro-day-16.md`, `retros/proposal-retro-day-23.md`, `retros/cold-email-retro-day-28.md`
2. Pull hard numbers. Be honest about zeros.
3. Diagnose 4 dimensions: bucket fit, channel ROI, sales process, Anchors.
4. Force the decision. Scale / Pivot / Kill. Exactly one.
5. Write the Month 2 hypothesis.
6. Save to `retros/month-1.md` and update `business.md ## Month 1 Decision` and `business.md ## Hypothesis`.
7. Draft the public Squad post for the operator to ship (Squad thread first, then manual copy to LinkedIn or X).

## The Decide framework

**SCALE.** Reply rate above your threshold AND at least 1 close. Hypothesis works. Continue same bucket x niche x offer into Month 2. Productize the offer based on the close. Increase volume.

**PIVOT.** Reply rate above threshold (bucket reaches inboxes), but 0 closes. Bucket is right, offer or copy is wrong. Adjust offer + copy in Month 2. Same bucket. Different angle.

**KILL.** Reply rate below threshold AND 0 closes. Bucket is wrong. Pick bucket #2 from `business.md ## Past Self` candidates. Restart Month 1 with new bucket + new hypothesis.

The Rule applies after the decision is written. No changes until Day 60.

## Phases

### Phase 1. Hard numbers (5 min)
Count from the Squad CRM Sheet and source channels:
- Total messages sent (inner-circle DMs + community DMs + cold email if applicable)
- Total replies received
- Total positive replies
- Total calls booked / held
- Total proposals sent
- Total closes (paying clients)
- Total revenue collected (Stripe + outstanding)

Numbers do not lie. If you closed 0, write 0.

### Phase 2. Channel ROI (5 min)
Per channel: time spent, replies, calls, closes, revenue, cost per closed client. Some operators close 100% from inner circle. Others 80% cold. Most mixed.

### Phase 3. Bucket fit (10 min)
Look at the people who replied + the people who closed. Did they match the bucket as defined?
- Yes: bucket is real. Scale signal.
- Mostly bucket-adjacent: bucket may be too narrow or named wrong. Pivot signal.
- Random buckets: bucket guess was off. Kill signal.

Compare the 3 niches tested. The winner becomes the Month 2 niche.

### Phase 4. Sales process (5 min)
Pull the calls retro and proposal retro. Recurring drop stage? If most calls died on Implication, that fix carries to Month 2. If proposals died on Pricing, that fix carries.

### Phase 5. Anchors check (3 min)
Was the Family · Workout · Build · Customers filter held? Morning Deep Work, Body, Family, Sleep. Where did the operator slip? If held, note what worked. If slipped, name where and the fix for Month 2.

### Phase 6. Highs and lows (3 min)
Specific moments, not "I felt overwhelmed." More like "Day 12 I almost quit after 0 replies on 30 sends." Specific moments become content and future operator wisdom.

### Phase 7. The Decision (5 min)
Push for Scale if there is 1+ close and reply rate above 5%. Push for Pivot if reply rate is above 5% but 0 closes. Push for Kill if both are weak.

Write the decision in `retros/month-1.md` and `business.md ## Month 1 Decision` as one explicit sentence:

> "I am [SCALE / PIVOT / KILL]. For Month 2 I am [bucket x niche x offer for Month 2]."

### Phase 8. Month 2 hypothesis (3 min)
Write to `business.md ## Hypothesis` in 1 paragraph:

> "If I run [bucket x winning niche x winning offer] at [volume] across [channels] in Month 2, I will close [N] additional clients at [average value] for [total revenue]. The Rule: I do not change this hypothesis until Day 60 retro."

### Phase 9. Public Squad post (1 min)
Format:

```
Month 1 done.

Numbers:
- Messages: X
- Replies: Y
- Calls: Z
- Proposals: W
- Closes: K
- Revenue: $V

Decision: SCALE / PIVOT / KILL → [bucket x niche x offer for Month 2]

What worked: [specific].
What did not: [specific].
What surprised me: [specific].

Onward.
```

Post to Squad first, then operator manually copies to LinkedIn or X.

## Output file format

Save to `retros/month-1.md`:

```markdown
# Month 1 retro · Day 30

Date: [today]
Decision: [SCALE / PIVOT / KILL]

## Numbers
- Messages sent: [N]
- Replies: [R]
- Positive replies: [P]
- Calls booked: [B]
- Calls held: [H]
- Proposals sent: [PR]
- Closes: [C]
- Revenue collected: $[V]
- Revenue outstanding: $[O]

## Channel ROI

| Channel | Hours | Replies | Calls | Closes | Revenue | Cost/close |
|---|---|---|---|---|---|---|
| Inner circle | ... | ... | ... | ... | ... | ... |
| Community | ... | ... | ... | ... | ... | ... |
| Cold email | ... | ... | ... | ... | ... | ... |

Highest-ROI channel: [name]

## Bucket fit
[Did replies + closes match the bucket?]
[Winning niche of the 3 tested]
[Lost niches and why]

## Sales process
[Recurring drop stage on calls]
[Recurring drop on proposals]
[Fixes carrying to Month 2]

## Anchors
[Held / slipped on Family · Workout · Build · Customers]
[Specific slip moments]
[Fixes for Month 2]

## Highs and lows
[Specific moments]

## The Decision
I am [SCALE / PIVOT / KILL]. For Month 2 I am [bucket x niche x offer for Month 2].

## Month 2 hypothesis
If I run [bucket x winning niche x winning offer] at [volume] across [channels] in Month 2, I will close [N] additional clients at [average value] for [total revenue]. The Rule: no change until Day 60.

## Public Squad post
[generated post text, ready to ship to Squad first then copy to LinkedIn or X]
```

## Worked example

Day 30 numbers:
- 235 messages (60 inner-circle + 25 community + 150 cold)
- 28 replies (12% inner-circle, 10% community, 2% cold)
- 8 calls booked, 5 held
- 3 proposals sent
- 1 close at $8.5K (Tier V niche A)
- $4,250 collected (50% deposit), $4,250 outstanding

Channel ROI: Inner-circle highest. 25 hours, 7 replies, 3 calls, 1 close. Cold second. Community strong engagement but 0 closes yet.

Bucket fit: 4 of 5 calls from niche A. The 1 close was niche A. Niche B silent on calls. Niche A wins.

Sales process: 2 of 4 calls died on Price stage. Fix carrying to Month 2 (say price out loud, no email-it deflection).

Anchors: held all 4 weeks except 2 days where family commitments pushed Deep Work to afternoon. Acceptable.

Decision: SCALE. Niche A x QBO Close Automation Build (Tier V) into Month 2.

Month 2 hypothesis: "If I run solo bookkeepers in US/Canada using QBO x QBO Close Automation Build at 80 inner-circle messages and 1,500 cold sends across the month, I will close 3 additional clients at $8.5K each for $25.5K total. The Rule: no change until Day 60."

## Anti-pattern to flag

Operators want to Scale on weak data. 0 closes but "the calls felt good." Push back: "Felt-good is not a number. Scale requires a close. Pivot is the right call when reply rate is up but close rate is 0."

Operators want to Kill at the first hard week. Push back: "Pivot first. Bucket changes are expensive. Same bucket with new offer beats new bucket with same offer 8 of 10 times."

Operators want to skip writing the Month 2 hypothesis. Push back: "The hypothesis is the lock. Without it, Month 2 has no Rule and you drift back into mid-week pivots. Write it. Specific numbers."

Operators want to Decide privately. Push back: "Public commitment is the mechanism. Squad post mandatory. Manual copy to LinkedIn or X."

## When this skill is done

`retros/month-1.md` saved. `business.md ## Month 1 Decision` and `business.md ## Hypothesis` updated. Public Squad post shipped. Month 2 is locked.
