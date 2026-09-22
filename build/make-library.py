# -*- coding: utf-8 -*-
"""Write the repeating library pages into src/.

Michael's note of 22 Aug: "item/products will be added in the same categories
that are built today." These are those categories, filled with the names he has
given so far. Run once, then edit the src/ files by hand as his copy arrives —
this script does not overwrite a file that already exists.

    python build/make-library.py

Every page it writes is honest about what is missing. None of them invent copy.
"""

import io, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC  = os.path.join(ROOT, "src")

# ── Michael's material ────────────────────────────────────────────────────

FAMILIES = {
    "acceptance": ("Acceptance Family", "acceptance"),
    "worth":      ("Worth Family",      "worth"),
    "trust":      ("Trust Family",      "trust"),
    "none":       (None,                None),
}

# slug, name, family key
CONCEPTS = [
    ("rejection",      "Rejection",      "acceptance"),
    ("approval",       "Approval",       "acceptance"),
    ("inadequacy",     "Inadequacy",     "worth"),
    ("inferiority",    "Inferiority",    "worth"),
    ("undeserving",    "Undeserving",    "worth"),
    ("self-rejection", "Self-Rejection", "acceptance"),
    ("abandonment",    "Abandonment",    "none"),
    ("shame",          "Shame",          "none"),
    ("fear-and-doubt", "Fear and Doubt", "none"),
    ("suspicion",      "Suspicion",      "trust"),
]

PATTERNS = [
    ("approval-rejection",         "Approval-Rejection"),
    ("people-pleasing",            "People Pleasing"),
    ("control",                    "Control"),
    ("fear-and-doubt",             "Fear and Doubt"),
    ("denial",                     "Denial"),
    ("defensiveness",              "Defensiveness"),
    ("avoidance-of-responsibility","Avoidance of Responsibility"),
    ("guilt",                      "Guilt"),
    ("resentment",                 "Resentment"),
    ("comparison",                 "Comparison"),
    ("perfectionism",              "Perfectionism"),
    ("procrastination",            "Procrastination"),
]

# slug, number, name, summary, principle (Michael's own, where he gave one)
SCHOOLS = [
    ("human-patterns", "01", "School of Human Patterns",
     u"The most relatable entry point. Students begin with the Patterns they already "
     u"recognise in daily life.",
     u"First, because it answers the question most students arrive with: why do I keep "
     u"doing this?"),
    ("human-operating-system", "02", "School of the Human Operating System",
     u"Explains why life repeats, and how consciousness, mind, brain, Concepts, "
     u"expectations, emotions and Patterns work together.", None),
    ("identity", "03", "School of Identity",
     u"Acceptance, approval and rejection, the mother and father relationships, "
     u"self-image, self-worth, roles, masks and belonging.", None),
    ("concepts-and-beliefs", "04", "School of Concepts and Beliefs",
     u"How experiences receive meaning, Concepts are accepted, expectations develop, "
     u"and Patterns are created to validate Concepts.", None),
    ("relationships", "05", "School of Relationships",
     u"Applies the teachings to expectations, communication, responsibility, recurring "
     u"relationship Patterns and resolution.",
     u"Relationships do not create the Concepts within us. They reveal the Concepts that "
     u"already exist."),
    ("consciousness", "06", "School of Consciousness",
     u"Develops awareness, understanding, conscious choice, and participation in the "
     u"direction of life.", None),
]

# slug, name, kind, what it gathers
COLLECTIONS = [
    ("worth-family", "The Worth Family",
     u"Concept Family",
     u"Unworthiness, Inadequacy, Inferiority and Undeserving studied as one set, with the "
     u"Patterns each of them produces."),
    ("interwoven-concepts", "Interwoven Concepts",
     u"Interwoven Study",
     u"Several Concepts that rarely appear alone, studied together because separating them "
     u"misrepresents how they are actually met."),
    ("interwoven-patterns", "Interwoven Patterns",
     u"Interwoven Study",
     u"Patterns that reinforce one another, studied as the braid they form rather than as "
     u"separate habits."),
]


def write(path, text):
    full = os.path.join(SRC, path)
    if os.path.exists(full):
        print("  kept    %s" % path)
        return 0
    d = os.path.dirname(full)
    if not os.path.isdir(d):
        os.makedirs(d)
    io.open(full, "w", encoding="utf-8", newline="\n").write(text)
    print("  wrote   %s" % path)
    return 1


FM = u"""<!--
title: {title}
desc: {desc}
css: study
body: {body}
-->

"""


