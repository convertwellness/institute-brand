# -*- coding: utf-8 -*-
"""Write the Institute's library pages from the two data files.

    python build/make-catalog.py      write the pages into src/
    python build/build.py             then build the site as usual

content/catalog.json   every item: what it is, where it lives, its status
content/pricing.json   every tier and price, and whether prices are shown

Every page this writes carries `generated: catalog` in its front matter and is
rewritten on every run, so edit the data, not the page. A page marked
"page": "hand" in the catalogue is never touched.

Nothing here writes teaching copy. Where Michael's words are missing the page
says so in place, with the open item it is waiting on (O1 to O13, listed in
docs/questions-for-michael.md).

While pricing.json has display: "held", no figure is written into any page.
"""

import io, os, re, sys, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC  = os.path.join(ROOT, "src")

CAT   = json.load(io.open(os.path.join(ROOT, "content", "catalog.json"), encoding="utf-8"))
PRICE = json.load(io.open(os.path.join(ROOT, "content", "pricing.json"), encoding="utf-8"))

HELD  = PRICE["display"] != "show"
GATE  = CAT["settings"]["foundation_gate"]
ITEMS = [i for i in CAT["items"]]
SHIP  = [i for i in ITEMS if i["status"] != "hold"]
FAM   = {f["id"]: f for f in CAT["families"]}
SCH   = {s["id"]: s for s in CAT["schools"]}
BYID  = {i["id"]: i for i in ITEMS}

TBC = "To be confirmed"
FORMAT_NAME = {"watch": "Watch", "self-guided": "Self-guided", "written": "Written"}

# the routes this script owns besides the item pages
OWNED_INDEXES = []


# ── small helpers ────────────────────────────────────────────────────────

