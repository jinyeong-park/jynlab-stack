# 12 · Resend wiring (transactional welcome email)

The welcome email sends from the operator's own Resend account, on the operator's verified sender domain. No Mailchimp, no Kit middleman in the welcome path. Resend handles delivery, the operator owns the data.

## Why Resend

- React Email components for templating (operator's site stack already speaks this)
- Per-email send logs in the dashboard
- Free tier covers 100 emails per day, 3000 per month
- Custom domains with DKIM/SPF auto-setup
- API simple enough to wire in 10 minutes

## Account setup

1. Sign up at https://resend.com
2. Add the operator's sender domain (e.g. `mail.<operator-domain>.com` or apex)
3. Resend gives DNS records for DKIM/SPF/DMARC
4. Operator adds those at their registrar
5. Wait for verification (5 minutes to 24 hours)
6. Once green, copy the API key from the dashboard

Add to env vars:

```
RESEND_API_KEY=re_xxxxxxxxxxxx
RESEND_FROM_EMAIL=hi@<operator-domain>.com
RESEND_FROM_NAME=<Operator Brand Name>
```

In Vercel, add to Production environment.

## Install

```bash
npm install resend
npm install -D @react-email/components
```

`@react-email/components` is optional. Plain HTML templating works too. React Email gives type-safe components and live preview during development.

## File structure

```
src/lib/
└── resend.ts                  # client + send helpers

src/emails/
└── welcome.tsx                # React Email template (or .html if not using components)
```

## Resend client (`src/lib/resend.ts`)

```ts
import { Resend } from "resend";
import { WelcomeEmail } from "@/emails/welcome";
import { render } from "@react-email/render";

const resend = new Resend(process.env.RESEND_API_KEY);

const FROM_NAME = process.env.RESEND_FROM_NAME ?? "[Brand]";
const FROM_EMAIL = process.env.RESEND_FROM_EMAIL ?? "hi@example.com";

export async function sendWelcomeEmail(
  email: string,
  firstName: string | null,
) {
  const html = await render(
    WelcomeEmail({ firstName: firstName ?? "there" }),
  );

  const result = await resend.emails.send({
    from: `${FROM_NAME} <${FROM_EMAIL}>`,
    to: email,
    subject: "Your [lead magnet] is here",
    html,
    headers: {
      "List-Unsubscribe": `<https://${process.env.NEXT_PUBLIC_SITE_URL}/unsubscribe?email=${encodeURIComponent(email)}>`,
    },
  });

  if (result.error) {
    throw new Error(`Resend send failed: ${result.error.message}`);
  }

  return result.data;
}
```

The `List-Unsubscribe` header tells Gmail/Apple Mail to show a one-click unsubscribe button in the inbox. Improves trust and deliverability.

## Welcome email template (`src/emails/welcome.tsx`)

```tsx
import {
  Body,
  Container,
  Head,
  Heading,
  Html,
  Link,
  Preview,
  Section,
  Text,
} from "@react-email/components";

const ACCENT = "#DB011C"; // REPLACE: operator brand accent from business.md

export function WelcomeEmail({ firstName }: { firstName: string }) {
  return (
    <Html>
      <Head />
      <Preview>Your [lead magnet] is here.</Preview>
      <Body style={body}>
        <Container style={container}>
          <Section>
            <Heading style={h1}>Hi {firstName},</Heading>
            <Text style={text}>
              Your [lead magnet] is below. Open it on the machine you actually
              work on, not your phone. The file is small and easy to install.
            </Text>

            <Section style={cta}>
              <Link
                href={`https://${process.env.NEXT_PUBLIC_SITE_URL}/downloads/[file]`}
                style={ctaButton}
              >
                Download [lead magnet] →
              </Link>
            </Section>

            <Text style={text}>
              While you install it, watch the 8-minute walkthrough. It shows
              you exactly how I use it on my own machine.
            </Text>

            <Section style={cta}>
              <Link
                href={`https://${process.env.NEXT_PUBLIC_SITE_URL}/?utm_source=welcome-email`}
                style={ctaButtonAlt}
              >
                Watch the walkthrough →
              </Link>
            </Section>

            <Text style={text}>
              You will hear from me again soon with the next step.
            </Text>

            <Text style={text}>
              [Operator first name]
            </Text>
          </Section>

          <Section style={footer}>
            <Text style={footerText}>
              [Operator brand name]. [City, region].
            </Text>
            <Text style={footerText}>
              <Link
                href={`https://${process.env.NEXT_PUBLIC_SITE_URL}/unsubscribe`}
                style={footerLink}
              >
                Unsubscribe
              </Link>
            </Text>
          </Section>
        </Container>
      </Body>
    </Html>
  );
}

const body = {
  backgroundColor: "#0a0a0a",
  color: "#e4e4e7",
  fontFamily:
    "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
  margin: 0,
  padding: 0,
};

const container = {
  margin: "0 auto",
  padding: "40px 20px",
  maxWidth: "560px",
};

const h1 = {
  color: "#fff",
  fontSize: "24px",
  fontWeight: 500,
  lineHeight: 1.3,
  margin: "0 0 24px",
};

