---
name: proposal-retro
description: Runs a structured retrospective on the operator's proposals sent in the past 14 days. Reads PandaDoc analytics (or operator's manual notes), invokes past-self-pattern internally, identifies the page where buyers dropped off, and writes a 1-page retro to retros/proposal-retro-day-23.md naming the 2 changes for next week. Use on Day 23 of Month 1, or whenever the operator says "run a proposal retro" or "review my proposals."
---

# Proposal Retro

By Day 23 the operator has sent 1-5 proposals. Today they look at the proposal funnel to find the 1-2 changes that close more proposals next week.

If they have sent 0 proposals, the issue is upstream (no calls, or calls not converting to proposal-send). Pivot to a calls retro instead and post in Squad: "0 proposals sent by Day 23, here is what is happening upstream."

## What to do

1. Read `business.md ## Past Self`, `business.md ## Niches`, `business.md ## Offers`, and the `proposals/` folder (sent copies + PandaDoc analytics export if any).
2. Confirm 1+ proposals sent in past 14 days. If 0, switch to upstream diagnosis.
3. Pull each proposal with the operator. PandaDoc analytics or manual notes. Track: send date, buyer, time-from-call-to-send, opened or not, time spent per page, result.
4. Identify drop-off pages.
5. Invoke `past-self-pattern` with the batch.
6. Save to `retros/proposal-retro-day-23.md`.

## The 3 common drop-off issues

Most proposal "no" replies come from one of these. Diagnose which is yours.

**Price felt too high.** Buyer spent 30 seconds on the pricing page, did not sign, did not negotiate. Usually means the value frame in pages 1-5 was thin. Fix: build more value before the price.

**Scope unclear.** Buyer spent 8+ minutes on Scope of Work and bounced. Deliverables were abstract or language was wishy-washy. Fix: list scope as concrete deliverables with dates, not phases.

**Timeline unclear.** Buyer cannot picture when they get the result. Dates were missing or vague ("about 4-6 weeks"). Fix: name the exact start and end dates.

## Phases

### Phase 1. Inventory (5 min)
Per proposal: niche (A/B/C), offer tier (S or V), time from call to send, opened (yes/no), time spent per page (PandaDoc), result (signed / negotiating / silent / declined).

### Phase 2. Drop-off analysis (5 min)
Walk through each declined or silent proposal. Identify the page where the buyer left.

### Phase 3. Pattern (3 min)
Invoke `past-self-pattern`. Look at:
- Which niche has the best proposal close rate
- Which offer tier closes more (S or V)
- Whether time-from-call-to-send correlates with close rate (under 1 hour wins, usually)

### Phase 4. Pick 2 changes (3 min)
Common shifts:
- Send within 30 minutes of the call, not 2 hours later
- Add a deposit + final structure to make price feel smaller per stage
- List scope as concrete deliverables with dates
- Drop the optional Tier V add-ons that buyers did not engage with

Imperative one-liners.

### Phase 5. Save (1 min)

## Output file format

Save to `retros/proposal-retro-day-23.md`:

```markdown
# Proposal retro · Day 23

Date: [today]
Proposals sent: [N]
Opened: [O]
Signed: [S]
Negotiating: [G]
Silent: [I]
Declined: [D]

## Inventory

| # | Niche | Tier | Time-to-send | Opened | Drop page | Result |
|---|---|---|---|---|---|---|
| 1 | A | V | 25 min | yes | . | Signed |
| ...

## Drop-off pattern
[Most common drop page]
[Best close-rate niche]
[Best close-rate tier]
[Time-to-send effect]

## The 2 changes for next week
1. [Change one. imperative]
2. [Change two. imperative]
```

## Worked example

4 proposals in past 14 days. 1 signed, 1 negotiating, 2 silent. Time-to-send mattered most: 25 min won, 2-4 hours lost. Drop page was Scope (2 of 4 stalled there, wishy-washy phase language).

The 2 changes:
1. Send every proposal within 30 minutes of the call. Calendar block 45 min after every scheduled call to write and send.
2. Rewrite Scope of Work as concrete deliverables with dates ("Week 1: QBO close audit doc delivered by Friday EOD") instead of phases.

Saved to `retros/proposal-retro-day-23.md`.

## Anti-pattern to flag

Operators want to drop the price after one declined proposal. Push back: "Price felt too high is a value-frame issue, not a price issue. We do not lower the price. We raise the value built before the price page."

Also flag: operator has no PandaDoc analytics. Without per-page time data, drop-off diagnosis is guesswork. Tell them to set up PandaDoc tracking (Day 5.4 Resources) or ask buyers directly "what made you say no?" on the next call.

## When this skill is done

`retros/proposal-retro-day-23.md` saved with 2 imperative changes for next week.
