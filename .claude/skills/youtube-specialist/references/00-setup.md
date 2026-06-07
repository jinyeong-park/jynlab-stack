# Step 0: one-time local setup

**When to load this reference:** the student runs `/youtube setup` in the Claude Code panel (before their first video) or the `/youtube cut-edit` step fails because `ffmpeg`, Python 3.10+, or the Deepgram API key is missing.

**Purpose:** install the three things Mission 2 did not install. `ffmpeg` (video tool), Python 3.10 or newer (runs the retake-detection script), and a free Deepgram API key (word-level transcription). You run the shell commands yourself via the Bash tool. The student never opens a terminal, never reads Homebrew docs, never copies a pip command. They just answer questions one at a time.

**Runs once per machine.** After the first successful run, `/youtube cut-edit` just works. Do not re-run unless the cut-edit step tells the student to.

## Input

- `$ARGUMENTS`: (empty)
- Read `./.env` (append a `DEEPGRAM_API_KEY` line at the end)
- Run shell commands via the Bash tool (brew, apt, pip, python, ffmpeg)

---

## Step 1: Confirm the student is inside the starter kit

Before touching anything, verify the student is in the agent-founders starter kit folder, not a random directory.

1. Check `./CLAUDE.md` exists.
2. Check `./.claude/skills/youtube/` exists.
3. Check `./.env` exists (it should, from `/setup`).

If any fails, stop and say:
> "I don't see your Agent Founders starter kit here. Open the starter kit folder in Antigravity (File → Open Folder), then run /youtube-setup again."

Do not create any of these files. They should already be there.

---

## Step 2: Detect the operating system

Run:

```bash
uname -s
```

- `Darwin` → macOS. Install path: Homebrew.
- `Linux` → Linux. Install path: apt / dnf / pacman depending on distro (run `cat /etc/os-release` to find out).
- `MINGW*` / `MSYS*` / Windows → Windows. Tell the student: "On Windows, ffmpeg installs from [ffmpeg.org/download.html](https://ffmpeg.org/download.html) and Python from [python.org/downloads](https://python.org/downloads). I'll open those pages for you and walk through each step. Ready?"

Do not hardcode behavior. Detect first, then branch.

---

## Step 3: Install ffmpeg

### 3.1 Check if ffmpeg is already installed

```bash
ffmpeg -version
```

If you see a version number, say:
> "ffmpeg is already installed. Moving on."

Move to Step 4.

### 3.2 Install ffmpeg if missing

**macOS:** check for Homebrew first.

```bash
brew --version
```

If Homebrew is missing, install it:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

This takes 1 to 2 minutes and asks for the student's password. Tell the student:
> "I'm installing Homebrew (the package manager) so I can install ffmpeg. It'll ask for your Mac password in a second. That's normal. Type it in and press enter."

When Homebrew is installed, install ffmpeg:

```bash
brew install ffmpeg
```

This can take 3 to 5 minutes. While it runs, tell the student:
> "Installing ffmpeg. This usually takes 3 to 5 minutes because it has a lot of dependencies. Grab water."

**Linux (apt-based):**

```bash
sudo apt-get update && sudo apt-get install -y ffmpeg
```

