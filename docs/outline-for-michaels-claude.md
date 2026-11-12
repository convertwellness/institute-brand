# The Institute: outline for Michael's Claude

Prepared Nov 12, 2026 by Sara Anderson (Convert Wellness) with Claude Code.

## 0. What this document is for

Michael's Claude holds Michael's material. This document holds ours: what has been built, where it
lives, what we believe is true, and how we think the whole site should fit together, from the home
page to the purchase pages to the student dashboard.

**What we are asking Michael's Claude to do:**

1. Read what has been built (Section 2 explains how).
2. Check every statement in Sections 4 to 8 against Michael's own material.
3. Correct anything that is wrong, fill in anything marked **Open**, and say where each piece belongs.
4. Send back one final structure: front end, purchase flow and dashboard. Section 10 has a reply format.

**Ground rules:**

- **Michael loves the home page as it is.** Do not propose redesigning it. Suggestions about what
  it links to are welcome.
- Nothing on the live or staging site changes until Sara approves.
- Where Michael's material does not settle a question, say "unknown" rather than guess.
- Statuses used below: **Locked** (Michael confirmed in writing), **From notes** (our reading of his
  files, not yet confirmed), **Open** (needs his answer).

## 1. Sources we worked from

| Source | Date | What it is |
|---|---|---|
| Michael's handwritten answers (fax, 2 pages) | Nov 4 | His answers written on the Content Map and Portal Plan |
| Institute Site Update Planning doc (Google Doc) | Nov 4 | The plan he was answering: inventory, sitemap, product model, portal, 16 questions |
| 30-Min Friday Call Plan | Nov 6 | Built from his answers. The call notes captured only 6 seconds, so no outcomes are recorded |
| SARA THREE Dropbox upload | Nov 5 | Price Menu and Membership Tiers (Final, Nov 3), Membership Rules and Refund Policy draft, Scholarship Fund, Foundational Principles, Belonging Six Principles PDF |
| Michael's site notes, Sep 2026 | Aug to Sep | Definitions of Concepts, Patterns, Schools, Courses, and the six "unplaced pieces" (on the site outline page) |

**A caution on the library lists.** The names of new Concepts, Patterns, Relationship Studies and
self-study guides in Sections 5 and 6, the Scholarship Fund details, and the Seeker "up to $9" limit
come from an inventory of SARA TWO and SARA THREE in the Nov 11 assistant-written brief
(`.agents/inbox.md`). We have not checked them against the files themselves. They are marked
*(brief)* below. Please check each one against Michael's folders.

We do **not** have: the Nov 5 CamScanner revision notes, the Holistic Health Educator outline, the
Nutritional Concepts I outline, or the "Sara Four" folder. If Michael's Claude has them, they matter
(see Section 9, question 13).

## 2. How to see what has been built

### Option A: the staging site (public, no login, easiest)

**https://institute-brand-fvawt.sevalla.page/**

It is the current build exactly. Useful addresses:

| Address | What it gives you |
|---|---|
| `/` | The home page |
| `/sitemap` | The site outline: every page, how it nests, and how much of each is still to be written |
| `/search-index.json` | The full text of every page in one file, ideal for reading the whole site at once |
| `/membership`, `/concepts`, `/courses/foundation`, `/schools` | The main templates |

If Michael's Claude can fetch web pages, start with `/search-index.json` and `/sitemap`.

### Option B: the code repository (private)

**github.com/convertwellness/institute-brand**, branch `main`.

It is private. Three ways to give Michael's Claude read access, from simplest to tightest:

1. **Claude's GitHub connector.** If Michael has a GitHub account, Sara adds him to the repo, and he
   connects GitHub in his Claude settings. His Claude can then add this repo to a Project and read
   every file. Note: on a personal GitHub account, an invited collaborator can also push changes, so
   Michael's Claude should be told to read only.
2. **A read-only access token.** Sara creates a fine-grained GitHub token limited to this one repo
   with "Contents: read" only, and gives it to Michael's Claude (Claude Code) to clone with. It
   cannot change anything.
