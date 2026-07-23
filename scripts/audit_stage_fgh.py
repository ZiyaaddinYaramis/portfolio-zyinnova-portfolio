#!/usr/bin/env python3
"""Audit Stage F accessibility, Stage G web quality and Stage H documentation."""

from __future__ import annotations

import json
from pathlib import Path

from lxml import etree, html
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
CSS = ROOT / "assets/css/style.css"
JS = ROOT / "assets/js/main.js"
HTACCESS = ROOT / ".htaccess"


def main() -> None:
    source = INDEX.read_text(encoding="utf-8")
    css = CSS.read_text(encoding="utf-8")
    js = JS.read_text(encoding="utf-8")
    htaccess = HTACCESS.read_text(encoding="utf-8")
    document = html.fromstring(source)

    toggle = document.xpath(
        '//button[contains(concat(" ", normalize-space(@class), " "), '
        '" mobile-nav-toggle ")]'
    )
    scripts = set(document.xpath("//script/@src"))
    styles = set(document.xpath('//link[@rel="stylesheet"]/@href'))

    og_path = ROOT / "assets/img/og-cover-2026.jpg"
    background_path = ROOT / "assets/img/background-portfolio.webp"
    profile_path = ROOT / "assets/img/profile-zy.webp"
    with Image.open(og_path) as og_image:
        og_dimensions = og_image.size

    parser = etree.XMLParser()
    sitemap = etree.parse(str(ROOT / "sitemap.xml"), parser)
    sitemap_namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    sitemap_url = sitemap.xpath("string(/s:urlset/s:url/s:loc)", namespaces=sitemap_namespace)
    sitemap_lastmod = sitemap.xpath(
        "string(/s:urlset/s:url/s:lastmod)", namespaces=sitemap_namespace
    )

    required_docs = [
        ROOT / "docs/CV-UPDATE-PROCEDURE.md",
        ROOT / "docs/RELEASE-CHECKLIST.md",
        ROOT / "docs/github/PROFILE-README.md",
        ROOT / "docs/github/TODO-README.md",
        ROOT / "docs/github/MOVIE-README.md",
    ]

    checks = {
        "mobile_toggle_is_accessible_button": len(toggle) == 1
        and toggle[0].get("type") == "button"
        and toggle[0].get("aria-controls") == "header"
        and toggle[0].get("aria-expanded") == "false"
        and toggle[0].get("aria-label") == "Open navigation",
        "mobile_state_and_focus_are_managed": all(
            value in js
            for value in [
                'event.key === "Escape"',
                'event.key !== "Tab"',
                '"aria-expanded"',
                '"aria-label"',
                'toggleAttribute("inert"',
                "mobileToggle.focus()",
                "navbarlinks[0]?.focus()",
            ]
        ),
        "active_navigation_is_announced": 'setAttribute("aria-current", "page")'
        in js,
        "skip_link_and_focus_styles_exist": bool(
            document.xpath('//a[@class="skip-link" and @href="#main"]')
        )
        and ".skip-link:focus" in css
        and ":focus-visible" in css,
        "reduced_motion_is_complete": all(
            value in css + js
            for value in [
                "prefers-reduced-motion: reduce",
                "reduceMotion",
                "typed.textContent = strings[0]",
                "disable: reduceMotion",
                "scroll-behavior: auto !important",
            ]
        ),
        "bootstrap_javascript_is_absent": not any(
            "bootstrap" in script for script in scripts
        ),
        "required_vendor_assets_only": {
            "https://unpkg.com/aos@2.3.4/dist/aos.js",
            "https://cdn.jsdelivr.net/npm/typed.js@2.0.12",
            "assets/js/main.js?v=20260723f",
        }.issubset(scripts)
        and {
            "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css",
            "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css",
            "https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css",
            "https://unpkg.com/aos@2.3.4/dist/aos.css",
        }.issubset(styles),
        "remote_font_stylesheet_is_absent": "fonts.googleapis.com" not in source
        and "fonts.gstatic.com" not in source,
        "optimized_images_are_referenced": all(
            value in source + css
            for value in [
                "assets/img/background-portfolio.webp",
                "assets/img/profile-zy.webp",
                "assets/img/og-cover-2026.jpg",
            ]
        ),
        "optimized_image_budgets_pass": background_path.stat().st_size < 300_000
        and profile_path.stat().st_size < 100_000
        and og_path.stat().st_size < 200_000
        and og_dimensions == (1200, 630),
        "security_headers_are_declared": all(
            value in htaccess
            for value in [
                "Content-Security-Policy",
                "Strict-Transport-Security",
                "Permissions-Policy",
                "X-Content-Type-Options",
                "X-Frame-Options",
                "Referrer-Policy",
                "upgrade-insecure-requests",
            ]
        ),
        "cache_and_compression_are_declared": all(
            value in htaccess
            for value in [
                "mod_expires",
                "Cache-Control",
                "immutable",
                "no-cache",
                "mod_deflate",
            ]
        ),
        "seo_metadata_is_canonical": all(
            value in source
            for value in [
                'rel="canonical" href="https://portfolio.zyinnova.com/"',
                'property="og:site_name"',
                'property="og:locale"',
                'name="twitter:image:alt"',
                '"@type": "Person"',
                '"https://github.com/zyinnova"',
            ]
        ),
        "robots_and_sitemap_are_current": (
            "Sitemap: https://portfolio.zyinnova.com/sitemap.xml"
            in (ROOT / "robots.txt").read_text(encoding="utf-8")
            and sitemap_url == "https://portfolio.zyinnova.com/"
            and sitemap_lastmod == "2026-07-23"
        ),
        "documentation_set_is_complete": all(path.exists() for path in required_docs),
        "github_corrections_are_prepared": all(
            value
            in (ROOT / "docs/github/PROFILE-README.md").read_text(encoding="utf-8")
            for value in ["Software Developer", "LemmikkiLife", "GameScan"]
        )
        and "personal Gmail"
        not in (ROOT / "docs/github/MOVIE-README.md").read_text(encoding="utf-8")
        and "public prototype"
        in (ROOT / "docs/github/TODO-README.md").read_text(encoding="utf-8").lower(),
    }

    result = {
        "passed": all(checks.values()),
        "checks": checks,
        "image_bytes": {
            "background": background_path.stat().st_size,
            "profile": profile_path.stat().st_size,
            "open_graph": og_path.stat().st_size,
        },
        "open_graph_dimensions": og_dimensions,
    }
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
