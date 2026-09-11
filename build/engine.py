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
    "sluzby/linkbuilding/", "cennik/", "jak-pracujeme/", "vysledky/",
    "villa-paris/", "faq/", "o-nas/", "kontakt/", "blog/", "privacy/", "terms/",
}
CZ_PATHS = {
    "", "sluzby/", "sluzby/seo-optimalizace/", "sluzby/lodalne-seo/",
    "sluzby/seo-pre-ai-vyhledavace/", "sluzby/seo-pre-eshopy/", "sluzby/seo-audit/",
    "sluzby/linkbuilding/", "cenik/", "jak-pracujeme/", "vysledky/", "faq/", "kontakt/", "blog/",
    "privacy/", "terms/",
}
EN_PATHS = {
    "", "services/", "about/", "contact/", "faq/", "blog/", "portfolio/",
    "villa-paris/", "privacy/", "terms/",
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
    "sluzby/linkbuilding/": "sluzby/linkbuilding/",
    "jak-pracujeme/": "jak-pracujeme/",
    "vysledky/": "vysledky/",
    "faq/": "faq/",
    "o-nas/": None,
    "kontakt/": "kontakt/",
    "blog/": "blog/",
    "privacy/": "privacy/",
    "terms/": "terms/",
}


# SK path -> EN path. Only SK paths with a real EN page get an EN alternate
# (the EN market is a core-pages mirror; service subpages live on one EN hub).
EN_PAIR = {
    "": "",
    "sluzby/": "services/",
    "kontakt/": "contact/",
    "o-nas/": "about/",
    "faq/": "faq/",
    "blog/": "blog/",
    "vysledky/": "portfolio/",
    "villa-paris/": "villa-paris/",
    "privacy/": "privacy/",
    "terms/": "terms/",
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
            ("/cz/sluzby/seo-audit/", "SEO audit a analýza"),
            ("/cz/sluzby/linkbuilding/", "Linkbuilding"),
        ])
        rest = [("Ceník", "/cz/cenik/"), ("Jak pracuji", "/cz/jak-pracujeme/"),
                ("Výsledky", "/cz/vysledky/"), ("Blog", "/cz/blog/"),
                ("Kontaktujte mě", "/cz/kontakt/")]
    else:
        svc = ("Services", "/en/services/", [
            ("/en/services/#ai", "AI search visibility"),
            ("/en/services/#seo", "Google visibility"),
            ("/en/services/#local", "Google Maps visibility"),
            ("/en/services/#eshop", "E-commerce SEO"),
            ("/en/services/#audit", "SEO audit and analysis"),
            ("/en/services/#links", "Link building"),
        ])
        rest = [("Pricing", "/en/services/#pricing"), ("About", "/en/about/"),
                ("Portfolio", "/en/portfolio/"), ("Blog", "/en/blog/"),
                ("Contact us", "/en/contact/")]
    return [svc] + rest


def cta_label(market: str) -> str:
    return {"sk": "Kontaktuj ma", "cz": "Kontaktujte mě", "en": "Contact me"}[market]


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
        <a href="{PHONE_TEL}" class="btn btn-primary btn-sm nav-phone-btn">{PHONE_DISPLAY}</a>
        <button class="hamburger" id="hamburger" aria-label="Menu"><span></span><span></span><span></span></button>
      </div>
    </nav>
  </div>
</header>
<nav class="nav-mobile" id="nav-mobile">
  {mob_nav}
  <a href="{KONTAKT_LINK[market]}" class="btn btn-primary" style="margin-top:10px;">{cta_label(market)}</a>
  <a href="{PHONE_TEL}" class="mob-phone">{PHONE_DISPLAY}</a>
</nav>

{body}

