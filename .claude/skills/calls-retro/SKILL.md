---
name: calls-retro
description: Runs a structured retrospective on the operator's first batch of sales calls (typically 2-8 calls held by Day 16). Reads call notes from calls/, invokes past-self-pattern internally, identifies where calls fell off using the BS-WISP frame, and writes a 1-page retro to retros/calls-retro-day-16.md naming the 2 changes for week 3. Use on Day 16 of Month 1, or whenever the operator says "run a calls retro" or "review my sales calls."
---

# Calls Retro

By Day 16 the operator has held 2-8 sales calls. Today they look back to find the 1-2 changes that close more of next week's calls.

## What to do

1. Read `business.md ## Past Self`, `business.md ## Niches`, `business.md ## Offers` (6 offers from Day 13), and the `calls/` folder (recordings, transcripts, or notes).
2. Confirm 2+ calls held with notes or recordings. Under 2, stop. Operator keeps prospecting and re-runs when they have at least 2.
3. Walk through each call using the BS-WISP frame to find where it fell off.
4. Invoke `past-self-pattern` with the batch.
5. Save to `retros/calls-retro-day-16.md`.

## The BS-WISP frame

Sales skeleton from `business.md ## Sales Skeleton` (Day 4.3):
- **B.** Build rapport (open)
- **S.** Set the agenda
- **W.** What is the situation? (current state)
- **I.** What is the implication? (cost of the problem)
- **S.** What is the solution? (your offer)
- **P.** Price + next step

For each call, identify the stage where it stopped converting:
- Bad rapport (nervous, talked too fast, did not listen)
- Skipped agenda (buyer felt pitched before ready)
- Thin Situation (did not ask enough about current state)
- Missing Implication (did not show cost of doing nothing)
- Unclear Solution (offer vague, mismatched niche, or mispriced)
- Stalled Price (hedged, did not name the price or next step)

## Phases

### Phase 1. Inventory the calls (5 min)
Per call: niche (A/B/C), source (DM / community / inner circle / proposal-led), outcome (closed / proposal sent / follow-up / dead), drop stage.

### Phase 2. Pattern across calls (5 min)
Invoke `past-self-pattern`. Plus look at: most common drop stage, niche split, source split.

### Phase 3. Replay the worst call together (10 min)
Pick the call that fell off earliest. Walk through stage by stage. Operator names what they would say differently. This is the deepest learning of the day.

### Phase 4. Pick 2 changes (3 min)
Common shifts:
- Add 2 minutes of rapport at the open
- Always explicitly set the agenda
- Cut Situation discovery time in half
- Add an Implication question to every call
- Always name the price out loud, never email it

Imperative one-liners.

### Phase 5. Save (1 min)

## Output file format

Save to `retros/calls-retro-day-16.md`:

```markdown
# Calls retro · Day 16

Date: [today]
Calls held: [N]
Closed: [C]
Proposals sent: [P]
Follow-ups scheduled: [F]
Dead: [D]

## Inventory

| # | Niche | Source | Outcome | Drop stage |
|---|---|---|---|---|
| 1 | A | DM | Proposal sent | . |
| ...

## Pattern
[Most common drop stage]
[Best niche by close rate]
[Best source by close rate]
[Past-self alignment effect on rapport]

## Replay of [call ID]
[Operator's reflection on what went wrong + what they would do differently]

## The 2 changes for week 3
1. [Change one. imperative]
2. [Change two. imperative]
```

## Worked example

Day 16. 4 calls held. 1 closed (Niche A, Tier V $8.5K). 1 proposal pending. 1 dead on Implication (Niche B). 1 follow-up scheduled (Niche A, drop stage was Price stalled. operator said "let me email you the proposal").

Pattern: 2 of 4 calls died late stage (Implication or Price). Niche A is the right focus. DM-sourced and community-sourced close similarly.

Replay of call 4: operator got nervous when asked "what does it cost?" and deflected. Fix: rehearse the Tier V price out loud 5x before each call.

The 2 changes for week 3:
1. Always say the price out loud on the call. No "let me email it." Practice 5x before each call.
2. Add an Implication question every call. "What is this costing you per month not solving it?"

Saved to `retros/calls-retro-day-16.md`.

## Anti-pattern to flag

Operators want to scrap the offer or pivot the niche after one bad call. Push back: "We do not pivot offer or niche after 4 calls. We fix the drop stage. Calls fix themselves with reps. Pivots happen at Month 1 retro."

Also flag: operator skipped recording. Without recordings or notes, the retro is guesswork. Tell them to set up Fathom or Fireflies (Day 4.4) and re-run with real data next week.

## When this skill is done

`retros/calls-retro-day-16.md` saved with 2 imperative changes for week 3.
