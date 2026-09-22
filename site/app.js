/* ============================================================================
   The Institute — interface behaviour

   Five things and no more:
     1. The five doors — mega panels, hover on a fine pointer, click anywhere
     2. The mobile drawer and its accordions
     3. The Operating System ring — hover, tab or tap a stage to read it
     4. The path — each tier opens
     5. Section reveal and the ring draw, each once
   ========================================================================== */

(function () {
  "use strict";

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");
  var fine   = window.matchMedia("(hover: hover) and (pointer: fine)");

  /* ── 1. The five doors ────────────────────────────────────────────────── */

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
      closeAllDoors(door);
      openDoor(door, !open);
    });

    door.addEventListener("mouseenter", function () {
      if (!fine.matches) return;
      window.clearTimeout(hoverTimer);
      closeAllDoors(door);
      openDoor(door, true);
    });

    door.addEventListener("mouseleave", function () {
      if (!fine.matches) return;
      hoverTimer = window.setTimeout(function () { openDoor(door, false); }, 140);
    });

    door.addEventListener("focusout", function (e) {
      if (!door.contains(e.relatedTarget)) openDoor(door, false);
    });
  });

  document.addEventListener("click", function (e) {
    if (!e.target.closest(".door")) closeAllDoors(null);
  });

  /* ── 2. Drawer and accordions ─────────────────────────────────────────── */

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

  Array.prototype.forEach.call(document.querySelectorAll(".acc__btn"), function (btn) {
    btn.addEventListener("click", function () {
      var panel = document.getElementById(btn.getAttribute("aria-controls"));
      var open  = btn.getAttribute("aria-expanded") === "true";
      btn.setAttribute("aria-expanded", String(!open));
      panel.setAttribute("data-open", String(!open));
    });
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

  /* ── Escape closes whatever is open ───────────────────────────────────── */

  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    if (drawer.getAttribute("data-open") === "true") { setDrawer(false); return; }
    if (pinned) { pinned = null; if (diagram) diagram.removeAttribute("data-active"); }
    var openBtn = document.querySelector('.door .door__btn[aria-expanded="true"]');
    if (openBtn) { closeAllDoors(null); openBtn.focus(); }
  });

  /* ── The header hairline, once the page has moved ─────────────────────── */

  var header = document.getElementById("header");
  var onScroll = function () {
    header.setAttribute("data-scrolled", String(window.scrollY > 8));
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
