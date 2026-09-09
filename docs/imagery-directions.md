# Imagery directions

Written 1 Sep 2026. Michael's note on the dark build: *too dark, the imagery does not pop,
more colour and more luminous.* Sara's steer, clarified: **keep the inner cosmos — do not
warm it into gold — and make the glow far more apparent. Not so dark.**

Nothing here is generated yet. The OpenArt connector broke mid-session
(`params: Invalid input: expected record, received string`) and needs a reconnect. These
prompts are ready to paste into OpenArt directly, or to run through the connector once it
is back.

---

## The diagnosis

The first set was **gold linework on pure black**. That worked on a dark shell. On a white
page it fails twice over: each image becomes a heavy dark rectangle punched into the light,
and the figure reads as an outline in a void rather than a body full of light.

The fix is **not** to warm the cosmos into gold and amber — that throws away the thing the
brand actually owns. The fix is to move the darkness so it lives **only inside the figure**,
and then light that interior up.

## The target

**The body as a lantern.** A pale, high-key ground. All the depth of the picture sits inside
the figure — a genuine cosmos, violet and indigo and deep blue, with nebulae and stars — but
it is *radiant*, with a bright core at the chest and light blooming softly out past the
outline onto the page.

Three consequences, and all three matter:

1. **The page stays light.** The plate's ground is ivory. Nothing dark touches the layout.
2. **The cosmos stays the cosmos.** Violet and indigo, not gold. The seal and the emblem
   still belong to the same family.
3. **The figure becomes the brightest thing in the frame**, not the darkest. That single
   inversion is what "make the glow more apparent" actually means.

## The constraint everyone forgets

Flat brand Gold `#E8BE45` measures **1.55:1 on a light ground** and fails at any size. In
imagery it is fine — a picture is not text — but the moment gold touches the page as a rule,
a label or an icon it must become Bronze `#836919` (5.4:1). That is why the site's accent is
bronze, not gold.

---

## Four directions

All four share a spine, which should stay fixed so the set holds together:

> a standing human figure, androgynous, no facial features · the interior of the figure is a
> **luminous** cosmos, violet and indigo, glowing rather than dark · a bright core at the
> chest · light blooming past the outline onto a **pale** ground · flat, printed, no drop
> shadows · no text, no lettering, no watermark

What varies is the treatment.

### A · Illuminated plate — *recommended*

Warm ivory paper, gold outline, the interior a glowing violet-and-indigo cosmos. Bronze
botanicals at the feet. Closest to the existing brand, simply inverted into the light, so
the seal and emblem still read as one family.

```
An antique illuminated plate printed on warm ivory paper. A standing human figure,
androgynous, no facial features, outlined in one unbroken fine gold line. The interior of
the figure is a deep luminous cosmos: glowing nebulae in violet, indigo and deep blue,
brilliant white and gold stars, and a radiant bright core at the heart of the chest. The
whole interior is lit up and glowing rather than dark. Soft light blooms outward past the
gold outline onto the pale ivory ground, as though the body were a lantern. Delicate bronze
botanical stems rise at the feet. Flat printed plate, gold leaf quality, no drop shadows, no
text, no lettering, no watermark, no signature. Pale warm ivory background, generous empty
margin, high key surroundings with a brilliant luminous interior.
```

### B · Lantern

The same idea pushed further: the bloom is the subject. Light floods well past the outline
and washes the surrounding paper. The most *luminous* of the four; the least contained.

```
A luminous study on pale warm white paper. A standing human figure, androgynous, no facial
features, whose whole body is a window into a glowing cosmos of violet, indigo and rose
nebulae with brilliant stars. A radiant core burns at the centre of the chest and floods
light outward, so the figure glows like a lantern and the light spills far past its outline,
washing the surrounding pale paper in soft violet and gold. A fine gold line barely
describes the edge of the body where the light does not overwhelm it. High key, radiant,
luminous. No heavy black anywhere, no drop shadows, no text, no lettering, no watermark.
```

### C · Teaching plate

Pale cream, faint bronze construction lines and thin ruled arcs passing through and around
the body, gold star points along its centre line, the interior a luminous cosmos. The most
*educational* of the four — it looks like the Institute teaches something.

```
An antique scientific teaching plate on pale cream paper. A standing human figure,
androgynous, no facial features, outlined in precise fine gold line and presented as an
instructional diagram: faint bronze construction lines and thin ruled arcs pass through and
around the body, with small gold star points marking positions along its centre line. The
interior of the figure is a luminous glowing cosmos of violet and indigo nebulae and bright
stars, radiant rather than dark, with a brilliant core at the chest casting soft light onto
the cream ground. Precise, measured, educational. Faint plate border. Flat linework, no
shading, no drop shadows, no text, no lettering, no numerals, no watermark.
```

### D · Nebula wash

Translucent cosmic washes bleeding softly at the edges of the silhouette, gold line over the
top. The warmest and most human; the loosest, and the hardest to keep consistent across
fifty Concept pages.

```
A soft watercolour and gold line study on warm white cotton paper. A standing human figure,
androgynous, no facial features, its silhouette filled with luminous translucent washes of
violet, indigo, rose and pale turquoise, like a glowing nebula seen through wet pigment,
with fine bright stars suspended inside and a warm radiant core at the chest. The washes
bleed gently past the edge of the body onto the paper. A single unbroken gold line describes
the outline. Loose bronze botanical sprigs at the base. Warm white ground, generous margin.
No heavy black, no drop shadows, no text, no lettering, no watermark.
```

---

## How to run the exploration

1. Generate **all four at 4:5, 2K, two images each** — eight pictures, one subject. Comparing
   four directions on one subject is the only way to see the *direction* rather than the
   subject.
2. Pick one.
3. Propagate the winner to the other five plates: four tiles at 3:4 (Concept Studies,
   Courses, Books, Live Events) and the Membership close at 1:1.
4. Only then decide whether the site's accent stays bronze or takes a colour from the
   chosen direction.

**Do not skip step 1.** Generating the six final plates before the direction is settled
produces six images that do not agree with each other.

## A caution on scale

The launch library is 24 Concepts, 8 Families and 12 Weaves, growing to ~50 Concepts. If
each wants a bespoke plate, the direction has to be **reproducible by recipe**, not by
taste. A and C survive that. D probably does not — worth weighing before falling for the
loosest option.

## The tone study now on the page

The placeholders on the light build carry a CSS approximation of direction A/B: warm cream
ground, the figure filled with a violet cosmos, a gold core burning at the chest, and a
bloom spilling onto the plate. It is a **colour target, not artwork** — one flat figure
repeated six times, which is exactly what the real imagery must not be.

Two implementation notes worth keeping:

- The figure is sized with **container query units** (`46cqh`) against the plate. A
  percentage height resolves against the auto-sized grid row instead and collapses the
  figure to a dark speck — which was the original complaint in miniature.
- It uses the **solid** cut of the mark (`mark-micro-mask.svg`), because the outline cut only
  lets the cosmos fill a hairline. The footer lockup keeps the outline cut, which is correct
  for the 48–120px range.

Exploratory values, **not yet in `BRAND-TOKENS.css`**: cream `#FCF8F0`, body violet
`#4A3780` / `#5E4A9C`. Brand values used: nebula `#2A1B45`, starlight `#B0A3C9`, starfire
`#FFE9A8`, gold `#E8BE45`, bronze `#836919`. If a direction is approved, these want adding
to the token file properly.
