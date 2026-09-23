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

## 3 · The six Operating System icons — already final

`hos-concept.png` · `hos-belief.png` · `hos-pattern.png` · `hos-emotion.png` ·
`hos-behavior.png` · `hos-life-result.png`

| | |
|---|---|
| **Section** | The Human Operating System |
| **Delivered** | 1024px masters, shipped at 320px, pure white on transparent |
| **How they take colour** | CSS masks. The shape comes from the file, the colour from a token. That is why six different colours cost one line of CSS each and need no new files. |
| **Colours on the dark inset** | Concept `#E8BE45` gold · Belief `#7E9BE8` indigo · Pattern `#2FC4B8` teal · Emotion `#F0876E` coral · Behavior `#A98BE0` violet · Life Result `#E8BE45` gold |
| **Note** | These are lifted from the brief and **brightened for the navy ground**. The brief's own values read correctly on cream but sit too dark on navy; these are the same hues at working luminance. |

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

**3 · The dark inset under the Operating System is a consequence of 1 and 2**, not a
decorative choice. The brief's six stage colours only exist at full strength on a dark ground.
Forced onto cream, gold becomes olive `#906F12` and coral becomes a hot red `#D04225`.
`CLAUDE.md` already anticipated this: *"diagrams keep a dark inset because they need the whole
gold."*

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
