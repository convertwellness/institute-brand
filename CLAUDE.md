# The Institute — build instructions

> **Amended 1 Sep 2026.** Two things below have been superseded by Sara's direction.
> The built home page lives in `site/`; `site/README.md` explains both in full.
>
> - **Stack.** Not Next.js. Plain HTML, CSS and vanilla JS, no build step. The gate still
>   needs a server, but that is the study layer, not the catalogue.
> - **Light mode.** There is now a shell switch. It is not a theme inversion — it grows
>   the Page, the brand's own ivory reading surface, to full size, with Bronze in place of
>   flat Gold. The hero, the Operating System diagram and the seal stay cosmic in both.
>
> Everything else in this file still stands, and the brand rules below are unchanged.

You are building the website for **The Institute of The Spiritual Science of Human Patterns**.
The brand is decided, the content is written, and the structure is settled. Your job is to build
it well — not to redesign it.

## Read these first, in order

1. `BRAND-TOKENS.css` — the palette with every contrast ratio measured. Copy it into
   `app/globals.css`. Do not introduce a colour that is not in it.
2. `DESIGN.md` — grounds, hover states, depth and motion. The previous attempt was flat; this
   says exactly how not to repeat that.
3. `content/site.ts` and `content/navigation.ts` — every string. Import from these; do not
   retype copy into components.
4. `STRUCTURE.md` — the sitemap and page inventory.

## Stack

- Next.js (App Router) · Tailwind v4 (CSS-first, no `tailwind.config.js`) · shadcn/ui on Radix
- Fraunces (display) and Source Sans 3 (body and interface), via `next/font/google`
- TypeScript strict

Wire the brand into the **shadcn token slots** — `--primary`, `--card`, `--muted-foreground` and
so on — so every component you add later inherits the brand without being restyled. Two brand
rules live as tokens, not as discipline:

- `--radius: 0rem`. The brand has no rounded corners.
- Flat gold is `--gold`; the metallic ramp is `--metal`, for seals and foil only.
  **A gradient in a diagram is a bug.**

## Non-negotiable brand rules

Violating any of these is a defect, not a preference.

- **Dark shell, always. There is no light mode.** The Page (`--page`, ivory) is a surface inside
  the dark shell for long-form reading — not a theme, not a toggle.
- Anything over roughly 400 words sits on the Page. Everything scanned or operated stays dark.
- **Flat gold never touches the Page** (1.55:1). Use `--bronze`, or put it in a dark inset.
  Diagrams keep a dark inset because they need the whole gold.
- **One accent per screen.** Gold is rare on purpose.
- **One glint.** Starfire marks star points and the single star at the heart of the mark. If it
  appears more than a handful of times, it is overused.
- The full name is never shortened to an acronym, never all-caps, always three lines broken
  exactly as `BRAND.fullName` gives them. In navigation and body copy after first mention it is
  "The Institute".
- Capitalisation is a rule: Concept, Pattern, Concept Family, Concept Weave, Pattern Weave,
  School, Foundation Course, Human Operating System. Lowercase when ordinary — a pattern in a
  carpet is not a Pattern.
- Never: countdown timers, seat scarcity, before-and-after testimonials, stock photography of
  people meditating, chakra charts, mandalas as wallpaper, rounded corners, drop shadows on
  interface, gradients on buttons.
- Never the words *vibration*, *frequency*, or *quantum*. Every term is one of Michael's own.

## The gate

The Foundation Course is **mandatory**: nothing in Concept Studies, Families, Weaves, Extended
Foundation or the Schools can be *started* until it is complete.

**The gate stops study, never browsing or buying.** Every page stays fully readable and
purchasable to anyone — otherwise the catalogue cannot sell. Four states per study item, in
`GATING` in `content/site.ts`: open, locked, in progress, complete.

A locked page shows the full description, the Patterns it covers, the price, and one line saying
what opens it. In Michael's voice, never a marketer's. Nothing that implies the visitor is
behind.

This means the real site needs accounts, enrolment records, per-lesson progress, and a
completion event at the end of Foundation week ten. Static export will not cover it.

## Assets

In `assets/`:

- `seal.png` — the seal, beaded ring, transparent corners. Large use: hero, certificates, covers.
- `mark.svg` / `mark-micro.svg` — the vector mark, one path. Outline for 48–120px, solid below.
- `hero-field.jpg` — the hero ground, deliberately empty through the middle.
- `tile-*.jpg` — three engraved tiles: constellation, study editions, botanical.

Mark scale rules: **Full** ≥120px · **Simple** 48–120px · **Micro** below 48px. Stroke is a
property, not geometry — export the cut you need, never scale one.

## Content gaps

Search `content/` for `needsMichael`. Those strings are not yet written. Ship the route, ship a
clear placeholder, do not invent copy. The largest gap is the names of the twenty-four Concepts,
eight Families and twelve Weaves that make up the launch library.

Michael, 22 Aug: *"item/products will be added in the same categories that are built today."*
Build the categories properly and the library fills in without a rebuild.

## Build order

1. Tokens, fonts, base layer. Verify contrast against the annotations before writing components.
2. shadcn primitives wired to the tokens — button, card, badge, accordion, navigation-menu, sheet.
3. Header with the five doors, plus mobile drawer. Footer.
4. Home page.
5. The Concept page template — it repeats 24 times now and ~50 later, so it is the one that
   matters most.
6. Index templates (Concepts, Courses, Schools, Books, Events).
7. Course, School, Book and Event templates.
8. Account, cart, membership.

## Verify before claiming done

- No horizontal overflow at 390, 768, 1024 and 1440.
- Both fonts actually loading, with `opsz` set at each step of the scale.
- Every interactive element has a visible focus ring.
- All three motion moments respect `prefers-reduced-motion`.
- No colour outside `BRAND-TOKENS.css`.
- Keyboard-only pass through the header, accordion and a course card.
