# -*- coding: utf-8 -*-
"""Nokto Studio - CZ page content (localized for Czech market, targeting CZ keywords)."""
from engine import (base, page_hero, cta_band, faq_block, faq_schema,
                    steps_block, price_cards, benefit_cards, schema_service,
                    ORG_SCHEMA_CZ, CAL, EMAIL, BASE, gicon)

# ---------------------------------------------------------------- shared

CZ_TRUST = """
<div class="trust-strip">
  <div class="container">
    <div class="trust-grid">
      <div class="trust-stat reveal" data-delay="100">
        <span class="trust-num tn-blue">12&nbsp;EUR</span>
        <span class="trust-label">transparentní hodinová<br>sazba, žádné paušály</span>
      </div>
      <div class="trust-stat reveal" data-delay="200">
        <span class="trust-num tn-red">0 EUR</span>
        <span class="trust-label">první hovor a audit<br>webu jsou bezplatné</span>
      </div>
      <div class="trust-stat reveal" data-delay="300">
        <span class="trust-num tn-yellow">1. den</span>
        <span class="trust-label">bezplatný audit<br>začíná hned po prvním hovoru</span>
      </div>
      <div class="trust-stat reveal" data-delay="400">
        <span class="trust-num tn-green">30 min</span>
        <span class="trust-label">měsíční report<br>jako hovor se mnou</span>
      </div>
    </div>
  </div>
</div>
"""

CZ_PROCESS_STEPS = [
    {"title": "Bezplatný audit", "text": "Začínáme 30-minutovým hovorem a bezplatným auditem webu. Uvidíte přesně, co brzdí pozice, prodej a doporučení v AI."},
    {"title": "Plán podle priorit", "text": "Z auditu vyrobíme jasný plán: co opravit jako první, která klíčová slova přinášejí zákazníky a kolik hodin měsíčně to zabere."},
    {"title": "Práce v týdenních dávkách", "text": "Děláme: technika, obsah, firemní profil, AI viditelnost, odkazy. Vždy víte, co se stalo v uplynulém týdnu."},
    {"title": "Měření a report", "text": "Měsíční report dostáváte osobně: 30minutový telefonát se mnou. Pozice, kliky z Google, objednávky, zmínky v AI. Platíte jen za odpracované hodiny."},
]


def cz_process_section(label: str = "Jak pracujeme") -> str:
    return f"""
<section class="section section-alt" id="proces">
  <div class="container">
    <div class="section-head">
      <span class="section-label">{label}</span>
      <h2>Čtyři kroky. Žádné pevné smlouvy.</h2>
      <p class="section-subheading">Vždy víte, co děláme, proč a co to přineslo. Každá hodina je vykazovaná.</p>
    </div>
    {steps_block(CZ_PROCESS_STEPS)}
  </div>
</section>
"""


# ---------------------------------------------------------------- HOME

CZ_HOME_FAQ = [
    ("Kolik stojí SEO optimalizace webu?",
     "Za práci platíte 12 EUR za hodinu. Menší web zvládneme v 10 hodinách měsíčně (120 EUR), větší e-shop v 40 hodinách (480 EUR). Přesný rozsah potvrdíme v plánu po bezplatném auditu."),
    ("Jak dlouho trvá, než SEO přinese výsledky?",
     "První pohyby na méně konkurenčních klíčových slovech obvykle do 2 až 4 měsíců. Na hlavní dotazy v konkurenčních oborech 6 až 12 měsíců. Realistické termíny řekneme už v auditu."),
    ("Uvidím, za co platím?",
     "Ano. Každý měsíc dostanete report s odpracovanými hodinami, jejich obsahem a výsledky: pozice, kliky z Google, kontakty a objednávky, zmínky v AI."),
    ("Pomůžete mi, aby mě doporučoval ChatGPT?",
     "Ano, to je naše specializace. Optimalizujeme web pro AI nástroje (ChatGPT, Gemini, AI Overviews) tak, aby vás doporučovali při dotazech vašich zákazníků."),
    ("Jsou smlouvy vážoucí na 12 měsíců?",
     "Ne. Pracujeme měsíčně, spolupráci můžete kdykoliv ukončit. Důvěru stavíme na výsledcích, ne na vázanosti."),
]

# Tri pilíře viditelnosti + podpůrné služby + partnerské doplňky.
CZ_PILLARS = [
    ("/cz/sluzby/seo-pre-ai-vyhledavace/", "AI viditelnost",
     "ChatGPT, Gemini a Google AI Overviews vás doporučí zákazníkům jako první volbu.", "ai", "#34A853"),
    ("/cz/sluzby/seo-optimalizace/", "Google viditelnost",
     "Pozice v Google, které přinášejí zákazníky, ne jen návštěvnost.", "search", "#1A73E8"),
    ("/cz/sluzby/lodalne-seo/", "Google Mapy viditelnost",
     "Firemní profil, Mapy a hodnocení. Zákazníci z okolí vás najdou první.", "pin", "#EA4335"),
]
CZ_SUPPORT = [
    ("/cz/sluzby/seo-pre-eshopy/", "SEO pro e-shopy",
     "Více prodeje z kategorií a produktů. Shoptet, Marketplace, Google Shopping.", "shop", "#FBBC04"),
    ("/cz/sluzby/seo-audit/", "SEO audit a analýza",
     "Přesný obraz toho, co váš web brzdí, s akčním plánem podle priorit.", "audit", "#1A73E8"),
    ("/cz/sluzby/linkbuilding/", "Linkbuilding",
     "Zpětné odkazy a autorita, bez kterých se nahoru nedostanete.", "link", "#EA4335"),
]
CZ_PARTNERS = [
    ("https://flamia.studio", "Web dizajn: Flamia Studio",
     "Web na míru, který se najde a prodává. Dizajn a vývoj řeší náš partner Flamia Studio.",
     "web", "#1A73E8"),
    ("https://peterkocur.sk", "PPC reklama: Peter Kocur",
     "Google Ads pro výsledky hned, než SEO nabere tempo. Vedeme ho s partnerem Petrem Kocurem.",
     "target", "#EA4335"),
]


def _cz_card(href, title, text, icon, color, tag, delay, external=False):
    ext = ' target="_blank" rel="noopener noreferrer"' if external else ""
    return f"""
<div class="benefit-card card-hover reveal" data-delay="{delay}">
  <span class="benefit-icon">{gicon(icon, color, 26)}</span>
  <h3><a href="{href}"{ext} style="color:var(--text);">{title}</a></h3>
  <p>{text}</p>
  <div class="project-tags"><span class="project-tag {tag}">{'Partner' if external else 'Služba'}</span></div>
</div>"""


def cz_services_grid(cols: int = 3) -> str:
    pillars = "".join(_cz_card(*s, ["tag-green", "tag-blue", "tag-red"][i], (i + 1) * 100)
                      for i, s in enumerate(CZ_PILLARS))
    support = "".join(_cz_card(*s, ["tag-yellow", "tag-blue", "tag-red"][i], (i + 1) * 100)
                      for i, s in enumerate(CZ_SUPPORT))
    partners = "".join(_cz_card(*s, "tag-blue" if "flamia" in s[0] else "tag-red", (i + 1) * 100, external=True)
                       for i, s in enumerate(CZ_PARTNERS))
    return (f'<div class="grid-3">{pillars}</div>'
            f'<h3 style="margin:42px 0 22px;">K tomu i podpůrné služby</h3>'
            f'<div class="grid-3">{support}</div>'
            f'<h3 style="margin:42px 0 22px;">Doplňkové služby od partnerů</h3>'
            f'<p style="max-width:720px; margin:0 0 20px; color:var(--text-muted);">Tvorbu webu a PPC reklamu neřešíme sami. Nabízíme ji v tandemu s ověřenými partnery, se kterými pracujeme na jednom projektu.</p>'
            f'<div class="partner-band">{partners}</div>')


