# The Institute — static build

The home page, built as plain HTML, CSS and one file of vanilla JavaScript. No build
step, no framework, no dependencies. Open `index.html` or serve the folder.

```bash
python -m http.server 4477 --directory site
```

```
index.html    the page
styles.css    tokens, components, sections, motion — commented by section
app.js        shell switch, doors, drawer, reveal, diagram draw
assets/       images, plus the two mask cuts of the mark
```

## Two decisions that depart from the handoff

Both were Sara's calls on 1 Sep 2026. `CLAUDE.md` still describes the original plan.

**1 · Static, not Next.js.** Everything on the marketing and catalogue side is static
content. The framework was carrying no weight. The gate — accounts, enrolment records,
per-lesson progress, the completion event at the end of Foundation week ten — still needs
a server, but that is the *study* layer, and it can sit behind `/account` and the lesson
player without the catalogue paying for it.

**2 · A shell switch, where the brand said dark only.** Reconciled rather than overridden:
the brand already has an ivory reading surface, the Page. The switch does not invert the
site — it grows the Page to full size. Void ink, `--page-muted` for captions, and Bronze
in place of flat Gold, because flat Gold measures 1.55:1 on ivory and fails at any size.

Three moments stay cosmic in both shells, because they need the whole gold and the whole
dark: **the hero**, **the Operating System ring**, and **the Membership plate**. The light comes up
in the rooms; the sky stays the sky. Those carry `.inset`, which re-points the tokens
locally.

**3 · Nocturne is no longer a section ground.** Navy against violet was the one colour
pairing in the system that jarred. Nocturne now appears only on raised surfaces — cards,
School panels, mega-menu panels — which always sit on Void, never against Nebula. Section
grounds run: field → Nebula → Void → Void → Void → Nebula → Void.

**4 · Hover deepens rather than tints.** A hovered surface drops to `--hover-ground` (Void
in the Cosmos shell, Page one step down in the Page shell) and takes a hairline in
`--hover-line` (Gold, Bronze). Where a grid gap already draws the divider, the hairline is
an inset ring, not a border, so nothing shifts.

## The Operating System diagram

Michael's chain — Concept, Belief, Pattern, Emotion, Behavior, Life Result — is drawn as a
closed ring, Life Result returning to Concept, confirmed by Sara on 1 Sep 2026. That is what
makes the section's own copy legible: *"a sequence that can be drawn, followed, and
interrupted"*, and *"why do certain experiences continue to repeat?"* — you interrupt a loop,
not a line.

A star sits at the centre: the person the system runs in, echoing the star at the heart of
the seal. Below 800px the ring becomes a vertical chain with the return leg running back up
the left, because a ring that size loses its labels.

## Ground transitions

Two grounds are never butted together. A `.bridge-top` / `.bridge-bottom` overlay fades one
into the other over 14rem, on an **eased** ramp — a straight alpha ramp holds full strength
for a single pixel and then falls, and the eye reads that change of slope as an edge, which
is exactly the seam this was added to remove.

Bridges live on the section whose ground follows the shell, and fade from or to the fixed
cosmic colour. That way one rule holds in both shells.

## Colour

Every value comes from `BRAND-TOKENS.css` with two exceptions, both in the Page shell,
both Page carried toward white, both measured:

| | | on Void ink | on Bronze | on `--page-muted` |
|---|---|---|---|---|
| Page   | `#F3F0E7` | 16.68 | 4.63 | 5.19 |
| *added* | `#FBF9F4` | 18.40 | 5.10 | 5.71 |
| *added* | `#FFFFFF` | 19.30 | 5.37 | 6.01 |

The ladder runs upward, because on ivory a raised surface is lighter, not darker.

## Assets

`emblem-cut.webp` and `seal-cut.webp` are generated from `assets/emblem.jpg` and
`assets/seal.png`, which both ship on a solid black ground. Alpha is baked from luminance
so the figure floats on any surface — no `mix-blend-mode`, which breaks the moment
anything above it opens a stacking context.

```python
lut = [0 if i < 14 else min(255, int(((i/255)**0.85)*255*1.12)) for i in range(256)]
a = im.convert("L").point(lut); out = im.convert("RGBA"); out.putalpha(a)
```

`membership-sphere.webp` and `tile-events.webp` were generated with OpenArt (Nano Banana
Pro, text-to-image, 2K, 1 Sep 2026) and cut the same way. Both prompts share a style spine —
*flat single-weight metallic gold hairlines on a pure black ground, interiors opening into a
deep indigo and violet field of stars, antique celestial atlas engraving* — and both
explicitly exclude text, lettering, shading, gradients and drop shadows. Subjects:

- **Membership** — a brass armillary sphere on a beaded ring, botanical stems rooted at its
  base, 1:1.
- **Live Events** — five figures in gold outline around a wide circle, joined by
  constellation lines, 9:16 with the lower third left empty for the tile's type.

The mark is used at two cuts, never scaled from one: `mark-micro-mask.svg` (solid, below
48px) and `mark-mask.svg` (outline, 48–120px). Both are applied as CSS masks so they take
`currentColor` and follow the shell.

## Verified

390 / 768 / 1024 / 1440 with no horizontal overflow · Fraunces and Source Sans 3 both
loading, `opsz` set explicitly at every step · visible focus ring on every interactive
element · all three motion moments inside `prefers-reduced-motion` · keyboard pass through
the header doors, the drawer accordions and a tile.

## Not built yet

The other sixteen templates in `STRUCTURE.md`. The Concept page is the one that matters —
24 at launch, ~50 complete, and the likeliest search landing page.
