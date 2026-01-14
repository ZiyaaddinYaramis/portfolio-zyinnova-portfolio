(function () {
  "use strict";

  /* =========================
     Helper functions
  ========================= */
  const select = (el, all = false) => {
    el = el.trim();
    return all
      ? [...document.querySelectorAll(el)]
      : document.querySelector(el);
  };

  const on = (type, el, listener, all = false) => {
    const elements = select(el, all);
    if (!elements) return;
    if (all) elements.forEach((e) => e.addEventListener(type, listener));
    else elements.addEventListener(type, listener);
  };

  const onscroll = (el, listener) => {
    el.addEventListener("scroll", listener);
  };

  /* =========================
     Navbar active state (Safari-safe + footer-safe)
  ========================= */
  const navbarlinks = select("#navbar .scrollto", true);

  const setActiveLinkById = (id) => {
    navbarlinks.forEach((link) => {
      const hash = link.hash || link.getAttribute("href");
      link.classList.toggle("active", hash === `#${id}`);
    });
  };

  const navbarlinksActive = () => {
    const doc = document.documentElement;

    // Safari-safe scroll metrics
    const scrollTop = window.pageYOffset || doc.scrollTop || 0;
    const viewportH = window.innerHeight || doc.clientHeight || 0;
    const scrollH = doc.scrollHeight || 0;

    // If near page bottom -> force Contact active
    // Small buffer helps Safari rounding
    const nearBottom = scrollTop + viewportH >= scrollH - 8;
    if (nearBottom) {
      setActiveLinkById("contact");
      return;
    }

    // Normal activation by section bounds
    const position = scrollTop + 200;

    let currentId = null;

    navbarlinks.forEach((link) => {
      if (!link.hash) return;
      const section = select(link.hash);
      if (!section) return;

      const top = section.offsetTop;
      const bottom = top + section.offsetHeight;

      if (position >= top && position <= bottom) {
        currentId = section.getAttribute("id");
      }
    });

    if (currentId) setActiveLinkById(currentId);
  };

  window.addEventListener("load", navbarlinksActive);
  window.addEventListener("scroll", navbarlinksActive, { passive: true });
  window.addEventListener("resize", navbarlinksActive);

  // Keep legacy scroll binding too (harmless, sometimes helpful)
  onscroll(document, navbarlinksActive);

  /* =========================
     Smooth scroll
  ========================= */
  const scrollto = (el) => {
    const elementPos = select(el).offsetTop;
    window.scrollTo({
      top: elementPos,
      behavior: "smooth",
    });
  };

  on(
    "click",
    ".scrollto",
    function (e) {
      if (!select(this.hash)) return;
      e.preventDefault();

      const body = select("body");
      if (body.classList.contains("mobile-nav-active")) {
        body.classList.remove("mobile-nav-active");
        const toggle = select(".mobile-nav-toggle");
        toggle.classList.toggle("bi-list");
        toggle.classList.toggle("bi-x");
      }

      scrollto(this.hash);
    },
    true
  );

  /* =========================
     Mobile navigation
  ========================= */
  on("click", ".mobile-nav-toggle", function () {
    select("body").classList.toggle("mobile-nav-active");
    this.classList.toggle("bi-list");
    this.classList.toggle("bi-x");
  });

  /* =========================
     Back to top
  ========================= */
  const backtotop = select(".back-to-top");
  if (backtotop) {
    const toggleBacktotop = () => {
      backtotop.classList.toggle("active", window.scrollY > 100);
    };
    window.addEventListener("load", toggleBacktotop);
    window.addEventListener("scroll", toggleBacktotop, { passive: true });
    onscroll(document, toggleBacktotop);
  }

  /* =========================
     Preloader
  ========================= */
  const preloader = select("#preloader");
  if (preloader) {
    window.addEventListener("load", () => {
      preloader.remove();
    });
  }

  /* =========================
     Hero typed effect
  ========================= */
  const typed = select(".typed");
  if (typed && typeof Typed !== "undefined") {
    const strings = typed
      .getAttribute("data-typed-items")
      .split(",")
      .map((s) => s.trim());

    new Typed(".typed", {
      strings,
      loop: true,
      typeSpeed: 90,
      backSpeed: 45,
      backDelay: 1800,
    });
  }

  /* =========================
     AOS init
  ========================= */
  window.addEventListener("load", () => {
    if (typeof AOS === "undefined") return;
    AOS.init({
      duration: 900,
      easing: "ease-out-cubic",
      once: true,
      mirror: false,
    });
  });

  // Footer year
  const yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();
})();