const text = {
  color: "#d4d4d8",
  fontSize: "16px",
  lineHeight: 1.55,
  margin: "0 0 20px",
};

const cta = {
  margin: "28px 0",
};

const ctaButton = {
  backgroundColor: ACCENT,
  borderRadius: "999px",
  color: "#fff",
  display: "inline-block",
  fontSize: "15px",
  fontWeight: 500,
  padding: "14px 28px",
  textDecoration: "none",
};

const ctaButtonAlt = {
  border: "1px solid #3f3f46",
  borderRadius: "999px",
  color: "#fff",
  display: "inline-block",
  fontSize: "14px",
  padding: "12px 24px",
  textDecoration: "none",
};

const footer = {
  borderTop: "1px solid #27272a",
  margin: "40px 0 0",
  paddingTop: "20px",
};

const footerText = {
  color: "#71717a",
  fontSize: "12px",
  lineHeight: 1.5,
  margin: "0 0 4px",
};

const footerLink = {
  color: "#71717a",
  textDecoration: "underline",
};
```

## Domain verification

This is the most common failure point. Resend requires SPF, DKIM, and DMARC records for the sender domain.

### Records Resend gives you (example)

```
Type: MX
Name: send
Value: feedback-smtp.us-east-1.amazonses.com
Priority: 10

Type: TXT
Name: send
Value: v=spf1 include:amazonses.com ~all

Type: TXT
Name: resend._domainkey
Value: p=MIGfMA0GCSq...

Type: TXT
Name: _dmarc
Value: v=DMARC1; p=none;
```

The exact records vary by Resend's region routing. Operator adds these at their registrar (Cloudflare, Namecheap, GoDaddy, etc.) exactly as Resend prints them.

Once added, click "Verify" in the Resend dashboard. Verification takes 5 to 60 minutes typically.

### Choosing the sender subdomain

Two options:

1. **Apex domain:** `hi@<operator-domain>.com`. The operator's main domain. Best for trust but commits the apex to email.
2. **Subdomain:** `hi@mail.<operator-domain>.com`. Isolates email infra from the marketing site. Recommended for most operators.

Default to the subdomain unless the operator explicitly wants apex.

## Sending broadcasts (later)

This reference covers transactional welcome only. For marketing broadcasts (the "next step" email, weekly check-ins, launch announcements), the operator can either:

- Use Resend's Broadcast feature (in dashboard) for one-off blasts
- Use ConvertKit/Kit for sequence automation (more flexible)

The standard funnel only needs Resend for the transactional welcome. Broadcasts are a phase 2 concern.

## Verifying the wiring

After deploy:

1. Submit a test email through `/squeeze`
2. Within 30 seconds, the welcome email should arrive in the inbox
3. Check Resend dashboard → Logs to confirm the send succeeded
4. Click the download CTA in the email. It should link to the lead magnet URL.
5. Click the unsubscribe link. It should hit the `/unsubscribe` route (see `11-supabase-wire.md`).

## Failure modes

**Email never arrives.** Check Resend dashboard → Logs. Most common causes:

1. Domain not verified. Click "Verify" in dashboard.
2. API key wrong or missing. Confirm `RESEND_API_KEY` is set in Vercel production env vars.
3. From email mismatch. The "from" must match the verified domain. `hi@<wrong-domain>.com` will be rejected silently.

**Email lands in spam.** Almost always means SPF/DKIM/DMARC records are wrong. Use https://www.mail-tester.com to score deliverability. Aim for 9/10 or higher.

**Email looks broken in Outlook.** Outlook does not support modern CSS. Either:

1. Use React Email components (they handle this)
2. Test in https://www.litmus.com or https://www.emailonacid.com before sending
3. Strip unsupported CSS (modern flexbox, gradients, fancy fonts)

**The from name shows as plain email.** Check `from: \`${FROM_NAME} <${FROM_EMAIL}>\`` syntax. Both name and email in the same string.

## Don'ts

- **Do not put unsubscribe at the bottom only.** Include it both in the footer link AND the `List-Unsubscribe` header.
- **Do not send marketing content from the welcome email address.** Keep transactional and marketing separate, even on the same domain. `hi@` for transactional, `news@` for marketing.
- **Do not blast unverified domains.** Resend will reject. Verify first, send second.
- **Do not skip the preview text.** The `<Preview>` component sets the inbox preview line. Without it, Gmail shows the first sentence of HTML which often reads as garbage.
- **Do not include a tracking pixel without disclosure.** Resend has open tracking off by default. Leave it off unless the operator explicitly wants opens tracked, in which case include it in the privacy policy.

## Resend cost expectation

- Free: 100 emails/day, 3,000/month
- Pro: $20/mo for 50,000/month
- Most operator funnels stay free for the first 100 leads, then upgrade

## Run report addition

After deploy, drop the email setup status in the run report at `.claude/owner-inbox/`:

```
## Resend
- API key: configured ✓
- From: <FROM_NAME> <<FROM_EMAIL>>
- Domain status: verified ✓
- Welcome email: tested, delivered in ~12 seconds
- List-Unsubscribe header: present ✓
- Mail-tester score: <X>/10
```
