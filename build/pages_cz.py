# -*- coding: utf-8 -*-
"""Nokto Studio - CZ page content (localized for Czech market, targeting CZ keywords)."""
from engine import (base, page_hero, cta_band, faq_block, faq_schema,
                    steps_block, price_cards, benefit_cards, schema_service,
                    results_slider, result_block, partner_logo_card,
                    ORG_SCHEMA_CZ, EMAIL, BASE, PHONE_TEL, PHONE_DISPLAY, gicon, _bars, _sparkline,
                    _VIOLET_L, _VIOLET, _ORANGE, _CERULEAN)

# ---------------------------------------------------------------- shared

CZ_TRUST = """
<div class="trust-strip">
  <div class="container">
    <div class="trust-grid">
      <div class="trust-stat reveal" data-delay="100">
        <span class="trust-num tn-violet">12&nbsp;EUR</span>
        <span class="trust-label">transparentní hodinová<br>sazba, žádné paušály</span>
      </div>
      <div class="trust-stat reveal" data-delay="200">
        <span class="trust-num tn-orange">0 EUR</span>
        <span class="trust-label">první hovor a audit<br>webu jsou bezplatné</span>
      </div>
      <div class="trust-stat reveal" data-delay="300">
        <span class="trust-num tn-cerulean">1. den</span>
        <span class="trust-label">bezplatný audit<br>začíná hned po prvním hovoru</span>
      </div>
      <div class="trust-stat reveal" data-delay="400">
        <span class="trust-num tn-violet-light">30 min</span>
        <span class="trust-label">měsíční report<br>jako hovor se mnou</span>
      </div>
    </div>
  </div>
</div>
"""

CZ_PROCESS_STEPS = [
    {"title": "Bezplatný audit", "text": "Začínáme 30minutovým hovorem a bezplatným auditem webu. Uvidíte přesně, co brzdí pozice, prodej a doporučení v AI."},
    {"title": "Plán podle priorit", "text": "Z auditu vyrobíme jasný plán: co opravit jako první, která klíčová slova přinášejí zákazníky a kolik hodin měsíčně to zabere."},
    {"title": "Práce v týdenních dávkách", "text": "Dělám: technika, obsah, firemní profil, AI viditelnost, odkazy. Vždy víte, co se stalo v uplynulém týdnu."},
    {"title": "Měření a report", "text": "Měsíční report dostáváte osobně: 30minutový telefonát se mnou. Pozice, kliky z Googlu, objednávky, zmínky v AI. Platíte jen za odpracované hodiny."},
]


def cz_process_section(label: str = "Jak pracuji") -> str:
    return f"""
<section class="section section-alt" id="proces">
  <div class="container">
    <div class="section-head">
      <span class="section-label">{label}</span>
      <h2>Čtyři kroky. Žádné pevné smlouvy.</h2>
      <p class="section-subheading">Vždy víte, co dělám, proč a co to přineslo. Každá hodina je vykazována.</p>
    </div>
    {steps_block(CZ_PROCESS_STEPS)}
  </div>
</section>
"""


# ---------------------------------------------------------------- HOME

CZ_HOME_FAQ = [
    ("Kolik stojí SEO optimalizace webu?",
     "Za práci platíte 12 EUR za hodinu. Menší web zvládnu za 10 hodin měsíčně (120 EUR), větší e-shop za 40 hodin (480 EUR). Přesný rozsah potvrdím v plánu po bezplatném auditu."),
    ("Jak dlouho trvá, než SEO přinese výsledky?",
     "První pohyby na méně konkurenčních klíčových slovech obvykle do 2 až 4 měsíců. Na hlavní dotazy v konkurenčních oborech 6 až 12 měsíců. Realistické termíny řeknu už v auditu."),
    ("Uvidím, za co platím?",
     "Ano. Každý měsíc dostanete report s odpracovanými hodinami, jejich obsahem a výsledky: pozice, kliky z Google, kontakty a objednávky, zmínky v AI."),
    ("Pomůžete mi, aby mě doporučoval ChatGPT?",
     "Ano, to je moje specializace. Optimalizuji web pro AI nástroje (ChatGPT, Gemini, AI Overviews) tak, aby vás doporučovaly při dotazech vašich zákazníků."),
    ("Jsou smlouvy vážoucí na 12 měsíců?",
     "Ne. Pracuji měsíčně, spolupráci můžete kdykoli ukončit. Důvěru stavím na výsledcích, ne na vázanosti."),
]

