# Sitemap & page inventory

**Updated Nov 11, 2026 from Sara's layout brief** (`.agents/inbox.md`). Where this file and the
brief disagree, the brief wins. The August route plan below the templates table is kept for history.

Five header doors, unchanged in number: **Begin Here, Explore, Learn, The Schools, Membership**,
plus Search and Sign in. The three tracks fit inside them.

Every library route is listed in `content/catalog.json` and written by `build/make-catalog.py`.
**149 pages at Nov 11.**

## Routes

```
Begin Here
/begin                                Orientation video (coming), Five Laws, Personal Mastery,
                                      Foundational Principles, the five-step loop
/begin/personal-mastery               Track 1: three free lessons          O9
/begin/personal-mastery/lesson-<n>    × 3                                  O9
/courses/five-laws                    Five Laws of Human Experience, free
/courses/human-operating-system       The five-step loop
/begin/the-path

Explore
/concepts, /concepts/<slug>           Concept Studies                      × 27 (3 more held, no page)
/patterns, /patterns/<slug>           Pattern Studies                      × 19
/concepts/families, /<family>         The ten Concept Families             × 10
/collections, /collections/<slug>     Interwoven Studies and collections   × 6
/relationships, /relationships/<slug> Relationship Studies                 × 6   O13

Learn
/learn                                Learn index
/learn/holistic-health-educator       Track 2: six-module certification    O9
/learn/holistic-health-educator/module-<n>                                 × 6
/learn/wholistic-essays               Track 3                              O9
/courses, /courses/<slug>             Courses                              × 8
/universal-teachings, /<slug>         Universal Teachings                  × 4
/eightfold-path                       Short videos                         O12
/self-guided-studies, /<slug>         Self-Guided Studies (disease)        × 10
/books, /events                       unchanged

The Schools
/schools, /schools/<slug>             Twelve-week programs                 × 12  O8

Membership
/membership                           Tiers from content/pricing.json      O1 O5 O7 O11
/scholarship, /scholarship/apply      The Scholarship Fund

Account
/account                              Dashboard: My Library, member orientation, progress,
                                      downloads, billing. Spec only: docs/portal-spec.md   O2
/cart
```

**Every study page carries the same buying block:** buy this study, buy its collection, or become
a member, with its formats (Watch, Self-guided, Written), its Concept Family and its Interwoven
Studies.

**Held, no page, not in navigation:** Stubbornness, Sacrifice, the standalone Concept of Love (O4),
and the Doctrine of Personal Responsibility. They stay in `content/catalog.json` with
`"status": "hold"`.

---

# The August plan (history)

Reconciled from Michael's educational architecture (19 Aug 2026) and his handwritten navigation
sketch (23 Aug 2026).

## Templates

| Template | Pages | Surface | Notes |
|---|---|---|---|
| Home | 1 | Shell | One sentence, one primary action, one secondary. |
| Begin Here | 1 | Shell | Free course, the path, the Operating System. |
| Index | 8 | Shell | Filter, sort, state badges. One template, eight uses. |
| **Concept** | **24** | **Page** | **The workhorse. Build this one properly.** |
| Concept Family | 8 | Page | Same template, different centre. |
| Concept Weave | 12 | Page | Draws the chain between three to six Concepts. |
| Course | 5 | Page | Curriculum, audio/video toggle, workbook, price, enrol. |
| School | 6 | Page | Mostly placeholder at launch. |
| Human Operating System | 1 | Page | Bespoke. The chain drawn once, referred back to. |
| Book | 4 | Page | Cover, sample, formats, price. |
| Event | 7 | Shell | Subject, date, Zoom registration, later the recording. |
| Membership | 1 | Shell | Public against member pricing. |
| Lesson player | — | Page | Presentation, transcript, reflection, exercise, next. |
| Account | 4 | Shell | |
| Editorial | 6 | Page | About, Michael, Contact, and the three legal pages. |
| Commerce | 3 | Shell | Cart, checkout, confirmation. |
| Utility | 2 | Shell | Search, 404. |

**Surface rule:** anything read at length sits on the Page. Anything scanned or operated stays on
the dark shell. The threshold is roughly 400 words.

## The Concept page

24 at launch, ~50 complete, and the likeliest search landing page. Section order — one to six are
Michael's own headings, seven to nine are what makes it a product:

1. The Concept, named, with one sentence of definition
2. How the Concept influences perception
3. The beliefs and expectations that form around it
4. Its three or six Patterns of Behavior, each with its presentation
5. Recognising the Patterns in everyday life
6. Opportunities for conscious change
7. The Family it belongs to, and the Weaves it appears in
8. The written edition, where one exists
9. Price — public and member — and its state

It links out to: one Family, zero to three Weaves, its Patterns, an optional book, and its price.

## Held open deliberately

**Pattern Weaves** (in his architecture, absent from his sketch) · **Video Studies** (no titles
yet) · the six **Schools** (real URLs and skeleton pages, so they can be filled and promoted to a
sixth top-level door without a rebuild).