def concept_page(slug, name, famkey):
    fam, famslug = FAMILIES[famkey]
    crumb_fam = (u'\n    <a href="/concepts/families/%s">%s</a> <i aria-hidden="true">/</i>'
                 % (famslug, fam)) if fam else u""
    if fam:
        belongs = u"""
        <section class="sec">
          <p class="sec__n">03</p>
          <h2 class="sec__h">Where it belongs</h2>
          <p>{name} sits in the <a class="link" href="/concepts/families/{famslug}">{fam}</a>,
             where several Concepts are studied as one set because they rarely appear alone.</p>
        </section>
""".format(name=name, famslug=famslug, fam=fam)
    else:
        belongs = u"""
        <section class="sec">
          <p class="sec__n">03</p>
          <h2 class="sec__h">Where it belongs</h2>
          <div class="needs">
            <span class="needs__k">Awaiting Michael</span>
            <p>{name} appears in none of the four Concept Families as they stand. Either it
               belongs to one that has not been written out yet, or it stands on its own —
               and which of those is true is his to say.</p>
          </div>
        </section>
""".format(name=name)

    return FM.format(
        title=u"%s — Concept Study — The Institute" % name,
        desc=(u"A Concept Study of %s: the beliefs that form around it, the Patterns it "
              u"produces, and how it is validated. $6.99, or $4.99 to a member." % name),
        body=u'data-state="open"',
    ) + u"""<main id="main">
<div class="shell">
  <nav class="crumb" aria-label="Breadcrumb">
    <a href="/">The Institute</a> <i aria-hidden="true">/</i>
    <a href="/concepts">Concept Studies</a> <i aria-hidden="true">/</i>{crumb_fam}
    <span aria-current="page">{name}</span>
  </nav>

  <div class="study">
    <div>
      <div class="study__head">
        <p class="eyebrow eyebrow--plain">Concept Study</p>
        <h1 class="study__title">{name}</h1>

        <span class="state state--open is-open">Available now</span>
        <span class="state state--locked is-locked">Opens after the Foundation</span>
        <span class="state state--progress is-progress">In progress</span>
        <span class="state state--complete is-complete">Complete</span>

        <div class="needs">
          <span class="needs__k">Awaiting Michael</span>
          <p>One sentence defining the Concept, in his words. It appears here, under the name,
             and again wherever this Study is listed.</p>
        </div>

        <p class="gatehelp is-locked">Foundation Studies opens this Study, and every other. You
           can read this page in full and buy it whenever you like.</p>
      </div>

      <div class="sections">

        <section class="sec">
          <p class="sec__n">01</p>
          <h2 class="sec__h">What this Study covers</h2>
          <div class="needs">
            <span class="needs__k">Awaiting Michael</span>
            <p>How {name} influences perception, the beliefs that form around it, the
               expectations it sets, and the way experience is read back as proof of it.</p>
          </div>
        </section>

        <section class="sec">
          <p class="sec__n">02</p>
          <h2 class="sec__h">The Patterns it produces</h2>
          <div class="needs">
            <span class="needs__k">Awaiting Michael</span>
            <p>Which of the Patterns of Behavior this Concept creates. Twelve Patterns are
               named so far — <a class="link" href="/patterns">see them all</a> — but which
               belong to {name} has not been set down.</p>
          </div>
        </section>
{belongs}
        <section class="sec">
          <p class="sec__n">04</p>
          <h2 class="sec__h">What a Study contains</h2>
          <p>The presentation in an audio and a video edition, questions for personal
             investigation, and a Personal Action Plan. Yours permanently once purchased.</p>
        </section>

      </div>

      <div class="belongs" style="margin-top:clamp(2.5rem,4vw,3.5rem)">
        <a href="/concepts">
          <span class="belongs__k">All twelve</span>
          <span class="belongs__n">Concept Studies</span>
          <span class="belongs__d">Twelve Concepts to begin with, each with its Patterns.</span>
        </a>
        <a href="/courses/foundation">
          <span class="belongs__k">What opens this Study</span>
          <span class="belongs__n">Foundation Studies</span>
          <span class="belongs__d">Ten weeks, thirty Patterns. It opens everything that follows.</span>
        </a>
      </div>
    </div>

    <aside class="buy" aria-label="Purchase">
      <div class="buy__card">
        <span class="buy__k">Concept Study</span>

        <div>
          <div class="price">
            <span class="price__now">$6.99</span>
            <span class="price__note">one-off</span>
          </div>
          <p class="price__member">$4.99 with Institute Membership</p>
        </div>

        <a class="btn btn--primary is-open" href="/cart">Add to cart</a>
        <a class="btn btn--primary is-locked" href="/cart">Buy now, begin later</a>
        <a class="btn btn--primary is-progress" href="/account">Resume the Study</a>
        <a class="btn btn--primary is-complete" href="/account">Open the Study</a>

        <a class="btn btn--secondary is-open" href="/courses/five-laws">Start the free course first</a>
        <a class="btn btn--secondary is-locked" href="/courses/foundation">See Foundation Studies</a>

        <ul class="includes">
          <li>The presentation, in an audio and a video edition</li>
          <li>Questions for personal investigation</li>
          <li>A Personal Action Plan</li>
          <li>Yours permanently once purchased</li>
        </ul>
      </div>

      <div class="upsell">
        <p class="upsell__h">Every Study, at the member price</p>
        <p>$19.95 a month brings the member price on Studies, Collections, books and Schools,
           three purchase credits, one featured teaching each month, and question-and-answer
           sessions every six weeks.</p>
        <a class="arrow" href="/membership">Compare the three memberships</a>
      </div>
    </aside>
  </div>
</div>
</main>
""".format(name=name, crumb_fam=crumb_fam, belongs=belongs)


