# 10 · Vercel deploy

The site lives on the operator's Vercel account. Their domain. Their environment variables. Their deploy history. Portable to Railway, Cloudflare Pages, or self-hosted in an afternoon if Vercel ever gets weird.

## Prerequisites

Before deploy, the operator must have:

- A Vercel account (free tier is fine for one site)
- A registered domain (or one they are about to register)
- The site's git repo pushed to GitHub, GitLab, or Bitbucket
- All env vars ready (Supabase URL + anon key, Resend API key, etc.)

## Install Vercel CLI

```bash
npm install -g vercel
vercel login
```

The CLI uses the operator's Vercel account credentials.

## First deploy (preview)

From the project root:

```bash
vercel
```

CLI prompts:

1. **Set up and deploy?** Yes
2. **Which scope?** Operator's personal scope (or team)
3. **Link to existing project?** No
4. **Project name?** Operator's brand slug (e.g. `executionsquad`)
5. **Code directory?** `./` (current directory)
6. **Override settings?** No (Next.js auto-detected)

CLI deploys, returns a preview URL like `https://<project>-<hash>.vercel.app`. Test it.

## Configure environment variables

Two ways: dashboard or CLI.

### Via CLI

```bash
vercel env add SUPABASE_URL
# CLI prompts for value, then for which environments (production / preview / development)

vercel env add SUPABASE_ANON_KEY
vercel env add SUPABASE_SERVICE_ROLE_KEY
vercel env add RESEND_API_KEY
vercel env add NEXT_PUBLIC_SITE_URL
```

Re-deploy after adding env vars:

```bash
vercel --prod
```

### Via dashboard

1. Go to https://vercel.com/<scope>/<project>/settings/environment-variables
2. Add each variable
3. Pick environments (Production, Preview, Development)
4. Save
5. Redeploy from dashboard or CLI

### Required env vars for the standard funnel

| Var | Where used | Public? |
|---|---|---|
| `NEXT_PUBLIC_SITE_URL` | Email links, redirects | Public |
| `NEXT_PUBLIC_SUPABASE_URL` | Browser Supabase client | Public |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | Browser Supabase client | Public |
| `SUPABASE_SERVICE_ROLE_KEY` | API route admin client | Server-only |
| `RESEND_API_KEY` | API route welcome email | Server-only |
| `RESEND_FROM_EMAIL` | Email "from" header | Server-only |

The `NEXT_PUBLIC_*` prefix exposes to the browser bundle. Everything else stays server-only.

## Custom domain

```bash
vercel domains add <operator-domain>.com
```

Vercel returns DNS records to add to the operator's domain registrar:

```
Type: A
Name: @
Value: 76.76.21.21

Type: CNAME
Name: www
Value: cname.vercel-dns.com
```

The operator adds these at their registrar (Cloudflare, Namecheap, GoDaddy, etc.). Propagation takes 5 minutes to 24 hours. SSL provisions automatically once DNS resolves.

### Apex vs www

Pick one. Default: bare apex (`<operator-domain>.com`) with `www` 301-redirecting to apex.

```bash
vercel domains add www.<operator-domain>.com
# In Vercel dashboard, set redirect: www.<operator-domain>.com → <operator-domain>.com (301)
```

Or the inverse: `www.<operator-domain>.com` as canonical with apex redirecting. Pick one and stick with it.

## Production deploy

Once DNS resolves and SSL is green:

```bash
vercel --prod
```

