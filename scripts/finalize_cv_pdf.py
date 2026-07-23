#!/usr/bin/env python3
"""Copy a rendered CV PDF while replacing metadata with publication-safe values."""

from __future__ import annotations

import argparse
from pathlib import Path

from pypdf import PdfReader, PdfWriter


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument(
        "--title", default="Ziyaaddin Yaramis - English CV"
    )
    parser.add_argument(
        "--author", default="Ziyaaddin Yaramis"
    )
    parser.add_argument(
        "--subject", default="General English curriculum vitae"
    )
    parser.add_argument(
        "--keywords",
        default="Software Developer, ZyInnova, Flutter, Firebase",
    )
    parser.add_argument("--creator", default="ZyInnova CV workflow")
    args = parser.parse_args()

    reader = PdfReader(args.input)
    writer = PdfWriter()
    writer.clone_document_from_reader(reader)
    writer.add_metadata(
        {
            "/Title": args.title,
            "/Author": args.author,
            "/Subject": args.subject,
            "/Keywords": args.keywords,
            "/Creator": args.creator,
        }
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("wb") as handle:
        writer.write(handle)


if __name__ == "__main__":
    main()
