#!/usr/bin/env python3
"""Audit the Stage D portfolio content and downloadable CV assets."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit

from lxml import etree, html


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
EN_CV = "assets/cv/Ziyaaddin_Yaramis_CV_EN.pdf"
FI_CV = "assets/cv/Ziyaaddin_Yaramis_CV_FI.pdf"
OLD_CV = "assets/cv/MyResume-Ziyaaddin-Yaramis.pdf"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalized_text(node) -> str:
    return " ".join(node.text_content().split())


def main() -> None:
    source = INDEX.read_text(encoding="utf-8")
    parser = html.HTMLParser(encoding="utf-8", recover=False)
    document = html.fromstring(source.encode("utf-8"), parser=parser)
    page_text = normalized_text(document)

    json_ld_nodes = document.xpath(
        '//script[@type="application/ld+json"]/text()'
    )
    person = json.loads(json_ld_nodes[0]) if len(json_ld_nodes) == 1 else {}

    title = normalized_text(document.xpath("//title")[0])
    hero = normalized_text(document.get_element_by_id("hero"))
    about = normalized_text(document.get_element_by_id("about"))
    resume = normalized_text(document.get_element_by_id("resume"))
    projects = normalized_text(document.get_element_by_id("portfolio"))

    required_resume = [
        "Full-Stack Software Developer",
        "Founder & Software Developer — ZyInnova",
        "Current role",
        "Flutter, Dart",
        "Firebase Authentication",
        "Cloud Firestore",
        "REST/HTTP APIs",
        "TMDB API",
        "Graduated 2025",
        "Qualification title: Software Developer",
        "Turkish: Native",
        "English: B2",
        "Finnish: B2",
        "LemmikkiLife",
        "In development",
        "Multi-language Todo App",
        "Public prototype",
        "Founder Portfolio",
        "Live",
        "Earlier Experience",
        "Flutter Developer Intern — Roseance Oy",
        "Oct 2024–Dec 2024",
        "Web Developer Intern — Sisustusklinikka.fi",
        "Feb 2024–May 2024",
        "Java Mentor — Wise Quarter",
        "Police Officer — Turkish National Police",
        "2006–2016",
        "Additional Training",
        "Full-Stack Java Developer Training",
        "TechPro Education • 2021",
        "Finnish CV",
    ]
    forbidden = [
        "MyResume-Ziyaaddin-Yaramis.pdf",
        "Kerava",
        "Founder-driven",
        "Founder & Full-Stack Developer",
        "Product Builder",
        "Startup Founder",
        "Founder & Lead Developer",
        "2023 – Present",
        "Professional working level",
        "Finnish: Developing",
        "Metropolia",
        "Wisequarter",
        "Techproed",
        "Next ZyInnova Product",
        "Studio Template System",
        "production-ready",
    ]

    local_missing: list[str] = []
    for attribute in document.xpath("//@href | //@src"):
        value = str(attribute)
        parsed = urlsplit(value)
        if parsed.scheme or value.startswith(("#", "mailto:", "data:")):
            continue
        target = ROOT / unquote(parsed.path)
        if not target.exists():
            local_missing.append(value)

    ids = document.xpath("//@id")
    image_alts = document.xpath("//img/@alt")
    images = document.xpath("//img")
    en_links = document.xpath(f'//a[@href="{EN_CV}"]')
    fi_links = document.xpath(f'//a[@href="{FI_CV}"]')

    checks = {
        "html_parses": not parser.error_log,
        "title_is_canonical": title
        == "Ziyaaddin Yaramis | Software Developer • Founder of ZyInnova",
        "hero_is_canonical": (
            "Software Developer • Founder of ZyInnova" in hero
        ),
        "about_is_canonical": all(
            value in about
            for value in [
                "software developer and founder of ZyInnova",
                "evidence-based communication",
                "LemmikkiLife is the current priority product in development",
            ]
        ),
        "resume_has_verified_content": all(
            value in resume for value in required_resume
        ),
        "lemmikkilife_is_first_resume_project": (
            resume.find("LemmikkiLife")
            < resume.find("Multi-language Todo App")
            < resume.find("Founder Portfolio")
        ),
        "projects_match_verified_selection": all(
            value in projects
            for value in [
                "LemmikkiLife",
                "In Development",
                "Multi-language Todo App",
                "Public Prototype",
                "Founder Portfolio",
                "Live",
            ]
        )
        and projects.find("LemmikkiLife")
        < projects.find("Multi-language Todo App")
        < projects.find("Founder Portfolio"),
        "forbidden_content_absent": not any(
            value.casefold() in source.casefold() for value in forbidden
        ),
        "structured_title_is_canonical": person.get("jobTitle")
        == "Full-Stack Software Developer | Founder, ZyInnova",
        "structured_address_absent": "address" not in person,
        "structured_links_are_approved": set(person.get("sameAs", []))
        == {
            "https://github.com/ZiyaaddinYaramis",
            "https://www.linkedin.com/in/ziyaaddin-y-8768841bb/",
            "https://zyinnova.com/",
        },
        "structured_zyinnova_company_link_is_approved": (
            person.get("worksFor", {}).get("name") == "ZyInnova"
            and set(person.get("worksFor", {}).get("sameAs", []))
            == {
                "https://github.com/zyinnova",
                "https://www.linkedin.com/company/zyinnova/",
            }
        ),
        "personal_linkedin_is_available": len(
            document.xpath(
                '//a[@href="https://www.linkedin.com/in/ziyaaddin-y-8768841bb/"]'
            )
        )
        >= 4,
        "company_linkedin_is_available": len(
            document.xpath(
                '//a[@href="https://www.linkedin.com/company/zyinnova/"]'
            )
        )
        >= 2,
        "hero_typed_focus_is_available": len(
            document.xpath(
                '//*[@id="hero"]//*[@class="typed" and '
                '@data-typed-items="Flutter & Firebase, Web & Mobile Development, ZyInnova Products"]'
            )
        )
        == 1,
        "english_cv_linked_three_times": len(en_links) == 3,
        "finnish_cv_linked_three_times": len(fi_links) == 3,
        "old_cv_absent": not (ROOT / OLD_CV).exists()
        and OLD_CV not in source,
        "english_cv_matches_verified_output": sha256(ROOT / EN_CV)
        == sha256(ROOT / "output/pdf/Ziyaaddin_Yaramis_CV_EN.pdf"),
        "finnish_cv_matches_verified_output": sha256(ROOT / FI_CV)
        == sha256(ROOT / "output/pdf/Ziyaaddin_Yaramis_CV_FI.pdf"),
        "local_assets_exist": not local_missing,
        "ids_are_unique": len(ids) == len(set(ids)),
        "all_images_have_alt": len(image_alts) == len(images)
        and all(value.strip() for value in image_alts),
    }

    result = {
        "passed": all(checks.values()),
        "checks": checks,
        "missing_local_assets": sorted(set(local_missing)),
        "cv_sha256": {
            "english": sha256(ROOT / EN_CV),
            "finnish": sha256(ROOT / FI_CV),
        },
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
