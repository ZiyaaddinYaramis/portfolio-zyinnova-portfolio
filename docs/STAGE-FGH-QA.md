# Stage F–H Quality Record

Release date: 23 July 2026  
Canonical site: <https://portfolio.zyinnova.com/>

## Local verification

### Automated checks

| Check | Result |
|---|---|
| `scripts/audit_stage_d.py` | Passed |
| `scripts/audit_stage_e.py` | Passed |
| `scripts/audit_stage_fgh.py` | Passed |
| `scripts/audit_cv_pair.py` | Passed |
| `node --check assets/js/main.js` | Passed |
| `git diff --check` | Passed |
| Optimized Open Graph image | 1200 × 630, 58,828 bytes |
| Optimized hero background | 236,180 bytes |
| Optimized profile image | 77,972 bytes |

### Browser checks

| View or behavior | Result |
|---|---|
| Mobile menu state and accessible name | Passed |
| Focus moves into the opened mobile menu | Passed |
| Escape closes the menu and returns focus | Passed |
| 375 px horizontal overflow | None |
| 768 px horizontal overflow | None |
| 1440 px horizontal overflow | None |
| Four selected project cards and images | Passed at all three widths |
| Site-owned browser console errors | None |

Reduced-motion behavior is covered by the static audit: CSS removes transition
and entrance motion, JavaScript renders the first hero focus as static text and
disables AOS.

### Link check

The following public targets returned HTTP 200 before deployment:

- ZyInnova
- LemmikkiLife project page
- GameScan project page
- Multi-language Todo App repository
- Founder Portfolio repository

LinkedIn returned its automated-client protection status (`999`). Both
LinkedIn URLs remain the approved canonical addresses and are retained.

## GitHub record

- Todo README update commit:
  `f36fccac191d45a1759121a3f5423c3832a3f02c`
- Movie Explorer README update commit:
  `0e5d6a3d5d408cc4eddd922676f9f37d0ced8e60`
- Profile README update commit:
  `d316ce2`
- Profile bio: `Software Developer • Founder of ZyInnova | Flutter, Firebase,
  web and mobile products.`
- Profile company: `@zyinnova`
- Profile pins: Founder Portfolio, Multi-language Todo App and
  `zyinnova/zyinnova`
- Old Java training pins: removed
- Old `ZiyaaddinYaramis.github.io` Pages source: disabled
- Old repository visibility/state: private and archived
- Old Pages URL: HTTP 404

## Production record

To be completed immediately after publishing:

- Portfolio source commit: `f803aab`
- Hostinger deployment: completed to `public_html/portfolio`
- Live desktop/mobile verification: passed at 375 px and 1440 px
- Live project images: four of four loaded when scrolled into view
- Live browser console: no site-owned errors or warnings
- English CV: HTTP 200, 97,753 bytes
- Finnish CV: HTTP 200, 96,832 bytes
- Open Graph image: HTTP 200, 58,828 bytes
- Live security headers: CSP, HSTS, nosniff, frame, referrer and permissions
  policies passed
- Live cache policy: HTML `no-cache`, CSS 30 days, images one year immutable
- Old public CV path: HTTP 404
- Hostinger temporary files and old `assets.9404`: moved to Trash
- Rollback source: Git commit `3a6bcf3`
- Local rollback archive SHA-256:
  `a214dc41340cbd8c4c2c9a972de16c04b50b1b91729a54b2f2a5d7baf0f2b5ba`
