---
name: past-self-pattern
description: Internal pattern analyzer used INSIDE other retro skills. Reads a batch of operator data (messages, posts, calls, proposals, cold emails) and surfaces the 1-3 patterns that explain what worked through the lens of the operator's Past Self bucket and 3 niches. Not called directly by the operator. The retro skills (message-retro, community-post-retro, calls-retro, proposal-retro, cold-email-retro, month-1-retro-decide) invoke this internally so analysis stays consistent across the month. Use when a retro skill needs structured pattern output.
---

# Past Self Pattern

Internal helper. The operator does not call this directly. Retro skills invoke you with a batch of recent output (messages, posts, calls, etc.) and you return the 1-3 patterns that explain what worked, viewed through `business.md ## Past Self` and the 3 niches in `business.md ## Niches`.

## What to do

1. Read `business.md ## Past Self` (bucket, identity, case studies) and `business.md ## Niches`.
2. Receive the batch from the calling skill (raw messages/posts/calls/proposals/emails with outcomes).
3. Run the 4-pass analysis below.
4. Return structured pattern output to the calling skill.

## The 4-pass analysis

### Pass 1. Niche split

Bucket every item by which of the 3 niches it targeted. Calculate hit rate per niche. If one niche converts 2x better than the others, that is pattern #1: **niche signal**.

### Pass 2. Past Self alignment

Check each item against the Past Self bucket. Did it lean on a specific case study, identity, or lived experience? Or was it generic?

If past-self-aligned items convert better, that is pattern #2: **past self color matters**. If the rates match, the operator is probably using past self as a signature line, not in the hook itself. That is also a finding.

### Pass 3. Hook variation

Bucket items by opening line / hook type:
- Cold pattern interrupt (specific personal observation)
- Credibility-led (case study first)
- Problem-stated (you have X pain)
- Question-led (open with a question)
- Social proof (mutual connection or community mention)

The highest-rate hook goes into the patterns. Operator doubles down on it next week.

### Pass 4. Friction surfacing

For partial-engagement items (read but no reply, opened but not booked, call held but not closed), look for the common friction:
- Pitch was too soon after intro
- Offer was unclear (vague pricing or scope)
- The "what next" was missing
- Case study did not match the niche pitched into

Top 1-2 frictions become pattern #3 if they are clearly costing replies.

## Output format

Return JSON-shaped structure:

```
{
  "niche_signal": {
    "best_niche": "Niche A name",
    "best_rate": "12% reply",
    "worst_niche": "Niche C name",
    "worst_rate": "2% reply",
    "verdict": "Niche A converts 6x better. Lean week 2 sends here."
  },
  "past_self_alignment": {
    "aligned_rate": "9%",
    "generic_rate": "3%",
    "verdict": "Past-self color triples reply rate. Add specific past credentials to every send."
  },
  "best_hook": {
    "type": "Credibility-led",
    "rate": "11%",
    "example": "actual line from the data",
    "verdict": "Open with the case study. Drop the question-led hooks."
  },
  "top_friction": {
    "issue": "Pitch too soon after intro",
    "evidence": "5 of 7 partial-engaged messages had a pitch in message 1",
    "fix": "Push pitch to message 2. Message 1 is rapport only."
  }
}
```

The calling skill turns this into the operator-facing retro doc.

## Anti-pattern to flag

If the sample is too small (under 10 items for messages, under 5 for posts, under 3 for calls), do not force patterns. Return: "Sample size too small. No meaningful pattern. Operator should keep sending and re-run after the next batch." False patterns on small data drive bad pivots.

## When this skill is done

Structured pattern output returned. Calling skill takes it from there.