def pattern_page(slug, name):
    return FM.format(
        title=u"%s — Pattern Study — The Institute" % name,
        desc=(u"A Pattern Study of %s: how the Pattern runs, and the Concept underneath it. "
              u"$6.99, or $4.99 to a member." % name),
        body=u'data-state="open"',
    ) + u"""<main id="main">
<div class="shell">
  <nav class="crumb" aria-label="Breadcrumb">
    <a href="/">The Institute</a> <i aria-hidden="true">/</i>
    <a href="/patterns">Patterns of Behavior</a> <i aria-hidden="true">/</i>
    <span aria-current="page">{name}</span>
  </nav>

  <div class="study">
    <div>
      <div class="study__head">
        <p class="eyebrow eyebrow--plain">Pattern Study</p>
        <h1 class="study__title">{name}</h1>

        <span class="state state--open is-open">Available now</span>
        <span class="state state--locked is-locked">Opens after the Foundation</span>
        <span class="state state--progress is-progress">In progress</span>
        <span class="state state--complete is-complete">Complete</span>

        <div class="needs">
          <span class="needs__k">Awaiting Michael</span>
          <p>One sentence describing the Pattern as it is actually met — what it looks like
             from inside, before it has a name.</p>
        </div>

        <p class="gatehelp is-locked">Foundation Studies opens this Study, and every other. You
           can read this page in full and buy it whenever you like.</p>
      </div>

      <div class="sections">

        <section class="sec">
          <p class="sec__n">01</p>
          <h2 class="sec__h">How the Pattern runs</h2>
          <div class="needs">
            <span class="needs__k">Awaiting Michael</span>
            <p>The sequence {name} follows, and the situations that set it going. The purpose
               is not to judge or label, but to make the Pattern visible while it is happening.</p>
          </div>
        </section>

        <section class="sec">
          <p class="sec__n">02</p>
          <h2 class="sec__h">The Concept underneath it</h2>
          <div class="needs">
            <span class="needs__k">Awaiting Michael</span>
            <p>Which Concept this Pattern was built to validate. A Pattern is never the
               beginning of anything — <a class="link" href="/concepts">the Concept Studies</a>
               hold the Concepts, but the pairing has not been set down.</p>
          </div>
        </section>

        <section class="sec">
          <p class="sec__n">03</p>
          <h2 class="sec__h">Where it is met</h2>
          <p>{name} is one of the thirty Patterns introduced across
             <a class="link" href="/courses/foundation">Foundation Studies</a>, three to a week.
             It can also be studied on its own, before or after the Foundation.</p>
        </section>

        <section class="sec">
          <p class="sec__n">04</p>
          <h2 class="sec__h">What a Study contains</h2>
          <p>The presentation in an audio and a video edition, questions for personal
             investigation, and a Personal Action Plan. Yours permanently once purchased.</p>
        </section>

      </div>

      <div class="belongs" style="margin-top:clamp(2.5rem,4vw,3.5rem)">
        <a href="/patterns">
          <span class="belongs__k">All twelve</span>
          <span class="belongs__n">Patterns of Behavior</span>
          <span class="belongs__d">Each studied on its own, or with the Concept beneath it.</span>
        </a>
        <a href="/courses/foundation">
          <span class="belongs__k">Thirty of them, in ten weeks</span>
          <span class="belongs__n">Foundation Studies</span>
          <span class="belongs__d">The programme that opens every Study at the Institute.</span>
        </a>
      </div>
    </div>

    <aside class="buy" aria-label="Purchase">
      <div class="buy__card">
        <span class="buy__k">Pattern Study</span>

        <div>
          <div class="price">
            <span class="price__now">$6.99</span>
            <span class="price__note">one-off</span>
          </div>
          <p class="price__member">$4.99 with Institute Membership</p>
        </div>

        <a class="btn btn--primary is-open" href="/cart">Add to cart</a>
        <a class="btn btn--primary is-locked" href="/cart">Buy now, begin later</a>
        <a class="btn btn--primary is-progress" href="/account">Resume the Study</a>
        <a class="btn btn--primary is-complete" href="/account">Open the Study</a>

        <a class="btn btn--secondary is-open" href="/courses/five-laws">Start the free course first</a>
        <a class="btn btn--secondary is-locked" href="/courses/foundation">See Foundation Studies</a>

        <ul class="includes">
          <li>The presentation, in an audio and a video edition</li>
          <li>Questions for personal investigation</li>
          <li>A Personal Action Plan</li>
          <li>Yours permanently once purchased</li>
        </ul>
      </div>

      <div class="upsell">
        <p class="upsell__h">Every Study, at the member price</p>
        <p>$19.95 a month brings the member price on Studies, Collections, books and Schools,
           three purchase credits, one featured teaching each month, and question-and-answer
           sessions every six weeks.</p>
        <a class="arrow" href="/membership">Compare the three memberships</a>
      </div>
    </aside>
  </div>
</div>
</main>
""".format(name=name)


