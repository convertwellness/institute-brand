# Portal spec: accounts, entitlements and billing

From Section 5 of the Nov 11, 2026 layout brief. **Nothing here is built yet.** The catalogue
(`site/`) stays static; the portal is a separate small app beside it. `/account` and `/cart` on the
static site are placeholders until it exists.

**Status: from notes, not yet confirmed as a signed build plan (open item O2).** Michael's questions
about the plug-in approach (Approach B) point the same way as this one.

## Recommended stack (Approach A)

| Piece | Choice | Why |
|---|---|---|
| Catalogue | The existing static site, built from `content/catalog.json` and `content/pricing.json` | Already built; every product has a stable id to map to |
| Accounts | Supabase Auth (email sign-up or magic link) | One account per student, instant join |
| Records | Supabase Postgres | One row per student, per entitlement; exportable to Excel |
| Payments | Stripe Checkout and Stripe Billing | One-off purchases and monthly or annual tiers |
| Entitlements | Stripe webhooks write entitlement rows | The webhook, not the browser, decides what a student owns |
| Video | A streaming host (Bunny Stream, Mux or Vimeo) | Signed URLs, no download button. Never in git |

Michael asked (Nov 4) whether each student can have their own file, page or spreadsheet. Answer:
each student has their own portal account and record, and the Institute can export everyone to
Excel at any time.

## Requirements

1. **Account.** One account per student: email sign-up or magic link, and a profile. Instant join,
   no application. (The scholarship application is separate and stays.) Admin can export all
   students to Excel.
2. **Entitlements.** One record per student and item, bundle or tier, with:
   - `source`: purchase, membership, gift or scholarship
   - `expires`: none for owned items; the membership end date for streamed access
   - the catalogue `id` from `content/catalog.json`
3. **My Library.** Shows only what the student is entitled to, grouped by track and content type,
   with progress. What it contains follows the tier (Seeker, Explorer, Discoverer in the Nov 3
   draft). Counselor is unlimited.
4. **Locked but visible.** Related items the student does not own show "Add for $X" or "Upgrade for
   the difference." Upgrades credit everything already spent (Q16).
5. **Lesson player.** Streamed video with signed URLs and no download button; self-guided slides as
   images or a view-only PDF; reflection prompts; a Personal Action Plan; mark complete.
6. **Downloads.** Written material only, stamped with the buyer's name or email. Kept after
   cancelling, for personal study only. Per-tier download caps: **open item O7**.
7. **Foundation gate.** Build the flag; leave it off until Michael answers **O3**. The static site
   already carries it: `settings.foundation_gate` in `content/catalog.json`.
8. **Orientation videos.** The member orientation video on the dashboard; the non-member one on the
   public Begin Here page (`/begin`, slot in place). Neither has arrived (**O13**).
9. **Billing self-service.** Card, invoices, cancel, move between tiers.
   - An upgrade starts its benefits now and bills the new rate on the next cycle.
   - A monthly downgrade takes effect on the next billing date; an annual downgrade only at renewal.
   - Failed payment: 7 days before access pauses.
   - The introductory price is kept while the membership stays active.
10. **Account sharing.** One person per membership; the Institute can suspend shared accounts.
11. **Admin.** Grant or revoke access, comp a student, award scholarships, map products to content,
    view progress, export.

## Protection (Michael's Nov 4 questions)

| He asked | What we can do |
|---|---|
| "Can we prevent theft?" of owned items | Downloads are written material only, stamped with the buyer's name or email |
| "Can we prevent download or screen copying?" of streamed video | Stream only, signed URLs that expire, no download button. **Screen recording cannot be fully blocked on any site** |
| "Can we determine [My Library] by S, E, D. C = unlimited" | Yes: library contents and allowances follow the tier; Counselor is unlimited |

## Release rules the portal must enforce

From the Nov 3 Price Menu, held in `content/pricing.json` under `release_rules`:

- Annual members get their tier's material up front; monthly members get it at a steady pace.
- Explorer and Discoverer monthly: each School releases one week per week over 12 weeks; the next
  School opens when the first is finished. The eBook unlocks with the second payment. One disease
  study a quarter.
- Counselor monthly: month 1 unlocks everything Discoverer gets, the Foundation of the Institute
  Course and the first live session. Months 2 to 11 unlock one School a month with related
  collections and Family studies. Month 12 unlocks the rest. Every month: a live session and one
  disease study.
- Buy ahead: unreleased items can be bought at the member's own discount. Switch to annual at any
  time by paying the rest; everything unlocks.
- Schools unlock in the order the Institute sets (**O8**).
- Unused free monthly or quarterly benefits do not carry over.
- **Discounts, not credits.** Do not build a credits wallet.

## Refunds and cancelling

Drafted by Michael in SARA THREE. **Needs attorney review before publishing (O11).**

- Monthly: a full refund of the first payment if cancelled within 30 days, once per member. After
  that, cancel any time, effective at the end of the paid month, no partial refunds.
- Annual paid in full: cannot be cancelled or refunded; full access for 12 months; auto-renews
  unless turned off; reminder at least 14 days before renewal.
- **Checkout must show the annual no-cancellation terms with a checkbox to agree before payment.**
- The cancellation method and contact email are blank in the draft.
- Health disclaimer: the material is educational, not diagnosis or treatment.

## Product mapping

Every item has an `id` and a `price` key in `content/catalog.json`; every price key resolves in
`content/pricing.json`. Stripe products should be created from those two files so the catalogue,
the price menu and Stripe cannot drift apart. Price keys that have no figure yet:
`hos-collection` and `video-bundle`.
