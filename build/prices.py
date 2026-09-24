# -*- coding: utf-8 -*-
"""Hold every price on the site as "to be confirmed" — and put them back.

    python build/prices.py --hold      every price becomes to-be-confirmed
    python build/prices.py --restore   put the numbers back, exactly
    python build/prices.py --list      what is held, and what is showing

Sara, 24 Sep 2026. Twenty-five distinct prices are published across the site
and not one of them traces to a file in this repository. content/site.ts —
which CLAUDE.md names as the source of every string — carries no numbers at
all, only Michael's definitions of Public Price and Member Price. The figures
came off a pricing document that was never committed, and Michael has since
said the pricing needs to change. So the site should stop asserting them.

Every change is recorded in build/prices-held.json as the exact pair of
strings, in the order applied. --restore walks that list backwards, so the
round trip is byte-for-byte; the tool checks that itself before it writes.

Prose is rewritten sentence by sentence rather than by swapping the number
inside it. "Each Study is $6.99, or $4.99 with Institute Membership" would
otherwise read "Each Study is to be confirmed, or to be confirmed with
Institute Membership", which is worse than saying nothing.
"""

import io, os, re, sys, glob, json, hashlib

ROOT  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC   = os.path.join(ROOT, "src")
STORE = os.path.join(ROOT, "build", "prices-held.json")

P = r"\$[0-9][0-9,]*(?:\.[0-9]{2})?"          # a price
TBC = "to be confirmed"
TBC_C = "To be confirmed"


M = u"(?:&#8212;|\u2014)"                     # an em dash, either way it is written


def rx(pattern):
    return re.compile(pattern.replace("{P}", P).replace("{M}", M), re.S)


