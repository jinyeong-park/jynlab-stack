---
name: message-retro
description: Runs a structured retrospective on the operator's last 7 days of Squad CRM Sheet outreach (DMs and replies, not cold email yet). Reads the Sheet (or pasted batch), invokes past-self-pattern internally, writes a 1-page retro to retros/message-retro-week-N.md, and names the 2 changes for next week. Use on Day 10 (week 1), Day 17 (week 2), and Day 24 (week 3) of Month 1, or whenever the operator says "run a message retro" or "review my outreach week."
---

# Message Retro

Each week the operator pauses on their sent messages to find the 1-2 changes that make next week convert better. Runs Day 10, 17, and 24 of Month 1.

## What to do

1. Read `business.md ## Past Self` and `business.md ## Niches`.
2. Pull last 7 days from the Squad CRM Sheet, or ask the operator to paste the batch.
3. Confirm at least 30 sent messages with reply / no-reply tagged. Under 30, stop and ask them to finish today's Send 10 first.
4. Invoke `past-self-pattern` with the batch.
5. Translate the patterns into a 1-page retro at 4th-grade level.
6. Save to `retros/message-retro-week-[N].md`.
7. Tell the operator the 2 changes for next week.

## Phases

### Phase 1. Confirm sample size (1 min)
Verify 30+ messages with reply state. Under, stop.

### Phase 2. Run patterns (2 min)
Invoke `past-self-pattern`. Wait for output.

### Phase 3. Read the patterns in plain words (5 min)
Walk through each. No analyst tone. Example: "Niche A got 12% reply rate. Niche C got 2%. Drop Niche C this week. Pour the saved time into Niche A."

### Phase 4. Pick 2 changes (5 min)
Two only. More dilutes focus. Common shifts:
- Move volume to the winning niche
- Switch from question hook to credibility hook
- Push the pitch from message 1 to message 2
- Add a specific past-self detail to every opener

Write them as imperative one-liners.

### Phase 5. Save (1 min)

## Output file format

Save to `retros/message-retro-week-[N].md`:

```markdown
# Message retro · week [N]

Date: [today]
Batch size: [N messages, R replies]
Reply rate overall: [X]%

## What worked
[Best niche + rate]
[Best hook + rate]
[Past self alignment: yes/no, with rate]

## What did not work
[Worst niche + rate]
[Worst hook + rate]
[Friction observed]

## The 2 changes for week [N+1]
1. [Change one. imperative]
2. [Change two. imperative]

## Open questions for next retro
[e.g., "Niche B is 4% but only 8 messages, need bigger sample"]
```

## Worked example

Day 10. 38 messages sent, 5 replies. Per-niche sample is under 15 each, so the pattern analyzer flags it as too thin for a niche breakout. Pivot to hooks + past-self alignment only.

Hooks across all 38: credibility-led 4 of 12 (33%), question-led 1 of 14 (7%), generic intro 0 of 12. 4 of 5 replies came from messages opening with a specific case study line.

The 2 changes:
1. Open every message with the Tier 1 case study line. Drop question hooks.
2. Track sends by niche this week. Need 15+ per niche for the Day 17 breakout.

Saved to `retros/message-retro-week-1.md`.

## Anti-pattern to flag

Operators rush to pivot the entire strategy after one bad week. Push back: "One week is signal, not proof. Two changes. We do not change the bucket, the case studies, or the offer. Two changes only." A 3rd change request gets the same answer. Discipline beats variety.

## When this skill is done

`retros/message-retro-week-[N].md` saved. Operator has 2 imperative changes and knows what to track next.
