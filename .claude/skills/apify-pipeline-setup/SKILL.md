---
name: apify-pipeline-setup
description: Walks the operator through a working Apify scrape + email enrichment pipeline tied to one of their 3 niches. Reads business.md ## Niches, picks a fitting Apify actor, runs a 100-lead test, verifies columns, adds enrichment if needed, and writes the working configuration to outreach/apify-pipeline.md so Day 10, 12, 14, and 25 scrapes are 10-minute reruns. Use on Day 8 of Month 1 (cold email path), or whenever the operator says "set up my Apify pipeline" or "build the scrape config for cold email."
---

# Apify Pipeline Setup

The operator took the cold email path on Day 1. Today you set up a working scrape + enrichment pipeline tied to one of their 3 niches. The same config gets reused on Day 10, 12, 14, and 25 to scrape 1,000 leads per batch. 90 minutes today saves 20+ hours over Month 1.

## What to do

1. Read `business.md ## Niches`. If missing, stop and tell them to finish Day 2 first.
2. Confirm cold email path. Ask if they set up a sending mailbox on Day 1. If they skipped Day 1 task 3, tell them to skim today's lesson for context but skip the build. Send them back to inner-circle expansion or community work.
3. Pick the strongest of the 3 niches. Usually the one with the cleanest sub-type definition (clear tool, clear price band, clear size).
4. Walk through the 5 pipeline steps. Operator does each step. Confirm each before moving on.
5. Save the working configuration to `outreach/apify-pipeline.md`.

## The pipeline (5 steps)

### Step 1. Sign up and find an actor (15 min)

Operator signs up for Apify (Squad discount in Library, Discounts page).

Then in Apify Store, search for an actor that fits their niche source. Common sources:
- LinkedIn Sales Navigator (if they have a paid Sales Nav seat)
- Google Maps (good for local-business niches like dentists, plumbers, gyms)
- Apollo (broad B2B database)
- Google Search results (custom URL list)
- Platform-specific scrapers (Skool, Substack, YouTube, Reddit)

Suggest 2-3 candidate actors based on their niche. Operator picks one.

### Step 2. Read the input schema first (5 min)

Run `fetch-actor-details` on it before calling. Walk through each input field. Confirm the operator can fill in inputs that target their niche (job title, location, company size, keyword).

### Step 3. Test scrape, 100 leads (15 min)

Operator runs it themselves so they see the cost meter and output format.

Verify the output has at minimum: first name, last name, company name, LinkedIn URL or company URL, email if the actor returns it. Missing any of those means messages cannot send. Pick a different actor.

### Step 4. Add email enrichment if needed (15 min)

If the actor does not return emails, chain an enrichment actor:
- Anymailfinder (~$0.01 per email, high accuracy)
- Icypeas (similar price, alternative)
- Apollo's enrichment endpoint (if they have a seat)

Apify supports actor chains. Scrape output flows into enrichment as input. Confirm enriched output has emails on 70%+ of rows. Under 70% means the source list is too obscure and the niche needs a different lead source.

### Step 5. Save the test output (5 min)

Save the 100-lead test as JSON in `~/Squad/temp/`. Naming: `YYYY-MM-DD_test-100-leads_[niche].json`.

Open it. Check 5 random rows. Real names? Real companies? Plausible emails?

## Output file format

Save to `outreach/apify-pipeline.md`:

```markdown
# Apify pipeline · [Niche A name]

Source: Apify Store, [actor name]
Actor URL: [link]
Cost per 1,000 leads: $[amount]

## Input schema (locked for this niche)

```json
{
  "field1": "value1",
  "field2": "value2"
}
```

## Enrichment

Chained actor: [Anymailfinder / Icypeas / none]
Email hit rate on test: [X]%

## Output columns verified
- first_name
- last_name
- company
- linkedin_url
- email

## Test result

100 leads scraped on [date]. Saved at `temp/YYYY-MM-DD_test-100-leads.json`. 5 rows spot-checked.

## Reuse plan

- Day 10 batch 1: 1,000 leads, same input schema
- Day 12 batch 2: same
- Day 14 batch 3: same
- Day 25 batch 4: same

Total: 4,000 leads in [niche] for cold email starting Day 21.
```

## Worked example

Niche: solo bookkeepers in US/Canada using QuickBooks Online, $300-$800 per client, 5-15 clients.

LinkedIn Sales Navigator scraper picked (operator had a Sales Nav seat). Filters: title = "bookkeeper" OR "owner bookkeeper", location = US + Canada, company size = 1-10. Test scrape returned 100 leads, no emails. Chained Anymailfinder, 78% hit rate (above the 70% threshold). Saved JSON to `temp/2026-XX-XX_test-100-leads_qbo-bookkeepers.json`. Spot-checked 5 rows, all real bookkeepers in QBO niche.

Day 10 the operator runs the same input schema at 1,000 leads in 10 minutes.

## Anti-pattern to flag

Operators try to scrape generic lists ("CEOs in San Francisco" or "founders in tech"). That is not a niche. Push back: "Your niche is solo bookkeepers using QBO. The input schema needs to filter on bookkeeping job titles AND QBO mention. If you cannot filter that tightly, the niche statement in `business.md ## Niches` is too loose. Go back and tighten it." A list that is not niche-aligned wastes the cold email budget for the rest of the month.

## When this skill is done

`outreach/apify-pipeline.md` saved with working configuration. 100-lead test JSON in `temp/`. Operator is ready for Day 10 to run the first 1,000-lead batch in 10 minutes.
