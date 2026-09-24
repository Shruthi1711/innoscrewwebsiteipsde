/* INNO-SCREW — shared site behaviour: language toggle, theme, mobile nav */
(function () {
  "use strict";

  var SVG_MOON = '<svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
  var SVG_SUN = '<svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>';

  function store(key, val) {
    try {
      if (val === undefined) return localStorage.getItem(key);
      localStorage.setItem(key, val);
    } catch (e) { /* storage unavailable — fall back to defaults */ }
    return null;
  }

  var LANG = store("lang") || "de";
  var THEME = store("theme") || "light";

  function applyTheme(t) {
    THEME = t;
    document.documentElement.setAttribute("data-theme", t);
    var b = document.getElementById("bthm");
    if (b) b.innerHTML = (t === "dark") ? SVG_SUN : SVG_MOON;
    store("theme", t);
  }

  function applyLang(l) {
    LANG = l;
    document.querySelectorAll("[data-de]").forEach(function (el) {
      if (el.children.length === 0) {
        el.textContent = (l === "de") ? el.getAttribute("data-de") : el.getAttribute("data-en");
      }
    });
    document.querySelectorAll(".de-block").forEach(function (el) {
      el.style.display = (l === "de") ? "" : "none";
    });
    document.querySelectorAll(".en-block").forEach(function (el) {
      el.style.display = (l === "en") ? "" : "none";
    });
    var b = document.getElementById("blng");
    if (b) b.textContent = (l === "de") ? "EN" : "DE";
    document.documentElement.lang = l;
    store("lang", l);
  }

  document.addEventListener("DOMContentLoaded", function () {
    try {
      applyTheme(THEME);
      applyLang(LANG);

      var bt = document.getElementById("bthm");
      if (bt) {
        bt.addEventListener("click", function () {
          applyTheme(THEME === "dark" ? "light" : "dark");
        });
      }

      var bl = document.getElementById("blng");
      if (bl) {
        bl.addEventListener("click", function () {
          applyLang(LANG === "de" ? "en" : "de");
        });
      }

      var ham = document.getElementById("ham");
      var nl = document.getElementById("nl");
      if (ham && nl) {
        ham.addEventListener("click", function () {
          nl.classList.toggle("open");
        });
      }

      /* Mark the current page in the main navigation */
      var page = location.pathname.split("/").pop() || "index.html";
      document.querySelectorAll(".nl a").forEach(function (a) {
        if (a.getAttribute("href") === page) {
          a.classList.add("active");
        } else {
          a.classList.remove("active");
        }
      });

      /* News category filter (news.html only) */
      var fbtns = document.querySelectorAll(".nfbtn");
      if (fbtns.length) {
        fbtns.forEach(function (btn) {
          btn.addEventListener("click", function () {
            var cat = btn.getAttribute("data-cat");
            fbtns.forEach(function (b) { 
              b.classList.remove("on"); 
            });
            btn.classList.add("on");
            document.querySelectorAll(".nentry").forEach(function (e) {
              var match = (cat === "all" || e.getAttribute("data-cat") === cat);
              e.classList.toggle("hide", !match);
            });
          });
        });
      }
    } catch (error) {
      console.error("Error during page initialization:", error);
    }
  });

  /* Tab switching on the research-infrastructure page */
  window.switchSystem = function (e, id) {
    if (e) e.preventDefault();
    document.querySelectorAll(".station-panel").forEach(function (p) {
      p.classList.remove("active");
    });
    var target = document.getElementById("panel-" + id);
    if (target) target.classList.add("active");
    document.querySelectorAll(".stnav a").forEach(function (a) {
      a.classList.remove("active");
    });
    var tab = document.querySelector('.stnav a[data-panel="' + id + '"]');
    if (tab) tab.classList.add("active");
    if (history.replaceState) history.replaceState(null, "", "#" + id);
    var stnav = document.getElementById("stnav");
    if (stnav && e) window.scrollTo({ top: stnav.offsetTop - 70, behavior: "smooth" });
  };

  document.addEventListener("DOMContentLoaded", function () {
    var hash = location.hash.replace("#", "");
    if (hash && document.getElementById("panel-" + hash)) window.switchSystem(null, hash);
  });
})();
