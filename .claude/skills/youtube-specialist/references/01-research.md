# Viral topic research

**When to load**: Step 1 of /youtube. Find the best topic for your next video.

---

## Research workflow

### Source 1: YouTube search (YouTube MCP)

1. Search for 3-5 keywords from your business.md niche using `youtube_search`
2. Filter: last 30-90 days, sorted by view count
3. For each result: pull title, views, subscriber count, publish date
4. Calculate viral ratio: views / subscribers. Above 3x = outperformer.
5. Pull transcripts from top 3 videos using `youtube_get_transcript` to extract hook patterns

### Source 2: X/Twitter trends (Apify)

1. Search X for trending topics related to your niche using Apify Twitter scraper
2. Look for: high engagement posts, threads with 100+ likes, topics that are being debated
3. Cross-reference with YouTube: if a topic is trending on X but has few YouTube videos, that is the gap

### Source 3: YouTube search suggestions (YouTube MCP)

1. Run `youtube_search_suggestions` for 5 keywords
2. High suggestion count (5+) = active demand
3. Low count = nobody is teaching this yet. Potential gap.

## Output format

Present 5-10 topic candidates in a ranked table:

```
| # | Topic | Top video views | Channel subs | Viral ratio | Competition | Gap? |
|---|---|---|---|---|---|---|
| 1 | [topic] | [views] | [subs] | [ratio]x | Low/Med/High | Yes/No |
```

Recommend the top 3 with one-line reasoning for each.

## Title rules (apply during research)

- "Claude Code" in the first half of every title
- Under 58 characters
- Include one specific number or dollar amount
- No banned patterns ("Claude Code fires X", "Claude Code makes Y")
- Use proven patterns: "I [verb] X with Claude Code", "Claude Code + [thing] = [result]"
