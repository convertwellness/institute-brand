# Inbox: Claude Code and Grok Bot

Two-way inbox for this repo. Each entry: date and time in ET, a subject, and a status of `open` or `done`.
Never put secrets here: name a variable, never its value.

## To Claude

### 2026-11-11 5:41 PM ET | Brief: Institute site layout (Nov 11, 2026) | done

#### Claude Code Brief: The Michael Schwartz Institute for Wholistic Education website

Prepared November 11, 2026 for Convert Wellness. Use this as the single consolidated brief for laying out the Institute site. Where this brief and older repo docs disagree, this brief wins. Where this brief marks something as open, do not guess. Build a clearly labeled placeholder and list it in your summary.

##### 1. Context

- **Client:** Michael Schwartz, N.D. (michael383@me.com). His assistant is Bunny (he spells it Bunnie). Bunny is preparing additional Schools paperwork.
- **Official name in use:** The Michael Schwartz Institute for Wholistic Education. Spell "Wholistic" with a W. Note: the Membership Rules document still says "Institute of the Spiritual Science of Human Patterns." Use the official name everywhere and flag the Rules document text for Michael.
- **Repository:** `github.com/convertwellness/institute-brand` (last commit Sep 25, 2026). None of the November planning has been committed yet.
- **Staging:** https://institute-brand-fvawt.sevalla.page/ (Sevalla static site, publishes `site/`).
- **Stack:** plain HTML, CSS and vanilla JS. `build/build.py` stamps partials onto `src/*.html` and writes `site/`. Next.js was dropped Sep 1, 2026. Content strings live in `content/site.ts` and `content/navigation.ts`. `build/make-library.py` and `make-stubs.py` generate pages. `build/prices.py` holds and restores prices. `build/audit.py` checks dead links and counts placeholders. `build/drafts.py --strip` removes draft copy. Read `CLAUDE.md` (brand rules), `DESIGN.md`, `STRUCTURE.md`, `site/README.md` and `docs/questions-for-michael.md` before changing anything.
- **State at Nov 4:** 67 pages on staging, all prices held as "to be confirmed," 141 placeholders across 62 pages, no accounts, payments or dashboard. `/account` and `/cart` are placeholders.
- **An earlier Phase 1 prompt exists** (`claude-prompt-phase1.md`, written against the SARA TWO material). This brief supersedes it where they differ.

###### Source materials

| Source | Date | What it is |
|---|---|---|
| Content Map and Portal Plan (Google Doc sent to Michael) | Nov 4 | Inventory of SARA TWO, sitemap, product model, portal requirements, 6-phase plan, 16 decision questions |
| Michael's 2-page handwritten fax ("Internet Fax Job") | Nov 4 | His written answers to the 16 questions and his comments on the portal and approach |
| SARA THREE Dropbox folder | Nov 5 | Price Menu and Membership Tiers Final 11 3, Membership Rules and Refund Policy, Foundational Principles, Scholarship Fund and Application, Credit and Cash guidelines, Belonging Six Principles PDF, Self Exploratory Intro Course deck, intro videos, 5 Laws videos, 12 School folders ("Schools Completed 10 30") |
| Michael's 9-page CamScanner revision notes, plus Holistic Health Educator OUTLINE.docx and Nutritional Concepts I Outline.docx | Nov 5 | Handwritten site revisions that move toward 3 tracks and 3 pricing tiers (see Section 3) |
| Friday call plan (sent to Michael Nov 6) | Nov 6 | Summary of what his fax and SARA THREE settled, plus 6 decisions to lock |
| Nov 6 review call | Nov 6 | 30 minute call. The automatic notes captured only 6 seconds, so no outcomes are recorded |
| Michael's verbal feedback to Sara | Nov 11 | He confirmed much of the summary sheet and said it looked good (verbal, no written record) |

###### Status labels used below

