# 03 · VSL script (8 minutes, 6 beats)

The VSL is the persuasion artifact. Eight minutes. Six beats. **The operator films themselves.** Higgsfield is not used here. This is talking head plus simple B-roll the operator captures with their phone or webcam.

## Why 8 minutes

Cold-traffic VSLs convert best between 5 and 9 minutes. Eight is the upper end and gives room for a real story without losing the casual scroller. Push to 12 minutes for offers over $2,000. Cut to 5 for offers under $200.

## Why filmed, not AI-generated

Faces convert. The operator's accent, stumbles, and silences are the proof. AI-generated avatars and voices read as fake within 10 seconds. Higgsfield handles the static images on the website. The VSL is human.

## The 6 beats

| # | Beat | Time | Job |
|---|---|---|---|
| 1 | Hook | 0:00 to 0:30 | Pattern interrupt. Pain-led inversion line. |
| 2 | Loop | 0:30 to 2:00 | Operator's "before" state. Agitation. |
| 3 | Pivot | 2:00 to 3:30 | What changed. The alternative path. |
| 4 | Reveal | 3:30 to 5:30 | The product. Specifics. Proof. |
| 5 | Offer | 5:30 to 7:30 | Commitment + guarantee + urgency. |
| 6 | Close | 7:30 to 8:00 | One-line action call. |

## Output format

Each beat gets three pieces: **spoken text** the operator reads, **on-camera direction** for what they show, and **filming tip** for how they capture it.

```
## Beat N · [Name] (start:end)

**Spoken** (operator reads):
> [Exact words]

**On camera:**
[What the audience sees: face, B-roll, screen, etc.]

**Filming tip:**
[How to capture it. Camera, lighting, location, length.]
```

## Beat 1 · Hook (0:00 to 0:30)

**Spoken**:
> "[Pain-led inversion line, lifted from the website hero]. If you [behavior pattern of the addict] this week and built nothing, this is for you. Watch the next eight minutes. I will show you the exit."

### Example

> "Stop learning AI. Start executing it. If you opened another AI tutorial this week and built nothing, this is for you. Watch the next eight minutes. I will show you the exit."

**On camera:** Operator face, half-lit. Eye contact direct to lens. No music. Static or barely-moving frame.

**Filming tip:** Sit close to a window with the light coming from one side, not behind you. Phone on a tripod at eye level. Hit record, deliver the line, hit stop. Do three takes, pick the most direct.

## Beat 2 · Loop (0:30 to 2:00)

**Spoken**:
> "I lived this for years. [Concrete pattern from the operator's own past]. [Numbers]. [What it cost]. You are not lazy. You are addicted because someone built a business out of selling you the next thing."

### Example

> "I lived in this loop for years. Twenty browser tabs open. Three half-finished platforms. A Notion graveyard with names like 'AI Strategy' and 'Q4 Plan' I had not opened in months. I was teaching this. Selling it. Fourteen hundred students at FutureFlow watched me learn out loud. Ninety-three percent never shipped a single client. They paid me to keep the loop spinning. I was the dealer."

**On camera:** Mix of operator face and B-roll. Show actual screen recordings of their cluttered desktop, browser tabs, course library, Notion graveyard. Real screenshots from their real machine.

**Filming tip:** Open OBS or QuickTime, capture 30 seconds of you scrolling your real browser tabs and Notion sidebar. Then capture your face delivering the spoken text. Editor cuts back and forth.

## Beat 3 · Pivot (2:00 to 3:30)

**Spoken**:
> "Here is what stopped it. [The change the operator made]. [Specific tools/system]. [What that gave them]."

### Example

> "Here is what stopped it. I moved everything to one folder on my own machine. Plain markdown. Claude Code as the brain. My platform on the front. Twelve specialists I built once that keep running. No new tab. No new tutorial. No new chase. The chase stopped because I stopped renting."

**On camera:** Operator at their actual workspace. Real laptop, real terminal, real folder. Slow zoom on the screen if their phone has a tripod.

**Filming tip:** Film at the desk you actually work at. The realness is the proof. Open Claude Code, show the prompt, type a command, let the agent run for a few seconds. Capture the whole thing in one take.

## Beat 4 · Reveal (3:30 to 5:30)

**Spoken**:
> "Here is what you get. [Product name + format]. [Specific deliverables, list of 3 to 5]. [Sequencing: when each lands]. [Proof, if any]."

### Example