This pushes the current branch to production. Future pushes to `main` (or whatever the operator's production branch is) auto-deploy if connected to git.

### Connect git repo for auto-deploy

```bash
vercel git connect
```

Or in dashboard: Settings → Git → Connect Repository.

Once connected:
- Push to `main` → auto-deploys to production
- Push to feature branch → auto-deploys to preview URL
- Pull request → preview URL posted in PR comments

## Preview deploys

Every push to a non-production branch creates a preview URL. Use these for client review before merging:

```bash
git checkout -b feature/new-hero
git commit -am "New hero copy"
git push origin feature/new-hero
# Vercel posts preview URL in 60 seconds
```

Share the preview URL with the operator. They review. Merge when approved.

## Build settings

Defaults work for a standard Next.js 16 App Router project. If the operator has a custom setup:

- **Framework preset:** Next.js
- **Build command:** `npm run build`
- **Output directory:** `.next` (default)
- **Install command:** `npm install`
- **Node.js version:** 20.x or 22.x (current LTS)

Override in `vercel.json` at project root if needed:

```json
{
  "buildCommand": "npm run build",
  "framework": "nextjs",
  "regions": ["iad1"]
}
```

## Regions

Default region is `iad1` (Washington DC). For European or Asian audiences, change in Vercel dashboard → Settings → Functions → Regions.

For most operators: leave the default. Edge functions and ISR cover the latency gap.

## Performance verification

After production deploy:

1. Run Lighthouse on the live URL
2. Target: Performance > 85 mobile, > 95 desktop
3. Target: LCP < 2.5s mobile
4. Target: CLS < 0.1
5. Target: hero chunk < 250KB gzip

If any target misses:
- LCP over 2.5s → headline is not the LCP. Check `dynamic` import on the 3D scene with `ssr: false`.
- CLS over 0.1 → canvas wrapper missing `aspectRatio`. Fix `app/page.tsx`.
- Hero chunk over 250KB → trim Drei imports, drop the post-process pass, or fall back to poster on mobile.

## Rollback

If a production deploy breaks:

```bash
vercel rollback
```

Or via dashboard: Deployments → pick the last working deploy → "Promote to Production".

Vercel keeps the last 7 days of deploys by default. Free tier may keep less.

## Cost expectation

Free tier (Hobby plan) covers:
- 100GB bandwidth per month
- Unlimited preview deploys
- 1 production project
- Custom domain with SSL

Most operator funnels stay under 100GB unless they go viral. Pro plan ($20/mo) is for scale.

## Backup deploy targets

If Vercel becomes unfit (rare but planning matters):

### Railway

```bash
npm install -g @railway/cli
railway login
railway init
railway up
```

Same Next.js code. Different deploy. ~10 minutes to migrate.

### Cloudflare Pages

```bash
npm install -g wrangler
wrangler login
wrangler pages deploy .next/static
```

Requires Next.js export mode (limits some features). Best for fully static sites.

### Self-hosted

```bash
docker build -t op-site .
docker run -p 3000:3000 op-site
```

The operator owns the binary. Hosts on any VPS (Hetzner, DigitalOcean, OVH, AWS).

The point: the code is portable. Vercel is the default because it's the fastest. The operator can move in an afternoon if they need to.

## Don'ts

- **Do not deploy to `<random>.vercel.app` for production.** Looks amateur. Always custom domain.
- **Do not commit `.env.local` to git.** That file holds secrets. `.gitignore` handles this by default.
- **Do not put secrets in `NEXT_PUBLIC_*` vars.** They ship in the browser bundle.
- **Do not skip the rollback rehearsal.** Do one rollback test before launch so the operator knows the muscle memory.

## Common mistakes

**DNS does not resolve.** Operator added the records but they pointed to the wrong place. Check `dig <domain>.com` or `nslookup <domain>.com`. Should return `76.76.21.21` for the apex.

**SSL certificate does not provision.** Wait 30 minutes after DNS resolves. If still missing, in Vercel dashboard click "Refresh" next to the domain.

**Build fails on Vercel but works locally.** Almost always a missing env var. Check Vercel dashboard → Settings → Environment Variables. All vars must be set for `Production` environment.

**Site loads but Supabase calls fail.** `NEXT_PUBLIC_SUPABASE_URL` or `NEXT_PUBLIC_SUPABASE_ANON_KEY` not set. Add them, redeploy.

**Welcome email never sends.** Resend key missing or domain not verified. See `12-resend-wire.md` for the fix.

## Run report addition

After deploy, drop the URL and stats in the run report at `.claude/owner-inbox/`:

```
## Vercel deploy
- Production URL: https://<domain>.com
- Vercel dashboard: https://vercel.com/<scope>/<project>
- Last deploy: <timestamp>
- Lighthouse mobile: <score>/100 (LCP <X>ms, CLS <Y>)
- Hero chunk size: <X>KB gzip
```
