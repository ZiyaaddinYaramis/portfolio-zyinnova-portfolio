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

  const reduceMotion = window.matchMedia(
    "(prefers-reduced-motion: reduce)"
  ).matches;

  /* =========================
     Navbar active state (Safari-safe + footer-safe)
  ========================= */
  const navbarlinks = select("#navbar .scrollto", true);

  const setActiveLinkById = (id) => {
    navbarlinks.forEach((link) => {
      const hash = link.hash || link.getAttribute("href");
      const isActive = hash === `#${id}`;
      link.classList.toggle("active", isActive);
      if (isActive) link.setAttribute("aria-current", "page");
      else link.removeAttribute("aria-current");
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
    const target = select(el);
    if (!target) return;
    const elementPos = target.offsetTop;
    window.scrollTo({
      top: elementPos,
      behavior: reduceMotion ? "auto" : "smooth",
    });
  };

  const mobileToggle = select(".mobile-nav-toggle");
  const mobileToggleIcon = mobileToggle
    ? mobileToggle.querySelector("i")
    : null;
  const header = select("#header");
  const mobileMedia = window.matchMedia("(max-width: 991px)");

  const setMobileNavigation = (open, restoreFocus = false) => {
    if (!mobileToggle || !header) return;

    document.body.classList.toggle("mobile-nav-active", open);
    mobileToggle.setAttribute("aria-expanded", String(open));
    mobileToggle.setAttribute(
      "aria-label",
      open ? "Close navigation" : "Open navigation"
    );
    mobileToggleIcon?.classList.toggle("bi-list", !open);
    mobileToggleIcon?.classList.toggle("bi-x", open);

    if (mobileMedia.matches) {
      header.toggleAttribute("inert", !open);
      header.setAttribute("aria-hidden", String(!open));
    } else {
      header.removeAttribute("inert");
      header.removeAttribute("aria-hidden");
    }

    if (open) {
      navbarlinks[0]?.focus();
    } else if (restoreFocus) {
      mobileToggle.focus();
    }
  };

  const syncMobileNavigation = () => {
    if (!mobileMedia.matches) {
      setMobileNavigation(false);
      return;
    }
    const isOpen = document.body.classList.contains("mobile-nav-active");
    setMobileNavigation(isOpen);
  };

  on(
    "click",
    ".scrollto",
    function (e) {
      if (!select(this.hash)) return;
      e.preventDefault();

      const body = select("body");
      if (body.classList.contains("mobile-nav-active")) {
        setMobileNavigation(false, true);
      }

      scrollto(this.hash);
    },
    true
  );

  /* =========================
     Mobile navigation
  ========================= */
  on("click", ".mobile-nav-toggle", () => {
    const open = !document.body.classList.contains("mobile-nav-active");
    setMobileNavigation(open, !open);
  });

  document.addEventListener("keydown", (event) => {
    if (!document.body.classList.contains("mobile-nav-active")) return;

    if (event.key === "Escape") {
      event.preventDefault();
      setMobileNavigation(false, true);
      return;
    }

    if (event.key !== "Tab") return;
    const focusable = [mobileToggle, ...navbarlinks].filter(Boolean);
    const first = focusable[0];
    const last = focusable[focusable.length - 1];

    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last?.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first?.focus();
    }
  });

  document.addEventListener("click", (event) => {
    if (!document.body.classList.contains("mobile-nav-active")) return;
    if (header?.contains(event.target) || mobileToggle?.contains(event.target))
      return;
    setMobileNavigation(false, true);
  });

  mobileMedia.addEventListener("change", syncMobileNavigation);
  syncMobileNavigation();

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
  if (typed) {
    const strings = typed
      .getAttribute("data-typed-items")
      .split(",")
      .map((s) => s.trim());

    if (reduceMotion || typeof Typed === "undefined") {
      typed.textContent = strings[0];
    } else {
      new Typed(".typed", {
        strings,
        loop: true,
        typeSpeed: 55,
        backSpeed: 70,
        backDelay: 650,
      });
    }
  }

  /* =========================
     AOS init
  ========================= */
  window.addEventListener("load", () => {
    if (typeof AOS === "undefined") return;
    AOS.init({
      disable: reduceMotion,
      duration: 700,
      easing: "ease-out-cubic",
      once: true,
      mirror: false,
    });
  });

  // Footer year
  const yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();
})();