# Order matters: the specific shapes first, the loose prose last.
RULES = [
    # ── slots whose whole content is a price ────────────────────────────
    (rx(r'<span class="price__now">{P}</span>'),
     '<span class="price__now price__now--tbc">%s</span>' % TBC_C),
    (rx(r'<span class="price__was">{P}</span>'),
     '<span class="price__was">&#8212;</span>'),
    (rx(r'<p class="price__member">{P} with Institute Membership</p>'),
     '<p class="price__member">Member price to be confirmed</p>'),
    (rx(r'<span class="item__p">{P} &middot; <b>{P}</b> to a member</span>'),
     '<span class="item__p">Price to be confirmed</span>'),
    (rx(r'<span class="item__p">{P} &middot; <b>{P}</b> bought separately</span>'),
     '<span class="item__p">Price to be confirmed</span>'),
    (rx(r'<span class="edition__p">{P}</span>'),
     '<span class="edition__p">%s</span>' % TBC_C),
    (rx(r'<span class="edition__m">{P} member</span>'),
     '<span class="edition__m">Member price to be confirmed</span>'),
    (rx(r'<span class="tier__price">{P}</span>'),
     '<span class="tier__price tier__price--tbc">%s</span>' % TBC_C),
    (rx(r'<span class="contents__p">{P} separately</span>'),
     '<span class="contents__p">Price to be confirmed</span>'),
    (rx(r'<span class="offer__p">{P}</span>'),
     '<span class="offer__p">%s</span>' % TBC_C),
    (rx(r'(<td[^>]*>){P}(</td>)'), r'\1%s\2' % TBC_C),

    # ── the membership line, which repeats on 35 pages ──────────────────
    (rx(r'{P} a month brings the member price'),
     'Institute Membership brings the member price'),
    (rx(r'<span>{P} a month, and the member price on everything\.</span>'),
     '<span>Institute Membership, and the member price on everything.</span>'),
    (rx(r'Institute Membership is {P} a month and brings'),
     'Institute Membership brings'),
    (rx(r'Membership on its own is {P} a month and brings the member price on'),
     'Membership on its own brings the member price on'),

    # ── descriptive spans ───────────────────────────────────────────────
    (rx(r'<span class="belongs__d">Twelve Concepts to begin with, each at {P}\.</span>'),
     '<span class="belongs__d">Twelve Concepts to begin with, each at a price to be confirmed.</span>'),
    (rx(r'<span class="belongs__d">{P}, or {P} to a member\.</span>'),
     '<span class="belongs__d">Price to be confirmed.</span>'),
    (rx(r'<span class="belongs__d">{P} a month, with three purchase credits\.</span>'),
     '<span class="belongs__d">Three purchase credits, and the member price.</span>'),
    (rx(r'<span class="belongs__d">Three woven together from {P}, or a Concept with its Patterns from {P}\.'),
     '<span class="belongs__d">Three woven together, or a Concept with its Patterns. Prices to be confirmed.'),
    (rx(r'<span class="belongs__d">A set costs less than its parts\. The Unworthiness set is {P} against {P}\.</span>'),
     '<span class="belongs__d">A set costs less than its parts. Prices to be confirmed.</span>'),
    (rx(r'<span class="belongs__d">{P} a month\. Joining alongside Foundation Studies costs {P}\.</span>'),
     '<span class="belongs__d">Joining alongside Foundation Studies costs less than the two apart. Prices to be confirmed.</span>'),
    (rx(r'<span class="belongs__n">Foundation with Membership, {P}</span>'),
     '<span class="belongs__n">Foundation with Membership</span>'),
    (rx(r'(<span class="belongs__d">[^<]*?)\s*{P}, or {P} to a member\.</span>'),
     r'\1 Price to be confirmed.</span>'),

    # ── the Pattern list on a Concept Study ─────────────────────────────
    (rx(r'<span class="pat__d">Pattern Study &middot; {P}, or {P} to a member</span>'),
     '<span class="pat__d">Pattern Study &middot; price to be confirmed</span>'),

    # ── the offers ──────────────────────────────────────────────────────
    (rx(r'Collections start at {P}\.'), 'Collection prices are to be confirmed.'),

    # ── prose, sentence by sentence ─────────────────────────────────────
    (rx(r'Each Study is {P}, or {P} with Institute\s*\n(\s*)Membership\.'),
     r'The price of a Study is to be confirmed.'),
    (rx(r'Each Study is {P}, or {P} with Institute\s*\n(\s*)Membership, and carries'),
     'The price of a Study is to be confirmed, and each\n\\1carries'),
    (rx(r'An introductory price for the first three years, against {P}'),
     'An introductory price for the first three years, against a figure'),
    (rx(r'Six Patterns woven together is {P}, or\s*\n(\s*){P} to a member\. Three is {P}, or {P}\. A Concept with three of its connected\s*\n(\s*)Patterns is {P}, or {P}\.'),
     r'Six Patterns woven together, three woven together, and a Concept with three of\n\1its connected Patterns are each priced separately. All three prices are to be\n\1confirmed.'),
    (rx(r'A member pays <strong>{P}</strong> for the collection against {P} for the four'),
     'A member pays less for the collection than for the four'),
    (rx(r'Foundation Studies taken together with Institute Membership is {P} {M} less than the\s*\n(\s*)programme alone at {P}\.'),
     r'Foundation Studies taken together with Institute Membership costs less than the\n\1programme alone. Both prices are to be confirmed.'),
    (rx(r'{P} buys the programme and Institute Membership together {M} less than the programme'),
     'One price buys the programme and Institute Membership together &#8212; less than the programme'),
    (rx(r'Take it with membership {M} {P}'), 'Take it with membership'),
    (rx(r'whether {P} is its own product or a discount applied in the'),
     'whether the combined price is its own product or a discount applied in the'),

    # ── front matter descriptions ───────────────────────────────────────
    (rx(r'{P}, or {P} with Institute Membership\.'), 'Prices to be confirmed.'),
    (rx(r'{P}, or {P} to a member\.'), 'Prices to be confirmed.'),
    (rx(r'Institute at {P} a month, Sustaining at {P} a year, and Core Studies\.'),
     'Institute, Sustaining and Core Studies. Prices to be confirmed.'),
    (rx(r'An introductory presentation at {P} or the complete written study at {P}\.'),
     'An introductory presentation, or the complete written study. Prices to be confirmed.'),
    (rx(r'An eBook at three depths, from {P}\.'),
     'An eBook at three depths. Prices to be confirmed.'),
    (rx(r'{P}, or {P} to a member'), 'prices to be confirmed'),
    (rx(r'{P} to a member'), 'a member price to be confirmed'),
]