# Tri pilíře viditelnosti + podpůrné služby + partnerské doplňky.
CZ_PILLARS = [
    ("/cz/sluzby/seo-pre-ai-vyhledavace/", "AI viditelnost",
     "ChatGPT, Gemini a Google AI Overviews vás doporučí zákazníkům jako první volbu.", "ai", "#9B6FD9"),
    ("/cz/sluzby/seo-optimalizace/", "Google viditelnost",
     "Pozice v Google, které přinášejí zákazníky, nejen návštěvnost.", "search", "#6A3FC4"),
    ("/cz/sluzby/lodalne-seo/", "Google Mapy viditelnost",
     "Firemní profil, Mapy a hodnocení. Zákazníci z okolí vás najdou jako první.", "pin", "#F75940"),
]
CZ_SUPPORT = [
    ("/cz/sluzby/seo-pre-eshopy/", "SEO pro e-shopy",
     "Více prodeje z kategorií a produktů. Shoptet, Marketplace, Google Shopping.", "shop", "#1DACD6"),
    ("/cz/sluzby/seo-audit/", "SEO audit a analýza",
     "Přesný obraz toho, co váš web brzdí, s akčním plánem podle priorit.", "audit", "#6A3FC4"),
    ("/cz/sluzby/linkbuilding/", "Linkbuilding",
     "Zpětné odkazy a autorita, bez kterých se nahoru nedostanete.", "link", "#F75940"),
]
CZ_PARTNERS = [
    ("https://flamia.studio", "flamia.png", "Web dizajn: Flamia Studio",
     "Web na míru, který se najde a prodává. Dizajn a vývoj řeší náš partner Flamia Studio."),
    ("https://peterkocur.sk", "peterkocur.png", "PPC reklama: Peter Kocur",
     "Google Ads pro okamžité výsledky, než SEO nabere tempo. Vede ho můj partner Petr Kocur."),
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
    pillars = "".join(_cz_card(*s, ["tag-violet-light", "tag-violet", "tag-orange"][i], (i + 1) * 100)
                      for i, s in enumerate(CZ_PILLARS))
    support = "".join(_cz_card(*s, ["tag-cerulean", "tag-violet", "tag-orange"][i], (i + 1) * 100)
                      for i, s in enumerate(CZ_SUPPORT))
    partners = "".join(partner_logo_card(href, logo, title, text, (i + 1) * 100)
                       for i, (href, logo, title, text) in enumerate(CZ_PARTNERS))
    return (f'<div class="grid-3">{pillars}</div>'
            f'<h3 style="margin:42px 0 22px;">K tomu i podpůrné služby</h3>'
            f'<div class="grid-3">{support}</div>'
            f'<h3 style="margin:42px 0 22px;">Doplňkové služby od partnerů</h3>'
            f'<p style="max-width:720px; margin:0 0 20px; color:var(--text-muted);">Tvorbu webu a PPC reklamu neřeším sám. Nabízím je v tandemu s ověřenými partnery, se kterými pracuji na jednom projektu.</p>'
            f'<div class="partner-band">{partners}</div>')


def cz_home() -> tuple[str, str]:
    h1 = ('Ať vás zákazníci najdou v <span class="hl-violet">Google</span>, '
          'na <span class="hl-orange">Google Mapách</span> i v <span class="hl-cerulean-light">ChatGPT</span>.')
    sub = ("Jmenuji se Šimon Štermenský a SEO dělám pro podnikatele bez placené reklamy: "
           "pracuji na obsahu webu, technické stránce webu a profilu na Google Mapách, "
           "aby vás zákazníci našli, když hledají vaše produkty a služby. Za transparentních "
           "12 EUR za hodinu. Bez paušálů, bez pevných smluv, s reportem, kterému rozumíte.")

    body = f"""
<section class="hero">
  <div class="container">
    <div class="hero-flex">
      <div class="hero-content">
        <span class="hero-label">SEO bez placené reklamy · CZ a SK</span>
        <h1>{h1}</h1>
        <p class="hero-sub">{sub}</p>
        <div class="hero-ctas">
          <a href="tel:+421917316105" class="btn btn-primary btn-lg">Zavolejte +421 917 316 105</a>
          <a href="/cz/kontakt/" class="btn btn-outline btn-lg">Chci bezplatný audit webu</a>
        </div>
        <p class="hero-scarcity">Nebo napište: <a href="/cz/kontakt/" style="font-weight:700; color:var(--text); text-decoration:none;">kontaktní formulář</a> · <a href="mailto:hello@noktostudio.com" style="font-weight:700; color:var(--text); text-decoration:none;">hello@noktostudio.com</a></p>
        <p class="hero-scarcity" style="margin-top:6px;">Kapacita pro nové projekty: otevřeno od října 2026.</p>
      </div>
      <div class="hero-photo">
        <img src="/assets/img/simon.png" alt="Šimon Štermenský, SEO specialista a majitel Nokto Studio" width="220" height="220" loading="eager">
        <span class="hero-photo-cap">Šimon Štermenský<br>SEO specialista · Nokto Studio</span>
      </div>
    </div>
  </div>
</section>

{CZ_TRUST}

{results_slider("cz")}

<!-- PRE KOHO -->
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Pro koho to dělám?</span>
      <h2>Čtyři věci, které od nás podnikatelé chtějí</h2>
    </div>
    <div class="grid-4">
      <div class="benefit-card card-hover reveal" data-delay="100">
        <span class="benefit-icon icon-violet-light">{gicon("ai", "#9B6FD9", 26)}</span>
        <h3>Ať vás AI doporučí</h3>
        <p>Když si zákazník u ChatGPT nebo Gemini vyžádá doporučení, chcete být v odpovědi. Stavím web tak, aby mu nástroje AI rozuměly a citovaly ho.</p>
      </div>
      <div class="benefit-card card-hover reveal" data-delay="200">
        <span class="benefit-icon icon-orange">{gicon("pin", "#F75940", 26)}</span>
        <h3>Zákazníci z Google a Mapy</h3>
        <p>Lokální vyhledávání a firemní profil Google jsou nejrychlejší cesta k zákazníkům z okolí. Nastavím je a každý týden vyhodnocuji.</p>
      </div>
      <div class="benefit-card card-hover reveal" data-delay="300">
        <span class="benefit-icon icon-cerulean">{gicon("shop", "#1DACD6", 26)}</span>
        <h3>Více prodeje na e-shopu</h3>
        <p>Kategorie a produkty optimalizuji na klíčová slova, která kupují. Google Shopping a Heureku sleduji jako součást systému.</p>
      </div>
      <div class="benefit-card card-hover reveal" data-delay="400">
        <span class="benefit-icon icon-violet">{gicon("grow", "#6A3FC4", 26)}</span>
        <h3>Více poptávek pro služby</h3>
        <p>Služby prodáváme přes obsahové stránky, které odpovídají na otázky zákazníků. Z většího zájmu získáte více poptávek a zakázek.</p>
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
      <h2>12 EUR za hodinu. Platíte jen za odvedenou práci.</h2>
      <p class="section-subheading">Žádné měsíční paušály, u kterých nevíte, co obsahují. Každá hodina je vykazována v reportu.</p>
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
        <img src="/assets/img/simon.png" alt="Šimon Štermenský, SEO specialista a majitel Nokto Studio" width="300" height="300" loading="lazy">
      </div>
      <div class="reveal" data-delay="150">
        <span class="section-label">Kdo za Nokto stojí</span>
        <h2 style="margin:10px 0 14px;">S vámi komunikuji já, ne account manager.</h2>
        <p style="color:var(--text-muted);">Jsem Šimon, SEO specialista. Za roky praxe v online marketingu mě nejvíc baví SEO a viditelnost v Google i AI nástrojích, protože vidím, jak reálně mění prodej malých firem. Pracuji s malým týmem a s partnery na webdesignu a PPC reklamě, takže vám vždy odpoví ten, kdo práci dělá.</p>
        <p style="color:var(--text-muted);">První hodina s vámi je bezplatný hovor a audit. Pokud vám čísla nedají smysl, nic neplatíte.</p>
        <a href="/cz/kontakt/" class="btn btn-primary" style="margin-top:18px;">Dohodnout si hovor se mnou</a>
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
    {cta_band("Začněte bezplatným auditem", "30 minut telefonátu a bezplatný audit vašeho webu. Dozvíte se, co brzdí vaše pozice a prodej, i když se nakonec rozhodnete pro jinou cestu.", "cz")}
  </div>
</section>
"""
    html = base(market="cz", path="", title="Nokto Studio | SEO agentura pro podnikatele: Google i ChatGPT",
                desc="SEO agentura pro podnikatele. Zákazníci z Google a Google Maps, doporučení v ChatGPT a AI nástrojích, více prodejů na e-shopu. 12 EUR za hodinu, bezplatný audit.",
                canonical=BASE + "/cz/", body=body, prefix="..",
                extra_head=ORG_SCHEMA_CZ + faq_schema(CZ_HOME_FAQ, BASE + "/cz/"))
    return ("cz/index.html", html)


# ---------------------------------------------------------------- SERVICE PAGES (CZ)

def _cz_service(*, slug: str, title: str, desc: str, label: str, h1: str,
                intro: str, for_who: list[str], deliverables: list[str],
                faq: list[tuple[str, str]], svc_name: str,
                proof: dict | None = None, time_estimate: str = "8 až 20 hodin měsíčně") -> tuple[str, str]:
    url = BASE + f"/cz/sluzby/{slug}/"
    who = "".join(f"<li>{w}</li>" for w in for_who)
    deliv = "".join(f'<li><span class="check">✓</span><span>{d}</span></li>' for d in deliverables)
    proof_html = ""
    if proof:
        nums = "".join(
            f'<div><strong style="color:{n[2]};">{n[0]}</strong><span>{n[1]}</span></div>'
            for n in proof["numbers"])
        proof_html = f"""
<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Výsledek z praxe</span>
      <h2>{proof['title']}</h2>
    </div>
    <div class="case-result proof-band">{nums}</div>
    <p style="margin-top:16px; max-width:720px; color:var(--text-2);">{proof['caption']}</p>
    <p style="margin-top:4px; font-size:0.8rem; color:var(--text-muted);">{proof['source']}</p>
  </div>
</section>"""
    body = f"""
{page_hero(label, h1, intro, [("Domů", "/cz/"), ("Služby", "/cz/sluzby/"), (label.replace("Služba · ", ""), None)])}

<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:start;">
      <div class="prose">
        <h2>Pro koho je tato služba?</h2>
        <ul>{who}</ul>
      </div>
      <div class="card">
        <span class="section-label">Co dodávám</span>
        <ul class="deliv-list">{deliv}</ul>
      </div>
    </div>
  </div>
</section>

{proof_html}

{cz_process_section("Jak bude probíhat spolupráce?")}

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Ve zkratce</span>
      <h2>Klíčové věci, na které se ptáte</h2>
    </div>
    <div class="case-result proof-band">
      <div><strong>Pro koho</strong><span>{' '.join(for_who[:1]).split('.')[0][:80] or 'firmy a e-shopy'}</span></div>
      <div><strong>Časový odhad</strong><span>{time_estimate}</span></div>
      <div><strong>Cena</strong><span>12 EUR za hodinu, vykazované v reportu</span></div>
      <div><strong>Další krok</strong><span><a href="/cz/kontakt/" style="color:var(--brand-primary-deep); font-weight:700;">Bezplatný vstupní audit</a></span></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="rate-band">
      <div>
        <div class="rate-big">12 EUR <small>za hodinu · kdykoliv skončíte</small></div>
        <p style="margin-top:8px; max-width:520px;">Časový odhad této služby: {time_estimate}, podle rozsahu webu a konkurence.</p>
      </div>
      <div class="hero-ctas">
        <a href="/cz/kontakt/" class="btn btn-primary btn-lg">Bezplatný hovor</a>
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
    {cta_band("Chcete vědět, co by tato služba přinesla vašemu webu.", "Bezplatný audit a 30 minut času. Žádné závazky.", "cz")}
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
        time_estimate="10 hodin měsíčně pro firemní web (120 EUR), e-shop 20 až 40 hodin",
        h1="SEO optimalizace, která přivede zákazníky",
        intro="Zákazník, který vás hledá v Googlu, je nejlevnější zákazník. Postavím web tak, aby mu Google rozuměl, zařadil ho nahoru a návštěvníci odcházeli s odpovědí, ne s otazníkem.",
        for_who=[
            "Máte web, který nepřináší kontakty ani objednávky z vyhledávání.",
            "Konkurence vás předbíhá na dotazech, které vás zajímají.",
            "Jste vidět jen na názvu firmy, ne na tom, co prodáváte.",
            "Platíte reklamu a rádi byste část dotazů zachytili zdarma.",
        ],
        deliverables=[
            "Analýza klíčových slov: po čem zákazníci opravdu hledají a co stojí za námahu.",
            "Technická oprava webu: rychlost, indexace, kanonizace, chyby 404, sitemap.",
            "Přepis titulků a popisků na dotazy se skutečnou poptávkou.",
            "Nové obsahové stránky pro dotazy, kde konkurence není silná.",
            "Interní prolinkování, které posune silné stránky výše.",
            "Měsíční report osobně: 30minutový hovor se mnou, pozice, kliky ze Search Console, objednávky.",
        ],
        faq=[
            ("Kolik hodin měsíčně zabere SEO optimalizace?",
             "Firemní web zvládnu za 10 hodin měsíčně (120 EUR), e-shop za 20 až 40 hodin (240 až 480 EUR). Rozsah potvrdím v plánu po auditu."),
            ("Za jak dlouho se projeví výsledky?",
             "První pohyby na méně konkurenčních dotazech za 2 až 4 měsíce, na hlavní dotazy 6 až 12 měsíců. Záleží na konkurenci a stavu webu."),
            ("Děláte i obsah? Nemám čas psát.",
             "Ano, psaní obsahu je součástí hodin. Sám navrhnu strukturu, napíšu texty a před publikací je schválíte."),
            ("Co když jsem SEO už dělal a nic to nepřineslo?",
             "Bezplatný audit přesně řekne, co předchozí práce nechala nedokončené. Často chybí dva až tři kroky, ne celé SEO."),
        ],
        svc_name="SEO optimalizace webu",
        proof={
            "title": "Kliky z Google: +355 % za 3 měsíce spolupráce",
            "numbers": [("250", "kliků za 3 měsíce", "#6A3FC4"),
                        ("+355 %", "růst oproti předchozímu období", "#F75940"),
                        ("8 950", "zobrazení měsíčně (+246 %)", "#1DACD6")],
            "caption": "Firemní web, který jsem převzal s minimální organickou návštěvností. Práce: technická oprava, obsahové stránky na reálné dotazy zákazníků a měsíční vyhodnocení. Růst přicházel každý měsíc, bez jednorázového skoku.",
            "source": "Zdroj: Google Search Console klienta, ukázka ze září 2026.",
        },
    )


def cz_lodalne_seo() -> tuple[str, str]:
    return _cz_service(
        slug="lodalne-seo",
        title="Lokální SEO a firemní profil Google Mapy | Nokto Studio",
        desc="Lokální SEO: firemní profil Google, Google Mapy, hodnocení a lokální klíčová slova. Zákazníci z okolí vás najdou první. 12 EUR za hodinu.",
        label="Služba · Lokální SEO",
        time_estimate="8 hodin na nastavení profilu, poté 4 hodiny měsíčně",
        h1="Lokální SEO: zákazníci z okolí vás najdou první",
        intro="Když si někdo vyhledá zubaře, autoservis, kuchyně nebo střechaře ve svém městě, rozhodnou tři věci: Google Mapy, hodnocení a web. Nastavím všechny tři a udržuji je v pořádku.",
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
             "Mám jednoduchý postup přes SMS a QR kód, který zákazníky vyzve hned po provedení služby. Míru recenzí zvyšuje násobně."),
            ("Jak řešíte špatná hodnocení?",
             "Odpovídám profesionálně a na místě. Špatná hodnocení nelze odstranit, ale dobrý poměr a kultivované odpovědi působí na zákazníky víc než počet hvězdiček."),
        ],
        svc_name="Lokální SEO a firemní profil Google",
        proof={
            "title": "359 lidí vidělo firemní profil klienta za jedno sledované období",
            "numbers": [("359", "zobrazení firemního profilu", "#6A3FC4"),
                        ("54 %", "zobrazení přes Google Mapy", "#F75940"),
                        ("46 %", "zobrazení přes Google Search", "#9B6FD9")],
            "caption": "Lokální zákazník hledá dvěma cestami: přes Mapy (54 % zobrazení) a přes běžné Google hledání (46 %). Proto řešíme obojí: profil nastavený na doraz, hodnocení přicházejí pravidelně a web podporuje mapové pozice.",
            "source": "Zdroj: statistiky firemního profilu Google klienta, ukázka ze září 2026.",
        },
    )


def cz_seo_ai() -> tuple[str, str]:
    return _cz_service(
        slug="seo-pre-ai-vyhledavace",
        title="SEO pro AI vyhledávače: ChatGPT a AI Overviews | Nokto Studio",
        desc="Optimalizace pro AI vyhledávače a AI Overviews. ChatGPT a Gemini vás doporučí zákazníkům. Jako první na českém trhu.",
        label="Služba · SEO pro AI",
        time_estimate="6 až 12 hodin první měsíc, poté 4 až 8 hodin měsíčně",
        h1="Ať vás ChatGPT doporučuje zákazníkům",
        intro="Zákazník dnes neptá jen Google. Ptá ChatGPT: \u201eDoporuč mi dobrou ordinaci v Brně.\u201c AI nástroj odpoví dvěma až pěti jmény. Mým úkolem je, aby tam bylo vaše jméno.",
        for_who=[
            "Chcete, aby vás AI nástroje doporučovaly jako první volbu ve vašem oboru?",
            "Vidíte, že zákazníci přicházejí s větou \u201enašlo mi ChatGPT, že...\u201c",
            "Konkurence se na AI doporučování zatím nepřipravuje (to je výhoda).",
            "Máte odbornost a chcete ji mít viditelnou i pro AI, nejen pro Google.",
        ],
        deliverables=[
            "Audit AI viditelnosti: kdo vás dnes ChatGPT, Gemini a AI Overviews cituje a kdo ne.",
            "Přímé odpovědi na stránkách: úvodní odstavce ve formátu, který čerpá AI.",
            "Strukturovaná data (schema.org) pro snadné čtení AI nástroji.",
            "Obsahové stránky odpovídající na reálné otázky zákazníků.",
            "Měsíční sledování: ve kterých AI odpovědích se objevujete a co se změnilo.",
            "Nastavení přístupu pro AI roboty (llms.txt, robots.txt, GPTBot, PerplexityBot).",
        ],
        faq=[
            ("Je toto SEO, nebo marketing?",
             "Je to přímé pokračování SEO. Google i ChatGPT čerpají z webu, rozdíl je v tom, co a jak čtou. Nastavím obojí najednou."),
            ("Jak měříte, jestli mě AI doporučuje?",
             "Pravidelně testuji sadu dotazů, které vaši zákazníci kladou, a zaznamenávám, zda se vaše jméno v odpovědích objevuje. Výsledky máte v reportu."),
            ("Není brzy na to investovat?",
             "Je to právě naopak. Konkurence v AI doporučeních teprve začíná, takže být první je výhoda. První zmínky vidíme často do 2 až 3 měsíců."),
            ("Pro koho to dává smysl?",
             "Pro služby, kde zákazník hledá doporučení: zdravotnictví, právo, servis, stavebnictví, školení. Pro e-shopy pomáhá u dotazů typu \u201ekdo prodává...\" a v recenzích."),
        ],
        svc_name="Optimalizace pro AI vyhledávače",
        proof={
            "title": "13 AI citací e-shopu v Google AI režimu za 3 měsíce",
            "numbers": [("13", "AI citací webu v Google AI režimu", "#9B6FD9"),
                        ("8", "citací jedné stránky /overaly/", "#6A3FC4"),
                        ("3", "citací blogového článku", "#1DACD6")],
            "caption": "Po nasazení našeho obsahu cituje Google AI Mode konkrétní stránky e-shopu přímo v odpovědích zákazníkům. Nejvíce citovaná stránka má 8 citací, blogový článek 3. Konkurence v AI odpovědích na tyto dotazy ještě není, takže první jména tam zůstávají.",
            "source": "Zdroj: Google AI Mode (report citací), ukázka ze srpna 2026.",
        },
    )


def cz_eshop_seo() -> tuple[str, str]:
    return _cz_service(
        slug="seo-pre-eshopy",
        title="SEO pro e-shopy: Shoptet a Google Shopping | Nokto Studio",
        desc="SEO optimalizace e-shopu: kategorie, produkty, Shoptet, Marketplace i Google Shopping. Více prodejů z organického vyhledávání. 12 EUR za hodinu.",
        label="Služba · SEO pro e-shopy",
        time_estimate="20 až 40 hodin měsíčně (240 až 480 EUR)",
        h1="E-shop SEO: více objednávek z Google",
        intro="E-shop má jediné skutečné měřítko úspěchu: objednávky. Optimalizuji kategorie a produkty na dotazy, které kupují, aby vás Google i Marketplace našli bez placení za každý klik.",
        for_who=[
            "Máte e-shop (Shoptet, WooCommerce, vlastní řešení) a prodej závisí na reklamě.",
            "Kategorie nemají vlastní texty a neprodávají samy od sebe.",
            "Jste vidět jen na názvech produktů, ne na tom, co zákazník skutečně hledá.",
            "Chcete snížit náklady na reklamu tím, že část dotazů zachytíte zdarma?",
        ],
        deliverables=[
            "Analýza klíčových slov pro kategorie a klíčové produkty.",
            "Texty kategorií a produktů, které prodávají, nejen popisují.",
            "Technická hygiena: kanonizace, filtrovaná URL, rychlost, produktová data.",
            "Google Merchant Center a Google Shopping v pořádku.",
            "Poradenství pro Heureku a Marketplace integrace.",
            "Report v objednávkách a tržbách z organického kanálu.",
        ],
        faq=[
            ("Děláte SEO i pro Shoptet?",
             "Ano, Shoptet je v Česku nejrozšířenější platforma a známe její specifika (filtry, varianty, SEO moduly)."),
            ("Kolik objednávek z toho bude?",
             "Reálná čísla vám řeknu po auditu, na základě vašich klíčových slov a jejich poptávky. Nikdy nenabídnu číslo, které nedokážu podpořit daty."),
            ("Musím dělat i linkbuilding?",
             "Pro konkurenční kategorie ano, odezva bez autority je pomalá. Doporučíme rozsah, který dává smysl pro váš rozpočet."),
            ("Jak měříte úspěch?",
             "V Google Analytics a Search Console sleduji objednávky a tržby z organického vyhledávání. Report dostáváte měsíčně."),
        ],
        svc_name="SEO pro e-shopy",
        proof={
            "title": "E-shop (klient): 2 492,75 EUR tržeb za 9 měsíců",
            "numbers": [("2 492,75 EUR", "tržby za 9 měsíců", "#6A3FC4"),
                        ("15", "Objednávek z e-mailu a organiky.", "#9B6FD9"),
                        ("722 EUR", "největší objednávka", "#1DACD6")],
            "caption": "Regionální dodavatel s e-shopem na vlastní platformě, API integrací na účetní systém a e-mail marketingem. Objednávky chodí z kanálů e-mail a organický Google. Součástí je i lokální SEO a optimalizace pro AI vyhledávače.",
            "source": "Zdroj: objednávky připsané do kanálů e-mail a organický Google, 9 měsíců.",
        },
    )


def cz_audit() -> tuple[str, str]:
    return _cz_service(
        slug="seo-audit",
        title="SEO audit webu a analýza klíčových slov | Nokto Studio",
        desc="SEO audit webu s akčním plánem: technika, obsah, klíčová slova, konkurence. Bezplatný vstupní audit, detailní od 12 EUR za hodinu.",
        label="Služba · SEO audit",
        time_estimate="vstupní audit zdarma do 3 dní, detailní audit 20 až 40 hodin (240 až 480 EUR)",
        h1="SEO audit: přesný obraz toho, co váš web brzdí",
        intro="Audit není PDF do šuplíku. Je to seznam úloh s prioritami a odhadem hodin. Začíná bezplatným vstupním auditem, který máte do tří dnů.",
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
             "Ano. Plán je ve srozumitelném formátu s úlohami krok za krokem, přímo pro CMS nebo vývojáře."),
            ("Musím potom brát i další služby?",
             "Ne. Plán si můžete provést sami nebo s jiným partnerem. Pokud se rozhodnete s námi spolupracovat, plán slouží jako základ."),
            ("Jak rychle dostanu audit?",
             "Vstupní audit do 3 pracovních dnů od prvního hovoru. Detailní audit za 7 až 10 dnů."),
        ],
        svc_name="SEO audit a analýza klíčových slov",
        proof={
            "title": "Jen 6 nových stránek zvedlo celý web o 11 000 zobrazení.",
            "numbers": [("11 000", "zobrazení měsíčně (+14 %)", "#1DACD6"),
                        ("+43 %", "kliků v posledním týdnu", "#6A3FC4"),
                        ("6", "stránek, které to udělaly", "#9B6FD9")],
            "caption": "Toto je síla správného plánu: nezůstávat u 300 stránek webu, ale přidat 6 přesně zacílených obsahových stránek na dotazy, na které se zákazníci reálně ptají. Přesně takové příležitosti audit hledá jako první.",
            "source": "Zdroj: Google Search Console, ukázka ze září 2026.",
        },
    )


def cz_linkbuilding() -> tuple[str, str]:
    return _cz_service(
        slug="linkbuilding",
        title="Linkbuilding a zpětné odkazy | Nokto Studio",
        desc="Linkbuilding: zpětné odkazy a autorita webu. Bezpečné metody, reálné domény, transparentní vykazování. 12 EUR za hodinu.",
        label="Služba · Linkbuilding",
        time_estimate="4 až 8 hodin měsíčně, cena odkazů vykazovaná zvlášť",
        h1="Linkbuilding: autorita, která drží pozice",
        intro="Technika a obsah vás dovedou do středu výsledků, autorita vás posune nahoru. Stavím odkazy, které Google akceptuje a zákazníci citují.",
        for_who=[
            "Máte technicky v pořádku web i obsah, ale pozice stagnují.",
            "Konkurence má silnější link profil a předbíhá vás.",
            "Chcete odkazy z reálných českých a slovenských domén, ne ze spamu.",
            "Chcete transparentní vykazování, kde odkazy vznikly a co stály?",
        ],
        deliverables=[
            "Rozbor link profilu: co vás brzdí, které odkazy chybí.",
            "Tematické a lokální odkazy: adresáře, obory, média, partneři.",
            "Připravené obsahy a PR články, které nesou odkazy.",
            "Sledování nových i ztracených odkazů.",
            "Jasná cena za odkaz, bez skrytých přirážek.",
            "Měsíční přehled: nové domény, posun pozic.",
        ],
        faq=[
            ("Kolik stojí odkazy?",
             "Cena odkazu závisí na doméně. Většina českých odkazů stojí 1 200 až 7 500 Kč, mediální PR články víc. Vykazujeme skutečné ceny bez přirážky."),
            ("Jak dlouho trvá, než odkazy pomohou?",
             "Nové odkazy se projeví za 4 až 12 týdnů. Proto kombinujeme linkbuilding s obsahovou prací, která něco přináší už teď."),
            ("Kupujete odkazy?",
             "Pracujeme jen s reálnými, viditelnými místy. Nikdy nepoužíváme sítě automatizovaného spamu, které Google dříve nebo později sankcionuje."),
            ("Kolik odkazů potřebuji měsíčně?",
             "Menší firemní web 2 až 5, e-shop v konkurenčním oboru 5 až 10. Vyšší čísla ne vždy znamenají lepší výsledek."),
        ],
        svc_name="Linkbuilding",
        proof={
            "title": "Růst každý měsíc: 250 kliků za 3 měsíce spolupráce",
            "numbers": [("250", "kliků za 3 měsíce (+355 %)", "#6A3FC4"),
                        ("8 950", "zobrazení (+246 %)", "#F75940"),
                        ("5", "měsíců měřeného růstu", "#9B6FD9")],
            "caption": "Odkazy fungují jen v kombinaci s obsahem a technikou. Toto je výsledek celého systému: obsahové stránky na reálné dotazy, interní prolinkování a odkazy z reálných českých a slovenských domén. Posun přicházel každý měsíc.",
            "source": "Zdroj: Google Search Console klienta, ukázka ze září 2026.",
        },
    )


# ---------------------------------------------------------------- CENIK

CZ_PACKAGES = [
    {"name": "Start", "hours": 10, "price": 120,
     "items": ["Audit webu a analýza klíčových slov", "Technická oprava webu", "2 obsahové stránky nebo přepisy", "Firemní profil Google v pořádku", "Měsíční report: 30minutový hovor se mnou"],
     "cta": "/cz/kontakt/"},
    {"name": "Růst", "hours": 20, "price": 240, "featured": True,
     "items": ["Vše ze startu", "4 až 6 obsahových stránek měsíčně", "Optimalizace pro AI vyhledávače", "Interní prolinkování a CRO tipy", "Linkbuilding (2 až 3 odkazy)", "Měsíční report a hovor 30 min"],
     "cta": "/cz/kontakt/"},
    {"name": "E-shop", "hours": 40, "price": 480,
     "items": ["Vše z růstu", "Texty kategorií a produktů", "Google Merchant Center a Shopping", "Poradenství Heureka / Marketplace", "Automatizace email marketingu", "Report s tržbami z organiky"],
     "cta": "/cz/kontakt/"},
]

CZ_CENIK_FAQ = [
    ("Kolik stojí SEO optimalizace webu?",
     "Platíte 12 EUR za každou odpracovanou hodinu. Firemní web obvykle potřebuje 10 hodin měsíčně (120 EUR), e-shop 20 až 40 hodin (240 až 480 EUR). Rozsah si nastavíte sami a můžete ho kdykoliv měnit."),
    ("Proč je to levnější než konkurence?",
     "Nemáme kanceláře ani manažerské vrstvy. Práci automatizujeme tam, kde automatizace nic nezkazí, a odbornou energii dáváme tam, kde se počítá. Úspory přenášíme na vás."),
    ("Co je v ceně zahrnuto?",
     "Vše kromě reklamních výdajů a nákladů na odkazy či nástroje třetích stran. Ty vám vykazuji ve skutečné ceně, bez přirážky."),
    ("Musím platit měsíčně předem?",
     "Fakturuji měsíčně zpětně za skutečně odpracované hodiny, s fakturou. Paušál není potřeba."),
    ("Můžu spolupráci kdykoliv ukončit?",
     "Ano, kdykoliv, bez sankcí a bez závazků. Důvěru si zasloužíme výsledky."),
    ("Jak vím, že práce byla odvedena?",
     "Každý měsíc dostanete seznam úloh s hodinami a jejich výsledkem. Vy jste ten, kdo kontroluje."),
]


def cz_cenik() -> tuple[str, str]:
    body = f"""
{page_hero("Ceník", "Ceník: 12 EUR za hodinu, bez paušálů",
           "Platíte za odpracované hodiny. Každá hodina je vykazována v reportu. Spolupráci můžete kdykoliv ukončit.",
           [("Domů", "/cz/"), ("Ceník", None)])}

<section class="section">
  <div class="container">
    <div class="rate-band">
      <div>
        <div class="rate-big">12 EUR <small>za hodinu práce</small></div>
        <p style="margin-top:8px; max-width:560px;">SEO optimalizace, lokální SEO, AI viditelnost, obsah, linkbuilding, weby i PPC. Jedna sazba, jednoduché počty.</p>
      </div>
      <a href="/cz/kontakt/" class="btn btn-primary btn-lg">Nezávazná nabídka</a>
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
          <li><span class="check">✓</span><span>Veškerá práce: technika, obsah, firemní profil, AI viditelnost, odkazy, weby, PPC.</span></li>
          <li><span class="check">✓</span><span>Měření a reportování: Search Console, Analytics, pozice, konverze, zmínky v AI.</span></li>
          <li><span class="check">✓</span><span>Komunikace: měsíční 30minutový telefonát se mnou, neomezené otázky mezitím.</span></li>
        </ul>
        <h2>Co není v ceně</h2>
        <ul class="deliv-list">
          <li><span class="check" style="background:#FDEBE8;color:var(--brand-warm-deep);">×</span><span>Reklamní výdaje (Google Ads, Meta Ads). Platíte přímo Googlu, ne nám.</span></li>
          <li><span class="check" style="background:#FDEBE8;color:var(--brand-warm-deep);">×</span><span>Náklady na odkazy a PR články. Vykazujeme skutečnou cenu média.</span></li>
          <li><span class="check" style="background:#FDEBE8;color:var(--brand-warm-deep);">×</span><span>Pronájem placených nástrojů třetích stran, pokud je potřeba (např. platební brána, hosting).</span></li>
        </ul>
      </div>
      <div class="card">
        <span class="section-label">Příklad z praxe</span>
        <p style="margin-bottom:14px;">Firemní web advokátní kanceláře ve městě s 50 000 obyvateli.</p>
        <ul class="deliv-list">
          <li><span class="check">✓</span><span><strong>Měsíc 1:</strong> audit + technická oprava + firemní profil (12 h = 144 EUR)</span></li>
          <li><span class="check">✓</span><span><strong>Měsíce 2 až 4:</strong> obsahové stránky na dotazy zákazníků (10 h = 120 EUR)</span></li>
          <li><span class="check">✓</span><span><strong>Měsíce 5+</strong>Údržba, linkbuilding, AI viditelnost (8 h = 96 EUR)</span></li>
        </ul>
        <p style="margin-top:14px; font-size:0.9rem; color:var(--text-muted);">Reálná čísla pro váš web potvrdím v bezplatném auditu.</p>
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
{page_hero("Proces", "Jak pracuji: plán, práce, měření",
           "Jasný proces bez černé skříňky. Vždy víte, co dělám, proč a co to přineslo.",
           [("Domů", "/cz/"), ("Jak pracuji", None)])}

<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Dva pilíře</span>
      <h2>Dva hlavní pilíře mé práce</h2>
      <p class="section-subheading">Takto zákazníkům pomáhám růst v Google a AI vyhledávání. Jeden bez druhého nefunguje.</p>
    </div>
    <div class="grid-2">
      <div class="benefit-card card-hover">
        <span class="benefit-icon">{gicon("search", "#6A3FC4", 26)}</span>
        <h3>Psaní obsahu</h3>
        <p>Expertní články a texty stránek na dotazy, které zákazníci skutečně ptají. Obsah, který Google cituje i v AI odpovědích a doporučuje zákazníkům.</p>
      </div>
      <div class="benefit-card card-hover">
        <span class="benefit-icon">{gicon("audit", "#9B6FD9", 26)}</span>
        <h3>Opravy technických věcí na webu</h3>
        <p>Technické SEO: rychlost, indexace, kanonizace, interní prolinkování a čistá struktura webu. Základ, na kterém obsah funguje.</p>
      </div>
    </div>
  </div>
</section>
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
          <li><span class="check">✓</span><span>Pozice na sledovaných klíčových slovech (trend, nejen číslo).</span></li>
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
    <div class="section-head"><span class="section-label">Měření</span><h2>Jak měřím výsledky?</h2></div>
    <table class="metric-table">
      <tr><th>Co sleduji</th><th>Nástroj</th><th>Co to říká</th></tr>
      <tr><td><strong>Pozice</strong></td><td>Sledování klíčových slov</td><td>Na kterých dotazech web roste a kde stagnuje.</td></tr>
      <tr><td><strong>Kliky z Google</strong></td><td>Search Console</td><td>Kolik lidí nás vidí a kolik z nich klikne.</td></tr>
      <tr><td><strong>Kontakty a objednávky</strong></td><td>Google Analytics 4</td><td>Kolik návštěvníků se stalo zákazníky.</td></tr>
      <tr><td><strong>Viditelnost v mapě</strong></td><td>Firemní profil Google</td><td>Kolik lidí vidělo firmu, zatelefonovalo, šlo na trasu.</td></tr>
      <tr><td><strong>AI doporučení</strong></td><td>Pravidelné AI testy</td><td>Zda vás ChatGPT, Gemini a AI Overviews citují.</td></tr>
      <tr><td><strong>Tržby z organiku</strong></td><td>Analytics + e-shop</td><td>Pro e-shopy: přímý vztah SEO úsilí k prodeji.</td></tr>
    </table>
  </div>
</section>
<section class="section" style="padding-top:0;">
  <div class="container">
    {cta_band("Chcete takový proces pro svůj web?", "Začněte bezplatným auditem a 30 minutami času.", "cz")}
  </div>
</section>
"""
    html = base(market="cz", path="jak-pracujeme/", title="Jak pracuji: proces, dodávky a měření výsledků | Nokto Studio",
                desc="Náš SEO proces: bezplatný audit, plán s čísly, týdenní práce, měsíční měření. Pozice, kliky, objednávky a AI doporučení v jednom reportu.",
                canonical=BASE + "/cz/jak-pracujeme/", body=body, prefix="../..", extra_head=ORG_SCHEMA_CZ)
    return ("cz/jak-pracujeme/index.html", html)


def cz_vysledky() -> tuple[str, str]:
    """Výsledky: real numbers from GSC exports, AI Mode and client reports."""
    c_klient1 = _bars([145, 115, 61, 42, 38], _VIOLET_L,
                      ["vypínač", "ceny el.", "přípojka", "zásuvka", "vzduchem"])
    c_klient2 = _bars([413, 412, 407, 407, 385], _VIOLET,
                      ["pyžamo", "body", "trička", "kalhoty", "čelenky"])
    c_itc = _sparkline([40, 55, 48, 62, 58, 75, 70, 88, 95, 92, 110, 121], _VIOLET)
    blocks = "".join([
        result_block(
            title="Elektroservis (klient)", period="březen až září 2026",
            nums=[{"big": "991", "color": _VIOLET, "label": "kliků z Google za 28 dní (+6 %)"},
                  {"big": "72 873", "color": _ORANGE, "label": "zobrazení za 28 dní (+3 %)"},
                  {"big": "96", "color": _VIOLET_L, "label": "citací v AI odpovědích"}],
            chart=c_klient1,
            caption="Dva expertní články, které jsem napsal, Google cituje v AI odpovědích a doporučuje klienta zákazníkům. Web (69 stránek): 9 700 → 12 000 zobrazení za 28 dní (+24 %). Graf: růst hlavních stránek v procentech.",
            source="Google Search Console, posledních 28 dní (do září 2026)",
            partner="", market="cz"),
        result_block(
            title="E-shop s oblečením (vlastní projekt)", period="Search Console + AI Mode, červen až září 2026",
            nums=[{"big": "893", "color": _VIOLET_L, "label": "zobrazení v Google AI Mode za 3 měsíce"},
                  {"big": "+80 %", "color": _VIOLET, "label": "srpen oproti červnu (182 → 329)"},
                  {"big": "413", "color": _ORANGE, "label": "kliků na hlavní kategorii"}],
            chart=_bars([182, 293, 329, 89], _VIOLET_L, ["červ", "čvc", "srp", "zář"]),
            caption="Google AI Mode cituje e-shop denně po nasazení mého obsahu. Růst měsíčně: červen 182, červenec 293, srpen 329. Nejvíc citované: domovská stránka a blogové články (174, 167 a 119 citací). Kategorie mají desítky tisíc organických zobrazení měsíčně. Konkurence v AI odpovědích ještě není.",
            source="Google Search Console + Google AI Mode (report citací), červen až září 2026",
            partner="own", market="cz"),
        result_block(
            title="Aplikace pro reality (klient)", period="posledních 28 dní",
            nums=[{"big": "121", "color": _VIOLET, "label": "kliků z Google (+49 %)"},
                  {"big": "4 390", "color": _ORANGE, "label": "zobrazení (+43 %)"},
                  {"big": "+142 %", "color": _VIOLET_L, "label": "růst hlavní stránky"}],
            chart=c_itc,
            caption="SEO od nuly: technické SEO a obsah v prvním měsíci spolupráce. Google začal přinášet zákazníky hned.",
            source="Google Search Console",
            partner="own", market="cz"),
        result_block(
            title="E-shop s měřicími zařízeními (klient)", period="leden až září 2026, rework v průběhu",
            nums=[{"big": "203", "color": _VIOLET, "label": "kliků z Google od založení"},
                  {"big": "3 266", "color": _ORANGE, "label": "zobrazení od založení"},
                  {"big": "2", "color": _VIOLET_L, "label": "zakázky ještě před dokončením projektu"}],
            chart=_sparkline([402, 415, 677, 415, 33, 12], _VIOLET),
            caption="E-shop s produkty pro monitorování energie. Zakázky přišly ještě před dokončením one-time projektu: web dostává objednávky z organického vyhledávání i přesto, že rework teprve probíhá. Pozice v průměru 10,0, CTR 6,2 %. Po nasazení nové verze očekáváme násobný růst.",
            source="Google Search Console, leden až září 2026",
            partner="flamia", market="cz"),
        result_block(
            title="Villa Paris, Piešťany (SK)", period="rebrand + web + lokální SEO",
            nums=[],
            chart="",
            caption="Premium ubytování. Rebrand, nový web, hotelový copywriting a lokální SEO v jednom systému. Značku a web děláme ve spolupráci s Flamia Studio. Cíl: více přímých rezervací bez provizí portálů.",
            source="příběh projektu na /sk/villa-paris/ (SK)",
            partner="flamia", market="cz"),
    ])
    body = f"""
{page_hero("Výsledky", "Ako jsem pomohl zákazníkům růst v Google a AI vyhledávání",
           "Psaním obsahu a opravami technických věcí na webu. Výsledky z Google Search Console a Google AI Mode.",
           [("Domů", "/cz/"), ("Výsledky", None)])}

<section class="section">
  <div class="container">
    <div class="grid-2">{blocks}</div>
    <p style="text-align:center; margin-top:28px; color:var(--text-muted); font-size:0.9rem;">
      Další výsledky a reference na žádost, včetně kontaktů na klienty. Klienty cituji jen s jejich souhlasem.
    </p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Zpětná vazba</span>
      <h2>Co říká pokračování spoluprací</h2>
      <p class="section-subheading">Nejlepší reference je fakt, že zákazníci zůstávají. Kontakty na klienty poskytnu na žádost, cituji je jen s jejich souhlasem.</p>
    </div>
    <div class="grid-3">
      <div class="benefit-card card-hover">
        <span class="benefit-icon">{gicon("grow", "#9B6FD9", 26)}</span>
        <h3>E-shop: spolupráce pokračuje</h3>
        <p>Zákazník byl spokojený s prvním e-shopem, proto teď děláme rework: více produktů a lepší SEO.</p>
      </div>
      <div class="benefit-card card-hover">
        <span class="benefit-icon">{gicon("ai", "#6A3FC4", 26)}</span>
        <h3>Elektroservis: měsíční spolupráce běží</h3>
        <p>991 kliků a 96 citací v AI odpovědích za posledních 28 dní. Report vychází každý měsíc s čísly.</p>
      </div>
      <div class="benefit-card card-hover">
        <span class="benefit-icon">{gicon("pin", "#F75940", 26)}</span>
        <h3>Villa Paris: projekt běží s Flamia Studio</h3>
        <p>Rebrand, web a lokální SEO v jednom systému. Značku a web děláme ve spolupráci s Flamia Studio.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="grid-2" style="align-items:start;">
      <div class="prose">
        <span class="section-label">Další krok</span>
        <h2>Napište mi nebo volejte</h2>
        <p>Do 24 hodin vám odpovím s prvními nápady pro váš web. Bezplatný vstupní audit: co brzdí vaše pozice, prodej a AI doporučení.</p>
        <p style="margin-top:18px;"><a href="{PHONE_TEL}" class="btn btn-primary btn-lg" style="width:100%;">Zavolejte {PHONE_DISPLAY}</a></p>
        <p style="margin-top:12px;">Nebo email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
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
                <option>Více prodejů na e-shopu</option>
                <option>Nový web nebo redesign</option>
                <option>Něco jiného</option>
              </select>
            </div>
            <div class="form-field full"><label class="form-label" for="msg">Zpráva</label><textarea class="form-textarea" id="msg" name="msg" placeholder="Pár slov o vaší firmě a čeho chcete dosáhnout."></textarea></div>
          </div>
          <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off" aria-hidden="true">
          <input type="hidden" name="_subject" value="Dotaz ze stránky Výsledky - noktostudio.com">
          <button type="submit" class="btn btn-primary" style="margin-top:18px; width:100%;">Poslat zprávu</button>
          <p class="form-note">Odesláním souhlasíte se zpracováním údajů pro účel odpovědi (viz <a href="/cz/privacy/">zásady ochrany osobních údajů</a>).</p>
        </form>
        <div class="form-success" style="display:none; margin-top:16px; background:#F5F1FC; color:var(--brand-cool-deep); padding:16px; border-radius:10px;">
          ✓ Děkuji, zpráva odletěla na {EMAIL}. Ozvu se osobně do 24 hodin. Nebo volejte rovnou: <a href="tel:+421917316105" style="font-weight:700;">+421 917 316 105</a>
        </div>
      </div>
    </div>
  </div>
</section>
"""
    html = base(market="cz", path="vysledky/", title="Výsledky SEO: kliky, zobrazení, AI citace | Nokto Studio",
                desc="Reálné výsledky z Google Search Console: 991 kliků a 96 citací v AI odpovědích pro elektroservis, 893 zobrazení v AI Mode pro e-shop, 203 kliků a zakázky ještě před dokončením projektu. Čísla z praxe.",
                canonical=BASE + "/cz/vysledky/", body=body, prefix="../..", extra_head=ORG_SCHEMA_CZ)
    return ("cz/vysledky/index.html", html)


CZ_FAQ_SECTIONS = [
    ("Všeobecné", [
        ("Co přesně Nokto Studio dělá?",
         "SEO optimalizaci webu, lokální SEO a firemní profil Google, optimalizaci pro AI vyhledávače (ChatGPT, Gemini, AI Overviews), SEO pro e-shopy, SEO audity, linkbuilding, tvorbu webů a PPC reklamu Google Ads. K tomu i e-mail marketing pro e-shopy a firmy."),
        ("Pro jaké firmy pracujete?",
         "Především pro menší a střední firmy: lokální služby (řemeslníci, zdravotnictví, právo, autoservis), e-shopy a firmy s odbornými službami. Působím na trzích Česka a Slovenska."),
    ]),
    ("Cena a smlouvy", [
        ("Kolik stojí SEO?",
         "12 EUR za odpracovanou hodinu. Menší firemní web obvykle 10 hodin měsíčně (120 EUR), e-shop 20 až 40 hodin (240 až 480 EUR). Balíčky jsou doporučené rozsahy, ne povinné paušály."),
        ("Jsou smlouvy vážoucí?",
         "Ne. Spolupráci můžete kdykoli ukončit, bez sankcí. Fakturuji měsíčně za skutečně odpracované hodiny."),
        ("Jsou v ceně zahrnuty reklamní výdaje?",
         "Ne. Reklamu (Google Ads) platíte přímo Googlu. Kampaně řídím za 12 EUR na hodinu. Náklady na odkazy a PR vykazuji ve skutečné ceně."),
    ]),
    ("Proces a výsledky", [
        ("Jak dlouho trvá, než SEO přinese výsledky?",
         "První pohyby na méně konkurenčních dotazech za 2 až 4 měsíce, na hlavní dotazy 6 až 12 měsíců. Lokální SEO a firemní profil se zlepšují často za 4 až 8 týdnů."),
        ("Jak uvidím, že práce byla odvedena?",
         "Měsíční report: odpracované hodiny a jejich obsah, pozice, kliky ze Search Console, kontakty a objednávky z Analytics, viditelnost v mapě a zmínky v AI odpovědích."),
        ("Nabízíte záruky první pozice?",
         "Ne. Nikdo reálně nemůže zaručit první místo v Googlu, kdo to slibuje, prodává fikci. Zaručuji proces, transparentnost a měřitelný postup, který k pozicím vede."),
    ]),
    ("AI a nové vyhledávání", [
        ("Nahradí ChatGPT Google?",
         "Doplní ho, nezničí. Zákazníci dnes hledají obojí. Moje práce pokrývá obojí: klasické pozice v Google i viditelnost v AI odpovědích."),
        ("Jak zjistím, jestli mě AI doporučuje?",
         "Pravidelně testuji sady dotazů, které vaši zákazníci kladou, a zaznamenávám, zda se vaše jméno objevuje v odpovědích ChatGPT, Gemini a Google AI Overviews. Výsledek máte v reportu."),
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
{page_hero("FAQ", "Časté otázky", "Odpovědi na to, na co se mě klienti ptají nejvíc. Pokud vaše otázka chybí, ptejte se přímo.", [("Domů", "/cz/"), ("FAQ", None)])}
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
                desc="Časté otázky: kolik stojí SEO, jak dlouho trvá, jak se měří výsledky, co je SEO pro AI vyhledávače. Nokto Studio, SEO agentura.",
                canonical=BASE + "/cz/faq/", body=body, prefix="../..", extra_head=ORG_SCHEMA_CZ + faq_html)
    return ("cz/faq/index.html", html)


def cz_kontakt() -> tuple[str, str]:
    body = f"""
{page_hero("Kontakt", "Zavolejte nebo napište. Ozveme se osobně.",
           "Nejrychlejší cestou je telefon. Nebo pošlete formulář a do 24 hodin máte odpověď s prvními nápady.",
           [("Domů", "/cz/"), ("Kontakt", None)])}
<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:start;">
      <div class="card" style="text-align:center;">
        <span class="section-label">Zavolejte přímo</span>
        <a href="tel:+421917316105" class="btn btn-primary btn-lg contact-phone-btn" style="width:100%; margin-top:14px; font-size:1.25rem;">+421 917 316 105</a>
        <p style="margin:14px 0 6px; color:var(--text-muted);">Šimon Štermenský, SEO specialista. Většinou zvedám hned, jinak volám zpět do pár hodin.</p>
        <ul class="deliv-list" style="text-align:left; margin-top:20px;">
          <li><span class="check">✓</span><span>30 minut bezplatné konzultace o vašem webu</span></li>
          <li><span class="check">✓</span><span>Bezplatný vstupní audit webu po hovoru</span></li>
          <li><span class="check">✓</span><span>Skutečná čísla: co by SEO u vás mohlo znamenat</span></li>
          <li><span class="check">✓</span><span>Nezávazné. Rozhodnete se, kdy a zda.</span></li>
        </ul>
        <p style="margin-top:22px; border-top:1px solid var(--border-light); padding-top:18px;">
          Email: <a href="mailto:{EMAIL}" style="font-weight:700; color:var(--text);">{EMAIL}</a>
        </p>
        <a href="mailto:{EMAIL}" class="btn btn-outline" style="width:100%; margin-top:10px;">Napsat email</a>
      </div>
      <div class="card contact-form-wrap">
        <span class="section-label">Nebo formulář</span>
        <form class="contact-form-el" style="margin-top:16px;">
          <div class="form-grid">
            <div class="form-field"><label class="form-label" for="name">Jméno a firma *</label><input class="form-input" id="name" name="name" type="text" required></div>
            <div class="form-field"><label class="form-label" for="email">Email *</label><input class="form-input" id="email" name="email" type="email" required></div>
            <div class="form-field full"><label class="form-label" for="url">Adresa webu (pokud ji máte)</label><input class="form-input" id="url" name="url" type="url" placeholder="https://"></div>
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
          <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off" aria-hidden="true">
          <input type="hidden" name="_subject" value="Nový dotaz z webu noktostudio.com">
          <button type="submit" class="btn btn-primary" style="margin-top:18px; width:100%;">Poslat zprávu</button>
          <p class="form-note">Odesláním souhlasíte se zpracováním údajů za účelem odpovědi (viz). <a href="/cz/privacy/">zásady ochrany osobních údajů</a>).</p>
        </form>
        <div class="form-success" style="display:none; margin-top:16px; background:#F5F1FC; color:var(--brand-cool-deep); padding:16px; border-radius:10px;">
          ✓ Děkujeme, zpráva odlétla na {EMAIL}. Ozveme se osobně do 24 hodin. Nebo volejte rovnou: <a href="tel:+421917316105" style="font-weight:700;">+421 917 316 105</a>
        </div>
      </div>
    </div>
  </div>
