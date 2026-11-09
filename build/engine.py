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
PHONE_DISPLAY = "+421 917 316 105"
PHONE_TEL = "tel:+421917316105"
KONTAKT_LINK = {"sk": "/sk/kontakt/", "cz": "/cz/kontakt/", "en": "/en/contact/"}
EMAIL = "hello@noktostudio.com"

# og:locale per market (used in the head template)
OG_LOCALE = {"sk": "sk_SK", "cz": "cs_CZ", "en": "en_US"}

# Google logo letters: N(blue) o(red) k(yellow) t(green)
LOGO = ('<span class="logo-n">N</span><span class="logo-o">o</span>'
        '<span class="logo-k">k</span><span class="logo-t">t</span>o Studio')


MARKET_ROOTS = {"sk": "/sk/", "cz": "/cz/", "en": "/en/"}   # subpage roots
MARKET_HOME = {"sk": "/", "cz": "/cz/", "en": "/en/"}       # brand home

# Paths that exist per market (used by the language toggle to avoid 404s).
SK_PATHS = {
    "", "sluzby/", "sluzby/seo-optimalizacia/", "sluzby/lodalne-seo/",
    "sluzby/seo-pre-ai-vyhladavace/", "sluzby/seo-pre-eshopy/", "sluzby/seo-audit/",
    "sluzby/seo-pre-wordpress/",
    "sluzby/linkbuilding/", "cennik/", "jak-pracujeme/", "vysledky/",
    "villa-paris/", "faq/", "o-nas/", "kontakt/", "blog/", "privacy/", "terms/",
    "blog/seo-pre-eshop/", "blog/seo-audit-co-to-je/",
}
CZ_PATHS = {
    "", "sluzby/", "sluzby/seo-optimalizace/", "sluzby/lodalne-seo/",
    "sluzby/seo-pre-ai-vyhledavace/", "sluzby/seo-pre-eshopy/", "sluzby/seo-audit/",
    "sluzby/seo-pre-wordpress/",
    "sluzby/linkbuilding/", "cenik/", "jak-pracujeme/", "vysledky/", "faq/", "kontakt/", "blog/",
    "privacy/", "terms/",
    "blog/seo-pro-eshop/", "blog/seo-audit-co-to-je/",
}
EN_PATHS = {
    "", "services/", "pricing/", "about/", "contact/", "faq/", "blog/", "portfolio/",
    "villa-paris/", "privacy/", "terms/",
    "blog/ecommerce-seo/", "blog/seo-audit-guide/",
}
LANG_PATHS = {"sk": SK_PATHS, "cz": CZ_PATHS, "en": EN_PATHS}

# SK <-> CZ hreflang pairs. Every SK path here has a 1:1 CZ equivalent.
# Paths missing from this map (villa-paris/, o-nas/) get self-canonical only.
HREFLANG_PAIR = {
    "": "",
    "cennik/": "cenik/",
    "cenik/": "cennik/",
    "sluzby/": "sluzby/",
    "sluzby/seo-optimalizacia/": "sluzby/seo-optimalizace/",
    "sluzby/seo-optimalizace/": "sluzby/seo-optimalizacia/",
    "sluzby/lodalne-seo/": "sluzby/lodalne-seo/",
    "sluzby/seo-pre-ai-vyhladavace/": "sluzby/seo-pre-ai-vyhledavace/",
    "sluzby/seo-pre-ai-vyhledavace/": "sluzby/seo-pre-ai-vyhladavace/",
    "sluzby/seo-pre-eshopy/": "sluzby/seo-pre-eshopy/",
    "sluzby/seo-audit/": "sluzby/seo-audit/",
    "sluzby/seo-pre-wordpress/": "sluzby/seo-pre-wordpress/",
    "sluzby/linkbuilding/": "sluzby/linkbuilding/",
    "jak-pracujeme/": "jak-pracujeme/",
    "vysledky/": "vysledky/",
    "faq/": "faq/",
    "o-nas/": None,
    "kontakt/": "kontakt/",
    "blog/": "blog/",
    "privacy/": "privacy/",
    "terms/": "terms/",
    "blog/seo-pre-eshop/": "blog/seo-pro-eshop/",
    "blog/seo-pro-eshop/": "blog/seo-pre-eshop/",
    "blog/seo-audit-co-to-je/": "blog/seo-audit-co-to-je/",
}


# SK path -> EN path. Only SK paths with a real EN page get an EN alternate
# (the EN market is a core-pages mirror; service subpages live on one EN hub).
EN_PAIR = {
    "": "",
    "sluzby/": "services/",
    "cennik/": "pricing/",
    "kontakt/": "contact/",
    "o-nas/": "about/",
    "faq/": "faq/",
    "blog/": "blog/",
    "vysledky/": "portfolio/",
    "villa-paris/": "villa-paris/",
    "privacy/": "privacy/",
    "terms/": "terms/",
    "blog/seo-pre-eshop/": "blog/ecommerce-seo/",
    "blog/seo-audit-co-to-je/": "blog/seo-audit-guide/",
}
EN_PAIR_REV = {v: k for k, v in EN_PAIR.items()}


def _market_url(m: str, sub: str) -> str:
    """Absolute URL of a page inside market m. sub == '' means market home."""
    return BASE + (MARKET_HOME[m] if sub == "" else MARKET_ROOTS[m] + sub)


_HFLANG_CODE = {"sk": "sk", "cz": "cs", "en": "en"}


def hreflang_links(market: str, path: str) -> str:
    """Three-language hreflang (SK, CS, EN) for pages with equivalents in at
    least one other language. x-default points to the SK version (primary
    market). Single-language pages stay self-canonical only."""
    if market == "en":
        sk_path = EN_PAIR_REV.get(path)
    elif market == "sk":
        sk_path = path
    else:
        sk_path = HREFLANG_PAIR.get(path)
    if sk_path is None or (sk_path != "" and sk_path not in SK_PATHS):
        return ""
    subs = {"sk": sk_path,
            "cz": HREFLANG_PAIR.get(sk_path),
            "en": EN_PAIR.get(sk_path)}
    subs = {m: s for m, s in subs.items() if s is not None}
    if len(subs) < 2:
        return ""
    links = [f'<link rel="alternate" hreflang="{_HFLANG_CODE[m]}" href="{_market_url(m, subs[m])}">'
             for m in ("sk", "cz", "en") if m in subs]
    links.append(f'<link rel="alternate" hreflang="x-default" href="{_market_url("sk", sk_path)}">')
    return "\n  ".join(links)


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
    "code":   '<path d="m8 8-4 4 4 4"/><path d="m16 8 4 4-4 4"/><path d="m13 6-2 12"/>',
}

