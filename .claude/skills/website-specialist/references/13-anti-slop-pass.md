# 13 · Anti-slop pass (the deploy gate)

The final check before the site goes live. Zero AI tells. Zero em dashes. Zero formulaic openings. If any check fails, fix it. Do not deploy until clean.

## When to run

After all copy is written and all components are wired, BEFORE `vercel --prod`. Every text block, every email, every alt tag, every microcopy fragment goes through this pass.

## The full checklist

### 1. Banned vocabulary (Tier 1, never use)

Scan all copy files for these words. Any hit fails the pass.

```
delve · tapestry · multifaceted · landscape · leverage · robust · testament ·
pivotal · underscore · encompass · realm · embark · interplay · intricate ·
nuance · garner · paramount · commendable · meticulous · showcase · symphony ·
beacon · indelible · bustling · vibrant · enigma · unwavering · nestled ·
annals · bespoke
```

### 2. Banned vocabulary (Tier 2, avoid)

These read AI-ish but might survive a single use in context. Aim for zero.

```
elevate · navigate · harness · unlock · foster · bolster · captivate ·
comprehensive · cutting-edge · groundbreaking · seamless · holistic ·
transformative · pioneering · trailblazing · streamline · innovative ·
revolutionary · supercharge · reimagine · orchestrate · synergy · align ·
dynamic · profound · esteemed · whimsical · burgeon · aptly · poised
```

### 3. Banned phrases

Hard fail on any of these.

```
"in today's fast-paced world"
"in today's digital age"
"in today's ever-evolving landscape"
"in the realm of"
"when it comes to"
"it's worth noting that"
"it's important to note that"
"it is crucial to understand"
"stands as a testament"
"plays a vital/crucial/pivotal role"
"paving the way"
"at the forefront of"
"left an indelible mark"
"game-changer"
"best-in-class"
"the future looks bright"
"only time will tell"
"unleash the power of"
"navigate the complexities of"
"embark on a journey"
```

### 4. Banned formatting

| Pattern | Fix |
|---|---|
| em dash (`—`) | period, comma, parens, or restructure |
| Title Case headings | sentence case |
| Decorative emoji in body text | remove |
| Inline-header bullets (**Bold:** explanation) | restructure as paragraphs or proper lists |
| `Furthermore,` `Moreover,` `Additionally,` at sentence start | delete the connector, just start the sentence |

### 5. Sentence rhythm check

AI text is uniform. Human text is bursty. For each paragraph, check:

- Are there sentences under 6 words?
- Are there sentences over 25 words?
- Is there a one-word or two-word sentence somewhere on the page?

If every sentence is 12 to 18 words, the prose reads as AI. Cut some, lengthen others.

### 6. Opinion check

Each section should have at least one direct opinion or take. "I think X" / "Y is wrong" / "Most people get this backwards." Sections without a take read as Wikipedia.

### 7. Specifics check

Every claim has a number, date, or name attached. "Hundreds of clients" fails. "Fourteen hundred students at FutureFlow" passes.

### 8. First-person consistency

The operator's voice is "I", not "we", except when intentionally speaking for a team. If "we" creeps in for solo content, flip to "I".

### 9. CTA verb check

Every CTA button uses an action verb. Pass: "Claim", "Install", "Book", "Start", "Download", "Watch". Fail: "Learn more", "Click here", "Get started", "Discover", "Explore".

### 10. Formulaic closing check

Sections should not end with a tidy bow. Failing closings:

```
"The future looks bright."
"Only time will tell."
"As we move forward..."
"In conclusion..."
"Embark on a journey..."
```

Replace with a direct call to the reader's action or simply stop on the last factual sentence.

### 11. Decorative element scan

- Logo soup ("Trusted by 10,000+ founders") → remove unless real
- Decorative gradient blobs → remove
- Emoji in headings → remove
- Glassmorphism on body content → remove
- Cookie banner that blocks the first view → use a small dismissible banner instead

### 12. Em dash final scan

Run a literal grep for `—` and `–` across all content files. Zero hits required.

```bash
grep -rn "—\|–" src/ content/ public/
```

If anything found, replace.

## How Jude runs the pass

### Automated portion

```bash
# Run the humanizer skill on every text block
# Pulls from /humanizer-check skill
```

The `/humanizer-check` skill handles vocabulary and phrase scans automatically. Run it on every copy file:

- `src/app/page.tsx` (extract text-only content)
- `src/app/squeeze/page.tsx`
- `src/components/*.tsx` (text content within)
- `src/emails/welcome.tsx`
- Any markdown content files

### Manual portion (Jude's judgment)

The automated scan does not catch:

- Sentence rhythm
- Opinion presence
- Specifics density
- First-person consistency
- CTA verb strength

Jude reads the live page out loud (or in the head) and judges these. If the prose sounds like an essay, rewrite for the ear.

## What to do when a check fails

1. Identify the specific block that failed (file, line, text)
2. Cut and rewrite the failing block. Do not negotiate. The humanizer rules are non-negotiable.
3. Re-run `/humanizer-check` on the revised file
4. Repeat until clean

## Common operator pushback

**"But everyone uses 'leverage' in business writing."** That is exactly why we do not. The operator's prose should not blend in.

**"My niche expects this kind of language."** Pick another niche. Or keep the niche and stand out by writing differently.

**"The em dash looks better here."** No. The em dash is a hard rule of the craft. Period, comma, parens, restructure.

**"This sentence is fine, the AI scanner is too aggressive."** The scanner is calibrated against actual AI corpora. If it flags, it flags for a real reason. Trust the scanner.

## Output of the pass

A clean log dropped at `.claude/owner-inbox/YYYY-MM-DD_jude_anti-slop.md`:

```markdown
# Anti-slop pass · <date>

## Files scanned
- src/app/page.tsx (12 text blocks)
- src/app/squeeze/page.tsx (4 text blocks)
- src/components/character-select.tsx (13 item descriptions)
- src/emails/welcome.tsx (5 paragraphs)

## Tier 1 vocabulary
- 0 hits ✓

## Tier 2 vocabulary
- 0 hits ✓

## Banned phrases
- 0 hits ✓

## Em dashes
- 0 hits ✓

## Title Case headings
- 0 hits ✓

## Formulaic closings
- 0 hits ✓

## Manual review
- Sentence rhythm: passed ✓
- Opinion density: passed ✓
- Specifics: passed ✓
- First-person consistency: passed ✓
- CTA verbs: passed ✓

## Status
READY TO DEPLOY.
```

If anything fails:

```
## Status
BLOCKED. Fixes required:

1. src/app/page.tsx:142 · "leverage" appears in offer paragraph. Replace with "use".
2. src/components/footer.tsx:18 · em dash in "Chilliwack — BC". Use comma.
3. src/emails/welcome.tsx:24 · sentence reads as Wikipedia. Add an opinion or specific.

Re-run pass after fixes.
```

## Why this matters

The operator's site is a craft signal. Every AI tell knocks them down a tier in the reader's mind. Every "delve" or "leverage" or em dash says "this is generic content, not someone with a real point of view."

The anti-slop pass is the moat. Most operators will skip it. The operators who run it produce sites that read as written by a person with conviction. That is the conversion difference.

## Related

- `/humanizer-check` skill, handles the automated scans
- `02-copy-blocks.md`: has the full banned vocabulary list at the top
- The operator's `business.md`: pull the voice from there before writing copy

## When to re-run

- Every deploy (the gate)
- Every major copy revision
- Every new email or page
- After the operator hand-edits copy (they will accidentally introduce slop)

The pass takes 5 to 15 minutes for a 2-page site. Do not skip it. The deploy waits.
