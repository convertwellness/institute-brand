/* ============================================================================
   The Institute — interface behaviour

   Five things and no more:
     1. The doors — mega panels, hover on a fine pointer, click anywhere
     2. The mobile menu
     3. The Operating System ring — hover, tab or tap a stage to read it
     4. The path — each tier opens
     5. Search — a body-text index, fetched on first open
     6. Section reveal and the ring draw, each once
   ========================================================================== */

(function () {
  "use strict";

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");
  var fine   = window.matchMedia("(hover: hover) and (pointer: fine)");

  /* ── 1. The doors ────────────────────────────────────────────────── */

  var doors = Array.prototype.slice.call(document.querySelectorAll(".door"));
  var hoverTimer = null;

  function openDoor(door, open) {
    var btn   = door.querySelector(".door__btn");
    var panel = door.querySelector(".panel");
    if (!btn || !panel) return;
    btn.setAttribute("aria-expanded", String(open));
    panel.setAttribute("data-open", String(open));
  }

  function closeAllDoors(except) {
    doors.forEach(function (d) { if (d !== except) openDoor(d, false); });
  }

  doors.forEach(function (door) {
    var btn = door.querySelector(".door__btn");

    btn.addEventListener("click", function () {
      var open = btn.getAttribute("aria-expanded") === "true";
      closeSearch();
      closeAllDoors(door);
      // On a fine pointer the panel is already open from hovering, so a click
      // that toggled it shut would leave it shut: the pointer never left, so
      // no mouseenter fires to bring it back. Escape and clicking away still
      // close it. Where there is no hover, the click has to do both jobs.
      openDoor(door, fine.matches ? true : !open);
    });

    door.addEventListener("mouseenter", function () {
      if (!fine.matches) return;
      window.clearTimeout(hoverTimer);
      closeSearch();
      closeAllDoors(door);
      openDoor(door, true);
    });

    door.addEventListener("mouseleave", function () {
      if (!fine.matches) return;
      hoverTimer = window.setTimeout(function () { openDoor(door, false); }, 260);
    });

    door.addEventListener("focusout", function (e) {
      if (!door.contains(e.relatedTarget)) openDoor(door, false);
    });
  });

  document.addEventListener("click", function (e) {
    if (!e.target.closest(".door")) closeAllDoors(null);
  });

  /* ── 2. The mobile menu ─────────────────────────────────────────── */

  var burger   = document.getElementById("burger");
  var drawer   = document.getElementById("drawer");
  var closeBtn = document.getElementById("drawer-close");

  function setDrawer(open) {
    drawer.setAttribute("data-open", String(open));
    burger.setAttribute("aria-expanded", String(open));
    document.body.style.overflow = open ? "hidden" : "";
    if (open) { var f = drawer.querySelector("a, button"); if (f) f.focus(); }
    else burger.focus();
  }

  burger.addEventListener("click", function () {
    setDrawer(drawer.getAttribute("data-open") !== "true");
  });
  closeBtn.addEventListener("click", function () { setDrawer(false); });
  drawer.addEventListener("click", function (e) {
    if (e.target.closest("a")) setDrawer(false);
  });

  /* ── 3. The ring — hover, tab or tap a stage ──────────────────────────── */

  var diagram = document.getElementById("diagram");
  var pinned  = null;

  if (diagram) {
    var nodes = Array.prototype.slice.call(diagram.querySelectorAll(".node"));
    var items = Array.prototype.slice.call(diagram.querySelectorAll(".readout__item"));
    var idle  = diagram.querySelector(".readout__idle");

    var show = function (term) {
      nodes.forEach(function (n) {
        n.classList.toggle("is-active", !!term && n.dataset.term === term);
      });
      items.forEach(function (it) { it.hidden = it.dataset.term !== term; });
      if (idle) idle.hidden = !!term;
      if (term) diagram.setAttribute("data-active", term);
      else diagram.removeAttribute("data-active");
    };

    nodes.forEach(function (n) {
      var term = n.dataset.term;

      n.addEventListener("mouseenter", function () { if (!pinned) show(term); });
      n.addEventListener("mouseleave", function () { if (!pinned) show(null); });
      n.addEventListener("focus",      function () { if (!pinned) show(term); });
      n.addEventListener("blur",       function () { if (!pinned) show(null); });

      // a tap pins the stage open, so it survives the finger lifting
      n.addEventListener("click", function () {
        pinned = pinned === term ? null : term;
        show(pinned);
      });

      n.addEventListener("keydown", function (e) {
        if (e.key !== "Enter" && e.key !== " ") return;
        e.preventDefault();
        pinned = pinned === term ? null : term;
        show(pinned || term);
      });
    });

    document.addEventListener("click", function (e) {
      if (pinned && !e.target.closest(".node")) { pinned = null; show(null); }
    });
  }

  /* ── 4. The path — each tier opens ────────────────────────────────────── */

  Array.prototype.forEach.call(document.querySelectorAll(".path__row"), function (btn) {
    btn.addEventListener("click", function () {
      var open = btn.getAttribute("aria-expanded") === "true";
      btn.setAttribute("aria-expanded", String(!open));
    });
  });

  /* ── 5. Search ─────────────────────────────────────────────────────────
     Sixty-six pages is past the point where anyone remembers which one a
     sentence was on. So the index carries the body text of every page, not
     just the titles — asking "where does it say governs?" is the whole
     point of it. It is fetched the first time search opens and never on an
     ordinary page load, so it costs a visitor who never searches nothing. */

  var sBtn   = document.getElementById("search-btn");
  var sPanel = document.getElementById("p-search");
  var sInput = document.getElementById("search-q");
  var sSaid  = document.getElementById("search-said");
  var sList  = document.getElementById("search-results");

  var KIND = {
    home: "Home", concepts: "Concepts", patterns: "Patterns", courses: "Courses",
    books: "Books", events: "Live Events", schools: "The Schools",
    collections: "Interwoven Studies", membership: "Membership",
    begin: "Begin here", about: "The Institute", michael: "The Institute",
    contact: "The Institute", account: "Your account", cart: "Cart", legal: "Legal"
  };

  function closeSearch() {
    if (!sPanel) return;
    sPanel.setAttribute("data-open", "false");
    sBtn.setAttribute("aria-expanded", "false");
  }

  if (sBtn && sPanel && sInput) {
    var pages = null, pending = null, timer = null;

    var load = function () {
      if (pending) return pending;
      // no-cache revalidates rather than refetching: correct when the content
      // has changed, nearly free when it has not.
      pending = fetch("/search-index.json", { cache: "no-cache" })
        .then(function (r) { return r.json(); })
        .then(function (j) {
          pages = j.pages.map(function (p) {
            return { u: p.u, t: p.t, d: p.d, k: p.k, x: p.x,
                     T: p.t.toLowerCase(), D: p.d.toLowerCase(),
                     H: (p.h || []).join(" ").toLowerCase(),
                     X: p.x.toLowerCase() };
          });
          return pages;
        })
        .catch(function () { pages = []; return pages; });
      return pending;
    };

    var count = function (hay, needle) {
      var n = 0, at = hay.indexOf(needle);
      while (at >= 0 && n < 12) { n += 1; at = hay.indexOf(needle, at + needle.length); }
      return n;
    };

    var score = function (p, terms, phrase) {
      var i, t, n = 0;
      // every term has to appear somewhere, or it is not a match
      for (i = 0; i < terms.length; i += 1) {
        t = terms[i];
        if (p.T.indexOf(t) < 0 && p.D.indexOf(t) < 0 &&
            p.H.indexOf(t) < 0 && p.X.indexOf(t) < 0) return 0;
      }
      // a page whose name *begins* with what you typed is likelier to be the
      // one you meant than one that merely contains it somewhere
      if (p.T.toLowerCase().indexOf(phrase) === 0) n += 70;
      if (p.T.indexOf(phrase) >= 0) n += 140;
      if (p.D.indexOf(phrase) >= 0) n += 40;
      if (p.H.indexOf(phrase) >= 0) n += 30;
      if (p.X.indexOf(phrase) >= 0) n += 16;
      for (i = 0; i < terms.length; i += 1) {
        t = terms[i];
        if (p.T.indexOf(t) >= 0) n += 28;
        if (p.D.indexOf(t) >= 0) n += 8;
        if (p.H.indexOf(t) >= 0) n += 6;
        n += count(p.X, t) * 2;
      }
      return n;
    };

    /* Built as nodes rather than innerHTML — the snippet is page text and the
       query is the visitor's, and neither should ever be parsed as markup. */
    var snippet = function (text, low, needle) {
      var frag = document.createDocumentFragment();
      var at = needle ? low.indexOf(needle) : -1;
      if (at < 0) {
        frag.appendChild(document.createTextNode(text.slice(0, 150) + "\u2026"));
        return frag;
      }
      var from = Math.max(0, at - 78), to = Math.min(text.length, at + needle.length + 96);
      if (from > 0) { from = text.indexOf(" ", from) + 1 || from; }
      frag.appendChild(document.createTextNode((from > 0 ? "\u2026" : "") + text.slice(from, at)));
      var m = document.createElement("mark");
      m.textContent = text.slice(at, at + needle.length);
      frag.appendChild(m);
      frag.appendChild(document.createTextNode(
        text.slice(at + needle.length, to) + (to < text.length ? "\u2026" : "")));
      return frag;
    };

    var render = function (hits, phrase, total) {
      sList.textContent = "";
      hits.forEach(function (h) {
        var li = document.createElement("li");
        var a  = document.createElement("a");
        a.className = "sres";
        a.href = h.p.u;

        var k = document.createElement("span");
        k.className = "sres__k";
        k.textContent = KIND[h.p.k] || "The Institute";

        var t = document.createElement("span");
        t.className = "sres__t";
        t.textContent = h.p.t;

        var sn = document.createElement("span");
        sn.className = "sres__s";
        sn.appendChild(snippet(h.p.x, h.p.X, h.needle));

        a.appendChild(k); a.appendChild(t); a.appendChild(sn);
        li.appendChild(a); sList.appendChild(li);
      });
      sSaid.textContent = total === 0
        ? "Nothing found."
        : (total === 1 ? "1 page" : total + " pages") +
          (total > hits.length ? ", showing the closest " + hits.length + "." : ".");
    };

    var run = function () {
      var q = sInput.value.trim();
      if (q.length < 2) { sList.textContent = ""; sSaid.textContent = ""; return; }
      if (!pages) { sSaid.textContent = "Searching\u2026"; load().then(run); return; }

      var phrase = q.toLowerCase();
      var terms  = phrase.split(/\s+/).filter(function (t) { return t.length > 1; });
      if (!terms.length) terms = [phrase];

      var hits = [];
      pages.forEach(function (p) {
        var n = score(p, terms, phrase);
        if (!n) return;
        var needle = p.X.indexOf(phrase) >= 0 ? phrase : null;
        if (!needle) {
          terms.forEach(function (t) {
            if (!needle && p.X.indexOf(t) >= 0) needle = t;
          });
        }
        hits.push({ p: p, n: n, needle: needle });
      });
      hits.sort(function (a, b) { return b.n - a.n; });
      render(hits.slice(0, 12), phrase, hits.length);
    };

    var setSearch = function (open) {
      sPanel.setAttribute("data-open", String(open));
      sBtn.setAttribute("aria-expanded", String(open));
      if (open) {
        closeAllDoors(null);
        load();
        sInput.focus();
        sInput.select();
      } else {
        sBtn.focus();
      }
    };

    sBtn.addEventListener("click", function () {
      setSearch(sPanel.getAttribute("data-open") !== "true");
    });

    sInput.addEventListener("input", function () {
      window.clearTimeout(timer);
      timer = window.setTimeout(run, 120);
    });

    // down from the field walks into the results; up from the first comes back
    sPanel.addEventListener("keydown", function (e) {
      if (e.key !== "ArrowDown" && e.key !== "ArrowUp") return;
      var links = Array.prototype.slice.call(sList.querySelectorAll("a"));
      if (!links.length) return;
      e.preventDefault();
      var i = links.indexOf(document.activeElement);
      if (e.key === "ArrowDown") {
        links[i < 0 ? 0 : Math.min(i + 1, links.length - 1)].focus();
      } else if (i <= 0) {
        sInput.focus();
      } else {
        links[i - 1].focus();
      }
    });

    document.addEventListener("click", function (e) {
      if (sPanel.getAttribute("data-open") !== "true") return;
      if (e.target.closest("#p-search") || e.target.closest("#search-btn")) return;
      closeSearch();
    });
  }

  /* ── The site outline's work layer ────────────────────────────────────
     Off by default, because the outline itself is useful to anyone. On, it
     shows what is still to be written. /sitemap#work opens straight into
     it, so the link can be sent as one or the other. */

  var outline = document.getElementById("outline");
  var workBtn = document.getElementById("work-toggle");

  if (outline && workBtn) {
    var setWork = function (on) {
      outline.setAttribute("data-work", String(on));
      workBtn.setAttribute("aria-expanded", String(on));
      if (history.replaceState) {
        history.replaceState(null, "", on ? "#work" : location.pathname);
      }
    };
    setWork(location.hash === "#work");
    workBtn.addEventListener("click", function () {
      setWork(outline.getAttribute("data-work") !== "true");
    });
  }

  /* A link to the site outline, kept in the corner of every page for whoever
     is reviewing. Off for everyone else, and remembered per browser — the
     switch is on the outline itself. localStorage throws in a private window
     and comes back empty when site data is cleared, so every touch of it is
     wrapped and the page is correct without it. */

  var PIN_KEY = "institute:outline-pin";
  var pin     = document.getElementById("outline-pin");
  var pinBtn  = document.getElementById("pin-toggle");

  var pinned = function () {
    try { return window.localStorage.getItem(PIN_KEY) === "1"; }
    catch (e) { return false; }
  };
  var setPinned = function (on) {
    try {
      if (on) window.localStorage.setItem(PIN_KEY, "1");
      else window.localStorage.removeItem(PIN_KEY);
    } catch (e) {}
    if (pin) pin.hidden = !on;
    if (pinBtn) pinBtn.setAttribute("aria-pressed", String(on));
  };

  if (pin || pinBtn) setPinned(pinned());
  // never in its own corner
  if (pin && location.pathname.indexOf("/sitemap") === 0) pin.hidden = true;

  if (pinBtn) {
    pinBtn.addEventListener("click", function () {
      setPinned(pinBtn.getAttribute("aria-pressed") !== "true");
    });
  }

  /* ── Escape closes whatever is open ───────────────────────────────────── */

  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    if (sPanel && sPanel.getAttribute("data-open") === "true") {
      closeSearch(); sBtn.focus(); return;
    }
    if (drawer.getAttribute("data-open") === "true") { setDrawer(false); return; }
    if (pinned) { pinned = null; if (diagram) diagram.removeAttribute("data-active"); }
    var openBtn = document.querySelector('.door .door__btn[aria-expanded="true"]');
    if (openBtn) { closeAllDoors(null); openBtn.focus(); }
  });

  /* ── The header hairline, once the page has moved ─────────────────────── */

  /* Two thresholds, not one. The masthead is sticky, so it occupies space in
     normal flow, and compacting takes 28px out of the document -- the page
     rises by 28px under the pointer. Against a single 8px threshold that
     shift can carry scrollY back under the line, which expands the masthead,
     which pushes the page down again, which compacts it: the lockup flickering
     between its two states. 28 cannot cross a 70px gap. */
  var header = document.getElementById("header");
  var COMPACT_AT = 110, EXPAND_AT = 40;
  var compact = null;

  var onScroll = function () {
    var y = window.scrollY || 0;
    var next = compact ? y > EXPAND_AT : y > COMPACT_AT;
    if (next === compact) return;
    compact = next;
    header.setAttribute("data-scrolled", String(compact));
  };
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  /* ── 5. Reveal, and the ring draw — each once ─────────────────────────── */

  var revealables = Array.prototype.slice.call(document.querySelectorAll("[data-reveal]"));

  if (reduce.matches || !("IntersectionObserver" in window)) {
    revealables.forEach(function (el) { el.classList.add("is-in"); });
  } else {
    var seen = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-in");
        obs.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -12% 0px", threshold: 0.05 });
    revealables.forEach(function (el) { seen.observe(el); });
  }

  // the hero trace measures its own length, like the ring does
  var trace = document.querySelector(".trace__line");
  if (trace && trace.getTotalLength) {
    trace.style.setProperty("--len", Math.ceil(trace.getTotalLength()));
  }

  var chains = Array.prototype.slice.call(document.querySelectorAll(".chain"));

  chains.forEach(function (svg) {
    var line = svg.querySelector(".chain__line");
    if (line && line.getTotalLength) {
      line.style.setProperty("--len", Math.ceil(line.getTotalLength()));
    }
  });

  if (reduce.matches || !("IntersectionObserver" in window)) {
    chains.forEach(function (svg) { svg.classList.add("is-drawn"); });
  } else {
    var drawn = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-drawn");
        obs.unobserve(entry.target);
      });
    }, { threshold: 0.25 });
    chains.forEach(function (svg) { drawn.observe(svg); });
  }

  /* ── Index filters ────────────────────────────────────────────────────
     Any index with #grid and [data-filter] buttons gets this — Concepts and
     Patterns today, the rest of the library as Michael's mapping arrives. A
     card marked data-fam="all" survives every filter; that is the placeholder
     card, which belongs to no Family because it has no name yet.

     The count is spoken as well as shown: without it a filter that empties a
     grid reads as a broken page to anyone not watching the cards. */

  var grid = document.getElementById("grid");
  if (grid) {
    var items   = Array.prototype.slice.call(grid.querySelectorAll(".item"));
    var fbtns   = Array.prototype.slice.call(document.querySelectorAll("[data-filter]"));
    var readout = document.getElementById("filter-said");

    /* A placeholder card stands for something not yet named, so it is not one
       of the Studies and is left out of both counts. It appears unfiltered
       only, since it belongs to no Family until it has a name. */
    var real = items.filter(function (it) {
      return !it.classList.contains("item--awaited");
    });

    var applyFilter = function (f, label) {
      var shown = 0;
      items.forEach(function (it) {
        var keep = f === "all" || it.dataset.fam === f || it.dataset.fam === "all";
        it.hidden = !keep;
        if (keep && !it.classList.contains("item--awaited")) shown += 1;
      });
      if (readout) {
        readout.textContent = f === "all"
          ? "Showing all " + shown + "."
          : "Showing " + shown + " of " + real.length + " — " + label + ".";
      }
    };

    fbtns.forEach(function (b) {
      b.addEventListener("click", function () {
        fbtns.forEach(function (o) { o.setAttribute("aria-pressed", String(o === b)); });
        applyFilter(b.dataset.filter, (b.dataset.label || b.textContent).trim());
      });
    });
  }

  /* ── Small change ─────────────────────────────────────────────────────── */

  var year = document.getElementById("year");
  if (year) year.textContent = String(new Date().getFullYear());

  var news = document.getElementById("news");
  if (news) {
    news.addEventListener("submit", function (e) {
      e.preventDefault();
      var said = document.getElementById("news-said");
      if (said) said.hidden = false;
      news.reset();
    });
  }
})();