def gicon(kind: str, color: str = "#6A3FC4", size: int = 24) -> str:
    """Material-style line icon, Google colors only, no emoji."""
    path = _GICON_PATHS[kind]
    return (f'<span class="gicon" style="color:{color};width:{size}px;height:{size}px;" aria-hidden="true">'
            f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="currentColor" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{path}</svg></span>')


# ---------------------------------------------------------------- navs

def nav_items(market: str) -> list[tuple[str, str]]:
    """(label, href) pairs for the desktop nav. Href uses {{p}} placeholders? No: plain."""
    if market == "sk":
        svc = ("Služby", "/sk/sluzby/", [
            ("/sk/sluzby/seo-pre-ai-vyhladavace/", "AI viditeľnosť"),
            ("/sk/sluzby/seo-optimalizacia/", "Google viditeľnosť"),
            ("/sk/sluzby/lodalne-seo/", "Google Mapy viditeľnosť"),
            ("/sk/sluzby/seo-pre-eshopy/", "SEO pre e-shopy"),
            ("/sk/sluzby/seo-pre-wordpress/", "SEO pre WordPress"),
            ("/sk/sluzby/seo-audit/", "SEO audit a analýza"),
            ("/sk/sluzby/linkbuilding/", "Linkbuilding"),
        ])
        rest = [("Cenník", "/sk/cennik/"), ("Ako pracujem", "/sk/jak-pracujeme/"),
                ("Výsledky", "/sk/vysledky/"), ("Blog", "/sk/blog/"),
                ("Kontaktujte ma", "/sk/kontakt/")]
    elif market == "cz":
        svc = ("Služby", "/cz/sluzby/", [
            ("/cz/sluzby/seo-pre-ai-vyhledavace/", "AI viditelnost"),
            ("/cz/sluzby/seo-optimalizace/", "Google viditelnost"),
            ("/cz/sluzby/lodalne-seo/", "Google Mapy viditelnost"),
            ("/cz/sluzby/seo-pre-eshopy/", "SEO pro e-shopy"),
            ("/cz/sluzby/seo-pre-wordpress/", "SEO pro WordPress"),
            ("/cz/sluzby/seo-audit/", "SEO audit a analýza"),
            ("/cz/sluzby/linkbuilding/", "Linkbuilding"),
        ])
        rest = [("Ceník", "/cz/cenik/"), ("Jak pracuji", "/cz/jak-pracujeme/"),
                ("Výsledky", "/cz/vysledky/"), ("Blog", "/cz/blog/"),
                ("Kontaktujte mě", "/cz/kontakt/")]
    else:
        svc = ("Services", "/en/services/", [
            ("/en/services/#ai", "AI visibility"),
            ("/en/services/#seo", "Google visibility"),
            ("/en/services/#local", "Google Maps visibility"),
            ("/en/services/#eshop", "E-commerce SEO"),
            ("/en/services/#wordpress", "WordPress SEO"),
            ("/en/services/#audit", "SEO audit and analysis"),
            ("/en/services/#links", "Link building"),
        ])
        rest = [("Pricing", "/en/pricing/"), ("How I work", "/en/about/"),
                ("Results", "/en/portfolio/"), ("Blog", "/en/blog/"),
                ("Contact me", "/en/contact/")]
    return [svc] + rest


def cta_label(market: str) -> str:
    """Primary CTA label: the free audit offer, going to the contact form."""
    return {"sk": "Audit webu zdarma", "cz": "Audit webu zdarma", "en": "Free website audit"}[market]


GOOGLE_REVIEW = ("Šimon mi robil obsah na webovú stránku, články, produktový feed na e-shop "
                 "a SEO optimalizáciu. Oceňujem jeho proaktívny prístup, ochotu vysvetliť a "
                 "edukovať staršieho človeka, ktorý nemá taký prehľad v technológiách, a "
                 "výbornú spoluprácu, okamžité reakcie a férové ceny. Veľmi som spokojný "
                 "s poskytnutými službami.")


def google_review_band(market: str) -> str:
    """Real 5-star Google review, shown sitewide above the footer."""
    head = {"sk": "Čo hovoria klienti", "cz": "Co říkají klienti", "en": "What clients say"}[market]
    label = {"sk": "Google recenzia", "cz": "Google recenze", "en": "Google review"}[market]
    attr = {"sk": "Overená Google recenzia", "cz": "Ověřená Google recenze", "en": "Verified Google review"}[market]
    link_lbl = {"sk": "Google profile", "cz": "Google profilu", "en": "Google profile"}[market]
    more = {"sk": f"Viac recenzií na mojom <a href=\"https://www.google.com/maps/place/Nokto+Studio\" target=\"_blank\" rel=\"noopener\" style=\"font-weight:700; color:var(--brand-primary-deep);\">{link_lbl}</a>.",
            "cz": f"Více recenzí na mém <a href=\"https://www.google.com/maps/place/Nokto+Studio\" target=\"_blank\" rel=\"noopener\" style=\"font-weight:700; color:var(--brand-primary-deep);\">{link_lbl}</a>.",
            "en": f"More reviews on my <a href=\"https://www.google.com/maps/place/Nokto+Studio\" target=\"_blank\" rel=\"noopener\" style=\"font-weight:700; color:var(--brand-primary-deep);\">{link_lbl}</a>."}[market]
    return f"""
<section class="section section-alt">
  <div class="container">
    <div class="section-head" style="text-align:center;">
      <span class="section-label">{label}</span>
      <h2>{head}</h2>
    </div>
    <div style="max-width:720px; margin:0 auto;">
      <div class="benefit-card card-hover" style="padding:32px;">
        <div style="font-size:1.4rem; color:var(--brand-warm); letter-spacing:2px;">★★★★★</div>
        <p style="font-size:1.05rem; line-height:1.75; margin-top:14px; color:var(--text);">„{GOOGLE_REVIEW}"</p>
        <p style="margin-top:16px; font-weight:700; color:var(--text);">{attr}, 2026</p>
      </div>
      <p style="text-align:center; margin-top:20px; color:var(--text-muted); font-size:0.88rem;">{more}</p>
    </div>
  </div>
</section>
"""


def lang_toggle(market: str, path: str) -> str:
    """EN | SK | CZ toggle. Path-aware: links to the equivalent page in the
    target language when it exists, otherwise to that market's blog listing
    for blog posts and to that market's home otherwise. The active language
    always keeps the reader on the current page."""
    if market == "en":
        sk_path = EN_PAIR_REV.get(path, "")
    elif market == "sk":
        sk_path = path
    else:
        sk_path = HREFLANG_PAIR.get(path) or ""
    if sk_path and sk_path not in SK_PATHS:
        # SK-only pages (blog posts): fall back to the blog listing instead
        # of dumping the reader on a market home page.
        sk_path = "blog/" if path.startswith("blog/") else ""
    if sk_path and sk_path not in SK_PATHS:
        sk_path = ""
    pairs = []
    for m, label in (("sk", "SK"), ("cz", "CZ"), ("en", "EN")):
        if m == "sk":
            sub = sk_path
        elif m == "cz":
            sub = HREFLANG_PAIR.get(sk_path) if sk_path in HREFLANG_PAIR else ""
        else:
            sub = EN_PAIR.get(sk_path, "")
        if sub not in LANG_PATHS[m]:
            sub = ""
        href = _market_url(m, sub)
        if m == market:
            # active language: the button stays on the page being rendered
            href = _market_url(m, path)
        active = " active" if m == market else ""
        pairs.append(f'<a href="{href}" class="lang-btn{active}">{label}</a>')
    return '<div class="lang-toggle">' + ' <span>|</span> '.join(pairs) + "</div>"


# ---------------------------------------------------------------- base template

def base(*, market: str, path: str, title: str, desc: str, canonical: str,
         body: str, prefix: str, extra_head: str = "", h1: bool = True,
         og_type: str = "website") -> str:
    """Render one full page.

    market   : sk | cz | en
    path     : url path after the market root, e.g. 'sluzby/seo-optimalizacia/'
    canonical: full absolute URL
    prefix   : relative prefix for assets from this page, e.g. '../..' or ''
    """
    nav = ""
    root = {"sk": "/sk/", "cz": "/cz/", "en": "/en/"}[market]
    cur = (root + path).rstrip('/')
    for item in nav_items(market):
        lbl, href = item[0], item[1]
        if len(item) > 2:
            is_active = bool(path) and (cur + '/').startswith(href.rstrip('/') + '/')
            drop_cls = 'nav-drop-link active' if is_active else 'nav-drop-link'
            dd = "".join('<li><a href="%s">%s</a></li>' % (u, n) for u, n in item[2])
            nav += ('<li class="nav-drop"><a href="%s" class="%s">%s'
                    '<svg width="10" height="10" viewBox="0 0 10 10" fill="none" aria-hidden="true">'
                    '<path d="M2 4l3 3 3-3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>'
                    '</svg></a><ul class="nav-dropdown">%s</ul></li>') % (href, drop_cls, lbl, dd)
        else:
            is_active = path and cur == href.rstrip('/')
            if not is_active:
                seg = href.rstrip('/').split('/')[-1]
                is_active = bool(path) and path.rstrip('/').split('/')[0] == seg and seg not in ("", "en", "cz", "sk")
            cls = ' class="active"' if is_active else ''
            nav += '<li><a href="%s"%s>%s</a></li>' % (href, cls, lbl)
    mob_nav = ""
    for item in nav_items(market):
        lbl, href = item[0], item[1]
        mob_nav += '<a href="%s">%s</a>' % (href, lbl)
        if len(item) > 2:
            mob_nav += "".join('<a href="%s" class="mob-sub">%s</a>' % (u, n) for u, n in item[2])

    asset = (prefix.rstrip("/") + "/") if prefix else ""
    hreflang = hreflang_links(market, path)
    results_html = "" if ('id="vysledky"' in body or 'class="results-slider"' in body) else f"\n{results_slider(market)}\n"

    return f"""<!DOCTYPE html>
<html lang="{ {'sk':'sk','cz':'cs','en':'en'}[market] }">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{_html.escape(title)}</title>
  <meta name="description" content="{_html.escape(desc)}">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <meta property="og:type" content="{og_type}">
  <meta property="og:site_name" content="Nokto Studio">
  <meta property="og:locale" content="{OG_LOCALE[market]}">
  <meta property="og:title" content="{_html.escape(title)}">
  <meta property="og:description" content="{_html.escape(desc)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{BASE}/assets/img/og-cover.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{_html.escape(title)}">
  <meta name="twitter:description" content="{_html.escape(desc)}">
  <meta name="twitter:image" content="{BASE}/assets/img/og-cover.png">
  <meta name="theme-color" content="#ffffff">
  <link rel="canonical" href="{canonical}">
{hreflang}
  <meta name="msvalidate.01" content="3b43ea1af0ee49f082ab3c4e94ed5f4f">
  <meta name="google-site-verification" content="np1uzdVrceOrWA4HhduUl6JaUupw1as8DDwqcVg3sHs">
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
        <a href="{KONTAKT_LINK[market]}" class="btn btn-primary btn-sm nav-phone-btn">{cta_label(market)}</a>
        <button class="hamburger" id="hamburger" aria-label="Menu"><span></span><span></span><span></span></button>
      </div>
    </nav>
  </div>
</header>
<nav class="nav-mobile" id="nav-mobile">
  {mob_nav}
  <a href="{KONTAKT_LINK[market]}" class="btn btn-primary" style="margin-top:10px;">{cta_label(market)}</a>
</nav>

{body}
{results_html}
{google_review_band(market)}

{footer(market, prefix)}

<script src="{asset}assets/js/clarity.js"></script>
<script src="{asset}assets/js/ga4.js"></script>
<script src="{asset}assets/js/nav.js"></script>
<script src="{asset}assets/js/slider.js"></script>
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
                        ("/sk/sluzby/seo-pre-wordpress/", "SEO pre WordPress"),
                        ("/sk/sluzby/seo-audit/", "SEO audit a analýza"),
                        ("/sk/sluzby/linkbuilding/", "Linkbuilding")]),
            ("Partneri", [("https://flamia.studio", "Flamia Studio: web dizajn"),
                          ("https://peterkocur.sk", "Peter Kocur: PPC reklama")]),
            ("Agentúra", [("/sk/jak-pracujeme/", "Ako pracujem"),
                          ("/sk/cennik/", "Cenník"),
                          ("/sk/vysledky/", "Výsledky"),
                          ("/sk/o-nas/", "O nás"),
                          ("/sk/blog/", "Blog"),
                          ("/sk/faq/", "FAQ")]),
            ("Kontakt", [(f"mailto:{EMAIL}", EMAIL),
                         ("/sk/kontakt/", "Kontaktný formulár a telefón"),
                         ("/sk/privacy/", "Ochrana súkromia"),
                         ("/sk/terms/", "Obchodné podmienky")]),
        ]
    elif market == "cz":
        cols = [
            ("Služby", [("/cz/sluzby/seo-optimalizace/", "SEO optimalizace"),
                        ("/cz/sluzby/lodalne-seo/", "Lokální SEO a firemní profil"),
                        ("/cz/sluzby/seo-pre-ai-vyhledavace/", "SEO pro AI vyhledávače"),
                        ("/cz/sluzby/seo-pre-eshopy/", "SEO pro e-shopy"),
                        ("/cz/sluzby/seo-pre-wordpress/", "SEO pro WordPress"),
                        ("/cz/sluzby/seo-audit/", "SEO audit a analýza"),
                        ("/cz/sluzby/linkbuilding/", "Linkbuilding")]),
            ("Partneři", [("https://flamia.studio", "Flamia Studio: web dizajn"),
                          ("https://peterkocur.sk", "Peter Kocur: PPC reklama")]),
            ("Agentura", [("/cz/jak-pracujeme/", "Jak pracuji"),
                          ("/cz/cenik/", "Ceník"),
                          ("/cz/vysledky/", "Výsledky"),
                          ("/cz/blog/", "Blog"),
                          ("/cz/faq/", "FAQ")]),
            ("Kontakt", [(f"mailto:{EMAIL}", EMAIL),
                         ("/cz/kontakt/", "Kontaktní formulář a telefon"),
                         ("/cz/privacy/", "Zásady ochrany osobních údajů"),
                         ("/cz/terms/", "Obchodní podmínky")]),
        ]
    else:
        cols = [
            ("Services", [("/en/services/#seo", "SEO optimization"),
                          ("/en/services/#local", "Local SEO and Business Profile"),
                          ("/en/services/#ai", "SEO for AI search engines"),
                          ("/en/services/#eshop", "E-commerce SEO"),
                          ("/en/services/#wordpress", "WordPress SEO"),
                          ("/en/services/#audit", "SEO audit and analysis"),
                          ("/en/services/#links", "Link building")]),
            ("Partners", [("https://flamia.studio", "Flamia Studio: web design"),
                          ("https://peterkocur.sk", "Peter Kocur: PPC advertising")]),
            ("Agency", [("/en/about/", "How I work"),
                        ("/en/pricing/", "Pricing"),
                        ("/en/portfolio/", "Results"),
                        ("/en/blog/", "Blog"),
                        ("/en/faq/", "FAQ")]),
            ("Contact", [(f"mailto:{EMAIL}", EMAIL),
                         ("/en/contact/", "Contact form and phone"),
                         ("/en/privacy/", "Privacy"),
                         ("/en/terms/", "Terms")]),
        ]
    if market == "en":
        foot_intro = "SEO for business owners by Šimon Štermenský: website content, technical SEO and your Google Business Profile. Measurable results at a transparent 12 EUR / hour."
        foot_copy = "© 2026 Nokto Studio. SEO in English for European businesses."
        foot_tagline = "I do it myself: fast, measurable, without lock-in contracts."
    elif market == "cz":
        foot_intro = "SEO pro podnikatele od Šimona Štermenského: obsah webu, technika webu a firemní profil Google. Měřitelné výsledky za transparentních 12 EUR / hodinu."
        foot_copy = "© 2026 Nokto Studio. SEO pro Česko i Slovensko."
        foot_tagline = "Dělám to sám, rychle, měřitelně a bez pevných smluv."
    else:
        foot_intro = "SEO pre podnikateľov od Šimona Štermenského: obsah webu, technika webu a Google firemný profil. Merateľné výsledky za transparentných 12 EUR/hodinu."
        foot_copy = "© 2026 Nokto Studio. SEO pre Slovensko a Česko."
        foot_tagline = "Robím to sám, rýchlo, merateľne a bez pevných zmlúv."
    foot_cols = ""
    for title, links in cols:
        links_html = "".join(f'<a href="{h}">{t}</a>' for h, t in links)
        foot_cols += f'<div class="footer-col"><h4>{title}</h4>{links_html}</div>'
    # Sesterské weby: the niche satellite sites (reciprocal link, they link back).
    sisters_label, sisters = {
        "sk": ("Špecializované weby", [
            ("https://seopreeshopy.pro/", "SEO pre e-shopy"),
            ("https://seoaudit.blog/", "SEO audity"),
            ("https://seoprewordpress.info/", "SEO pre WordPress")]),
        "cz": ("Specializované weby", [
            ("https://seopreeshopy.pro/cz/", "SEO pro e-shopy"),
            ("https://seoaudit.blog/cz/", "SEO audity"),
            ("https://seoprewordpress.info/cz/", "SEO pro WordPress")]),
        "en": ("Specialised sites", [
            ("https://seopreeshopy.pro/", "SEO for e-shops"),
            ("https://seoaudit.blog/", "SEO audits"),
            ("https://seoprewordpress.info/", "SEO for WordPress")]),
    }[market]
    sisters_html = ' <span style="color:var(--text-muted);">·</span> '.join(
        f'<a href="{u}">{t}</a>' for u, t in sisters)
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
    <p class="footer-sisters" style="margin:18px 0 0; font-size:0.9rem; color:var(--text-muted);"><span style="font-weight:600;">{sisters_label}:</span> {sisters_html}</p>
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
    btn = cta_label(market)
    audit_href = {"sk": "/sk/kontakt/?audit=1", "cz": "/cz/kontakt/?audit=1", "en": "/en/contact/?audit=1"}[market]
    return f"""
<div class="cta-band">
  <div>
    <h2>{title}</h2>
    <p>{text}</p>
  </div>
  <div class="hero-ctas">
    <a href="{audit_href}" class="btn btn-white btn-lg">{btn}</a>
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


def related_block(market: str, articles=None, services=None, heading: str | None = None) -> str:
    """Internal linking block: related blog articles + related service pages.

    articles / services: list of (href, label). Renders one grid of cards with
    a tag per card type. Used on service pages and blog posts to spread link
    equity between the money pages and the content cluster.
    """
    if not articles and not services:
        return ""
    L = {
        "sk": dict(label="Súvisiace", head="Súvisiace články a služby", article="Článok", service="Služba"),
        "cz": dict(label="Související", head="Související články a služby", article="Článek", service="Služba"),
        "en": dict(label="Related", head="Related reading", article="Article", service="Service"),
    }[market]
    cards = ""
    for u, t in (articles or []):
        cards += (f'<div class="benefit-card card-hover related-card">'
                  f'<span class="project-tags"><span class="project-tag tag-violet">{L["article"]}</span></span>'
                  f'<h3><a href="{u}" style="color:var(--text);">{t}</a></h3></div>')
    for u, t in (services or []):
        cards += (f'<div class="benefit-card card-hover related-card">'
                  f'<span class="project-tags"><span class="project-tag tag-cerulean">{L["service"]}</span></span>'
                  f'<h3><a href="{u}" style="color:var(--text);">{t}</a></h3></div>')
    return f"""
<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="section-head"><span class="section-label">{L["label"]}</span><h2>{heading or L["head"]}</h2></div>
    <div class="grid-3">{cards}</div>
  </div>
</section>
"""


def article_schema(*, url: str, title: str, desc: str, date_iso: str,
                   lang: str = "sk") -> str:
    """BlogPosting JSON-LD for a blog post. References the Organization by @id,
    so the publisher block is defined once in ORG_SCHEMA."""
    lang_name = {"sk": "Šimon Štermenský", "cz": "Šimon Štermenský", "en": "Simon Stremensky"}[lang]
    about_url = {"sk": "/sk/o-nas/", "cz": "/cz/", "en": "/en/about/"}[lang]
    return (
        '<script type="application/ld+json">\n'
        f'{{"@context":"https://schema.org","@type":"BlogPosting","@id":"{url}#article",'
        f'"mainEntityOfPage":{{"@type":"WebPage","@id":"{url}"}},'
        f'"headline":{_json_str(title)},"description":{_json_str(desc)},'
        f'"datePublished":"{date_iso}","dateModified":"{date_iso}",'
        f'"author":{{"@type":"Person","name":{_json_str(lang_name)},"url":"{BASE}{about_url}"}},'
        f'"publisher":{{"@id":"{BASE}/#organization"}},'
        f'"url":"{url}","image":"{BASE}/assets/img/og-cover.png","inLanguage":"{_HFLANG_CODE[lang]}"}}\n'
        "</script>"
    )


def _json_str(s: str) -> str:
    import json
    return json.dumps(s, ensure_ascii=False)


def price_cards(cards: list[dict], market: str) -> str:
    """cards: [{name, hours, price, featured, badge, items[], cta}]

    The retainer price is shown as the headline number; the hours line stays
    honest when a rounded price covers slightly more than whole hours.
    """
    default_badge = {"sk": "Najčastejšia voľba", "cz": "Nejčastější volba", "en": "Most popular"}[market]
    btn_label = {"sk": "Nezáväznú ponuku", "cz": "Nezávaznou nabídku", "en": "Get a quote"}[market]
    period = {"sk": "mesiac", "cz": "měsíc", "en": "month"}[market]
    work = {"sk": "práce / mesiac", "cz": "práce / měsíc", "en": "hours of work / month"}[market]
    out = []
    for c in cards:
        feat = " featured" if c.get("featured") else ""
        badge = ""
        if c.get("featured"):
            badge = f'<span class="price-badge">{c.get("badge", default_badge)}</span>'
        lis = "".join(f"<li>{i}</li>" for i in c["items"])
        hours_label = f"{c['hours']} h"
        breakdown_html = f'<div style="font-size:0.8rem; color:var(--text-muted); margin-top:-14px; margin-bottom:16px;">{c["breakdown"]}</div>' if c.get("breakdown") else ''
        out.append(f"""
<div class="price-card{feat}">
  {badge}<span class="price-hours">{c['name']}</span>
  <div class="price-amount">{c['price']}<small> EUR / {period}</small></div>
  <div class="price-monthly"><strong>{hours_label}</strong> {work}</div>
  {breakdown_html}<ul>{lis}</ul>
  <a href="{KONTAKT_LINK[market]}" class="btn btn-primary">{btn_label}</a>
</div>""")
    return f'<div class="pricing-grid">{"".join(out)}</div>'


def steps_block(steps: list[dict]) -> str:
    nums = ["num-violet", "num-orange", "num-cerulean", "num-violet-light"]
    out = []
    for i, s in enumerate(steps):
        out.append(f"""
<div class="step">
  <span class="step-num {nums[i % 4]}">{i + 1}</span>
  <h3>{s['title']}</h3>
  <p>{s['text']}</p>
</div>""")
    return f'<div class="steps">{"".join(out)}</div>'


# ---------------------------------------------------------------- results slider
# Real numbers taken from client Google Search Console / Google AI Mode
# screenshots (Sep 2026). Charts are inline SVG, Google palette, no JS chart lib.

_VIOLET, _ORANGE, _CERULEAN, _VIOLET_L = "#7A50D6", "#F75940", "#1DACD6", "#9B6FD9"


def _sparkline(points: list[int], color: str, w: int = 560, h: int = 120, pad: int = 10) -> str:
    """Simple rising sparkline SVG from integer series."""
    n = len(points)
    lo, hi = min(points), max(points)
    rng = (hi - lo) or 1
    step = (w - 2 * pad) / max(n - 1, 1)
    coords = []
    for i, v in enumerate(points):
        x = pad + i * step
        y = h - pad - (v - lo) / rng * (h - 2 * pad)
        coords.append(f"{x:.1f},{y:.1f}")
    poly = " ".join(coords)
    area = f"{pad},{h - pad} " + poly + f" {w - pad},{h - pad}"
    return (f'<svg viewBox="0 0 {w} {h}" role="img" aria-hidden="true" preserveAspectRatio="none">'
            f'<polygon points="{area}" fill="{color}" opacity="0.12"/>'
            f'<polyline points="{poly}" fill="none" stroke="{color}" stroke-width="3" '
            f'stroke-linecap="round" stroke-linejoin="round"/></svg>')


def _bars(values: list[int], color: str, labels: list[str] | None = None,
          w: int = 560, h: int = 140, pad: int = 18) -> str:
    """Vertical bar chart SVG with optional labels under bars."""
    n = len(values)
    hi = max(values) or 1
    slot = (w - 2 * pad) / n
    bw = min(slot * 0.6, 64)
    rects, texts = [], []
    for i, v in enumerate(values):
        bh = (v / hi) * (h - pad * 2 - 18)
        x = pad + i * slot + (slot - bw) / 2
        y = h - pad - 18 - bh
        rects.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="4" '
                     f'fill="{color}" opacity="{0.45 if i < n - 1 else 1.0}"/>')
        if labels:
            texts.append(f'<text x="{x + bw / 2:.1f}" y="{h - 4}" text-anchor="middle" '
                         f'font-size="11" fill="#5F6368" font-family="Manrope,sans-serif">{labels[i]}</text>')
    return (f'<svg viewBox="0 0 {w} {h}" role="img" aria-hidden="true">'
            + "".join(rects) + "".join(texts) + "</svg>")