</section>
"""
    html = base(market="cz", path="kontakt/", title="Kontakt: telefon, email a formulář | Nokto Studio",
                desc="Spojte se s Nokto Studio. Zavolejte +421 917 316 105, napište email nebo použijte kontaktní formulář. Bezplatný vstupní audit webu.",
                canonical=BASE + "/cz/kontakt/", body=body, prefix="../..", extra_head=ORG_SCHEMA_CZ)
    return ("cz/kontakt/index.html", html)


def cz_blog() -> tuple[str, str]:
    topics = [
        ("Návod", "tag-violet", "SEO optimalizace: kompletní návod 2026",
         "Krok za krokem od auditu po měření. Postup pro malé firmy, s reálnými čísly z praxe."),
        ("Ceník", "tag-cerulean", "Kolik stojí SEO v 2026?",
         "Ceny na českém trhu a co za ně dostanete. Proč je cena 12 EUR za hodinu veřejná."),
        ("SEO test", "tag-violet-light", "SEO test: 15bodový kontrolní seznam pro váš web",
         "Projděte si web sami za 30 minut: technika, obsah, firemní profil Google a AI viditelnost."),
        ("Linkbuilding", "tag-orange", "Linkbuilding: co to je, co stojí a jak se dělá bezpečně",
         "Co jsou zpětné odkazy, reálné ceny a bezpečné metody. Co Google sankcionuje."),
        ("Lokální SEO", "tag-violet", "Firemní profil Google: návod od založení po hodnocení",
         "Založení, ověření, kategorie, fotky a hodnocení. Návod s případovou studií."),
        ("WordPress", "tag-cerulean", "SEO pro WordPress: 12 nastavení, která je třeba udělat",
         "Rychlost, permalinky, schéma a pluginy. 12 konkrétních nastavení."),
    ]
    cards = "".join(f"""