- **Confirmed by Michael (written):** in his own handwriting, email or his own documents.
- **Confirmed by Michael (verbal, Nov 11):** covered by his Nov 11 "looks good" on the summary sheet. Treat as confirmed but keep it easy to change.
- **From notes, not yet confirmed:** our recommendation or an inference from his files. Build it, but keep it configurable and list it in your summary.
- **Open:** do not build final copy or logic. Placeholder only. See Section 8.

##### 2. Confirmed decisions

Michael's fax answers map to the 16 questions in Section 8 of the Nov 4 Content Map and Portal Plan.

| # | Topic | Decision | Status and source |
|---|---|---|---|
| Q1 to Q3 | Tier names, credits, member discount | Fax gave no direct answer. The SARA THREE Price Menu (Final 11 3) answers them with 4 tiers and percentage discounts (details in Section 4). The separate credits documents conflict and should not drive the build. | From notes, not yet confirmed. Superseded in part by the Nov 5 three-tier notes. See Open item O1 |
| Q4 | All-access | Counselor level only. | Confirmed by Michael (written, Nov 4 fax: "Counselor level only") |
| Q5 | Naming | Michael will make a list of new names in the form old = new. | Confirmed by Michael (written, Nov 4). List not received yet. Open item O6 |
| Q6 | Foundation gate | "Good question, had same thought." No yes or no given. | Open item O3 |
| Q7 | The Operating System loop | 5 steps: Concept → Belief System / Pattern → Experience → Fulfilled Expectation → Validation of Concept. Replace the 6-stage ring graphic and the older Concept → Expectation → Pattern → Experience → Validation sequence. | Confirmed by Michael (written, Nov 4 fax) |
| Q8 | Families | "Will get back to you on this." SARA THREE then listed the same 10 launch Families (see Section 6). Placement of Abandonment and Shame is still unknown. | 10 Families: From notes (Price Menu Nov 3, Friday plan Nov 6), covered by Nov 11 verbal. Abandonment and Shame placement: Open item O4 |
| Q9 | Ship or hold | Ship based on the new material in SARA THREE. Per the Nov 6 summary: Fear and Doubt ships as Core Study #7 inside the School of Fear, Safety and Trust. Hold Sacrifice, Stubbornness and a standalone Love study. | Confirmed by Michael (written, Nov 4). Specific placements: From notes (Nov 6 summary), covered by Nov 11 verbal |
| Q10 | New areas | Multiple new videos sold separately and in bundles: 8 videos, 12 courses, and webinars that are really self-study guides. These may also include Patterns and Concepts as well as webinars. Use the label "Self-Guided Studies," not "Webinars." | Confirmed by Michael (written, Nov 4). Label: Sara's Nov 4 comment on the plan, matches Michael's "webs = self study guides" |
| Q11 | Orientation videos | Two new orientation videos are coming: one for non-members (public) and one for members (dashboard only). | Confirmed by Michael (written, Nov 4). Videos not received yet |
| Q12 | Formats and pricing | "Yes, new numbers and membership coming." This led to the Nov 3 Price Menu and then the Nov 5 revision. | Confirmed by Michael (written, Nov 4) |
| Q13 | Access and downloads | Many products will contain written material that may be downloaded. Presentations (voiced or self-guided) may not be downloaded. They are stream or view only. Downloaded written material is kept after cancelling, for personal study only. | Confirmed by Michael (written, Nov 4 fax, plus SARA THREE Price Menu and Rules) |
| Q14 | Counselor tier | Counselor is limited to 120 per year. Weekly consults by Michael and a second provider (written "Candly" in the fax; spelling unconfirmed). Conflict: the Nov 3 Price Menu says one monthly live group session with Michael. | Cap and weekly consults: Confirmed by Michael (written, Nov 4). Session format and second provider name: Open item O5 |
| Q15 | Joining | Instant join. No application gate for membership. (The scholarship application is separate and stays.) | Confirmed by Michael (written, Nov 4) |
| Q16 | Upgrades | Yes. The full amount a student has already spent counts toward bundles, courses and tier upgrades. Upgrade benefits start immediately and the new rate bills on the next cycle. | Confirmed by Michael (written, Nov 4), billing timing from SARA THREE Rules |