def _donut(parts: list[tuple[int, str, str]], w: int = 160, h: int = 160) -> str:
    """Donut chart from (value, color) pairs. Used for the local GBP split."""
    total = sum(v for v, _c, _l in parts) or 1
    r, cx, cy = 60, 80, 80
    circ = 2 * 3.14159 * r
    segs, offset = [], 0.0
    for v, color, _label in parts:
        frac = v / total
        dash = frac * circ
        segs.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" '
                    f'stroke-width="24" stroke-dasharray="{dash:.1f} {circ - dash:.1f}" '
                    f'stroke-dashoffset="{-offset:.1f}" transform="rotate(-90 {cx} {cy})"/>')
        offset += dash
    return (f'<svg viewBox="0 0 {w} {h}" width="200" height="200" role="img" aria-hidden="true" '
            f'style="width:200px;height:200px;display:block;margin:0 auto;">{"".join(segs)}</svg>')


def _slide(client: str, chip: str, period: str, nums: list[dict], chart: str,
           caption: str, market: str, logo: str = "") -> str:
    """One slider slide. nums: [{big, color, label}]"""
    num_html = "".join(
        f'<div class="rs-num"><strong style="color:{n["color"]};">{n["big"]}</strong>'
        f'<span>{n["label"]}</span></div>' for n in nums)
    client_lbl = {"sk": client, "cz": client, "en": client}[market]
    source = {"sk": "Google Search Console", "cz": "Google Search Console", "en": "Google Search Console"}[market]
    logo_html = (f'<img src="/assets/img/logos/{logo}" alt="{client_lbl}" loading="lazy" '
                 f'style="height:34px; width:auto; object-fit:contain;">') if logo else         f'<span class="rs-chip">{chip}</span>'
    return f"""
<div class="rs-slide">
  <div class="rs-card">
    <div class="rs-head">
      <div><h3>{client_lbl}</h3><span class="rs-period">{period}</span></div>
      {logo_html}
    </div>
    <div class="rs-chart">{chart}</div>
    <div class="rs-nums">{num_html}</div>
    <p class="rs-caption">{caption}</p>
    <p class="rs-source">Zdroj: {source}</p>
  </div>
</div>"""


