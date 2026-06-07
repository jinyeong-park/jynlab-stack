---
name: setup
description: One-time Day 1 setup. Personalizes the shipped CLAUDE.md with the operator's info, collects 7 API keys one at a time (Perplexity, Apify, Instantly, Supabase, YouTube, Gmail, Cal), writes them into .env, fills placeholders in .claude/settings.json, and tells the operator to reload the Claude Code panel. Stripe gets added later when the first client pays. Use on Day 1 of Month 1, or whenever the operator says "run setup", "wire my API keys", or "configure my .env".
argument-hint: "(no arguments)"
user-invocable: true
---

# Setup: your workspace in 45 minutes

Walk the operator through Day 1 setup in one interactive session. They already installed Antigravity (or VS Code / Cursor), the Claude Code extension, signed in with their Claude Max account, and opened the unzipped starter kit folder. This skill runs inside that Claude Code panel.

The operator never memorizes commands or sees jargon. They never touch `.env`, `.claude/settings.json`, or a terminal. You read and edit those files for them using your normal file tools. Every message is plain English. Every question is one at a time.

## Input

- `$ARGUMENTS`: (empty)
- Working directory is the unzipped starter kit root. Already contains `CLAUDE.md`, `README.md`, `.env.example`, `.gitignore`, and a `.claude/` folder with `settings.json` and `skills/`.
- You read and rewrite `./CLAUDE.md`, `./.env`, and `./.claude/settings.json`.

---

## Step 1: Verify the operator is in the starter kit folder

Confirm the 3 files the kit ships are all present:

1. `./CLAUDE.md` exists.
2. `./.claude/settings.json` exists.
3. `./.claude/skills/` has at least 4 subfolders (`setup`, `business`, `outreach-specialist`, `youtube`).

If all 3 are present, move on silently. Do not announce "all checks passed". The operator does not need to hear this.

If any is missing, stop:
> "I don't see the starter kit files here. You probably opened the wrong folder. Click File → Open Folder and select the unzipped `agent-founders-starter-kit` folder. Then run /setup again."

Do not try to create missing files. The kit is the source of truth.

---

## Step 2: Personalize CLAUDE.md

The shipped `CLAUDE.md` has a "Who you are" section with 5 placeholders in `{{double curly braces}}`. Read the file, ask 5 questions one at a time, rewrite with the operator's answers.

### 2.1 Read CLAUDE.md and find placeholders

Locate this sentence shape:

> I'm {{your name}}, based in {{city}}. I'm building {{one sentence about your business or the one you want to build}}. My background is {{one line}}. I've already {{what you've tried, if anything}}.

If no `{{...}}` placeholders remain, the operator already personalized this. Skip to Step 3.

### 2.2 Ask 5 questions, one at a time

Wait for each answer. Never two questions in one message. Never summarize back.

1. "What's your first name?"
2. "What city are you in? Country is fine if you'd rather not share city."
3. "One sentence on what you're building, or what you want to build. 'Not sure yet' is valid."
4. "One line on your background. What were you doing before this?"
5. "Have you tried anything already? One line. 'Nothing yet' is valid."

### 2.3 Rewrite CLAUDE.md in place

Replace only the "Who you are" paragraph. Touch nothing else. The mission list, rules, MCP table, voice guide all stay exactly as shipped.

After rewriting:
> "CLAUDE.md personalized. Moving on to your API keys."

---

## Step 3: Collect 7 API keys and wire them in

The kit ships with `.claude/settings.json` pre-configured for 7 MCP servers. Each has a placeholder like `YOUR_PERPLEXITY_KEY`. You:

1. Ask the operator for each key, one at a time, with a direct link to where they create it.
2. Write the value into `./.env` under the matching variable name (create from `./.env.example` if missing).
3. Replace the matching placeholder in `./.claude/settings.json`.
4. Confirm briefly: "perplexity: connected. Next: apify."

The operator never sees the JSON or .env files. They see you asking one question at a time.

### 3.1 Order and prompts

