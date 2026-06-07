# The Jynlab Stack

This folder is your operating workspace for the next 6 months. Pre-Program through Month 6 all run from inside this folder. You open it once, install Claude Code, and you're ready.

---

## What you need before you start

1. **A Claude Max subscription.** Claude Code runs on Claude Max ($100/mo plan is enough to start). Sign up at [claude.ai](https://claude.ai) → Settings → Subscription.
2. **30 to 45 minutes for first-run setup.** One sitting. You never do this setup again.

---

## Install in 3 steps

### Step 1. Install a code editor that runs Claude Code

Pick one. They all work.

- **Antigravity** (Google's free editor). Download at [antigravity.google](https://antigravity.google).
- **VS Code** with the Claude Code extension.
- **Cursor** with the Claude Code extension.

If you're new, use Antigravity. It's the simplest path.

### Step 2. Open this folder in your editor

1. Click **File → Open Folder**.
2. Select the unzipped `Jynlab/` folder you got from jynlab.com/classroom
3. The editor opens the folder. You see `CLAUDE.md`, `README.md`, and the empty subfolders (`calls/`, `outreach/`, `proposals/`, `retros/`, `marketing/`, `temp/`) in the file tree.

Now install the Claude Code extension inside your editor:

1. Open the **Extensions** panel.
2. Search for `Claude Code`.
3. Install the one published by **Anthropic**.
4. A Claude Code panel appears in the right sidebar with a sign-in button. Click it and sign in with your Claude Max account.

When you see a `>` prompt in the Claude Code panel, you're ready for Step 3.

### Step 3. Start Pre-Program

Go to jynlab.com/classroom and watch the 9 Pre-Program lessons. No file outputs in Pre-Program. Concepts only. You finish the mental model in 1-2 sittings, then start Month 1 Day 1.

Month 1 Day 2 is where `business.md` gets written. That is your single strategy file. Everything from Day 3 onward reads from it.

---

## What's in this folder

```
Jynlab/
├── CLAUDE.md                  ← your agent brain (read first)
├── README.md                  ← this file
├── business.md                ← (created Day 2) your single strategy file
├── .claude/skills/            ← pre-installed Skills
├── calls/                     ← call recordings + transcripts
├── proposals/                 ← sent proposals
├── outreach/                  ← apify pipeline config (cold email path)
├── marketing/posts/           ← drafted community posts
├── retros/                    ← weekly + monthly retros
└── temp/                      ← scratch + scrape JSON
```

Jynlab CRM Sheet lives separately in Google Sheets, not in this folder. Cold email lives in Instantly. Both linked from `business.md` (## Numbers right now section) once you set them up.

---

## Two patterns inside the Jynlab

**Pre-Program is concept only.** Watch the 9 videos. No file outputs. Just the mental model.

**Month 1+ work uses Skills.** Reusable procedures pre-installed in `.claude/skills/`. You invoke them by typing "Use the X skill." Skills make sense for work you repeat weekly (outreach, retros, etc.). The Day 2 cards bring `business.md` into existence; from Day 3 onward, every Skill reads sections of `business.md` and writes back to it.

Skills shipped here (14 total): `business`, `setup`, `apify-pipeline-setup`, `cold-sequence-writer`, `past-self-pattern`, `message-retro`, `community-post-retro`, `calls-retro`, `proposal-retro`, `cold-email-retro`, `month-1-retro-decide`, `outreach-specialist`, `website-specialist`, `youtube-specialist`.

Other Month 1 tasks (niche selection, case studies, profile, message templates, community finder, sales skeleton, lifestyle audit, offer builder, CRM audit) ship as **inline prompts inside each Day card**. You copy the paste block from the card and drop it into Claude Code directly. No skill abstraction needed.

Each platform lesson tells you which skill to invoke.

---

## "I only see four files in Finder"

That's normal. Your Mac hides any file or folder that starts with a dot (`.claude/`, `.gitignore`). They're all there and your editor reads them fine.

You also see the empty placeholder folders (`calls/`, `proposals/`, etc). Those are real. They fill in as Skills run.

---

## Updating the kit later

When the Jynlab ships a new version of the Starter Kit, you'll see a banner on the platform.

1. Download the fresh `jynlab-stack.zip`.
2. Drag the new `.claude/skills/` folder into your existing workspace, replacing the old one.
3. **Keep your own `CLAUDE.md` (with your edits at top), `business.md`, and everything else you produced.** Only `.claude/skills/` changes between versions.

---

## If you're stuck

1. Ask Claude Code in plain English. That's the whole point.
2. Re-read the lesson on the platform.
3. Post in #threads on the platform with your numbers attached. The Jynlab helps operators who execute.

Ship first. Data second. Opinions never before data.

Jynlab
