# -*- coding: utf-8 -*-
"""Assemble site/ from src/ and build/partials/.

Every page is a <main> block, optionally a tail block, plus a few lines of front
matter. The header, the mobile drawer and the footer live in one place each;
change them once and every page changes. Run from anywhere:

    python build/build.py

Nothing here is clever. It is string substitution, on purpose — the point is
that the next person can read it in a minute.
"""

import io, os, re, sys, glob, json, hashlib

ROOT  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC   = os.path.join(ROOT, "src")
OUT   = os.path.join(ROOT, "site")
PARTS = os.path.join(ROOT, "build", "partials")

CSS_V, JS_V, STUDY_V = "41", "15", "12"   # bump to bust caches

TAIL_MARK = u"<!-- \u2550\u2550 page tail"

SHELL = u"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#FDFBF3">

<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/icon-192.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Inter:wght@400;500;600&display=swap">
<link rel="stylesheet" href="{up}styles.css?v={cssv}">{study}
</head>
<body{bodyattr}>

<a class="skip" href="#main">Skip to content</a>

{header}

{drawer}

{main}

{footer}

<script src="{up}app.js?v={jsv}"></script>
{tail}</body>
</html>
"""


def read(p):
    return io.open(p, encoding="utf-8").read()


def asset_stamp(url):
    """?v=<first 8 of the file's sha1>. The filename never changes, so a browser
    that already has the old picture keeps it — which is exactly what happened
    when the hero was replaced. Stylesheets have been versioned since the start;
    images were not."""
    rel = url.split("?")[0].lstrip("/")
    f = os.path.join(OUT, rel)
    if not os.path.isfile(f):
        return url
    h = hashlib.sha1(io.open(f, "rb").read()).hexdigest()[:8]
    return url.split("?")[0] + "?v=" + h


ASSET_RE = re.compile(r'(src|href)="(/assets/[^"?]+\.(?:webp|png|jpg|svg))"')


def stamp_assets(html):
    return ASSET_RE.sub(lambda m: '%s="%s"' % (m.group(1), asset_stamp(m.group(2))), html)


# -- The search index -----------------------------------------------------
# Michael and Sara need to find a word across 67 pages -- "where does it say
# governs?" -- so the index carries the body text, not just the titles. It is
# written once here and fetched by the browser only when someone actually
# opens search, so it costs nothing on an ordinary page load.

SCRIPT_RE  = re.compile(r"<(script|style)[^>]*>.*?</\1>", re.S | re.I)
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
TAG_RE     = re.compile(r"<[^>]+>")
WS_RE      = re.compile(r"\s+")
HEAD_RE    = re.compile(r"<h[1-3][^>]*>(.*?)</h[1-3]>", re.S | re.I)
# the breadcrumb repeats the title and the section on every page, so it
# would otherwise be the first thing in every snippet
CRUMB_RE   = re.compile(r'<nav class="crumb".*?</nav>', re.S | re.I)

ENTITIES = [("&amp;", "&"), ("&#8212;", u"\u2014"), ("&nbsp;", " "),
            ("&middot;", u"\u00b7"), ("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"')]


def plain(html):
    """Visible text, with markup, scripts and our own notes taken out."""
    t = COMMENT_RE.sub(" ", html)     # AWAITING-MICHAEL notes are ours, not the page
    t = SCRIPT_RE.sub(" ", t)
    t = TAG_RE.sub(" ", t)
    for a, b in ENTITIES:
        t = t.replace(a, b)
    return WS_RE.sub(" ", t).strip()


def index_entry(route, meta, main):
    main = CRUMB_RE.sub(" ", main)
    title = meta["title"]
    short = title.split(u"\u2014")[0].strip() or title
    heads = [plain(h) for h in HEAD_RE.findall(main)]
    heads = [h for h in heads if h and h != short]
    return {
        "u": route,
        "t": short,
        "d": meta["desc"],
        "h": heads[:12],
        "x": plain(main),
        "k": (route.strip("/").split("/")[0] or "home"),
    }


# -- The site outline -----------------------------------------------------
# Drawn from the routes themselves rather than written by hand, so it cannot
# drift the way a maintained list would. A group whose own address has no page
# -- /begin, /legal -- is shown as a heading rather than a link.

# Four states, counted from the page itself rather than tracked by hand.
#   written  nothing outstanding
#   draft    scaffolding is standing in and needs his words
#   open     a placeholder is showing; nothing is there at all
#   held     deliberately not his to write, or waiting on a server
HELD = {
    "/legal/terms": "The Institute's advisers",
    "/legal/privacy": "The Institute's advisers",
    "/legal/refunds": "The Institute's advisers",
    "/michael": "His own biography",
    "/account": "Needs a server",
    "/cart": "Needs a server",
}

AREA_NEED = {
    "concepts":    "A definition, how it shapes perception, and its Patterns \u2014 for each Concept",
    "patterns":    "What it looks like from inside, its sequence, and the Concept it validates",
    "schools":     "The Course list inside each School, and what a School costs",
    "collections": "What each set contains, in what order, and what it costs",
    "books":       "Every book is a title and nothing else \u2014 no description, format or price",
    "courses":     "The five Laws and their format; the ten weeks of the Foundation",
    "events":      "Date, format, length, price and subject for each seminar",
    "membership":  "How much membership the bundle includes, and for how long",
    "about":       "What the Institute is, in his voice",
    "contact":     "An address for enquiries and one for support",
    "begin":       "The order he would put a new student through",
}

STATE_LABEL = {"written": "Written", "draft": "Draft standing in",
               "open": "Nothing yet", "held": "Held"}


def page_state(route, body):
    if route in HELD:
        return "held", 0
    slots = body.count("AWAITING-MICHAEL")
    showing = body.count('<div class="needs"')
    if not slots and not showing:
        return "written", 0
    return ("open" if showing else "draft"), (slots or showing)


def sitemap_grid(routes):
    """Areas ranked by how much of them is still his to write."""
    areas = {}
    for r, _t, _d, state, n in routes:
        g = (r.strip("/").split("/")[0] or "home")
        a = areas.setdefault(g, {"pages": 0, "todo": 0, "slots": 0})
        a["pages"] += 1
        if state in ("draft", "open"):
            a["todo"] += 1
            a["slots"] += n

    rows = sorted(areas.items(), key=lambda kv: (-kv[1]["slots"], kv[0]))
    # the note sits outside the scroll box: a <caption> takes the table's
    # width, so on a phone it would be clipped with the columns
    out = ['<p class="grid__note">Ranked by how much is still to write. '
           'Counted from the pages themselves each time the site is built.</p>',
           '<div class="gridwrap"><table class="grid">',
           "<caption class=\"vh\">What is still to be written, by area</caption>",
           "<thead><tr><th scope=\"col\">Area</th>"
           "<th scope=\"col\" class=\"num\">Pages</th>"
           "<th scope=\"col\" class=\"num\">Needing him</th>"
           "<th scope=\"col\" class=\"num\">Pieces to write</th>"
           "<th scope=\"col\">What is needed</th></tr></thead><tbody>"]
    tp = tt = ts = 0
    for g, a in rows:
        tp += a["pages"]; tt += a["todo"]; ts += a["slots"]
        cls = ' class="grid__r--done"' if not a["slots"] else ""
        out.append(
            "<tr%s><th scope=\"row\">%s</th>"
            "<td class=\"num\">%d</td><td class=\"num\">%d</td>"
            "<td class=\"num\"><b>%d</b></td><td>%s</td></tr>"
            % (cls, esc(GROUP_NAME.get(g, g.title())), a["pages"], a["todo"],
               a["slots"], esc(AREA_NEED.get(g, "\u2014"))))
    out.append("</tbody><tfoot><tr><th scope=\"row\">All of it</th>"
               "<td class=\"num\">%d</td><td class=\"num\">%d</td>"
               "<td class=\"num\"><b>%d</b></td><td></td></tr></tfoot>"
               % (tp, tt, ts))
    out.append("</table></div>")
    return "".join(out)


GRID_MARK = "<!-- SITEMAP-GRID -->"

OUTLINE_ORDER = ["begin", "concepts", "patterns", "collections", "courses",
                 "schools", "books", "events", "membership",
                 "about", "michael", "contact", "account", "cart", "legal"]

GROUP_NAME = {
    "begin": "Begin here", "concepts": "Concept Studies",
    "patterns": "Pattern Studies", "collections": "Interwoven Studies",
    "courses": "Courses", "schools": "The Schools", "books": "Books",
    "events": "Live Events", "membership": "Membership", "about": "The Institute",
    "michael": "Michael Schwartz, N.D.", "contact": "Contact",
    "account": "Your account", "cart": "Cart", "legal": "Legal",
    "sitemap": "Site outline", "home": "Home page",
}

SITEMAP_MARK = "<!-- SITEMAP -->"


def esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def _node(route, meta_by_route, depth, kids_html, count=None):
    m = meta_by_route.get(route)
    name = esc(m["short"]) if m else esc(route)
    out = ['<li class="tree__i tree__i--%d">' % depth]
    if m:
        out.append('<a class="tree__link" href="%s">' % route)
        out.append('<span class="tree__n">%s</span>' % name)
        out.append('<span class="tree__u">%s</span>' % esc(route))
        out.append('<span class="tag tag--%s">%s%s</span></a>'
                   % (m["state"], STATE_LABEL[m["state"]],
                      (" &middot; %d" % m["n"]) if m["n"] else ""))
        # a description where it explains a branch, not on all 67 entries
        if m["desc"] and (depth == 1 or (depth == 2 and kids_html)):
            out.append('<p class="tree__d">%s</p>' % esc(m["desc"]))
    else:
        out.append('<p class="tree__n tree__n--plain">%s</p>' % name)
    if count:
        out.append('<p class="tree__c">%s</p>' % count)
    out.append(kids_html)
    out.append("</li>")
    return "".join(out)


def sitemap_tree(routes):
    """routes: list of (route, title, desc), every page in the site."""
    meta = {}
    for r, title, desc, state, n in routes:
        meta[r] = {"short": title.split(u"\u2014")[0].strip() or title,
                   "desc": desc, "state": state, "n": n}

    groups = {}
    for r, _t, _d, _s, _n in routes:
        if r == "/":
            continue
        groups.setdefault(r.strip("/").split("/")[0], []).append(r)

    order = [g for g in OUTLINE_ORDER if g in groups]
    order += sorted(g for g in groups if g not in OUTLINE_ORDER)

    html = ['<ol class="tree">']
    for g in order:
        rs = sorted(groups[g])
        root = "/" + g
        children = [r for r in rs if r != root and r.count("/") == 2]
        kids = []
        for c in sorted(children):
            gks = [r for r in rs if r.startswith(c + "/")]
            gk_html = ""
            if gks:
                gk_html = ('<ol class="tree__kids">'
                           + "".join(_node(x, meta, 3, "") for x in sorted(gks))
                           + "</ol>")
            kids.append(_node(c, meta, 2, gk_html,
                              count=("%d pages" % len(gks)) if gks else None))
        kids_html = ('<ol class="tree__kids">' + "".join(kids) + "</ol>") if kids else ""

        if root in meta:
            n = len([r for r in rs if r != root])
            html.append(_node(root, meta, 1, kids_html,
                              count=("%d pages beneath" % n) if n else None))
        else:
            html.append('<li class="tree__i tree__i--1">'
                        '<p class="tree__n tree__n--plain">%s</p>%s</li>'
                        % (esc(GROUP_NAME.get(g, g.title())), kids_html))
    html.append("</ol>")
    return "".join(html)


def split_tail(text):
    """A page may carry markup and script of its own after the footer — the mock
    gate-state bar, the Concepts filter. Everything past the marker goes there."""
    i = text.find(TAIL_MARK)
    if i < 0:
        return text, u""
    nl = text.index(u"\n", i) + 1
    return text[:i], text[nl:]


def front_matter(text):
    """Pull `key: value` lines out of the leading HTML comment."""
    m = re.match(r"\s*<!--\s*\n(.*?)\n\s*-->\s*\n", text, re.S)
    if not m:
        sys.exit("no front matter in source file")
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, text[m.end():]


def mark_current(chrome, route):
    """Give the link to the page you are on aria-current, so the header says
    where you are to a screen reader as well as to the eye."""
    if route in (None, "/"):
        return chrome
    return chrome.replace('href="%s"' % route, 'href="%s" aria-current="page"' % route)


def build():
    header, drawer, footer = (read(os.path.join(PARTS, n + ".html")).rstrip("\n")
                              for n in ("header", "drawer", "footer"))

    sources = sorted(glob.glob(os.path.join(SRC, "**", "*.html"), recursive=True))
    if not sources:
        sys.exit("src/ is empty — nothing to build")

    # every route and its front matter, so the outline can be drawn before
    # the first page is written
    routes = []
    for src_path in sources:
        m, _ = front_matter(read(src_path))
        r = "/" + os.path.relpath(src_path, SRC).replace("\\", "/")[:-5]
        if r == "/index":
            r = "/"
        if m.get("flat") == "yes":
            continue                                # 404 is not a destination
        st, n = page_state(r, _)
        routes.append((r, m["title"], m["desc"], st, n))
    outline = sitemap_tree(routes)
    grid    = sitemap_grid(routes)

    entries = []

    for s in sources:
        rel   = os.path.relpath(s, SRC).replace("\\", "/")
        route = "/" + rel[:-5]                      # strip .html
        if route == "/index":
            route, depth = "/", 0
        else:
            depth = route.count("/")
        up = "../" * depth

        meta, body = front_matter(read(s))

        # A flat page sits beside index.html rather than in a folder of its own.
        # 404.html is the only one: the host serves it for any address it cannot
        # match, so it must live at the root and link with absolute paths.
        # Assets must be absolute: the host serves this file's contents at
        # whatever address failed, so "styles.css" would resolve against that
        # address and 404 in its turn.
        if meta.get("flat") == "yes":
            depth, up, route = 0, "/", None
        main, tail = split_tail(body)
        if SITEMAP_MARK in main:
            main = main.replace(SITEMAP_MARK, outline)
        if GRID_MARK in main:
            main = main.replace(GRID_MARK, grid)
        tail  = ("\n" + tail.strip() + "\n") if tail.strip() else ""
        study = ('\n<link rel="stylesheet" href="%sstudy.css?v=%s">' % (up, STUDY_V)
                 if meta.get("css") == "study" else "")

        page = SHELL.format(
            title=meta["title"], desc=meta["desc"], up=up,
            cssv=CSS_V, jsv=JS_V, study=study, tail=tail,
            bodyattr=(" " + meta["body"]) if meta.get("body") else "",
            header=mark_current(header, route),
            drawer=mark_current(drawer, route),
            main=main.strip(), footer=footer,
        )

        if route is None:
            dest = os.path.join(OUT, rel)
        elif route == "/":
            dest = os.path.join(OUT, "index.html")
        else:
            dest = os.path.join(OUT, rel[:-5], "index.html")
        d = os.path.dirname(dest)
        if not os.path.isdir(d):
            os.makedirs(d)
        io.open(dest, "w", encoding="utf-8", newline="\n").write(stamp_assets(page))
        if route:                       # 404 is not a destination
            entries.append(index_entry(route, meta, main))
        print("  %-34s -> %s" % (route or "(404)", os.path.relpath(dest, ROOT).replace("\\", "/")))

    idx = os.path.join(OUT, "search-index.json")
    io.open(idx, "w", encoding="utf-8", newline="\n").write(
        json.dumps({"v": 1, "pages": entries}, ensure_ascii=False, separators=(",", ":")))

    print("\n%d pages built.  search-index.json: %d pages, %.0f KB."
          % (len(sources), len(entries), os.path.getsize(idx) / 1024.0))


if __name__ == "__main__":
    build()
