# -*- coding: utf-8 -*-
"""
Nokto Studio - site builder.

Generates the static HTML of noktostudio.com from the content modules in
build/. Run from the repo root:

    python3 build_site.py

What it does:
  1. Renders all SK pages (root index is the SK homepage).
  2. Renders all CZ pages.
  3. Renders core EN pages (projects stay as legacy pages).
  4. Writes sitemap.xml and robots.txt.
  5. Preserves the pre-redesign CSS as legacy files for the EN project demos.

Everything the script writes is plain static HTML; the live site needs no
Python. Re-run any time after editing build/*.py.
"""
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO / "build"))

import pages_sk as sk          # noqa: E402
import pages_sk2 as sk2        # noqa: E402
import pages_cz as cz          # noqa: E402
from engine import BASE        # noqa: E402

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
add(sk.tvorba_webov())
add(sk.ppc_reklama())
add(sk.email_marketing())
add(sk.cennik())
add(sk2.jak_pracujeme())
add(sk2.pripady())
add(sk2.villa_paris())
add(sk2.faq())
add(sk2.o_nas())
add(sk2.kontakt())
add(sk2.blog())
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
add(cz.cz_tvorba_webu())
add(cz.cz_ppc())
add(cz.cz_cenik())
add(cz.cz_jak_pracujeme())
add(cz.cz_pripady())
add(cz.cz_faq())
add(cz.cz_kontakt())
add(cz.cz_blog())
add(cz.cz_privacy())
add(cz.cz_terms())

# ---------------------------------------------------------------- EN pages
import pages_en as en          # noqa: E402
for p in en.ALL:
    add(p)

# ---------------------------------------------------------------- write HTML

def write_pages():
    for rel, html in PAGES:
        out = REPO / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        print(f"  wrote {rel}  ({len(html):,} B)")
    print(f"{len(PAGES)} pages written.")


# ---------------------------------------------------------------- sitemap

SITEMAP_ENTRIES = [
    # (path, priority)
    ("",                    "1.0"),
    ("cennik/",             "0.9"),
    ("sluzby/",             "0.9"),
    ("sluzby/seo-optimalizacia/",         "0.8"),
    ("sluzby/lodalne-seo/",               "0.8"),
    ("sluzby/seo-pre-ai-vyhladavace/",    "0.8"),
    ("sluzby/seo-pre-eshopy/",            "0.8"),
    ("sluzby/seo-audit/",                 "0.8"),
    ("sluzby/linkbuilding/",              "0.7"),
    ("sluzby/tvorba-webov/",              "0.7"),
    ("sluzby/ppc-reklama/",               "0.7"),
    ("sluzby/email-marketing/",           "0.7"),
    ("jak-pracujeme/",      "0.8"),
    ("pripady/",            "0.7"),
    ("villa-paris/",        "0.6"),
    ("faq/",                "0.6"),
    ("o-nas/",              "0.6"),
    ("kontakt/",            "0.6"),
    ("blog/",               "0.5"),
    ("privacy/",            "0.2"),
    ("terms/",              "0.2"),
]


def sitemap_url(loc: str, priority: str, lang: str, home: bool = False) -> str:
    if home:
        hrefs = {"sk": BASE + "/", "cz": BASE + "/cz/", "en": BASE + "/en/"}
        alt = "".join(
            f'<xhtml:link rel="alternate" hreflang="{cl}" href="{h}"/>'
            for cl, h in (("sk", hrefs["sk"]), ("cs", hrefs["cz"]), ("en", hrefs["en"]),
                          ("x-default", BASE + "/"))
        )
        return f"""  <url>
    <loc>{loc}</loc>
    {alt}
    <priority>{priority}</priority>
  </url>"""
    return f"""  <url>
    <loc>{loc}</loc>
    <priority>{priority}</priority>
  </url>"""


def write_sitemap():
    rows = [sitemap_url(BASE + "/", "1.0", "sk", home=True)]
    for path, pr in SITEMAP_ENTRIES:
        rows.append(sitemap_url(f"{BASE}/sk/{path}", pr, "sk"))
    # CZ
    cz_paths = [
        ("", "1.0"), ("cenik/", "0.9"), ("sluzby/", "0.9"),
        ("sluzby/seo-optimalizace/", "0.8"), ("sluzby/lodalne-seo/", "0.8"),
        ("sluzby/seo-pre-ai-vyhledavace/", "0.8"), ("sluzby/seo-pre-eshopy/", "0.8"),
        ("sluzby/seo-audit/", "0.8"), ("sluzby/linkbuilding/", "0.7"),
        ("sluzby/tvorba-webu/", "0.7"), ("sluzby/ppc/", "0.7"),
        ("jak-pracujeme/", "0.8"), ("pripady/", "0.7"),
        ("faq/", "0.6"), ("kontakt/", "0.6"), ("blog/", "0.5"),
        ("privacy/", "0.2"), ("terms/", "0.2"),
    ]
    rows.append(sitemap_url(BASE + "/cz/", "1.0", "cz", home=True))
    for path, pr in cz_paths:
        if path == "":
            continue
        rows.append(sitemap_url(f"{BASE}/cz/{path}", pr, "cz"))
    # EN (legacy pages keep self-canonical, include the ones we regenerate)
    en_paths = ["", "services/", "about/", "contact/", "faq/", "blog/", "portfolio/",
                "villa-paris/", "privacy/", "terms/"]
    for p in en_paths:
        rows.append(f"""  <url>
    <loc>{BASE}/en/{p}</loc>
    <priority>0.5</priority>
  </url>""")
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