> "Twelve specialists. Each one is a Claude Code agent that owns one layer of your business. Jude builds your website. Simon runs your paid ads. Peter builds new agents on demand. Twelve roles, three releases per week, all live by Sunday May 24. You install them once and they keep running. Plus a one-on-one onboarding call with me within forty-eight hours of joining."

**On camera:** Mix of operator face and product walkthrough. Screen recording of the actual product (the agent files, the platform, the dashboard). Real assets, not mock-ups.

**Filming tip:** Screen-record the inside of the product for 60 to 90 seconds. Walk through one full feature end to end. The editor cuts to face on every list-item transition so the audience does not lose the human.

## Beat 5 · Offer (5:30 to 7:30)

**Spoken**:
> "Here is the commitment. [Price] per [period]. [What is included]. [Guarantee]. [Urgency: seats, deadline, or price step-up]."

### Example

> "Nine hundred ninety-seven dollars per year. Locked for life. You get every specialist as it launches. Every new skill they ship for the year you stay enrolled. The sovereign platform the day Mason deploys USDC. A one-on-one onboarding call within forty-eight hours. Twice-weekly group calls with me. Plus the original five-mission curriculum. The guarantee. Sovereign business live in ninety days. One owned domain. One owned platform. One paying client. One launched specialist that serves that client. If any of those four is not live in ninety days, I keep working with you free until all four are. Hundred seats. Sixty-four taken. Thirty-six remain. The price doubles to twenty-nine ninety-seven on Sunday May 24."

**On camera:** Mostly face. Occasional cut to the website's offer section animating row-by-row (screen recording of the live page).

**Filming tip:** This is the longest unbroken delivery in the VSL. Practice it three times before recording. The audience needs to feel the conviction. Do not read off a teleprompter for this beat. Memorize and deliver direct to lens.

## Beat 6 · Close (7:30 to 8:00)

**Spoken**:
> "[Final CTA from website, two lines]. [Action verb: claim / install / book / start]. The link is below. [Optional: deadline reminder]."

### Example

> "Close the tabs. Open the folder. Claim your seat below. Founding pricing closes Sunday May 24. Shut up and execute."

**On camera:** Operator face, last shot of the video. Hold the final frame for a beat after the last word.

**Filming tip:** Same as Beat 1. Single take, three attempts, pick the one with the most direct gaze.

## Production rules

- **Operator films themselves.** Phone, webcam, or DSLR. No AI avatars. No AI voiceovers.
- **B-roll comes from real screen captures.** Operator's actual desktop, browser, terminal, dashboard. No stock.
- **Hero image at the bottom of the VSL belongs to Higgsfield** (see `04-higgsfield-prompts.md`). Not the talking-head footage.
- **No royalty-free music in the body.** Either license real music or use silence plus subtle sound design (typing, ambient room).
- **No subtitle burn-in.** Add a CC track in the YouTube/Vimeo embed for accessibility but do not bake.

## What gear the operator needs (minimum viable)

- Phone with a decent camera (any iPhone or Android from the last 4 years)
- A tripod or a stack of books at eye level
- One window or a single warm lamp for the key light
- A wired earbud mic (better than the phone's built-in for voice clarity)
- OBS or QuickTime for screen recordings
- Descript, Final Cut, or CapCut for cuts and basic edit

## Editing rules

- **Talking head fills 60 to 70 percent of the runtime.** B-roll is the cutaway, not the lead.
- **Cut every silence over 0.5 seconds.** Tightens the pace.
- **No transitions.** Hard cuts only. Wipes and fades read as 2010.
- **Keep the cuts plain.** No quick zooms on punchlines, no "MrBeast" energy. Caravaggio not Vegas.

## Common mistakes

**The hook is generic.** "In today's fast-paced AI world..." is a slop tell. Use a specific accusation. "If you opened another tutorial this week and built nothing, this is for you."

**The pivot drags.** The operator dwells too long on what they did. The audience cares about what THEY can do. Cut everything that is not directly transferable.

**The offer skips proof.** Numbers, names, dates, screenshots. If the operator has none, they should not be running paid traffic to this VSL yet.

**The close says "click below to learn more."** No. Always a verb. "Claim your seat." "Install Jude." "Book the call." Action, not exploration.

**The script reads like writing.** Read every beat aloud. If it sounds like an essay, rewrite it for the ear. Contractions, fragments, beats.

## Final pass

Run `/humanizer-check` on the spoken text before recording. The operator does not want to re-record because they accidentally said "delve" or "leverage" on tape.
