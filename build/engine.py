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
PHONE_DISPLAY = "+421 917 316 105"
PHONE_TEL = "tel:+421917316105"
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
    "sluzby/linkbuilding/", "cennik/", "jak-pracujeme/", "pripady/",
    "villa-paris/", "faq/", "o-nas/", "kontakt/", "blog/", "privacy/", "terms/",
}
CZ_PATHS = {
    "", "sluzby/", "sluzby/seo-optimalizace/", "sluzby/lodalne-seo/",
    "sluzby/seo-pre-ai-vyhledavace/", "sluzby/seo-pre-eshopy/", "sluzby/seo-audit/",
    "sluzby/linkbuilding/", "cenik/", "jak-pracujeme/", "pripady/", "faq/", "kontakt/", "blog/",
    "privacy/", "terms/",
}
EN_PATHS = {
    "", "services/", "about/", "contact/", "faq/", "blog/", "portfolio/",
    "villa-paris/", "privacy/", "terms/",
}
LANG_PATHS = {"sk": SK_PATHS, "cz": CZ_PATHS, "en": EN_PATHS}


def logo(market: str) -> str:
    return f'<a href="{MARKET_HOME[market]}" class="nav-logo">{LOGO}</a>'


# ------------------------------------------------- svg icons (no emojis)
_GICON_PATHS = {
    "ai":     '<path d="M12 3a5 5 0 0 1 5 5c0 2.4-1.7 4.4-4 4.9V16h-2v-3.1c-2.3-.5-4-2.5-4-4.9a5 5 0 0 1 5-5Z"/><circle cx="12" cy="20.5" r="1.6"/>',
    "search": '<circle cx="10.5" cy="10.5" r="6.5"/><path d="m15.5 15.5 5 5"/>',
    "pin":    '<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11Z"/><circle cx="12" cy="10" r="2.5"/>',
    "shop":   '<path d="M4 7h16l-1.5 13h-13L4 7Z"/><path d="M8.5 10V6.5a3.5 3.5 0 0 1 7 0V10"/>',
    "audit":  '<path d="M6 3h9l4 4v14H6V3Z"/><path d="M9 12h6M9 16h6M9 8h3"/>',
    "link":   '<path d="M10 14a4 4 0 0 0 6 .4l3-3a4 4 0 1 0-5.7-5.7l-1.5 1.5"/><path d="M14 10a4 4 0 0 0-6-.4l-3 3a4 4 0 1 0 5.7 5.7l1.5-1.5"/>',
    "mail":   '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    "web":    '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M7 6.5h.01M10 6.5h.01"/>',
    "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="0.5"/>',
    "chart":  '<path d="M4 20h16"/><path d="M7 20v-6M12 20V9M17 20v-9"/>',
    "shield": '<path d="M12 3 5 6v6c0 4.5 3 7.6 7 9 4-1.4 7-4.5 7-9V6l-7-3Z"/>',
    "bolt":   '<path d="M13 2 5 13h6l-1 9 8-11h-6l1-9Z"/>',
    "check":  '<path d="m4.5 12.5 5 5L19.5 7"/>',
    "grow":   '<path d="M4 19 10 13l3.5 3.5L20 10"/><path d="M20 15v-5h-5"/>',
}