def esc(t):
    return (t or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def money(n):
    if isinstance(n, (int, float)):
        if n == 0:
            return "Free"
        return ("$%.2f" % n) if (isinstance(n, float) and n != int(n)) else ("$%d" % n)
    return n


def figures(text):
    """{{9}} is a figure: shown as $9, or not at all while prices are held."""
    def rep(m):
        v, pct = m.group(1), m.group(2)
        if pct:
            return "a discount to be confirmed" if HELD else "%s%% off" % v
        return "an amount to be confirmed" if HELD else money(float(v) if "." in v else int(v))
    return re.sub(r"\{\{([0-9.]+)(%)?\}\}", rep, text)


def opens(o):
    return (" &middot; " + ", ".join(o)) if o else ""


def needs(text, o=None, label="Awaiting Michael"):
    return (u'<div class="needs"><span class="needs__k">%s%s</span>\n'
            u'            <p>%s</p></div>' % (label, opens(o), text))


def crumbs(*pairs):
    out = ['<nav class="crumb" aria-label="Breadcrumb">',
           '    <a href="/">The Institute</a> <i aria-hidden="true">/</i>']
    for href, name in pairs[:-1]:
        out.append('    <a href="%s">%s</a> <i aria-hidden="true">/</i>' % (href, esc(name)))
    out.append('    <span aria-current="page">%s</span>' % esc(pairs[-1][1]))
    out.append('  </nav>')
    return "\n".join(out)


def page(title, desc, main, css="study"):
    return (u"<!--\ntitle: %s | The Institute\ndesc: %s\ncss: %s\nbody: \n"
            u"generated: catalog\n-->\n\n<main id=\"main\">\n<div class=\"shell\">\n  %s\n</div>\n</main>\n"
            % (title, desc, css, main))


def write(route, text):
    rel = route.strip("/") + ".html"
    full = os.path.join(SRC, rel.replace("/", os.sep))
    if os.path.exists(full):
        old = io.open(full, encoding="utf-8").read()
        if "generated: catalog" not in old and not ADOPT:
            print("  SKIP   %s  (written by hand; pass --adopt to take it over)" % rel)
            return 0
    d = os.path.dirname(full)
    if not os.path.isdir(d):
        os.makedirs(d)
    io.open(full, "w", encoding="utf-8", newline="\n").write(text)
    return 1


# ── prices ───────────────────────────────────────────────────────────────

def price_row(key):
    return PRICE["prices"].get(key) if key else None


def price_lines(key):
    """(headline, member line) for one price key."""
    p = price_row(key)
    if p is None:
        return ("Price not yet set", "Not on the Price Menu yet")
    if p.get("public") == 0:
        return ("Free", "Free to everyone")
    if HELD:
        return (TBC, "Member prices to be confirmed (O1)")
    if p.get("public") is None:
        return ("Price to be set", p.get("note", ""))
    nums = [p[c] for c in ("seeker", "explorer", "discoverer") if isinstance(p.get(c), (int, float))]
    member = ("Members from %s" % money(min(nums))) if nums else "Member pricing by tier"
    return (money(p["public"]), member)


def tbc_class(head):
    return " price__now--tbc" if head in (TBC, "Price not yet set", "Price to be set") else ""


def item_price_note(key):
    head, _ = price_lines(key)
    return "Price to be confirmed" if head == TBC else head


# ── the buying block, the same on every study page ───────────────────────

def formats_text(formats):
    return ", ".join(FORMAT_NAME[f] for f in formats) if formats else "Formats to be confirmed"


def buy_block(kind, item, collection=None, extra_buttons="", study=True):
    head, member = price_lines(item.get("price"))
    alt = ""
    if item.get("price_alt"):
        ah, _ = price_lines(item["price_alt"])
        alt = ('\n        <p class="price__member">%s: %s</p>'
               % (esc(PRICE["prices"][item["price_alt"]]["label"]), ah))
    coll = ""
    if collection:
        href, name = collection
        coll = '\n        <a class="btn btn--secondary" href="%s">Buy %s</a>' % (href, esc(name))
    free = head == "Free"
    primary = ('<a class="btn btn--primary" href="/account">Start free</a>' if free
               else '<a class="btn btn--primary" href="/cart">Buy this %s</a>' % kind.lower())
    fam = item.get("family")
    fam_dd = ('<a class="link" href="%s">The %s Family</a>' % (FAM[fam]["route"], esc(FAM[fam]["title"]))
              if fam else "Not yet placed")
    gate = ""
    if GATE and not free:
        gate = ('\n        <p class="gatehelp">The Foundation of the Institute Course opens this '
                'study. You can read this page in full and buy it now.</p>')
    return u"""<aside class="buy" aria-label="Purchase">
      <div class="buy__card">
        <span class="buy__k">{kind}</span>
        <div>
          <div class="price">
            <span class="price__now{tbc}">{head}</span>
            <span class="price__note">{once}</span>
          </div>
          <p class="price__member">{member}</p>{alt}
        </div>{gate}
        {primary}{coll}
        <a class="btn btn--secondary" href="/membership">Become a member</a>{extra}
        <dl class="facts">
          <dt>Formats</dt><dd>{formats}</dd>{studyfacts}
        </dl>
      </div>
    </aside>""".format(kind=esc(kind), tbc=tbc_class(head), head=head,
                       once="" if free else "one-off", member=member, alt=alt,
                       gate=gate, primary=primary, coll=coll, extra=extra_buttons,
                       formats=formats_text(item.get("formats")),
                       studyfacts=(STUDY_FACTS % fam_dd) if study else "")


STUDY_FACTS = u"""
          <dt>Concept Family</dt><dd>%s</dd>
          <dt>Interwoven Studies</dt><dd>To be confirmed</dd>"""


def facts_section(n, item):
    note = ""
    if item.get("note"):
        note = "\n          " + needs(esc(item["note"]), item.get("open"), label="Note for Michael")
    return u"""<section class="sec">
          <p class="sec__n">{n}</p>
          <h2 class="sec__h">Formats</h2>
          <p>{formats}. Written material can be downloaded and kept for personal study.
             Presentations, voiced or self-guided, are streamed and cannot be downloaded.</p>{note}
        </section>""".format(n=n, formats=formats_text(item.get("formats")), note=note)


def study_shell(kind, crumb, title, head_extra, sections, aside, belongs):
    return u"""{crumb}

  <div class="study">
    <div>
      <div class="study__head">
        <p class="eyebrow eyebrow--plain">{kind}</p>
        <h1 class="study__title">{title}</h1>
        {head}
      </div>

      <div class="sections">
        {sections}
      </div>

      <div class="belongs" style="margin-top:clamp(2.5rem,4vw,3.5rem)">
        {belongs}
      </div>
    </div>

    {aside}
  </div>""".format(crumb=crumb, kind=esc(kind), title=esc(title), head=head_extra,
                   sections="\n\n        ".join(sections), aside=aside, belongs=belongs)


def belong(href, k, n, d):
    return (u'<a href="%s">\n          <span class="belongs__k">%s</span>\n'
            u'          <span class="belongs__n">%s</span>\n'
            u'          <span class="belongs__d">%s</span>\n        </a>' % (href, k, n, d))


def sec(n, h, body):
    return (u'<section class="sec">\n          <p class="sec__n">%s</p>\n'
            u'          <h2 class="sec__h">%s</h2>\n          %s\n        </section>' % (n, h, body))


# ── item pages ───────────────────────────────────────────────────────────

def family_collection(item):
    f = item.get("family")
    if f:
        return (FAM[f]["route"], "the %s Family" % FAM[f]["title"])
    return ("/collections", "an Interwoven Study")


def concept_page(i):
    fam = i.get("family")
    if fam:
        where = ('<p>%s is studied in the <a class="link" href="%s">%s Family</a>, where several '
                 'Concepts are studied as one set.</p>' % (esc(i["title"]), FAM[fam]["route"], esc(FAM[fam]["title"])))
    else:
        where = needs("Which Concept Family %s belongs to. It has not been placed in one of the ten."
                      % esc(i["title"]), i.get("open"))
    crumb = [("/concepts", "Concept Studies")]
    if fam:
        crumb.append((FAM[fam]["route"], "%s Family" % FAM[fam]["title"]))
    crumb.append((None, i["title"]))
    main = study_shell(
        "Concept Study", crumbs(*crumb), i["title"],
        needs("One sentence defining the Concept, in his words."),
        [sec("01", "What this Study covers",
             needs("How %s influences perception, the beliefs and expectations that form around it, "
                   "and how experience is read back as proof of it." % esc(i["title"]))),
         sec("02", "The Patterns it produces",
             needs("Which Patterns this Concept produces.")),
         sec("03", "Where it belongs", where),
         facts_section("04", i)],
        buy_block("Concept Study", i, family_collection(i)),
        belong("/concepts", "All of them", "Concept Studies", "Each Concept studied on its own.") +
        "\n        " + belong("/concepts/families", "Studied as a set", "The ten Concept Families",
                              "Each Family is a package of five studies."))
    return page("%s, Concept Study" % i["title"],
                "A Concept Study of %s. Price to be confirmed." % i["title"] if HELD
                else "A Concept Study of %s." % i["title"], main)


def pattern_page(i):
    where = '<p>%s can be studied on its own, before or after the Foundation of the Institute Course.</p>' % esc(i["title"])
    if i.get("school"):
        s = SCH[i["school"]]
        where = ('<p>%s is Core Study %d in the <a class="link" href="%s">%s</a>. It can also be '
                 'studied on its own.</p>' % (esc(i["title"]), i["core_study"], s["route"], esc(s["title"])))
    main = study_shell(
        "Pattern Study", crumbs(("/patterns", "Patterns of Behavior"), (None, i["title"])), i["title"],
        needs("One sentence describing the Pattern as it is met, in his words."),
        [sec("01", "How the Pattern runs", needs("The sequence %s follows, and what sets it going." % esc(i["title"]))),
         sec("02", "The Concept underneath it", needs("Which Concept this Pattern validates.")),
         sec("03", "Where it is studied", where),
         facts_section("04", i)],
        buy_block("Pattern Study", i, ("/collections/interwoven-patterns", "an Interwoven Pattern Study")),
        belong("/patterns", "All of them", "Patterns of Behavior", "Each Pattern studied on its own.") +
        "\n        " + belong("/collections", "Studied together", "Interwoven Studies", "Three or six Patterns woven together."))
    return page("%s, Pattern Study" % i["title"], "A Pattern Study of %s." % i["title"], main)


def relationship_page(i):
    main = study_shell(
        "Relationship Study", crumbs(("/relationships", "Relationship Studies"), (None, i["title"])), i["title"],
        needs("The files for this study have not arrived. It is on the Price Menu.", ["O13"]),
        [sec("01", "What this Study covers", needs("What %s covers, in his words." % esc(i["title"]))),
         facts_section("02", i)],
        buy_block("Relationship Study", i, ("/relationships", "three Relationship Studies")),
        belong("/relationships", "All six", "Relationship Studies", "Bought singly, in threes, or as the complete collection."))
    return page("%s, Relationship Study" % i["title"], "A Relationship Study: %s." % i["title"], main)


def teaching_page(i):
    extra = ""
    if i.get("bundle"):
        h, _ = price_lines(i["bundle"])
        extra = ('\n        <p class="price__member">%s together: %s</p>'
                 % (esc(PRICE["prices"][i["bundle"]]["label"]), h))
    head = needs(esc(i["note"]), i.get("open")) if i["status"] == "placeholder" else needs("A sentence introducing %s, in his words." % esc(i["title"]))
    main = study_shell(
        "Universal Teaching", crumbs(("/universal-teachings", "Universal Teachings"), (None, i["title"])), i["title"],
        head,
        [sec("01", "What it teaches", needs("What %s teaches." % esc(i["title"]))),
         facts_section("02", dict(i, note=None if i["status"] == "placeholder" else i.get("note")))],
        buy_block("Universal Teaching", i, ("/universal-teachings", "the Complete Universal Teachings Collection"), extra),
        belong("/universal-teachings", "All of them", "Universal Teachings", "The Twelve Spiritual Gifts, the Twelve Disciplines, and more."))
    return page(i["title"], "%s, one of the Universal Teachings of the Institute." % i["title"], main)


def selfguided_page(i):
    parts = ""
    if i.get("parts"):
        parts = sec("02", "In this study",
                    '<ul class="includes">%s</ul>' % "".join("<li>%s</li>" % esc(p) for p in i["parts"]))
    secs = [sec("01", "What this study covers", needs("What the %s study covers, in his words." % esc(i["title"])))]
    if parts:
        secs.append(parts)
    secs.append(sec("%02d" % (len(secs) + 1), "Two editions",
                    "<p>The slides on their own, or the slides with the written study.</p>"))
    secs.append(facts_section("%02d" % (len(secs) + 1), i))
    secs.append(sec("%02d" % (len(secs) + 1), "Education, not treatment",
                    "<p>This study is educational. It is not diagnosis or treatment.</p>"))
    main = study_shell(
        "Self-Guided Study", crumbs(("/self-guided-studies", "Self-Guided Studies"), (None, i["title"])), i["title"],
        needs("A sentence introducing the study, in his words."),
        secs,
        buy_block("Self-Guided Study", i, study=False),
        belong("/self-guided-studies", "All of them", "Self-Guided Studies", "Studies of health, taken at your own pace."))
    return page("%s, Self-Guided Study" % i["title"], "A self-guided study of %s." % i["title"], main)


def course_page(i):
    secs = [sec("01", "What the Course covers", needs("What %s covers, and how it is taught." % esc(i["title"]))),
            facts_section("02", i)]
    main = study_shell(
        "Course", crumbs(("/courses", "Courses"), (None, i["title"])), i["title"],
        ('<p class="study__def">%s</p>' % esc(i["summary"])) if i.get("summary") else needs("A sentence introducing the Course, in his words."),
        secs,
        buy_block("Course", i, study=False),
        belong("/courses", "All of them", "Courses", "From the free Five Laws to the ten-week Foundation."))
    return page(i["title"], "%s, a Course of the Institute." % i["title"], main)


def collection_page(i):
    secs = []
    if i.get("lessons"):
        lh, _ = price_lines(i.get("lesson_price"))
        lis = "".join('<li class="week"><span class="week__n">%02d</span><span class="week__h">%s</span>'
                      '<span class="week__d">Lesson on its own: %s</span></li>' % (n + 1, esc(t), lh)
                      for n, t in enumerate(i["lessons"]))
        secs.append(sec("01", "The lessons", '<ol class="weeks">%s</ol>' % lis))
    else:
        secs.append(sec("01", "What it gathers", needs("Which studies belong to this set, and in what order.")))
    secs.append(sec("%02d" % (len(secs) + 1), "Why they are studied together",
                    needs("A line on why these are studied together, in his words.")))
    if i.get("redirect_family"):
        f = FAM[i["redirect_family"]]
        secs.append(sec("%02d" % (len(secs) + 1), "The Family package",
                        '<p>This set is the <a class="link" href="%s">%s Family</a> package.</p>' % (f["route"], esc(f["title"]))))
    main = study_shell(
        "Interwoven Study", crumbs(("/collections", "Interwoven Studies"), (None, i["title"])), i["title"],
        '<p class="study__def">%s</p>' % esc(i.get("summary", "")),
        secs,
        buy_block("Collection", i, study=False),
        belong("/collections", "All of them", "Interwoven Studies", "Concepts and Patterns studied together."))
    return page(i["title"], i.get("summary", i["title"]), main)


# ── families ─────────────────────────────────────────────────────────────

def family_page(f, n):
    concepts = [i for i in SHIP if i["type"] == "concept" and i.get("family") == f["id"] and i.get("route")]
    pkg = "".join(
        '<li class="week"><span class="week__n">%02d</span><span class="week__h">%s</span>'
        '<span class="week__d">%s</span></li>' % (k + 1, esc(p["title"].replace("{family}", f["title"])),
                                                 FORMAT_NAME.get(p["format"], "Format to be confirmed"))
        for k, p in enumerate(CAT["family_package"]))
    if concepts:
        cl = ('<ul class="includes">%s</ul>' % "".join(
            '<li><a class="link" href="%s">%s</a></li>' % (c["route"], esc(c["title"])) for c in concepts))
    else:
        cl = needs("Which Concept Studies sit in the %s Family." % esc(f["title"]))
    note = ""
    if f.get("note"):
        note = "\n        " + sec("04", "A note on this Family", needs(esc(f["note"]), f.get("open"), label="Note for Michael"))
    fake = {"price": "family-collection", "formats": [], "family": f["id"]}
    main = study_shell(
        "Concept Family %02d of 10" % n,
        crumbs(("/concepts", "Concept Studies"), ("/concepts/families", "Concept Families"), (None, "The %s Family" % f["title"])),
        "The %s Family" % f["title"],
        needs("The Family's own description, in his words."),
        [sec("01", "The Family package", '<p>Every Family is studied as the same five pieces.</p><ol class="weeks">%s</ol>' % pkg),
         sec("02", "Concept Studies in this Family", cl),
         sec("03", "Its Patterns", needs("The primary Patterns of the %s Family." % esc(f["title"])))] + ([note.strip()] if note else []),
        buy_block("Pattern Family Collection", fake, study=False),
        belong("/concepts/families", "All ten", "Concept Families", "The ten Families that open the library."))
    return page("The %s Family" % f["title"], "The %s Family: a package of five studies." % f["title"], main)


# ── schools ──────────────────────────────────────────────────────────────

def school_page(s, n):
    weeks = CAT["school_weeks"]
    core = ""
    if s.get("core_studies"):
        rows = []
        for k, iid in sorted(s["core_studies"].items(), key=lambda kv: int(kv[0])):
            it = BYID[iid]
            rows.append('<li class="week"><span class="week__n">%02d</span><span class="week__h">'
                        '<a class="link" href="%s">%s</a></span></li>' % (int(k), it["route"], esc(it["title"])))
        core = sec("{N}", "Core Studies",
                   '<ol class="weeks">%s</ol>\n          %s' % ("".join(rows),
                   needs("The other Core Studies in this School, and their order.", ["O13"])))
    principle = ""
    if s.get("principle"):
        principle = sec("02", "Why it sits here", "<p>%s</p>" % esc(s["principle"]))
    notes = []
    if s.get("open"):
        msg = {"O8": "Whether this is a School of its own. It is listed as: %s." % esc(s["listed"]),
               "O6": "Its final name. It is listed as: %s." % esc(s["listed"]),
               "O13": esc(s.get("note", "Material for this School has not arrived."))}
        for o in s["open"]:
            notes.append(needs(msg[o], [o], label="Open question"))
    head = ('<p class="study__def">%s</p>' % esc(s["summary"])) if s.get("summary") else needs("A sentence introducing the School, in his words.")
    if notes:
        head += "\n        " + "\n        ".join(notes)
    secs = [sec("01", "A twelve-week program",
                "<p>Each School is a twelve-week program. Monthly members receive one week at a time.</p>")]
    if principle:
        secs.append(principle)
    if core:
        secs.append(core.replace("{N}", "%02d" % (len(secs) + 1)))
    secs.append(sec("%02d" % (len(secs) + 1), "The weeks", needs("The %d weeks of this School, in order." % weeks)))
    fake = {"price": "school", "formats": [], "family": None}
    main = study_shell(
        "School %02d" % n, crumbs(("/schools", "The Schools"), (None, s["title"])), s["title"],
        head, secs, buy_block("School", fake, study=False),
        belong("/schools", "All of them", "The Schools of the Institute", "Each a twelve-week program."))
    return page(s["title"], s.get("summary") or "%s, a twelve-week program." % s["title"], main)


# ── tracks ───────────────────────────────────────────────────────────────

def track_page(t):
    parts = ""
    if t["parts"]:
        lis = "".join(
            '<li class="week week--needs"><span class="week__n">%02d</span><span class="week__h">'
            '<a class="link" href="%s/%s-%d">%s %d</a></span><span class="week__d">Title awaiting Michael</span></li>'
            % (k, t["route"], t["parts_label"].lower(), k, t["parts_label"], k) for k in range(1, t["parts"] + 1))
        parts = sec("02", "The %ss" % t["parts_label"].lower(), '<ol class="weeks">%s</ol>' % lis)
    else:
        parts = sec("02", "The essays and teachings", needs("The titles in this track.", ["O9"]))
    note = ""
    if t.get("note"):
        note = sec("03", "A note on this track", needs(esc(t["note"]), t.get("open"), label="Open question"))
    door = ("/begin", "Begin Here") if t["door"] == "begin" else ("/learn", "Learn")
    head = '<p class="study__def">%s</p>' % esc(t["summary"])
    secs = [sec("01", "About this track", needs("What Track %d is for, and who it is for, in his words." % t["number"], ["O9"])), parts]
    if note:
        secs.append(note)
    main = u"""{crumb}

  <div class="study" style="grid-template-columns:1fr">
    <div>
      <div class="study__head">
        <p class="eyebrow eyebrow--plain">Track {n}</p>
        <h1 class="study__title">{title}</h1>
        {head}
      </div>
      <div class="sections">
        {secs}
      </div>
      <div class="belongs" style="margin-top:clamp(2.5rem,4vw,3.5rem)">
        {b1}
        {b2}
      </div>
    </div>
  </div>""".format(crumb=crumbs(door, (None, t["title"])), n=t["number"], title=esc(t["title"]),
                   head=head, secs="\n\n        ".join(secs),
                   b1=belong("/membership", "Membership", "Every track, at the member price", "Four tiers in the current draft."),
                   b2=belong("/", "Three tracks", "Back to the Institute", "Personal Mastery, Holistic Health Educator, Wholistic Essays and Teachings."))
    return page(t["title"], "Track %d of the Institute: %s. %s" % (t["number"], t["title"], t["summary"]), main)


def track_part(t, k):
    label = "%s %d" % (t["parts_label"], k)
    free = t.get("free")
    main = u"""{crumb}

  <div class="stub">
    <p class="stub__k">{track}</p>
    <h1 class="stub__h">{label}</h1>
    <p class="stub__lead">{lead}</p>
    {needs}
    <div class="stub__on">
      <a class="arrow" href="{back}">{tname}</a>
    </div>
  </div>""".format(crumb=crumbs(("/begin" if t["door"] == "begin" else "/learn", "Begin Here" if t["door"] == "begin" else "Learn"),
                                (t["route"], t["title"]), (None, label)),
                   track="Track %d &middot; %s" % (t["number"], esc(t["title"])), label=label,
                   lead=("Free." if free else "Part of the %s." % esc(t["summary"].rstrip(".").lower())),
                   needs=needs("The title and content of %s." % label, ["O9"]),
                   back=t["route"], tname=esc(t["title"]))
    return page("%s, %s" % (label, t["title"]), "%s of the %s track." % (label, t["title"]), main)


# ── index pages ──────────────────────────────────────────────────────────

def define(key):
    return ('<section class="define">\n    %s\n  </section>' %
            "\n    ".join("<p>%s</p>" % esc(p) for p in CAT["definitions"][key]))


def card(href, k, n, d, p=None, fam=None):
    attr = (' data-fam="%s"' % fam) if fam else ""
    pp = ('\n      <span class="item__p">%s</span>' % p) if p else ""
    return (u'<a class="item" href="%s"%s>\n      <span class="item__k">%s</span>\n'
            u'      <span class="item__n">%s</span>\n      <span class="item__d">%s</span>%s\n    </a>'
            % (href, attr, k, esc(n), d, pp))


def index_page(crumb, eyebrow, h1, lead, body, cards, foot="", define_key=None, title=None, desc=None, extra=""):
    main = u"""{crumb}

  <div class="index__head">
    <p class="eyebrow eyebrow--plain">{eyebrow}</p>
    <h1 class="index__title">{h1}</h1>
    <p class="index__lead">{lead}</p>
    {body}
  </div>
  {define}
  {extra}
  <div class="cards" id="grid">
    {cards}
  </div>

  <div class="index__foot">
    {foot}
  </div>""".format(crumb=crumb, eyebrow=eyebrow, h1=h1, lead=lead, body=body,
                   define=define(define_key) if define_key else "", extra=extra,
                   cards="\n    ".join(cards), foot=foot)
    return page(title or eyebrow, desc or lead, main)


def concepts_index():
    cs = [i for i in SHIP if i["type"] == "concept" and i.get("route")]
    cs.sort(key=lambda i: i["title"])
    counts = {}
    for c in cs:
        counts[c.get("family") or "none"] = counts.get(c.get("family") or "none", 0) + 1
    btns = ['<button class="filt" type="button" data-filter="all" aria-pressed="true">All <span class="filt__n">%d</span></button>' % len(cs)]
    for f in CAT["families"]:
        if counts.get(f["id"]):
            btns.append('<button class="filt" type="button" data-filter="%s" data-label="the %s Family" aria-pressed="false">%s <span class="filt__n">%d</span></button>'
                        % (f["id"], esc(f["title"]), esc(f["title"]), counts[f["id"]]))
    if counts.get("none"):
        btns.append('<button class="filt" type="button" data-filter="none" data-label="no Family yet" aria-pressed="false">Not yet placed <span class="filt__n">%d</span></button>' % counts["none"])
    filters = ('<div class="filters" role="group" aria-label="Filter by Concept Family">\n    <span class="filters__k">Family</span>\n    %s\n  </div>\n  <p class="sr-only" id="filter-said" role="status" aria-live="polite"></p>'
               % "\n    ".join(btns))
    cards = [card(c["route"], ("%s Family" % FAM[c["family"]]["title"]) if c.get("family") else "Family not yet placed",
                  c["title"], formats_text(c["formats"]), item_price_note(c["price"]), c.get("family") or "none") for c in cs]
    held = [i["title"] for i in ITEMS if i["type"] == "concept" and i["status"] == "hold"]
    foot = needs("Held by Michael, and not shown in the library: %s." % ", ".join(held), ["O4"], label="Held")
    return index_page(crumbs((None, "Concept Studies")), "Concept Studies", "Everything begins with&nbsp;Concept.",
                      "Each Concept is studied on its own. Choose the ones most relevant to your life now.",
                      "", cards, foot, "concepts", extra=filters)


def patterns_index():
    ps = sorted([i for i in SHIP if i["type"] == "pattern"], key=lambda i: i["title"])
    cards = [card(p["route"], "Pattern Study", p["title"], formats_text(p["formats"]), item_price_note(p["price"])) for p in ps]
    return index_page(crumbs((None, "Patterns of Behavior")), "Patterns of Behavior", "Patterns of&nbsp;Behavior",
                      "Each Pattern is studied on its own, with the Concept underneath it.",
                      "", cards, needs("About twenty-seven voiced Pattern videos are in the material. Their titles are not yet listed here.", ["O12"]),
                      "patterns")


def families_index():
    cards = []
    for n, f in enumerate(CAT["families"], 1):
        cs = [i["title"] for i in SHIP if i["type"] == "concept" and i.get("family") == f["id"] and i.get("route")]
        cards.append(card(f["route"], "Family %02d" % n, f["title"],
                          (", ".join(esc(c) for c in cs) + ".") if cs else "Concepts not yet placed.",
                          item_price_note("family-collection")))
    foot = needs("Which Family Abandonment and Shame belong to.", ["O4"], label="Open question")
    return index_page(crumbs(("/concepts", "Concept Studies"), (None, "Concept Families")), "Concept Families",
                      "Ten Concept&nbsp;Families", "Each Family is studied as a package of five: the Concept itself, the Approval and Rejection Pathways, Personal Application and Review, and the Modus Operandi video.",
                      "", cards, foot, title="Concept Families")


def collections_index():
    cs = [i for i in SHIP if i["type"] == "collection"]
    cards = [card(c["route"], "Interwoven Study" if "interwoven" in c["id"] else "Collection", c["title"],
                  esc(c.get("summary", "")), item_price_note(c["price"])) for c in cs]
    return index_page(crumbs((None, "Interwoven Studies")), "Interwoven Studies", "Studied together, because they are met&nbsp;together.",
                      "Concepts and Patterns woven together, in threes and sixes, and the collections built from them.",
                      "", cards, "", title="Interwoven Studies")


def relationships_index():
    rs = [i for i in SHIP if i["type"] == "relationship"]
    cards = [card(r["route"], "Relationship Study", r["title"], "Files not yet received.", item_price_note(r["price"])) for r in rs]
    h3, _ = price_lines("three-relationship")
    hc, _ = price_lines("complete-relationship")
    body = ('<p class="index__body">Three Relationship Studies together: %s. The complete collection: %s.</p>' % (h3, hc))
    return index_page(crumbs((None, "Relationship Studies")), "Relationship Studies", "Relationship&nbsp;Studies",
                      "Six studies of the relationships that shape us.", body, cards,
                      needs("The files for these six studies have not arrived. They are on the Price Menu.", ["O13"]),
                      title="Relationship Studies")


def teachings_index():
    ts = [i for i in SHIP if i["type"] == "teaching"]
    cards = [card(t["route"], "Universal Teaching", t["title"], formats_text(t["formats"]),
                  item_price_note(t["price"]) if t["price"] else "Price not yet set") for t in ts]
    hb, _ = price_lines("gifts-and-disciplines")
    hc, _ = price_lines("complete-universal")
    body = ('<p class="index__body">The Twelve Spiritual Gifts and Twelve Disciplines together: %s. '
            'The Complete Universal Teachings Collection: %s.</p>' % (hb, hc))
    return index_page(crumbs(("/learn", "Learn"), (None, "Universal Teachings")), "Universal Teachings", "Universal&nbsp;Teachings",
                      "The principles the teachings rest on.", body, cards, "", title="Universal Teachings")


def eightfold_index():
    vs = [i for i in SHIP if i.get("series") == "eightfold"]
    h, _ = price_lines("short-video")
    cards = ['<div class="item"><span class="item__k">Short video %02d</span><span class="item__n">%s</span>'
             '<span class="item__d">Watch. Streamed only.%s</span><span class="item__p">%s</span></div>'
             % (n, esc(v["title"]), (" " + esc(v["note"])) if v.get("note") else "",
                "Price to be confirmed" if h == TBC else h)
             for n, v in enumerate(vs, 1)]
    body = ('<p class="index__body">Short videos of three to five minutes. Members watch them as part of '
            'their tier; anyone can buy them singly. Bundles are to be set.</p>')
    return index_page(crumbs(("/learn", "Learn"), (None, "The Eightfold Path")), "Short videos", "The Eightfold&nbsp;Path",
                      "A series of short videos.", body, cards,
                      needs("Whether these are the eight new videos Michael mentioned, and the short video series on body parts, vitamins and diseases that will follow.", ["O12", "O13"], label="Open question"),
                      title="The Eightfold Path")


def selfguided_index():
    ss = [i for i in SHIP if i["type"] == "self-guided"]
    cards = [card(s["route"], "Self-Guided Study", s["title"],
                  ("In three parts: %s." % ", ".join(s["parts"])) if s.get("parts") else "Slides, or slides with the written study.",
                  item_price_note(s["price"])) for s in ss]
    body = ('<p class="index__body">Each study is self-guided slides, with a written study as a second edition. '
            'They are educational, not diagnosis or treatment.</p>')
    return index_page(crumbs(("/learn", "Learn"), (None, "Self-Guided Studies")), "Self-Guided Studies", "Self-Guided&nbsp;Studies",
                      "Studies of health, taken at your own pace.", body, cards, "", title="Self-Guided Studies")


def schools_index():
    cards = []
    for n, s in enumerate(CAT["schools"], 1):
        k = "School %02d" % n
        if s.get("open") and "O8" in s["open"]:
            k += " &middot; O8"
        cards.append(card(s["route"], k, s["title"], esc(s.get("summary") or "A twelve-week program."), item_price_note("school")))
    return index_page(crumbs((None, "The Schools")), "The Schools", "The Schools of the&nbsp;Institute",
                      "Each School is a twelve-week program.", "", cards,
                      needs(esc(CAT["schools_order_note"]) + " The Price Menu lists ten Schools; the folders hold twelve. Belonging and Relationships are in the folders only.", ["O8"], label="Open question"),
                      "schools", title="The Schools")


def courses_index():
    cs = [i for i in SHIP if i["type"] == "course" and i.get("route")]
    cards = [card(c["route"], "Free course" if c.get("free") else "Course", c["title"],
                  esc(c.get("summary") or formats_text(c["formats"])), item_price_note(c["price"])) for c in cs]
    return index_page(crumbs(("/learn", "Learn"), (None, "Courses")), "Courses", "Courses",
                      "Organised studies of one subject, in a purposeful sequence.", "", cards, "", "courses", title="Courses")


def learn_index():
    tr = [t for t in CAT["tracks"] if t["door"] == "learn"]
    cards = [card(t["route"], "Track %d" % t["number"], t["title"], esc(t["summary"])) for t in tr]
    cards += [
        card("/courses", "Courses", "Courses", "The Foundation of the Institute Course, the Self Exploratory Course and more."),
        card("/universal-teachings", "Universal Teachings", "Universal Teachings", "The Twelve Spiritual Gifts and the Twelve Disciplines, and more."),
        card("/eightfold-path", "Short videos", "The Eightfold Path", "A series of short videos."),
        card("/self-guided-studies", "Self-Guided Studies", "Self-Guided Studies", "Studies of health, taken at your own pace."),
        card("/books", "Books", "Books and study editions", "Written editions."),
        card("/events", "Live Events", "Live Events", "Seminars on a single subject."),
    ]
    return index_page(crumbs((None, "Learn")), "Learn", "Learn",
                      "The taught material: two tracks, the Courses, the Universal Teachings and the self-guided studies.",
                      "", cards, "", title="Learn")


# ── membership ───────────────────────────────────────────────────────────

def tier_card(t, lead):
    name = t["name"] or "Name awaiting Michael"
    if HELD or t["monthly"] is None:
        price = '<span class="tier__price tier__price--tbc">%s</span>' % TBC
        per = '<span class="tier__per">monthly or annual</span>'
    else:
        price = '<span class="tier__price">%s</span>' % money(t["monthly"])
        per = '<span class="tier__per">a month, or %s a year</span>' % money(t["annual"])
    if t.get("discount_note"):
        disc = t["discount_note"]
    elif t.get("discount_pct") is None:
        disc = "Member discount to be confirmed"
    else:
        disc = "Member discount to be confirmed" if HELD else "%d%% off every purchase" % t["discount_pct"]
    cap = ""
    if t.get("cap_per_year"):
        cap = '\n              <p class="tier__cap">Limited to %d a year</p>' % t["cap_per_year"]
    lis = "".join("<li>%s</li>" % esc(figures(x)) for x in t["inclusions"]) or "<li>Inclusions awaiting Michael (O1)</li>"
    return u"""<div class="tier{lead}">
              <span class="tier__k">{disc}</span>
              <span class="tier__name">{name}</span>
              <div>{price} {per}</div>{cap}
              <ul class="tier__list">{lis}</ul>
              <a class="btn btn--primary" href="/account">Join as {name}</a>
            </div>""".format(lead=" tier--lead" if lead else "", disc=esc(disc), name=esc(name),
                             price=price, per=per, cap=cap, lis=lis)


def membership_page():
    m = PRICE["models"][PRICE["active_model"]]
    other = [v for k, v in PRICE["models"].items() if k != PRICE["active_model"]]
    tiers = "\n            ".join(tier_card(t, n == 0) for n, t in enumerate(m["tiers"]))
    rules = "".join("<li>%s</li>" % esc(r) for r in PRICE["release_rules"])
    o_note = needs("Two tier models are on the table. This page shows %s, the current draft. "
                   "The other is %s, of which only the first tier, Foundation Free, is known. "
                   "Michael to say which is final." % (esc(m["label"]), esc(other[0]["label"]) if other else "none"),
                   ["O1"], label="Open question")
    refund = needs("Monthly: a full refund of the first payment if cancelled within 30 days, once per member. "
                   "After that, cancel any time, effective at the end of the paid month. "
                   "Annual paid in full: not cancellable or refundable, with full access for twelve months, "
                   "and a reminder at least fourteen days before it renews. How to cancel, and the contact "
                   "address, are still blank.", ["O11"], label="Pending legal review")
    main = u"""{crumb}

  <div class="index__head">
    <p class="eyebrow eyebrow--plain">Membership</p>
    <h1 class="index__title">Join in a&nbsp;moment.</h1>
    <p class="index__lead">There is no application. Choose a tier and you are a member at once.
       Membership brings a discount on everything you buy, and more of the library with each tier.</p>
    {o_note}
  </div>

  <div class="study" style="grid-template-columns:1fr">
    <div>
      <div class="sections">

        <section class="sec">
          <h2 class="sec__h">{label}</h2>
          <div class="tiers tiers--4">
            {tiers}
          </div>
          <p>Annual membership is ten months' price for twelve months. Prices are held until Michael confirms them.</p>
        </section>

        <section class="sec">
          <h2 class="sec__h">How material is released</h2>
          <ul class="includes">{rules}</ul>
        </section>

        <section class="sec">
          <h2 class="sec__h">Upgrading</h2>
          <p>{upgrade}</p>
        </section>

        <section class="sec">
          <h2 class="sec__h">What you keep</h2>
          <div class="access">
            <div><h3>Streamed</h3><p>Presentations, voiced or self-guided, are streamed for as long as you have access. They cannot be downloaded.</p></div>
            <div><h3>Downloaded</h3><p>Written material can be downloaded, carries your name, and is yours to keep for personal study, even after you cancel.</p></div>
            <div><h3>One person</h3><p>A membership is for one person. Shared accounts can be suspended.</p></div>
          </div>
          {caps}
        </section>

        <section class="sec">
          <h2 class="sec__h">Refunds and cancelling</h2>
          {refund}
        </section>

        <section class="sec">
          <h2 class="sec__h">The Scholarship Fund</h2>
          <p>The Scholarship Fund sponsors memberships for students.
             <a class="link" href="/scholarship">Give to the fund, or apply for a scholarship.</a></p>
        </section>

      </div>
    </div>
  </div>""".format(crumb=crumbs((None, "Membership")), o_note=o_note, label=esc(m["label"]),
                   tiers=tiers, rules=rules, upgrade=esc(PRICE["upgrade_rule"]),
                   caps=needs("Whether any tier has a limit on downloads.", ["O7"], label="Open question"),
                   refund=refund)
    return page("Membership", "Membership of the Institute: instant join, four tiers in the current draft. Prices to be confirmed.", main)


# ── the Scholarship Fund ─────────────────────────────────────────────────

def scholarship_page():
    sc = PRICE["scholarship"]
    if HELD:
        gifts = ('<p>Gift levels are set and will show here once Michael confirms the prices, '
                 'with any amount welcome.</p>')
        monthly = "A small monthly gift sponsors a Seeker membership. The amount is held with the prices."
    else:
        gifts = '<ul class="gifts">%s%s</ul>' % ("".join("<li>%s</li>" % money(g) for g in sc["gift_levels"]),
                                                  "<li>Any amount</li>" if sc["any_amount"] else "")
        monthly = "%s a month sponsors a %s." % (money(sc["monthly_sponsor"]["amount"]), sc["monthly_sponsor"]["sponsors"])
    main = u"""{crumb}

  <div class="index__head">
    <p class="eyebrow eyebrow--plain">The Scholarship Fund</p>
    <h1 class="index__title">The Scholarship&nbsp;Fund</h1>
    <p class="index__lead">The Scholarship Fund sponsors memberships for students.
       Give to the fund, or apply for a scholarship.</p>
  </div>

  <div class="study" style="grid-template-columns:1fr">
    <div>
      <div class="sections">
        <section class="sec">
          <p class="sec__n">01</p>
          <h2 class="sec__h">Give</h2>
          {gifts}
          <p>{monthly}</p>
          <a class="btn btn--primary" href="/scholarship" style="align-self:flex-start">Give to the fund</a>
          {give_needs}
        </section>

        <section class="sec">
          <p class="sec__n">02</p>
          <h2 class="sec__h">Who receives the gift</h2>
          <p>The fund is held by the {charity}, a {status} organisation.</p>
          {tax_needs}
        </section>

        <section class="sec">
          <p class="sec__n">03</p>
          <h2 class="sec__h">Apply for a scholarship</h2>
          <p>A scholarship is applied for separately from membership. Membership itself needs no application.</p>
          <p><a class="arrow" href="/scholarship/apply">The scholarship application</a></p>
        </section>
      </div>
    </div>
  </div>""".format(crumb=crumbs((None, "Scholarship Fund")), gifts=gifts, monthly=monthly,
                   charity=esc(sc["charity"]), status=esc(sc["charity_status"]),
                   give_needs=needs("How gifts are taken: a payment link, and the address for questions. Both are blank in Michael's document.", ["O2"]),
                   tax_needs=needs("The wording Michael wants about tax deductibility, if any.", label="Awaiting Michael"))
    return page("Scholarship Fund", "The Scholarship Fund of the Institute: give to the fund, or apply for a scholarship.", main)


def scholarship_apply_page():
    main = u"""{crumb}

  <div class="stub">
    <p class="stub__k">The Scholarship Fund</p>
    <h1 class="stub__h">Apply for a scholarship</h1>
    <p class="stub__lead">Michael's Scholarship Application is written. It goes here.</p>
    {n1}
    {n2}
    <div class="stub__on">
      <a class="arrow" href="/scholarship">The Scholarship Fund</a>
      <a class="arrow" href="/membership">Membership</a>
    </div>
  </div>""".format(crumb=crumbs(("/scholarship", "Scholarship Fund"), (None, "Apply")),
                   n1=needs("The link to the application form. It is blank in Michael's document.", ["O2"]),
                   n2=needs("The email address applications and questions go to. Blank in Michael's document."))
    return page("Apply for a Scholarship", "Apply to the Scholarship Fund of the Institute.", main)


# ── run ──────────────────────────────────────────────────────────────────

ADOPT = "--adopt" in sys.argv


def main():
    n = 0
    pages = []
    gen = {"concept": concept_page, "pattern": pattern_page, "relationship": relationship_page,
           "teaching": teaching_page, "self-guided": selfguided_page, "course": course_page,
           "collection": collection_page}
    for i in SHIP:
        if i.get("page") == "gen" and i.get("route"):
            pages.append((i["route"], gen[i["type"]](i)))
    for k, f in enumerate(CAT["families"], 1):
        pages.append((f["route"], family_page(f, k)))
    for k, s in enumerate(CAT["schools"], 1):
        pages.append((s["route"], school_page(s, k)))
    for t in CAT["tracks"]:
        pages.append((t["route"], track_page(t)))
        for k in range(1, t["parts"] + 1):
            pages.append(("%s/%s-%d" % (t["route"], t["parts_label"].lower(), k), track_part(t, k)))
    pages += [("/concepts", concepts_index()), ("/patterns", patterns_index()),
              ("/concepts/families", families_index()), ("/collections", collections_index()),
              ("/relationships", relationships_index()), ("/universal-teachings", teachings_index()),
              ("/eightfold-path", eightfold_index()), ("/self-guided-studies", selfguided_index()),
              ("/schools", schools_index()), ("/courses", courses_index()), ("/learn", learn_index()),
              ("/membership", membership_page()),
              ("/scholarship", scholarship_page()), ("/scholarship/apply", scholarship_apply_page())]

    for route, text in pages:
        if HELD and re.search(r"\$[0-9]", re.sub(r"<!--.*?-->", "", text, flags=re.S)):
            sys.exit("%s: a price leaked while prices are held" % route)
        if re.search(u"[–—]|&#821[12];|&[mn]dash;", text):
            sys.exit("%s: an em or en dash in generated copy" % route)
        n += write(route, text)
    print("%d pages written from content/catalog.json (prices %s)." % (n, "held" if HELD else "shown"))


if __name__ == "__main__":
    main()
