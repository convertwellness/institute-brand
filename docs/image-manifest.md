# Image Asset Manifest

Homepage redesign, first pass. 23 Sep 2026.

Every slot below is live on the page with a **temporary image** in it, generated to the brief
so there is something real to review. Replace the file at the same path and nothing else needs
to change — the containers are responsive, the crops are handled by CSS, and no image carries
baked-in text.

**A note on what a good hero costs in scrim.** Sara's image needed far less
darkening than the one generated before it, because its left third is genuinely dark. The
gradient dropped from 92% to 62% and the mountains came back. That is the practical value of
the safe area below: the darker the left, the more of the picture survives.

**Two rules that apply to every asset.**

1. **No text, lettering, watermark or signature in the image.** All type is live HTML.
2. **No baked-in darkening or scrim.** The hero's gradient is CSS, so the picture can be
   swapped, re-cropped or lightened later without a designer reopening the file.

---

## 1 · `hero-tree-cosmos.webp`

| | |
|---|---|
| **Section** | Hero — the page's first immersive moment |
| **Purpose** | The Tree of Life as symbolic focal point against a night sky. Expansive and contemplative, not psychedelic. Replaces the glowing human silhouette. |
| **Desktop** | 2200 × 1238 (source 1672 × 941) |
| **Mobile** | Same file. CSS crops it — no second asset needed |
| **Aspect ratio** | 16 : 9 |
| **Object position** | `62% 50%` — the frame is pulled right so the tree clears the type |
| **Safe area** | **The left 42% must stay quiet and dark.** The headline, body, both buttons and the supporting line sit there. A CSS gradient darkens it further, but it cannot rescue a busy or bright left third. Keep the subject right of centre. |
| **Alt-text intent** | Describe what is actually in the frame — the tree, the sky, the horizon. Not "spirituality" or "consciousness". |
| **Current file** | **Sara's, 23 Sep — in use.** A great tree lit from within on a rocky outcrop, spiral galaxy above, valley of mountains, mist and water falling away left. Measured: white type over the left 42% reads 14.7:1 at the 90th percentile and 9.6:1 at the 99th, so the quiet zone is genuinely quiet and the scrim could be lightened from 92% to 62% — the landscape now shows through instead of being hidden. |

---

## 2 · `path-horizon.webp`

| | |
|---|---|
| **Section** | Begin Where You Are |
| **Purpose** | A restrained landscape anchoring the five waypoints. Atmosphere, not subject. |
| **Desktop** | 2400 × 1047 |
| **Mobile** | Same file, full width at 14% opacity |
| **Aspect ratio** | ~ 2.3 : 1, flexible — it is masked on all four edges |
| **Placement** | Held to the **right 58%**, faded in from the left, veiled in cream, 22% opacity |
| **Safe area** | **The left 42% is type.** All five waypoints and the closing line live there. Anything busy on the left will show through the veil. A horizon low in the frame works best. |
| **Alt-text intent** | Decorative — ships with `alt=""` and `aria-hidden`. The section reads identically without it. |
| **Current file** | Cut from the left of the hero frame — the mountains, lake and mist, with the tree outside the crop. Distinct from the hero without being a second commission, and they agree because they are the same photograph. Replace if you want the path to carry its own place. |

---

## 3 · The six Operating System icons — final, 23 Sep

`hos-concept.webp` · `hos-belief.webp` · `hos-pattern.webp` · `hos-emotion.webp` ·
`hos-behavior.webp` · `hos-life-result.webp`

| | |
|---|---|
| **Section** | The Human Operating System |
| **Delivered** | 1254 × 1254 RGBA, full colour and dimensional. Masters kept at source size in `assets/masters/icons/stage/`; shipped at 480 × 480 WebP, ~55 KB each, 334 KB for the set |
| **Subjects** | 01 Concept, gold compass star · 02 Belief, blue profile filled with a constellation · 03 Pattern, teal figure of eight · 04 Emotion, coral heart · 05 Behavior, violet winding path · 06 Life Result, gold sun |
| **Rendered at** | 130px at 1440 · 123px at 1366 · 92px at 1024 · 100px at 768 · 72px at 390. Two clamps, not one: stacked they scale off viewport width steeply, six-across they cannot. |
| **Rules honoured** | Shipped as real `<img>` with explicit width and height, `object-fit: contain`, no CSS recolouring, no background behind them, outer beaded geometry never cropped, never upscaled past 480 |
| **Alt text** | Each describes its own artwork — "a teal figure of eight, one continuous line crossing itself at the centre" — rather than naming the doctrine, which the adjacent label already carries |

**The earlier monochrome masks** (`hos-*.png`) are superseded and no longer referenced.

