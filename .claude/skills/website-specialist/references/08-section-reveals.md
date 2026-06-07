# 08 · Section reveals (scroll fade-up + page-load entrance)

Sections fade-up as they enter the viewport. Hero copy fades in on page load with staggered delays. Same easing curve everywhere.

## Why

Scroll reveals reward the reader's attention. Page-load entrance signals craft. Without these the page feels dead. With them it feels considered.

The trick is restraint. One easing curve. One direction (up). One trigger per section. No popping, no bouncing, no parallax.

## File structure

```
src/components/
└── reveal.tsx              # client component, IntersectionObserver-based
```

## Reveal component (`reveal.tsx`)

```tsx
"use client";

import { useEffect, useRef, useState } from "react";

type Props = {
  children: React.ReactNode;
  delay?: number;
  duration?: number;
  amount?: number;
  className?: string;
  once?: boolean;
};

export function Reveal({
  children,
  delay = 0,
  duration = 700,
  amount = 24,
  className,
  once = true,
}: Props) {
  const [visible, setVisible] = useState(false);
  const ref = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    const el = ref.current;
    if (!el) return;

    if (typeof IntersectionObserver === "undefined") {
      setVisible(true);
      return;
    }

    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setVisible(true);
          if (once) observer.disconnect();
        } else if (!once) {
          setVisible(false);
        }
      },
      { threshold: 0.12, rootMargin: "0px 0px -8% 0px" },
    );

    observer.observe(el);
    return () => observer.disconnect();
  }, [once]);

  return (
    <div
      ref={ref}
      className={className}
      style={{
        opacity: visible ? 1 : 0,
        transform: visible ? "translateY(0)" : `translateY(${amount}px)`,
        transition: `opacity ${duration}ms cubic-bezier(0.22, 1, 0.36, 1) ${delay}ms, transform ${duration}ms cubic-bezier(0.22, 1, 0.36, 1) ${delay}ms`,
        willChange: "opacity, transform",
      }}
    >
      {children}
    </div>
  );
}
```

## Easing curve (locked)

`cubic-bezier(0.22, 1, 0.36, 1)` everywhere. Same curve for:

- Section fade-ups
- Page-load hero entrance
- Bottom CTA bar slide-in
- Seats progress bar fill
- Card hover micro-states

This is the ONE curve. Do not introduce a second.

## Where to wrap

Wrap the **inner container** of each major section (not the `<section>` element itself). That way the `<section>` keeps its background, border, and padding, while the content fades up.

### Pattern

```tsx
import { Reveal } from "@/components/reveal";

<section className="border-y border-zinc-900 px-6 py-20 md:py-24">
  <Reveal className="mx-auto max-w-3xl">
    {/* heading + paragraphs */}
  </Reveal>
</section>
```

### Sections to wrap on the long-form landing

- VSL placeholder
- "Actual problem" section
- Roster section (the heading + character select)
- Your pack download section (if present)
- Founding offer section
- Testimonials
- Final CTA

### Sections NOT to wrap

- The hero (page-load animation handles this, see below)
- The footer (always-visible nav-like content)
- The bottom CTA bar (its own slide-in)

## Page-load hero entrance

CSS keyframes only. No IntersectionObserver. The hero is above the fold so it animates on first paint.

### Keyframe

```tsx
<style>{`
  @keyframes hero-rise {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }
`}</style>
```

### Application (with stagger)

```tsx
<section className="px-6 pt-24 pb-16">
  <div className="mx-auto max-w-5xl text-center">
    <h1
      style={{
        animation: "hero-rise 900ms cubic-bezier(0.22, 1, 0.36, 1) 80ms both",
      }}
    >
      [Hero H1]
    </h1>

    <p
      style={{
        animation: "hero-rise 900ms cubic-bezier(0.22, 1, 0.36, 1) 280ms both",
      }}
    >
      [Subhead]
    </p>

    <div
      style={{
        animation: "hero-rise 900ms cubic-bezier(0.22, 1, 0.36, 1) 460ms both",
      }}
    >
      [CTA or form]
    </div>
  </div>
</section>
```

The `both` fill mode is non-negotiable. Without it the animation can flash at frame 0.

### Stagger timing

- 80ms · headline
- 280ms · subhead (200ms after headline starts)
- 460ms · CTA / form (180ms after subhead starts)

That's it. Three elements, three delays. Do not add a fourth.

## Reveal usage examples

### Default (no delay)

```tsx
<Reveal>
  <h2>Section heading</h2>
  <p>Body text</p>
</Reveal>
```

### Custom delay (for staggered content within a section)

```tsx
<Reveal delay={0}>
  <h2>Heading</h2>
</Reveal>
<Reveal delay={120}>
  <p>Subhead</p>
</Reveal>
<Reveal delay={240}>
  <div>Card row</div>
</Reveal>
```

Use sparingly. One Reveal per section is the default. Multiple reveals within a section is for the offer or roadmap where the user dwells.

### Custom amount (more dramatic distance)

```tsx
<Reveal amount={48} duration={900}>
  <h2>Big drop-in heading</h2>
</Reveal>
```

Cap at `amount={48}`. Beyond that it feels theatrical.

### Re-trigger on scroll back up

```tsx
<Reveal once={false}>
  <div>Repeats every time it enters viewport</div>
</Reveal>
```

Default is `once={true}`. Use `once={false}` only for genuinely repeatable elements (like a sticky note that flashes when re-entered). For sections, leave it `true`.

## Reduced motion

The `Reveal` component does not currently disable animation under `prefers-reduced-motion`. Add this to globals.css for accessibility:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

This blanket-disables animation for users who request it. The site still works perfectly without motion.

## Performance

- Each `<Reveal>` creates one `IntersectionObserver`. Across a 7-section page that is 7 observers. Lightweight.
- The page-load keyframes run once on first render. Zero ongoing cost.
- `will-change: opacity, transform` keeps the GPU pre-warmed for the transition. Browsers free this after the transition completes.

## Don'ts

- **Do not nest Reveals.** A Reveal inside a Reveal cascades the delays unpredictably. Use a single wrapper per section.
- **Do not animate from below 16px or above 48px.** Below feels like nothing happened. Above feels theatrical.
- **Do not use a second easing curve.** One curve everywhere. Consistency reads as taste.
- **Do not animate the hero on scroll-up.** It is above the fold. Page-load only.
- **Do not animate the footer.** It is structural, not narrative.

## Common mistakes

**Sections never appear.** Almost always means `IntersectionObserver` is unsupported (very old browsers). The component falls back to immediate visible state. Confirm by adding `console.log("IO supported:", typeof IntersectionObserver !== "undefined")` in the effect.

**Section flashes visible then animates.** Forgot the `both` fill mode or the initial `opacity: 0` style. Check the inline styles on the wrapper div.

**Animation feels janky.** The element is too heavy for compositing. Add `will-change: opacity, transform` to the styles. If still janky, the animated element contains a `<video>` or large image. Move the animation to a parent wrapper instead.

**Re-triggering on scroll feels distracting.** Default to `once={true}` and only override when the operator explicitly wants the repeat behavior.
