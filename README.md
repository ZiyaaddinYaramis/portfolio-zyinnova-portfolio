# Ziyaaddin Yaramis — Founder Portfolio

The canonical personal portfolio of Ziyaaddin Yaramis, Software Developer and
Founder of [ZyInnova](https://zyinnova.com/).

**Production:** <https://portfolio.zyinnova.com/>

## What this repository contains

- An accessible, responsive single-page portfolio
- Verified professional experience and selected project work
- English and Finnish CV downloads
- SEO, Open Graph, JSON-LD, sitemap and robots metadata
- Apache security, compression and cache rules
- Deterministic CV source and quality-audit scripts

The canonical professional facts live in
[`docs/PROFESSIONAL-PROFILE-SOURCE.md`](docs/PROFESSIONAL-PROFILE-SOURCE.md).
Do not introduce a public claim that conflicts with that source.

## Technology

- Semantic HTML5
- Custom CSS and Bootstrap 5 grid/utilities
- Vanilla JavaScript
- AOS for progressive scroll animation
- Typed.js for the optional hero effect
- Apache `.htaccess` rules for production headers and caching

There is no application build step. Bootstrap JavaScript is intentionally not
loaded because the site does not use Bootstrap interactive components.

## Project structure

```text
/
├── index.html
├── .htaccess
├── robots.txt
├── sitemap.xml
├── assets/
│   ├── css/style.css
│   ├── js/main.js
│   ├── cv/
│   │   ├── Ziyaaddin_Yaramis_CV_EN.pdf
│   │   └── Ziyaaddin_Yaramis_CV_FI.pdf
│   └── img/
├── docs/
├── output/
│   ├── docx/
│   └── pdf/
└── scripts/
```

## Run locally

From the repository root:

```bash
python3 -m http.server 8765
```

Open <http://127.0.0.1:8765/>.

Opening `index.html` directly is not recommended because browser security rules
and absolute production checks behave more reliably through HTTP.

## Quality checks

```bash
python3 scripts/audit_stage_d.py
python3 scripts/audit_stage_e.py
python3 scripts/audit_stage_fgh.py
node --check assets/js/main.js
```

The CV parity command and document-generation procedure are documented in
[`docs/CV-UPDATE-PROCEDURE.md`](docs/CV-UPDATE-PROCEDURE.md).

## Deployment

Production is a static Hostinger deployment:

- Domain: <https://portfolio.zyinnova.com/>
- Target directory: `public_html/portfolio`
- Build step: none

Follow [`docs/RELEASE-CHECKLIST.md`](docs/RELEASE-CHECKLIST.md). Upload the
validated public site files only; development sources such as `output/`,
`scripts/` and internal documentation do not need to be served publicly.

## Related profiles

- [ZyInnova website](https://zyinnova.com/)
- [ZyInnova GitHub](https://github.com/zyinnova)
- [Personal GitHub](https://github.com/ZiyaaddinYaramis)
- [LinkedIn](https://www.linkedin.com/in/ziyaaddin-y-8768841bb/)

## Contact

[contact@zyinnova.com](mailto:contact@zyinnova.com)

## License

Source code is available under the [MIT License](LICENSE). Personal content,
name and branding remain the author's material.
