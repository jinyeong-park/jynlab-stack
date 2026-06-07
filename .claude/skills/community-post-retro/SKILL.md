---
name: community-post-retro
description: Runs a structured retrospective on the operator's last 7 days of community posts (Squad threads first, then the outside communities they joined on Day 3, plus the manually cross-posted X/LinkedIn versions). Reads marketing/posts/, invokes past-self-pattern internally, writes a 1-page retro to retros/community-post-retro-week-N.md, and names the 2 changes for next week. Use on Day 11 (week 1) and Day 18 (week 2) of Month 1, or whenever the operator says "run a post retro" or "review my community posts."
---

# Community Post Retro

Each week the operator looks back at posts shipped across Squad, the 3 outside communities, and the manual cross-posts to X/LinkedIn. Goal: find the 1-2 changes that drive more DMs and booked calls. Runs Day 11 and Day 18.

## What to do

1. Read `business.md ## Past Self`, `business.md ## Niches`, and `marketing/posts/` (calendar + drafts + ship records).
2. Confirm 5-10 posts shipped in the past 7 days. Under 5, stop and ask the operator to ship today's post first.
3. Ask the operator to paste engagement counts per post: platform, niche, hook type, likes / replies / DMs, booked calls credited to that post.
4. Invoke `past-self-pattern` with the batch.
5. Translate to a 1-page retro.
6. Save to `retros/community-post-retro-week-[N].md`.

## Phases

### Phase 1. Inventory (3 min)
List each post: platform, niche, hook type, engagement, DMs, booked calls.

### Phase 2. Patterns (3 min)
Invoke `past-self-pattern`.

### Phase 3. Plain-language readout (5 min)
- Which platform produced the most DMs (not likes. DMs are the only signal that matters)
- Which niche the winning posts spoke to
- Which hook worked
- Whether past-self color helped

### Phase 4. Booked calls vs likes (2 min)
Did any post produce a booked call? If yes, dissect what made it work. If no, note the pattern: posts have not yet driven calls. Change hook or increase frequency.

### Phase 5. Pick 2 changes (3 min)
Common shifts:
- Drop the platform that produced 0 DMs
- Double down on the winning hook type
- Speak only to the winning niche next week
- Stop tip-style content, switch to story-style

Imperative one-liners.

### Phase 6. Save (1 min)

## Output file format

Save to `retros/community-post-retro-week-[N].md`:

```markdown
# Community post retro · week [N]

Date: [today]
Posts shipped: [N]
Total likes: [X]
Total replies: [Y]
Total DMs from posts: [Z]
Booked calls from posts: [B]

## Inventory

| # | Platform | Niche | Hook type | Likes | Replies | DMs | Calls |
|---|---|---|---|---|---|---|---|
| 1 | Squad | A | Credibility | 12 | 3 | 1 | 0 |
| ...

## What worked
[Top platform by DMs]
[Top niche by DMs]
[Top hook by DMs]
[Past self alignment effect]

## What did not work
[Lowest engagement and why]
[Hooks to stop]

## The 2 changes for week [N+1]
1. [Change one. imperative]
2. [Change two. imperative]

## Frequency for next week
[N posts targeted, by platform]
```

## Worked example

Day 11. 6 posts shipped (Squad x 2, Community A x 1, Community B x 2, Community C x 1). 3 manually cross-posted to LinkedIn.

Pattern read: Most DMs from Squad (3) and Community A (1, with a call). Credibility hook beat tip-style (3 DMs vs 0). Niche A 4 DMs, Niche B 0. Tip-style posts produced 0 DMs across the board.

The 2 changes for week 2:
1. Drop tip-style posts. Switch all posts to credibility-led or story-led.
2. Stop posting in Community B. Niche wrong. Reinvest the time in Community A.

Saved to `retros/community-post-retro-week-1.md`.

## Anti-pattern to flag

Operators measure success by likes. Push back: "Likes pay nothing. DMs and booked calls are the only metrics. A post with 5 likes and 1 booked call beats 50 likes and 0."

Also do not let the operator add new platforms in week 2. Same 3 communities + Squad. Optimize, do not expand.

## When this skill is done

`retros/community-post-retro-week-[N].md` saved with 2 imperative changes.
