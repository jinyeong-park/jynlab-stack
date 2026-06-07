---
name: outreach-specialist
description: Build your cold outreach agent. A web dashboard that scrapes leads via Apify, loads them into Instantly, launches 5-step email sequences with A/B testing, and shows AI-powered performance insights. One dashboard. One button. The agent sends for you.
argument-hint: "[optional: 'setup' for first build, 'scrape' for new batch, 'analyze' for insights]"
user-invocable: true
---

# Cold Outreach Agent: your automated outreach dashboard

**Purpose:** Build a web-based outreach agent that runs your entire cold email pipeline from one dashboard. Scrape leads, write sequences, load to Instantly, launch campaigns, analyze results. No manual email writing. No spreadsheet tracking. One page controls everything.

**What the agent does:**
- Scrapes 100+ leads per batch via Apify (Apollo database, 300M+ B2B contacts)
- Loads leads into Instantly via API with one button click
- Runs a 5-step email sequence over 14 days with A/B testing on Step 1
- Shows AI-powered insights after each batch (subject line, body, targeting, list quality diagnostics)
- Tracks performance vs targets (Open >40%, Reply >3%, Bounce <2%)
- Displays full lead list with step status and engagement data

**Required:** Apify MCP, Instantly MCP, Supabase MCP. Platform must be a Next.js app (or equivalent web framework).

## What you build

### 1. Admin dashboard page (`/admin/outreach`)

One page that controls the entire outreach operation:

**Scrape section:**
- "Scrape 100 leads" button that calls Apify Apollo actor
- Filters: job title, company size, country, industry
- Results auto-save to Supabase `cold_campaign_batches` table
- Shows lead count, personal vs company email breakdown

**Sequence viewer:**
- 5 clickable steps showing full email content
- Step 1 has A/B test variant tabs (Variant A / Variant B)
- Day 0, 3, 6, 9, 13 send schedule visible
- Emails read from `cold_campaign_config` Supabase table (editable)

**Launch control:**
- Daily send limit selector (10/20/30/40/50 per account per day)
- "Load to Instantly" button (transfers leads from Supabase to Instantly via API)
- "Launch Campaign" button (activates the Instantly campaign)
- 3-step flow: scrape → load → launch

**14-day timeline:**
- Visual timeline showing which days emails go out
- Current day highlighted

**Campaign history:**
- Date-sorted batch records
- Lead count, open %, reply %, changes made, status per batch
- Clickable for detailed view

**AI Insight panel:**
- Auto-generated after each batch completes its first week
- 4 diagnostic cards: Subject line analysis, Email body analysis, Target audience fit, List quality score
- Next batch recommendation based on what worked and what didn't

**Performance vs targets:**
- Open rate gauge (target >40%)
- Reply rate gauge (target >3%)
- Bounce rate gauge (target <2%)
- Color-coded: green (hit), amber (close), red (miss)

**Lead list table:**
- Airtable-style table with columns: email, first name, last name, company, type (personal/company), current step, step status, dates
- Sortable and filterable

### 2. API routes (3 endpoints)

**`/api/outreach/scrape-leads`**
- Calls Apify `x_guru/Leads-Scraper-apollo-zoominfo` actor
- Input: job title keywords, company size range, country, industry
- Filters personal emails first (higher deliverability)
- Saves to Supabase `cold_campaign_batches` table
- Returns lead count and email type breakdown

**`/api/outreach/load-instantly`**
- Reads leads from Supabase for the current batch
- Sends each lead to Instantly API v2 one at a time
- Maps fields: email, first_name, last_name, company_name
- Updates Supabase lead status to "loaded"

**`/api/outreach/activate-campaign`**
- Activates the Instantly campaign via API
- Updates Supabase batch status to "active"
- Logs activation timestamp

### 3. Supabase tables (2 tables)

**`cold_campaign_config`**
- Campaign settings: sender accounts, daily limit, sequence content
- 5-step email sequence stored as JSON
- Step 1 A/B variants stored separately
- Editable from the dashboard

