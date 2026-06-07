---
name: cold-email-retro
description: Runs the Day 28 structured retrospective on the operator's first 7 days of cold email (Day 21 launch through Day 27). Reads Instantly campaign analytics, invokes past-self-pattern internally, identifies the winning sequence, kills the bottom 1-2, and writes the retro to retros/cold-email-retro-day-28.md. The Day 29 cold-sequence-writer rerun reads from this. Use on Day 28 of Month 1, or whenever the operator says "run a cold email retro" or "review my Instantly campaigns."
---

# Cold Email Retro

By Day 28 the cold campaign has been live for 7 days. Around 700 emails sent (ramping schedule). Today the operator finds the winner, kills dead sequences, and pulls the data that feeds tomorrow's 3 new sequences.

Cold email iterates faster than any other channel. A bad campaign tweaked correctly can move from 1% reply to 5% inside two weeks.

## What to do

1. Read `business.md ## Past Self`, `business.md ## Niches`, `business.md ## Offers`, the 6 Instantly campaigns from Day 16, and `outreach/apify-pipeline.md`.
2. Pull Instantly analytics. Reply rate per sequence, positive reply rate, calls booked. Either via the Instantly MCP or have the operator paste the dashboard numbers.
3. Invoke `past-self-pattern` with the batch (replies + sent data).
4. Identify the winner (top positive reply rate).
5. Identify the killers (sequences under 1% reply).
6. Save to `retros/cold-email-retro-day-28.md`.

## The 4 metrics that matter

Per sequence:
- **Sent.** Total emails sent.
- **Reply rate.** Replies / sent. Includes positive, neutral, negative.
- **Positive reply rate.** Interested + asking-for-more / sent. The only long-term metric.
- **Calls booked.** From this sequence specifically.

Expect meaningful variance. Some 4%+, some under 1%. Variance tells you which offer + hook combination landed.

## Phases

### Phase 1. Pull the numbers (5 min)
Per sequence: sent, reply rate, positive reply rate, calls booked. Instantly MCP or paste from dashboard.

### Phase 2. Identify the winner (3 min)
Highest positive reply rate. Note:
- Niche it targeted
- Offer used
- Hook variant
- Opening line word-for-word
- Follow-up cadence

This DNA goes into tomorrow's 3 new sequences.

### Phase 3. Identify the killers (3 min)
Sequences under 1% reply. Common root causes:
- Wrong niche targeting (filter pulled leads outside the niche)
- Wrong offer for this segment
- Hook line generic or AI-sounding
- Initial email over 75 words
- Voice is corporate (does not pass the text-message test)

### Phase 4. Pattern (3 min)
Invoke `past-self-pattern`. Look for niche split, hook variant split, past-self alignment effect.

### Phase 5. Pick the changes (3 min)
Three actions:
1. Kill the bottom 1-2 sequences. Volume reallocates to top performers.
2. List the 2-3 specific copy changes for tomorrow (winner pattern + killer diagnosis).
3. Adjust scrape filters for the next batch (Day 25 batch loaded into new sequences).

### Phase 6. Save (1 min)

## Output file format

Save to `retros/cold-email-retro-day-28.md`:

```markdown
# Cold email retro · Day 28

Date: [today]
Total sent: [N]
Total replies: [R]
Total positive: [P]
Total calls booked from cold: [C]
Overall reply rate: [X]%
Overall positive reply rate: [Y]%

## Sequence performance

| # | Niche | Hook | Sent | Replies | Positive | Calls |
|---|---|---|---|---|---|---|
| 1 | A | Credibility | 130 | 6 | 4 | 1 |
| ...

## The winner

Sequence: [#]
Niche: [A / B / C]
Offer: [Tier S or V from business.md ## Offers]
Hook: [variant]
Opening line: "[exact text]"
Positive reply rate: [Z]%

## The killers
[Sequence #. diagnosis]
[Sequence #. diagnosis]

## Pattern findings
[Niche split]
[Hook variant split]
[Past-self alignment effect]

## Changes for Day 29 sequence rewrite
1. [Specific copy or structure change drawn from winner]
2. [Specific copy or structure change drawn from killer diagnosis]
3. [Filter adjustment for next scrape batch]
```

## Worked example

Day 28. 720 sent, 18 replies (2.5%), 11 positive (1.5%), 2 calls booked.

Sequences:
- Seq 1 (niche A, credibility-led): 130 sent, 4 positive (3.1%), 1 call. Winner.
- Seq 2 (niche A, pain-named): 125 sent, 1 positive (0.8%). Kill candidate (redundant alongside Seq 1).
- Seq 3 (niche B, story-led): 120 sent, 2 positive (1.7%), 1 call. Hold.
- Seq 4 (niche B, question hook): 118 sent, 0 positive. Kill (AI-sounding).
- Seq 5 (niche C, peer-reference): 122 sent, 3 positive (2.5%). Hold.
- Seq 6 (niche C, result-tightness): 105 sent, 1 positive (1.0%). Hold.

Winner: Seq 1 opening line "I added $42K in recurring revenue to my own bookkeeping practice in 6 months by automating QBO close. Same niche as you."

Pattern: Niche A has the strongest cold signal (5 of 11 positives from its 2 sequences). Past-self alignment matters (4 of 5 niche A positives mentioned operator's lived experience).

Changes for Day 29:
1. New sequences inherit credibility-led structure with past-self specifics in opener.
2. Drop question hooks entirely. Replace with niche-tailored insight in E3.
3. Filter Day 25 batch tighter on QBO mention to lift niche A volume.

## Anti-pattern to flag

Operators want to declare a winner after 100 sends per sequence. Push back: "Under 100 positive replies total, single-sequence variance is high. Trust the relative ranking. Kill the bottom 1-2. Hold the middle. Scale the top."

Also flag: operator counts a "no thanks" as a negative reply only. Auto-reply, vacation, or "wrong person" emails do not count as engagement signal. Strip those.

Also: they want to lower the price after slow cold replies. Push back: "Cold reply rate is an opener and offer issue, not a price issue. Buyers do not see the price in cold. Fix the opener."

## When this skill is done

`retros/cold-email-retro-day-28.md` saved with the winner, the killers, and the 3 changes for tomorrow's rewrite. Operator runs `cold-sequence-writer` on Day 29.
