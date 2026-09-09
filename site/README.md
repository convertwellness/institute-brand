# The Institute — static build

The home page, built as plain HTML, CSS and one file of vanilla JavaScript. No build
step, no framework, no dependencies. Open `index.html` or serve the folder.

```bash
python -m http.server 4477 --directory site
```

```
index.html    the page
styles.css    tokens, components, sections, motion — commented by section
app.js        doors, drawer, the ring readout, the path, reveal
assets/       the shipped cuts. Masters live in ../assets/masters/
```

## Where this stands

A light site — white ground, faintly lavender bands, charcoal text — carrying a set of
deep cosmic images. The rhythm is deliberate: rich plates on a quiet page, so the page
reads as luminous rather than dark. Michael's first note on the original build was that it
was *far too dark*; this answers that without giving up the cosmos.

## The two departures from the handoff

`CLAUDE.md` still describes the original plan. Both changes were Sara's, 1 Sep 2026.

**Static, not Next.js.** Everything on the marketing and catalogue side is static. The gate —
accounts, enrolment, per-lesson progress, the completion event at the end of Foundation
week ten — still needs a server, but that is the *study* layer, not the catalogue.

**A light shell.** The brand said dark-only. The site is now light, with the cosmos carried
by imagery and one gold band rather than by the ground. The full dark "Inner Cosmos" build
is preserved at commit `1e3406f` (`git show 1e3406f:site/index.html`).

## Colour

| | | on white | on band `#F6F5FA` |
|---|---|---|---|
| charcoal | `#16181D` | 17.8 | 16.6 |
| quiet    | `#5A6172` |  6.0 |  5.6 |
| amethyst | `#5B4A9E` |  7.2 |  6.7 |
| bronze   | `#836919` |  5.4 |  5.0 |

**Amethyst leads**; bronze is the warm second voice. Amethyst is the brand's own Starlight
`#B0A3C9` taken down far enough to carry type — Starlight itself is 2.06 on white and is
decorative only. Flat Gold `#E8BE45` is 1.55 and never touches a light ground as type; it
appears only inside imagery and as star points.

## The three set pieces

**The Operating System ring.** Michael's chain drawn as a closed loop, Life Result returning
to Concept. Each stage is a real button — hover on a pointer, tab to it, tap it — and the
readout underneath is a live region. Below 800px it becomes a vertical chain with the return
leg up the left. **Three of the six stages carry a visible placeholder**: Emotion, Behavior
and Life Result have no description from Michael yet, and the page says so rather than
inventing copy.

**The path.** Five tiers that open on hover or click. Height animates through
`grid-template-rows: 0fr → 1fr`, so there is no guessed `max-height` and no jump when copy
length changes.

**The library band.** A warm gold light on cream — not a photograph — carrying the counts,
which are three doors that bloom and reveal a line of description on hover.

## Imagery

Six cosmic plates, all generated with OpenArt (Nano Banana Pro) and sharing one language:
a deep violet galaxy, fine luminous linework, and a single warm star. The hero is the seal's
own idea — a figure outline in the cosmos with a star at its heart.

Masters for everything in use are in `../assets/masters/` as full-resolution WebP.

**Raw PNG output is gitignored.** Thirty-eight generations, about 180 MB, most of them
rejected explorations — too heavy to carry in git history forever. Nothing live depends on
them; the prompts that made them are in `../docs/imagery-directions.md`.

The mark is filled with a galaxy at every size, masked over `galaxy-figure.webp`.

## Verified

390 / 768 / 1024 / 1440 with no horizontal overflow · both fonts loading with `opsz` set at
every step · visible focus ring on every interactive element · motion inside
`prefers-reduced-motion` · keyboard pass through the header, the ring and the path.

**A note on previewing.** `IntersectionObserver` does not fire in a backgrounded tab, so the
reveal animations and the ring draw stay dormant until the page is actually visible. If a
screenshot tool shows the page faded or inert, that is why.

## Not built yet

The other sixteen templates in `STRUCTURE.md`. The Concept page is the one that matters —
24 at launch, ~50 complete, and the likeliest search landing page.
