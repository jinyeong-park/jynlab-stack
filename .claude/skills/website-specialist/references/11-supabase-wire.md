# 11 · Supabase wiring (auth + lead capture)

The form submits to the operator's own Supabase. Their database, their RLS policies, their service-role key. No third-party CRM in the middle.

## Why Supabase

- Postgres under the hood. SQL the operator owns.
- Auth, storage, realtime built in (for later).
- Free tier covers a reasonable lead funnel.
- Portable. The schema works on any Postgres.

## Project create

1. Go to https://supabase.com/dashboard
2. New project. Pick a region close to the operator's audience.
3. Name: `<operator-slug>` (e.g. `executionsquad`)
4. Database password: generate strong, save in 1Password / operator's vault
5. Wait 90 seconds for provisioning

Once provisioned, copy these from Settings → API:

- `Project URL` → goes into `NEXT_PUBLIC_SUPABASE_URL`
- `anon public` key → goes into `NEXT_PUBLIC_SUPABASE_ANON_KEY`
- `service_role` key → goes into `SUPABASE_SERVICE_ROLE_KEY` (never expose to browser)

Add to `.env.local` and Vercel env vars (see `10-vercel-deploy.md`).

## Install client libraries

```bash
npm install @supabase/supabase-js @supabase/ssr
```

## Schema: `newsletter_contacts` table

Run this in Supabase SQL Editor:

```sql
create table newsletter_contacts (
  id uuid default gen_random_uuid() primary key,
  email text not null unique,
  first_name text,
  source text default 'landing-page',
  tags text[] default array[]::text[],
  subscribed boolean default true,
  created_at timestamp with time zone default now(),
  updated_at timestamp with time zone default now()
);

create index newsletter_contacts_email_idx on newsletter_contacts(email);
create index newsletter_contacts_source_idx on newsletter_contacts(source);

-- RLS
alter table newsletter_contacts enable row level security;

-- No public read (visitors don't see other visitors)
-- No public write (only API route writes)
-- Service role bypasses RLS, used by the API route
create policy "service role only"
  on newsletter_contacts
  for all
  using (false);

-- Auto-update updated_at
create or replace function update_updated_at()
returns trigger as $$
begin
  new.updated_at = now();
  return new;
end;
$$ language plpgsql;

create trigger newsletter_contacts_updated_at
  before update on newsletter_contacts
  for each row execute function update_updated_at();
```

That is the full schema. One table. Indexed on email and source. RLS locked to service role only. Trigger for `updated_at`.

## Supabase clients (admin only)

The lead-capture API route uses the admin (service role) client. No browser-side Supabase needed for the basic funnel.

### `src/lib/supabase/admin.ts`

```ts
import { createClient } from "@supabase/supabase-js";

export function createAdminClient() {
  const url = process.env.NEXT_PUBLIC_SUPABASE_URL;
  const serviceRole = process.env.SUPABASE_SERVICE_ROLE_KEY;

  if (!url || !serviceRole) {
    throw new Error("Missing Supabase env vars");
  }

  return createClient(url, serviceRole, {
    auth: {
      autoRefreshToken: false,
      persistSession: false,
    },
  });
}
```

The admin client bypasses RLS. Only use it in server code (API routes, server actions, webhooks).

## API route: `/api/newsletter/subscribe`

The squeeze form posts here.

### `src/app/api/newsletter/subscribe/route.ts`

```ts
import { createAdminClient } from "@/lib/supabase/admin";
import { sendWelcomeEmail } from "@/lib/resend";
import { NextRequest, NextResponse } from "next/server";

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { email, name, source } = body;

    if (!email || typeof email !== "string") {
      return NextResponse.json({ error: "Email is required." }, { status: 400 });
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const normalizedEmail = email.toLowerCase().trim();
    if (!emailRegex.test(normalizedEmail)) {
      return NextResponse.json({ error: "Invalid email address." }, { status: 400 });
    }

    const supabase = createAdminClient();
    const sourceTag = typeof source === "string" ? source : "landing-page";

    // Upsert (insert or update if email exists)
    const { data: existing } = await supabase
      .from("newsletter_contacts")
      .select("id, subscribed, tags")
      .eq("email", normalizedEmail)
      .single();

    if (existing) {
      const currentTags: string[] = existing.tags || [];
      const nextTags = currentTags.includes(sourceTag)
        ? currentTags
        : [...currentTags, sourceTag];

      const updateData: Record<string, unknown> = {
        subscribed: true,
        tags: nextTags,
      };
      if (name) updateData.first_name = name;

      await supabase
        .from("newsletter_contacts")
        .update(updateData)
        .eq("id", existing.id);
    } else {
      const { error } = await supabase.from("newsletter_contacts").insert({
        email: normalizedEmail,
        first_name: name || null,
        subscribed: true,
        source: sourceTag,
        tags: [sourceTag],
      });

      if (error) {
        console.error("Supabase insert error:", error);
        return NextResponse.json(
          { error: "Something went wrong. Try again." },
          { status: 500 },
        );
      }
    }

    // Fire welcome email (Resend handles it). Don't block on failure.
    try {
      await sendWelcomeEmail(normalizedEmail, name || null);
    } catch (err) {
      console.error("Resend send failed:", err);
      // Operator can manually re-send from the admin if needed.
    }

    return NextResponse.json({ success: true, resubscribed: !!existing });
  } catch {
    return NextResponse.json({ error: "Invalid request." }, { status: 400 });
  }
}
```

