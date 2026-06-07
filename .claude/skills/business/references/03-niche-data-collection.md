# Niche data collection engine

**When to load**: Phase 2 of /business, after Socratic questions generate niche candidates. This reference contains the full scraping workflow for validating niches with real data.

---

## 3-source data collection

Pick sources based on niche type:

**Online niches** (creators, SaaS, AI services, digital): Reddit + YouTube comments are primary.
**Local niches** (dental, restaurants, real estate): Google Maps (Apify) is primary. Reddit is secondary.

### Source 1: Reddit scrape (Apify)

Run `fetch-actor-details` first to check input schema before calling any actor.

**Scraper**: `parseforge/reddit-posts-scraper` or equivalent.

**Always specify target subreddits. Global search returns noise.** If a scrape returns irrelevant posts, document the failure AND the fix in the output.

| Niche type | Target subreddits |
|---|---|
| AI services / automation | r/ClaudeAI, r/SaaS, r/EntrepreneurRideAlong, r/Entrepreneur |
| Web development / design | r/webdev, r/freelance, r/web_design |
| Marketing / ads | r/PPC, r/digital_marketing, r/marketing |
| Local business services | r/smallbusiness, r/sweatystartup |
| E-commerce | r/ecommerce, r/shopify, r/FulfillmentByAmazon |

Settings: 20-50 results from 2-3 target subreddits. Sort by top/hot.

**What to look for:**
- Posts with high upvotes showing the problem the niche solves
- Comments: frustration, confusion, "I wish someone would just do this for me"
- Price points mentioned (what people pay, what people charge)
- AI Addict signals: learning but not executing, "how do I start" for the 50th time

### Source 2: YouTube comment scraping (YouTube MCP)

**Tool**: `mcp__youtube__youtube_list_comments`

Highest-signal prospect data. Every comment expressing a pain point is a self-identified potential customer.

**How to run:**
1. Search for 2-3 competitor videos using `mcp__youtube__youtube_search` (pick videos with 50K+ views)
2. Scrape 20-30 comments per video using `mcp__youtube__youtube_list_comments`
3. Pull commenter username, comment text, like count

**What to look for:**
- AI Addict self-identification: "I need to stop procrastinating," "great tutorial, now I just need to start"
- Pain points: "I still can't figure out how to get clients"
- Fear of commoditization: "clients will expect this for $100 now"
- Content treadmill: "haven't finished the last video and you already released a new one"

**Quote real comments with usernames in the output.** Add analysis explaining why each person represents a prospect.

### Source 3: YouTube search suggestions (YouTube MCP)

**Tool**: `mcp__youtube__youtube_search_suggestions`

Run for 3 keywords per candidate niche.

**Interpretation:**
- High suggestion count (5+) = active demand
- Low suggestion count (1-2) = demand gap, nobody teaching this yet
- Compare "learning" vs "selling/getting clients" keywords. If learning has 6+ suggestions but selling has 1-2, that is the AI Addict pattern. The student fills the gap.

### Source 4: Local niche scrapers (Apify)

| Niche type | Scraper | What to pull |
|---|---|---|
| Local businesses | Google Maps scraper (Apify) | Names, addresses, websites, ratings, review counts, phones |
| E-commerce | Shopify store scraper | Store names, products, traffic estimates |
| B2B services | LinkedIn scraper | Decision-makers, company size, recent activity |

Settings: 20-50 results. Filter to target geography.

### Save scrape data

Save all raw results to `temp/{YYYY-MM-DD}_niche-prospects-{niche-keyword}.json`.

---

## Perplexity validation (3 queries)

**Query 1 (Market size + demand)**: market size, growth rate, search volume, active demand.

**Query 2 (Competitor deep dive)**: top 5-10 competitors. For each: what they sell, price point, platform, member count, core positioning, weakness. Real pricing, delivery model, tools taught, gaps.

**Query 3 (Positioning gaps)**: "What do none of these competitors offer? What complaints do their students have? Where is the gap?"

### Scoring (each dimension 1-5, total /20)

1. **Demand**: active search volume, posts about problem, community discussion. Use Reddit + YouTube suggestions.
2. **Competition**: how many competitors, pricing, platform, gap. Use Perplexity data.
3. **Willingness to pay**: do they already buy? Budget range. Use Reddit spending mentions + competitor pricing.
4. **Reachability**: can you find and contact them? YouTube, Reddit, LinkedIn, Google Maps. Use scrape results.

### Scoring bands

- 17-20: **GO.** Lock the niche.
- 13-16: **MAYBE.** Sharpen the angle (e.g., "dental clinics" → "dental clinics with under 50 Google reviews"). Re-score.
- 10-12: **WEAK.** Pivot the angle or narrow further.
- Below 10: **NO.** Go back to Phase 1 and explore a different direction.

---

## Error handling

- **Apify MCP not connected**: "Can't pull Reddit data. Connect Apify and re-run, or validate with YouTube + Perplexity only."
- **YouTube MCP not connected**: "Can't scrape competitor comments or search suggestions. Big miss for online niches. Connect and re-run, or continue with Reddit + Perplexity."
- **Both missing**: "Validating with Perplexity only. Data will be weaker. Connect at least one and re-run."
- **Perplexity MCP not connected**: "Scoring based on Reddit and YouTube data plus what I know. Scores will be less reliable."