def partner_logo_card(href: str, logo: str, title: str, text: str, delay: int = 100) -> str:
    """Partner card with a real logo image instead of an icon."""
    ext = ' target="_blank" rel="noopener noreferrer"'
    return f"""
<div class="benefit-card card-hover reveal" data-delay="{delay}">
  <img src="/assets/img/logos/{logo}" alt="{title}" loading="lazy"
       style="height:42px; width:auto; max-width:80%; object-fit:contain; margin-bottom:14px;">
  <h3><a href="{href}"{ext} style="color:var(--text);">{title}</a></h3>
  <p>{text}</p>
  <div class="project-tags"><span class="project-tag tag-violet">Partner</span></div>
</div>"""


def result_block(*, title: str, period: str, nums: list[dict], chart: str,
                 caption: str, source: str, partner: str = "", market: str = "sk") -> str:
    """One results-page project card with a chart.

    partner: '' (no chip), 'own' (own project chip) or 'flamia'
    (cooperation chip linking to Flamia Studio)."""
    chips = {
        "own": {"sk": "Vlastný projekt", "cz": "Vlastní projekt", "en": "Own project"},
        "flamia": {"sk": "s Flamia Studio", "cz": "s Flamia Studio", "en": "with Flamia Studio"},
    }
    tag_cls = {"own": "tag-violet-light", "flamia": "tag-violet"}
    if partner:
        chip_txt = chips[partner][market]
        if partner == "flamia":
            chip_html = (f'<span class="project-tag {tag_cls[partner]}">'
                         f'<a href="https://flamia.studio" target="_blank" rel="noopener noreferrer" '
                         f'style="color:inherit;">{chip_txt}</a></span>')
        else:
            chip_html = f'<span class="project-tag {tag_cls[partner]}">{chip_txt}</span>'
    else:
        chip_html = ""
    num_html = "".join(
        f'<div class="rs-num"><strong style="color:{n["color"]};">{n["big"]}</strong>'
        f'<span>{n["label"]}</span></div>' for n in nums)
    chart_html = f'<div class="rs-chart">{chart}</div>' if chart else ""
    owner_html = chip_html + " " if chip_html else ""
    return f"""
<div class="project-card card-hover">
  <div class="project-card-body">
    <div class="rs-head">
      <div><h3>{title}</h3><span class="rs-period">{period}</span></div>
      {owner_html}
    </div>
    {chart_html}
    <div class="rs-nums">{num_html}</div>
    <p>{caption}</p>
    <p class="rs-source">Zdroj: {source}</p>
  </div>
</div>"""


