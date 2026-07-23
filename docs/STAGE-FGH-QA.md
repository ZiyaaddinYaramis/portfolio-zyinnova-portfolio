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
- Profile fields, pins and old Pages privacy: pending authenticated browser
  access

## Production record

To be completed immediately after publishing:

- Portfolio source commit: pending
- Hostinger deployment: pending
- Live desktop/mobile verification: pending
- Live CV download verification: pending
- Live HTTP security/cache headers: pending
- Rollback backup: pending