**Windows:** walk the student through the [ffmpeg.org](https://ffmpeg.org/download.html) Windows build. Tell them to download the "full" build from the gyan.dev link, unzip it to `C:\ffmpeg`, and add `C:\ffmpeg\bin` to their PATH. Offer to check each step.

### 3.3 Verify

After the install finishes, run:

```bash
ffmpeg -version
```

If you see a version number, say:
> "ffmpeg installed. Next: Python."

If the command still fails, ask the student to close and reopen the Claude Code panel (which reloads the shell PATH) and run `/youtube-setup` again.

---

## Step 4: Install or verify Python 3.10+

### 4.1 Check current Python

Try both `python3` and `python`:

```bash
python3 --version 2>/dev/null || python --version 2>/dev/null
```

Parse the version number. If it is `3.10` or higher, say:
> "Python 3.10+ is already installed. Moving on."

Move to Step 5.

### 4.2 Install Python if missing or too old

**macOS (Homebrew is already installed from Step 3):**

```bash
brew install python@3.12
```

**Linux (apt):**

```bash
sudo apt-get install -y python3.12 python3-pip
```

**Windows:** walk the student through the [python.org/downloads](https://python.org/downloads) installer. Key instruction: **check "Add Python to PATH"** on the first screen of the installer. If they miss this, they have to rerun the installer.

### 4.3 Install the Python packages the cut-edit script needs

The `/youtube cut-edit` step calls a local Python script (`auto_detect_retakes.py`) that uses a few libraries. Install them:

```bash
python3 -m pip install --upgrade pip
python3 -m pip install deepgram-sdk pydub numpy
```

If pip fails with a "permission denied" error, retry with `--user`:

```bash
python3 -m pip install --user deepgram-sdk pydub numpy
```

### 4.4 Verify

Run:

```bash
python3 -c "import deepgram; import pydub; import numpy; print('all good')"
```

If you see `all good`, say:
> "Python and its libraries are ready. Last step: your Deepgram key."

If an import fails, the install did not take effect. Close and reopen the Claude Code panel, then rerun `/youtube-setup`.

---

## Step 5: Collect the Deepgram API key

Deepgram is a free-tier speech-to-text service. The free tier gives every new account $200 in credits, which is enough for hundreds of YouTube videos. No credit card required.

Tell the student:
> "Last step. Go to [console.deepgram.com/signup](https://console.deepgram.com/signup), create a free account with your email, and once you're signed in you'll land on a page called 'API Keys'. Click 'Create a New API Key', copy the key (it starts with a long random string), and paste it back here."

Wait for the student to paste the key.

When you receive it:

1. Validate the shape. Deepgram keys are long hex-like strings. If the student pastes something that is clearly not a key (`"yes"`, `"ok"`, a URL), ask again: "That doesn't look like a Deepgram key. Open [console.deepgram.com](https://console.deepgram.com), click API Keys, create one, and paste the whole string."

2. Append (or update) `DEEPGRAM_API_KEY=<the-key>` in `./.env`. If the variable already exists, replace its value. Do not echo the key back to the student in your reply.

3. Confirm:
> "Deepgram key saved."

---

## Step 6: Final sanity check

Run all 3 checks. Each must pass before declaring `/youtube-setup` complete.

```bash
# ffmpeg
ffmpeg -version | head -1

# python 3.10+
python3 --version

# python deepgram library
python3 -c "import deepgram; print('deepgram sdk ok')"
```

Also check that `DEEPGRAM_API_KEY` in `./.env` is not empty:

```bash
grep "^DEEPGRAM_API_KEY=" .env
```

If all 4 pass, send the completion message:

```
/youtube-setup complete.

Your machine is ready for the cut-edit step:
- ffmpeg installed
- Python 3.10+ with deepgram, pydub, numpy
- Deepgram API key saved

Next time you run /youtube cut-edit, everything just works. You never
run /youtube-setup again.

Back to the mission: /youtube research to pick your topic, then
/youtube outline to structure it, then /youtube script to write it.
```

---

## Handling edge cases

**Homebrew install asks for sudo password:** that is normal. Tell the student "type your Mac password when it asks, press enter, and wait."

**Homebrew install fails on Apple Silicon (M-series):** make sure the student is running Terminal natively (not under Rosetta). If they are not sure, tell them to right-click Terminal in Applications → Get Info → uncheck "Open using Rosetta," then reopen Terminal and rerun `/youtube-setup`.

**brew install ffmpeg takes forever:** it can. ffmpeg has ~40 dependencies. Tell the student: "Still going. ffmpeg is a big install. First time is slow, every time after is instant. Grab water."

**Python 3 is old (3.9, 3.8):** Mac system Python is stuck at 3.9. That's why we install `python@3.12` via Homebrew. If the student's PATH resolves `python3` to the old system one, tell them to open a new terminal tab (Homebrew's paths load on shell startup) and rerun the Python check.

**pip install fails with "externally-managed-environment":** this happens on newer Homebrew Pythons and Debian 12+. Install with `--break-system-packages` as a fallback, or create a virtualenv in `./.venv` and activate it before running the `pip install`. Venv is the cleaner option.

**Deepgram says "free tier exhausted":** the student probably ran the setup twice with the same account. Tell them their key still works, the free credits were just used in testing. Continue.

**Windows student:** be extra patient. Walk through each installer screen. On the Python installer, the big trap is missing the "Add Python to PATH" checkbox. If they miss it, the fastest fix is to rerun the installer and pick "Modify" → check the box.

---

## Conversation style rules

1. One action at a time. Never run two installs in parallel.
2. Explain what you're doing right before you do it, in one sentence. "Installing Homebrew now. Will ask for your password."
3. Never read out or repeat a key the student pastes, even redacted.
4. Keep status messages short: "ffmpeg: done. Next: Python." No lectures.
5. If something fails, stop and fix THAT thing. Do not try to continue past a broken install.
6. Never tell the student to open a terminal and type a command. You run the commands. They watch and answer questions.
7. Never use em dashes in messages to the student. Periods, commas, or parentheses.
8. If the student asks "what is ffmpeg?" or "what is pip?" answer in one sentence and redirect. "ffmpeg is the tool that cuts video files. pip is Python's package installer. Moving on."

---

## Self-check before finishing

1. `ffmpeg -version` returns a real version number.
2. `python3 --version` is 3.10 or higher.
3. `python3 -c "import deepgram"` runs without error.
4. `./.env` contains a non-empty `DEEPGRAM_API_KEY`.
5. The student received the "youtube-setup complete" message.
6. No broken state: no half-finished Homebrew install, no missing Python lib.

---

## Change log

| Date | Changes |
|---|---|
| 2026-04-11 | v1: Initial skill. One-time install of ffmpeg, Python 3.10+, and Deepgram API key for the `/youtube cut-edit` step. Wraps Homebrew / apt / Windows installers in natural-language delegation so the student never sees a shell command. |
