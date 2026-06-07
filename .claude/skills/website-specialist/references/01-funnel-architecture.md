# 01 · Funnel architecture

The 2-page funnel. Two routes, one redirect. No nav chrome. No thanks page. No popup. No third page.

## The pattern

```
Cold visitor → /squeeze → email captured → redirect to / (long-form landing)
                                                ↓
                                         VSL + offer + claim
```

That is the whole funnel. A squeeze page that does one job, and a long-form home page that does everything else. No thanks banner. No interstitial. The Resend welcome email confirms in the inbox; the landing page does the conversion work.

## Why two pages, no thanks banner

A separate `/thanks` page or post-signup banner wastes the warmest moment. The visitor just gave their email. Their attention is highest right now. Send them straight to the VSL. If they want confirmation, the email lands in their inbox within 30 seconds.

## Page 1 · `/squeeze`

One job: capture an email in exchange for the lead magnet.

### Block order (top to bottom)

| Block | Purpose | Notes |
|---|---|---|
| Hero H1 | Pain-led inversion | Two lines. Second line italic + accent. See `02-copy-blocks.md` |
| Subhead | Free + lead magnet promise | Four short clauses max. No white-highlight clutter |
| Stacked email form | Single field + button | Mobile-first. Use `stacked` prop. See `02-copy-blocks.md` for consent line |
| Visual proof | 3D hero loop or rendered video | Top black gradient only. No side or bottom vignettes |
| Senja testimonials | Social proof | Real quotes only. If operator has none, omit the block |
| Second CTA | Repeat the form | Fresh hero copy on the close, same form below |
| Footer | Minimal | Wordmark + email + city + privacy/terms |

### What to skip

- No nav bar. The page is the menu.
- No "About" or "Pricing" links.
- No multiple CTAs above the fold. One field, one button.
- No exit-intent popups. They feel cheap.

### The redirect

When the form submits successfully, push the visitor straight to `/`. No query params. No banner. The Resend welcome email (reference `12-resend-wire.md`) lands in their inbox within 30 seconds, which is the only confirmation needed.

## Page 2 · `/` (long-form landing)

Order is the persuasion. Do not reorder the sections.

### Block order

1. **Hero**: same pain-frame as squeeze, slightly longer subhead. Use the page-load entrance animation (reference `08-section-reveals.md`).
2. **VSL**: embedded video or "coming soon" placeholder until the operator records. The placeholder is a dark card with a pulsing red dot, drop date, and "We email you the moment it lands" line. See `02-copy-blocks.md` for the placeholder copy.
3. **The actual problem**: agitation block. First-person. "You" accusation. Pain-led. Pull patterns from `02-copy-blocks.md`.
4. **The roster**: character select component if the offer involves a list of N items (modules, weeks, deliverables, team members). Use `06-character-select.md`.
5. **Your pack**: lead magnet downloads if the operator's offer includes downloadable assets (agent files, PDFs, templates). Skip if the lead magnet is content-only.
6. **The offer / The commitment**: price + included items + roadmap (week-by-week if applicable) + guarantee + animated seats progress bar + claim CTA. The biggest, most detailed section on the page. See `02-copy-blocks.md` and `07-bottom-cta-bar.md`.
7. **Testimonials** . Senja embed or hand-rolled. Real quotes only.
8. **Final CTA**: pain-led close. Two-line italic title. Single claim button below. See `02-copy-blocks.md`.
9. **Footer**: same as squeeze.
10. **Sticky bottom CTA bar**: fixed component. Appears after 480px scroll. Hides when offer section enters view. See `07-bottom-cta-bar.md`.

### What to skip on `/`

- No "Features vs benefits" tables. The roster + offer block already does this.
- No FAQ accordion above the offer. Push it below testimonials only if the operator insists.
- No three-column "process" graphic. The roadmap is the process.
- No live chat widget on the home page. Operator can add it later.

## Lead magnet handling

The lead magnet is whatever the operator sells. Examples:

- An agent file (e.g. `jude.md`)
- A PDF playbook
- A 90-day roadmap as `.md`
- A video link
- A Notion template

### Delivery options

1. **Direct download from squeeze** (no email gate). Wastes the email opportunity. Avoid.
2. **Email-only delivery via Resend** (default). Lead magnet attached or linked in the welcome email. See `12-resend-wire.md`.

Default to option 2. The opt-in goes straight to the landing page; the welcome email confirms the delivery and ships the asset.

## Routes (Next.js App Router)

```
src/app/
├── layout.tsx              # root layout, global fonts + dark bg
├── page.tsx                # / (long-form landing)
├── squeeze/
│   └── page.tsx            # /squeeze (lead magnet)
└── api/
    └── newsletter/
        └── subscribe/
            └── route.ts    # POST handler
```

For agency-style sites where the operator has multiple offers, scale to:

```
src/app/
├── page.tsx                # main landing
├── squeeze/page.tsx        # one squeeze per offer
├── squeeze/[offer]/page.tsx
└── api/...
```

## URL params reference

- `/` → default landing, same view for new and returning visitors
- `/squeeze?ref=youtube` → tag the source in the form submission

## Domain pattern

- Production: bare apex (`<operator-domain>.com`) or `www`. Not both. Pick one and 301-redirect the other.
- Staging: `staging.<operator-domain>.com` or a Vercel preview URL.
- Never deploy to a `<random>.vercel.app` URL for production. Operators look like amateurs.

## Decision tree at the start of a build

```
Operator asks: "Build me a website."
├── Do they have a business.md?
│   ├── No → write it together first. Stop.
│   └── Yes → proceed
├── Do they have a lead magnet?
│   ├── No → ask what they want to give away. The squeeze needs a thing.
│   └── Yes → proceed
├── Is the offer a list of N items (modules, weeks, deliverables)?
│   ├── Yes → use character select for the roster section
│   └── No → use a list block in the offer section
├── Does the offer have a deadline or seat limit?
│   ├── Yes → use animated seats progress bar
│   └── No → skip the bar, use a simpler urgency line
└── Begin Phase 2 (copy blocks)
```

## What "ownership" means in this funnel

- The form posts to the operator's own Supabase table (`newsletter_contacts`). Not to a third-party CRM. Reference `11-supabase-wire.md`.
- The welcome email sends from the operator's own Resend account on their own verified domain. Reference `12-resend-wire.md`.
- The page lives on the operator's Vercel account. Reference `10-vercel-deploy.md`.
- The code lives in the operator's git repo. The operator can move the deploy to Railway, Cloudflare, or self-hosted in an afternoon if Vercel ever gets weird.

No piece of the funnel is rented from a third party that can shut the operator down.
