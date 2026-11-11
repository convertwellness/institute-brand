# Questions for Michael

Current at **Nov 11, 2026**. This replaces the Sep 24 list. The open items O1 to O13 come from the
Nov 11 layout brief; every page that is waiting on one shows its number in an "Awaiting Michael" or
"Open question" note, so a page and this list can always be matched.

Live counts of what is still to be written, page by page, are on **`/sitemap`**, which is generated
from the pages each time the site is built.

**Prices are held.** Every figure lives in `content/pricing.json` and none is written into any page
until Michael confirms them (`python build/prices.py --show` puts them on the site in one step).

---

## The open items

| # | Question | Where it shows on the site |
|---|---|---|
| **O1** | **Pricing model.** The Nov 3 Price Menu has four tiers (Seeker, Explorer, Discoverer, Counselor). The Nov 5 revision notes have three, the first being Foundation Free. The names, prices and inclusions of tiers two and three in the Nov 5 model are unknown. Which is final? | `/membership`; every buying block ("Member prices to be confirmed (O1)") |
| **O2** | **Build sign-off.** The Phase 1 green light and the Stripe plus Supabase approach were on the Nov 6 agenda; no outcome is recorded. See `docs/portal-spec.md`. | `/scholarship` (how gifts are taken), `/scholarship/apply` (the form link) |
| **O3** | **Foundation gate.** Must a student finish the Foundation before studying a single study they bought? The gate is built as a switch and is **off** (`settings.foundation_gate` in `content/catalog.json`). | `/courses/foundation` |
| **O4** | **Love, Abandonment, Shame.** Is Love a standalone study, or only inside the Love Family? Which Family do Abandonment and Shame belong to? | `/concepts/families/love`, `/concepts/abandonment`, `/concepts/shame`, `/concepts/families`, `/concepts` |
| **O5** | **Counselor live sessions.** His fax: weekly consults by Michael and a second provider (written "Candly"; spelling unconfirmed). The Nov 3 Price Menu: one monthly live group session with Michael. Which, and how are they booked? | `/membership` (Counselor tier) |
| **O6** | **Old to new names.** Michael's list (old = new) is coming. Includes whether "Foundation" becomes "Institute Core Studies Program". The site uses the Price Menu's names meanwhile. | `/schools/concepts-and-beliefs`, `/schools/universal-teachings`, `/schools/symbolic-understanding`, `/courses/foundation`, `/courses/body-symbology` |
| **O7** | **Download caps by tier.** Does any tier have a limit on downloads? | `/membership` |
| **O8** | **School list.** Twelve folders against ten on the Price Menu. Are Belonging and Relationships Schools of their own? Do Relationships and Human Relationships merge? And the order of all twelve: the site uses his August order for the first six, then the Price Menu, then the two folder-only Schools. | `/schools`, `/schools/relationships`, `/schools/human-relationships`, `/schools/belonging` |
| **O9** | **Track content.** The three Personal Mastery lessons, the six Holistic Health Educator modules, and the Track 3 titles. Does Nutritional Concepts I belong to Track 2? | `/begin/personal-mastery` and its lessons, `/learn/holistic-health-educator` and its modules, `/learn/wholistic-essays` |
| **O10** | **Institute name in the Membership Rules.** The Rules still say "Institute of the Spiritual Science of Human Patterns". The site now uses **The Michael Schwartz Institute for Wholistic Education** everywhere. The Rules document needs the same change. | Not on the site |
| **O11** | **Refund policy wording**, and how to cancel, pending attorney review. | `/membership` ("Pending legal review") |
| **O12** | **Video counts and placement.** 93 catalogued videos, about 40% duplicate. No count is published. Which Mindfulness cut ships? Which titles are the voiced Pattern videos? | `/eightfold-path`, `/patterns`, the greeting slot on `/` |
| **O13** | **Missing files.** Identity School Week 1; the Discipline of Cycles PDF; the two orientation videos; the 8 Eightfold Path videos (if new); Bunny's Schools paperwork; the CamScanner notes and both outlines; anything in the new "Sara Four" folder; the files for the six Relationship Studies. | `/begin`, `/schools/identity`, `/universal-teachings/discipline-of-cycles`, `/relationships` |

## Found while laying out the site

Smaller questions that came up while building. None is guessed on the site; each shows as a note.

| Question | Where it shows |
|---|---|
| **Concepts from the earlier site.** Inferiority, Undeserving, Self-Rejection, Shame, and Fear and Doubt (as a Concept) are on the site from the August and September material but are not in the Nov brief's inventory. Do they stay? They are marked `"source": "earlier"` in `content/catalog.json`. | `/concepts` |
| **Fear and Doubt.** The Nov brief makes it a Pattern, Core Study 7 of the School of Fear, Safety and Trust. The earlier site also has it as a Concept. Keep both? | `/concepts/fear-and-doubt`, `/patterns/fear-and-doubt` |
| **The other Core Studies** of the School of Fear, Safety and Trust, and their order. Only number 7 is known. | `/schools/fear-safety-trust` |
| **Patterns from the earlier site.** Approval-Rejection, People Pleasing, Control, Denial, Avoidance of Responsibility, Guilt, Comparison, Perfectionism and Procrastination are not named in the Nov inventory. Are they among the 27 voiced videos? | `/patterns` |
| **The Interwoven Study names.** About 11 Concept weaves and 21 Pattern weaves are in the material; none is named in the brief. | `/collections/interwoven-concepts`, `/collections/interwoven-patterns` |
| **The Foundational Principles text** is in SARA THREE. It needs to be copied in, unedited. | `/begin` |
| **The Doctrine of Personal Responsibility** is on the Price Menu as free and "proposed". It is held, with no page. Ship it? | Not on the site |
| **Human Operating System Collection and video bundles**: no price on the menu yet. | `/collections/human-operating-system`, `/eightfold-path` |
| **Scholarship Fund wording**: anything Michael wants said about tax deductibility; and the address applications go to. | `/scholarship`, `/scholarship/apply` |
