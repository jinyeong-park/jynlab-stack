# 07 · Bottom CTA bar (sticky, animated, urgency)

A fixed bottom bar that appears once the user scrolls past the hero and hides when they reach the offer section. Pulsing red dot, animated progress bar, claim button.

## When to use

Always, on the long-form landing page. The visitor who scrolls past the hero is reading. The bar guarantees they always have a one-click path to claim, no matter where they are on the page.

Skip on the squeeze page (the form is already prominent).

## Anatomy

```
┌──────────────────────────────────────────────────────────┐
│  ● Only 36 seats left · Closes May 24       64 of 100   │
│  ████████████████░░░░░░░░░░░░░░░░░░░░░░░░░  [Claim →]   │
└──────────────────────────────────────────────────────────┘
```

- Fixed at the bottom of the viewport
- Slides up when user scrolls past 480px
- Slides down when offer section enters view
- Pulsing red dot
- Filling progress bar (0% → N% on mount, where N is `seatsTaken / totalSeats * 100`)
- Right-aligned CTA button

## File structure

```
src/components/
└── bottom-cta-bar.tsx          # client component
```

## Component (`bottom-cta-bar.tsx`)

```tsx
"use client";

import { useEffect, useState } from "react";

// Pull from the operator's business.md and substitute below.
// Example values shown for one operator; replace with the operator's brand hex.
const ACCENT = "#YOUR_BRAND_HEX_HERE"; // operator's brand accent from business.md

type Props = {
  seatsTaken: number;        // e.g. 64
  totalSeats: number;        // e.g. 100
  closesLabel: string;       // "Sunday May 24, May 24"
  ctaHref?: string;          // default "#claim"
  scrollThreshold?: number;  // default 480px
  hideAtSelector?: string;   // default "#claim"
};

export function BottomCtaBar({
  seatsTaken,
  totalSeats,
  closesLabel,
  ctaHref = "#claim",
  scrollThreshold = 480,
  hideAtSelector = "#claim",
}: Props) {
  const [scrolledPastHero, setScrolledPastHero] = useState(false);
  const [offerInView, setOfferInView] = useState(false);

  const seatsLeft = totalSeats - seatsTaken;
  const fillPct = (seatsTaken / totalSeats) * 100;

  useEffect(() => {
    function onScroll() {
      setScrolledPastHero(window.scrollY > scrollThreshold);
    }
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });

    const el = document.querySelector(hideAtSelector);
    let observer: IntersectionObserver | null = null;
    if (el) {
      observer = new IntersectionObserver(
        ([entry]) => setOfferInView(entry.isIntersecting),
        { threshold: 0.15 },
      );
      observer.observe(el);
    }

    return () => {
      window.removeEventListener("scroll", onScroll);
      observer?.disconnect();
    };
  }, [scrollThreshold, hideAtSelector]);

  const visible = scrolledPastHero && !offerInView;

  return (
    <>
      <style>{`
        @keyframes bottombar-fill { from { width: 0%; } to { width: ${fillPct}%; } }
        @keyframes bottombar-pulse { 0%, 100% { opacity: 1; transform: scale(1); } 50% { opacity: 0.55; transform: scale(0.85); } }
      `}</style>

      <div
        aria-hidden={!visible}
        className="fixed inset-x-0 bottom-0 z-50 border-t border-zinc-800 transition-all duration-300 ease-out"
        style={{
          backgroundColor: "rgba(0,0,0,0.92)",
          backdropFilter: "blur(12px)",
          WebkitBackdropFilter: "blur(12px)",
          transform: visible ? "translateY(0)" : "translateY(100%)",
          opacity: visible ? 1 : 0,
          pointerEvents: visible ? "auto" : "none",
        }}
      >
        <div className="mx-auto flex max-w-5xl items-center gap-4 px-4 py-3 md:gap-6 md:px-6 md:py-4">
          <div className="min-w-0 flex-1">
            <div className="mb-1.5 flex flex-wrap items-baseline justify-between gap-x-4 gap-y-1">
              <div className="flex min-w-0 items-center gap-2">
                <span
                  className="inline-block h-2 w-2 shrink-0 rounded-full"
                  style={{
                    backgroundColor: ACCENT,
                    boxShadow: `0 0 10px ${ACCENT}`,
                    animation: "bottombar-pulse 1.5s ease-in-out infinite",
                  }}
                />
                <span
                  className="truncate text-[11px] uppercase tracking-[0.16em] text-white md:text-[12px]"
                  style={{ fontWeight: 500 }}
                >
                  <span className="md:hidden">{seatsLeft} left · Closes {closesLabel}</span>
                  <span className="hidden md:inline">
                    Only {seatsLeft} seats left · Closes {closesLabel}
                  </span>
                </span>
              </div>
              <div
                className="hidden text-[10px] uppercase tracking-[0.16em] tabular-nums text-zinc-500 md:block md:text-[11px]"
                style={{ fontWeight: 500 }}
              >
                {seatsTaken} of {totalSeats} claimed
              </div>
            </div>
            <div className="relative h-1.5 w-full overflow-hidden rounded-full bg-zinc-900">
              <div
                className="absolute inset-y-0 left-0 rounded-full"
                style={{
                  width: `${fillPct}%`,
                  backgroundColor: ACCENT,
                  boxShadow: "0 0 12px rgba(219,1,28,0.5)",
                  animation: visible
                    ? "bottombar-fill 1.1s cubic-bezier(0.22,1,0.36,1) 0.05s both"
                    : undefined,
                }}
              />
            </div>
          </div>

          <a
            href={ctaHref}
            className="inline-flex shrink-0 items-center justify-center rounded-full px-4 text-[13px] text-white transition-all duration-150 md:px-7 md:text-[14px]"
            style={{
              backgroundColor: ACCENT,
              height: 44,
              fontWeight: 500,
            }}
          >
            <span className="md:hidden">Claim →</span>
            <span className="hidden md:inline">Claim your seat →</span>
          </a>
        </div>
      </div>
    </>
  );
}
```