def cz_home() -> tuple[str, str]:
    h1 = ('Ať vás zákazníci najdou v <span class="hl-blue">Google</span>, '
          'na <span class="hl-red">Google Mapách</span> i v <span class="hl-green">ChatGPT</span>.')
    sub = ("Nokto Studio je SEO agentura pro podnikatele. Přivedeme vám zákazníky z organického "
           "vyhledávání, Google Map i AI nástrojů a posuneme prodej vašeho e-shopu. Za transparentních "
           "12 EUR za hodinu. Bez paušálů, bez pevných smluv, s reportem, kterému rozumíte.")
    body = f"""
<section class="hero">
  <div class="container">
    <div class="hero-content">
      <span class="hero-label">SEO agentura pro podnikatele · CZ a SK</span>
      <h1>{h1}</h1>
      <p class="hero-sub">{sub}</p>
      <div class="hero-ctas">
        <a href="{CAL}" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg">Bezplatný strategický hovor</a>
        <a href="/cz/kontakt/?audit=1" class="btn btn-outline btn-lg">Chci bezplatný audit webu</a>
      </div>
      <p class="hero-scarcity">Nebo rovnou volejte: <a href="tel:+421917316105" style="font-weight:700; color:var(--text); text-decoration:none;">+421 917 316 105</a></p>
      <p class="hero-scarcity" style="margin-top:6px;">Kapacita pro nové projekty: otevřeno od října 2026.</p>
    </div>
  </div>
</section>

{CZ_TRUST}

<!-- PRE KOHO -->
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Pro koho to děláme</span>
      <h2>Čtyři věci, které podnikatelé od nás chtějí</h2>
    </div>
    <div class="grid-4">
      <div class="benefit-card card-hover reveal" data-delay="100">
        <span class="benefit-icon icon-green">{gicon("ai", "#34A853", 26)}</span>
        <h3>Ať mě AI doporučí</h3>
        <p>Když si zákazník u ChatGPT nebo Gemini vyžádá doporučení, chcete být v odpovědi. Stavíme web tak, aby mu AI nástroje rozuměly a citovaly ho.</p>
      </div>
      <div class="benefit-card card-hover reveal" data-delay="200">
        <span class="benefit-icon icon-red">{gicon("pin", "#EA4335", 26)}</span>
        <h3>Zákazníci z Google a Map</h3>
        <p>Lokální vyhledávání a firemní profil Google jsou nejrychlejší cesta k zákazníkům z okolí. Nastavíme je a vyhodnocujeme každý týden.</p>
      </div>
      <div class="benefit-card card-hover reveal" data-delay="300">
        <span class="benefit-icon icon-yellow">{gicon("shop", "#FBBC04", 26)}</span>
        <h3>Více prodeje na e-shopu</h3>
        <p>Kategorie a produkty optimalizujeme na klíčová slova, která kupují. Google Shopping a Heureka sledujeme jako součást systému.</p>
      </div>
      <div class="benefit-card card-hover reveal" data-delay="400">
        <span class="benefit-icon icon-blue">{gicon("grow", "#1A73E8", 26)}</span>
        <h3>Více poptávek pro služby</h3>
        <p>Služby prodáváme přes obsahové stránky, které odpovídají na otázky zákazníků. Z většího zájmu vyrábíte více poptávek a zakázek.</p>
      </div>
    </div>
  </div>
</section>

<!-- SLUZBY -->
<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Služby</span>
      <h2>Tři pilíře viditelnosti, ve kterých jsem nejlepší</h2>
      <p class="section-subheading">AI viditelnost, Google viditelnost a viditelnost v Google Mapách. K tomu podpůrné služby a doplňky od ověřených partnerů.</p>
    </div>
    {cz_services_grid(3)}
    <div style="text-align:center; margin-top:36px;">
      <a href="/cz/sluzby/" class="btn btn-outline">Všechny služby a ceny za hodinu</a>
    </div>
  </div>
</section>

{cz_process_section()}

<!-- CENIK TEASER -->
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Ceník</span>
      <h2>12 EUR za hodinu. Platíte jen za práci.</h2>
      <p class="section-subheading">Žádné měsíční paušály, u kterých nevíte, co obsahují. Každá hodina je vykazovaná v reportu.</p>
    </div>
    <div class="rate-band">
      <div>
        <div class="rate-big">12 EUR <small>za hodinu práce</small></div>
        <p style="margin-top:8px; max-width:520px;">Balíčky jsou jen doporučené rozsahy. Kdykoliv je můžete měnit, bez sankcí.</p>
      </div>
      <a href="/cz/cenik/" class="btn btn-primary btn-lg">Zobrazit celý ceník</a>
    </div>
  </div>
</section>


<!-- KDO ZA TYM STOJI -->
<section class="section section-alt" id="o-mne">
  <div class="container">
    <div class="about-simon">
      <div class="about-simon-photo reveal">
        <img src="/assets/img/simon.png" alt="Simon Stremensky, SEO specialista a majitel Nokto Studio" width="300" height="300" loading="lazy">
      </div>
      <div class="reveal" data-delay="150">
        <span class="section-label">Kdo za Nokto stojí</span>
        <h2 style="margin:10px 0 14px;">S vámi komunikuju já, ne account manager.</h2>
        <p style="color:var(--text-muted);">Jsem Simon, SEO specialista. Za roky praxe v online marketingu mě nejvíc baví SEO a viditelnost v Google i AI nástrojích, protože vidím, jak reálně mění prodej malých firem. Pracuji s malým týmem a s partnery na web dizajnu a PPC reklamě, takže vám vždy odpoví ten, kdo práci dělá.</p>
        <p style="color:var(--text-muted);">První hodina s vámi je bezplatný hovor a audit. Pokud vám čísla nedají smysl, nic neplatíte.</p>
        <a href="{CAL}" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="margin-top:18px;">Dohodnout si hovor se mnou</a>
      </div>
    </div>
  </div>
</section>

<!-- VYSLEDKY -->
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Výsledky v Google</span>
      <h2>Jak klientům roste web i AI citace</h2>
      <p class="section-subheading">Ukázky z Google Search Console našeho projektu a klienta z posledních měsíců. Čísla vám vždy před spoluprací ukážu naživo.</p>
    </div>
    <div class="grid-4">
      <div class="growth-card reveal" data-delay="100">
        <h3 style="color:#1A73E8;">+355%</h3>
        <p>kliků z Google za 3 měsíce od začátku spolupráce</p>
        <div class="growth-bar" style="background:#1A73E8; width:100%;"></div>
        <p class="growth-spark">250 kliků měsíčně, průběžný růst</p>
      </div>
      <div class="growth-card reveal" data-delay="200">
        <h3 style="color:#EA4335;">+246%</h3>
        <p>zobrazení v Google za stejné období</p>
        <div class="growth-bar" style="background:#EA4335; width:85%;"></div>
        <p class="growth-spark">8 950 zobrazení měsíčně</p>
      </div>
      <div class="growth-card reveal" data-delay="300">
        <h3 style="color:#F9AB00;">+49%</h3>
        <p>kliků za posledních 28 dní oproti předchozímu období</p>
        <div class="growth-bar" style="background:#FBBC04; width:70%;"></div>
        <p class="growth-spark">121 kliků za 28 dní</p>
      </div>
      <div class="growth-card reveal" data-delay="400">
        <h3 style="color:#34A853;">13</h3>
        <p>AI citací webu klienta v Google AI Overviews po nasazení našeho obsahu</p>
        <div class="growth-bar" style="background:#34A853; width:55%;"></div>
        <p class="growth-spark">nejvíc citovaná stránka 8-krát za měsíc</p>
      </div>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="section section-alt">
  <div class="container">
    <div class="section-head"><span class="section-label">Časté otázky</span><h2>Nejdůležitější odpovědi</h2></div>
    {faq_block(CZ_HOME_FAQ)}
    <div style="text-align:center; margin-top:28px;">
      <a href="/cz/faq/" class="btn btn-outline">Všechny časté otázky</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    {cta_band("Začněte bezplatným auditem", "30 minut telefonátu a bezplatný audit vašeho webu. Dozvíte se, co brzdí vaše pozice a prodej, i když se nakonec rozhodnete jinak.", "cz")}
  </div>
</section>
"""
    html = base(market="cz", path="", title="Nokto Studio | SEO agentura pro podnikatele: Google i ChatGPT",
                desc="SEO agentura pro podnikatele. Zákazníci z Google a Google Map, doporučení v ChatGPT a AI nástrojích, více prodeje na e-shopu. 12 EUR za hodinu, bezplatný audit.",
                canonical=BASE + "/cz/", body=body, prefix="..",
                extra_head=ORG_SCHEMA_CZ + faq_schema(CZ_HOME_FAQ, BASE + "/cz/"))
    return ("cz/index.html", html)


