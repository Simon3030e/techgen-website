# -*- coding: utf-8 -*-
"""
Nokto Studio - site builder.

Generates the static HTML of noktostudio.com from the content modules in
build/. Run from the repo root:

    python3 build_site.py

What it does:
  1. Renders all SK pages (root index is the SK homepage).
  2. Renders all CZ pages.
  4. Writes sitemap.xml and robots.txt.
  5. Preserves the pre-redesign CSS as legacy files for the EN project demos.

Everything the script writes is plain static HTML; the live site needs no
Python. Re-run any time after editing build/*.py.
"""
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO / "build"))

import pages_sk as sk          # noqa: E402
import pages_sk2 as sk2        # noqa: E402
import pages_cz as cz          # noqa: E402
import pages_en as en          # noqa: E402
from engine import (BASE, HREFLANG_PAIR, EN_PAIR, EN_PAIR_REV, CZ_PATHS,  # noqa: E402
                    MARKET_HOME, MARKET_ROOTS)

PAGES: list[tuple[str, str]] = []

def add(p: tuple[str, str]):
    PAGES.append(p)

# ---------------------------------------------------------------- SK pages
add(sk.home())                 # root index.html = SK homepage
add(sk.sluzby())
add(sk.seo_optimalizacia())
add(sk.lodalne_seo())
add(sk.seo_ai())
add(sk.eshop_seo())
add(sk.audit_seo())
add(sk.linkbuilding())
add(sk.cennik())
add(sk2.jak_pracujeme())
add(sk2.vysledky())
add(sk2.vysledky_redirect())
add(sk2.villa_paris())
add(sk2.faq())
add(sk2.o_nas())
add(sk2.kontakt())
add(sk2.blog())
add(sk2.blog_post_navod())
add(sk2.blog_post_kolko_stoji())
add(sk2.blog_post_seo_test())
add(sk2.blog_post_linkbuilding())
add(sk2.blog_post_gbp())
add(sk2.blog_post_wordpress())
add(sk2.sk_redirect())
add(sk2.sk_privacy())
add(sk2.sk_terms())

# ---------------------------------------------------------------- CZ pages
add(cz.cz_home())
add(cz.cz_sluzby_hub())
add(cz.cz_seo_optimalizace())
add(cz.cz_lodalne_seo())
add(cz.cz_seo_ai())
add(cz.cz_eshop_seo())
add(cz.cz_audit())
add(cz.cz_linkbuilding())
add(cz.cz_cenik())
add(cz.cz_jak_pracujeme())
add(cz.cz_vysledky())
add(cz.cz_vysledky_redirect())
add(cz.cz_faq())
add(cz.cz_kontakt())
add(cz.cz_blog())
add(cz.cz_privacy())
add(cz.cz_terms())

# ---------------------------------------------------------------- EN pages
add(en.en_home())
add(en.en_services())
add(en.en_portfolio())
add(en.en_about())
add(en.en_contact())
add(en.en_faq())
add(en.en_blog())
add(en.en_villa_paris())
add(en.en_privacy())
add(en.en_terms())

# ---------------------------------------------------------------- write HTML

def write_pages():
    for rel, html in PAGES:
        out = REPO / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        print(f"  wrote {rel}  ({len(html):,} B)")
    print(f"{len(PAGES)} pages written.")


# ---------------------------------------------------------------- sitemap

SK_ENTRIES = [
    # (path, priority)  path "" = SK home = https://noktostudio.com/
    ("",                    "1.0"),
    ("cennik/",             "0.9"),
    ("sluzby/",             "0.9"),
    ("sluzby/seo-optimalizacia/",         "0.8"),
    ("sluzby/lodalne-seo/",               "0.8"),
    ("sluzby/seo-pre-ai-vyhladavace/",    "0.8"),
    ("sluzby/seo-pre-eshopy/",            "0.8"),
    ("sluzby/seo-audit/",                 "0.8"),
    ("sluzby/linkbuilding/",              "0.7"),
    ("jak-pracujeme/",      "0.8"),
    ("vysledky/",           "0.7"),
    ("villa-paris/",        "0.6"),
    ("faq/",                "0.6"),
    ("o-nas/",              "0.6"),
    ("kontakt/",            "0.6"),
    ("blog/",               "0.5"),
    ("blog/seo-optimalizacia-navod/",     "0.5"),
    ("blog/kolko-stoji-seo/",             "0.5"),
    ("blog/seo-test-15-bodov/",           "0.5"),
    ("blog/linkbuilding-co-to-je/",       "0.5"),
    ("blog/google-firmy-profil-navod/",   "0.5"),
    ("blog/seo-wordpress/",               "0.5"),
    ("privacy/",            "0.2"),
    ("terms/",              "0.2"),
]