{results_slider(market)}

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
                         (PHONE_TEL, PHONE_DISPLAY),
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
            ("Agentura", [("/cz/jak-pracujeme/", "Jak pracuji"),
                          ("/cz/cenik/", "Ceník"),
                          ("/cz/vysledky/", "Výsledky"),
                          ("/cz/blog/", "Blog"),
                          ("/cz/faq/", "FAQ")]),
            ("Kontakt", [(f"mailto:{EMAIL}", EMAIL),
                         (PHONE_TEL, PHONE_DISPLAY),
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
                         ("/en/contact/", "Contact form"),
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
    btn1 = {"sk": "Napíšte mi", "cz": "Napište mi", "en": "Get in touch"}[market]
    btn2 = {"sk": "Chcem bezplatný audit", "cz": "Chci bezplatný audit", "en": "Get my free audit"}[market]
    call = {"sk": "Alebo zavolajte rovno:", "cz": "Nebo volejte rovnou:", "en": "Or call directly:"}[market]
    audit_href = {"sk": "/sk/kontakt/?audit=1", "cz": "/cz/kontakt/?audit=1", "en": "/en/contact/?audit=1"}[market]
    return f"""
<div class="cta-band">
  <div>
    <h2>{title}</h2>
    <p>{text}</p>
  </div>
  <div class="hero-ctas">
    <a href="{KONTAKT_LINK[market]}" class="btn btn-white btn-lg">{btn1}</a>
    <a href="{audit_href}" class="btn btn-outline btn-lg" style="border-color:rgba(255,255,255,0.3);color:#fff;">{btn2}</a>
  </div>
  <p class="cta-phone-line">{call} <a href="{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
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


def results_slider(market: str) -> str:
    """Slider of real client results (GSC + AI Mode screenshots, Sep 2026)."""
    t = {
        "sk": {
            "label": "Moje výsledky", "head": "Čísla z praxe, nie obrázky zo šablóny",
            "sub": "Skutočné ukážky z Google Search Console a Google AI Mode mojich projektov a klientov. Čísla vám pred spoluprácou ukážem naživo.",
            "chip1": "Obsah + technika", "chip2": "SEO od nuly", "chip3": "AI viditeľnosť",
            "chip4": "Obsah na 6 stránkach", "chip5": "Lokálne SEO",
            "prev": "Predchádzajúci", "next": "Nasledujúci", "all": "Všetky výsledky",
            "case_url": "/sk/vysledky/",
        },
        "cz": {
            "label": "Moje výsledky", "head": "Čísla z praxe, ne obrázky ze šablony",
            "sub": "Skutečné ukázky z Google Search Console a Google AI Mode mých projektů a klientů. Čísla vám před spoluprací ukážu naživo.",
            "chip1": "Obsah + technika", "chip2": "SEO od nuly", "chip3": "AI viditelnost",
            "chip4": "Obsah na 6 stránkách", "chip5": "Lokální SEO",
            "prev": "Předchozí", "next": "Další", "all": "Všechny výsledky",
            "case_url": "/cz/vysledky/",
        },
        "en": {
            "label": "Results", "head": "Real numbers, not stock images",
            "sub": "Actual screenshots from Google Search Console and Google AI Mode of our projects and clients.",
            "chip1": "Content + tech", "chip2": "SEO from zero", "chip3": "AI visibility",
            "chip4": "Content on 6 pages", "chip5": "Local SEO",
            "prev": "Previous", "next": "Next", "all": "All results",
            "case_url": "/en/portfolio/",
        },
    }[market]

    chart1 = _sparkline([40, 55, 48, 62, 58, 75, 70, 88, 95, 92, 110, 121], _VIOLET)
    s1 = _slide(
        {"sk": "Aplikácia (klient)", "cz": "Aplikace (klient)", "en": "App (client)"}[market],
        t["chip1"],
        {"sk": "posledných 28 dní", "cz": "posledních 28 dní", "en": "last 28 days"}[market],
        [{"big": "121", "color": _VIOLET, "label": {"sk": "klikov z Google (+49 %)", "cz": "kliků z Google (+49 %)", "en": "clicks (+49%)"}[market]},
         {"big": "4 390", "color": _ORANGE, "label": {"sk": "zobrazení v Google (+43 %)", "cz": "zobrazení v Google (+43 %)", "en": "impressions (+43%)"}[market]},
         {"big": "+142 %", "color": _VIOLET_L, "label": {"sk": "rast hlavnej stránky", "cz": "růst hlavní stránky", "en": "top page growth"}[market]}],
        chart1,
        {"sk": "Prvý mesiac spolupráce: technické SEO a obsah. Google začal prinášať zákazníkov hneď.",
         "cz": "První měsíc spolupráce: technické SEO a obsah. Google začal přinášet zákazníky hned.",
         "en": "First month of cooperation: technical SEO and content. Google started delivering customers immediately."}[market],
        logo="inthecity.png", market=market)

    chart2 = _bars([68, 92, 130, 171, 250], _ORANGE, ["mesiac 1", "mesiac 2", "mesiac 3", "mesiac 4", "teraz"] if market != "en" else ["m1", "m2", "m3", "m4", "now"])
    s2 = _slide(
        {"sk": "Klient (firemný web)", "cz": "Klient (firemní web)", "en": "Client (company site)"}[market],
        t["chip2"],
        {"sk": "posledné 3 mesiace", "cz": "poslední 3 měsíce", "en": "last 3 months"}[market],
        [{"big": "250", "color": _VIOLET, "label": {"sk": "klikov za 3 mesiace (+355 %)", "cz": "kliků za 3 měsíce (+355 %)", "en": "clicks in 3 months (+355%)"}[market]},
         {"big": "8 950", "color": _CERULEAN, "label": {"sk": "zobrazení (+246 %)", "cz": "zobrazení (+246 %)", "en": "impressions (+246%)"}[market]},
         {"big": "5", "color": _ORANGE, "label": {"sk": "násobný rast klikov", "cz": "násobný rast kliků", "en": "x growth in clicks"}[market]}],
        chart2,
        {"sk": "Kliky za 3 mesiace od začiatku spolupráce. Rast každý mesiac, žiadny skok, ktorý sa nedá opakovať.",
         "cz": "Kliky za 3 měsíce od začátku spolupráce. Růst každý měsíc, žádný skok, který se nedá opakovat.",
         "en": "Clicks in 3 months since the start of cooperation. Growth every month, no one-off spike."}[market],
        market)

    chart3 = _bars([182, 293, 329, 413], _VIOLET_L, ["jún", "júl", "aug", "sep"])
    s3 = _slide(
        {"sk": "E-shop (vlastný projekt)", "cz": "E-shop (vlastní projekt)", "en": "E-shop (own project)"}[market],
        t["chip3"],
        {"sk": "Google AI Mode, jún až september 2026", "cz": "Google AI Mode, červen až září 2026", "en": "Google AI Mode, June to September 2026"}[market],
        [{"big": "893", "color": _VIOLET_L, "label": {"sk": "zobrazení v AI Mode za 3 mesiace", "cz": "zobrazení v AI Mode za 3 měsíce", "en": "AI Mode impressions in 3 months"}[market]},
         {"big": "+80 %", "color": _VIOLET, "label": {"sk": "august oproti júnu (182 → 329)", "cz": "srpen oproti červnu (182 → 329)", "en": "August vs June (182 → 329)"}[market]},
         {"big": "174", "color": _CERULEAN, "label": {"sk": "citácií homepage", "cz": "citací domovské stránky", "en": "homepage citations"}[market]}],
        chart3,
        {"sk": "Google AI Mode cituje e-shop denne po nasadení môjho obsahu. Rast mesačne: jún 182, júl 293, august 329. Najviac citované: homepage a blogové články (167 a 119 citácií). Konkurencia v AI odpovediach ešte nie je.",
         "cz": "Google AI Mode cituje e-shop denně po nasazení mého obsahu. Růst měsíčně: červen 182, červenec 293, srpen 329. Nejvíc citované: domovská stránka a blogové články (167 a 119 citací). Konkurence v AI odpovědích ještě není.",
         "en": "Google AI Mode cites the shop daily after deploying my content. Monthly growth: June 182, July 293, August 329. Most cited: homepage and blog articles (167 and 119 citations)."}[market],
        logo="speem.webp", market=market)

    chart4 = _sparkline([30, 38, 42, 50, 55, 62, 66, 72, 78, 84, 92, 102], _CERULEAN)
    s4 = _slide(
        {"sk": "Rast po pridaní nášho obsahu", "cz": "Růst po přidání našeho obsahu", "en": "Growth after our content"}[market],
        t["chip4"],
        {"sk": "28 dní + posledný týždeň", "cz": "28 dní + poslední týden", "en": "28 days + last week"}[market],
        [{"big": "11 000", "color": _CERULEAN, "label": {"sk": "zobrazení mesačne (+14 %)", "cz": "zobrazení měsíčně (+14 %)", "en": "monthly impressions (+14%)"}[market]},
         {"big": "+43 %", "color": _VIOLET, "label": {"sk": "klikov posledný týždeň", "cz": "kliků poslední týden", "en": "clicks last week"}[market]},
         {"big": "6", "color": _ORANGE, "label": {"sk": "stránok, na ktorých sa to stalo", "cz": "stránek, na kterých se to stalo", "en": "pages that did it"}[market]}],
        chart4,
        {"sk": "Pridané obsahové stránky na reálne dopyty zákazníkov. Len 6 stránok z celého webu posunulo celý web.",
         "cz": "Přidané obsahové stránky na reálné dotazy zákazníků. Jen 6 stránek z celého webu posunulo celý web.",
         "en": "Added content pages based on real customer queries. Just 6 pages moved the whole site."}[market],
        market)

    chart5 = _donut([(193, _VIOLET, "Maps"), (166, _VIOLET_L, "Search")])
    s5 = _slide(
        {"sk": "Klient: Google firemný profil", "cz": "Klient: Google firemní profil", "en": "Client: Google Business Profile"}[market],
        t["chip5"],
        {"sk": "zobrazenia profilu", "cz": "zobrazení profilu", "en": "profile views"}[market],
        [{"big": "359", "color": _VIOLET, "label": {"sk": "ľudí videlo profil", "cz": "lidí vidělo profil", "en": "people saw the profile"}[market]},
         {"big": "54 %", "color": _ORANGE, "label": {"sk": "cez Google Mapy", "cz": "přes Google Mapy", "en": "via Google Maps"}[market]},
         {"big": "46 %", "color": _VIOLET_L, "label": {"sk": "cez Google Search", "cz": "přes Google Search", "en": "via Google Search"}[market]}],
        chart5,
        {"sk": "Zákazníci hľadajú lokálne služby na Mapách aj v Search. Profil musí fungovať na oboch miestach.",
         "cz": "Zákazníci hledají lokální služby na Mapách i v Search. Profil musí fungovat na obou místech.",
         "en": "Customers look for local services on Maps and Search. The profile must work in both."}[market],
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