<div class="blog-card">
  <div><span class="project-tag {tag}">{cat}</span></div>
  <h3>{t}</h3>
  <p>{d}</p>
  <div class="blog-card-foot"><span class="project-tag tag-muted">Připravujeme</span><span class="blog-read" style="color:var(--text-muted);">Vychází brzy</span></div>
</div>""" for cat, tag, t, d in topics)
    body = f"""
{page_hero("Blog", "Praktické články o SEO a AI",
           "Návody, ceny a kontrolní seznamy z praxe. Každý článek vychází z dotazů, které zákazníci reálně hledají.", [("Domů", "/cz/"), ("Blog", None)])}
<section class="section">
  <div class="container">
    <div class="blog-grid">{cards}</div>
    <div style="text-align:center; margin-top:36px;">
      <p style="color:var(--text-muted);">Chcete se o něčem dozvědět víc už teď? Zavolejte <a href="tel:+421917316105" style="font-weight:700; color:var(--text);">+421 917 316 105</a> nebo napište.</p>
      <a href="/cz/kontakt/" class="btn btn-primary" style="margin-top:14px;">Kontakt</a>
    </div>
  </div>
</section>
"""
    html = base(market="cz", path="blog/", title="Blog o SEO, Mapách Google a AI vyhledávačích | Nokto Studio",
                desc="Praktické články: SEO návod krok za krokem, kolik stojí SEO v roce 2026, SEO test webu, linkbuilding, firemní profil Google a SEO pro WordPress.",
                canonical=BASE + "/cz/blog/", body=body, prefix="../..", extra_head=ORG_SCHEMA_CZ)
    return ("cz/blog/index.html", html)


def cz_privacy() -> tuple[str, str]:
    body = f"""
{page_hero("Ochrana osobních údajů", "Zásady ochrany osobních údajů",
           "Zpracovávám jen data, která potřebuji k odpovědi a spolupráci. Žádný prodej dat třetím stranám.",
           [("Domů", "/cz/"), ("Ochrana osobních údajů", None)])}
