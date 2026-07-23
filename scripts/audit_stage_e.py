#!/usr/bin/env python3
"""Audit the evidence-based Stage E project portfolio."""

from __future__ import annotations

import json
from pathlib import Path

from lxml import html


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
JS = ROOT / "assets/js/main.js"

EXPECTED_PROJECTS = [
    "LemmikkiLife",
    "GameScan",
    "Multi-language Todo App",
    "Founder Portfolio",
]

EXPECTED_VISUALS = {
    "assets/img/projects/lemmikkilife-cover.webp": 150_000,
    "assets/img/projects/gamescan-cover.webp": 150_000,
    "assets/img/projects/todo-app-cover.svg": 25_000,
    "assets/img/projects/founder-portfolio-cover.svg": 25_000,
}


def normalized_text(node) -> str:
    return " ".join(node.text_content().split())


def main() -> None:
    source = INDEX.read_text(encoding="utf-8")
    document = html.fromstring(source)
    project_section = document.get_element_by_id("portfolio")
    cards = project_section.xpath('.//article[contains(@class, "project-card")]')
    titles = [
        normalized_text(card.xpath('.//*[contains(@class, "project-title")]')[0])
        for card in cards
    ]
    card_by_title = dict(zip(titles, cards, strict=True))

    missing_visuals: list[str] = []
    oversized_visuals: list[str] = []
    for relative_path, byte_limit in EXPECTED_VISUALS.items():
        path = ROOT / relative_path
        if not path.exists():
            missing_visuals.append(relative_path)
        elif path.stat().st_size > byte_limit:
            oversized_visuals.append(relative_path)

    images = project_section.xpath(".//article//img")
    image_sources = {image.get("src") for image in images}
    game_text = normalized_text(card_by_title.get("GameScan"))
    lemmikki_text = normalized_text(card_by_title.get("LemmikkiLife"))
    todo_text = normalized_text(card_by_title.get("Multi-language Todo App"))
    portfolio_text = normalized_text(card_by_title.get("Founder Portfolio"))
    js_source = JS.read_text(encoding="utf-8")

    checks = {
        "four_evidence_based_cards": titles == EXPECTED_PROJECTS,
        "lemmikkilife_is_priority": titles[0] == "LemmikkiLife",
        "gamescan_is_private_without_unverified_stack": all(
            value not in game_text
            for value in ["React", "Vite", "Flutter", "Firebase"]
        )
        and all(
            value in game_text
            for value in [
                "Private / In Development",
                "Technical implementation remains private",
            ]
        ),
        "lemmikkilife_scope_is_limited": all(
            value in lemmikki_text
            for value in ["In Development", "Private", "Pet care"]
        )
        and "Live" not in lemmikki_text
        and "Flutter" not in lemmikki_text,
        "todo_scope_matches_code": all(
            value in todo_text
            for value in [
                "Public Prototype",
                "Flutter",
                "Firebase",
                "English and Finnish localization",
                "Cloud Firestore",
                "local notifications",
            ]
        ),
        "portfolio_is_live_and_linked": all(
            value in portfolio_text
            for value in ["Live", "HTML", "CSS", "JavaScript"]
        ),
        "learning_and_collaboration_projects_absent": all(
            value not in normalized_text(project_section)
            for value in [
                "Movie Explorer",
                "Zikirmatik",
                "Space Invaders",
                "Super Mario",
                "Zelda",
            ]
        ),
        "placeholders_absent": all(
            value not in source
            for value in ["Next ZyInnova Product", "Studio Template System"]
        ),
        "project_links_are_direct": all(
            value in source
            for value in [
                "https://github.com/zyinnova",
                "https://zyinnova.com/projects/lemmikkilife",
                "https://zyinnova.com/projects/gamescan",
                "https://github.com/ZiyaaddinYaramis/github_io_todo_app",
                "https://portfolio.zyinnova.com/",
                "https://github.com/ZiyaaddinYaramis/portfolio-zyinnova-portfolio",
            ]
        ),
        "personal_and_company_github_are_distinct": all(
            value in source
            for value in [
                "https://github.com/ZiyaaddinYaramis",
                "https://github.com/zyinnova",
                "Ziyaaddin Yaramis on GitHub",
                "ZyInnova on GitHub",
            ]
        ),
        "visuals_exist_and_are_optimized": not missing_visuals
        and not oversized_visuals
        and set(EXPECTED_VISUALS).issubset(image_sources),
        "visual_dimensions_and_alt_are_present": len(images) == 4
        and all(
            image.get("width") == "1280"
            and image.get("height") == "720"
            and image.get("loading") == "lazy"
            and (image.get("alt") or "").strip()
            for image in images
        ),
        "typed_animation_is_faster": all(
            value in js_source
            for value in [
                "typeSpeed: 55",
                "backSpeed: 70",
                "backDelay: 650",
            ]
        ),
    }

    result = {
        "passed": all(checks.values()),
        "checks": checks,
        "project_order": titles,
        "missing_visuals": missing_visuals,
        "oversized_visuals": oversized_visuals,
        "visual_bytes": {
            path: (ROOT / path).stat().st_size
            for path in EXPECTED_VISUALS
            if (ROOT / path).exists()
        },
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
