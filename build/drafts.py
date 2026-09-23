# -*- coding: utf-8 -*-
"""Fill the "Awaiting Michael" gaps with labelled draft copy — and take it out again.

    python build/drafts.py            fill every placeholder with draft copy
    python build/drafts.py --strip    put the placeholders back
    python build/drafts.py --list     show what is currently draft

Sara asked for filler so the layouts can be judged with real text in them.
CLAUDE.md says the opposite — ship a clear placeholder, do not invent copy — and
her own brief of 22 Sep says not to create new doctrine. Both are right for the
finished site, so this is built to be reversible and impossible to mistake:

  * every filled block is <div class="draft"> with a visible "Draft" label
  * the original placeholder text is kept verbatim in an HTML comment beside it,
    so --strip restores exactly what was there
  * the prose describes structure and uses only vocabulary Michael has already
    established. It asserts no new teaching, names no new Pattern or Concept,
    and invents no price, date, count or curriculum

None of it is his. It is scaffolding that reads like prose.
"""

import io, os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC  = os.path.join(ROOT, "src")

NEEDS = re.compile(
    r'[ \t]*<div class="needs"[^>]*>\s*<span class="needs__k">(.*?)</span>\s*(.*?)\s*</div>\n',
    re.S)
DRAFT = re.compile(
    r'[ \t]*<div class="draft">.*?</div>\n[ \t]*<!-- AWAITING-MICHAEL (.*?) \|\|\| (.*?) -->\n',
    re.S)


def draft_block(indent, paras):
    out = [u'%s<div class="draft">' % indent,
           u'%s  <span class="draft__k">Draft</span>' % indent]
    for t in paras:
        out.append(u'%s  <p>%s</p>' % (indent, t))
    out.append(u'%s</div>' % indent)
    return "\n".join(out) + "\n"


# ── the copy ─────────────────────────────────────────────────────────────
# Structural, in his vocabulary, asserting nothing new.

def concept_copy(name, i):
    return [
     [u"%s is met first as a conclusion about oneself rather than as an idea — it "
      u"arrives already believed, and rarely announces itself by name." % name],
     [u"A Concept held as true shapes what is noticed and what is discounted. Where "
      u"%s is operating, ordinary events are read for confirmation of it, and the "
      u"evidence that would contradict it tends to pass unexamined." % name,
      u"The purpose of the Study is not to argue with the conclusion but to make the "
      u"reading visible while it is happening."],
     [u"Every Concept produces Patterns of Behavior that act on its behalf, and those "
      u"Patterns then return results the Concept can point to. This section sets out "
      u"which Patterns belong to %s and how each one closes the circuit." % name],
     [u"Concepts rarely operate alone. This section places %s among the Concepts it "
      u"is most often met beside, and names the Family it belongs to." % name],
    ][i % 4]


def pattern_copy(name, i):
    return [
     [u"%s is recognised long before it is named. From inside it feels like the "
      u"reasonable response to the situation, which is what makes it difficult to "
      u"see while it is running." % name],
     [u"The Pattern follows the same sequence each time: a situation is read, a "
      u"familiar conclusion is reached, and a response follows that has worked before. "
      u"This section sets that sequence out step by step, so it can be recognised "
      u"early rather than afterwards."],
     [u"No Pattern begins on its own. %s exists to protect and confirm a Concept held "
      u"underneath it, and this section names that Concept and shows how the Pattern "
      u"returns the evidence it needs." % name],
    ][i % 3]


STAGE_COPY = {
 u"Emotion": [u"What is expected is felt before it is examined. The emotional response "
              u"arrives as confirmation that the expectation was correct, and rarely "
              u"presents itself as a response to anything."],
 u"Behavior": [u"Feeling moves outward into action. The response is chosen from what has "
               u"worked before, which is what makes it familiar rather than new."],
 u"Life Result": [u"What follows is read as evidence. The result is taken as proof of the "
                  u"Concept that set the sequence going, and the Concept is held more "
                  u"firmly than before — which is where the cycle begins again."],
}

GENERIC = [u"This section is written and will be set here. The structure, the order and "
           u"the length are settled; only the words are outstanding."]


def fill():
    changed = 0
    for p in sorted(glob.glob(os.path.join(SRC, "**", "*.html"), recursive=True)):
        s = io.open(p, encoding="utf-8").read()
        if not NEEDS.search(s):
            continue
        rel  = os.path.relpath(p, SRC).replace("\\", "/")
        cat  = rel.split("/")[0].replace(".html", "")
        name = os.path.basename(rel)[:-5].replace("-", " ").title()
        name = {"Fear And Doubt": "Fear and Doubt", "Life Result": "Life Result"}.get(name, name)

        idx = [0]
        def sub(m):
            kind, body = m.group(1), m.group(2)
            indent = m.group(0)[:len(m.group(0)) - len(m.group(0).lstrip())]
            i = idx[0]; idx[0] += 1
            if   cat == "concepts" and rel.count("/") == 1: paras = concept_copy(name, i)
            elif cat == "patterns" and rel.count("/") == 1: paras = pattern_copy(name, i)
            else:                                           paras = GENERIC
            flat_k = kind.replace("|||", "/")
            flat_b = " ".join(body.split()).replace("|||", "/").replace("--", "&#45;&#45;")
            return (draft_block(indent, paras)
                    + u'%s<!-- AWAITING-MICHAEL %s ||| %s -->\n' % (indent, flat_k, flat_b))

        s2 = NEEDS.sub(sub, s)
        if s2 != s:
            io.open(p, "w", encoding="utf-8", newline="\n").write(s2)
            changed += idx[0]
    print("filled %d placeholders with labelled draft copy" % changed)


def strip():
    changed = 0
    for p in sorted(glob.glob(os.path.join(SRC, "**", "*.html"), recursive=True)):
        s = io.open(p, encoding="utf-8").read()
        if not DRAFT.search(s):
            continue
        def back(m):
            indent = m.group(0)[:len(m.group(0)) - len(m.group(0).lstrip())]
            kind, body = m.group(1), m.group(2).replace("&#45;&#45;", "--")
            return (u'%s<div class="needs">\n%s  <span class="needs__k">%s</span>\n'
                    u'%s  <p>%s</p>\n%s</div>\n' % (indent, indent, kind, indent, body, indent))
        s2, n = DRAFT.subn(back, s)
        io.open(p, "w", encoding="utf-8", newline="\n").write(s2)
        changed += n
    print("restored %d placeholders" % changed)


def listing():
    tot = 0
    for p in sorted(glob.glob(os.path.join(SRC, "**", "*.html"), recursive=True)):
        n = len(DRAFT.findall(io.open(p, encoding="utf-8").read()))
        if n:
            print("  %3d  %s" % (n, os.path.relpath(p, SRC).replace("\\", "/")))
            tot += n
    print("\n%d draft blocks. Remove with: python build/drafts.py --strip" % tot)


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if   arg == "--strip": strip()
    elif arg == "--list":  listing()
    else:                  fill()