def school_page(slug, num, name, summary, principle):
    pr = (u"""
        <section class="sec">
          <p class="sec__n">02</p>
          <h2 class="sec__h">Why it sits here</h2>
          <p>%s</p>
        </section>
""" % principle) if principle else u""
    return FM.format(
        title=u"%s — The Institute" % name,
        desc=u"%s" % summary,
        body=u'data-state="open"',
    ) + u"""<main id="main">
<div class="shell">
  <nav class="crumb" aria-label="Breadcrumb">
    <a href="/">The Institute</a> <i aria-hidden="true">/</i>
    <a href="/schools">The Schools</a> <i aria-hidden="true">/</i>
    <span aria-current="page">{name}</span>
  </nav>

  <div class="study">
    <div>
      <div class="study__head">
        <p class="eyebrow eyebrow--plain">School {num} of six</p>
        <h1 class="study__title">{name}</h1>

        <span class="state state--open is-open">Available now</span>
        <span class="state state--locked is-locked">Opens after the Foundation</span>

        <p class="study__def">{summary}</p>

        <p class="gatehelp is-locked">Foundation Studies opens the Schools. You can read this
           page in full and buy from it whenever you like.</p>
      </div>

      <div class="sections">

        <section class="sec">
          <p class="sec__n">01</p>
          <h2 class="sec__h">What a School is</h2>
          <p>Rather than examining only a single Concept or Pattern, each School contains
             multiple Courses devoted to a major area of human understanding. It is the longest
             form of study the Institute offers.</p>
        </section>
{pr}
        <section class="sec">
          <p class="sec__n">03</p>
          <h2 class="sec__h">The Courses inside it</h2>
          <div class="needs">
            <span class="needs__k">Awaiting Michael</span>
            <p>The complete Course list for this School. He notes there is considerably more
               School material already developed than the outline shows.</p>
          </div>
        </section>

        <section class="sec">
          <p class="sec__n">04</p>
          <h2 class="sec__h">Where it falls in the order</h2>
          <p>This is School {num} of the six that open the Institute, in the order Michael
             recommends beginning them. The order is a recommendation, not a requirement —
             <a class="link" href="/schools">see all six</a>.</p>
        </section>

      </div>

      <div class="belongs" style="margin-top:clamp(2.5rem,4vw,3.5rem)">
        <a href="/schools">
          <span class="belongs__k">All six</span>
          <span class="belongs__n">The Schools of the Institute</span>
          <span class="belongs__d">In the order Michael recommends beginning them.</span>
        </a>
        <a href="/courses/foundation">
          <span class="belongs__k">What opens the Schools</span>
          <span class="belongs__n">Foundation Studies</span>
          <span class="belongs__d">Ten weeks, thirty Patterns. It opens everything that follows.</span>
        </a>
      </div>
    </div>

    <aside class="buy" aria-label="Purchase">
      <div class="buy__card">
        <span class="buy__k">School {num}</span>

        <div class="needs" style="margin:0">
          <span class="needs__k">Awaiting Michael</span>
          <p>What a School costs, and whether it is bought whole or by the Course.</p>
        </div>

        <a class="btn btn--secondary" href="/membership">See what membership includes</a>
      </div>

      <div class="upsell">
        <p class="upsell__h">The member price, on the Schools too</p>
        <p>$19.95 a month brings the member price on Studies, Collections, books and Schools,
           three purchase credits, one featured teaching each month, and question-and-answer
           sessions every six weeks.</p>
        <a class="arrow" href="/membership">Compare the three memberships</a>
      </div>
    </aside>
  </div>
</div>
</main>
""".format(name=name, num=num, summary=summary, pr=pr)


