# Questions for Michael

Current at **24 Sep 2026**. Every item here corresponds to something visible on a
real page. Nothing is hypothetical, and nothing has been invented to fill a gap.

**Counts are not in this document.** They were, and they went stale within a day.
The live figures are on **[`/sitemap#work`](/sitemap#work)**, which is generated from the
pages themselves each time the site is built and therefore cannot disagree with
them. It ranks the areas by how much is still to write and marks every page
*Written*, *Draft standing in*, *Nothing yet* or *Held*. This document carries only
the things a generated page cannot know: the decisions, and the questions.

**How to read the priority column.** *Sells* blocks the catalogue from taking
money. *Ships* blocks a page from being finished. *Open* is a real question that
does not stop anything today.

---

## 1 · The pricing, which is now the largest single item

**Every price on the site is held.** As of 24 Sep the catalogue says "to be
confirmed" in 209 places across 45 pages, and no number appears in visible text
anywhere.

The reason is not that the numbers were wrong. It is that **none of them could be
sourced.** `content/site.ts` — which `CLAUDE.md` names as the source of every
string on the site — carries no prices at all, only Michael's definitions of
Public Price and Member Price. The figures came off a pricing document that was
never committed to this repository, and Michael has since said the pricing needs
to change.

The numbers come straight back with `python build/prices.py --restore`; the
round trip is byte-for-byte and the tool proves it before it writes.

| | Question | Priority |
|---|---|---|
| 1.1 | **The price list itself.** Every figure, re-issued, ideally as a file we can keep under version control rather than a document that goes out of date in an inbox. | Sells |
| 1.2 | **Does a Concept Study include its Patterns?** Michael, 24 Sep: *"the Concept do not include patterns. Concepts and patterns are separate offerings based on the concept chosen."* This is a product question as much as a copy one, and it may be the same decision as the price. | Sells |
| 1.3 | **Does the Foundation gate survive a standalone purchase?** Anyone may buy a Study today. If someone buys one before completing Foundation Studies, can they begin it, or does it sit in their account until the Foundation is done? | Sells |
| 1.4 | **One member price, or three?** The Membership Types document gives tiered discounts of 10 / 20 / 25 per cent. The Member Pricing document gives a single member price running 20–40 per cent below public. The site shows one member price per item. | Sells |
| 1.5 | **What does one purchase credit buy?** Institute Membership includes three. Is a credit worth one item of any price, one item up to a value, or a fixed sum? | Sells |
| 1.6 | **The Foundation-with-membership bundle.** Michael thinks it should be $169 rather than $179, from $149 plus a month. He is going from memory and will check. The underlying question is unchanged: **how much membership does it include, and for how long?** | Sells |
| 1.7 | **What "qualifying" means.** The site says members get preferred pricing on *qualifying* Courses, books and materials. Michael has marked this with a question mark, and it has never been defined. Is it everything, or a list? | Sells |

---

## 2 · Writing still needed

Volumes are on [`/sitemap#work`](/sitemap#work). What follows is what each piece has to say.

| | What | Priority |
|---|---|---|
| 2.1 | **Per-Concept text.** For each named Concept: one sentence defining it; how it influences perception; which Patterns it produces. His own six teaching headings are already the page structure. | Ships |
| 2.2 | **Per-Pattern text.** For each of the twelve Patterns: what it looks like from inside before it has a name; the sequence it follows and what sets it going; which Concept it was built to validate. | Ships |
| 2.3 | **The twelfth Concept.** Eleven of the top twelve are named. | Ships |
| 2.4 | **Foundation's ten weeks.** Which three Patterns fall in which week — thirty in all, twelve named. Also what a week consists of, and whether the ten weeks run to a calendar or at the student's own pace. | Ships |
| 2.5 | **The five Laws.** Their names, a line on each, and the format of the free course. It is the front door and the emptiest important page on the site. | Ships |
| 2.6 | **Books.** *Awakening* and *T.J.* have titles and nothing else. Same for the Workbooks, Awakening Portfolios and Video Studies. Books is the one category where nothing is sellable. | Sells |
| 2.7 | **The Schools.** The Course list inside each. He notes there is considerably more School material developed than the outline shows. | Ships |
| 2.8 | **Live Events.** Date, format, length, price and subject for each seminar. Only the two subjects have ever been given. | Sells |
| 2.9 | **About the Institute, his biography, and Contact.** Three pages that have to be in his voice. | Ships |

---

## 3 · Corrections he has raised, needing his words

| | What | Where |
|---|---|---|
| 3.1 | **"The whole of the method" is wrong, and it was ours.** `/courses/foundation` says *"A Pattern seen is already a Pattern that has lost some of its authority; that is the whole of the method."* Michael: identification is **step one in eliminating the Pattern**, not the method — on its own it changes nothing, and the Pattern keeps repeating. That sentence was written here, not by him. His replacement is wanted rather than another attempt at ours. | `/courses/foundation` |
| 3.2 | **Concepts do not include their Patterns.** The summary line *"Twelve Concepts to begin with, each with its Patterns"* appears on fifteen pages and reads as inclusion. The Concept detail pages already get it right — each Pattern is listed as its own Study. **What should the summary line say instead?** | 15 pages |
| 3.3 | **"Eliminate the 'may' everywhere."** Sixteen instances, and they are two different things. Five hedge the teaching — *"Patterns of Behavior **may** influence how we think, choose, relate and respond to life."* The rest are ordinary permissions — *"Material **may** be viewed for as long as the membership is active."* **Is the rule: remove it from statements about how the teaching works, keep it where it says what a customer is allowed to do?** | 16 places |
| 3.4 | **"Governs" is the wrong word.** Nothing says the Five Laws govern anything; what the site says, twice, is *"The **Foundation** governs when study begins, never what you may look at or buy."* Sara is choosing a replacement — *determines*, *sets*, *decides* or *opens*. | 2 places |
| 3.5 | **What he saw on `/patterns`.** His note reads *"Under 12 patterns you have eliminate me."* The word "eliminate" appears nowhere on the site, so it cannot be found from here. | `/patterns` |
| 3.6 | **The remaining capitalisation.** Two were found and fixed — *"The five Laws"* on the Five Laws page, and the hero saying *Patterns* in one sentence and *patterns* in the next. One is deliberately untouched: his own formula, *"Concepts influence beliefs, expectations, patterns, choices and life experiences,"* appears three times. Belief and Pattern are both stages of the Operating System, so by the brand rule they would be capitals — but it is his sentence, and capitalising *Patterns* while leaving *beliefs* lowercase would read as a typo. **His call on the whole phrase.** | 3 places |

---

## 4 · Structural questions the build surfaced

| | Question |
|---|---|
| 4.1 | **Fifteen Families or four?** The August architecture names fifteen: Acceptance, Freedom, Control, Emotional Expression, Belonging, Achievement, Safety and Protection, Responsibility, Relationship, Love, Identity, Worth, Trust, Truth and Communication, Spiritual Connection. September names four — and all four appear in the fifteen. **Are the four a launch subset?** If so that probably answers 4.2 as well. |
| 4.2 | **Three Concepts have no Family.** Abandonment, Shame, and Fear and Doubt appear in none of the four Family lists. The site shows them as unassigned rather than placing them by guess. |
| 4.3 | **How many Patterns are there really?** The Worth Family names six primary Patterns — Comparison, Perfectionism, Overcompensation, Self-Criticism, Self-Devaluation, Self-Sabotage. Only the first two are among the top twelve, so the library already runs to at least sixteen, and `/patterns` shows the top twelve rather than all. Is that the intention? |
| 4.4 | **Self-Criticism** is in the Worth Family list and in the Unworthiness collection, but is not one of the twelve. It appears without a link, since there is no Study to link to. |
| 4.5 | **Which three of the Worth Family's six** connect specifically to Unworthiness? The specification says each Concept carries three or six of its own. |
| 4.6 | **Body Symbology naming.** The pricing sheet says introductory / expanded / comprehensive. The books themselves are *Symbolic Body Atlas*, *Tier 2 — From Signals to Meaning*, and *The Mastery Atlas — Tier 3*. Someone buying "Tier 1" and someone buying "the introductory eBook" should not have to wonder whether they bought the same thing. |
| 4.7 | **Pattern Weaves — in or out?** Described fully in the August architecture, absent from the September navigation. The page exists and carries his description. |
| 4.8 | **T.J.** — in the launch set or not, and what does T.J. stand for? It appears in both the Courses row and the Books row of the original sketch. |
| 4.9 | **Video Studies and Special Topics** — under Books, or beside the Courses? The Human Operating System and Body Symbology already moved out of Books. |
| 4.10 | **The Schools.** The School of the Symbolic Body is in the August six but not the September six — does it return as a seventh? |
| 4.11 | **Written editions.** Which Studies have one? Where a written edition exists it is bought separately from the audiovisual Study, so the Study page needs to know. |
| 4.12 | **The wider catalogue.** The Body Symbology books list many more titles under The Body, The Mind and The Spirit — *Amino Acid Symbology*, *Autoimmune Diseases*, *Life Beginnings*, *The Seven Causes of Cancer*, *The Emotional Causes of Diseases*, *The Naturopathic Healing Handbook*, and others. Are any in scope for the Institute site? |
| 4.13 | **What happens to a seminar after its date?** Events are the one part of the catalogue that goes stale on its own. Does a past seminar disappear, or stay as a recording for sale? This decides whether an Event page outlives its date. |
| 4.14 | **Contact.** The Body Symbology books carry a publisher — Center for Universal Teachings Applied, Inc., with a street address and telephone number in San Antonio. **Should that go on the public site?** It has been left off pending his answer. |

---

## 5 · Waiting on a decision, not on writing

**The three Operating System stages are written and not yet live.** From his notes
of 24 Sep:

> **Emotion** — gives energy for Patterns to operate
> **Behavior** — actions to complete the Pattern
> **Life Result** — life validates the Concept as being true

The home page still says *"Michael has not written this stage yet"* in three
places, because one question is open first: the first three stages run a full
sentence or two each and these are clauses. **Set them as written, or expand them
to match?** Either answer puts them live the same day.

---

## 6 · Answered, so they are not asked twice

| | Question | Answer |
|---|---|---|
| 6.1 | **Which Human Operating System chain is current** — the five-stage version in the pricing document, or the six-stage version on the home page? | **Six.** Concept → Belief → Pattern → Emotion → Behavior → Life Result, confirmed by the September implementation brief. |
| 6.2 | **What separates the three Body Symbology depths?** | Answered by the books themselves: 56, 187 and 386 pages, each a distinct titled Tier. Only the naming (4.6) is still open. |
| 6.3 | **The Human Operating System lesson list** — ten lesson names were needed before individual lessons could be sold at $8.99. | **Withdrawn, 24 Sep.** Michael does not remember there being lessons and finds the option confusing. It never came from him; it came off the pricing sheet. The edition, the price, the table row and the placeholder are all gone. |

---

## A note on the draft copy now on the site

Most of the gaps above are filled with **draft prose that is not Michael's.** Sara
asked for it so the layouts could be judged with real text in them. Every piece
carries a visible "Draft" label, the original placeholder wording is kept in an
HTML comment beside it, and `python build/drafts.py --strip` removes all of it and
restores the placeholders verbatim. [`/sitemap#work`](/sitemap#work) marks every page that is
standing on it.

The draft copy describes structure using only vocabulary Michael has already
established. It asserts no teaching, names no new Concept or Pattern, and invents
no price, date or count. **It answers none of the questions above.**

Four kinds of page were left honest and never filled:

- **Terms, Privacy and Refunds** — a plausible-looking legal page is the one piece
  of filler that could actually cause harm, because someone would ship it. These
  must come from the Institute and its advisers. Privacy also depends on decisions
  not yet made: what the enrolment layer stores, which payment processor is used,
  and whether there is analytics. Refunds is a real decision rather than
  boilerplate, because Studies are sold as permanent access and downloadable
  material.
- **Michael Schwartz** — a fabricated biography of a real person.
- **Your account** and **Cart** — these do not say Michael has not written them.
  They say a static site cannot do accounts, which is true and stays true.

## Not questions for Michael

Two gaps that are ours and Sara's rather than his:

- **Accounts, enrolment, progress and checkout.** The gate has nothing to read
  without a server. Every page is built and every buying path is drawn, but
  nothing transacts yet.
- **Sevalla.** The publish directory needs to point at `site`, and the host has to
  be told to serve `/404.html` for addresses it cannot match.
