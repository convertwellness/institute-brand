# Design direction

The v1 mockup was structurally right and visually flat. This document says exactly why, and
what to build instead. Read it with `BRAND-TOKENS.css` open.

## What was wrong

| Problem | Evidence |
|---|---|
| Two background values for the whole page | Void, and Nebula at 25%. Nothing else. |
| Hover states only swapped a colour | No lift, no border change, no underline, no image movement. |
| No depth anywhere | The brand forbids drop shadows, and nothing replaced them. |
| No motion | The brand specifies "content fades up as though being lit" and "each diagram draws itself once on first view." Neither was implemented. |
| Sections all announced themselves the same way | Eyebrow, heading, body. Nine times. |

Fix those five and the page stops looking like a wireframe in brand colours.

## 1. Grounds — build a ladder, not a switch

Five distinct grounds, used deliberately. Never alternate two.

```
Void       #0B0E16   the base. the page starts and ends here
Nocturne   #171E2E   raised neutral: cards, tables, lists
Nebula     #2A1B45   raised cosmos: heroes, feature wells, School openers
Page       #F3F0E7   the reading surface, for anything over ~400 words
```

Plus one that is not a colour: **the field** — Void carrying a faint starfield and a very low
radial nebula wash. Use it behind the hero and one or two moments per page, never twice in a
row.

**Transitions between grounds matter more than the grounds.** Do not butt two flat colours
together with a hairline. Either:

- fade the incoming ground in over ~12rem with a linear gradient to transparent, or
- separate them with a full-bleed image or diagram band, so the eye has something to cross.

**Section rhythm.** Over a long page, vary the ground in a pattern that means something —
grounds should track the *kind* of content, not alternate for variety:

```
Void field  → hero
Nebula      → the argument (the Human Operating System)
Void        → the offer (courses, cards)
Nocturne    → dense structure (the path, tables)
Page        → reading
Void        → the Schools
Nebula      → membership, closing
```

## 2. Depth without shadows

The brand forbids drop shadows and bevels. Depth comes from three things instead:

1. **Value.** A raised surface is lighter than its ground. Never outline a card that is already
   a lighter value — pick one.
2. **A single hairline.** `1px solid --rule (#2A2647)`. Never 2px, never a doubled border.
3. **A contact glow, sparingly.** A raised cosmos surface may carry an inset radial highlight at
   very low opacity, as if lit from above:
   `background-image: radial-gradient(120% 80% at 50% -20%, rgba(232,190,69,.05), transparent 60%)`

For the emblem and seal only, an ambient shadow is permitted — they are objects, not interface:
`0 40px 120px rgba(0,0,0,.55)`.

## 3. Hover, focus and active — every interactive element

Transitions: **160ms** for colour, **240ms** for transform, `cubic-bezier(.2,.6,.2,1)`.
Everything inside `@media (prefers-reduced-motion: reduce)` drops to 0.

**Primary button** — gold fill
- rest: `bg-gold text-void`
- hover: `bg-starfire` (brighter, not darker — the light is coming up)
- active: `bg-gold` and `translate-y-px`
- focus-visible: `outline 2px gold, offset 3px`

**Secondary button** — gold hairline
- rest: `border-gold text-gold bg-transparent`
- hover: `bg-gold text-void`
- active: `translate-y-px`

**Text link, inline**
- rest: gold with a 1px underline at 35% opacity, `text-underline-offset: 4px`
- hover: underline to 100%. Do not change the text colour.

**Nav item**
- rest: Starlight
- hover: Moonlight, and a 1px gold rule draws in beneath from left to right over 240ms
- current page: Moonlight, rule at rest, full width

**Card** (Course, Concept, School)
- rest: Nocturne, hairline rule
- hover: ground lifts one step toward Nebula, rule brightens to `#3A3560`, title turns gold,
  and the whole card rises 2px. All four together — one alone reads as a bug.
- the whole card is the hit area, not just the title

**Figure / image tile**
- hover: image scales to 1.03 inside `overflow-hidden`, over 400ms. The frame never moves.

**Accordion trigger**
- hover: title to gold, the `+` rotates 45° over 300ms
- open: `+` stays rotated, content fades and slides up 8px over 240ms

**Focus-visible, everywhere**: `outline: 2px solid var(--gold); outline-offset: 3px`. Never
remove it, never replace it with a background change alone.

## 4. Motion — three moments, and no more

The brand says content is *lit*, not slid. Everything moves up and fades in; nothing slides
sideways, nothing bounces, nothing springs.

1. **Section reveal.** On first scroll into view, a section's contents fade from 0 to 1 and rise
   12px over 600ms, children staggered 60ms apart. Once. Use `IntersectionObserver` with
   `once: true` — never re-trigger on scroll back.
2. **Diagram draw.** A diagram animates its strokes once on first view — `stroke-dasharray` and
   `stroke-dashoffset` over ~1200ms, arrowheads fading in last. Then it holds still forever.
3. **The glint.** The single star at the heart of the mark may pulse very slowly — opacity .75
   to 1 over 4s, ease-in-out, infinite. One per page maximum. This is the only looping animation
   in the system.

Everything else is instant. No parallax, no scroll-jacking, no counters that count up.

## 5. Type in practice

Already specified in the brand — what the mockup underused:

- **Fraunces needs its `opsz` axis set explicitly at each step.** Left at the default, the large
  sizes lose their contrast and look like any other serif. Masthead 144, section heads 96,
  subheads 24–36.
- Leave `SOFT` and `WONK` at 0.
- Body is Source Sans 3 **400**, never 300 on dark.
- One uppercase style only: `.eyebrow`, 600 weight, .12em tracking, 0.72rem. Nothing smaller
  ships.

## 6. Detail that earns its place

- **Numbers where sequence is real.** The path has five tiers in order — number them. The
  Schools are a set, not a sequence — do not.
- **Rules carry meaning.** A hairline between list items is structure. A hairline decorating a
  heading is noise.
- **Tabular numerals** wherever figures align — prices, counts, week numbers.
- **One accent per screen.** Gold earns its weight by being rare. If a screen has a gold button,
  gold linework and gold headings all at once, remove two.

## 7. Accessibility, non-negotiable

- Every pairing in `BRAND-TOKENS.css` is annotated with its measured ratio. Do not introduce a
  colour that is not in that file.
- **Flat gold on the Page measures 1.55:1 and fails.** Use Bronze, or put the element in a dark
  inset.
- Target size 44×44 minimum for anything tappable.
- The gate must be readable by screen reader: a locked study announces its state and what opens
  it, not just a padlock icon.
- Respect `prefers-reduced-motion` for all three motion moments.
