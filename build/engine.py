# -*- coding: utf-8 -*-
"""
Nokto Studio site engine.

Shared layout + components used by build_site.py to generate the static
HTML pages of noktostudio.com. Every page is plain HTML after the build,
no runtime dependencies.

Google-colored design system. All pages share one CSS + one JS set under
/assets/. Class names are stable: if you change them here, check that
assets/js/nav.js, forms.js and animations.js still find their hooks.
"""
import html as _html

# ---------------------------------------------------------------- constants

BASE = "https://noktostudio.com"
CAL = "https://calendly.com/hello-noktostudio/30-min-meeting"
EMAIL = "hello@noktostudio.com"

# Google logo letters: N(blue) o(red) k(yellow) t(green)
LOGO = ('<span class="logo-n">N</span><span class="logo-o">o</span>'
        '<span class="logo-k">k</span><span class="logo-t">t</span>o Studio')


MARKET_ROOTS = {"sk": "/sk/", "cz": "/cz/", "en": "/en/"}   # subpage roots
MARKET_HOME = {"sk": "/", "cz": "/cz/", "en": "/en/"}       # brand home

# Paths that exist per market (used by the language toggle to avoid 404s).
SK_PATHS = {
    "", "sluzby/", "sluzby/seo-optimalizacia/", "sluzby/lodalne-seo/",
    "sluzby/seo-pre-ai-vyhladavace/", "sluzby/seo-pre-eshopy/", "sluzby/seo-audit/",
    "sluzby/linkbuilding/", "sluzby/tvorba-webov/", "sluzby/ppc-reklama/",
    "sluzby/email-marketing/", "cennik/", "jak-pracujeme/", "pripady/",
    "villa-paris/", "faq/", "o-nas/", "kontakt/", "blog/", "privacy/", "terms/",
}
CZ_PATHS = {
    "", "sluzby/", "sluzby/seo-optimalizace/", "sluzby/lodalne-seo/",
    "sluzby/seo-pre-ai-vyhledavace/", "sluzby/seo-pre-eshopy/", "sluzby/seo-audit/",
    "sluzby/linkbuilding/", "sluzby/tvorba-webu/", "sluzby/ppc/",
    "cenik/", "jak-pracujeme/", "pripady/", "faq/", "kontakt/", "blog/",
    "privacy/", "terms/",
}
EN_PATHS = {
    "", "services/", "about/", "contact/", "faq/", "blog/", "portfolio/",
    "villa-paris/", "privacy/", "terms/",
}
LANG_PATHS = {"sk": SK_PATHS, "cz": CZ_PATHS, "en": EN_PATHS}


def logo(market: str) -> str:
    return f'<a href="{MARKET_HOME[market]}" class="nav-logo">{LOGO}</a>'


# ---------------------------------------------------------------- navs

def nav_items(market: str) -> list[tuple[str, str]]:
    """(label, href) pairs for the desktop nav. Href uses {{p}} placeholders? No: plain."""
    if market == "sk":
        return [
            ("Služby", "/sk/sluzby/"),
            ("Cenník", "/sk/cennik/"),
            ("Ako pracujeme", "/sk/jak-pracujeme/"),
            ("Prípady", "/sk/pripady/"),
            ("Blog", "/sk/blog/"),
            ("Kontakt", "/sk/kontakt/"),
        ]
    if market == "cz":
        return [
            ("Služby", "/cz/sluzby/"),
            ("Ceník", "/cz/cenik/"),
            ("Jak pracujeme", "/cz/jak-pracujeme/"),
            ("Případy", "/cz/pripady/"),
            ("Blog", "/cz/blog/"),
            ("Kontakt", "/cz/kontakt/"),
        ]
    return [
        ("Services", "/en/services/"),
        ("Pricing", "/en/services/"),
        ("How we work", "/en/about/"),
        ("Blog", "/en/blog/"),
        ("Contact", "/en/contact/"),
    ]


def cta_label(market: str) -> str:
    return {"sk": "Bezplatný hovor", "cz": "Bezplatný hovor", "en": "Free call"}[market]


def lang_toggle(market: str, path: str) -> str:
    """EN | SK | CZ toggle. path is the current page path WITHOUT market prefix.
    Falls back to the market root when the equivalent page does not exist there."""
    pairs = []
    for m, label in (("sk", "SK"), ("cz", "CZ"), ("en", "EN")):
        sub = path if path in LANG_PATHS[m] else ""
        href = MARKET_HOME[m] if sub == "" else MARKET_ROOTS[m] + sub
        active = " active" if m == market else ""
        pairs.append(f'<a href="{href}" class="lang-btn{active}">{label}</a>')
    return '<div class="lang-toggle">' + ' <span>|</span> '.join(pairs) + "</div>"