# ---------------------------------------------------------------- SERVICE PAGES (CZ)

def _cz_service(*, slug: str, title: str, desc: str, label: str, h1: str,
                intro: str, for_who: list[str], deliverables: list[str],
                faq: list[tuple[str, str]], svc_name: str) -> tuple[str, str]:
    url = BASE + f"/cz/sluzby/{slug}/"
    who = "".join(f"<li>{w}</li>" for w in for_who)
    deliv = "".join(f'<li><span class="check">✓</span><span>{d}</span></li>' for d in deliverables)
    body = f"""
{page_hero(label, h1, intro, [("Domů", "/cz/"), ("Služby", "/cz/sluzby/"), (label.replace("Služba · ", ""), None)])}

<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:start;">
      <div class="prose">
        <h2>Pro koho je tato služba</h2>
        <ul>{who}</ul>
      </div>
      <div class="card">
        <span class="section-label">Co dodáváme</span>
        <ul class="deliv-list">{deliv}</ul>
      </div>
    </div>
  </div>
</section>

{cz_process_section("Jak bude spolupráce probíhat")}

<section class="section section-alt">
  <div class="container">
    <div class="rate-band">
      <div>
        <div class="rate-big">12 EUR <small>za hodinu · kdykoliv skončíte</small></div>
        <p style="margin-top:8px; max-width:520px;">Tato služba obvykle potřebuje 8 až 20 hodin měsíčně, podle rozsahu webu a konkurence.</p>
      </div>
      <div class="hero-ctas">
        <a href="{CAL}" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg">Bezplatný hovor</a>
        <a href="/cz/cenik/" class="btn btn-outline btn-lg">Ceník</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head"><span class="section-label">FAQ</span><h2>Časté otázky</h2></div>
    {faq_block(faq)}
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    {cta_band("Chcete vědět, co by tato služba přinesla vašemu webu?", "Bezplatný audit a 30 minut času. Žádné závazky.", "cz")}
  </div>
</section>
"""
    extra = schema_service(svc_name, desc, url) + faq_schema(faq, url)
    html = base(market="cz", path=f"sluzby/{slug}/", title=title, desc=desc,
                canonical=url, body=body, prefix="../../../", extra_head=ORG_SCHEMA_CZ + extra)
    return (f"cz/sluzby/{slug}/index.html", html)


def cz_sluzby_hub() -> tuple[str, str]:
    body = f"""
{page_hero("Služby", "Služby, které vám přivedou zákazníky",
           "Od technického SEO po AI viditelnost. Každá služba stojí 12 EUR za hodinu, rozsah domluvíte v plánu.",
           [("Domů", "/cz/"), ("Služby", None)])}
<section class="section">
  <div class="container">
    {cz_services_grid(3)}
  </div>
</section>
{cz_process_section()}
<section class="section" style="padding-top:0;">
  <div class="container">
    {cta_band("Nevíte, co potřebujete? Začněte auditem.", "Bezplatný audit vám řekne, kde jsou největší šance na růst.", "cz")}
  </div>
</section>
"""
    html = base(market="cz", path="sluzby/", title="Služby: SEO, Mapy, AI viditelnost, e-shopy | Nokto Studio",
                desc="SEO optimalizace webu, lokální SEO a firemní profil Google, SEO pro AI vyhledávače, e-shop SEO, audit, linkbuilding, weby a PPC. 12 EUR za hodinu.",
                canonical=BASE + "/cz/sluzby/", body=body, prefix="../..", extra_head=ORG_SCHEMA_CZ)
    return ("cz/sluzby/index.html", html)


def cz_seo_optimalizace() -> tuple[str, str]:
    return _cz_service(
        slug="seo-optimalizace",
        title="SEO optimalizace webových stránek | Nokto Studio",
        desc="SEO optimalizace webu: technika, obsah, klíčová slova. Pozice v Google, které přivedou zákazníky. 12 EUR za hodinu, bezplatný SEO audit.",
        label="Služba · SEO optimalizace",
        h1="SEO optimalizace, která přivede zákazníky",
        intro="Zákazník, který vás hledá v Google, je nejlevnější zákazník. Postavíme web tak, aby mu Google rozuměl, zařadil ho nahoru a návštěvníci odcházeli s poptávkou, ne s otazníkem.",
        for_who=[
            "Máte web, který nepřináší kontakty ani objednávky z vyhledávání.",
            "Konkurence vás předběhává na dotazech, které vás zajímají.",
            "Jste vidět jen na názvu firmy, ne na tom, co prodáváte.",
            "Platíte reklamu a rádi byste část dotazů zachytili zdarma.",
        ],
        deliverables=[
            "Analýza klíčových slov: po čem zákazníci opravdu hledají a co stojí za práci.",
            "Technická oprava webu: rychlost, indexace, kanonizace, chyby 404, sitemap.",
            "Přepis titulků a popisků na dotazy se skutečnou poptávkou.",
            "Nové obsahové stránky na dotazy, kde konkurence není silná.",
            "Interní prolinkování, které posune silné stránky výše.",
            "Měsíční report osobně: 30minutový hovor se mnou, pozice, kliky ze Search Console, objednávky.",
        ],
        faq=[
            ("Kolik hodin měsíčně zabere SEO optimalizace?",
             "Firemní web zvládneme v 10 hodinách měsíčně (120 EUR), e-shop v 20 až 40 hodinách (240 až 480 EUR). Rozsah potvrdíme v plánu po auditu."),
            ("Za jak dlouho se projeví výsledky?",
             "První pohyby na méně konkurenčních dotazech za 2 až 4 měsíce, na hlavní dotazy 6 až 12 měsíců. Záleží na konkurenci a stavu webu."),
            ("Děláte i obsah? Nemám čas psát.",
             "Ano, psaní obsahu je součást hodin. Sami navrhneme strukturu, napíšeme texty a před publikací je schválíte."),
            ("Co když jsem SEO už dělal a nic to nepřineslo?",
             "Bezplatný audit přesně řekne, co předchozí práce nechala nedokončené. Často chybí dva až tři kroky, ne celé SEO."),
        ],
        svc_name="SEO optimalizace webu",
    )


def cz_lodalne_seo() -> tuple[str, str]:
    return _cz_service(
        slug="lodalne-seo",
        title="Lokální SEO a firemní profil Google Mapy | Nokto Studio",
        desc="Lokální SEO: firemní profil Google, Google Mapy, hodnocení a lokální klíčová slova. Zákazníci z okolí vás najdou první. 12 EUR za hodinu.",
        label="Služba · Lokální SEO",
        h1="Lokální SEO: zákazníci z okolí vás najdou první",
        intro="Když si někdo vyhledá zubaře, autoservis, kuchyně nebo střechaře ve svém městě, rozhodnou tři věci: Google Mapy, hodnocení a web. Nastavíme všechny tři a držíme je v pořádku.",
        for_who=[
            "Provozujete firmu s působištěm: služby, restaurace, ordinace, dílna.",
            "Na Google Mapách chybíte, máte neúplná data nebo žádná hodnocení.",
            "Konkurence je v mapě nahoře, ač má horší nabídku.",
            "Chcete telefony a poptávky z okolí, ne z celé republiky.",
        ],
        deliverables=[
            "Kompletní nastavení a vyčištění firemního profilu Google.",
            "Kategorie, služby, otevírací doba, fotky a Q&A, které Google ocení.",
            "Strategie získávání hodnocení a profesionální odpovědi na ně.",
            "Lokální klíčová slova: město + služba, kraj + služba.",
            "Lokální citace v adresářích a oborových webech.",
            "Týdenní přehled: hovory, žádosti o trasu, zobrazení v mapě.",
        ],
        faq=[
            ("Kolik trvá, než firemní profil začne fungovat?",
             "První zlepšení v mapě vidíte za 4 až 8 týdnů, stabilní pozice trvá 3 až 6 měsíců. Záleží na konkurenci v okolí."),
            ("Mám jen jednu pobočku. Vyplatí se mi to?",
             "Právě pro jedno působiště je lokální SEO nejúčinnější. Soustředíte veškerou sílu do svého města a kraje, kde je konkurence nejmenší."),
            ("Jak získám více hodnocení na Google?",
             "Máme jednoduchý postup přes SMS a QR kód, který zákazníky vyzve hned po provedení služby. Zvyšuje míru recenzí násobně."),
            ("Jak řešíte špatná hodnocení?",
             "Odpovídáme profesionálně a na místě. Špatná hodnocení nelze odstranit, ale dobrý poměr a kultivované odpovědi působí na zákazníky víc než počty hvězdiček."),
        ],
        svc_name="Lokální SEO a firemní profil Google",
    )


