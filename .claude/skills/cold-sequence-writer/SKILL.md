---
name: cold-sequence-writer
description: Writes cold email sequences ready to load into Instantly for the Day 21 launch. Reads business.md ## Past Self, business.md ## Niches, business.md ## Offers and produces 6 sequences (3 niches x 2 hook variants, 3 emails each), each anchored to one of the operator's case studies. Writes strategy notes to business.md ## Cold Email. Use on Day 16 of Month 1 (initial 6 sequences) or Day 29 (3 new sequences after the cold-email retro), or whenever the operator says "write cold sequences" or "draft my Instantly campaigns."
---

# Cold Sequence Writer

By Day 16 the operator has run warm channels for 2 weeks and knows which niche is winning, which case study lands, which offer pulls. Today you turn that into cold email sequences ready to launch Day 21.

Each sequence = 3 emails (initial + 2 follow-ups). Each pair: one niche + one hook variant. 3 niches x 2 hook variants = 6 sequences.

Day 29 run: 3 new sequences based on `retros/cold-email-retro-day-28.md` learnings.

## What to do

1. Read the inputs:
   - `business.md ## Past Self` (case studies, bucket)
   - `business.md ## Niches` (3 niches)
   - `business.md ## Offers` (6 offers, 2 per niche)
   - Day 29 mode: also `retros/cold-email-retro-day-28.md`
2. Check the run mode. Day 16: write 6 fresh sequences. Day 29: write 3 new based on retro learnings.
3. Construct 3 emails per sequence using the structure below.
4. Save into Instantly campaigns and write a strategy note to `business.md ## Cold Email`.

## The 3-email structure

### Email 1. Pattern interrupt + credibility

- Subject: 3-5 words, lowercase, looks like an internal forward, not a pitch
- Opener: 1 sentence specific to the buyer's niche (not "I came across your website")
- Credibility line: 1 sentence with the operator's tightest case study and number
- Question or soft hook: 1 line, niche-specific
- Sign-off: 1 line, no signature block

Length: 45-75 words. Mobile-readable.

### Email 2. Reply-up bump (2 days after E1)

- Subject: empty OR "re:" prefix on E1 subject
- Body: 1-2 lines. Reference the question from E1. No case study repeat. No pitch.

Length: 15-30 words.

### Email 3. Specific value drop (3-4 days after E2)

- Subject: empty
- Body: a specific, niche-tailored insight (not a pitch, not a request). Something the buyer would screenshot and forward to a peer.

Length: 40-60 words.

Examples of specific value:
- "We notice 6 of 10 QBO bookkeepers leak 3+ hours per close on bank rec. The fix is a $0 automation rule. Want the doc?"
- "Recruitment agencies under 10 people running outbound on Apollo lose 20-40% of replies to inbox stuffing. There is a 5-min setting that fixes it."

## The 6 hook variants

Day 16: pair each niche with 2 of these.

1. **Tier 1 case study + niche match.** "$42K added for a QBO bookkeeper. You sound similar."
2. **Pain-named first.** "QBO close eating your Saturdays?"
3. **Specific peer reference.** "Saw [peer in niche] post about X. Most QBO bookkeepers we talk to feel similar."
4. **Result + timeline tightness.** "Cut close time from 4 hours to 45 minutes for 12 bookkeepers in 8 weeks."
5. **Unfair-advantage angle.** "I ran a QBO bookkeeping practice for 3 years before building this."
6. **Question hook.** "How long does your average close take in QBO?"

Pick the 2 that match the operator's case studies and niche identity best.

## Phases

### Phase 1. Confirm inputs (2 min)
Read aloud the 3 niches, 3 case studies, 6 offers. Confirm nothing changed in week 2-3.

### Phase 2. Pick hook variants (5 min)
For each niche, pick 2 of the 6 hook variants based on the strongest case study and identity fit. Tell the operator your picks. Confirm.

### Phase 3. Draft all 6 sequences (15 min)
Write each. 3 emails. Subject lines, bodies, follow-up cadence. Use real specifics from `business.md ## Past Self`.

### Phase 4. Read aloud, tighten (5 min)
Per sequence, check for:
- AI-sounding language (delete)
- Pitch-feel in E1 (rewrite to question or insight)
- Vague case studies (replace with the exact number from `business.md ## Past Self`)
- Same case study across all 6 (vary which one leads)

### Phase 5. Save (1 min)

## Output file format

Save to Instantly campaigns. The strategy note to `business.md ## Cold Email` follows this shape:

```markdown
# 6 Cold Sequences · Day 16

Date: [today]
Niches: [A, B, C]
Send platform: Instantly
Cadence: E1 day 0, E2 day +2, E3 day +5

---

## Sequence 1 · Niche A · Hook variant: Tier 1 case study

**E1**
Subject: [3-5 words]
[body]

**E2 · day +2**
Subject: re: [E1 subject]
[body]

**E3 · day +5**
Subject: [empty]
[body]

---

## Sequence 2 · Niche A · Hook variant: Pain-named first
[same structure]

[...sequences 3-6...]

---

## Volume plan

Day 21 launch: 200 sends/day across all 6 sequences (33/33/34 by niche).
Mailbox count: [X warmed mailboxes from Day 1]
Replies expected: 1-3% reply rate first week.

## Track these

- Reply rate by sequence
- Reply rate by niche
- Reply rate by hook variant
- Replies that book a call
```

## Worked example

Niche A: solo bookkeepers using QBO. Case study: $42K in 6 months. Tier V offer: $8.5K QBO Close Automation Build.

Sequence 1 picks "Tier 1 case study" hook.

E1:
> Subject: qbo close question
> Hey [first_name],
> Quick one. Most QBO bookkeepers I talk to lose 3-4 hours per client every close week.
> I added $42K in recurring revenue to my own bookkeeping practice in 6 months by automating QBO close. Same niche as you.
> Worth 15 minutes to compare notes?
> [name]

E2 (+2 days): "Subject: re: qbo close question. Quick bump. Worth 15?"

E3 (+5 days): "6 of 10 QBO bookkeepers we talk to leak 3+ hours per close on bank rec. The fix is a $0 automation rule that does 90% of the matching. Want the doc?"

Sequence 2 picks "Pain-named first" for the same niche, different angle. Sequences 3-6 cover niches B and C.

## Anti-pattern to flag

Operators paste the same case study into all 6 sequences. Push back: "Variety per niche. QBO case study fits niche A. Niche B is Xero. Use the Xero training case study there. Mismatched case study kills the hook."

Also flag: a sequence where E1 contains a pitch with a price. Push back: "E1 is rapport + credibility + question. Price comes after they reply. Move it to a follow-up sequence later."

Also: AI-sounding phrases. Run output through humanizer in your head. No "delve", "robust", em-dashes anywhere.

## When this skill is done

Instantly campaigns saved with 6 sequences (or 3 if Day 29 mode). Strategy note in `business.md ## Cold Email`. Operator is ready for Day 19-20 final review and Day 21 launch.
