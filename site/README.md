# The Institute — static build

Plain HTML, CSS and one file of vanilla JavaScript. No framework and no dependencies —
the only build step is a short Python script that stamps the shared chrome onto each
page, and its output is committed, so the site runs with or without it.

```bash
python build/build.py && python -m http.server 4477 --directory site
```

```bash
python build/audit.py
```

`audit.py` fails if any internal link points at a route that does not exist, and
reports how many "Awaiting Michael" placeholders are left and where. It is the
list to hand him.

**`site/` is generated. Do not edit it by hand** — the next build overwrites it.
Pages are written in `../src/`, the chrome lives in `../build/partials/`.

```
../src/<route>.html   a page: front matter, <main>, an optional tail block
../build/partials/    header.html · drawer.html · footer.html — one copy each
../build/build.py     assembles the two into site/. ~120 lines, no dependencies

site/index.html       generated
site/styles.css       tokens, components, sections, motion — commented by section
site/study.css        catalogue: study, collection, index, course templates
site/app.js           doors, drawer, the ring readout, the path, reveal
site/assets/          the shipped cuts. Masters live in ../assets/masters/
```

Adding a page is one file in `src/` and one run of the build. The header, the
mobile drawer and the footer are written once; changing a nav link changes it
everywhere. The build also marks the link to the current page with
`aria-current="page"`, so the header says where you are to a screen reader.

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

## Content — Michael's material of 11 Sep 2026

The home page, the Study, Collection and Membership templates all now run on his real
catalogue rather than the placeholder sets:

- **Four Courses** — Five Laws, Foundation Studies, the Human Operating System, Body Symbology.
  The Human Operating System and Body Symbology moved out of Books; Extended Foundation,
  Awakening of Consciousness and T.J. are out of launch.
- **Twelve Concepts** (eleven named), **twelve Patterns**, **four Concept Families**.
- **Six Schools**, in the order he recommends, with his own one-line descriptions. They are
  numbered now: they used to be a set and were deliberately unnumbered, but he gave an explicit
  opening order and a reason for it, and `DESIGN.md` says number what is genuinely sequential.
- **Weaves are "Interwoven Studies"** — his own name for them, from the pricing sheet.

**Deliberately not changed: the Operating System ring.** The Member Pricing document states the
chain as *Concept → Expectation → Pattern → Experience → Validation*; the ring draws his earlier
*Concept → Belief → Pattern → Emotion → Behavior → Life Result*. Five stages against six.
Redrawing it before he says which is current would be a guess, and it is the most prominent
thing on the page.

Three other answers are still open — whether the Foundation gate survives the $6.99 standalone
Study, whether the member price is one figure or three, and what a purchase credit buys. All are
set out in the launch-model document with the smaller gaps.

## Verified

390 / 768 / 1024 / 1440 with no horizontal overflow · both fonts loading with `opsz` set at
every step · visible focus ring on every interactive element · motion inside
`prefers-reduced-motion` · keyboard pass through the header, the ring and the path.

**A note on previewing.** `IntersectionObserver` does not fire in a backgrounded tab, so the
reveal animations and the ring draw stay dormant until the page is actually visible. If a
screenshot tool shows the page faded or inert, that is why.

## Routes

**Every internal link resolves.** 67 pages, 66 routes, 5,229 internal links, no
dead ends. `build/audit.py` enforces that.

```
/                              home
/concepts                      twelve Concepts, filterable by Family
/concepts/<slug>               11 Concept Studies
/concepts/families             the four Families
/concepts/families/<slug>      Acceptance · Worth · Control · Trust
/patterns                      twelve Patterns of Behavior
/patterns/<slug>               12 Pattern Studies
/collections                   Interwoven Studies
/collections/<slug>            4 sets
/courses                       the four Courses
/courses/<slug>                Five Laws · Foundation · HOS · Body Symbology
/schools                       six Schools, in Michael's order
/schools/<slug>                6 School pages
/books, /books/<slug>          2 books, 2 kinds of study material
/events, /events/<slug>        2 seminars
/membership                    the three tiers
/about /michael /contact       the Institute
/begin/the-path                how the education fits together
/legal/terms /privacy /refunds
/account /cart                 the application layer
404.html                       served for any unmatched address
```

**The host must be told to serve `/404.html`** for addresses it cannot match.
Without that, a wrong URL gets the host's own bare error page rather than the
Institute's. Most static hosts do this automatically for a root `404.html`;
confirm it on Sevalla.

### What is real and what is scaffold

Three kinds of page, and the difference matters when reading the site:

1. **Written** — home, the four Courses, the three indexes with real data, the
   Unworthiness Study and its Collection, Membership, the 404.
2. **Generated from Michael's names** — the 11 Concept Studies, 12 Pattern
   Studies, 6 Schools, 4 sets. Real names, real prices, real structure; the
   descriptions are placeholders. Written by `build/make-library.py`.
3. **Route only** — books, events, about, michael, contact, legal, account,
   cart. A real page at a real URL saying plainly what is missing. Written by
   `build/make-stubs.py`.

Neither generator overwrites a file that already exists, so replacing a
placeholder means editing its `src/` file and never running the script again for
that page.

**141 placeholders across 62 pages.** That is the backlog, and it is visible on
the site on purpose — `CLAUDE.md` says ship the route, ship a clear placeholder,
do not invent copy. The legal pages go further and say the text is not ours to
draft, because a plausible-looking placeholder there invites someone to ship it.

The Concepts index filter surfaces a real gap rather than hiding it:
**Abandonment, Shame, and Fear and Doubt appear in none of Michael's four Family
lists**, so they sit under "Family not yet assigned" instead of being quietly
placed in one.

The Course template flexes rather than branching: a free course, a ten-week
programme, a study in two editions and an eBook at three depths are all the same
page with different blocks filled. Foundation is the only one numbered, because
ten weeks in order is the only part of the catalogue that is genuinely sequential.

**No Course is gated.** The Foundation is the gate, and a Course page therefore
says what completing it *opens* — never what is closed against you.

## Not built yet

The other sixteen templates in `STRUCTURE.md`. The Concept page is the one that matters —
24 at launch, ~50 complete, and the likeliest search landing page.