def cz_seo_ai() -> tuple[str, str]:
    return _cz_service(
        slug="seo-pre-ai-vyhledavace",
        title="SEO pro AI vyhledávače: ChatGPT a AI Overviews | Nokto Studio",
        desc="Optimalizace pro AI vyhledávače a AI Overviews. ChatGPT a Gemini vás doporučí zákazníkům. Jako první na českém trhu.",
        label="Služba · SEO pro AI",
        h1="Ať vás ChatGPT doporučuje zákazníkům",
        intro="Zákazník dnes neptá jen Google. Ptá ChatGPT: \u201eDoporuč mi dobrou ordinaci v Brně.\u201c AI nástroj odpoví dvěma až pěti jmény. Naším úkolem je, aby tam bylo vaše jméno.",
        for_who=[
            "Chcete, aby vás AI nástroje doporučovaly jako první volbu ve vašem oboru.",
            "Vidíte, že zákazníci přicházejí s větou \u201enanělo mi ChatGPT, že...\u201c",
            "Konkurence se na AI doporučání zatím nepřipravuje (to je výhoda).",
            "Máte odbornost a chcete ji viditelnou i pro AI, ne jen pro Google.",
        ],
        deliverables=[
            "Audit AI viditelnosti: kdo vás dnes ChatGPT, Gemini a AI Overviews citují a kdo ne.",
            "Přímé odpovědi na stránkách: úvodní odstavce ve formátu, který AI čerpá.",
            "Strukturovaná data (schema.org) pro snadné čtení AI nástroji.",
            "Obsahové stránky odpovídající na reálné otázky zákazníků.",
            "Měsíční sledování: ve kterých AI odpovědích se objevujete a co se změnilo.",
            "Nastavení přístupu pro AI roboty (llms.txt, robots.txt, GPTBot, PerplexityBot).",
        ],
        faq=[
            ("Je toto SEO nebo marketing?",
             "Je to přímé pokračování SEO. Google i ChatGPT čerpají z webu, rozdíl je v tom, co a jak čtou. Nastavíme obojí najednou."),
            ("Jak měříte, jestli mě AI doporučuje?",
             "Pravidelně testujeme sadu dotazů, které vaši zákazníci kladou, a zaznamenáváme, zda se vaše jméno v odpovědích objevuje. Výsledky máte v reportu."),
            ("Není to brzy na to investovat?",
             "Je to právě naopak. Konkurence v AI doporučáních jen začíná, takže být první je výhoda. První zmínky vidíme často do 2 až 3 měsíců."),
            ("Pro koho to dává smysl?",
             "Pro služby, kde zákazník hledá doporučení: zdravotnictví, právo, servis, stavebnictví, školení. Pro e-shopy pomáhá u dotazů typu \u201ekdo prodává...\" a v recenzích."),
        ],
        svc_name="Optimalizace pro AI vyhledávače",
    )


def cz_eshop_seo() -> tuple[str, str]:
    return _cz_service(
        slug="seo-pre-eshopy",
        title="SEO pro e-shopy: Shoptet a Google Shopping | Nokto Studio",
        desc="SEO optimalizace e-shopu: kategorie, produkty, Shoptet, Marketplace i Google Shopping. Více prodeje z organického vyhledávání. 12 EUR za hodinu.",
        label="Služba · SEO pro e-shopy",
        h1="E-shop SEO: více objednávek z Google",
        intro="E-shop má jediné skutečné měřítko úspěchu: objednávky. Optimalizujeme kategorie a produkty na dotazy, které kupují, aby vás Google i Marketplace našli bez placení za každý klik.",
        for_who=[
            "Máte e-shop (Shoptet, WooCommerce, vlastní řešení) a prodej závisí na reklamě.",
            "Kategorie nemají vlastní texty a neprodávají samy od sebe.",
            "Jste vidět jen na názvech produktů, ne na tom, co zákazník skutečně hledá.",
            "Chcete snížit náklady na reklamu tím, že část dotazů zachytíte zdarma.",
        ],
        deliverables=[
            "Analýza klíčových slov pro kategorie a klíčové produkty.",
            "Texty kategorií a produktů, které prodávají, ne jen popisují.",
            "Technická hygiena: kanonizace, filtrovaná URL, rychlost, produktová data.",
            "Google Merchant Center a Google Shopping v pořádku.",
            "Poradenství pro Heureka a Marketplace integrace.",
            "Report v objednávkách a tržbách z organického kanálu.",
        ],
        faq=[
            ("Děláte SEO i pro Shoptet?",
             "Ano, Shoptet je v Česku nejrozšířenější platforma a známe její specifika (filtry, varianty, SEO moduly)."),
            ("Kolik objednávek z toho bude?",
             "Reálná čísla vám řekneme po auditu, na základě vašich klíčových slov a jejich poptávky. Nikdy nenabídáme číslo, které nedokážeme podpořit daty."),
            ("Musím dělat i linkbuilding?",
             "Pro konkurenční kategorie ano, odezva bez autority je pomalá. Doporučíme rozsah, který dává smysl pro váš rozpočet."),
            ("Jak měříte úspěch?",
             "V Google Analytics a Search Console sledujeme objednávky a tržby z organického vyhledávání. Report máte měsíčně."),
        ],
        svc_name="SEO pro e-shopy",
    )


def cz_audit() -> tuple[str, str]:
    return _cz_service(
        slug="seo-audit",
        title="SEO audit webu a analýza klíčových slov | Nokto Studio",
        desc="SEO audit webu s akčním plánem: technika, obsah, klíčová slova, konkurence. Bezplatný vstupní audit, detailní od 12 EUR za hodinu.",
        label="Služba · SEO audit",
        h1="SEO audit: přesný obraz toho, co váš web brzdí",
        intro="Audit není PDF do police. Je to seznam úloh s prioritami a odhadem hodin. Začíná bezplatným vstupním auditem, který máte do tří dnů.",
        for_who=[
            "Nevíte, proč web nepřináší zákazníky.",
            "SEO jste dělali, ale výsledky chybí.",
            "Před velkou investicí do webu chcete objektivní rozbor.",
            "Potřebujete plán, který provedete sami nebo s námi.",
        ],
        deliverables=[
            "Vstupní audit zdarma: 10 největších problémů na jedné straně.",
            "Detailní audit: technika, indexace, obsah, interní prolinkování.",
            "Analýza klíčových slov s objemy hledání a odhadem reálné šance.",
            "Rozbor konkurence: co dělat, aby vás nedoběhli.",
            "Plán s prioritami a odhadem hodin na každou položku.",
            "Prohlídka s vámi: 45 minut odpovídání na otázky.",
        ],
        faq=[
            ("Kolik stojí SEO audit?",
             "Vstupní audit je zdarma. Detailní audit stojí 240 až 480 EUR podle rozsahu webu (20 až 40 hodin × 12 EUR)."),
            ("Dostanu soubor, který můžu předat vývojáři?",
             "Ano. Plán je v srozumitelném formátu s úlohami krok za krokem, přímo pro CMS nebo vývojáře."),
            ("Musím potom brát i další služby?",
             "Ne. Plán si můžete provést sami nebo s jiným partnerem. Pokud se rozhodnete spolupracovat s námi, plán slouží jako základ."),
            ("Jak rychle audit dostanu?",
             "Vstupní audit do 3 pracovních dnů od prvního hovoru. Detailní audit za 7 až 10 dnů."),
        ],
        svc_name="SEO audit a analýza klíčových slov",
    )


