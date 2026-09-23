# ChatGPT Icon Generation Brief

**The Institute of The Spiritual Science of Human Patterns**
Written 22 Sep 2026, from an audit of the built site (67 pages, 66 routes).

Use the Implementation Brief image as the visual reference. This document does not
redescribe the brand — it says **which icons exist, what each one must depict, and the
one technical constraint that decides whether CSS can colour them.**

---

## 0 · The single most important instruction

> **Every icon must be monochrome — pure white line art on a fully transparent
> background. No gold. No teal. No purple. No two-tone. No fills of any colour.**

This sounds like it contradicts the brand reference. It does not, and getting it wrong
costs the whole set.

A flat single-colour shape on transparency can be used as a **CSS mask**. That means the
site paints the icon with a brand token at render time — gold on dark, bronze on light,
teal on hover, muted when a Study is locked, and so on. One file serves every state.

The moment an icon ships with gold and teal baked into the pixels, those colours are
fixed. It cannot respond to hover, it cannot go bronze where flat gold fails contrast on
the light page, and it needs a second file for every state. **The gold and teal in the
reference are applied by CSS, not drawn into the asset.**

So: draw the icon as if it were a rubber stamp. The colour is the ink, and the site
holds the ink.

### Delivery spec — applies to every icon in every batch

| | |
|---|---|
| Format | PNG, transparent background, no matte, no shadow |
| Size | 1024 × 1024, square, one icon per file |
| Colour | Pure white `#FFFFFF` only, on full transparency |
| Padding | Artwork fills ~78% of the frame, centred, ~11% clear margin all round |
| Stroke | One consistent weight across the entire batch — ~32px at 1024, round caps and joins |
| Construction | Line only. No solid fills, no gradients, no texture, no glow, no drop shadow |
| Geometry | Built on circles and arcs where possible. The brand has no rounded rectangles |
| Naming | `hos-concept.png`, `path-01-introduction.png`, etc. — names given per batch below |

**Optical sizing matters more than mathematical sizing.** A circle and a tall arrow at the
same bounding-box height do not look the same size. Balance them by eye so the set reads
evenly when placed in a row.

**Do not add:** text, numerals, lettering of any kind, watermarks, signatures, frames,
circular badges, coloured discs behind the mark, or a background of any sort. The site
draws the circular container in CSS — that is why the reference shows icons inside gold
rings and these files must not.

---

## 1 · Human Operating System — 6 icons

This is the most prominent element on the home page: Michael's chain, drawn as a closed
loop with Life Result returning to Concept. **These six are not six separate pictograms.
They are one idea in six stages, and the set fails if they do not read as a sequence.**

### The governing idea

A single point sits at the centre of every one of the six. That point is the Concept. At
each stage more structure accumulates around it, and by the sixth the structure has closed
into a circuit that feeds the point again. Someone looking at all six in a row should see
the same thing being progressively enclosed.

Keep the central point **identical in size and position in all six files.**

| # | File | Name | What it depicts |
|---|---|---|---|
| 1 | `hos-concept.png` | Concept | The bare origin. A single four-pointed star, alone, with a great deal of empty space around it. Nothing encloses it yet. |
| 2 | `hos-belief.png` | Belief | The same star, now with one closed ring drawn around it. The first thing that forms around a Concept and hardens. |
| 3 | `hos-pattern.png` | Pattern | The star and ring, with a second line orbiting — a path that visibly crosses its own track and returns. Repetition, not progress. |
| 4 | `hos-emotion.png` | Emotion | The same core, with three concentric arcs rippling outward from it, open at the sides. A response radiating, not a structure. |
| 5 | `hos-behavior.png` | Behavior | The core with a single line leaving the system outward — an arc breaking the outer ring and carrying an arrowhead away. The first thing that acts on the world. |
| 6 | `hos-life-result.png` | Life Result | The outward line curving all the way back and re-entering the core. The circuit closed. This is the one that must read as *return*. |

**The test for the set:** placed in order, 1 through 6, a viewer should be able to see that
something begins simple, accumulates structure, reaches outward, and comes back. If icon 6
does not obviously close what icon 5 opened, the sequence has not worked.

---

## 2 · Learning Path — 5 icons

Michael's own progression, from the home page section *Begin where you are*. The
implementation brief calls for a mountain/pathway treatment here, so these read as
**waypoints on an ascent** — each one higher and more complete than the last.

These are the real tier names and what each actually contains:

