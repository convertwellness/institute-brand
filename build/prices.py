# -*- coding: utf-8 -*-
"""Show or hold the prices. Every price lives in content/pricing.json.

    python build/prices.py --list      what is set, and whether it is showing
    python build/prices.py --hold      every page says "to be confirmed"
    python build/prices.py --show      every page shows the figures

--hold and --show flip "display" in content/pricing.json, then rewrite the
library pages (build/make-catalog.py) and rebuild the site (build/build.py).

Sara, Nov 11 2026: keep prices hidden until Michael confirms them (open item
O1). While held, no figure is written into any page at all, so the numbers
cannot be found by viewing the page source.

This replaces the Sep 2026 tool, which swapped figures in and out of the
hand-written pages and kept them in build/prices-held.json. Those were the
pre-November prices, which Michael's Nov 3 Price Menu supersedes; they are in
git history (commit be34060) if they are ever needed.
"""

import io, os, sys, json, subprocess

ROOT  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE  = os.path.join(ROOT, "content", "pricing.json")


def load():
    return io.open(FILE, encoding="utf-8").read()


def set_display(value):
    text = load()
    data = json.loads(text)
    if data["display"] == value:
        print("prices are already %s" % ("shown" if value == "show" else "held"))
    else:
        old = '"display": "%s"' % data["display"]
        if old not in text:
            sys.exit("could not find %s in content/pricing.json" % old)
        io.open(FILE, "w", encoding="utf-8", newline="\n").write(
            text.replace(old, '"display": "%s"' % value, 1))
        print("prices now %s" % ("shown" if value == "show" else "held"))
    for script in ("make-catalog.py", "build.py"):
        subprocess.run([sys.executable, os.path.join(ROOT, "build", script)], check=True,
                       stdout=subprocess.DEVNULL)
    print("pages rewritten and site rebuilt")


def listing():
    data = json.loads(load())
    print("display: %s    tier model shown: %s\n" % (data["display"], data["active_model"]))
    for key, m in data["models"].items():
        print("  %s  (%s)" % (m["label"], m["status"]))
        for t in m["tiers"]:
            print("     %-16s monthly %-6s annual %s" % (t["name"] or "(name unknown)", t["monthly"], t["annual"]))
    unset = [k for k, p in data["prices"].items() if p.get("public") is None]
    print("\n%d price lines, %d still to be set: %s"
          % (len(data["prices"]), len(unset), ", ".join(unset)))


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if   arg == "--hold": set_display("held")
    elif arg == "--show": set_display("show")
    elif arg == "--list": listing()
    else: sys.exit(__doc__)
