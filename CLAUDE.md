# Your Jynlab workspace

This file is your AI agent team's brain. Claude Code reads it every time you open this folder. It already knows the AI Jynlab system. You fill in the parts that are yours.

## Who you are

<!-- Replace this block with one paragraph about YOU. Example below. -->

> I'm {{your name}}, based in {{city}}. I'm building {{one sentence about your business or the one you want to build}}. My background is {{one line}}. I've already {{what you've tried, if anything}}.

**Why this block matters.** Claude uses this every session to stay on-voice and give advice that fits your situation. Update it any time your business changes.

## What you're building

<!-- This fills in across Day 2 of Month 1. -->

- **Past Self bucket:** \_\_\_ (Day 2 produces this in `business.md` ## Past Self)
- **3 niches to test:** \_\_\_ (Day 2 produces this in `business.md` ## Niches)
- **Shape:** \_\_\_ (Day 2 confirms; default Agency)
- **Hypothesis (this week):** \_\_\_ (Day 7 onward; updated every Sunday)

## The program shape

The AI Challenge is 6 months. Pre-Program first, then 6 monthly Loops.

**Pre-Program** is concept only. 9 lessons. No file outputs. AI Learning Addiction, 4 Shapes, Past Self method, Execution Flywheel, TCD (Traffic / Conversion / Delivery), Anchors, Daily public post, 6-month map, Jynlab rules. You watch the 9 videos before Month 1 Day 1.

**Month 1 (Execution Genesis).** 30-day daily roadmap. First paying client by Day 28. Day 2 is where `business.md` gets written. Every Skill from Day 3 onward reads and writes sections of `business.md`.

**Months 2-6.** Productize Scale, Content Economy, Ads Volume, Recurring Revenue, Scale to $30K/mo.

Each lesson on the platform tells you which Skill to run. You type "Use the X skill." Claude takes over.

## Two patterns: inline prompts and Skills

Most Day cards ship the prompt inline. You read the card, copy the paste block at the bottom, paste it into Claude Code. Claude follows the prompt. No skill install required. The prompt is right there in front of you, transparent and edit-able.

Skills are reserved for work that benefits from a separate procedure file:

- Retros that fire multiple times across the month and need a consistent frame
- Multi-tool technical setup (Apify pipeline, Instantly sequence load)
- Specialist bundles (cold outreach, websites)
- Internal helpers called by other Skills

The 14 Skills shipped in this folder:

**Day 2 master compile**

- `business` (Day 2.6) → writes most of `business.md` after the inline Past Self / niche / case-study / profile prompts have filled their sections

**Retros (consistent frame across the month)**

- `message-retro` (Day 10 / 17 / 24) → reads Jynlab CRM Sheet, writes `retros/message-retro-week-N.md`, appends 1 line to `business.md` ## Patterns
- `community-post-retro` (Day 11 / 18)
- `calls-retro` (Day 16)
- `proposal-retro` (Day 23)
- `cold-email-retro` (Day 28)
- `month-1-retro-decide` (Day 30) → writes `retros/month-1.md` + Scale / Pivot / Kill to `business.md` ## Month 1 Decision

**Cold email path (technical multi-tool)**

- `apify-pipeline-setup` (Day 8) → writes `outreach/apify-pipeline.md`
- `cold-sequence-writer` (Day 16, Day 29) → loads sequences into Instantly, writes strategy note to `business.md` ## Cold Email

**Internal helper (invoked by other Skills, not directly by you)**

- `past-self-pattern` → returns structured pattern data to retro Skills

**Specialists (multi-file bundles)**

- `outreach-specialist` → cold email + DM sequences, Apify scrape, Instantly send
- `website-specialist` → one-page agency site to Vercel in 15 minutes
- `youtube-specialist` → YouTube production pipeline (research, script, edit, publish)

**One-time setup**

- `setup` → walks you through `.env` configuration on Day 1

Everything else (niche selection, case studies, profile, message templates, community search, sales skeleton, lifestyle audit, offer builder, CRM audit) is an inline prompt on its Day card. Copy, paste, answer. Same result, fewer abstractions.

## Folder layout

You start with this skeleton. Skills fill in the files as you go.

```
Jynlab/
├── CLAUDE.md                  ← this file, your agent brain
├── README.md                  ← getting-started guide
├── business.md                ← (created Day 2) your single strategy file
├── .claude/
│   ├── settings.json
│   └── skills/                ← pre-installed Skills
├── outreach/                  ← apify pipeline config only
├── marketing/posts/           ← drafted community posts
├── calls/                     ← call recordings + transcripts (Day 4 onward)
├── proposals/                 ← sent proposals
├── retros/                    ← weekly + monthly retros
└── temp/                      ← scrape JSON, scratch
```

Empty folders ship with a `.gitkeep` so the structure is visible from Day 1.

`business.md` does not exist on Day 1. Day 2's `mine-past-self` Skill creates it and writes the first two sections. The rest of Day 2 fills it out. Every Skill from Day 3 onward reads sections from `business.md` and writes back to it.

## Rules Claude must follow when writing for you

### Voice

- First person. I, not we.
- Short sentences. Then long ones. Mix the rhythm.
- State opinions directly. Don't hedge.
- Never sound like AI. See the humanizer rule below.

### Humanizer rule (non-negotiable)

No em dashes. No "delve", "tapestry", "landscape", "robust", "testament", "pivotal", "nuanced", "meticulous", "seamless", "vibrant", "holistic", "foster", "harness", "unlock the power of". No "In today's fast-paced world". No "It's worth noting that". No "Let's dive in".

Write like you're talking to a smart friend over coffee, not giving a TED talk.

### Formatting

- Headings use sentence case. Not Title Case.
- Bold is for emphasis on ONE phrase per paragraph. Not every key term.
- Bullet lists under 5 items. Longer lists get sub-headings.
- No decorative emojis. Save emojis for genuine reactions in conversation.

## MCP servers you may use

These plug into Claude Code so Skills can pull data directly.

| Server    | What it does                        | Where it shows up                       |
| --------- | ----------------------------------- | --------------------------------------- |
| Apify     | Web scraping                        | Day 8 pipeline, Day 10/12/14/25 batches |
| Instantly | Cold email campaigns                | Day 21 launch, Day 28 retro             |
| Cal       | Booking calls with leads            | Day 1 setup                             |
| Stripe    | Charging clients                    | After your first close                  |
| Gmail     | Warm-network DMs by email           | Daily, Day 4 onward                     |
| Supabase  | Platform integration (later months) | Month 4+                                |

You don't need all of these on Day 1. The Pre-Program setup walks you through the essentials.

Jynlab CRM Sheet lives in Google Sheets, not via MCP. You log Send 10 manually each day. Five columns: Name, Channel, Status, Follow-up date, Revenue.

## What to do first

1. Open this folder in your code editor (Antigravity, VS Code, Cursor, anything that runs Claude Code).
2. Open the Claude Code panel.
3. Sign in to Claude Code with your Anthropic account.
4. Read `README.md` for the install + first-run flow.
5. Go to the platform, watch the 9 Pre-Program videos. No file outputs. Concept only.
6. Start Month 1 Day 1. Day 2 is where `business.md` gets written.

That's the start. Every other lesson tells you which Skill to run next.

---

**If you're stuck, the rule is simple: don't ask "should I do A or B" before you've tried anything. Ship the thing. Bring the numbers. Then we have something real to look at.**