Install in this order: Perplexity → Apify → Instantly → Supabase → YouTube → Gmail → Cal.com. Stripe is NOT installed here.

| # | Server | Prompt |
|---|---|---|
| 1 | Perplexity | "First one: open [perplexity.ai/settings/api](https://www.perplexity.ai/settings/api), create a new key, paste it here. Starts with `pplx-`." |
| 2 | Apify | "Open [console.apify.com/account/integrations](https://console.apify.com/account/integrations), copy your Personal API token, paste it here. Starts with `apify_api_`." |
| 3 | Instantly | "Open [app.instantly.ai/app/settings/integrations](https://app.instantly.ai/app/settings/integrations), generate an API key, paste it here." |
| 4 | Supabase | "Create a free project at [supabase.com/dashboard](https://supabase.com/dashboard) if needed. In Project Settings → API, copy your project URL and paste it here first." (then: "Good. Now copy the `service_role` secret key from the same page and paste it here.") |
| 5 | YouTube | "YouTube needs a Google Cloud API key. Create it at [console.cloud.google.com/apis/credentials](https://console.cloud.google.com/apis/credentials) and paste it here." |
| 6 | Gmail | "Gmail uses Google OAuth. No key to paste. A browser pop-up will run the first time a skill sends a warm email. Type `ok` to continue." |
| 7 | Cal.com | "Last one. Open [app.cal.com/settings/developer/api-keys](https://app.cal.com/settings/developer/api-keys), create a key, paste it here." |

Never ask for multiple keys in the same message.

### 3.2 For each key, update both files

When the operator gives you a key:

1. **Append to `.env`.** Create from `.env.example` if missing. Variable names (match the shipped `.env.example` and `.claude/settings.json`):
   - Perplexity → `PERPLEXITY_API_KEY`
   - Apify → `APIFY_TOKEN`
   - Instantly → `INSTANTLY_API_KEY`
   - Supabase → `SUPABASE_URL` and `SUPABASE_SERVICE_ROLE_KEY`
   - YouTube → `YOUTUBE_API_KEY`
   - Gmail → (no variable, OAuth)
   - Cal.com → `CAL_API_KEY`

2. **Edit `./.claude/settings.json`.** Find the matching placeholder (`YOUR_PERPLEXITY_KEY`, `YOUR_APIFY_TOKEN`, etc.), replace with the real value, write back. Preserve the rest exactly.

3. **Confirm briefly.** One short sentence. `perplexity: done. next: apify.` No lectures.

4. **Move to next server.**

### 3.3 Never echo keys back

Never print an API key in full. If you want to show progress, redact: `pplx-...abc`. Security rule.

### 3.4 If a key looks malformed

Perplexity should start with `pplx-`, Apify with `apify_api_`. If a key fails the pattern:
> "That doesn't look like the right format for `<service>`. Double-check you copied the whole key and try again."

Wait for a corrected key before writing.

---

## Step 4: Tell the operator to reload the Claude Code panel

The MCP servers are configured but the extension only reads `.claude/settings.json` when the panel starts.

> "All 7 API keys saved. Now reload the Claude Code panel so it picks them up. At the top of the panel there's a refresh or restart button (the circular arrow icon). Click it. Or close the panel and reopen it from the right sidebar. Once it reloads, your 7 MCP servers are live."

Wait for confirmation.

---

## Step 5: Quick verification

After confirmation, run a light sanity check. Ask:

> "Try typing: `use Perplexity to tell me one surprising stat about the AI services market in 2026`. If you get a real answer with sources, Perplexity is working."

If it works:
> "Perplexity is live. Your 6 other servers are wired the same way. They activate the first time a skill uses them. No need to test each one now."

If Perplexity fails:
1. Confirm they reloaded.
2. Have them re-paste the key.
3. Re-edit `.claude/settings.json` and tell them to reload again.

Do not spiral. If broken after 3 tries:
> "Let's skip the live test. Your settings file is configured. We'll catch any issue when `/business` actually uses Perplexity. Moving on."

---

## Step 6: Setup complete message