###### Michael's comments on the portal and approach (Nov 4 fax)

| Topic | What he wrote | How to treat it |
|---|---|---|
| 93 videos | "93 videos?" | He questioned the count. Videos are catalogued by name and size only. About 40% of video bytes are duplicates, leaving roughly 13 GB unique. Do not publish a video count |
| Keynote files | Discipline of Cycles: convert to PDF. Belonging Six Principles: convert to PDF | Belonging Six Principles PDF is now in SARA THREE. Discipline of Cycles PDF has not arrived |
| Love | "Love is alone?" | Treat Love as a held item until Michael confirms (see Q9). Open item O4 |
| Owned items | "Can we prevent theft?" | Protection rules in Section 5 |
| My Library by tier | "Can we determine by S, E, D. C = unlimited" | Library contents and allowances follow the tier (Seeker, Explorer, Discoverer). Counselor is unlimited |
| Locked items | Noted, no change | Keep locked-but-visible items |
| Streamed video | "Can we prevent download or screen copying?" | Stream-only with signed URLs and no download button. Note that screen recording cannot be fully blocked on any site |
| Downloads | Noted | Written PDFs only, stamped with the buyer's name or email |
| Approach B (Memberstack-style plug-in) | "Awkward at scale? Can each student have own file, page or Excel?" | Answer: each student gets their own portal account and record, and the Institute can export to Excel at any time. This fits Approach A |
| Refund policy, phased plan | Noted, no objection | Refund policy is drafted in SARA THREE (Section 5). Phased plan stands |

##### 3. Program structure (Nov 5 revision)

Michael's 9-page CamScanner notes (Nov 5) reorganize the Institute into three tracks and three pricing tiers. **From notes, not yet confirmed.** Only the summary below survives. The PDF and both outline documents are no longer in the SARA THREE folder, so their full contents (module lists, tier names two and three, prices) are not available. Build the track structure with placeholders and do not invent module titles or prices.

| Track | Program | What is recorded |
|---|---|---|
| Track 1 | Personal Mastery | All 3 lessons free |
| Track 2 | Holistic Health Educator | 6-module Certification Program (outline in Holistic Health Educator OUTLINE.docx). Nutritional Concepts I may belong here; unconfirmed |
| Track 3 | Wholistic Essays and Teachings | Library of essays and teachings |

**Pricing in the Nov 5 notes:** 3 tiers, the first being "Foundation Free." The other two tier names, prices and inclusions were not recovered.

**How to reconcile with the Nov 3 four-tier menu (Open item O1):** do not hard-code either model. Put tiers in one data file (extend `build/prices.py` or a `content/tiers` file) so the Membership page and every buying block render from data. Build the 3-track model as the public program structure, and keep the Nov 3 four tiers in the data file as the current draft until Michael says which is final.

##### 4. Pricing and membership data (Nov 3 Price Menu, Final 11 3)

**From notes, not yet confirmed as final.** Michael wrote this himself, so the figures are his. Whether it is still current after the Nov 5 revision is Open item O1. Keep prices held on the live site (`build/prices.py`) until Michael signs off.

###### Tiers

| Tier | Monthly | Annual (10 months) | Discount on purchases | Key inclusions |
|---|---|---|---|---|
| Seeker | $5 | $50 | 20% | 1 free individual study a month (up to $9), 1 free short video, Community meetings |
| Explorer | $18 | $180 | 30% | One School at a time, Introductory Body Symbology eBook on joining, 1 self-guided disease study a quarter, Community meetings |
| Discoverer | $29 | $290 | 40% | Everything in Explorer plus the full short video library, early access to new Schools and studies |
| Counselor | $69 | $690 | Everything included | All Schools, collections, Foundational courses and disease studies; live session(s) with Michael (format open, O5); the Counselor path (title awarded only after coursework); 50% off private sessions; optional permission to use materials with own clients. Cap of 120 per year |