def _mkurl(loc: str, priority: str, alts: str = "") -> str:
    return f"""  <url>
    <loc>{loc}</loc>
    {alts}<lastmod>{LASTMOD}</lastmod><priority>{priority}</priority>
  </url>"""


LASTMOD = time.strftime("%Y-%m-%d")

EN_ENTRIES = [
    # (path after /en/, priority)
    ("",             "1.0"),
    ("services/",    "0.9"),
    ("portfolio/",   "0.7"),
    ("about/",       "0.6"),
    ("contact/",     "0.6"),
    ("faq/",         "0.6"),
    ("blog/",        "0.5"),
    ("villa-paris/", "0.6"),
    ("privacy/",     "0.2"),
    ("terms/",       "0.2"),
]


def _alts3(sk_sub: str) -> str:
    """hreflang alternates for one logical page, identified by its SK sub-path.
    Only languages with a real page get an alternate; x-default = SK."""
    subs = {"sk": sk_sub,
            "cz": HREFLANG_PAIR.get(sk_sub),
            "en": EN_PAIR.get(sk_sub)}
    lang_code = {"sk": "sk", "cz": "cs", "en": "en"}
    out = []
    for m in ("sk", "cz", "en"):
        s = subs[m]
        if s is None:
            continue
        u = BASE + (MARKET_HOME[m] if s == "" else MARKET_ROOTS[m] + s)
        out.append(f'<xhtml:link rel="alternate" hreflang="{lang_code[m]}" href="{u}"/>')
    out.append(f'<xhtml:link rel="alternate" hreflang="x-default" href="{BASE + MARKET_HOME["sk"] if sk_sub == "" else BASE + "/sk/" + sk_sub}"/>')
    return "".join(out)


def write_sitemap():
    rows = []
    # SK variant of every logical page (root index is the SK home)
    for path, pr in SK_ENTRIES:
        sk_url = BASE + ("/" if path == "" else "/sk/" + path)
        rows.append(_mkurl(sk_url, pr, _alts3(path)))
    # CZ variants: every CZ page that is the 1:1 pair of an SK page.
    # Each variant is its own <url> entry, as Google recommends.
    for path, pr in SK_ENTRIES:
        cz_path = HREFLANG_PAIR.get(path)
        if cz_path is None or cz_path not in CZ_PATHS:
            continue
        cz_url = BASE + "/cz/" + cz_path
        rows.append(_mkurl(cz_url, pr, _alts3(path)))
    # EN variants (core pages only; service subpages live on the EN hub)
    for path, pr in EN_ENTRIES:
        en_url = BASE + "/en/" + path
        rows.append(_mkurl(en_url, pr, _alts3(EN_PAIR_REV[path])))
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
           'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    (REPO / "sitemap.xml").write_text(xml, encoding="utf-8")
    print(f"  wrote sitemap.xml ({xml.count('<loc>'):,} urls)")


def write_robots():
    robots = f"""User-agent: *
Allow: /

# AI crawlers: welcome. We want to be cited.
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: CCBot
Allow: /

Sitemap: {BASE}/sitemap.xml
"""
    (REPO / "robots.txt").write_text(robots, encoding="utf-8")
    print("  wrote robots.txt")


def write_legacy_css():
    """Preserve pre-redesign CSS for the EN project demo pages."""
    import subprocess
    legacy = REPO / "assets" / "css"
    for name in ("main.css", "components.css", "animations.css"):
        dst = legacy / f"legacy-{name}"
        src = subprocess.run(
            ["git", "show", f"HEAD:assets/css/{name}"],
            capture_output=True, text=True, cwd=REPO,
        )
        if src.returncode == 0 and src.stdout.strip():
            dst.write_text(src.stdout, encoding="utf-8")
            print(f"  wrote legacy-{name} for EN project demos")


def relink_legacy_pages():
    """Point EN project demo pages at the legacy CSS files."""
    import re
    targets = list((REPO / "en" / "projects").glob("*/index.html"))
    for page in targets:
        text = page.read_text(encoding="utf-8")
        text = text.replace("assets/css/main.css", "assets/css/legacy-main.css")
        text = text.replace("assets/css/components.css", "assets/css/legacy-components.css")
        text = text.replace("assets/css/animations.css", "assets/css/legacy-animations.css")
        page.write_text(text, encoding="utf-8")
    print(f"  relinked {len(targets)} EN project demo pages to legacy CSS")


if __name__ == "__main__":
    print("Building noktostudio.com ...")
    write_pages()
    write_sitemap()
    write_robots()
    write_legacy_css()
    relink_legacy_pages()
    print("Done.")