def cz_linkbuilding() -> tuple[str, str]:
    return _cz_service(
        slug="linkbuilding",
        title="Linkbuilding a zpětné odkazy | Nokto Studio",
        desc="Linkbuilding: zpětné odkazy a autorita webu. Bezpečné metody, reálné domény, transparentní vykazování. 12 EUR za hodinu.",
        label="Služba · Linkbuilding",
        h1="Linkbuilding: autorita, která drží pozice",
        intro="Technika a obsah vás dovedou do středu výsledků, autorita vás posune nahoru. Stavíme odkazy, které Google akceptuje a zákazníci citují.",
        for_who=[
            "Máte technicky v pořádku web i obsah, ale pozice stojí.",
            "Konkurence má silnější link profil a předběhává vás.",
            "Chcete odkazy z reálných českých a slovenských domén, ne z spamu.",
            "Chcete transparentní vykazování, kde odkazy vznikly a co stály.",
        ],
        deliverables=[
            "Rozbor link profilu: co vás brzdí, které odkazy chybí.",
            "Tematické a lokální odkazy: adresáře, obory, média, partneři.",
            "Připravené obsahy a PR články, které odkazy nesou.",
            "Sledování nových i ztracených odkazů.",
            "Jasná cena za odkaz, bez skrytých přirážek.",
            "Měsíční přehled: nové domény, posun pozic.",
        ],
        faq=[
            ("Kolik stojí odkazy?",
             "Cena odkazu závisí na doméně. Většina českých odkazů stojí 1 200 až 7 500 Kč, mediální PR články víc. Vykazujeme skutečné ceny, bez přirážky."),
            ("Jak dlouho trvá, než odkazy pomohou?",
             "Nové odkazy se uplatní za 4 až 12 týdnů. Proto kombinujeme linkbuilding s obsahovou prací, která něco přináší už teď."),
            ("Kupujete odkazy?",
             "Pracujeme jen s reálnými, viditelnými místy. Nikdy nepoužíváme sítě automatizovaného spamu, které Google dřív nebo později sankcionuje."),
            ("Kolik odkazů potřebuji měsíčně?",
             "Menší firemní web 2 až 5, e-shop v konkurenčním oboru 5 až 10. Vyšší čísla ne vždy znamenají lepší výsledek."),
        ],
        svc_name="Linkbuilding",
    )


# ---------------------------------------------------------------- CENIK

CZ_PACKAGES = [
    {"name": "Start", "hours": 10, "price": 120,
     "items": ["Audit webu a analýza klíčových slov", "Technická oprava webu", "2 obsahové stránky nebo přepisy", "Firemní Google profil v pořádku", "Měsíční report: 30minutový hovor se mnou"],
     "cta": "/cz/kontakt/"},
    {"name": "Růst", "hours": 20, "price": 240, "featured": True,
     "items": ["Vše ze startu", "4 až 6 obsahových stránek měsíčně", "Optimalizace pro AI vyhledávače", "Interní prolinkování a CRO tipy", "Linkbuilding (2 až 3 odkazy)", "Měsíční report a hovor 30 min"],
     "cta": "/cz/kontakt/"},
    {"name": "E-shop", "hours": 40, "price": 480,
     "items": ["Vše z růstu", "Texty kategorií a produktů", "Google Merchant Center a Shopping", "Poradenství Heureka / Marketplace", "Automatizace email marketingu", "Report s tržbami z organika"],
     "cta": "/cz/kontakt/"},
]

CZ_CENIK_FAQ = [
    ("Kolik stojí SEO optimalizace webu?",
     "Platíte 12 EUR za každou odpracovanou hodinu. Firemní web obvykle potřebuje 10 hodin měsíčně (120 EUR), e-shop 20 až 40 hodin (240 až 480 EUR). Rozsah si nastavíte sami a můžete ho kdykoliv měnit."),
    ("Proč je to levnější než konkurence?",
     "Nemáme kanceláře ani manažerské vrstvy. Práce automatizujeme tam, kde automatizace nic nezkazí, a odbornou energii dáváme tam, kde se počítá. Úspory přenášíme na vás."),
    ("Co je v ceně zahrnuto?",
     "Vše kromě reklamních výdajů a nákladů na odkazy či nástroje třetích stran. Ty vám vykazujeme ve skutečné ceně, bez přirážky."),
    ("Musím platit měsíčně předem?",
     "Fakturujeme měsíčně zpětně za skutečně odpracované hodiny, s fakturou. Paušál není potřeba."),
    ("Můžu spolupráci kdykoliv ukončit?",
     "Ano, kdykoliv, bez sankcí a bez vázanosti. Důvěru si zasloužíme výsledky."),
    ("Jak vím, že práce byla odvedena?",
     "Každý měsíc dostanete seznam úloh s hodinami a jejich výsledkem. Vy jste ten, kdo kontroluje."),
]


def cz_cenik() -> tuple[str, str]:
    body = f"""
{page_hero("Ceník", "Ceník: 12 EUR za hodinu, bez paušálů",
           "Platíte za odpracované hodiny. Každá hodina je vykazovaná v reportu. Spolupráci můžete kdykoliv ukončit.",
           [("Domů", "/cz/"), ("Ceník", None)])}

<section class="section">
  <div class="container">
    <div class="rate-band">
      <div>
        <div class="rate-big">12 EUR <small>za hodinu práce</small></div>
        <p style="margin-top:8px; max-width:560px;">SEO optimalizace, lokální SEO, AI viditelnost, obsah, linkbuilding, weby i PPC. Jedna sazba, jednoduché počty.</p>
      </div>
      <a href="{CAL}" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg">Nezávazná nabídka</a>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Balíčky</span>
      <h2>Doporučené rozsahy, ne povinné paušály</h2>
      <p class="section-subheading">Balíček je doporučený rozsah hodin na měsíc. Můžete ho kdykoliv změnit, pozastavit nebo ukončit.</p>
    </div>
    {price_cards(CZ_PACKAGES, "cz")}
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:start;">
      <div class="prose">
        <h2>Co je v ceně</h2>
        <ul class="deliv-list">
          <li><span class="check">✓</span><span>Všechna práce: technika, obsah, firemní profil, AI viditelnost, odkazy, weby, PPC.</span></li>
          <li><span class="check">✓</span><span>Měření a reportování: Search Console, Analytics, pozice, konverze, zmínky v AI.</span></li>
          <li><span class="check">✓</span><span>Komunikace: měsíční 30minutový telefonát se mnou, neomezené otázky mezitím.</span></li>
        </ul>
        <h2>Co není v ceně</h2>
        <ul class="deliv-list">
          <li><span class="check" style="background:#FCE8E6;color:var(--g-red-deep);">×</span><span>Reklamní výdaje (Google Ads, Meta Ads). Platíte přímo Google, ne nám.</span></li>
          <li><span class="check" style="background:#FCE8E6;color:var(--g-red-deep);">×</span><span>Náklady na odkazy a PR články. Vykazujeme skutečnou cenu od média.</span></li>
          <li><span class="check" style="background:#FCE8E6;color:var(--g-red-deep);">×</span><span>Pronájem nástrojů třetích stran, pokud je potřeba (kurzy, platby, hosting).</span></li>
        </ul>
      </div>
      <div class="card">
        <span class="section-label">Příklad z praxe</span>
        <p style="margin-bottom:14px;">Firemní web advokátní kanceláře ve městě s 50 000 obyvateli:</p>
        <ul class="deliv-list">
          <li><span class="check">✓</span><span><strong>Měsíc 1:</strong> audit + technická oprava + firemní profil (12 h = 144 EUR)</span></li>
          <li><span class="check">✓</span><span><strong>Měsíce 2 až 4:</strong> obsahové stránky na dotazy zákazníků (10 h = 120 EUR)</span></li>
          <li><span class="check">✓</span><span><strong>Měsíce 5+</strong>: udržování, linkbuilding, AI viditelnost (8 h = 96 EUR)</span></li>
        </ul>
        <p style="margin-top:14px; font-size:0.9rem; color:var(--text-muted);">Reálná čísla pro váš web potvrdíme v bezplatném auditu.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head"><span class="section-label">FAQ k ceně</span><h2>Časté otázky k ceníku</h2></div>
    {faq_block(CZ_CENIK_FAQ)}
  </div>
</section>

<section class="section">
  <div class="container">
    {cta_band("Kolik by to stálo vás?", "Bezplatný audit a odhad hodin pro váš konkrétní web. Bez závazků, se skutečnými čísly.", "cz")}
  </div>
</section>
"""
    faq_html = faq_schema(CZ_CENIK_FAQ, BASE + "/cz/cenik/")
    html = base(market="cz", path="cenik/", title="Ceník SEO: 12 EUR za hodinu, bez paušálů | Nokto Studio",
                desc="SEO ceník s transparentní hodinovou sazbou 12 EUR. Balíčky od 120 EUR měsíčně, bez pevných smluv. Bezplatný SEO audit.",
                canonical=BASE + "/cz/cenik/", body=body, prefix="../..", extra_head=ORG_SCHEMA_CZ + faq_html)
    return ("cz/cenik/index.html", html)


