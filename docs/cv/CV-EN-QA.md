# English CV Quality Record

> Verification date: 23 July 2026  
> Related tasks: B-01 through B-06  
> Result: Passed

## Final Artifacts

- Editable DOCX:
  `output/docx/Ziyaaddin_Yaramis_CV_EN.docx`
- General English PDF:
  `output/pdf/Ziyaaddin_Yaramis_CV_EN.pdf`
- Approved content:
  `docs/cv/CV-EN-CONTENT.md`
- Reproducible builders:
  `scripts/build_cv_en.py` and `scripts/finalize_cv_pdf.py`

## Content Verification

- Canonical professional title is used.
- LemmikkiLife is presented first and explicitly marked `In development`.
- Todo App is marked `Public prototype`, not `Live`.
- Project technologies and features are limited to code or public-status
  evidence.
- KEUDA/Keuda graduation is shown as 2025.
- Languages are Turkish Native, English B2, and Finnish B2.
- Roseance Oy, Sisustusklinikka.fi, Wise Quarter, and Turkish National Police
  appear under `Earlier Experience` with user-confirmed roles and dates.
- TechPro Education appears under `Additional Training`, not employment.
- Unsupported responsibility, technology, and outcome claims are excluded.

## Visual Verification

- DOCX was rendered with the bundled LibreOffice workflow.
- The rendered DOCX produced two A4 pages with a deliberate page break before
  `Selected Projects`.
- The finalized PDF was rendered independently with Poppler.
- Both page images were inspected at full resolution.
- No clipping, overlap, broken glyphs, awkward page break, or excessive blank
  page was found.
- The final layout is single-column and contains no photo, table, text box, or
  decorative layout object.

## Technical Verification

| Check | Result |
|---|---|
| PDF page count | 2 |
| PDF page size | A4 |
| Selectable PDF text | Passed; 2,931 extracted characters |
| Required sections | All eight present in DOCX and PDF |
| DOCX accessibility audit | 0 high, 0 medium, 0 low findings |
| DOCX heading hierarchy | Eight `Heading 1` sections; no skipped level |
| Images | None |
| PDF tagged | Yes |
| PDF JavaScript | None |
| PDF encryption | None |
| External links | Seven unique targets verified |
| Public email | Only `contact@zyinnova.com` |
| Forbidden personal-data terms | None found |
| DOCX creator/last editor | Blank |
| PDF author | Ziyaaddin Yaramis |
| PDF title | Ziyaaddin Yaramis - English CV |

Verified PDF targets:

- `mailto:contact@zyinnova.com`
- `https://portfolio.zyinnova.com/`
- `https://github.com/ZiyaaddinYaramis`
- `https://zyinnova.com/`
- `https://zyinnova.com/projects/lemmikkilife`
- `https://github.com/ZiyaaddinYaramis/github_io_todo_app`
- `https://github.com/ZiyaaddinYaramis/portfolio-zyinnova-portfolio`

## Integrity

- DOCX SHA-256:
  `c3410520f7d4a8a1a96c71ddf810a69ce2fb3a790003727e96bc30a639f2f3de`
- PDF SHA-256:
  `caa2d6418991b501c712c956fbd99f296da53f9a40271735f07b7ab3fe394fbc`

Hashes identify the exact artifacts that passed this record. Any later artifact
change requires a new render, audit, and hash update.
