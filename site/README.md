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

## Nov 11, 2026: the layout brief

Sara's Nov 11 brief (`.agents/inbox.md`, commit 629d008) supersedes the older docs where they
disagree. What it changed:

- **The name.** The Michael Schwartz Institute for Wholistic Education, everywhere. "The Institute"
  after first mention. The lockup image in the footer carried the old name, so the footer now sets
  the name as live text.
- **The library is data.** `content/catalog.json` holds every item (id, title, type, route,
  Family, School, formats, price key, status). `content/pricing.json` holds both tier models and
  every price. `build/make-catalog.py` writes the library pages, every index and every buying
  block from those two files. **Edit the data, not the page**: a page with `generated: catalog`
  in its front matter is rewritten on every run.
- **Prices are held.** `content/pricing.json` has `"display": "held"`, so no figure reaches any page.
  `python build/prices.py --show` puts every price on the site; `--hold` takes them off again.
  `make-catalog.py` refuses to write a page if a figure leaks while held.
- **Three tracks** (Personal Mastery, Holistic Health Educator, Wholistic Essays and Teachings),
  the **ten Concept Families** as five-piece packages, **twelve Schools**, and new areas:
  Relationship Studies, Universal Teachings, the Eightfold Path, Self-Guided Studies, the
  Scholarship Fund.
- **The Operating System** is now Michael's five-step loop (Nov 4 fax): Concept, Belief System /
  Pattern, Experience, Fulfilled Expectation, Validation of Concept. One copy, in
  `build/partials/os-loop.html`, dropped into a page with `<!-- OS-LOOP -->`. The six-stage ring
  is gone from the home page.
- **No em or en dashes in copy.** `build/audit.py` fails the build if one appears in visible text,
  or if the old name or old course names come back.
- **Open items O1 to O13** show on the pages that wait on them, numbered, and are listed in
  `docs/questions-for-michael.md`. The portal (accounts, payments) is specified, not built:
  `docs/portal-spec.md`.

To change the library:

```bash
python build/make-catalog.py
```

```bash
python build/build.py
```

```bash
python build/audit.py
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

**The Operating System loop.** Michael's five steps from his Nov 4 fax, drawn as a row on a
wide screen and a column on a phone, closing back on Concept. Step names only: he has not
written a line for each step, so none is shown.

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

**The Operating System.** Settled by Michael on Nov 4 (the five-step loop). The ring is gone.

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

**Every internal link resolves.** 149 pages at Nov 11. `build/audit.py` enforces that.

```
/                                   home: greeting video, three tracks, the loop, membership
/begin                              Begin Here: orientation, Five Laws, Personal Mastery, principles, loop
/begin/personal-mastery             Track 1, and /lesson-1 to /lesson-3
/begin/the-path                     how the education fits together
/concepts, /concepts/<slug>         Concept Studies, filterable by Family
/concepts/families, /<family>       the ten Concept Families, each a five-piece package
/patterns, /patterns/<slug>         Patterns of Behavior
/collections, /collections/<slug>   Interwoven Studies and collections
/relationships, /<slug>             six Relationship Studies
/learn                              Learn: tracks 2 and 3, courses, teachings, studies
/learn/holistic-health-educator     Track 2, and /module-1 to /module-6
/learn/wholistic-essays             Track 3
/courses, /courses/<slug>           Courses
/universal-teachings, /<slug>       Universal Teachings
/eightfold-path                     short videos
/self-guided-studies, /<slug>       the disease studies (not "webinars")
/schools, /schools/<slug>           twelve Schools (O8)
/books, /events                     unchanged
/membership                         rendered from content/pricing.json
/scholarship, /scholarship/apply    the Scholarship Fund
/about /michael /contact /sitemap
/legal/terms /privacy /refunds
/account /cart                      placeholders until the portal exists
404.html                            served for any unmatched address
```

**The host must be told to serve `/404.html`** for addresses it cannot match.
Without that, a wrong URL gets the host's own bare error page rather than the
Institute's. Most static hosts do this automatically for a root `404.html`;
confirm it on Sevalla.

### What is real and what is scaffold

1. **Written by hand** in `src/`: home, Begin Here, the Five Laws, the Foundation, the Human
   Operating System and Total Body Symbology Reference courses, the Unworthiness Study and its
   Collection, books, events, about, Michael, contact, legal, the site outline, the 404. The four
   hand-written course pages still carry their own buying block; moving them onto the data is the
   next step.
2. **Generated from `content/catalog.json`** by `build/make-catalog.py`: every other Concept,
   Pattern, Family, collection, Relationship Study, Universal Teaching, Self-Guided Study, School,
   track, the indexes, Membership and the Scholarship Fund. Real names and structure from Michael's
   files; every description is an "Awaiting Michael" note.
3. **Route only**: account and cart, until the portal exists.

`build/drafts.py` can still fill the placeholders with labelled draft copy for layout review.
On Nov 11 the drafts were taken out again, because the Nov brief says not to guess.

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