def collection_page(slug, name, kind, gathers):
    return FM.format(
        title=u"%s — %s — The Institute" % (name, kind),
        desc=u"%s" % gathers,
        body=u'data-state="open"',
    ) + u"""<main id="main">
<div class="shell">
  <nav class="crumb" aria-label="Breadcrumb">
    <a href="/">The Institute</a> <i aria-hidden="true">/</i>
    <a href="/collections">Interwoven Studies</a> <i aria-hidden="true">/</i>
    <span aria-current="page">{name}</span>
  </nav>

  <div class="study">
    <div>
      <div class="study__head">
        <p class="eyebrow eyebrow--plain">{kind}</p>
        <h1 class="study__title">{name}</h1>

        <span class="state state--open is-open">Available now</span>
        <span class="state state--locked is-locked">Opens after the Foundation</span>

        <p class="study__def">{gathers}</p>

        <p class="gatehelp is-locked">Foundation Studies opens this Study, and every other. You
           can read this page in full and buy it whenever you like.</p>
      </div>

      <div class="sections">

        <section class="sec">
          <p class="sec__n">01</p>
          <h2 class="sec__h">What it gathers</h2>
          <div class="needs">
            <span class="needs__k">Awaiting Michael</span>
            <p>Which Studies belong to this set, and in what order they are met. The shape is
               settled — one set, bought once, cheaper than its parts — but the contents are
               his to name.</p>
          </div>
        </section>

        <section class="sec">
          <p class="sec__n">02</p>
          <h2 class="sec__h">Why they are studied together</h2>
          <div class="needs">
            <span class="needs__k">Awaiting Michael</span>
            <p>A line on why separating these misrepresents how they are actually met. The
               <a class="link" href="/collections/unworthiness">Unworthiness set</a> is the
               worked example of the form.</p>
          </div>
        </section>

        <section class="sec">
          <p class="sec__n">03</p>
          <h2 class="sec__h">What a set contains</h2>
          <p>Every Study in the set, each with its presentation in an audio and a video edition,
             questions for personal investigation, and a Personal Action Plan. Yours permanently
             once purchased.</p>
        </section>

      </div>

      <div class="belongs" style="margin-top:clamp(2.5rem,4vw,3.5rem)">
        <a href="/collections">
          <span class="belongs__k">All of them</span>
          <span class="belongs__n">Interwoven Studies</span>
          <span class="belongs__d">Concepts and Patterns that are met together, studied together.</span>
        </a>
        <a href="/concepts">
          <span class="belongs__k">One at a time instead</span>
          <span class="belongs__n">Concept Studies</span>
          <span class="belongs__d">Twelve Concepts to begin with, each at $6.99.</span>
        </a>
      </div>
    </div>

    <aside class="buy" aria-label="Purchase">
      <div class="buy__card">
        <span class="buy__k">{kind}</span>

        <div class="needs" style="margin:0">
          <span class="needs__k">Awaiting Michael</span>
          <p>The price of this set. The Unworthiness set is $24.99 against $27.96 bought
             separately, which is the pattern the others will follow.</p>
        </div>

        <a class="btn btn--secondary" href="/collections/unworthiness">See the worked example</a>
      </div>

      <div class="upsell">
        <p class="upsell__h">Every set, at the member price</p>
        <p>$19.95 a month brings the member price on Studies, Collections, books and Schools,
           three purchase credits, one featured teaching each month, and question-and-answer
           sessions every six weeks.</p>
        <a class="arrow" href="/membership">Compare the three memberships</a>
      </div>
    </aside>
  </div>
</div>
</main>
""".format(name=name, kind=kind, gathers=gathers)


def main():
    n = 0
    print("Concept Studies")
    for slug, name, fam in CONCEPTS:
        n += write("concepts/%s.html" % slug, concept_page(slug, name, fam))
    print("Pattern Studies")
    for slug, name in PATTERNS:
        n += write("patterns/%s.html" % slug, pattern_page(slug, name))
    print("Schools")
    for args in SCHOOLS:
        n += write("schools/%s.html" % args[0], school_page(*args))
    print("Interwoven Studies")
    for args in COLLECTIONS:
        n += write("collections/%s.html" % args[0], collection_page(*args))
    print("\n%d pages written." % n)


if __name__ == "__main__":
    main()