def gicon(kind: str, color: str = "#1A73E8", size: int = 24) -> str:
    """Material-style line icon, Google colors only, no emoji."""
    path = _GICON_PATHS[kind]
    return (f'<span class="gicon" style="color:{color};width:{size}px;height:{size}px;" aria-hidden="true">'
            f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="currentColor" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{path}</svg></span>')


# ---------------------------------------------------------------- navs

def nav_items(market: str) -> list[tuple[str, str]]:
    """(label, href) pairs for the desktop nav. Href uses {{p}} placeholders? No: plain."""
    svc = ("Služby", "/sk/sluzby/", [
        ("/sk/sluzby/seo-pre-ai-vyhladavace/", "AI viditeľnosť"),
        ("/sk/sluzby/seo-optimalizacia/", "Google viditeľnosť"),
        ("/sk/sluzby/lodalne-seo/", "Google Mapy viditeľnosť"),
        ("/sk/sluzby/seo-pre-eshopy/", "SEO pre e-shopy"),
        ("/sk/sluzby/seo-audit/", "SEO audit a analýza"),
        ("/sk/sluzby/linkbuilding/", "Linkbuilding"),
    ]) if market == "sk" else ("Služby", "/cz/sluzby/", [
        ("/cz/sluzby/seo-pre-ai-vyhledavace/", "AI viditelnost"),
        ("/cz/sluzby/seo-optimalizace/", "Google viditelnost"),
        ("/cz/sluzby/lodalne-seo/", "Google Mapy viditelnost"),
        ("/cz/sluzby/seo-pre-eshopy/", "SEO pro e-shopy"),
        ("/cz/sluzby/seo-audit/", "SEO audit a analýza"),
        ("/cz/sluzby/linkbuilding/", "Linkbuilding"),
    ])
    if market == "sk":
        rest = [("Cenník", "/sk/cennik/"), ("Ako pracujeme", "/sk/jak-pracujeme/"),
                ("Prípady", "/sk/pripady/"), ("Blog", "/sk/blog/"), ("Kontakt", "/sk/kontakt/")]
    else:
        rest = [("Ceník", "/cz/cenik/"), ("Jak pracujeme", "/cz/jak-pracujeme/"),
                ("Případy", "/cz/pripady/"), ("Blog", "/cz/blog/"), ("Kontakt", "/cz/kontakt/")]
    return [svc] + rest


def cta_label(market: str) -> str:
    return {"sk": "Bezplatný hovor", "cz": "Bezplatný hovor"}[market]


def lang_toggle(market: str, path: str) -> str:
    """EN | SK | CZ toggle. path is the current page path WITHOUT market prefix.
    Falls back to the market root when the equivalent page does not exist there."""
    pairs = []
    for m, label in (("sk", "SK"), ("cz", "CZ")):
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
    nav = ""
    for item in nav_items(market):
        lbl, href = item[0], item[1]
        if len(item) > 2:
            dd = "".join('<li><a href="%s">%s</a></li>' % (u, n) for u, n in item[2])
            nav += ('<li class="nav-drop"><a href="%s" class="nav-drop-link">%s'
                    '<svg width="10" height="10" viewBox="0 0 10 10" fill="none" aria-hidden="true">'
                    '<path d="M2 4l3 3 3-3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>'
                    '</svg></a><ul class="nav-dropdown">%s</ul></li>') % (href, lbl, dd)
        else:
            nav += '<li><a href="%s">%s</a></li>' % (href, lbl)
    mob_nav = ""
    for item in nav_items(market):
        lbl, href = item[0], item[1]
        mob_nav += '<a href="%s">%s</a>' % (href, lbl)
        if len(item) > 2:
            mob_nav += "".join('<a href="%s" class="mob-sub">%s</a>' % (u, n) for u, n in item[2])
    phone = '<a href="%s" class="nav-phone">%s</a>' % (PHONE_TEL, PHONE_DISPLAY)

    asset = (prefix.rstrip("/") + "/") if prefix else ""
    # hreflang only on the market homepages (deep pages have no 1:1 equivalents;
    # per-URL alternates would claim pairs that do not exist)
    if path == "":
        alt_links = [f'<link rel="alternate" hreflang="{c}" href="{h}">' for c, h in
                     (("sk", BASE + "/"), ("cs", BASE + "/cz/"),
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
        {phone}
        <a href="{CAL}" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm">{cta_label(market)}</a>
        <button class="hamburger" id="hamburger" aria-label="Menu"><span></span><span></span><span></span></button>
      </div>
    </nav>
  </div>
</header>
<nav class="nav-mobile" id="nav-mobile">
  {mob_nav}
  <a href="{CAL}" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="margin-top:10px;">{cta_label(market)}</a>
  <a href="{PHONE_TEL}" class="mob-phone">{PHONE_DISPLAY}</a>
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
                        ("/sk/sluzby/linkbuilding/", "Linkbuilding")]),
            ("Partneri", [("https://flamia.studio", "Flamia Studio: web dizajn"),
                          ("https://peterkocur.sk", "Peter Kocur: PPC reklama")]),
            ("Agentúra", [("/sk/jak-pracujeme/", "Ako pracujeme"),
                          ("/sk/cennik/", "Cenník"),
                          ("/sk/pripady/", "Prípadové štúdie"),
                          ("/sk/o-nas/", "O nás"),
                          ("/sk/blog/", "Blog"),
                          ("/sk/faq/", "FAQ")]),
            ("Kontakt", [(f"mailto:{EMAIL}", EMAIL),
                         (PHONE_TEL, PHONE_DISPLAY),
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
                        ("/cz/sluzby/linkbuilding/", "Linkbuilding")]),
            ("Partneři", [("https://flamia.studio", "Flamia Studio: web dizajn"),
                          ("https://peterkocur.sk", "Peter Kocur: PPC reklama")]),
            ("Agentura", [("/cz/jak-pracujeme/", "Jak pracujeme"),
                          ("/cz/cenik/", "Ceník"),
                          ("/cz/pripady/", "Případové studie"),
                          ("/cz/blog/", "Blog"),
                          ("/cz/faq/", "FAQ")]),
            ("Kontakt", [(f"mailto:{EMAIL}", EMAIL),
                         (PHONE_TEL, PHONE_DISPLAY),
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
    if market == "cz":
        foot_intro = "SEO agentura pro podnikatele. Google, Google Mapy, AI vyhledávače a e-shopy. Měřitelné výsledky za transparentních 12 EUR / hodinu."
        foot_copy = "© 2026 Nokto Studio. SEO pro Česko i Slovensko."
        foot_tagline = "Vytvořeno rychle, měřitelně a bez pevných smluv."
    else:
        foot_intro = "SEO agentúra pre podnikateľov. Google, Google Mapy, AI vyhľadávače a e-shopy. Merateľné výsledky za transparentných 12 EUR / hodinu."
        foot_copy = "© 2026 Nokto Studio. SEO pre Slovensko a Česko."
        foot_tagline = "Vytvorené rýchlo, merateľné a bez pevných zmlúv."
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
        <p>{foot_intro}</p>
      </div>
      {foot_cols}
    </div>
    <div class="footer-bottom">
      <span>{foot_copy}</span>
      <span>{foot_tagline}</span>
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
  "description": "SEO agentúra pre podnikateľov. AI viditeľnosť, Google viditeľnosť a viditeľnosť v Google Mapách. SEO pre e-shopy, audity a linkbuilding. Hodinová cena 12 EUR.",
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


ORG_SCHEMA_CZ = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "{BASE}/#organization",
  "name": "Nokto Studio",
  "url": "{BASE}/",
  "logo": "{BASE}/assets/img/favicon.svg",
  "description": "SEO agentura pro podnikatele. AI viditelnost, Google viditelnost a viditelnost v Google Mapách. SEO pro e-shopy, audity a linkbuilding. Hodinová cena 12 EUR.",
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