def _screenshot_chart(gsc_img: str, ai_img: str, client_lbl: str, market: str) -> str:
    """Two-column screenshot comparison: Google Search Console + AI Visibility."""
    lbl_gsc = {"sk": "Google Vyhľadávanie (Search Console)",
               "cz": "Google Vyhledávání (Search Console)",
               "en": "Google Search (Search Console)"}[market]
    lbl_ai = {"sk": "AI Viditeľnosť (Google AI funkcie)",
              "cz": "AI Viditelnost (Google AI funkce)",
              "en": "AI Visibility (Google AI features)"}[market]
    return f"""
<div class="rs-shot-grid">
  <div class="rs-shot-box">
    <div class="rs-shot-label"><span class="dot dot-blue"></span> {lbl_gsc}</div>
    <img src="/assets/img/results/{gsc_img}" alt="{lbl_gsc}: {client_lbl}" loading="lazy" class="rs-shot-img">
  </div>
  <div class="rs-shot-box">
    <div class="rs-shot-label"><span class="dot dot-violet"></span> {lbl_ai}</div>
    <img src="/assets/img/results/{ai_img}" alt="{lbl_ai}: {client_lbl}" loading="lazy" class="rs-shot-img">
  </div>
</div>"""


def results_slider(market: str) -> str:
    """Slider of real client results (GSC + AI Mode screenshots, Nov 2026)."""
    t = {
        "sk": {
            "label": "Overené výsledky klientov",
            "head": "Google Vyhľadávanie aj AI viditeľnosť v praxi",
            "sub": "Skutočné screenshoty z Google Search Console a AI prehľadov našich klientov. Overené čísla z praxe, žiadne vymyslené makety.",
            "chip1": "Obsah + AI viditeľnosť",
            "chip2": "Rast za 2 mesiace",
            "chip3": "Nový web od nuly",
            "chip4": "Veľký objem + AI líder",
            "chip5": "Týždenný rast",
            "prev": "Predchádzajúci", "next": "Nasledujúci", "all": "Všetky výsledky",
            "case_url": "/sk/vysledky/",
        },
        "cz": {
            "label": "Ověřená data klientů",
            "head": "Google Vyhledávání i AI viditelnost v praxi",
            "sub": "Skutečné screenshoty z Google Search Console a AI přehledů našich klientů. Ověřená čísla z praxe, žádné vymyšlené makety.",
            "chip1": "Obsah + AI viditelnost",
            "chip2": "Růst za 2 měsíce",
            "chip3": "Nový web od nuly",
            "chip4": "Velký objem + AI lídr",
            "chip5": "Týdenní růst",
            "prev": "Předchozí", "next": "Další", "all": "Všechny výsledky",
            "case_url": "/cz/vysledky/",
        },
        "en": {
            "label": "Verified Client Results",
            "head": "Google Search and AI Visibility in Practice",
            "sub": "Actual screenshots from Google Search Console and AI Overview reports of our clients. Real data, zero stock mockups.",
            "chip1": "Content + AI visibility",
            "chip2": "2-month growth",
            "chip3": "New site from zero",
            "chip4": "High volume + AI leader",
            "chip5": "Weekly growth",
            "prev": "Previous", "next": "Next", "all": "All results",
            "case_url": "/en/portfolio/",
        },
    }[market]

    # Slide 1: 174k impressions / 2.01k clicks / 2.4k AI
    c1_title = {"sk": "E-shop a obsahový portál", "cz": "E-shop a obsahový portál", "en": "E-commerce and content portal"}[market]
    c1_period = {"sk": "12 mesiacov v Google Vyhľadávaní · 6 mesiacov v AI", "cz": "12 měsíců v Google Vyhledávání · 6 měsíců v AI", "en": "12 months in Google Search · 6 months in AI"}[market]
    chart1 = _screenshot_chart("client1-gsc-search.png", "client1-ai-overview.png", c1_title, market)
    s1 = _slide(
        c1_title,
        t["chip1"],
        c1_period,
        [{"big": "174 tis.", "color": _VIOLET, "label": {"sk": "zobrazení v Google za 12 mesiacov", "cz": "zobrazení v Google za 12 měsíců", "en": "impressions in Google (12 mo)"}[market]},
         {"big": "2 010", "color": _CERULEAN, "label": {"sk": "klikov z organického Google", "cz": "kliků z organického Google", "en": "clicks from organic Google"}[market]},
         {"big": "2 400", "color": _ORANGE, "label": {"sk": "zobrazení v generatívnej AI", "cz": "zobrazení v generativní AI", "en": "generative AI impressions"}[market]}],
        chart1,
        {"sk": "Dlhodobý rast organického vyhľadávania po nasadení nového obsahu a technickej štruktúry. Google prináša stabilné tisíce klikov a generatívna AI začala web masívne citovať s nárastom na 2 400 zobrazení.",
         "cz": "Dlouhodobý růst organického vyhledávání po nasazení nového obsahu a technické struktury. Google přináší stabilní tisíce kliků a generativní AI začala web masivně citovat s nárůstem na 2 400 zobrazení.",
         "en": "Long-term organic growth driven by fresh content and clean architecture. Google delivers thousands of search clicks while AI answer engines cite the site with 2.4K impressions."}[market],
        market)

    # Slide 2: 8.75k impressions / 339 clicks / 528 AI
    c2_title = {"sk": "B2B klient a špecializované služby", "cz": "B2B klient a specializované služby", "en": "B2B client and specialized services"}[market]
    c2_period = {"sk": "September až november 2026", "cz": "Září až listopad 2026", "en": "September to November 2026"}[market]
    chart2 = _screenshot_chart("client2-gsc-search.png", "client2-ai-overview.png", c2_title, market)
    s2 = _slide(
        c2_title,
        t["chip2"],
        c2_period,
        [{"big": "8 750", "color": _VIOLET, "label": {"sk": "zobrazení za 2 mesiace", "cz": "zobrazení za 2 měsíce", "en": "impressions in 2 months"}[market]},
         {"big": "339", "color": _CERULEAN, "label": {"sk": "klikov z Google (CTR 3,9 %)", "cz": "kliků z Google (CTR 3,9 %)", "en": "clicks from Google (CTR 3.9%)"}[market]},
         {"big": "528", "color": _ORANGE, "label": {"sk": "zobrazení v AI po zlomovom bode", "cz": "zobrazení v AI po zlomovém bodě", "en": "AI impressions after inflection point"}[market]}],
        chart2,
        {"sk": "Nábeh po nasadení optimalizácie kategórií a služieb. Zlom prišiel koncom októbra, kde sa prejavili indexované dopyty a web začal prudko nabiehať aj v AI prehľadoch (takmer 40 zobrazení denne).",
         "cz": "Náběh po nasazení optimalizace kategorií a služeb. Zlom přišel koncem října, kdy se projevily indexované dotazy a web začal prudce nabíhat i v AI přehledech (téměř 40 zobrazení denně).",
         "en": "Rapid acceleration after category and service optimization. Late October marked the turning point as indexed queries spiked in both Google Search and AI Overviews."}[market],
        market)

    # Slide 3: 718 impressions / 9 clicks / 306 AI
    c3_title = {"sk": "Nový klientsky projekt (štart od nuly)", "cz": "Nový klientský projekt (start od nuly)", "en": "New client project (launch from zero)"}[market]
    c3_period = {"sk": "Posledné 3 mesiace (od augusta 2026)", "cz": "Poslední 3 měsíce (od srpna 2026)", "en": "Last 3 months (since August 2026)"}[market]
    chart3 = _screenshot_chart("client3-gsc-search.png", "client3-ai-overview.png", c3_title, market)
    s3 = _slide(
        c3_title,
        t["chip3"],
        c3_period,
        [{"big": "718", "color": _VIOLET, "label": {"sk": "zobrazení v Google od spustenia", "cz": "zobrazení v Google od spuštění", "en": "impressions since launch"}[market]},
         {"big": "8,2", "color": _CERULEAN, "label": {"sk": "priemerná pozícia v Google", "cz": "průměrná pozice v Google", "en": "average position in Google"}[market]},
         {"big": "306", "color": _ORANGE, "label": {"sk": "zobrazení v AI za 1 mesiac", "cz": "zobrazení v AI za 1 měsíc", "en": "AI impressions in 1 month"}[market]}],
        chart3,
        {"sk": "Nový web s nulovou históriou. V auguste a septembri nulová viditeľnosť, začiatkom októbra po publikovaní prvých optimalizovaných článkov prišiel okamžitý nástup do Google a vrchol 28 zobrazení denne v AI.",
         "cz": "Nový web s nulovou historií. V srpnu a září nulová viditelnost, začátkem října po publikování prvních optimalizovaných článků přišel okamžitý nástup do Google a vrchol 28 zobrazení denně v AI.",
         "en": "Brand new site with zero history. After deploying foundation content, visibility jumped in October, climbing to an average position of 8.2 and up to 28 AI citations per day."}[market],
        market)

    # Slide 4: 246k impressions / 3.22k clicks / 50k AI
    c4_title = {"sk": "Líder segmentu (veľký e-shop)", "cz": "Lídr segmentu (velký e-shop)", "en": "Category leader (large e-commerce)"}[market]
    c4_period = {"sk": "Týždenné sledovanie výkonnosti", "cz": "Týdenní sledování výkonnosti", "en": "Weekly performance tracking"}[market]
    chart4 = _screenshot_chart("client4-gsc-search.png", "client4-ai-overview.png", c4_title, market)
    s4 = _slide(
        c4_title,
        t["chip4"],
        c4_period,
        [{"big": "246 tis.", "color": _VIOLET, "label": {"sk": "týždenných zobrazení v Google", "cz": "týdenních zobrazení v Google", "en": "weekly impressions in Google"}[market]},
         {"big": "3 220", "color": _CERULEAN, "label": {"sk": "klikov týždenne z vyhľadávania", "cz": "kliků týdně z vyhledávání", "en": "weekly search clicks"}[market]},
         {"big": "50 tis.", "color": _ORANGE, "label": {"sk": "zobrazení v generatívnej AI", "cz": "zobrazení v generativní AI", "en": "generative AI impressions"}[market]}],
        chart4,
        {"sk": "Masívny organický zásah v konkurenčnom odvetví s priemernou pozíciou 6,6. Google Search Console hlási vyše 50 000 zobrazení vo funkciách generatívnej umelej inteligencie s dennými špičkami cez 1 000 zobrazení.",
         "cz": "Masivní organický zásah v konkurenčním odvětví s průměrnou pozicí 6,6. Google Search Console hlásí přes 50 000 zobrazení ve funkcích generativní umělé inteligence s denními špičkami přes 1 000 zobrazení.",
         "en": "Dominant organic footprint with average position 6.6. Google Search Console records over 50,000 impressions in generative AI features with peak days above 1,000 impressions."}[market],
        market)

    # Slide 5: 6.19k impressions / 155 clicks / 409 AI
    c5_title = {"sk": "Rastúci e-shop (týždenný posun)", "cz": "Rostoucí e-shop (týdenní posun)", "en": "Growing e-commerce (weekly progress)"}[market]
    c5_period = {"sk": "August až november 2026 (Weekly)", "cz": "Srpen až listopad 2026 (Weekly)", "en": "August to November 2026 (Weekly)"}[market]
    chart5 = _screenshot_chart("client5-gsc-search.png", "client5-ai-overview.png", c5_title, market)
    s5 = _slide(
        c5_title,
        t["chip5"],
        c5_period,
        [{"big": "6 190", "color": _VIOLET, "label": {"sk": "zobrazení za týždeň", "cz": "zobrazení za týden", "en": "weekly impressions"}[market]},
         {"big": "155", "color": _CERULEAN, "label": {"sk": "klikov za týždeň (CTR 2,5 %)", "cz": "kliků za týden (CTR 2,5 %)", "en": "weekly clicks (CTR 2.5%)"}[market]},
         {"big": "409", "color": _ORANGE, "label": {"sk": "týždenných zobrazení v AI", "cz": "týdenních zobrazení v AI", "en": "weekly AI impressions"}[market]}],
        chart5,
        {"sk": "Týždenný prehľad stabilného rastu. Krivka kliknutí narástla z počiatočných 6 na viac než 20 za týždeň, zatiaľ čo fialová linka AI viditeľnosti stúpa z 20 na 60 zobrazení za týždeň.",
         "cz": "Týdenní přehled stabilního růstu. Křivka kliknutí narostla z počátečních 6 na více než 20 za týden, zatímco fialová linka AI viditelnosti stoupá z 20 na 60 zobrazení za týden.",
         "en": "Consistent weekly compounding. Weekly clicks quadrupled while AI Overview citations grew steadily from 20 to 60 weekly impressions."}[market],
        market)

    slides = "".join([s1, s2, s3, s4, s5])
    dots = '<span class="rs-dot active" data-i="0"></span>' + \
           "".join(f'<span class="rs-dot" data-i="{i}"></span>' for i in range(1, 5))
    return f"""
<section class="section section-alt" id="vysledky">
  <div class="container">
    <div class="section-head">
      <span class="section-label">{t['label']}</span>
      <h2>{t['head']}</h2>
      <p class="section-subheading">{t['sub']}</p>
    </div>
    <div class="results-slider">
      <button class="rs-btn rs-prev" aria-label="{t['prev']}">
        <svg width="20" height="20" viewBox="0 0 20 20" fill="none" aria-hidden="true"><path d="M12.5 4 6.5 10l6 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
      <div class="rs-viewport" tabindex="0">{slides}</div>
      <button class="rs-btn rs-next" aria-label="{t['next']}">
        <svg width="20" height="20" viewBox="0 0 20 20" fill="none" aria-hidden="true"><path d="m7.5 4 6 6-6 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
      <div class="rs-dots">{dots}</div>
    </div>
    <div style="text-align:center; margin-top:26px;">
      <a href="{t['case_url']}" class="btn btn-outline">{t['all']}</a>
    </div>
  </div>
</section>
"""


def benefit_cards(cards: list[dict]) -> str:
    icons = ["icon-violet", "icon-orange", "icon-cerulean", "icon-violet-light"]
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
