# CV Update and PDF Publication Procedure

## Source of truth

All facts must first be approved in
[`PROFESSIONAL-PROFILE-SOURCE.md`](PROFESSIONAL-PROFILE-SOURCE.md). English and
Finnish versions must describe the same roles, dates, projects, language levels
and public contact channels.

## Outputs

| Language | Editable source | Reviewed PDF | Public download |
|---|---|---|---|
| English | `output/docx/Ziyaaddin_Yaramis_CV_EN.docx` | `output/pdf/Ziyaaddin_Yaramis_CV_EN.pdf` | `assets/cv/Ziyaaddin_Yaramis_CV_EN.pdf` |
| Finnish | `output/docx/Ziyaaddin_Yaramis_CV_FI.docx` | `output/pdf/Ziyaaddin_Yaramis_CV_FI.pdf` | `assets/cv/Ziyaaddin_Yaramis_CV_FI.pdf` |

## Procedure

1. Update the canonical professional source.
2. Edit both CV generator scripts in the same change.
3. Generate the DOCX files:

   ```bash
   python3 scripts/build_cv_en.py
   python3 scripts/build_cv_fi.py
   ```

4. Render both DOCX files to PDF with Microsoft Word or LibreOffice. Preserve
   A4 page size, embedded links and one-to-two-page length.
5. Normalize publication metadata with `scripts/finalize_cv_pdf.py`, then place
   the reviewed files in `output/pdf/`.
6. Visually inspect every PDF page at normal size and as a thumbnail. Check
   clipping, page breaks, bullet alignment, link appearance and language.
7. Run the parity and privacy audit:

   ```bash
   python3 scripts/audit_cv_pair.py \
     --en-docx output/docx/Ziyaaddin_Yaramis_CV_EN.docx \
     --fi-docx output/docx/Ziyaaddin_Yaramis_CV_FI.docx \
     --en-pdf output/pdf/Ziyaaddin_Yaramis_CV_EN.pdf \
     --fi-pdf output/pdf/Ziyaaddin_Yaramis_CV_FI.pdf
   ```

8. Only after the audit and visual review pass, copy the two PDFs to
   `assets/cv/` using the exact public filenames in the table.
9. Re-run `scripts/audit_stage_d.py` to confirm the site downloads exactly the
   approved PDFs.

## Privacy rules

- Do not publish a street address, personal telephone number or personal Gmail
  address.
- Use `contact@zyinnova.com` as the public contact channel.
- Do not add a photo unless a new explicit publication decision is recorded.
- Remove author and editor metadata from DOCX. PDF metadata may use the public
  professional name and the `ZyInnova CV workflow` creator label.

## Release rule

Never replace only one language. English and Finnish CVs are a versioned pair
and must be released together.
