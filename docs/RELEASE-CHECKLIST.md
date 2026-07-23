# Portfolio Release Checklist

## 1. Content and privacy

- [x] Canonical professional source matches the site and both CVs.
- [x] LemmikkiLife remains the first selected project.
- [x] Private products do not expose private repositories or unsupported claims.
- [x] No street address, personal telephone number or personal Gmail is public.
- [x] Personal and ZyInnova GitHub/LinkedIn links are clearly distinguished.

## 2. Automated checks

- [x] `scripts/audit_stage_d.py` passes.
- [x] `scripts/audit_stage_e.py` passes.
- [x] `scripts/audit_stage_fgh.py` passes.
- [x] `scripts/audit_cv_pair.py` passes.
- [x] `node --check assets/js/main.js` passes.
- [x] `git diff --check` passes.

## 3. Browser checks

- [x] Mobile navigation opens with Enter/Space and reports `aria-expanded`.
- [x] Focus enters the opened menu, remains inside it and returns to the toggle.
- [x] Escape closes the menu.
- [x] Skip link becomes visible and moves focus to main content.
- [x] Reduced-motion mode shows static hero text and no entrance animation.
- [x] 375 px, 768 px and 1440 px widths have no horizontal overflow.
- [x] All four project cards, external links and both CV downloads work.
- [x] Browser console has no site-owned errors.

## 4. SEO, files and headers

- [x] Title, description, canonical, Open Graph, Twitter and JSON-LD agree.
- [x] `og-cover-2026.jpg` is 1200 × 630 and below 200 KB.
- [x] `robots.txt` references the canonical sitemap.
- [x] Sitemap `lastmod` matches the release date.
- [x] HTTPS, CSP, HSTS, nosniff, frame, referrer and permissions headers exist.
- [x] HTML is not long-term cached; versioned static assets are cached.

## 5. GitHub surfaces

- [x] Profile README uses the canonical title and selected projects.
- [x] Todo README describes only verified scope.
- [x] Movie Explorer README describes its collaborative prototype scope and has
      no personal Gmail.
- [x] Old GitHub Pages no longer serves personal information.
- [x] Old archived repository is private or its public history has been
      sanitized.
- [x] Old repository is not pinned.

## 6. Production

- [x] Commit and push the reviewed source.
- [x] Upload the public site package to Hostinger `public_html/portfolio`.
- [x] Purge or bypass stale caches.
- [x] Re-run the browser and HTTP checks against
      `https://portfolio.zyinnova.com/`.
- [x] Record the commit, deployment date and live verification result in the
      Stage F–H quality record.

Rollback: keep the previous Hostinger file set or backup archive until live
verification passes.