# ---------------------------------------------------------------- remaining CZ pages

def cz_jak_pracujeme() -> tuple[str, str]:
    body = f"""
{page_hero("Proces", "Jak pracujeme: plán, práce, měření",
           "Jasný proces bez černé skříňky. Vždy víte, co děláme, proč a co to přineslo.",
           [("Domů", "/cz/"), ("Jak pracujeme", None)])}
<section class="section">
  <div class="container">
    <div class="section-head"><span class="section-label">Proces</span><h2>Od prvního hovoru po měsíční report</h2></div>
    {steps_block(CZ_PROCESS_STEPS)}
  </div>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="section-head"><span class="section-label">Dodávky</span><h2>Co přesně dostanete každý měsíc</h2></div>
    <div class="grid-2" style="align-items:start;">
      <div class="card">
        <span class="section-label">Práce</span>
        <ul class="deliv-list">
          <li><span class="check">✓</span><span>Technická údržba webu: rychlost, indexace, opravy chyb.</span></li>
          <li><span class="check">✓</span><span>Obsahové stránky psané na reálné dotazy zákazníků.</span></li>
          <li><span class="check">✓</span><span>Firemní profil Google: data, fotky, hodnocení, Q&amp;A.</span></li>
          <li><span class="check">✓</span><span>Optimalizace pro ChatGPT, Gemini a AI Overviews.</span></li>
          <li><span class="check">✓</span><span>Linkbuilding podle dohody (cena odkazů vykazovaná zvlášť).</span></li>
        </ul>
      </div>
      <div class="card">
        <span class="section-label">Měření</span>
        <ul class="deliv-list">
          <li><span class="check">✓</span><span>Pozice na sledovaných klíčových slovech (trend, ne jen číslo).</span></li>
          <li><span class="check">✓</span><span>Kliky a zobrazení z Google (Search Console).</span></li>
          <li><span class="check">✓</span><span>Kontakty a objednávky (Google Analytics).</span></li>
          <li><span class="check">✓</span><span>Zobrazení v Google Mapách: hovory, trasy, recenze.</span></li>
          <li><span class="check">✓</span><span>Zmínky v AI odpovědích (ChatGPT, Gemini, AI Overviews).</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head"><span class="section-label">Měření</span><h2>Jak měříme výsledky</h2></div>
    <table class="metric-table">
      <tr><th>Co sledujeme</th><th>Nástroj</th><th>Co to říká</th></tr>
      <tr><td><strong>Pozice</strong></td><td>Sledování klíčových slov</td><td>Na kterých dotazech rosteme a kde jsme uvízli.</td></tr>
      <tr><td><strong>Kliky z Google</strong></td><td>Search Console</td><td>Kolik lidí nás vidí a kolik z nich klikne.</td></tr>
      <tr><td><strong>Kontakty a objednávky</strong></td><td>Google Analytics 4</td><td>Kolik návštěvníků se stalo zákazníky.</td></tr>
      <tr><td><strong>Viditelnost v mapě</strong></td><td>Firemní profil Google</td><td>Kolik lidí vidělo firmu, zatelefonovalo, šlo na trasu.</td></tr>
      <tr><td><strong>AI doporučení</strong></td><td>Pravidelné AI testy</td><td>Zda vás ChatGPT, Gemini a AI Overviews citují.</td></tr>
      <tr><td><strong>Tržby z organika</strong></td><td>Analytics + e-shop</td><td>Pro e-shopy: přímý vztah SEO úsilí k prodeji.</td></tr>
    </table>
  </div>
</section>
<section class="section" style="padding-top:0;">
  <div class="container">
    {cta_band("Chcete takový proces pro svůj web?", "Začněte bezplatným auditem a 30 minutami času.", "cz")}
  </div>
</section>
"""
    html = base(market="cz", path="jak-pracujeme/", title="Jak pracujeme: proces, dodávky a měření výsledků | Nokto Studio",
                desc="Náš SEO proces: bezplatný audit, plán s čísly, týdenní práce, měsíční měření. Pozice, kliky, objednávky a AI doporučení v jednom reportu.",
                canonical=BASE + "/cz/jak-pracujeme/", body=body, prefix="../..", extra_head=ORG_SCHEMA_CZ)
    return ("cz/jak-pracujeme/index.html", html)


def cz_pripady() -> tuple[str, str]:
    body = f"""
{page_hero("Případové studie", "Příklady práce, ne samá chvála",
           "Klienti, se kterými jsme pracovali, a to, co jsme pro ně stavěli. Čísla doplňujeme podle dohody s klientem.",
           [("Domů", "/cz/"), ("Případy", None)])}
<section class="section">
  <div class="container">
    <div class="grid-2">
      <div class="project-card card-hover">
        <div class="project-card-body">
          <h3>Villa Paris, Piešťany (SK)</h3>
          <p>Premium ubytování. Rebrand, nový web, hotelový copywriting a lokální SEO v jednom systému. Cíl: více přímých rezervací bez provizí portálů.</p>
          <div class="project-tags">
            <span class="project-tag tag-blue">Branding</span>
            <span class="project-tag tag-green">Web</span>
            <span class="project-tag tag-red">Lokální SEO</span>
          </div>
          <a href="/sk/villa-paris/" class="btn btn-outline" style="margin-top:20px;">Číst příběh (SK)</a>
        </div>
      </div>
      <div class="project-card card-hover">
        <div class="project-card-body">
          <h3>Mikramt.sk, Martin (SK)</h3>
          <p>Vlastní e-shop s API integrací na účetní systém Sunsoft Ecosun pro regionálního dodavatele truhlářského zboží. Za 9 měsíců 2 492,75 EUR online tržeb z 15 objednávek (email + organický Google), největší objednávka 722 EUR. Email marketing, lokální SEO a GEO optimalizace. Prodej v kamenné prodejně do sumy nezapočítáváme.</p>
          <div class="case-result">
            <div><strong>2 492,75 EUR</strong><span>tržby / 9 měsíců</span></div>
            <div><strong>15</strong><span>objednávek online</span></div>
          </div>
          <div class="project-tags">
            <span class="project-tag tag-yellow">E-shop SEO</span>
            <span class="project-tag tag-green">Email marketing</span>
            <span class="project-tag tag-red">Lokální SEO + GEO</span>
          </div>
          <a href="{CAL}" target="_blank" rel="noopener noreferrer" class="btn btn-outline" style="margin-top:20px;">Zeptat se víc</a>
        </div>
      </div>
    </div>
    <p style="text-align:center; margin-top:28px; color:var(--text-muted); font-size:0.9rem;">
      Další případy a reference na žádost, včetně kontaktů na klienty. Klienty citujeme jen s jejich souhlasem.
    </p>
  </div>
</section>
<section class="section" style="padding-top:0;">
  <div class="container">
    {cta_band("Vaše firma může být další příběh", "Začněme bezplatným auditem. Uvidíte, co bychom u vás řešili, ještě před první fakturou.", "cz")}
  </div>
</section>
"""
    html = base(market="cz", path="pripady/", title="Případové studie SEO a tvorby webů | Nokto Studio",
                desc="Případové studie Nokto Studio: Villa Paris Piešťany (rebrand, web, lokální SEO), e-shop SEO a další projekty.",
                canonical=BASE + "/cz/pripady/", body=body, prefix="../..", extra_head=ORG_SCHEMA_CZ)
    return ("cz/pripady/index.html", html)