When Step 5 passes (or is skipped with a note), print:

```
Setup complete.

Your workspace is ready. You have:
- Claude Code with your Claude Max subscription signed in
- Starter kit unzipped and open
- CLAUDE.md personalized with your details
- 7 MCP servers configured: perplexity, apify, instantly, supabase, youtube, gmail, cal
  (Stripe gets added later when your first client pays)

Next: Day 2. Build your business.md.
Type /business right here in the Claude Code panel.

Shut up and continue.
```

---

## Handling edge cases

**Operator opened the wrong folder** (CLAUDE.md or .claude/settings.json missing): stop at Step 1. Do NOT create files. Send them back to File → Open Folder and run /setup again.

**Operator already personalized CLAUDE.md** (no `{{...}}` remain): skip Step 2.

**Operator already has `.env` with some keys** (they ran /setup once and aborted): read `.env` first. For each variable with a value, skip and move on. For empty ones, ask.

**Invalid key**: catch the malformed format (see 3.4) and re-ask. Don't write garbage.

**No Supabase account**: walk them through signup at [supabase.com/dashboard](https://supabase.com/dashboard) → New Project → wait 2 minutes → Project Settings → API. Then continue.

**"Can I skip Instantly / Supabase / YouTube / Cal for now?"**: yes. Leave the placeholder. Tell them: "Noted. You can add `<server>` any time by running /setup again, or by opening `.env` and pasting the key yourself."

**Asks about Stripe**: "Stripe is not part of Day 1. You add it when you close your first paying client. No revenue yet means no reason to connect Stripe."

**Wants to add other MCP servers today** (Notion, Linear, Airtable, Vercel, Figma): push back. "You only add an MCP server when a specific skill requires it. Day 1 requires these 7. Nothing else until a later skill asks for it."

**Beginner questions mid-setup** ("what does Apify actually do?"): answer in 1-2 sentences and redirect: "Short answer: `<one line>`. Right now let's finish the install. Next up: `<thing>`."

---

## Conversation style rules

1. One question at a time. Never two in one message.
2. Keep confirmations short. `perplexity: done. next: apify.` No lectures.
3. Never summarize what the operator said back to them. Move on.
4. No sycophantic language. No "Great!" or "Perfect!" Just "OK" or silent confirmation.
5. No em dashes. Use periods, commas, or parentheses.
6. If anything breaks, stop and fix THAT thing before moving on.
7. When the operator gets distracted, answer in one sentence and redirect to the current step.
8. Never tell the operator the names of files you edited. Just say "Perplexity connected."
9. Never show a raw API key in your reply, even redacted. Keys live only inside the files.
10. Never suggest installing Node.js, running `npm install`, opening a terminal, or typing a shell command. None of that is part of this flow.

---

## Self-check before declaring setup complete

1. `./CLAUDE.md` exists, no `{{...}}` placeholders remain, "Your 5 missions" and "Rules Claude must follow" sections still intact.
2. `./.env` exists with the values the operator provided (minimum: Perplexity, Apify, Supabase URL + service role, Instantly, YouTube, Cal.com; Gmail is OAuth).
3. `./.claude/settings.json` no longer contains any `YOUR_*` placeholder strings for servers the operator filled in.
4. Operator confirmed they reloaded the Claude Code panel.
5. At least one live test returned a real MCP-powered answer (or the test was skipped with a note).
6. Operator has read the "Setup complete" message.
7. No broken state: no half-written JSON, no unanswered questions from Step 2.

---

## Change log

| Date | Changes |
|---|---|
| 2026-04-08 | v1: Installed MCP servers via `claude mcp add` CLI and wrote CLAUDE.md from scratch. |
| 2026-04-11 | v2: Rewritten for the Starter Kit flow. Personalizes shipped CLAUDE.md placeholders. |
| 2026-04-11 | v3: Rewritten for Antigravity + Claude Code extension. No CLI references. MCPs wired by editing `.claude/settings.json` and `.env` directly via file tools. Operator never sees terminal or JSON. Adds reload step and `/setup` resumability. |