<section class="section">
  <div class="container prose">
    <h2>Kdo zpracovává údaje</h2>
    <p>Správcem osobních údajů je Nokto Studio (Šimon Štermenský, provozovatel webových stránek noktostudio.com). Kontakt: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    <h2>Jaké údaje a proč?</h2>
    <ul>
      <li>Kontaktní formulář: jméno, e-mail, adresa webu a zpráva. Účelem je odpovědět na váš dotaz. Formulář odesílá oznámení na náš e-mail.</li>
      <li>Telefonát: číslo, ze kterého voláte, pokud si ho zapisujeme pro zpětné doplnění informací. Účelem je uskutečnit hovor.</li>
      <li>Analytika: anonymizovaná data o návštěvnosti (Google Analytics 4, Microsoft Clarity) pro zlepšování webu.</li>
    </ul>
    <h2>Jak dlouho uchovávám údaje?</h2>
    <p>Kontakty z formulářů a telefonátů uchovávám maximálně 24 měsíců od poslední komunikace, pokud nevznikne spolupráce.</p>
    <h2>Vaše práva</h2>
    <p>Máte právo na přístup k údajům, jejich opravu, výmaz a přenos. Požadavek zašlete na <a href="mailto:{EMAIL}">{EMAIL}</a>Máte také právo podat stížnost u Úřadu pro ochranu osobních údajů.</p>
    <h2>Cookies</h2>
    <p>Web používá analytické cookies po vašem souhlasu (cookie banner). Technické cookies nezbytné pro provoz webu jsou povoleny vždy.</p>
  </div>