CZ_FAQ_SECTIONS = [
    ("Všeobecné", [
        ("Co přesně Nokto Studio dělá?",
         "SEO optimalizaci webu, lokální SEO a firemní profil Google, optimalizaci pro AI vyhledávače (ChatGPT, Gemini, AI Overviews), SEO pro e-shopy, SEO audity, linkbuilding, tvorbu webů a PPC reklamu Google Ads. K tomu email marketing pro e-shopy a firmy."),
        ("Pro jaké firmy pracujete?",
         "Především pro menší a střední firmy: lokální služby (řemeslníci, zdravotnictví, právo, autoservis), e-shopy a firmy s odbornými službami. Působíme na trzích Česka a Slovenska."),
    ]),
    ("Cena a smlouvy", [
        ("Kolik stojí SEO?",
         "12 EUR za odpracovanou hodinu. Menší firemní web obvykle 10 hodin měsíčně (120 EUR), e-shop 20 až 40 hodin (240 až 480 EUR). Balíčky jsou doporučené rozsahy, ne povinné paušály."),
        ("Jsou smlouvy vážoucí?",
         "Ne. Spolupráci můžete kdykoliv ukončit, bez sankcí. Fakturujeme měsíčně za skutečně odpracované hodiny."),
        ("Jsou v ceně zahrnuty reklamní výdaje?",
         "Ne. Reklamu (Google Ads) platíte přímo Google. My kampaně řídíme za 12 EUR za hodinu. Náklady na odkazy a PR vykazujeme ve skutečné ceně."),
    ]),
    ("Proces a výsledky", [
        ("Jak dlouho trvá, než SEO přinese výsledky?",
         "První pohyby na méně konkurenčních dotazech za 2 až 4 měsíce, na hlavní dotazy 6 až 12 měsíců. Lokální SEO a firemní profil se zlepšují často za 4 až 8 týdnů."),
        ("Jak uvidím, že práce byla odvedena?",
         "Měsíční report: odpracované hodiny a jejich obsah, pozice, kliky ze Search Console, kontakty a objednávky z Analytics, viditelnost v mapě a zmínky v AI odpovědích."),
        ("Nabízíte záruky první pozice?",
         "Ne. Nikdo reálně nemůže zaručit první místo v Google, kdo to slibuje, prodává fikci. Zaručujeme proces, transparentnost a měřitelný postup, který k pozicím vede."),
    ]),
    ("AI a nové vyhledávání", [
        ("Nahradí ChatGPT Google?",
         "Doplní ho, ne zničí. Zákazníci dnes hledají obojí. Naše práce pokrývá obojí: klasické Google pozice i viditelnost v AI odpovědích."),
        ("Jak zjistím, jestli mě AI doporučuje?",
         "Pravidelně testujeme sady dotazů, které vaši zákazníci kladou, a zaznamenáváme, zda se vaše jméno objevuje v odpovědích ChatGPT, Gemini a Google AI Overviews. Výsledek máte v reportu."),
    ]),
]


def cz_faq() -> tuple[str, str]:
    sections_html = ""
    all_qa = []
    for sec_title, qas in CZ_FAQ_SECTIONS:
        qas_html = "".join(
            f'<div class="faq-item"><button class="faq-question" type="button">{q}</button>'
            f'<div class="faq-answer"><p>{a}</p></div></div>' for q, a in qas
        )
        sections_html += f'<h2 style="margin-top:36px;">{sec_title}</h2>{qas_html}'
        all_qa += qas
    body = f"""
{page_hero("FAQ", "Časté otázky", "Odpovědi na to, co nás klienti ptají nejvíc. Pokud chybí vaše otázka, ptejte se přímo.", [("Domů", "/cz/"), ("FAQ", None)])}
<section class="section">
  <div class="container" style="max-width:800px;">
    {sections_html}
  </div>
</section>
<section class="section" style="padding-top:0;">
  <div class="container">
    {cta_band("Chybí vám otázka?", "Napište nebo volejte. Bez závazků.", "cz")}
  </div>
</section>
"""
    faq_html = faq_schema(all_qa, BASE + "/cz/faq/")
    html = base(market="cz", path="faq/", title="FAQ: časté otázky k SEO, ceně a procesu | Nokto Studio",
                desc="Časté otázky: kolik stojí SEO, jak dlouho trvá, jak měříme výsledky, co je SEO pro AI vyhledávače. Nokto Studio, SEO agentura.",
                canonical=BASE + "/cz/faq/", body=body, prefix="../..", extra_head=ORG_SCHEMA_CZ + faq_html)
    return ("cz/faq/index.html", html)


def cz_kontakt() -> tuple[str, str]:
    body = f"""
{page_hero("Kontakt", "Napište. Ozveme se osobně.",
           "Nejrychlejší cestou je bezplatný hovor přes kalendář. Pokud upřednostníte formulář, využijte ho níže.",
           [("Domů", "/cz/"), ("Kontakt", None)])}
<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:start;">
      <div class="card">
        <span class="section-label">Bezplatný hovor 30 minut</span>
        <p style="margin:14px 0 22px;">Vyberte si termín přímo v kalendáři. Probereme cíle vaší firmy a na místě řekneme, co bychom dělali první. Žádný tlak, žádné závazky.</p>
        <a href="{CAL}" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg" style="width:100%;">Otevřít kalendář</a>
        <ul class="deliv-list" style="margin-top:24px;">
          <li><span class="check">✓</span><span>Bezplatný vstupní audit webu po hovoru</span></li>
          <li><span class="check">✓</span><span>Skutečná čísla: co by SEO u vás mohlo znamenat</span></li>
          <li><span class="check">✓</span><span>Nezávazné. Rozhodnete se, kdy a zda.</span></li>
        </ul>
      </div>
      <div class="card contact-form-wrap">
        <span class="section-label">Nebo formulář</span>
        <form class="contact-form-el" style="margin-top:16px;">
          <div class="form-grid">
            <div class="form-field"><label class="form-label" for="name">Jméno a firma *</label><input class="form-input" id="name" name="name" type="text" required></div>
            <div class="form-field"><label class="form-label" for="email">Email *</label><input class="form-input" id="email" name="email" type="email" required></div>
            <div class="form-field full"><label class="form-label" for="url">Adresa webu (pokud máte)</label><input class="form-input" id="url" name="url" type="url" placeholder="https://"></div>
            <div class="form-field full"><label class="form-label" for="goal">Jaký je váš cíl? *</label>
              <select class="form-select" id="goal" name="goal" required>
                <option value="">Vyberte...</option>
                <option>Více zákazníků z Google</option>
                <option>Lepší viditelnost na Google Mapách</option>
                <option>Doporučení v ChatGPT / AI</option>
                <option>Více prodeje na e-shopu</option>
                <option>Nový web nebo redesign</option>
                <option>Něco jiného</option>
              </select>
            </div>
            <div class="form-field full"><label class="form-label" for="msg">Zpráva</label><textarea class="form-textarea" id="msg" name="msg" placeholder="Pár slov o vaší firmě a tom, čeho chcete dosáhnout."></textarea></div>
          </div>
          <button type="submit" class="btn btn-primary" style="margin-top:18px; width:100%;">Poslat zprávu</button>
          <p class="form-note">Odesláním souhlasíte se zpracováním údajů za účelem odpovědi (viz <a href="/cz/privacy/">zásady ochrany osobních údajů</a>).</p>
        </form>
        <div class="form-success" style="display:none; margin-top:16px; background:#E6F4EA; color:var(--g-green-deep); padding:16px; border-radius:10px;">
          ✓ Děkujeme. Ozveme se osobně.
        </div>
        <p style="margin-top:20px;">Nebo email: <a href="mailto:{EMAIL}">{EMAIL}</a> · nebo volejte: <a href="tel:+421917316105" style="font-weight:700; color:var(--text); text-decoration:none;">+421 917 316 105</a></p>
      </div>
    </div>
  </div>
</section>
"""
    html = base(market="cz", path="kontakt/", title="Kontakt: bezplatný hovor a audit | Nokto Studio",
                desc="Spojte se s Nokto Studio. Bezplatný strategický hovor 30 minut a bezplatný vstupní audit webu.",
                canonical=BASE + "/cz/kontakt/", body=body, prefix="../..", extra_head=ORG_SCHEMA_CZ)
    return ("cz/kontakt/index.html", html)


