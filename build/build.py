# -*- coding: utf-8 -*-
"""Assemble site/ from src/ and build/partials/.

Every page is a <main> block, optionally a tail block, plus a few lines of front
matter. The header, the mobile drawer and the footer live in one place each;
change them once and every page changes. Run from anywhere:

    python build/build.py

Nothing here is clever. It is string substitution, on purpose — the point is
that the next person can read it in a minute.
"""

import io, os, re, sys, glob, hashlib

ROOT  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC   = os.path.join(ROOT, "src")
OUT   = os.path.join(ROOT, "site")
PARTS = os.path.join(ROOT, "build", "partials")

CSS_V, JS_V, STUDY_V = "27", "11", "12"   # bump to bust caches

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
        print("  %-34s -> %s" % (route or "(404)", os.path.relpath(dest, ROOT).replace("\\", "/")))

    print("\n%d pages built." % len(sources))


if __name__ == "__main__":
    build()
