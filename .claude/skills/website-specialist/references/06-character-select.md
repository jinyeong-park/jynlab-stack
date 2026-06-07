# 06 · Roster patterns (the list-of-N-items section)

When the operator's offer is a list of N items (modules, weeks, deliverables, team members, frameworks, courses, lessons, products), pick the roster pattern that matches the brand.

**This file describes six patterns. Character-select is one of them. Pick what fits the operator's brand, not what fits this file.**

## Decide first

Read `business.md`. The operator's aesthetic descriptor decides:

| Brand vibe (from `business.md`) | Pattern that fits |
|---|---|
| game-feel, theatrical, character-driven, dramatic | Character select (tekken-style) |
| editorial, magazine, publication-feel | Stacked list with byline-like meta |
| timeline-driven, sequenced, week-by-week | Vertical timeline with date column |
| product-catalog, retail, e-commerce | Card grid (square or 3:4 portraits) |
| data-dense, professional services, consulting | Comparison table |
| craft-led, single-photographer, artisan | Horizontal carousel with one-at-a-time focus |

If the operator says "I want it to feel like a Tekken character pick screen", use the character-select pattern. Otherwise pick from the table. Do not default to character-select.

## Skip the roster section entirely if

- The offer is "one thing, no list" (e.g. a single coaching package)
- The offer is "open-ended program" (no fixed module count)
- The N items are all unlocked from day one and operator has no narrative reason to highlight them individually

In those cases, replace the roster section with one of:
- A short "what's inside" bulleted list inside the offer block
- A one-line summary inside the body copy
- Nothing (cut the section)

## Pattern 1 · Character select (the example below)

Use ONLY when:
- Brand vibe is game-feel, theatrical, or character-driven
- AND the items have visual identities (portraits, illustrations, distinct icons)
- AND staggered unlock (some items "locked" with `?`) supports the offer narrative

The component below is the character-select pattern, lifted from one operator's site (executionsquad.co). It is one option, not the default. Components for the other five patterns live as separate files in the operator's repo when they are needed.

## Anatomy

```
┌─────────────────────────────────────────────────────┐
│  [FEATURED PANEL · 16:9]                            │
│  Big visual + name + role + bio                     │
│  Selected item appears here                         │
└─────────────────────────────────────────────────────┘

[ ? ] [ 01 ] [ ? ] [ ? ] [ ? ] [ ? ] [ ? ]
[ ? ] [ ? ]  [ ? ] [ ? ] [ ? ] [ ? ] [ ? ]
   ↑ grid of 13 cells (or however many items)
```

- Default selection: the first **unlocked** item.
- Hover or tap a cell → featured panel updates with that item.
- Locked cells show `?` silhouette + name on the cell + locked status in the panel.
- Mobile: 4-column grid. Desktop: 7-column.

## Props the component accepts

```ts
type Item = {
  id: string;          // stable key, used in URL fragments
  num: string;         // "01", "02", etc. or "★" for legendary
  name: string;        // full name shown in featured panel
  shortName: string;   // truncated name for cell
  role: string;        // "Website · Funnel · 3D"
  launch: string;      // "Mon Apr 27" or "Locked until..."
  locked: boolean;
  legendary?: boolean; // gold tint instead of red
  portrait?: string;   // /images/items/<id>/portrait.png (only if unlocked)
  video?: string;      // /videos/items/<id>/loop.mp4 (optional)
  poster?: string;     // /images/items/<id>/poster.jpg (video poster)
  biblical?: string;   // optional anchor quote (e.g. for specialist pattern)
  bio?: string;        // 2-3 line description for featured panel
};
```

## File structure

```
src/components/
└── character-select.tsx       # client component, single export
public/images/items/
├── jude/portrait.png
├── jude/silhouette.png
└── ...
public/videos/items/
└── jude/loop.mp4              # optional, if hover-loop is wanted
```