def cz_blog() -> tuple[str, str]:
    topics = [
        ("Jak vybrat SEO agenturu (a na co si dát pozor)", "Ceník, záruky, reporty. 8 otázek, které je potřeba položit před podpisem.", "tag-blue"),
        ("Kolik stojí SEO optimalizace webu v 2026?", "Přehled cen na českém trhu a proč se platí paušály za práci, která se neodvede.", "tag-yellow"),
        ("Jak se dostat do doporučení ChatGPT", "První příručka pro české firmy: jak AI nástroje vybírají, koho doporučit.", "tag-green"),
        ("Firemní profil Google: kompletní návod pro firmy", "Od založení po hodnocení. Co Google ocení a co ignoruje.", "tag-red"),
    ]
    cards = "".join(f"""
<div class="benefit-card card-hover">
  <span class="project-tag {tag}">Článek v přípravě</span>
  <h3 style="margin-top:12px;">{t}</h3>
  <p>{d}</p>
</div>""" for t, d, tag in topics)
    body = f"""
{page_hero("Blog", "Praktické články o SEO a AI",
           "Píšeme, co umíme ověřit v praxi. První články vycházejí tento měsíc.", [("Domů", "/cz/"), ("Blog", None)])}
<section class="section">
  <div class="container">
    <div class="grid-2">{cards}</div>
    <div style="text-align:center; margin-top:36px;">
      <p style="color:var(--text-muted);">Chcete se o něčem dozvědět víc už teď? Zeptejte se přímo, rádi poradíme i bez smlouvy.</p>
      <a href="{CAL}" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="margin-top:14px;">Bezplatný hovor</a>
    </div>
  </div>
</section>
"""
    html = base(market="cz", path="blog/", title="Blog o SEO, Google Mapách a AI vyhledávačích | Nokto Studio",
                desc="Praktické články: jak vybrat SEO agenturu, kolik stojí SEO, jak se dostat do doporučení ChatGPT, firemní profil Google od základů.",
                canonical=BASE + "/cz/blog/", body=body, prefix="../..", extra_head=ORG_SCHEMA_CZ)
    return ("cz/blog/index.html", html)


def cz_privacy() -> tuple[str, str]:
    body = f"""
{page_hero("Ochrana osobních údajů", "Zásady ochrany osobních údajů",
           "Zpracováváme jen data, která potřebujeme k odpovědi a spolupráci. Žádný prodej dat třetím stranám.",
           [("Domů", "/cz/"), ("Ochrana osobních údajů", None)])}
<section class="section">
  <div class="container prose">
    <h2>Kdo zpracovává údaje</h2>
    <p>Operátorem osobních údajů je Nokto Studio (Simon, provozovatel webových stránek noktostudio.com). Kontakt: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    <h2>Jaké údaje a proč</h2>
    <ul>
      <li>Kontaktní formulář: jméno, email, adresa webu a zpráva. Účelem je odpovědět na váš dotaz.</li>
      <li>Kalendář (Calendly): jméno, email a termín hovoru. Účelem je uskutečnit hovor.</li>
      <li>Analitika: anonymizovaná data o návštěvnosti (Google Analytics 4, Microsoft Clarity) pro zlepšování webu.</li>
    </ul>
    <h2>Jak dlouho údaje uchováváme</h2>
    <p>Kontakty z formulářů a kalendáře uchováváme maximálně 24 měsíců od poslední komunikace, pokud nevznikne spolupráce.</p>
    <h2>Vaše práva</h2>
    <p>Máte právo na přístup k údajům, jejich opravu, výmaz a přenos. Požadavek zašlete na <a href="mailto:{EMAIL}">{EMAIL}</a>. Máte také právo podat stížnost u Úřadu pro ochranu osobních údajů.</p>
    <h2>Cookies</h2>
    <p>Web používá analytické cookies po vašem souhlasu (cookie banner). Technické cookies nezbytné pro provoz webu jsou povolené vždy.</p>
  </div>
</section>
"""
    html = base(market="cz", path="privacy/", title="Zásady ochrany osobních údajů | Nokto Studio",
                desc="Zásady ochrany osobních údajů webu noktostudio.com: jaké údaje zpracováváme, proč a jaká máte práva.",
                canonical=BASE + "/cz/privacy/", body=body, prefix="../..", extra_head=ORG_SCHEMA_CZ)
    return ("cz/privacy/index.html", html)


def cz_terms() -> tuple[str, str]:
    body = f"""
{page_hero("Obchodní podmínky", "Obchodní podmínky",
           "Jednoduché podmínky bez právnické španělštiny: hodinová sazba, měsíční fakturace, bez vázanosti.",
           [("Domů", "/cz/"), ("Obchodní podmínky", None)])}
<section class="section">
  <div class="container prose">
    <h2>1. Předmět</h2>
    <p>Tyto podmínky upravují spolupráci mezi Nokto Studio (dále "poskytovatel") a klientem při poskytování marketingových služeb: SEO optimalizace, lokální SEO, AI viditelnost, SEO pro e-shopy, linkbuilding, email marketing a související poradenství.</p>
    <h2>2. Cena a fakturace</h2>
    <p>Služby se účtují hodinovou sazbou 12 EUR za odpracovanou hodinu. Fakturace probíhá měsíčně zpětně na základě reportu odpracovaných hodin. Reklamní výdaje a náklady na odkazy či nástroje třetích stran se účtují ve skutečné ceně bez přirážky.</p>
    <h2>3. Doba spolupráce</h2>
    <p>Spolupráce je sjednána na dobu neurčitou s měsíčním cyklem. Klient i poskytovatel mohou spolupráci ukončit ke konci kalendářního měsíce, písemně, bez sankcí.</p>
    <h2>4. Odpovědnost a výsledky</h2>
    <p>Poskytovatel nezaručuje konkrétní pozice ve vyhledávačích ani konkrétní objemy návštěvnosti. Zaručuje odvedenou práci, transparentní vykazování a postup podle dohodnutého plánu. Záruky konkrétních pozic ve vyhledávačích nejsou možné ani poskytovatelem, ani žádnou seriózní agenturou.</p>
    <h2>5. Práva k obsahu</h2>
    <p>Obsah vytvořený pro klienta v rámci placené spolupráce přechází na klienta po zaplacení faktury. Poskytovatel může práci ukázat v portfoliu po dohodě s klientem.</p>
    <h2>6. Proti spamu a praxím</h2>
    <p>Poskytovatel nepoužívá praktik, které porušují pokyny vyhledávačů (nákup odkazů ze sítí automatizovaného spamu, skryté texty, duplicitní obsah). Porušení pokynů hrozí sankcí, proto je vyhýbáme zásadně.</p>
  </div>
</section>
"""
    html = base(market="cz", path="terms/", title="Obchodní podmínky | Nokto Studio",
                desc="Obchodní podmínky Nokto Studio: hodinová sazba 12 EUR, měsíční fakturace, bez vázanosti, transparentní vykazování.",
                canonical=BASE + "/cz/terms/", body=body, prefix="../..", extra_head=ORG_SCHEMA_CZ)
    return ("cz/terms/index.html", html)
