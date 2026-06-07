# Apify scrape recipes

**When to load**: When configuring the lead scraping step of the cold outreach agent. Contains the exact Apify actor setup, input schemas, and filter configurations.

---

## Primary actor: `x_guru/Leads-Scraper-apollo-zoominfo`

This is the actor Chris uses. It connects to a 300M+ B2B database (Apollo/ZoomInfo aggregated data).

### Why this actor

- 300M+ business profiles with emails
- Filters by job title, company size, location, industry
- Returns personal AND company emails (personal preferred for cold outreach)
- Fast: ~30 seconds for 100-300 profiles
- Cost: check current pricing on Apify (typically $5-15 per 1,000 leads)

### Input schema (what to configure)

```json
{
  "max_results": 300,
  "job_titles": [
    "AI developer",
    "AI consultant", 
    "AI freelancer",
    "prompt engineer",
    "AI engineer",
    "chatbot developer",
    "AI agency owner",
    "automation developer"
  ],
  "employee_size": ["1-10", "11-50"],
  "person_location_country": [
    "United States",
    "United Kingdom", 
    "Canada",
    "Australia",
    "Germany"
  ],
  "email_status": "all",
  "include_emails": true,
  "include_phones": false
}
```

### Key parameters explained

**max_results**: Request 3x your target. If you want 100 qualified leads with emails, request 300. Many profiles lack valid emails.

**job_titles**: Pull from business.md ICP section. These should match the exact job titles your ideal client uses on LinkedIn.

**employee_size**: For solo founder / small agency niches, use "1-10" and "11-50". For mid-market, add "51-200". Never go above 500 for AI service businesses unless your offer specifically targets enterprise.

**person_location_country**: Start with English-speaking countries. Add others based on your niche geography.

**include_emails**: Must be true. This is the whole point.

**include_phones**: Set false to reduce cost and data noise.

### Output fields

The actor returns an array of objects. Key fields:

```
first_name: string
last_name: string
emails: Array<{address: string, type: string}>
personal_emails: string[]
work_email: string
title: string
company_name: string
linkedin_url: string
location: string
```

### Email extraction logic (from Chris's implementation)

```
1. Collect all emails from: emails[], personal_emails[], work_email
2. Filter for valid format (contains "@")
3. Deduplicate against existing leads in Supabase
4. Prefer personal emails (check against personal domain list)
5. If no personal email, use work email
6. If no email at all, skip the lead
```

**Personal domain list** (use to identify personal vs company emails):
gmail.com, yahoo.com, hotmail.com, outlook.com, protonmail.com, icloud.com, aol.com, live.com, me.com, mail.com, ymail.com, gmx.com, googlemail.com

**Why prefer personal emails**: higher deliverability. Company emails go through spam filters, IT firewalls, and shared inboxes. Personal emails land directly in the founder's inbox.

---

## Alternative actors by niche

### Local businesses (dental, restaurant, fitness, real estate)

**Actor**: `compass/crawler-google-places`

```json
{
  "searchStrings": ["dentist in Austin TX", "dental clinic Austin"],
  "maxCrawledPlacesPerSearch": 100,
  "language": "en",
  "maxReviews": 0,
  "includeWebResults": true
}
```

Returns: business name, address, phone, website, rating, review count, Google Maps URL.

**Note**: Google Maps does not return emails directly. You need a second step: scrape the website for contact emails, or use an email enrichment actor.

**Cost**: ~$4 per 1,000 places scraped.

### LinkedIn profiles (B2B decision makers)

**Actor**: `harvestapi/linkedin-profile-scraper`

```json
{
  "profileUrls": ["https://www.linkedin.com/in/username"],
  "maxProfiles": 50
}
```

Or search-based:
```json
{
  "searchTerms": ["AI consultant"],
  "maxProfiles": 50,
  "location": "United States"
}
```

Returns: name, headline, company, location, profile URL. Email requires enrichment.

### LinkedIn post commenters (warm-ish leads)

**Actor**: `harvestapi/linkedin-post-comments`

Scrapes commenters from a specific LinkedIn post. People who commented on a competitor's AI business post are self-identified as interested.

### Instagram profiles (DTC brands)

**Actor**: `apify/instagram-scraper`

For DTC/e-commerce niches. Scrape brand profiles to find founders.

---

## Scrape workflow (how it fits in the dashboard)

```
User presses "Scrape 100 Leads" button
  → API route calls Apify actor with configured filters
  → Polls for completion (10 sec intervals, max 5 min)
  → Extracts and deduplicates emails
  → Saves to Supabase cold_leads table
  → Creates batch record in cold_campaign_batches
  → Returns count to dashboard
  → User sees "94 leads scraped and saved"
```

---

## Customization per niche

Students replace these values based on their business.md:

| Field | Example (AI services) | Example (dental) | Example (DTC) |
|---|---|---|---|
| Actor | x_guru/Leads-Scraper | compass/crawler-google-places | apify/instagram-scraper |
| job_titles | AI developer, AI consultant | (n/a for Google Maps) | (n/a for Instagram) |
| employee_size | 1-10, 11-50 | (filter by rating/reviews) | (filter by follower count) |
| location | US, UK, CA | City-specific | (global or country) |
| Email source | Apollo database | Website scrape | Bio link scrape |

---

## Cost estimation

| Leads per batch | Apify cost (approx) | Instantly cost | Total per batch |
|---|---|---|---|
| 100 | $1-3 | $0 (included in $30/mo plan) | $1-3 |
| 500 | $5-10 | $0 | $5-10 |
| 1,000 | $10-20 | $0 | $10-20 |

At 100 leads per week for 4 weeks = $4-12/month in Apify costs. Negligible.

---

## Error handling

- **"Failed to start Apify run"**: check APIFY_TOKEN in .env.local
- **Run status FAILED/ABORTED**: actor may have hit rate limits. Wait 5 min and retry.
- **Zero leads returned**: job title keywords too narrow. Broaden or add more titles.
- **All leads are company emails**: the niche may not have many founders on personal email. Switch to LinkedIn scraper + email enrichment.
- **High duplicate rate**: you have scraped this niche before. Change the location filter or add new job titles.