## Component (`character-select.tsx`)

Drop this in as the working skeleton. Fill in the `ITEMS` constant with the operator's roster.

```tsx
"use client";

import { useState } from "react";

const ACCENT = "#DB011C"; // REPLACE: operator brand accent from business.md

type Item = {
  id: string;
  num: string;
  name: string;
  shortName: string;
  role: string;
  launch: string;
  locked: boolean;
  legendary?: boolean;
  portrait?: string;
  video?: string;
  poster?: string;
  biblical?: string;
  bio?: string;
};

const ITEMS: Item[] = [
  // Operator fills this in. Example shape:
  {
    id: "first",
    num: "01",
    name: "First Item",
    shortName: "First",
    role: "Role tag",
    launch: "Mon Apr 27",
    locked: false,
    portrait: "/images/items/first/portrait.png",
    video: "/videos/items/first/loop.mp4",
    poster: "/images/items/first/poster.jpg",
    biblical: "Optional anchor quote.",
    bio: "Two to three sentence description.",
  },
  // Locked items:
  {
    id: "second",
    num: "02",
    name: "Second Item",
    shortName: "Second",
    role: "Role tag",
    launch: "Wed Apr 29",
    locked: true,
  },
  // ... etc
];

export function CharacterSelect() {
  const [selectedId, setSelectedId] = useState(
    ITEMS.find(i => !i.locked)?.id ?? ITEMS[0].id,
  );
  const selected = ITEMS.find(i => i.id === selectedId) ?? ITEMS[0];

  return (
    <div className="space-y-3">
      <FeaturedPanel item={selected} />
      <div className="grid grid-cols-4 gap-1.5 sm:grid-cols-7 md:gap-2">
        {ITEMS.map(item => (
          <Cell
            key={item.id}
            item={item}
            isSelected={item.id === selectedId}
            onSelect={() => setSelectedId(item.id)}
          />
        ))}
      </div>
      <div
        className="pt-3 text-center text-[11px] uppercase tracking-[0.2em] text-zinc-500"
        style={{ fontWeight: 500 }}
      >
        Tap or hover to select
      </div>
    </div>
  );
}

function FeaturedPanel({ item }: { item: Item }) {
  if (!item.locked && item.video) {
    return (
      <div
        className="relative aspect-[16/9] w-full overflow-hidden rounded-sm"
        style={{
          backgroundColor: "#0A0A0A",
          border: `1px solid rgba(219,1,28,0.35)`,
        }}
      >
        <video
          key={item.id}
          src={item.video}
          poster={item.poster}
          autoPlay loop muted playsInline
          className="absolute inset-0 h-full w-full object-cover"
        />
        <div
          className="absolute inset-0"
          style={{
            background:
              "linear-gradient(to right, rgba(0,0,0,0.92) 0%, rgba(0,0,0,0.7) 35%, rgba(0,0,0,0.25) 65%, rgba(0,0,0,0.05) 100%)",
          }}
        />

        <div className="relative z-10 flex h-full max-w-2xl flex-col justify-end p-5 md:p-10">
          <div
            className="text-[10px] uppercase tracking-[0.22em] text-zinc-400 md:text-[11px]"
            style={{ fontWeight: 500 }}
          >
            <span style={{ color: ACCENT }}>#{item.num}</span>
            {" · "}
            {item.launch}
          </div>
          <h3
            className="mt-2 text-[44px] leading-[0.92] text-white md:text-[88px]"
            style={{
              fontFamily: "var(--font-fraunces), Georgia, serif",
              fontStyle: "italic",
              fontWeight: 400,
            }}
          >
            {item.name}
          </h3>
          <div
            className="mt-2 text-[12px] uppercase tracking-[0.2em] md:text-[13px]"
            style={{ color: ACCENT, fontWeight: 500 }}
          >
            {item.role}
          </div>
          {item.biblical && (
            <p className="mt-5 max-w-md text-[13px] italic leading-relaxed text-zinc-300 md:text-[15px]">
              {item.biblical}
            </p>
          )}
          {item.bio && (
            <p className="mt-3 max-w-md text-[13px] leading-relaxed text-zinc-300 md:text-[15px]">
              {item.bio}
            </p>
          )}
        </div>
      </div>
    );
  }

  // Locked
  return (
    <div
      className="relative aspect-[16/9] w-full overflow-hidden rounded-sm"
      style={{ backgroundColor: "#060606", border: "1px solid #1A1A1A" }}
    >
      <div className="absolute inset-0 flex items-center justify-center">
        <div
          className="select-none text-[180px] leading-none md:text-[320px]"
          style={{
            fontFamily: "var(--font-fraunces), Georgia, serif",
            color: item.legendary ? "#2A1F12" : "#161616",
          }}
        >
          ?
        </div>
      </div>
      <div className="relative z-10 flex h-full flex-col justify-end p-5 md:p-10">
        <div
          className="text-[10px] uppercase tracking-[0.22em] text-zinc-500 md:text-[11px]"
          style={{ fontWeight: 500 }}
        >
          #{item.num}{item.legendary ? " · legendary" : ""} · locked
        </div>
        <h3
          className="mt-2 text-[34px] leading-[0.96] text-white md:text-[64px]"
          style={{
            fontFamily: "var(--font-fraunces), Georgia, serif",
            fontStyle: "italic",
            fontWeight: 400,
          }}
        >
          {item.name}
        </h3>
        <div
          className="mt-2 text-[12px] uppercase tracking-[0.2em] text-zinc-500 md:text-[13px]"
          style={{ fontWeight: 500 }}
        >
          {item.role}
        </div>
        <p className="mt-3 text-[13px] text-zinc-400 md:text-[14px]">
          Reveals {item.launch}.
        </p>
      </div>
    </div>
  );
}

function Cell({
  item,
  isSelected,
  onSelect,
}: {
  item: Item;
  isSelected: boolean;
  onSelect: () => void;
}) {
  const isUnlocked = !item.locked && !!item.portrait;

  return (
    <button
      type="button"
      onMouseEnter={onSelect}
      onFocus={onSelect}
      onClick={onSelect}
      className="group relative aspect-square w-full overflow-hidden rounded-sm border bg-black transition-all duration-150"
      style={{
        borderColor: isSelected ? ACCENT : "#1A1A1A",
        boxShadow: isSelected
          ? `0 0 0 1px ${ACCENT}, 0 0 20px rgba(219,1,28,0.35)`
          : undefined,
      }}
    >
      {isUnlocked ? (
        // eslint-disable-next-line @next/next/no-img-element
        <img
          src={item.portrait}
          alt={item.name}
          className="absolute inset-0 h-full w-full object-cover transition-transform duration-300 group-hover:scale-105"
        />
      ) : (
        <div
          className="absolute inset-0 flex items-center justify-center"
          style={{ backgroundColor: item.legendary ? "#0E0905" : "#0A0A0A" }}
        >
          <span
            className="select-none text-[40px] leading-none"
            style={{
              fontFamily: "var(--font-fraunces), Georgia, serif",
              color: item.legendary ? "#3A2A14" : "#262626",
            }}
          >
            ?
          </span>
        </div>
      )}

      <div
        className="absolute inset-x-0 bottom-0 px-1.5 pb-1 pt-3"
        style={{
          background:
            "linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.5) 60%, rgba(0,0,0,0) 100%)",
        }}
      >
        <div
          className="truncate text-center text-[9px] uppercase tracking-[0.14em] md:text-[10px]"
          style={{
            color: isSelected ? "#fff" : "#888",
            fontWeight: 500,
          }}
        >
          {item.shortName}
        </div>
      </div>

      <div className="absolute left-1 top-1">
        <span
          className="rounded-sm bg-black/70 px-1 py-0.5 text-[8px] tabular-nums tracking-wider text-zinc-400 md:text-[9px]"
          style={{ fontWeight: 500 }}
        >
          {item.num}
        </span>
      </div>
    </button>
  );
}
```