This route:
1. Validates the email
2. Upserts to `newsletter_contacts`
3. Calls `sendWelcomeEmail` (see `12-resend-wire.md`)
4. Returns `{ success: true }` or an error

## Form on the squeeze page

The form posts to `/api/newsletter/subscribe`:

```tsx
"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export function NewsletterForm({ source = "squeeze" }: { source?: string }) {
  const [email, setEmail] = useState("");
  const [status, setStatus] = useState<"idle" | "loading" | "error">("idle");
  const [message, setMessage] = useState("");
  const router = useRouter();

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (!email) return;
    setStatus("loading");

    try {
      const res = await fetch("/api/newsletter/subscribe", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, source }),
      });

      if (res.ok) {
        router.push(`/?subscribed=1&email=${encodeURIComponent(email)}`);
      } else {
        const data = await res.json();
        setStatus("error");
        setMessage(data.error || "Something went wrong.");
      }
    } catch {
      setStatus("error");
      setMessage("Something went wrong. Try again.");
    }
  }

  return (
    <form onSubmit={handleSubmit} className="mx-auto flex max-w-md flex-col gap-3">
      <input
        name="email"
        type="email"
        placeholder="Your email"
        required
        value={email}
        onChange={e => setEmail(e.target.value)}
        className="h-12 rounded-full border border-zinc-800 bg-black px-5 text-white placeholder:text-zinc-500"
        disabled={status === "loading"}
      />
      <button
        type="submit"
        className="h-12 rounded-full px-6 text-white"
        style={{ backgroundColor: "#DB011C", fontWeight: 500 }}
        disabled={status === "loading"}
      >
        {status === "loading" ? "Sending..." : "Get the [lead magnet] →"}
      </button>
      <p className="text-center text-xs text-zinc-500">
        Click to get [the lead magnet] and follow-up emails. Unsubscribe anytime.
      </p>
      {status === "error" && (
        <p className="text-center text-sm text-red-400">{message}</p>
      )}
    </form>
  );
}
```

## Optional: tagging with date for cohort analysis

When multiple lead-magnet variants exist, tag with date and source for later analysis:

```ts
const today = new Date().toISOString().slice(0, 10); // "2026-04-25"
const newTags = [...currentTags, sourceTag, today];
```

The operator can later query `select * from newsletter_contacts where '2026-04-25' = any(tags)` for cohort splits.

## Verifying the wiring

After deploy, test the funnel:

1. Visit `/squeeze`
2. Submit a real test email
3. Check Supabase dashboard → Table Editor → `newsletter_contacts`. The new row should appear within 2 seconds.
4. Confirm the welcome email arrives (see `12-resend-wire.md`).
5. Resubmit the same email. The row should update, not duplicate.

## Admin querying

The operator can query their leads in Supabase SQL Editor:

```sql
-- All leads from the squeeze page in the last 7 days
select email, first_name, source, created_at
from newsletter_contacts
where source = 'squeeze'
  and created_at > now() - interval '7 days'
order by created_at desc;

-- Lead count by source
select source, count(*) as count
from newsletter_contacts
where subscribed = true
group by source
order by count desc;

-- Active vs unsubscribed
select subscribed, count(*) as count
from newsletter_contacts
group by subscribed;
```

## Unsubscribe handling

The welcome email (and any follow-up email) must include an unsubscribe link. Pattern:

```
https://<domain>.com/unsubscribe?email=<encoded-email>&token=<hmac>
```

Build a tiny `/unsubscribe` route that validates the HMAC and updates `subscribed = false`:

```ts
// src/app/unsubscribe/route.ts
import { createAdminClient } from "@/lib/supabase/admin";
import { NextRequest, NextResponse } from "next/server";
import crypto from "crypto";

export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url);
  const email = searchParams.get("email");
  const token = searchParams.get("token");

  if (!email || !token) {
    return new Response("Invalid link", { status: 400 });
  }

  const secret = process.env.UNSUBSCRIBE_SECRET!;
  const expected = crypto
    .createHmac("sha256", secret)
    .update(email)
    .digest("hex");

  if (token !== expected) {
    return new Response("Invalid link", { status: 400 });
  }

  const supabase = createAdminClient();
  await supabase
    .from("newsletter_contacts")
    .update({ subscribed: false })
    .eq("email", email.toLowerCase().trim());

  return new Response("Unsubscribed. You will not get more emails from us.", {
    status: 200,
  });
}
```

Add `UNSUBSCRIBE_SECRET` (any random 32-byte hex string) to env vars. Use the same secret to generate the token in the welcome email template.

## Don'ts

- **Do not store passwords in `newsletter_contacts`.** This is a lead list. Use Supabase Auth for any login.
- **Do not skip RLS.** Even on a single table, RLS is the safety net.
- **Do not expose the service role key in browser code.** Service role bypasses RLS. If it leaks, anyone can read or write the entire database.
- **Do not blast `/api/newsletter/subscribe` without rate limiting.** Add Vercel's `@vercel/edge-config` or Upstash for rate limit if traffic gets real.

## Common mistakes

**Insert fails with "permission denied".** RLS is on but no policy allows the write. The fix: the API route uses the service-role admin client, which bypasses RLS. Confirm `createAdminClient()` is imported, not the regular `createClient()`.

**Email duplicates appear.** The unique constraint on `email` should prevent this. If you see duplicates, check the SQL ran successfully.

**`first_name` is null even though I sent it.** The form does not collect first name in this minimal pattern. Add an optional `<input name="firstName">` to the form, post it, and the API route stores it.