# ---------------------------------------------------------------- base template

def base(*, market: str, path: str, title: str, desc: str, canonical: str,
         body: str, prefix: str, extra_head: str = "", h1: bool = True) -> str:
    """Render one full page.

    market   : sk | cz | en
    path     : url path after the market root, e.g. 'sluzby/seo-optimalizacia/'
    canonical: full absolute URL
    prefix   : relative prefix for assets from this page, e.g. '../..' or ''
    """
    nav = "".join(f'<li><a href="{href}">{lbl}</a></li>' for lbl, href in nav_items(market))
    mob_nav = "".join(f'<a href="{href}">{lbl}</a>' for lbl, href in nav_items(market))
    asset = (prefix.rstrip("/") + "/") if prefix else ""
    # hreflang only on the market homepages (deep pages have no 1:1 equivalents;
    # per-URL alternates would claim pairs that do not exist)
    if path == "":
        alt_links = [f'<link rel="alternate" hreflang="{c}" href="{h}">' for c, h in
                     (("sk", BASE + "/"), ("cs", BASE + "/cz/"), ("en", BASE + "/en/"),
                      ("x-default", BASE + "/"))]
        hreflang = "\n".join(alt_links)
    else:
        hreflang = ""

    return f"""<!DOCTYPE html>
<html lang="{ {'sk':'sk','cz':'cs','en':'en'}[market] }">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{_html.escape(title)}</title>
  <meta name="description" content="{_html.escape(desc)}">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{_html.escape(title)}">
  <meta property="og:description" content="{_html.escape(desc)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{BASE}/assets/img/og-cover.png">
  <link rel="canonical" href="{canonical}">
{hreflang}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="icon" href="{asset}assets/img/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{asset}assets/css/main.css">
  <link rel="stylesheet" href="{asset}assets/css/components.css">
  <link rel="stylesheet" href="{asset}assets/css/animations.css">
  {extra_head}
</head>
<body>

<header class="site-header" id="site-header">
  <div class="container">
    <nav class="nav">
      {logo(market)}
      <ul class="nav-links">{nav}</ul>
      <div class="nav-right">
        {lang_toggle(market, path)}
        <a href="{CAL}" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm">{cta_label(market)}</a>
        <button class="hamburger" id="hamburger" aria-label="Menu"><span></span><span></span><span></span></button>
      </div>
    </nav>
  </div>
</header>
<nav class="nav-mobile" id="nav-mobile">
  {mob_nav}
  <a href="{CAL}" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="margin-top:10px;">{cta_label(market)}</a>
</nav>

{body}

{footer(market, prefix)}

<script src="{asset}assets/js/clarity.js"></script>
<script src="{asset}assets/js/ga4.js"></script>
<script src="{asset}assets/js/nav.js"></script>
<script src="{asset}assets/js/animations.js"></script>
<script src="{asset}assets/js/forms.js"></script>
<script src="{asset}assets/js/cookie-banner.js"></script>
</body>
</html>
"""