## How to wire it into a page

```tsx
// app/page.tsx
import { CharacterSelect } from "@/components/character-select";

export default function Page() {
  return (
    <main>
      {/* hero, problem, etc. */}

      <section className="px-6 py-20 md:py-24">
        <div className="mx-auto max-w-6xl">
          <div className="mb-16 text-center">
            <div className="mb-6 text-[11px] uppercase tracking-[0.2em] text-zinc-500">
              The roster
            </div>
            <h2 className="text-[40px] text-white md:text-[72px]">
              [Roster headline]
            </h2>
            <p className="mt-6 max-w-xl text-zinc-400">
              [Intro paragraph]
            </p>
          </div>

          <CharacterSelect />
        </div>
      </section>

      {/* offer, testimonials, etc. */}
    </main>
  );
}
```

## Customization rules

- **Number of cells:** any. Component grids on 4 cols mobile / 7 desktop. For 12 items it works perfectly. For 6 it works. For 24 it gets visually busy, consider a different pattern.
- **Accent color:** swap the `ACCENT` constant. Keep the gold for legendary items consistent (`#9A7B3A` / `#C9A24A`).
- **Cell shape:** square is the default. Change `aspect-square` to `aspect-[3/4]` if portraits are vertical.
- **Featured panel aspect:** 16:9 default. Change to `aspect-[21/9]` for cinematic, `aspect-[4/3]` for classic.