**`cold_campaign_batches`**
- Per-batch records: date, search query, lead count, filters used
- Performance metrics: open rate, reply rate, bounce rate
- Changes made (what was different from previous batch)
- AI insight JSON (generated after first week of data)
- Status: draft / loaded / active / completed

### 4. Email sequence structure

| Step | Day | Purpose |
|---|---|---|
| 1A/1B | 0 | A/B test. Pain point hook + CTA to free resource. Two subject line variants. |
| 2 | 3 | Social proof. Student results. Specific numbers. |
| 3 | 6 | Honest question. "Are you building, or still deciding what to build?" |
| 4 | 9 | The simplest version. 4 steps anyone can follow today. |
| 5 | 13 | Breakup. Final touch. Free resource + YouTube link. No pressure. |

**Email writing rules:**
- Read business.md for niche, offer, voice, enemy
- Read `.claude/rules/humanizer.md` for banned words
- Under 100 words per email
- Subject lines under 6 words
- No em dashes, no Tier 1/2 banned words
- Personalization via {{firstName}} and {{companyName}} variables
- Pain point from business.md enemy section

### 5. Automation (optional, post-build)

- Daily unsubscribe checker via Gmail MCP or webhook
- Auto-remove bounced emails from future batches
- Inbound reply webhook to flag positive responses

## The build flow (for students)

```
Step 1: Create the 2 Supabase tables (cold_campaign_config, cold_campaign_batches)
Step 2: Write the 5-step email sequence based on business.md
Step 3: Build the 3 API routes
Step 4: Build the admin dashboard page
Step 5: Connect Instantly (API key in env)
Step 6: Connect Apify (API key in env)
Step 7: Run first scrape → Load → Launch
Step 8: Wait 7 days → Read AI Insight → Adjust → Scrape next batch
```

**Claude Code builds all of this for you.** You describe what you want. Claude reads this skill file and builds the dashboard, the routes, the tables, and the sequence. You review, approve, and launch.

## The daily workflow (after build)

```
Morning (5 min):
  Open /admin/outreach
  Check AI Insight from yesterday
  Check reply rate vs target
  If replies came in → respond (use /close-deal prep-call for anyone who wants a call)

Weekly (15 min):
  Review campaign history
  Read AI Insight recommendations
  Scrape next 100 leads with adjusted filters
  Load → Launch new batch
  
Monthly:
  Review all batches
  Identify best-performing subject line and sequence
  Update cold_campaign_config with winning version
  Scale daily send limit if metrics are green
```

## Self-check before finishing

1. Dashboard page loads at /admin/outreach
2. Scrape button calls Apify and saves to Supabase
3. Load button transfers leads to Instantly
4. Launch button activates the campaign
5. 5-step sequence is visible and matches business.md voice
6. Step 1 has A/B test variants
7. AI Insight panel shows after first batch data comes in
8. Performance vs targets gauges are color-coded
9. Lead list table shows all leads with status
10. Campaign history shows batch records
11. No em dashes in any email content
12. No Tier 1/2 banned words in any email content
13. All emails under 100 words
14. Subject lines under 6 words

## Reference library

| File | When to load |
|---|---|
| [references/01-dashboard-build-guide.md](references/01-dashboard-build-guide.md) | During initial build. Component structure, API route code patterns, Supabase schema. |
| [references/02-email-sequence-templates.md](references/02-email-sequence-templates.md) | When writing the 5-step sequence. Template examples across 5 niches. A/B test patterns. |
| [references/03-apify-scrape-recipes.md](references/03-apify-scrape-recipes.md) | When configuring the scrape. Actor input schemas, filter options, cost per lead. |

## Change log

| Date | Changes |
|---|---|
| 2026-04-10 | v1: Cold Outreach Agent. Dashboard-based system replacing CLI outreach-engine. Web dashboard at /admin/outreach with scrape, load, launch flow. 5-step sequence with A/B testing. AI Insight panel. Supabase storage. Instantly API integration. |