def footer(market: str, prefix: str) -> str:
    if market == "sk":
        cols = [
            ("Služby", [("/sk/sluzby/seo-optimalizacia/", "SEO optimalizácia"),
                        ("/sk/sluzby/lodalne-seo/", "Lokálne SEO a Google profil"),
                        ("/sk/sluzby/seo-pre-ai-vyhladavace/", "SEO pre AI vyhľadávače"),
                        ("/sk/sluzby/seo-pre-eshopy/", "SEO pre e-shopy"),
                        ("/sk/sluzby/seo-audit/", "SEO audit a analýza"),
                        ("/sk/sluzby/linkbuilding/", "Linkbuilding"),
                        ("/sk/sluzby/tvorba-webov/", "Tvorba webov"),
                        ("/sk/sluzby/ppc-reklama/", "PPC reklama")]),
            ("Agentúra", [("/sk/jak-pracujeme/", "Ako pracujeme"),
                          ("/sk/cennik/", "Cenník"),
                          ("/sk/pripady/", "Prípadové štúdie"),
                          ("/sk/o-nas/", "O nás"),
                          ("/sk/blog/", "Blog"),
                          ("/sk/faq/", "FAQ")]),
            ("Kontakt", [(f"mailto:{EMAIL}", EMAIL),
                         (CAL, "Bezplatný hovor 30 min"),
                         ("/sk/kontakt/", "Kontaktný formulár"),
                         ("/sk/privacy/", "Ochrana súkromia"),
                         ("/sk/terms/", "Obchodné podmienky")]),
        ]
    elif market == "cz":
        cols = [
            ("Služby", [("/cz/sluzby/seo-optimalizace/", "SEO optimalizace"),
                        ("/cz/sluzby/lodalne-seo/", "Lokální SEO a firemní profil"),
                        ("/cz/sluzby/seo-pre-ai-vyhledavace/", "SEO pro AI vyhledávače"),
                        ("/cz/sluzby/seo-pre-eshopy/", "SEO pro e-shopy"),
                        ("/cz/sluzby/seo-audit/", "SEO audit a analýza"),
                        ("/cz/sluzby/linkbuilding/", "Linkbuilding"),
                        ("/cz/sluzby/tvorba-webu/", "Tvorba webů"),
                        ("/cz/sluzby/ppc/", "PPC reklama")]),
            ("Agentura", [("/cz/jak-pracujeme/", "Jak pracujeme"),
                          ("/cz/cenik/", "Ceník"),
                          ("/cz/pripady/", "Případové studie"),
                          ("/cz/blog/", "Blog"),
                          ("/cz/faq/", "FAQ")]),
            ("Kontakt", [(f"mailto:{EMAIL}", EMAIL),
                         (CAL, "Bezplatný hovor 30 min"),
                         ("/cz/kontakt/", "Kontaktní formulář"),
                         ("/cz/privacy/", "Zásady ochrany osobních údajů"),
                         ("/cz/terms/", "Obchodní podmínky")]),
        ]
    else:
        cols = [
            ("Services", [("/en/services/", "All services"),
                          ("/en/services/#seo", "SEO & AI visibility"),
                          ("/en/services/#local", "Local SEO & Google Maps"),
                          ("/en/services/#eshop", "E-commerce SEO")]),
            ("Agency", [("/en/about/", "How we work"),
                        ("/en/services/#pricing", "Pricing"),
                        ("/en/portfolio/", "Portfolio"),
                        ("/en/blog/", "Blog"),
                        ("/en/faq/", "FAQ")]),
            ("Contact", [(f"mailto:{EMAIL}", EMAIL),
                         (CAL, "Free 30-min call"),
                         ("/en/contact/", "Contact form"),
                         ("/en/privacy/", "Privacy"),
                         ("/en/terms/", "Terms")]),
        ]
    foot_cols = ""
    for title, links in cols:
        links_html = "".join(f'<a href="{h}">{t}</a>' for h, t in links)
        foot_cols += f'<div class="footer-col"><h4>{title}</h4>{links_html}</div>'
    return f"""
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        {logo(market)}
        <p>SEO agentúra pre podnikateľov. Google, Google Mapy, AI vyhľadávače a e-shopy. Merateľné výsledky za transparentných 12 EUR / hodinu.</p>
      </div>
      {foot_cols}
    </div>
    <div class="footer-bottom">
      <span>© 2026 Nokto Studio. SEO pre Slovensko a Česko.</span>
      <span>Vytvorené rýchlo, merateľné a bez pevných zmlúv.</span>
    </div>
  </div>
</footer>
"""


# ---------------------------------------------------------------- components

def page_hero(label: str, h1_html: str, sub: str, crumbs: list[tuple[str, str]] | None = None) -> str:
    crumb_html = ""
    if crumbs:
        parts = []
        for text, href in crumbs:
            if href:
                parts.append(f'<a href="{href}">{text}</a>')
            else:
                parts.append(f"<span>{text}</span>")
        crumb_html = '<nav class="breadcrumb" aria-label="Drobková navigácia">' + ' <span>›</span> '.join(parts) + "</nav>"
    return f"""
<section class="page-hero">
  <div class="container">
    {crumb_html}
    <span class="section-label">{label}</span>
    <h1>{h1_html}</h1>
    <div class="divider"></div>
    <p class="section-subheading">{sub}</p>
  </div>
</section>
"""


def cta_band(title: str, text: str, market: str) -> str:
    btn1 = {"sk": "Bezplatný strategický hovor", "cz": "Bezplatný strategický hovor", "en": "Book a free call"}[market]
    btn2 = {"sk": "Chcem bezplatný audit", "cz": "Chci bezplatný audit", "en": "Get my free audit"}[market]
    audit_href = {"sk": "/sk/kontakt/?audit=1", "cz": "/cz/kontakt/?audit=1", "en": "/en/contact/?audit=1"}[market]
    return f"""
<div class="cta-band">
  <div>
    <h2>{title}</h2>
    <p>{text}</p>
  </div>
  <div class="hero-ctas">
    <a href="{CAL}" target="_blank" rel="noopener noreferrer" class="btn btn-white btn-lg">{btn1}</a>
    <a href="{audit_href}" class="btn btn-outline btn-lg" style="border-color:rgba(255,255,255,0.3);color:#fff;">{btn2}</a>
  </div>
</div>
"""


def faq_block(items: list[tuple[str, str]]) -> str:
    rows = "".join(
        f'<div class="faq-item"><button class="faq-question" type="button">{q}</button>'
        f'<div class="faq-answer"><p>{a}</p></div></div>' for q, a in items
    )
    return f'<div class="faq-list">{rows}</div>'