## Locked item philosophy

The locked `?` cells create anticipation. The visitor sees the full roster before they even enroll. They know what is coming, and they want to see the next reveal.

For agencies and educational programs, the operator's lock dates can be:
- "Reveals on signup"
- "Available in week 2"
- "Drops Mon Apr 27"
- "Sunday May 24 reveal" (legendary tier)

## Don'ts (for the character-select pattern specifically)

- **Do not auto-cycle the selected item.** Let the user drive. Auto-cycling reads as a banner ad.
- **Do not put a CTA inside the featured panel.** The page's own CTA is the only call to action. Keep this descriptive.
- **Do not animate the cells continuously.** Hover-only animation. Idle reads as restless.
- **Do not show prices in the cells.** Price lives in the offer section.

## The other five roster patterns (sketches)

When character-select does not fit the brand, use one of these. Operator's `business.md` aesthetic decides.

### Pattern 2 · Stacked list (editorial)

Each item is a wide row. Big serif name, small uppercase role tag, 1-2 line description, date or meta on the right. No portraits. Reads like a magazine table of contents.

Best for: writers, journalists, consultants, advisors, knowledge-product creators.

### Pattern 3 · Vertical timeline (sequenced)

Left column: week / phase / sequence label. Right column: items released in that block. Visually time-based.

Best for: cohort programs, week-by-week content drops, multi-phase deliverables.

### Pattern 4 · Card grid (catalog)

3 or 4 column grid. Each card: image / icon / illustration on top, name + 1-line below. All visible at once. No featured panel.

Best for: product catalogs, course libraries, template marketplaces.

### Pattern 5 · Comparison table (professional)

Rows are items. Columns are attributes (deliverable, time, owner, status). Dense but readable.

Best for: consulting deliverables, B2B service breakdowns, data-led offers.

### Pattern 6 · Horizontal carousel (craft-led)

One large item visible at a time. Side arrows or scroll-snap. Each item gets full attention.

Best for: portfolios, photographers, designers, anything where one item deserves the whole viewport.

Each pattern is a 100-300 line component. The operator's Jude scaffolds the right one based on `business.md`. The character-select code above is the most complex of the six. The others are simpler and not included as boilerplate in this reference.