3. **A download.** Sara sends a zip of the repo, or just this document plus the files below.

### Files worth reading first

| File | What it is |
|---|---|
| `site/README.md` | How the site is built and why, in plain language |
| `STRUCTURE.md` | The sitemap as planned in August |
| `docs/questions-for-michael.md` | The Sep 24 question list (this document supersedes it) |
| `src/<page>.html` | The source of each page. `site/` is the generated output |
| `build/partials/header.html` | The navigation, written once and stamped on every page |
| `content/site.ts` | Michael's original strings and gaps, from August. Reference only; the pages do not read it |
| `.agents/inbox.md` | A Nov 11 layout brief written by an assistant. **Not adopted** (see Section 5.4) |

## 3. What exists today

### 3.1 The build

- Plain HTML, CSS and one JavaScript file. No framework, no database.
- `src/` holds each page; `build/build.py` adds the shared header, mobile menu and footer and
  writes `site/`. Staging (Sevalla) publishes `site/`.
- `build/audit.py` checks every link and counts the placeholders.
- Every price on the site says "to be confirmed". They were held on Sep 24 because none could be
  traced to a file; the old figures are kept in `build/prices-held.json`.
- Where Michael's words are missing, the page says so. 125 of those gaps currently show labelled
  "Draft" stand-in text (not Michael's writing); 16 show a plain "Awaiting Michael" note.
- **No accounts, no checkout, no dashboard.** `/account` and `/cart` are pages that say so.

### 3.2 The home page (keep)

In order: the hero ("A Deeper Understanding of What It Means to Be Human", with Start the Free
Course and Explore the Institute); the Human Operating System ring (six stages: Concept, Belief,
Pattern, Emotion, Behavior, Life Result); "Begin Where You Are", a five-step path across a landscape
(Five Laws, Foundation Studies, Concepts and Patterns, Human Operating System and Body Symbology,
the Schools); "Explore the Institute" (Concept Studies, Courses, Books and Study Editions, Live
Events); the launch library (12 Concepts, 12 Patterns, 4 Families); the Schools (six, dark band);
the closing invitation (free course, or membership).

### 3.3 The navigation

Five doors, plus Search and Sign in:

| Door | What it opens |
|---|---|
| Begin Here | Five Laws of Manifestation (free), Foundation Studies, The Human Operating System, the path; About, Michael, Contact |
| Explore | Concepts, Patterns of Behavior, Concept Families, Interwoven Studies |
| Learn | Courses (Five Laws, Foundation, Human Operating System, Body Symbology); Books (Awakening, T.J., Workbooks, Video Studies); Live Events (Arthritis, Cancer) |
| The Schools | Six Schools in Michael's recommended order |
| Membership | Single link |

### 3.4 Every page (68)

| Area | Pages | Notes |
|---|---|---|
| Home | `/` | |
| Begin | `/begin/the-path` | No `/begin` page of its own |
| Concepts | `/concepts` + 11: Unworthiness, Rejection, Approval, Inadequacy, Inferiority, Undeserving, Self-Rejection, Abandonment, Shame, Fear and Doubt, Suspicion | Unworthiness is the fully worked example. A twelfth slot is awaiting a name |
| Concept Families | `/concepts/families` + Acceptance, Worth, Control, Trust | |
| Patterns | `/patterns` + 12: Approval-Rejection, People Pleasing, Control, Fear and Doubt, Denial, Defensiveness, Avoidance of Responsibility, Guilt, Resentment, Comparison, Perfectionism, Procrastination | |
| Interwoven Studies | `/collections` + Interwoven Concepts, Interwoven Patterns, Unworthiness and its Patterns, The Worth Family | |
| Courses | `/courses` + Five Laws, Foundation Studies (10 weeks), Human Operating System, Body Symbology | |
| Schools | `/schools` + Human Patterns, Human Operating System, Identity, Concepts and Beliefs, Relationships, Consciousness | |
| Books | `/books` + Awakening, T.J., Workbooks and Awakening Portfolios, Video Studies | |
| Live Events | `/events` + Arthritis, Cancer | |
| Membership | `/membership` | Shows the older three tiers: Institute, Sustaining, Core Studies, with purchase credits |
| The Institute | `/about`, `/michael`, `/contact` | |
| Commerce | `/account`, `/cart` | Placeholders |
| Legal | `/legal/terms`, `/legal/privacy`, `/legal/refunds` | Held for the Institute's advisers |
| Utility | `/sitemap`, `/404` | |

### 3.5 What every study page already does

Each Concept, Pattern, Collection and School page has the same shape: name, one-line definition,
numbered sections, "where it belongs" links, and a buying panel (price, member price, Add to cart,
what is included, a membership note). The study pages also carry four states (open, locked, in
progress, complete) for the Foundation gate, shown today only as a mock-up.

## 4. What we understand to be true (please check)

| # | Topic | What we understand | Status |
|---|---|---|---|
| 1 | Human Operating System | Five steps: Concept, Belief System / Pattern, Experience, Fulfilled Expectation, Validation of Concept, looping back to Concept. Replaces the six-stage ring and the older Concept, Expectation, Pattern, Experience, Validation order (which the Price Menu still prints) | Locked (fax Q7) |
| 2 | Membership tiers | Seeker $5/mo ($50/yr), Explorer $18 ($180), Discoverer $29 ($290), Counselor $69 ($690). Annual is priced at 10 months | Locked (fax Q12, Price Menu Nov 3) |
| 3 | Tier benefits | Seeker: 1 free study a month (up to $9 *(brief)*), 1 short video, Community, 20% off. Explorer: one School at a time, Introductory Body Symbology eBook, 1 disease study a quarter, 30% off. Discoverer: everything in Explorer, full short video library, early access, 40% off. Counselor: everything included | Locked (Price Menu) |
| 4 | Counselor | Counselor level only for all-access. Capped at 120 a year | Locked (fax Q4, Q14) |
| 5 | Counselor sessions | Fax: weekly consults with Michael and "Candly". Price Menu: one monthly live group session with Michael, plus 50% off private sessions | **Open** |
| 6 | Joining | Instant. No application for membership. The scholarship application is separate | Locked (fax Q15) |
| 7 | Upgrades | Everything already spent counts toward bundles, courses and tier upgrades. Benefits start at once; the new rate bills next cycle | Locked (fax Q16, Rules) |
| 8 | Downloads | Written material may be downloaded and is kept after cancelling, for personal study. Presentations (voiced or self-guided) are stream or view only | Locked (fax Q13, Rules) |
| 9 | Locked items | Shown to everyone with the tier discount price. Unreleased items can be bought ahead at the member's discount | Locked (fax, Portal 4) |
| 10 | Protection | No shared logins, no copying, accounts can be suspended. Signed streaming with no download button. PDFs stamped with the buyer's name. Screen recording cannot be fully blocked on any site | From notes (confirm live) |
| 11 | Concept Families | Ten at launch: Acceptance, Achievement, Belonging, Control, Emotional Expression, Love, Relationship, Responsibility, Trust, Worth | Locked (Price Menu, fax Q8) |
| 12 | Ship or hold | Ship from SARA THREE. Fear and Doubt is Core Study 7 in the 18-part School of Fear, Safety and Trust. Hold Sacrifice, Stubbornness and Love (no files) | Locked (fax Q9) |
| 13 | New material | Short videos at $4.99 (Eightfold Path, body parts, vitamins, diseases), bundles to follow. Self-study guides, not "webinars". A Twelve Spiritual Gifts and Twelve Disciplines course at $20 | Locked (fax Q10), files pending |
| 14 | Orientation videos | Two new ones coming: one public, one for members only | Locked (fax Q11), files pending |
| 15 | Prices | Studies $7 to $9 public. Collections $17 to $30. Each School $40. Foundation of the Institute Course $80. Self Exploratory Course (a Foundation Study) $25. Five Laws free. Doctrine of Personal Responsibility proposed free | From notes (Price Menu) |
| 16 | Discounts or credits | Price Menu uses percentage discounts. A separate Credit guideline describes 3 credits a month, capped at 9. We recommend discounts only | **Open** |
| 17 | Foundation gate | Michael: "Good question, had same thought." No answer yet | **Open** |
| 18 | Refunds | Monthly: full refund of the first payment within 30 days, once. Annual: no cancellation or refund, 12 months' access, reminder 14 days before renewal | Locked in draft, attorney review pending |
| 19 | Build approach | Approach A: each student gets their own record (purchases, tier, School progress, release schedule), exportable to Excel any time. Answers his "awkward at scale?" question about Approach B | **Open** (needs his green light) |
| 20 | Name | The site uses **The Institute of The Spiritual Science of Human Patterns**. A Nov 11 brief proposed "The Michael Schwartz Institute for Wholistic Education"; Sara has not adopted it. Does that name appear anywhere in Michael's material? | **Open** |

## 5. The structure we propose, end to end

Marked: **Keep** (exists, no change), **Change** (exists, needs updating), **New** (to build).

### 5.1 Front end (the catalogue: anyone can read and buy)

```
/                                   Keep. Home page as Michael likes it. Only the ring changes to
                                    the five-step loop (4.1) and the counts update (12/12/4).
Begin Here
  /begin                            New. Public orientation video (when it arrives), Five Laws,
                                    the five-step loop, Foundational Principles (text in SARA THREE)
  /courses/five-laws                Change. Free course. Confirm its name (Manifestation or other)
  /begin/the-path                   Keep, update names
Explore
  /concepts, /concepts/<name>       Change. Add the SARA TWO and THREE Concepts (Section 6)
  /concepts/families/<family>       Change. 4 becomes 10, each a Family package
  /patterns, /patterns/<name>       Change. Add the new self-guided Patterns
  /collections/<name>               Change. Collection types from the Price Menu
  Relationship Studies              New. Six named studies, files not received (brief)
Learn
  /courses/<name>                   Change. Foundation of the Institute Course, Self Exploratory,
                                    Awakening of Consciousness, Universal Principles and Teachings,
                                    The Four Selves, Twelve Gifts and Twelve Disciplines,
                                    Total Body Symbology Reference
  Short videos                      New. Eightfold Path now; body parts, vitamins, diseases later
  Self-study guides (disease)       New (brief). Arthritis, Bone Health, Brain and Memory, Cancer, Cardiovascular,
                                    Diabetes, Digestive Health, Hypertension, Immune Health,
                                    Weight and Metabolic Health. How do these relate to /events?
  /books, /events                   Keep
The Schools
  /schools/<name>                   Change. 6 becomes 10 or 12 (Section 9, question 7), each with
                                    its parts (Fear, Safety and Trust has 18)
Membership
  /membership                       Change. The four Nov 3 tiers replace the three old ones
  Scholarship Fund                  New. Give and apply. Held by the Center for Universal
                                    Teachings, a 501(c)(3) (brief)
```

### 5.2 Purchase flow

```
Any study page
  Buying panel: buy this item | buy the collection it belongs to | become a member
  Shows public price and the member price for each tier; formats (Watch, Self-guided, Written)
      |
/cart              New (real). Items, tier discount applied if signed in, upgrade credit applied
      |
/checkout          New. Stripe Checkout. Annual memberships show the no-cancellation terms with
                   a checkbox before payment. Health disclaimer: educational, not treatment
      |
Confirmation       New. Receipt, and a link straight into My Library
      |
/account           New (real). The student dashboard (Section 7)
```

### 5.3 Back end

Student dashboard and admin dashboard, specified in Section 7.

### 5.4 Things we tried and set aside

On Nov 11 an assistant-written brief proposed a new name, three "tracks" (Personal Mastery,
Holistic Health Educator, Wholistic Essays and Teachings) and a new home page. It was built on a
branch and then withdrawn by Sara. **Please tell us whether the three tracks come from Michael**
(they are said to be in his Nov 5 CamScanner notes, which we no longer have) and where, if anywhere,
they belong. They are not in his Nov 4 fax.

## 6. Changes needed to what exists

| Page or area | Change | Depends on |
|---|---|---|
| Home ring, `/courses/human-operating-system` | Six stages become the five-step loop | Nothing (Locked) |
| Price Menu document | Still prints the older loop; update to match the fax | Michael |
| `/membership` | Three old tiers and credits become the four Nov 3 tiers | Q16 (discounts or credits) |
| Every price | Fill from the Price Menu, still held until Michael says "publish" | Michael's sign-off |
| `/concepts` | *(brief)* Add: Acceptance, Achievement, Belonging, Control, Expectation, Expectation and Pattern, Fear, Freedom, Guilt, Identity, People Pleasing, Safety and Protection, Success and Failure, Trust, Truth, Unforgiveness. Keep or drop: Inferiority, Undeserving, Self-Rejection, Shame, Fear and Doubt (as a Concept) | Michael |
| `/patterns` | *(brief)* Add: Inconsistency, Becoming Indispensable, Managing Others, Self-Sabotage, Modus Operandi, Worrying, Hypervigilance. About 27 voiced Pattern videos exist; titles needed | Michael |
| Concept Families | Add Achievement, Belonging, Emotional Expression, Love, Relationship, Responsibility. Each is a package *(brief)*: The Concept of X, Approval Pathway, Rejection Pathway, Personal Application and Review, Modus Operandi video | Families Locked; package From notes |
| Schools | *(brief)* Add Conscious Living, Fear Safety and Trust, Human Relationships, Universal Teachings, Symbolic Body; decide Belonging and Relationships | Section 9, question 7 |
| Course names | "Foundation Studies" becomes "Foundation of the Institute Course"? Michael's old = new list | Q5 |
| The six unplaced pieces | Universal Principles, Concepts, Twelve Gifts, Twelve Disciplines, Six Senses, Four Selves. The Price Menu now places several as Courses (Gifts and Disciplines, Four Selves, Universal Principles and Teachings). Confirm | Michael |
| Draft stand-in text | 125 blocks of placeholder prose, not Michael's. Replace with his words, or remove | His copy |
| Legal pages | Terms, privacy, refunds from the Rules draft after attorney review | Attorney |

## 7. Dashboard spec (short)

### 7.1 Student dashboard (`/account`)

| Part | What it does |
|---|---|
| Sign in | Email and password or a magic link. Instant join |
| My Library | Only what the student owns or their tier includes, grouped by type (Courses, Schools, Concepts, Patterns, Collections, videos, self-study guides), with progress. Counselor sees everything |
| Locked but visible | Related items show "Add for $X" at their tier price, or "Upgrade for the difference" with prior spend credited |
| Release schedule | What unlocks next and when (monthly members), and "buy ahead" at their discount |
| Lesson player | Streamed video (signed links, no download button); self-guided slides as images or a view-only PDF; reflection prompts; Personal Action Plan; mark complete |
| Downloads | Written material only, stamped with their name. Kept after cancelling |
| Member orientation | The members-only orientation video |
| Counselor | Live session schedule and booking (format **Open**, 4.5) |
| Billing | Card, invoices, change tier, cancel. Upgrade now, bill next cycle. Monthly downgrade at next billing date; annual only at renewal. 7 days' grace on a failed payment |
| Certificates | Counselor path title after coursework; School completion (to confirm) |

### 7.2 Admin dashboard (for Michael, Bunny and Sara)

| Part | What it does |
|---|---|
| Students | Search, view one student's record: tier, purchases, progress, release schedule |
| Access | Grant or revoke an item, comp a student, award a scholarship, suspend a shared account |
| Orders and invoices | Every purchase and subscription, refunds |
| Catalogue mapping | Which files belong to which product, and which tier includes it |
| Progress | Who is where in each School and Course |
| Export | Everything to Excel, any time (answers Michael's "own file/page/Excel" question) |

### 7.3 Rules the system enforces

Release pacing per tier (annual up front; monthly paced: one School week a week for Explorer and
Discoverer; one School a month for Counselor), Schools unlock in the Institute's order, unused
monthly free benefits do not roll over, the Counselor cap of 120 a year, prior spend counts toward
upgrades, and (if Michael says yes) the Foundation gate.

### 7.4 How we would build it

- **Approach A** (pending Michael's green light): keep the catalogue as it is; add a small app with
  Supabase (accounts and database) and Stripe (checkout and subscriptions). Stripe tells the
  database what each student has bought. Video on a streaming host (Bunny Stream, Mux or Vimeo).
- **Starting point for the screens:** Sara has a licensed admin template, Vireo (Tailwind v4 and
  Alpine; also ships a Next.js version). Its sign-in, customers, orders, invoices, checkout and
  data-table screens map closely onto the admin dashboard. The student dashboard would be restyled
  to the Institute's own look so it feels like the same place as the catalogue.

## 8. What needs to be built, in order

| Phase | What | Needs first |
|---|---|---|
| 0 | Settle this outline: names, the library list, Schools, prices | Michael's Claude's corrections |
| 1 | Update the existing site to match (Section 6), prices still held | Phase 0 |
| 2 | Accounts, Stripe checkout, entitlements, My Library, basic admin with Excel export | Michael's green light (4.19) |
| 3 | Lesson player, streaming, stamped downloads, release schedule, upgrades | Video host chosen; files |
| 4 | Counselor sessions, certificates, scholarship workflow, bundles | Answers to 4.5, Section 9 |
| 5 | Publish prices; legal pages; launch | Michael's sign-off; attorney review |

## 9. Open questions for Michael

1. **Build approach:** confirm Approach A (each student has their own record, Excel export any time), and the Phase 1 green light.
2. **Discounts or credits:** the Price Menu's 20/30/40% discounts, or the Credit guideline's 3 credits a month? (We recommend discounts only.)
3. **Foundation gate:** can someone buy and study a single study right away, or must they finish the Foundation first?
4. **Counselor sessions:** weekly consults with Michael and "Candly" (who, and spelling?) or one monthly group session? How do Counselors book? Does the 120-a-year cap go in the Rules?
5. **Download caps:** does any tier have a limit?
6. **Love:** standalone study, or only inside the Love Family? Which Family do Abandonment and Shame belong to?
7. **Schools:** 12 folders against 10 on the Price Menu. Are Belonging and Relationships Schools of their own? Do Relationships and Human Relationships merge? What order? Identity School Week 1 is missing.
8. **Names (old = new):** the list he promised. Does "Foundation" become "Foundation of the Institute Course"? Is the free course "Five Laws of Manifestation" or something else?
9. **The library list:** which Concepts and Patterns ship at launch (Section 6), and the titles of the voiced Pattern videos.
10. **The six unplaced pieces:** where each lives now that the Price Menu names several as Courses.
11. **93 videos:** does the count look right? About 40% are duplicates.
12. **Missing files:** Discipline of Cycles PDF, the 2 orientation videos, the Eightfold Path videos if new, Bunny's Schools paperwork, the six Relationship Studies.
13. **Nov 5 material:** the CamScanner notes, the Holistic Health Educator and Nutritional Concepts I outlines, and the "Sara Four" folder. Do they change any of this, including the three tracks?
14. **Refunds:** cancellation method and contact email (blank in the draft).
15. **Name:** see 4.20.

## 10. How to reply

Please send one markdown file back, in this shape, so we can apply it directly:

```markdown
# Corrections from Michael's Claude (date)

## Section 4 checks
- 4.5 Counselor sessions: [answer], source: [Michael's document or note]
- ...

## Structure
- [page or area]: keep | change to [...] | remove | new, and why

## Library list
- Concepts at launch: ...
- Patterns at launch: ...
- Schools, in order: ...

## Answers to Section 9
1. ...

## Still unknown
- ...
```

Mark anything that is your inference rather than Michael's own words, so we can tell the two apart.
