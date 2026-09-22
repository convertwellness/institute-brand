# -*- coding: utf-8 -*-
"""Write the routes that exist before their content does.

A stub is a real page at a real URL that says plainly what has not been written
yet, and points somewhere useful instead. It is not an error page and it never
apologises to the visitor for something that is our side of the work.

Every one of these is a placeholder by policy, not by accident: CLAUDE.md says
ship the route, ship a clear placeholder, do not invent copy. Legal text in
particular is the client's to supply and must never be drafted here.

    python build/make-stubs.py

Existing files are never overwritten — replace a stub by editing its src/ file.
"""

import io, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC  = os.path.join(ROOT, "src")

FM = u"""<!--
title: {title}
desc: {desc}
css: study
body:
-->

"""

PAGE = u"""<main id="main">
<div class="shell">
  <nav class="crumb" aria-label="Breadcrumb">
    <a href="/">The Institute</a> <i aria-hidden="true">/</i>{mid}
    <span aria-current="page">{crumb}</span>
  </nav>

  <div class="stub">
    <p class="stub__k">{kicker}</p>
    <h1 class="stub__h">{heading}</h1>
    <p class="stub__lead">{lead}</p>

    <div class="needs">
      <span class="needs__k">{needs_k}</span>
      <p>{needs}</p>
    </div>

    <div class="stub__on">
{links}
    </div>
  </div>
</div>
</main>
"""


def link(href, label):
    return u'      <a class="arrow" href="%s">%s</a>' % (href, label)