| # | File | Tier | What it depicts |
|---|---|---|---|
| 1 | `path-01-introduction.png` | Free introduction — The Five Laws of Manifestation | An open threshold: two uprights and a lintel, or a simple arch, with one star visible through the opening. The way in. Costs nothing, asks nothing. |
| 2 | `path-02-recognition.png` | Recognition — Foundation Studies, thirty Patterns | A repeating waveform where one crest is circled. Seeing the pattern you were already inside. Not judgement — recognition. |
| 3 | `path-03-focused.png` | Focused study — Concepts, Patterns, Families, Interwoven Studies | A field of small equal points with one selected, larger and ringed. Choosing the Concept relevant to your life rather than following a fixed order. |
| 4 | `path-04-deeper.png` | Deeper understanding — The Human Operating System, Body Symbology | A cross-section: three nested arcs cut open on one side so the interior layers are visible. Seeing the mechanism, not the surface. |
| 5 | `path-05-comprehensive.png` | Comprehensive education — The Schools | A constellation: six points joined into one connected figure. Many courses forming a single body of understanding. |

**Note on 5:** six points, not five — it stands for the six Schools. That is deliberate and
worth keeping.

---

## 3 · Concept Library — 5 icons, and a recommendation against 12

**You asked me to identify which Concepts benefit from icons. My answer is: none of them
individually — and the Families do.**

Here is the reasoning, because it changes what you generate.

The launch library is 11 named Concepts and grows to roughly 50. Four of the current
eleven are *Unworthiness, Inadequacy, Inferiority and Undeserving*. These are close
neighbours by design; they sit in the same Family precisely because they are met together.
A distinct icon for each would have to invent a visual difference that the teaching does
not claim, and a viewer would not be able to tell them apart at 32px anyway. An icon that
cannot be distinguished from the one beside it is not navigation — it is noise, and it
implies a distinction that is not there.

There is also a scale problem. Eleven bespoke icons is a pleasant afternoon. Fifty is a
permanent commitment to commissioning a new icon every time Michael names a Concept, and
the set will drift in style as it grows.

**The Concept Families solve both.** There are four, they are genuinely distinct, every
Concept belongs to one, and a Family icon is inherited by every Concept inside it. Twelve
chips still get iconography; fifty will too; nothing new needs drawing when the library
grows.

| # | File | Family | What it depicts |
|---|---|---|---|
| 1 | `family-acceptance.png` | Acceptance | Two arcs curving toward one another and meeting cleanly — a form opening to receive. Holds *Rejection, Approval, Self-Rejection.* |
| 2 | `family-worth.png` | Worth | A balance: one horizontal beam on a central fulcrum, level, with a star suspended beneath the centre. Weighing, and the thing weighed. Holds *Unworthiness, Inadequacy, Inferiority, Undeserving.* |
| 3 | `family-control.png` | Control | A closed hexagon or tight ring with radial spokes holding it rigid. Structure imposed and gripped. |
| 4 | `family-trust.png` | Trust | Two separate rings overlapping so their intersection forms one shared shape. Something held in common. Holds *Suspicion.* |
| 5 | `family-unassigned.png` | Not yet assigned | A dashed or broken ring around an empty centre. Deliberately incomplete. |

**On the fifth icon.** Three of Michael's twelve Concepts — *Abandonment, Shame,* and
*Fear and Doubt* — appear in none of his four Family lists. The site currently shows them
under "Family not yet assigned" rather than placing them by guess. This icon is what that
state looks like, and it should look unresolved on purpose. When Michael places them, it
disappears.

---

## 4 · Utility and site icons — 12 essential, 6 optional

### 4a · Gate states — 4 icons · essential

The Foundation Course gates study, and every Study, Collection, Family and School carries
one of four states. These are load-bearing: they are how a visitor knows where they stand.

**Tone matters more here than anywhere else in the set.** The gate stops study, never
browsing or buying, and nothing may imply the visitor is behind. A padlock is the wrong
answer — it says *you are shut out.* The correct feeling is *not yet begun.*

| File | State | What it depicts |
|---|---|---|
| `state-open.png` | Available now | An open ring with a clear gap at the top, star at centre. Nothing closing it. |
| `state-locked.png` | Opens after the Foundation | A ring not yet joined — two arcs approaching but not touching, star at centre still fully visible. **Not a padlock, not a chain, not a barrier.** |
| `state-progress.png` | In progress | A ring drawn about two-thirds round, the remaining third absent. Plainly underway. |
| `state-complete.png` | Complete | A closed ring with a check inside. The only icon in the whole set that may use a check mark. |

### 4b · What a thing is — 8 icons · essential