###### Release rules

- Annual members get their tier's material up front. Monthly members get it at a steady pace.
- Explorer and Discoverer monthly: each School releases one week per week over 12 weeks, the next School opens when the first is finished. eBook unlocks with the second payment. One disease study a quarter.
- Counselor monthly: month 1 unlocks everything Discoverer gets, the Foundation of the Institute Course and the first live session. Months 2 to 11 unlock one School a month with related collections and Family studies. Month 12 unlocks the rest. Every month: live session and one disease study.
- Buy ahead: unreleased items can be bought at the member's own discount. Switch to annual any time by paying the rest; everything unlocks.
- Schools unlock in the order the Institute sets.
- Unused free monthly or quarterly benefits do not carry over.

###### Standalone prices (Public / Seeker / Explorer / Discoverer)

- Individual Pattern, Universal Teaching, Four Selves, Self, Relationship, Spiritual Gift, Discipline study: $7 / $6 / $5 / $4
- Individual Concept Study: $9 / $7 / $6 / $5. Self-Guided Concept Study: $8 / $6 / $6 / $5
- Individual Human Operating System Lesson: $9 / $7 / $6 / $5
- Introductory Body Symbology eBook: $10 / $8 / free on joining / free on joining
- Collections: Three Interwoven Concept Studies $24 / $19 / $17 / $14. Three Interwoven Pattern Studies $17 / $14 / $12 / $10. Six Interwoven Pattern Studies $30 / $24 / $21 / $18. Connected Concept and Pattern Collection $19 / $15 / $13 / $11. Pattern Family Collection (each) $30 / $24 / $21 / $18. Three Relationship Studies $17 / $14 / $12 / $10. Complete Relationship Collection and Complete Universal Teachings Collection $30 / $24 / $21 / $18. Human Operating System Collection: to be set.
- Courses: Five Laws of Human Experience free. Doctrine of Personal Responsibility free (proposed). Self Exploratory Course $25 / $20 / $18 / $15. Foundation of the Institute Course $80 / $64 / $56 / $48. Awakening of Consciousness $30 / $24 / $21 / $18. Universal Principles and Teachings $25 / $20 / $18 / $15. Total Body Symbology Reference $30 / $24 / $21 / $18. The Four Selves $19 / $15 / $13 / $11. Twelve Spiritual Gifts and Twelve Disciplines $20 / $16 / $14 / $12.
- Each School: $40 / $32 / included one at a time / $24.
- Self-guided disease study (slides): $25 / $20 / one free a quarter then $18 / one free a quarter then $15. With written study: $40 / $32 / $28 / $24.
- Short video: $4.99 / included / included / included. Video bundles: to be set.

**Discounts, not credits.** The recommendation on Nov 6 was to ship the simple percentage discounts and retire the separate credits documents (3 credits a month, $6.50 per credit, rollover caps). The Price Menu uses discounts only. **From notes, not yet confirmed.** Do not build a credits wallet.

##### 5. Portal, access and protection rules

Recommended stack (Approach A): keep the static catalogue, add a small app with Supabase Auth and Postgres plus Stripe Checkout and Billing, with webhooks writing entitlements. Video on a streaming host (Bunny Stream, Mux or Vimeo), never in git. **From notes, not yet confirmed as a signed build plan** (Open item O2), but Michael's questions about Approach B point the same way.

Portal requirements:

1. **Account:** one account per student (email sign-up or magic link, profile). Instant join, no application. Admin can export all students to Excel.
2. **Entitlements:** one record per student and item, bundle or tier, with source (purchase, membership, gift, scholarship) and expiry (none for owned items, membership end date for streamed access).
3. **My Library:** shows only what the student is entitled to, grouped by track and content type, with progress. Contents depend on tier; Counselor is unlimited.
4. **Locked but visible:** related items show "Add for $X" or "Upgrade for the difference." Upgrades credit everything already spent (Q16).
5. **Lesson player:** streamed video with signed URLs and no download button; self-guided slides as images or view-only PDF; reflection prompts; Personal Action Plan; mark complete.
6. **Downloads:** written material only, stamped with the buyer's name or email. Kept after cancelling for personal study. Per-tier download caps: Open item O7.
7. **Foundation gate:** build the flag, leave it off until Michael answers (Open item O3).
8. **Member orientation video** on the dashboard; non-member orientation on the public Begin Here page.
9. **Billing self-service:** card, invoices, cancel, move between tiers. Upgrade starts benefits now and bills next cycle. Monthly downgrade next billing date; annual downgrade only at renewal. Failed payment: 7 days before access pauses. Introductory price kept while membership stays active.
10. **Account sharing:** one person per membership; the Institute can suspend shared accounts.
11. **Admin:** grant or revoke access, comp a student, award scholarships, map products to content, view progress, export.

###### Refund and cancellation policy (drafted by Michael in SARA THREE, needs attorney review before publishing)

- Monthly: full refund of the first payment if cancelled within 30 days, once per member. After that, cancel any time, effective at the end of the paid month, no partial refunds.
- Annual paid in full: cannot be cancelled or refunded; full access for 12 months; auto-renews unless turned off; reminder at least 14 days before renewal.
- Checkout must show the annual no-cancellation terms with a checkbox to agree before payment.
- Cancellation method and contact email are blank in the draft. Use a placeholder.
- Health disclaimer: material is educational, not diagnosis or treatment.

##### 6. Site architecture and page layout

Keep the five header doors so navigation does not grow: **Begin Here, Explore, Learn, The Schools, Membership**, plus Search and Sign in. Fit the three tracks inside this structure.

- **Home:** Institute greeting video slot, the three tracks as three clear entry cards (Personal Mastery free, Holistic Health Educator certification, Wholistic Essays and Teachings), the Operating System loop, membership call to action, Scholarship Fund link.
- **Begin Here (`/begin`):** non-member orientation video (coming), Five Laws of Human Experience (free course, video in SARA THREE), Track 1 Personal Mastery (3 free lessons), Foundational Principles of the Institute (text in SARA THREE), the 5-step Operating System loop.
- **Explore:** Concepts, Patterns, the 10 Concept Families, Interwoven Studies (`/collections`), Relationship Studies.
- **Learn:** Track 2 Holistic Health Educator (6-module certification, module list placeholder), Track 3 Wholistic Essays and Teachings, Courses (Foundation of the Institute, Self Exploratory, Awakening of Consciousness, Universal Principles and Teachings, Four Selves, Total Body Symbology Reference), Universal Teachings (Twelve Spiritual Gifts and Twelve Disciplines, Discipline of Cycles), Eightfold Path videos, Self-Guided Studies (the disease studies; do not call them webinars), Books, Live Events.
- **The Schools:** list in the order Michael sets, each a 12-week program. See the School list conflict below.
- **Membership:** tiers rendered from the data file, release rules, upgrade rule, refund summary, instant join. Counselor shows the 120 per year cap.
- **Scholarship Fund:** donation page (gift levels $25, $40, $50, $80, $180, $290, any amount; $5 a month sponsors a Seeker) and scholarship application page. Center for Universal Teachings is the 501(c)(3). The application link and some emails are placeholders in his documents.
- **Sign in → Dashboard (`/account`):** My Library, member orientation, progress, downloads, billing.

**Every study page** carries the same buying block: buy this study, buy its collection, or become a member. Show formats (Watch, Self-guided, Written) and the Family and weaves it belongs to.

##### 7. Content inventory

From SARA TWO (Nov 4) and SARA THREE (Nov 5). Videos are catalogued by title and size only, not reviewed.

