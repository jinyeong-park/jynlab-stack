# Dashboard build guide

**When to load**: When Claude Code is building the cold outreach agent dashboard for the student. Contains the exact component structure, API route patterns, and Supabase schema from Chris's working implementation.

---

## Tech stack

- Next.js 15+ (App Router)
- TypeScript
- Tailwind CSS + shadcn/ui
- Supabase (leads storage, batch tracking)
- Instantly API v2 (campaign management, lead loading)
- Apify API (lead scraping via Apollo actor)

---

## File structure

```
src/app/admin/outreach/
├── page.tsx              # Server component, fetches data, renders cold-campaign
└── cold-campaign.tsx     # Client component, the full dashboard UI

src/app/api/outreach/
├── scrape-leads/route.ts     # POST: Apify scrape → Supabase
├── load-instantly/route.ts   # POST: Supabase → Instantly API
└── activate-campaign/route.ts # POST: Activate Instantly campaign
```

---

## Supabase tables

### `newsletter_contacts` (or `cold_leads` if building fresh)

Used for storing scraped leads. Chris reused his existing newsletter_contacts table with a `source` filter.

```sql
create table cold_leads (
  id uuid primary key default gen_random_uuid(),
  email text unique not null,
  first_name text,
  last_name text,
  company text,
  title text,
  linkedin_url text,
  source text default 'cold_outreach',
  tags text[] default '{}',
  subscribed boolean default true,
  pipeline_stage text default 'new',
  created_at timestamptz default now()
);

alter table cold_leads enable row level security;

create policy "Admin full access" on cold_leads
  for all using (
    exists (select 1 from profiles where id = auth.uid() and role = 'admin')
  );
```

### `cold_campaign_batches`

Tracks each weekly scrape batch with metrics.

```sql
create table cold_campaign_batches (
  id uuid primary key default gen_random_uuid(),
  campaign_id text not null,
  campaign_name text,
  week_label text not null,
  search_terms text[] default '{}',
  cities text[] default '{}',
  leads_scraped int default 0,
  leads_loaded int default 0,
  status text default 'active',
  open_rate numeric,
  reply_rate numeric,
  bounce_rate numeric,
  changes_made text,
  ai_insight jsonb,
  created_at timestamptz default now()
);

alter table cold_campaign_batches enable row level security;

create policy "Admin full access" on cold_campaign_batches
  for all using (
    exists (select 1 from profiles where id = auth.uid() and role = 'admin')
  );
```

### `cold_campaign_config`

Stores campaign settings and the 5-step email sequence.

```sql
create table cold_campaign_config (
  id uuid primary key default gen_random_uuid(),
  campaign_id text unique not null,
  campaign_name text,
  sender_accounts text[] default '{}',
  daily_limit int default 20,
  sequence jsonb not null,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);
```

Sequence JSON schema:
```json
{
  "steps": [
    {
      "step": 1,
      "delay": 0,
      "subject": "{{firstName}}, tired of the AI treadmill?",
      "body_html": "<p>...</p>",
      "variants": 2,
      "variant_b_subject": "the tool treadmill is killing your progress",
      "variant_b_html": "<p>...</p>"
    },
    {
      "step": 2,
      "delay": 3,
      "subject": "Re: this is what actually works",
      "body_html": "<p>...</p>",
      "variants": 1
    }
  ]
}
```

---

## API route: `/api/outreach/scrape-leads`

**Method**: POST
**Input**: `{ target: number }` (default 100)
**What it does**:
1. Calls Apify `x_guru/Leads-Scraper-apollo-zoominfo` actor
2. Filters: job titles (from business.md), company size 1-50, target countries
3. Extracts emails. Prefers personal emails (gmail, yahoo, etc.) over company emails
4. Deduplicates against existing leads in Supabase
5. Saves new leads to Supabase
6. Creates a batch record in `cold_campaign_batches`

**Key implementation details**:
- Request 3x the target (e.g., 300 for 100 leads) because many profiles lack emails
- Poll Apify run status every 10 seconds, max 5 minutes
- Personal email domains list: gmail.com, yahoo.com, hotmail.com, outlook.com, protonmail.com, icloud.com, etc.
- Upsert with `onConflict: "email", ignoreDuplicates: true` to prevent duplicates

**Env vars needed**: `APIFY_TOKEN`

---

## API route: `/api/outreach/load-instantly`

**Method**: POST
**What it does**:
1. Reads all cold_outreach leads from Supabase where subscribed = true
2. Sends each lead to Instantly API v2 `/api/v2/leads` endpoint
3. Maps: email, first_name, campaign ID
4. Rate limits: 500ms pause every 10 leads
5. Returns loaded/failed counts

**Key implementation details**:
- Instantly API v2 uses Bearer token auth
- Leads are added one at a time (bulk endpoint requires higher Instantly plan)
- Campaign ID is stored in env or in cold_campaign_config table

**Env vars needed**: `INSTANTLY_API_KEY`

---

## API route: `/api/outreach/activate-campaign`

**Method**: POST
**What it does**:
1. Calls Instantly API to activate the campaign
2. Updates batch status in Supabase to "active"

---

## Dashboard component structure

The `cold-campaign.tsx` client component receives props from the server page:

```typescript
interface ColdCampaignProps {
  campaign: {
    id: string;
    name: string;
    status: string;
    steps: CampaignStep[];
    sender_accounts: string[];
    daily_limit: number;
  };
  analytics: CampaignAnalytics | null;
  weeklyBatches: WeeklyBatch[];
  leads: Lead[];
  totalLeads: number;
}
```

### UI sections (top to bottom):

1. **Header**: campaign name, status badge, total leads count
2. **Scrape section**: "Scrape 100 Leads" button with loading state and result message
3. **Sequence viewer**: 5 clickable step cards. Step 1 has A/B variant tabs. Shows subject + body preview.
4. **Launch control**: daily limit selector (dropdown), "Load to Instantly" button, "Launch Campaign" button
5. **14-day timeline**: visual dots for Day 0, 3, 6, 9, 13
6. **Performance gauges**: 3 circular progress indicators for open rate (>40%), reply rate (>3%), bounce rate (<2%)
7. **Campaign history**: table of weekly batches with metrics
8. **AI Insight panel**: 4 diagnostic cards (subject, body, audience, list quality) + next batch recommendation
9. **Lead list**: sortable/filterable table with email, name, tags, source, status, date

### Metric targets (hardcoded constants):

```typescript
const METRIC_TARGETS = {
  open_rate: { target: 40, label: "Open rate", fix: "Subject line. A/B test new variants." },
  reply_rate: { target: 3, label: "Reply rate", fix: "Email body. Message not connecting." },
  bounce_rate: { target: 2, label: "Bounce rate", fix: "List quality. Try different lead sources.", inverted: true },
};
```

---

## Server page (`page.tsx`)

The server component:
1. Fetches campaign config from `cold_campaign_config` table
2. Fetches analytics from Instantly API (or from cached Supabase data)
3. Fetches weekly batches from `cold_campaign_batches`
4. Fetches leads from `cold_leads` / `newsletter_contacts`
5. Passes all data as props to the client component

---

## Instantly setup (prerequisites for the student)

Before building the dashboard:
1. Create Instantly account ($30/mo)
2. Add 3-5 sender email accounts (buy domains, set up SPF/DKIM/DMARC)
3. Enable warmup on all accounts (wait 14 days for full warmup)
4. Create a campaign in Instantly manually (to get the campaign ID)
5. Copy API key from Instantly settings
6. Add `INSTANTLY_API_KEY` and campaign ID to `.env.local`

The dashboard automates everything AFTER this initial setup.