# path, crumb-parent (href, label) or None, kicker, heading, lead, needs-key,
# needs, [(href, label), ...]
STUBS = [

    # ── The four Concept Families ────────────────────────────────────────
    ("concepts/families/acceptance.html", ("/concepts/families", "Concept Families"),
     u"Concept Family 01", u"The Acceptance Family",
     u"Rejection, Approval and Self-Rejection are studied as one set, because they are "
     u"rarely met one at a time.",
     u"Awaiting Michael",
     u"The Family's own description, its primary Patterns, and what the set costs against "
     u"its parts. The three Concepts in it are named; nothing else is.",
     [("/concepts", "The Concept Studies"), ("/concepts/families", "All four Families")]),

    ("concepts/families/worth.html", ("/concepts/families", "Concept Families"),
     u"Concept Family 02", u"The Worth Family",
     u"Unworthiness, Inadequacy, Inferiority and Undeserving — the largest of the four, and "
     u"the one most students meet first.",
     u"Awaiting Michael",
     u"The Family's own description and its primary Patterns. "
     u"Unworthiness is the one Concept written out in full so far.",
     [("/concepts/unworthiness", "The Unworthiness Study"),
      ("/collections/worth-family", "The Worth Family as a set")]),

    ("concepts/families/control.html", ("/concepts/families", "Concept Families"),
     u"Concept Family 03", u"The Control Family",
     u"The third of the four Families Michael names.",
     u"Awaiting Michael",
     u"Which Concepts belong to this Family. None of the twelve Concepts named so far has "
     u"been placed in it, so it is listed here without contents rather than filled by guess.",
     [("/concepts", "The Concept Studies"), ("/patterns/control", "The Control Pattern")]),

    ("concepts/families/trust.html", ("/concepts/families", "Concept Families"),
     u"Concept Family 04", u"The Trust Family",
     u"Suspicion is the one Concept placed here so far.",
     u"Awaiting Michael",
     u"The Family's own description, its primary Patterns, and the rest of its Concepts.",
     [("/concepts/suspicion", "The Suspicion Study"), ("/concepts/families", "All four Families")]),

    # ── Books ────────────────────────────────────────────────────────────
    ("books/awakening.html", ("/books", "Books"),
     u"Written edition", u"Awakening",
     u"One of the Institute's two books.",
     u"Awaiting Michael",
     u"The description, the length, the formats it is sold in, and the price. The title is "
     u"all that has been given so far.",
     [("/books", "All written editions"), ("/courses", "The four Courses")]),

    ("books/tj.html", ("/books", "Books"),
     u"Written edition", u"T.J.",
     u"One of the Institute's two books.",
     u"Awaiting Michael",
     u"The description, the length, the formats it is sold in, and the price. T.J. was also "
     u"noted as outside the launch set, so whether it appears at launch is still open.",
     [("/books", "All written editions"), ("/courses", "The four Courses")]),

    ("books/workbooks.html", ("/books", "Books"),
     u"Study materials", u"Workbooks and Awakening Portfolios",
     u"The written materials that accompany study rather than replace it.",
     u"Awaiting Michael",
     u"What a Workbook and an Awakening Portfolio each contain, which Studies they pair "
     u"with, whether they are sold singly or as a set, and the price.",
     [("/books", "All written editions"), ("/concepts", "The Concept Studies")]),

    ("books/video-studies.html", ("/books", "Books"),
     u"Study materials", u"Video Studies and Special Topics",
     u"Recorded study outside the Course structure.",
     u"Awaiting Michael",
     u"The list of Video Studies and Special Topics, what each covers, and how they are "
     u"priced. Whether these belong under Books at all is worth a moment of his time — they "
     u"may sit better beside the Courses.",
     [("/books", "All written editions"), ("/courses", "The four Courses")]),

    # ── Live events ──────────────────────────────────────────────────────
    ("events/arthritis.html", ("/events", "Live Events"),
     u"Seminar", u"Arthritis",
     u"One of the two seminars named so far.",
     u"Awaiting Michael",
     u"The date, the venue or platform, the length, the price, and what the seminar covers. "
     u"Nothing about this event has been set down except its subject.",
     [("/events", "All seminars"), ("/courses/body-symbology", "Body Symbology")]),

    ("events/cancer.html", ("/events", "Live Events"),
     u"Seminar", u"Cancer",
     u"One of the two seminars named so far.",
     u"Awaiting Michael",
     u"The date, the venue or platform, the length, the price, and what the seminar covers. "
     u"Nothing about this event has been set down except its subject.",
     [("/events", "All seminars"), ("/courses/body-symbology", "Body Symbology")]),

    # ── The Institute ────────────────────────────────────────────────────
    ("about.html", None,
     u"The Institute", u"About the Institute",
     u"What the Institute is, what it teaches, and why it was founded.",
     u"Awaiting Michael",
     u"This page has to be in his voice or it is worth nothing. It is the one page a "
     u"sceptical visitor reads before deciding whether to believe any of the rest.",
     [("/michael", "Michael Schwartz"), ("/begin/the-path", "How the education fits together")]),

    ("michael.html", None,
     u"The Institute", u"Michael Schwartz, N.D.",
     u"The teacher behind the Institute's material.",
     u"Awaiting Michael",
     u"A biography, in whatever length he wants it, and a photograph if he has one he likes. "
     u"Every term taught at the Institute is his own; this page is where that is established.",
     [("/about", "About the Institute"), ("/courses/five-laws", "Start the free course")]),

    ("contact.html", None,
     u"The Institute", u"Contact",
     u"How to reach the Institute.",
     u"Awaiting Michael",
     u"An address for enquiries, an address for support, and whatever else he wants reachable. "
     u"A working contact form needs the same server the enrolment layer needs.",
     [("/membership", "Membership"), ("/about", "About the Institute")]),

    ("begin/the-path.html", ("/", "Begin Here"),
     u"Begin here", u"How the education fits together",
     u"The Five Laws, then the Foundation, then everything the Foundation opens — Studies, "
     u"Families, Interwoven Studies and the six Schools.",
     u"Awaiting Michael",
     u"The order he would actually put a new student through, in his words. The home page "
     u"draws the shape of it; this page is where it gets explained properly.",
     [("/courses/five-laws", "The Five Laws — free"),
      ("/courses/foundation", "Foundation Studies"),
      ("/schools", "The six Schools")]),

    # ── Legal ────────────────────────────────────────────────────────────
    ("legal/terms.html", None,
     u"Legal", u"Terms of Service",
     u"The terms on which the Institute sells and teaches.",
     u"Not ours to write",
     u"Terms have to come from the Institute and its advisers. Nothing is drafted here, "
     u"because a plausible-looking placeholder is worse than an empty page — it invites "
     u"someone to ship it.",
     [("/contact", "Contact the Institute"), ("/membership", "Membership")]),

    ("legal/privacy.html", None,
     u"Legal", u"Privacy",
     u"What the Institute records about you, and what it does with it.",
     u"Not ours to write",
     u"This one depends on decisions not yet made: what the enrolment layer stores, which "
     u"payment processor is used, and whether there is analytics. It cannot be written "
     u"before those are settled.",
     [("/contact", "Contact the Institute"), ("/account", "Your account")]),

    ("legal/refunds.html", None,
     u"Legal", u"Refunds",
     u"Where a purchase stands once it is made.",
     u"Not ours to write",
     u"Studies are sold as permanent access and downloadable material, which makes the "
     u"refund position a real decision rather than boilerplate. Michael's call.",
     [("/contact", "Contact the Institute"), ("/membership", "Membership")]),

    # ── The application layer ────────────────────────────────────────────
    ("account.html", None,
     u"Your account", u"Sign in",
     u"Your Studies, your progress through the Foundation, and your membership.",
     u"Needs the application layer",
     u"This is the one part of the Institute a static site genuinely cannot do. Accounts, "
     u"enrolment records, per-lesson progress and the completion event at the end of "
     u"Foundation week ten all need a server — the gate has nothing to read without them. "
     u"Everything else on this site works today.",
     [("/membership", "What membership includes"),
      ("/courses/five-laws", "Start the free course")]),

    ("cart.html", None,
     u"Cart", u"Your cart",
     u"What you have chosen, before you pay for it.",
     u"Needs the application layer",
     u"Checkout needs a payment processor — Stripe is the assumption — and the same server "
     u"the accounts need. Until then every Add to cart on the site lands here, which is "
     u"deliberate: the buying path is drawn end to end even though it does not yet transact.",
     [("/membership", "Membership"), ("/concepts", "The Concept Studies")]),
]


def main():
    n = 0
    for path, parent, kicker, heading, lead, needs_k, needs, links in STUBS:
        full = os.path.join(SRC, path)
        if os.path.exists(full):
            print("  kept    %s" % path)
            continue
        mid = u'\n    <a href="%s">%s</a> <i aria-hidden="true">/</i>' % parent if parent else u""
        text = FM.format(
            title=u"%s — The Institute" % heading,
            desc=lead,
        ) + PAGE.format(
            mid=mid, crumb=heading, kicker=kicker, heading=heading, lead=lead,
            needs_k=needs_k, needs=needs,
            links=u"\n".join(link(h, l) for h, l in links),
        )
        d = os.path.dirname(full)
        if not os.path.isdir(d):
            os.makedirs(d)
        io.open(full, "w", encoding="utf-8", newline="\n").write(text)
        print("  wrote   %s" % path)
        n += 1
    print("\n%d stubs written." % n)


if __name__ == "__main__":
    main()