- **10 launch Families:** Acceptance, Achievement, Belonging, Control, Emotional Expression, Love, Relationship, Responsibility, Trust, Worth. Each Family package: The Concept of X, Approval Pathway, Rejection Pathway, Personal Application and Review, Modus Operandi video. Replaces the 4 on the site.
- **Concepts:** 22 self-guided decks (Abandonment, Acceptance, Achievement, Approval, Belonging, Control, Expectation, Expectation and Pattern, Fear, Freedom, Guilt, Identity, Inadequacy, People Pleasing, Rejection, Safety and Protection, Success and Failure, Trust, Unworthiness, plus held items Stubbornness and Sacrifice) and the Concept of Love deck (held). SARA THREE adds pages on Fear, Control, Suspicion, Truth, Trust, Unforgiveness.
- **Patterns:** about 27 voiced videos and 6 self-guided decks (including Fear and Doubt, Inconsistency, Resentment, Becoming Indispensable, Managing Others, Self-Sabotage), plus Modus Operandi. SARA THREE adds Worrying, Hypervigilance, Defensiveness.
- **Interwoven Studies:** about 11 Concept weaves and 21 Pattern weaves.
- **Relationship Studies:** Mother and Acceptance, Father and Approval, Trust and Rejection, Roles and Expectations, Relationships as Mirrors, Recurring Relationship Patterns (priced, files not received).
- **Human Operating System Collection:** Consciousness, Mind, Brain, Body, Four Selves, Concepts, Beliefs, Expectations, Patterns.
- **Self-Guided Studies (disease):** Arthritis, Bone Health, Brain and Memory, Cancer (Breast, Prostate, Causes of Cancer), Cardiovascular, Diabetes, Digestive Health, Hypertension, Immune Health, Weight and Metabolic Health.
- **Universal Teachings:** Twelve Spiritual Gifts, Twelve Disciplines, Discipline of Cycles (PDF pending), Belonging Six Principles (PDF received).
- **Eightfold Path:** 9 video files (View, Thought, Speech, Behavior, Livelihood, Effort, Mindfulness in 2 cuts, Meditation). Michael's "8 videos" likely refers to this series.
- **Short videos (3 to 5 minutes):** Eightfold Path, body parts, vitamins and diseases. Bundles to follow.
- **Intro videos (SARA THREE):** Institute Greeting, Concepts, Concepts 3's, Pattern Intro, Pattern explanation, Courses, Schools, 5 Laws intro and full course.
- **Courses:** Foundation 10-week outline (Foundation-Pattern-Course deck), Self Exploratory Intro Course deck.
- **Schools:** 12 folders in "Schools Completed 10 30": Belonging, Concepts, Consciousness, Fear Trust Safety, Human Patterns, Identity, Operating System, Relationships, School of Conscious Living, School of Human Relationships, School of Symbolic Understanding, Teachings. The Price Menu lists 10: Concepts, Consciousness, Conscious Living, Fear Safety and Trust, Identity, Human Operating System, Human Patterns, Human Relationships, Universal Teachings, Symbolic Body. Belonging and Relationships are extra folders. Open item O8.

##### 8. What Claude should build next

Work on a branch and open a pull request. Do not merge.