def faq_schema(items: list[tuple[str, str]], page_url: str) -> str:
    qas = ",".join(
        '{{"@type":"Question","name":{q},"acceptedAnswer":{{"@type":"Answer","text":{a}}}}}'.format(
            q=_json_str(q), a=_json_str(a)) for q, a in items
    )
    return f'<script type="application/ld+json">\n{{"@context":"https://schema.org","@type":"FAQPage","@id":"{page_url}#faq","mainEntity":[{qas}]}}\n</script>'


def _json_str(s: str) -> str:
    import json
    return json.dumps(s, ensure_ascii=False)


def price_cards(cards: list[dict], market: str) -> str:
    """cards: [{hours, price, monthly, featured, name, items[], cta}]  price shown = h*12 EUR"""
    out = []
    for c in cards:
        feat = " featured" if c.get("featured") else ""
        badge = '<span class="price-badge">Najčastejšia voľba</span>' if c.get("featured") else ""
        if market == "cz":
            badge = '<span class="price-badge">Nejčastější volba</span>' if c.get("featured") else ""
        elif market == "en":
            badge = '<span class="price-badge">Most popular</span>' if c.get("featured") else ""
        lis = "".join(f"<li>{i}</li>" for i in c["items"])
        btn_label = {"sk": "Nezáväznú ponuku", "cz": "Nezávaznou nabídku", "en": "Get a quote"}[market]
        period = {"sk": "mesiac", "cz": "měsíc", "en": "month"}[market]
        out.append(f"""
<div class="price-card{feat}">
  {badge}
  <span class="price-hours">{c['name']}</span>
  <div class="price-amount">{c['price']}<small> EUR / {period}</small></div>
  <div class="price-monthly"><strong>{c['hours']} {'hodín' if market == 'sk' else ('hodin' if market == 'cz' else 'hours')}</strong> × 12 EUR / {'h' if market == 'en' else 'hod.'}</div>
  <ul>{lis}</ul>
  <a href="{CAL}" target="_blank" rel="noopener noreferrer" class="btn btn-primary">{btn_label}</a>
</div>""")
    return f'<div class="pricing-grid">{"".join(out)}</div>'


def steps_block(steps: list[dict]) -> str:
    nums = ["num-blue", "num-red", "num-yellow", "num-green"]
    out = []
    for i, s in enumerate(steps):
        out.append(f"""
<div class="step">
  <span class="step-num {nums[i % 4]}">{i + 1}</span>
  <h3>{s['title']}</h3>
  <p>{s['text']}</p>
</div>""")
    return f'<div class="steps">{"".join(out)}</div>'


def benefit_cards(cards: list[dict]) -> str:
    icons = ["icon-blue", "icon-red", "icon-yellow", "icon-green"]
    out = []
    for i, c in enumerate(cards):
        out.append(f"""
<div class="benefit-card card-hover reveal" data-delay="{(i + 1) * 100}">
  <span class="benefit-icon {icons[i % 4]}">{c['icon']}</span>
  <h3>{c['title']}</h3>
  <p>{c['text']}</p>
</div>""")
    return f'<div class="grid-3">{"".join(out)}</div>'


def schema_service(name: str, desc: str, url: str, offers_hours: int = 10) -> str:
    """Service schema with a simple hourly-rate offer."""
    return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": "{url}#service",
  "name": {_json_str(name)},
  "description": {_json_str(desc)},
  "provider": {{"@id": "{BASE}/#organization"}},
  "areaServed": ["SK", "CZ"],
  "url": "{url}",
  "offers": {{
    "@type": "Offer",
    "price": "12",
    "priceCurrency": "EUR",
    "unitText": "hour",
    "url": "{url}"
  }}
}}
</script>"""


ORG_SCHEMA = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "{BASE}/#organization",
  "name": "Nokto Studio",
  "url": "{BASE}/",
  "logo": "{BASE}/assets/img/favicon.svg",
  "description": "SEO agentúra pre podnikateľov. SEO optimalizácia, lokálne SEO a Google profil, viditeľnosť v AI vyhľadávačoch, SEO pre e-shopy, PPC a tvorba webov. Hodinová cena 12 EUR.",
  "email": "{EMAIL}",
  "areaServed": [{{"@type":"Country","name":"Slovakia"}},{{"@type":"Country","name":"Czech Republic"}}],
  "knowsLanguage": ["sk", "cs", "en"]
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "{BASE}/#website",
  "url": "{BASE}/",
  "name": "Nokto Studio",
  "publisher": {{"@id": "{BASE}/#organization"}},
  "inLanguage": "sk"
}}
</script>"""