</section>
"""
    html = base(market="cz", path="privacy/", title="Zásady ochrany osobních údajů | Nokto Studio.",
                desc="Zásady ochrany osobních údajů webu noktostudio.com: jaké údaje zpracovávám, proč a jaká máte práva.",
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
    <p>Tyto podmínky upravují spolupráci mezi Nokto Studio (dále „poskytovatel“) a klientem při poskytování marketingových služeb: SEO optimalizace, lokální SEO, AI viditelnost, SEO pro e-shopy, linkbuilding, email marketing a související poradenství.</p>
    <h2>2. Cena a fakturace</h2>
    <p>Služby se účtují hodinovou sazbou 12 EUR za odpracovanou hodinu. Fakturace probíhá měsíčně zpětně na základě reportu odpracovaných hodin. Reklamní výdaje a náklady na odkazy či nástroje třetích stran se účtují ve skutečné ceně bez přirážky.</p>
    <h2>3. Doba spolupráce</h2>
    <p>Spolupráce je sjednána na dobu neurčitou s měsíčním cyklem. Klient i poskytovatel mohou spolupráci ukončit ke konci kalendářního měsíce, písemně, bez sankcí.</p>
    <h2>4. Odpovědnost a výsledky</h2>
    <p>Poskytovatel nezaručuje konkrétní pozice ve vyhledávačích ani konkrétní objemy návštěvnosti. Zaručuje odvedenou práci, transparentní vykazování a postup podle dohodnutého plánu. Záruky konkrétních pozic ve vyhledávačích nejsou možné ani poskytovatelem, ani žádnou seriózní agenturou.</p>
    <h2>5. Práva k obsahu</h2>
    <p>Obsah vytvořený pro klienta v rámci placené spolupráce přechází na klienta po zaplacení faktury. Poskytovatel může práci ukázat v portfoliu po dohodě s klientem.</p>
    <h2>6. Proti spamu a praxím</h2>
    <p>Poskytovatel nepoužívá praktiky, které porušují pokyny vyhledávačů (nákup odkazů ze sítí automatizovaného spamu, skryté texty, duplicitní obsah). Porušení pokynů hrozí sankcí, proto se jim zásadně vyhýbáme.</p>
  </div>
</section>
"""
    html = base(market="cz", path="terms/", title="Obchodní podmínky | Nokto Studio",
                desc="Obchodní podmínky Nokto Studio: hodinová sazba 12 EUR, měsíční fakturace, bez závazků, transparentní vykazování.",
                canonical=BASE + "/cz/terms/", body=body, prefix="../..", extra_head=ORG_SCHEMA_CZ)
    return ("cz/terms/index.html", html)


# ---------------------------------------------------------------- CZ /PRIPADY REDIRECT STUB

def cz_vysledky_redirect() -> tuple[str, str]:
    html = """<!DOCTYPE html>
<html lang="cs">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Nokto Studio | Výsledky</title>
  <link rel="canonical" href="https://noktostudio.com/cz/vysledky/">
  <meta http-equiv="refresh" content="0; url=/cz/vysledky/">
</head>
<body>
<p>Pokračujte na <a href="/cz/vysledky/">výsledky</a>.</p>
</body>
</html>
"""
    return ("cz/pripady/index.html", html)