Every card on the site carries a kicker naming its kind. These are the actual kinds in use,
counted from the built pages — they appear hundreds of times and are the highest-value
icons in the set after the Human Operating System.

| File | Kind | What it depicts |
|---|---|---|
| `kind-concept-study.png` | Concept Study | A single star with one ring. Matches `hos-concept` / `hos-belief` deliberately. |
| `kind-pattern-study.png` | Pattern Study | A looping line that crosses itself once. Matches `hos-pattern`. |
| `kind-collection.png` | Interwoven Study / Collection | Three strands braided over and under. |
| `kind-family.png` | Concept Family | Four small rings sharing one overlapping centre. |
| `kind-course.png` | Course | Five points rising, joined by one line — an ascending path. |
| `kind-school.png` | School | Six points evenly spaced on a single ring. |
| `kind-book.png` | Book / written edition | An open codex in pure line, two facing leaves, no shading. |
| `kind-event.png` | Seminar / live event | A ring of small points around one larger central point. People gathered — **abstract, never figures.** |

### 4c · Membership benefits — 6 icons · optional, do last

Three tiers carry twenty-three separate benefit lines between them, which is far too many
for individual icons. These six cover the recurring kinds and can be reused across all
three tiers.

| File | Benefit kind |
|---|---|
| `benefit-credit.png` | Purchase credits — a ring with a smaller ring inside it, like a token |
| `benefit-presentation.png` | Featured presentations and recordings — a play triangle inside a ring |
| `benefit-session.png` | Q&A sessions and consultations — two arcs facing each other in conversation |
| `benefit-pricing.png` | Member pricing — a tag outline with a star in place of the hole |
| `benefit-archive.png` | The archive and downloads — three stacked horizontal lines inside a ring |
| `benefit-certificate.png` | Certificates and recognition — a rosette: a small ring with two ribbon lines below |

---

## 5 · Do not generate these

The site already draws these in CSS, at a couple of hundred bytes each, perfectly crisp at
every size and in every colour state. An image file would be larger, blurrier, and worse.

- Chevrons and carets on the navigation doors
- The accordion and path expand/collapse plus
- The arrow on text links
- Check marks in the "includes" and "what this opens" lists
- The breadcrumb separator
- The search glyph, the menu burger, and the drawer close X (already clean inline SVG)

If ChatGPT offers these, skip them.

---

## 6 · Counts and order

| Batch | Icons | Priority |
|---|---|---|
| 1 · Human Operating System | 6 | Essential — the home page's centrepiece |
| 2 · Learning Path | 5 | Essential |
| 3 · Concept Families | 5 | Recommended, replacing 12+ per-Concept icons |
| 4a · Gate states | 4 | Essential |
| 4b · What a thing is | 8 | Essential — highest usage on the site |
| 4c · Membership benefits | 6 | Optional |
| | **34** | |

The implementation brief asked for 12–20. Batches 1, 2 and 4a come to 15 and are the ones
that carry meaning the page cannot say in words. Everything after that is real but
deferrable — stopping at any batch boundary leaves a coherent set.

---

## 7 · What happens when the files arrive

Drop them anywhere and I will handle the rest:

1. Trim and normalise each one to a consistent optical size and a square frame.
2. Convert to SVG where the line work traces cleanly, so it scales without any raster at
   all; keep the PNG as a mask elsewhere.
3. Wire them as CSS masks so each takes its colour from a brand token — gold inside dark
   sections, bronze on the light page where flat gold measures 1.55:1 and fails, teal on
   hover, muted when a Study is locked.
4. Build the circular containers, rings, glow and hover states in CSS, per your note.
5. Ship at three sizes with the right cut at each, and check every one against the page at
   390, 768, 1024 and 1440.

---

## 8 · One thing the brief settles, and one it raises

**Settles:** the implementation brief specifies the six-stage chain — Concept → Belief →
Pattern → Emotion → Behavior → Life Result. That has been an open question since Michael's
pricing document described a five-stage version, and the ring on the home page has been
drawn but unconfirmed. The brief confirms it. Good — the ring stands as built, and batch 1
is safe to generate.

**Raises:** the brief's palette and typography differ from what is live. It specifies Deep
Navy `#0B1A2F`, Teal `#0FA79C` and Inter; the site runs Amethyst `#5B4A9E`, Bronze
`#836919` and Source Sans 3. Teal on the cream ground measures about 3.0:1, which fails
normal body text, so it wants to be an accent and an icon colour rather than a type colour.
None of this blocks the icons — monochrome assets work with either palette — but it is a
decision to make before the redesign pass, not during it.