**No descriptors under the names.** The brief allowed an optional short descriptor and asked
to check the source first. Michael has written Concept, Belief and Pattern; Emotion, Behavior
and Life Result have nothing. Rather than label three and leave three bare — or invent the
missing three, which would be writing doctrine — the icon row carries number and name only,
and the readout beneath reveals his sentence where one exists and says plainly where one does
not.

## 4 · `path-journey.webp` and `path-journey-tall.webp`

| | |
|---|---|
| **Section** | Begin Where You Are |
| **Purpose** | The journey itself. Not a backdrop — the five stages are placed *in* the landscape, climbing from the foreground path to the horizon. |
| **Desktop** | 1586 × 992, shown full width below the ivory introduction |
| **Mobile / tablet** | `path-journey-tall.webp`, 1100 × 1146 — the left 60% of the same frame, so the path, lake and mountains survive a narrow screen instead of being squeezed |
| **Aspect ratio** | 1.6 : 1 desktop · 16 : 11 crop below 1280px |
| **Safe area** | There isn't one in the usual sense. The five stops are positioned against a **luminance map of the photograph** — every seat was measured, and all five land where white type reads 4.8:1 to 7.9:1 on the bare image. Replacing the photograph means re-measuring; the positions are `--x` / `--y` percentages on each `.stop`, and the trail path in the SVG must move with them. |
| **Alt-text intent** | Describe the place: the path, the mist, the lake, the mountains. |
| **Treatment** | **No global scrim.** A faint bottom gradient only, plus one soft ellipse behind each stop at 46% navy — enough to lift words off leaf and rock detail, not to rescue contrast. The sky, mist and depth are untouched. |

---

## Still to come — later passes

Slots not yet built. Listed so the imagery can be commissioned in one batch.

| Filename | Section | Purpose | Ratio | Notes |
|---|---|---|---|---|
| `explore-concepts.webp` | Explore the Institute | Concept Studies | 4 : 5 | Four distinct metaphors, not four galaxies |
| `explore-courses.webp` | Explore the Institute | Courses | 4 : 5 | |
| `explore-books.webp` | Explore the Institute | Books & Study Editions | 4 : 5 | |
| `explore-events.webp` | Explore the Institute | Live Events | 4 : 5 | Abstract — never photographs of groups |
| `library-field.webp` | The Concept Library | Second dark immersive moment, behind floating Concept names | 21 : 9 | Must stay quiet enough for a dozen words over it |
| `closing-twilight.webp` | Membership / closing | Final immersive twilight | 16 : 9 | Quiet and reflective, not salesy |

---

## Conflicts flagged rather than silently resolved

The brief asked for these to be raised rather than worked around.

**1 · Gold cannot be the emphasis colour on cream.** Flat Gold `#E8BE45` measures **1.71 : 1**
on cream — it fails even the relaxed large-text threshold, by a wide margin. On the navy
ground it is **9.84 : 1**. So gold is used exactly where it works: filled buttons and eyebrow
type on the dark hero, hairlines and rules on cream, and the star points on the path. Where
gold would have to carry text on cream it becomes **Bronze `#836919`, 5.07 : 1**. This is the
brand's own rule and the reason the site's warm accent has been bronze throughout.

**2 · Teal is a dark-ground colour.** `#0FA79C` is **2.88 : 1** on cream, which fails even
large text. It is live on the navy inset, where it is 5.82 : 1. A `--teal-ink` token
(`#0C827A`, 4.51 : 1) exists for the rare case it must sit on the page, but it is noticeably
duller and I have not used it yet.

**3 · The Operating System is light — resolved, 23 Sep.** The first pass put the diagram on a
dark inset because gold and teal fail on cream as *text*. Sara's direction was to keep the
section light, and on a second look the inset was answering the wrong question: these icons
each sit beside their name, so they supplement a label rather than carrying meaning alone.
That is the 3:1 graphics threshold, not 4.5:1 — and at 3:1 the hues hold. Only gold needed
moving, and only in lightness. The section is cream, with no inset, no discs and no cards.

**4 · Two system-wide changes, made deliberately.** The brief specifies Inter and a cream
ground; the site ran Source Sans 3 on white. Both are brand-system changes rather than page
redesigns, so they apply to all 67 pages. Every secondary page now renders cream with navy
Inter. **No secondary page has been redesigned** — only the tokens they inherit. Say the word
if you would rather they had stayed white until later.

**5 · One link I chose.** The hero's secondary call to action, "Explore the Institute", scrolls
to the Explore section further down the page rather than navigating away. The brief did not
say where it should go.

---

## Not touched

Sections five onward — Explore, the Concept Library, the Schools and the closing — are still
the previous design and will look inconsistent against the first four. That is the stopping
point the brief asked for.
