# Portfolio Release Checklist

## 1. Content and privacy

- [ ] Canonical professional source matches the site and both CVs.
- [ ] LemmikkiLife remains the first selected project.
- [ ] Private products do not expose private repositories or unsupported claims.
- [ ] No street address, personal telephone number or personal Gmail is public.
- [ ] Personal and ZyInnova GitHub/LinkedIn links are clearly distinguished.

## 2. Automated checks

- [ ] `scripts/audit_stage_d.py` passes.
- [ ] `scripts/audit_stage_e.py` passes.
- [ ] `scripts/audit_stage_fgh.py` passes.
- [ ] `scripts/audit_cv_pair.py` passes.
- [ ] `node --check assets/js/main.js` passes.
- [ ] `git diff --check` passes.

## 3. Browser checks

- [ ] Mobile navigation opens with Enter/Space and reports `aria-expanded`.
- [ ] Focus enters the opened menu, remains inside it and returns to the toggle.
- [ ] Escape closes the menu.
- [ ] Skip link becomes visible and moves focus to main content.
- [ ] Reduced-motion mode shows static hero text and no entrance animation.
- [ ] 375 px, 768 px and 1440 px widths have no horizontal overflow.
- [ ] All four project cards, external links and both CV downloads work.
- [ ] Browser console has no site-owned errors.

## 4. SEO, files and headers

- [ ] Title, description, canonical, Open Graph, Twitter and JSON-LD agree.
- [ ] `og-cover-2026.jpg` is 1200 × 630 and below 200 KB.
- [ ] `robots.txt` references the canonical sitemap.
- [ ] Sitemap `lastmod` matches the release date.
- [ ] HTTPS, CSP, HSTS, nosniff, frame, referrer and permissions headers exist.
- [ ] HTML is not long-term cached; versioned static assets are cached.

## 5. GitHub surfaces

- [ ] Profile README uses the canonical title and selected projects.
- [ ] Todo README describes only verified scope.
- [ ] Movie Explorer README describes its collaborative prototype scope and has
      no personal Gmail.
- [ ] Old GitHub Pages no longer serves personal information.
- [ ] Old archived repository is private or its public history has been
      sanitized.
- [ ] Old repository is not pinned.

## 6. Production

- [ ] Commit and push the reviewed source.
- [ ] Upload the public site package to Hostinger `public_html/portfolio`.
- [ ] Purge or bypass stale caches.
- [ ] Re-run the browser and HTTP checks against
      `https://portfolio.zyinnova.com/`.
- [ ] Record the commit, deployment date and live verification result in the
      Stage F–H quality record.

Rollback: keep the previous Hostinger file set or backup archive until live
verification passes.
