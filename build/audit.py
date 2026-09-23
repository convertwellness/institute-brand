# -*- coding: utf-8 -*-
"""Check the built site: dead internal links, and where content is still missing.

    python build/audit.py

Exits non-zero if any internal link points at a route that does not exist, so it
can go in CI later. The placeholder count is reported, not failed on — those are
deliberate and they are the list to hand Michael.
"""

import io, os, re, sys, glob, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT  = os.path.join(ROOT, "site")


def main():
    pages = sorted(glob.glob(os.path.join(OUT, "**", "*.html"), recursive=True))
    if not pages:
        sys.exit("site/ is empty — run python build/build.py first")

    routes, flat = set(), set()
    for p in pages:
        rel = os.path.relpath(p, OUT).replace("\\", "/")
        if os.path.basename(rel) != "index.html":
            flat.add("/" + rel)                     # 404.html and friends
            continue
        d = os.path.dirname(rel)
        routes.add("/" if d == "" else "/" + d)

    # A link can also point at a file that is not a page — the favicons, an
    # image, a stylesheet. Anything actually present under site/ is a real
    # target, so the whole tree counts, not just the HTML in it.
    for dirpath, _dirs, files in os.walk(OUT):
        for fn in files:
            rel = os.path.relpath(os.path.join(dirpath, fn), OUT).replace("\\", "/")
            flat.add("/" + rel)

    dead = collections.Counter()
    where = collections.defaultdict(set)
    needs = collections.Counter()
    drafts = collections.Counter()
    total_links = 0

    for p in pages:
        rel = os.path.relpath(p, OUT).replace("\\", "/")
        text = io.open(p, encoding="utf-8").read()

        n = text.count('class="needs"') + text.count('class="week week--needs"')
        if n:
            needs[rel] = n
        d = text.count('class="draft"')
        if d:
            drafts[rel] = d

        for h in re.findall(r'href="(/[^"#?]*)"', text):
            total_links += 1
            h2 = h.rstrip("/") or "/"
            if h2 not in routes and h2 not in flat:
                dead[h2] += 1
                where[h2].add(rel)

    print("%d pages, %d routes, %d internal links" % (len(pages), len(routes), total_links))

    if dead:
        print("\nDEAD LINKS — %d instances across %d targets" % (sum(dead.values()), len(dead)))
        for h, n in sorted(dead.items(), key=lambda kv: -kv[1]):
            src = sorted(where[h])
            tail = " (+%d more)" % (len(src) - 3) if len(src) > 3 else ""
            print("  %4d  %-40s from %s%s" % (n, h, ", ".join(src[:3]), tail))
    else:
        print("\nNo dead internal links.")

    if needs:
        print("\nAwaiting Michael — %d placeholders across %d pages"
              % (sum(needs.values()), len(needs)))
        for rel, n in sorted(needs.items(), key=lambda kv: (-kv[1], kv[0]))[:12]:
            print("  %3d  %s" % (n, rel))
        if len(needs) > 12:
            print("       ... and %d more pages" % (len(needs) - 12))

    if drafts:
        print("")
        print("Draft copy — %d blocks across %d pages. This is NOT Michael's writing."
              % (sum(drafts.values()), len(drafts)))
        print("  remove with: python build/drafts.py --strip")

    print("\nRemember: the host must serve /404.html for unmatched addresses,")
    print("otherwise a wrong URL gets the host's own bare error page.")

    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())
