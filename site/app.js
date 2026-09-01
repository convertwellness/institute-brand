/* ============================================================================
   The Institute — interface behaviour

   Five things and no more:
     1. The shell switch (Cosmos / Page), remembered per browser
     2. The five doors — mega panels, hover on a fine pointer, click anywhere
     3. The mobile drawer and its accordions
     4. Section reveal, once, on first scroll into view
     5. The diagram, drawn once, from its own measured path length
   ========================================================================== */

(function () {
  "use strict";

  var root   = document.documentElement;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");

  /* ── 1. The shell ─────────────────────────────────────────────────────── */

  var STORE = "institute-shell";
  var opts  = Array.prototype.slice.call(document.querySelectorAll("[data-shell-set]"));

  function setShell(name, remember) {
    if (name === "page") root.setAttribute("data-shell", "page");
    else root.removeAttribute("data-shell");

    opts.forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.dataset.shellSet === name));
    });

    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute("content", name === "page" ? "#F3F0E7" : "#0B0E16");

    if (remember) { try { localStorage.setItem(STORE, name); } catch (e) {} }
  }

  var saved = null;
  try { saved = localStorage.getItem(STORE); } catch (e) {}
  setShell(saved === "page" ? "page" : "cosmos", false);

  opts.forEach(function (b) {
    b.addEventListener("click", function () { setShell(b.dataset.shellSet, true); });
  });

  /* ── 2. The five doors ────────────────────────────────────────────────── */

  var doors = Array.prototype.slice.call(document.querySelectorAll(".door"));
  var fine  = window.matchMedia("(hover: hover) and (pointer: fine)");
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

    // Leaving the last focusable thing in a panel closes it.
    door.addEventListener("focusout", function (e) {
      if (!door.contains(e.relatedTarget)) openDoor(door, false);
    });
  });

  document.addEventListener("click", function (e) {
    if (!e.target.closest(".door")) closeAllDoors(null);
  });

  /* ── 3. Drawer and accordions ─────────────────────────────────────────── */

  var burger = document.getElementById("burger");
  var drawer = document.getElementById("drawer");
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

  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    if (drawer.getAttribute("data-open") === "true") { setDrawer(false); return; }
    var openDoorEl = document.querySelector('.door .door__btn[aria-expanded="true"]');
    if (openDoorEl) { closeAllDoors(null); openDoorEl.focus(); }
  });

  /* ── Header hairline, once the page has moved ─────────────────────────── */

  var header = document.getElementById("header");
  var onScroll = function () {
    header.setAttribute("data-scrolled", String(window.scrollY > 8));
  };
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  /* ── 4. Section reveal — once, never on scroll back ───────────────────── */

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

  /* ── 5. The diagram draws itself once, then holds still forever ───────── */

  var chains = Array.prototype.slice.call(document.querySelectorAll(".chain"));

  chains.forEach(function (svg) {
    var line = svg.querySelector(".chain__line");
    if (line && line.getTotalLength) {
      var len = Math.ceil(line.getTotalLength());
      line.style.setProperty("--len", len);
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