## How to wire it into a page

```tsx
// app/page.tsx
import { BottomCtaBar } from "@/components/bottom-cta-bar";

export default function Page() {
  return (
    <>
      <main>
        {/* hero, problem, roster, your pack, offer (#claim), testimonials, final CTA, footer */}
      </main>

      <BottomCtaBar
        seatsTaken={64}
        totalSeats={100}
        closesLabel="Sunday May 24, May 24"
      />
    </>
  );
}
```

The bar reads from props. Update them as the operator's seat count changes (or wire to a Supabase query if real-time).

## When the offer has no seat cap

If the operator does not have a seat limit but does have urgency (deadline only):

```tsx
<BottomCtaBar
  seatsTaken={75}        // fake the bar fill (use elapsed-time / total-time)
  totalSeats={100}
  closesLabel="Friday, Sep 5"
/>
```

Or build a deadline-only variant by removing the seats counter and replacing the progress bar with a simple "X days remaining" text.

## When there is no urgency at all

Skip the urgency framing in the bar. Show just a brand-line + CTA:

```tsx
{/* Operator can hand-roll a simpler bar */}
<div className="fixed inset-x-0 bottom-0 z-50 border-t border-zinc-800 bg-black/92 backdrop-blur-md">
  <div className="mx-auto flex max-w-5xl items-center justify-between gap-4 px-6 py-3">
    <span className="text-[12px] uppercase tracking-[0.16em] text-zinc-400">
      [Operator brand line]
    </span>
    <a href="#claim" className="rounded-full bg-[var(--accent)] px-6 py-2 text-white">
      [CTA →]
    </a>
  </div>
</div>
```

## Don'ts

- **Do not show on every page.** Only the long-form landing.
- **Do not auto-fill the bar to 100%.** That kills urgency. Use the real ratio.
- **Do not use neon glow.** Soft `box-shadow` is enough. Hard glow reads as 2010.
- **Do not block the page bottom on mobile.** The bar is 60-72px tall. The footer should still be reachable above it.
- **Do not animate the bar continuously.** The fill plays once on mount. The dot pulses. That is the only motion.

## Performance notes

- The `IntersectionObserver` is cheap. One observer per page.
- `position: fixed` does not cause reflow.
- `backdrop-filter: blur(12px)` is GPU-accelerated. Falls back gracefully on browsers that do not support it.
- The `<style>` tag with keyframes runs once on first render. Re-renders do not re-inject.

## Accessibility

- `aria-hidden={!visible}` so screen readers ignore the bar when off-screen.
- The CTA `<a>` has a real `href` for keyboard navigation.
- The pulse animation respects `prefers-reduced-motion` if the operator wants to add it (wrap the `animation` in a media query).

```tsx
@media (prefers-reduced-motion: reduce) {
  /* Set animation: none on the dot and the fill */
}
```