1. **Single catalogue data file** (`content/catalog.json` or similar) with every item: id, title, type, track, Family, School, formats, price keys, status (ship, hold, placeholder). All library pages and buying blocks generate from it.
2. **Tier and price data file** that holds the Nov 3 four-tier menu and a slot for the Nov 5 three-tier model, with prices still held on the live site.
3. **Three-track structure:** Track 1 Personal Mastery (3 free lessons, placeholders), Track 2 Holistic Health Educator (6 module placeholders), Track 3 Wholistic Essays and Teachings (index plus stubs). Wire them into Home, Begin Here and Learn.
4. **Families 4 to 10**, each as a Family package page.
5. **New Concept, Pattern and Interwoven routes** from Section 7, with held items (Sacrifice, Stubbornness, standalone Love) excluded from navigation and marked held in the catalogue.
6. **Fear and Doubt** as Core Study #7 inside the School of Fear, Safety and Trust.
7. **New areas:** Universal Teachings, Eightfold Path, Self-Guided Studies, Relationship Studies.
8. **Begin Here** with orientation and greeting video slots, Five Laws, Foundational Principles, and the new 5-step Operating System loop. Replace the 6-stage ring graphic.
9. **Membership page** rendered from the tier data file, with release rules, upgrade rule, instant join, the Counselor 120 cap and a refund summary marked "pending legal review."
10. **Scholarship Fund and application pages** with placeholders for the application link and emails.
11. **Portal spec doc** (`docs/portal-spec.md`) from Section 5. Do not build auth or payments yet.
12. **Update docs:** `site/README.md`, `STRUCTURE.md`, and replace `docs/questions-for-michael.md` with the open list below.
13. Run `build/audit.py` and report the placeholder count before and after.

##### 9. Questions Claude should not guess on

Use labeled placeholders for all of these and list them in your pull request summary.

- **O1. Pricing model.** Nov 3 four tiers (Seeker, Explorer, Discoverer, Counselor) versus Nov 5 three tiers starting with Foundation Free. Tier names two and three, prices and inclusions in the Nov 5 model are unknown.
- **O2. Build sign-off.** Phase 1 green light and the Stripe plus Supabase approach were on the Nov 6 agenda; no outcome is recorded.
- **O3. Foundation gate.** Must a student finish Foundation before studying a single study they bought?
- **O4. Love, Abandonment, Shame.** Is Love standalone or only inside the Love Family? Which Family do Abandonment and Shame belong to?
- **O5. Counselor live sessions.** Weekly consults with Michael and a second provider (name spelled "Candly" in the fax) versus a monthly group session with Michael. How are they booked?
- **O6. Old to new names.** Michael's list is coming. Includes whether "Foundation" becomes "Institute Core Studies Program."
- **O7. Download caps by tier.** Whether any tier has a download limit.
- **O8. School list.** 12 folders versus 10 on the Price Menu. Are Belonging and Relationships Schools, and do Relationships and Human Relationships merge?
- **O9. Track content.** The 3 Personal Mastery lessons, the 6 Holistic Health Educator modules, and the Track 3 titles.
- **O10. Institute name** in the Membership Rules document.
- **O11. Refund policy wording** and cancellation method, pending attorney review.
- **O12. Video counts and placement.** 93 catalogued videos, about 40% duplicate. Do not publish counts.
- **O13. Missing files:** Identity School Week 1, Discipline of Cycles PDF, 2 orientation videos, 8 Eightfold Path videos (if new), Bunny's Schools paperwork, the CamScanner notes and both outlines, and anything in the new "Sara Four" folder.

Do not invent teaching copy, prices, dates, counts or decisions. If something is unknown, mark it unknown.

## To Grok Bot

### 2026-11-11 6:10 PM ET | Institute layout built on branch site-layout-nov11, not for deploy yet | open
The Nov 11 layout brief is built on branch `site-layout-nov11`. **Do not deploy or merge: Sara has not approved it.**

- 149 pages. Library pages, indexes, Membership and the Scholarship Fund are generated from
  `content/catalog.json` and `content/pricing.json` by `build/make-catalog.py`.
- Prices are held (`"display": "held"`); no figure is in any built page.
- Open items O1 to O13 are labelled on the pages and listed in `docs/questions-for-michael.md`.
- Portal is specified, not built: `docs/portal-spec.md`.
- Pre-deploy checks: `python build/audit.py` (links, dashes, old names) and
  `python ~/.claude/tools/site-meta-check.py site` both pass on the branch.

Nothing is needed from Grok Bot yet. A new entry will follow when Sara approves the merge.