LEFTOVER = re.compile(P)


def unwind(text, pairs):
    """Reverse the pairs, newest first, splicing by the position each was
    applied at. Exact, where matching on the string alone is not."""
    for at, before, after in reversed(pairs):
        if text[at:at + len(after)] != after:
            raise ValueError("replacement moved")
        text = text[:at] + before + text[at + len(after):]
    return text


def sources():
    return sorted(glob.glob(os.path.join(SRC, "**", "*.html"), recursive=True))


def transform(text):
    """Apply the rules, returning the new text and the pairs that made it."""
    pairs = []
    for pattern, rep in RULES:
        while True:
            m = pattern.search(text)
            if not m:
                break
            before = m.group(0)
            after = m.expand(rep) if isinstance(rep, str) else rep(m)
            if LEFTOVER.search(after) or after == before:
                break                      # would loop, or changed nothing
            text = text[:m.start()] + after + text[m.end():]
            # the position matters: str.replace would reverse the first match,
            # not the one that was actually changed
            pairs.append([m.start(), before, after])
    return text, pairs


def hold():
    if os.path.isfile(STORE):
        sys.exit("already held - run --restore first")
    store, changed, missed = {}, 0, []
    for p in sources():
        rel = os.path.relpath(p, SRC).replace("\\", "/")
        original = io.open(p, encoding="utf-8").read()
        if not LEFTOVER.search(original):
            continue
        new, pairs = transform(original)

        # prove the round trip before writing anything
        back = unwind(new, pairs)
        if back != original:
            sys.exit("%s: the round trip does not reproduce the original" % rel)

        left = [m.group(0) for m in LEFTOVER.finditer(re.sub(r"<!--.*?-->", "", new, flags=re.S))]
        if left:
            missed.append("%s  %s" % (rel, " ".join(sorted(set(left)))))

        io.open(p, "w", encoding="utf-8", newline="\n").write(new)
        store[rel] = pairs
        changed += len(pairs)

    io.open(STORE, "w", encoding="utf-8", newline="\n").write(
        json.dumps(store, ensure_ascii=False, indent=1))
    print("held %d prices across %d pages" % (changed, len(store)))
    if missed:
        print("\nSTILL SHOWING A PRICE - a rule is missing:")
        for m in missed:
            print("   " + m)
        sys.exit(1)
    print("no price left anywhere in src/")


def restore():
    if not os.path.isfile(STORE):
        sys.exit("nothing held")
    store = json.load(io.open(STORE, encoding="utf-8"))
    n = 0
    for rel, pairs in store.items():
        p = os.path.join(SRC, rel.replace("/", os.sep))
        s = io.open(p, encoding="utf-8").read()
        try:
            s = unwind(s, pairs)
        except ValueError:
            sys.exit("%s: the page has been edited since it was held. "
                     "Restore it from git instead." % rel)
        io.open(p, "w", encoding="utf-8", newline="\n").write(s)
        n += len(pairs)
    os.remove(STORE)
    print("restored %d prices across %d pages" % (n, len(store)))


def listing():
    if not os.path.isfile(STORE):
        live = sum(len(LEFTOVER.findall(io.open(p, encoding="utf-8").read()))
                   for p in sources())
        print("Nothing held. %d prices are showing." % live)
        return
    store = json.load(io.open(STORE, encoding="utf-8"))
    print("%d prices held across %d pages.\n" % (
        sum(len(v) for v in store.values()), len(store)))
    for rel in sorted(store):
        print("  %3d  %s" % (len(store[rel]), rel))
    print("\nPut them back with: python build/prices.py --restore")


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if   arg == "--hold":    hold()
    elif arg == "--restore": restore()
    elif arg == "--list":    listing()
    else: sys.exit(__doc__)
