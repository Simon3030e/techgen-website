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
     "Za práci platíte 12 EUR za hodinu. Menší web zvládnu za 10 hodin měsíčně (120 EUR), větší e-shop za 40 hodin (180 EUR). Přesný rozsah potvrdím v plánu po bezplatném auditu."),
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
        time_estimate="10 hodin měsíčně pro firemní web (120 EUR), e-shop 10 až 15 hodin",
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
             "Firemní web zvládnu za 10 hodin měsíčně (120 EUR), e-shop za 10 až 15 hodin (120 až 180 EUR). Rozsah potvrdím v plánu po auditu."),
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
    """REFRESH 2026-09-16. Target CZ queries: 'seo pro eshopy', 'seo eshop'.
    Better angle: Shoptet-specific technical issues + category vs product SEO split +
    Mikramt real revenue case with concrete numbers, none of which appear in CZ SERP top-10."""
    url = BASE + "/cz/sluzby/seo-pre-eshopy/"
    title = "SEO pro e-shopy: Shoptet, WooCommerce, Google Shopping | Nokto Studio"
    desc = ("SEO pro e-shopy: kategorie, produkty, Shoptet technické problémy, Google Merchant Center, "
            "Heureka a Marketplace. Reálné tržby z organického vyhledávání, 12 EUR za hodinu.")
    label = "Služba · SEO pro e-shopy"
    h1 = "SEO pro e-shopy: více objednávek z Googlu bez placení za každý klik"
    intro = ("SEO pro e-shop je optimalizace kategorií, produktů a technické struktury tak, aby "
             "zákazník, který hledá konkrétní produkt, našel vás v Googlu a nevzal ho konkurentovi. "
             "Neměřím návštěvnost, měřím objednávky a tržby z organického kanálu. Pro Shoptet, "
             "WooCommerce i vlastní platformy. Moje práce stojí 12 EUR za hodinu, obvykle 20 až 40 "
             "hodin měsíčně pro menší až střední e-shop.")

    who = [
        "Máte e-shop na Shoptetu, WooCommerci nebo vlastní platformě a prodej závisí od placené reklamy.",
        "Kategorie nemají unikátní texty a Google je považuje za duplicitní s filtry.",
        "Jste vidět jen na přesných názvech produktů, ne na dotazech, které zákazník reálně hledá.",
        "Google Merchant Center odmítá vaše produkty a nevíte proč.",
        "Chcete snížit náklady na reklamu tím, že část dotazů zachytíte z organického vyhledávání zdarma.",
    ]
    deliv = [
        "Technický audit e-shopu: kanonizace filtrů, duplicitní URL, rychlost, indexace, Core Web Vitals.",
        "Klíčová slova pro kategorie i produkty, s objemy poptávek z Marketing Mineru.",
        "Texty kategorií, které prodávají a nejsou duplicitní s filtry ani s popisy výrobce.",
        "Texty produktů, které reálně odpovídají na otázky zákazníka a nejsou copy-paste z feedu.",
        "Google Merchant Center: feed struktura, atributy, schválení produktů, zaměření na Shopping.",
        "Heureka, Nakupujte, Mall: integrace a feed optimalizace pro porovnávače.",
        "Interní prolinkování: kategorie mezi sebou, související produkty, blok doporučení.",
        "Report v objednávkách a tržbách z organického kanálu, nejen v návštěvnosti.",
    ]

    faq = [
        ("Děláte SEO i pro Shoptet?",
         "Ano, Shoptet je nejrozšířenější platforma v Česku a znám její specifika. Nejčastější "
         "problémy: duplicitní URL při filtroch (Shoptet generuje parametrické URL bez canonical), "
         "chybějící H1 na kategoriích, copy-paste popisy produktů z feedu výrobce, a pomalé "
         "načítání kvůli velkým obrázkům. Řeším všechny přes Shoptet SEO modul nebo vlastní úpravy "
         "šablony, pokud máte verzi PRO."),
        ("Kolik objednávek z toho bude?",
         "Reálná čísla vám řeknu po auditu, na základě vašich klíčových slov a jejich objemu poptávky. "
         "Nikdy nenabídnu číslo, které nedokážu podpořit daty. Mikramt.sk, menší e-shop, po 9 "
         "měsících SEO práce: 15 objednávek z organického a e-mailového kanálu, 2492,75 EUR tržeb, "
         "největší objednávka 722 EUR. Vaše čísla závisí na vašem oboru, ceně a konkurenci."),
        ("Musím dělat i linkbuilding?",
         "Pro konkurenční kategorie (móda, elektronika, kosmetika) ano, bez autority je odezva "
         "pomalá a pozice přijdou až za rok. Pro specifické výrobky a malou konkurenci může "
         "postačit technická optimalizace a obsah kategorií. Po auditu doporučím rozsah, který "
         "dává smysl pro váš rozpočet, a cena odkazů bude vykazovaná zvlášť."),
        ("Jak měříte úspěch SEO pro e-shop?",
         "V Google Analytics 4 sleduji objednávky, tržby a konverzní poměr z organického "
         "vyhledávání. V Search Console kliky a zobrazení na produktové a kategoriové dotazy. "
         "V Google Merchant Centre schválení a výkonnost produktů v Shopping. Report dostáváte "
         "měsíčně, v něm reálné tržby z organického kanálu, nejen návštěvnost."),
        ("Co s Google Merchant Center, když mi odmítá produkty?",
         "Nejčastější důvody zamítnutí: chybějící GTIN nebo MPN, nekonzistentní data mezi feedem "
         "a e-shopem, politika reklam (například doplňky výživy), nízká kvalita obrázků, nebo "
         "produktové URL, které jsou canonical na filtrovanou verzi. Audituji feed, opravím "
         "atributy a podám žádost o re-schválení. Bez toho Shopping nefunguje."),
        ("Jak dlouho trvá, než e-shop začne růst z organického vyhledávání?",
         "První pohyby na méně konkurenčních produktových dotazech za 2 až 3 měsíce. Na "
         "kategoriové dotazy 4 až 8 měsíců. Plný potenciál, pokud spolu s linkbuildingem, "
         "12 až 18 měsíců. E-shop, který má 1000 produktů a žádný obsah kategorií, potřebuje "
         "nejméně 6 měsíců na to, aby Google vůbec pochopil, co prodává."),
    ]

    platform_table = """
<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Platformy</span>
      <h2>SEO pro Shoptet, WooCommerce a vlastní e-shopy: konkrétní rozdíly</h2>
      <p class="section-subheading">Každá platforma má jiné technické problémy. Tady jsou ty, které v auditu řeším jako první.</p>
    </div>
    <table class="metric-table">
      <tr><th>Aspekt</th><th>Shoptet</th><th>WooCommerce</th><th>Vlastní platforma</th></tr>
      <tr><td><strong>Duplicitní URL filtrů</strong></td><td>Ano, běžný problém, řeší canonical tag</td><td>Ano, závisí na pluginu, často chybí</td><td>Závisí na implementaci, často chybí</td></tr>
      <tr><td><strong>H1 na kategoriích</strong></td><td>Šablona generuje, dá se upravit přes SEO modul</td><td>Téma generuje, dá se přepsat</td><td>Treba nakódovat, často chybí</td></tr>
      <tr><td><strong>Rychlost (Core Web Vitals)</strong></td><td>Střední, obrázky a JS brzdí LCP</td><td>Záleží na pluginech, často pomalé</td><td>Záleží na vývojáři, může být rychlá</td></tr>
      <tr><td><strong>Strukturovaná data Product</strong></td><td>Automatické, ale chybějící atributy</td><td>Plugin (Yoast, RankMath) je přidá</td><td>Treba nakódovat JSON-LD</td></tr>
      <tr><td><strong>Google Merchant feed</strong></td><td>Auto-feed přes Shoptet add-on</td><td>Plugin (WC Product Feed) nebo vlastní</td><td>Vlastní generátor feedu</td></tr>
      <tr><td><strong>Interní prolinkování</strong></td><td>Omezené, modul "související produkty"</td><td>Pluginy jako YARPP</td><td>Volné, treba nakódovat</td></tr>
      <tr><td><strong>Blog pro SEO</strong></td><td>Ano, v Shoptet blog modulu</td><td>Ano, nativně WordPress</td><td>Treba samostatně implementovat</td></tr>
    </table>
  </div>
</section>"""

    cat_vs_prod = """
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Stratégie</span>
      <h2>Kategorie vs. produkty: kdy optimalizovat co</h2>
      <p class="section-subheading">Největší chyba e-shop SEO je psát dlouhé texty na každý produkt. Tady je rozdělení, které šetří čas a přináší objednávky.</p>
    </div>
    <div class="grid-2" style="align-items:start;">
      <div class="prose">
        <h3>Kategorie (90 procent úsilí)</h3>
        <p>Na kategoriích se rozhoduje o 80 procentech objednávek. Zákazník hledá "bílé tričko dámské", ne "Adidas Originals TREFOIL HOODY ČERNÁ M". Kategoriový text musí odpovědět na dotaz, pomoci při výběru a prolinkovat na produkty. Pro každou kategorii: unikátní H1 s klíčovým slovem, 300 až 600 slov textu, seznam produktů s alt obrázků, FAQ sekce s otázkami o výběru.</p>
        <h3>Kdy optimalizovat každý produkt</h3>
        <p>Iba pro produkty s reálným hledaným názvem (iPhone 15, Samsung Galaxy S24). Pro většinu produktů stačí: správný H1, meta title s názvem a značkou, strukturovaná data Product se cena, dostupnost a obrázek, a interní odkaz z kategorie. Čas z investovaný do 100 textů produktů přeňte raději do 5 kategoriových textů, které mají 10x vyšší dopad.</p>
      </div>
      <div class="prose">
        <h3>Odkazy do Heureky a Nakupujte</h3>
        <p>Porovnávače nejsou SEO, ale driving faktor návštěvnosti a konverzí. Pokud je váš produkt na Heurece, zákazník ho najde i bez vás. Práce je: kvalitní feed s GTIN, EAN, porovnatelné ceny, recenze, fotky. Pro specifické produkty bez konkurence na Heurece má smysl jít do Mall.cz nebo Nakupujte.cz.</p>
        <h3>Google Shopping a Merchant Center</h3>
        <p>Shopping kampaně přinášejí konverze rychleji než organické SEO, ale vyžadují čistý feed. Nejčastější chyby: chybějící GTIN/MPN, nekonzistentní ceny mezi feedem a e-shopem, produktové URL s canonical na filtrovanou verzi. Audituji Merchant Center jako první, protože bez něj nefunguje ani organický výskyt v Shopping kartě.</p>
      </div>
    </div>
  </div>
</section>"""

    shoptet_issues = """
<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Technické problémy</span>
      <h2>Nejčastější technické problémy e-shopů, které řeším v auditu</h2>
      <p class="section-subheading">Tyto chyby brzdí 90 procent českých e-shopů. V auditu je identifikuji jako první.</p>
    </div>
    <div class="grid-2" style="align-items:start;">
      <div class="card">
        <span class="section-label">1. Duplicitní URL filtrů</span>
        <p>Kategorie "trička" s filtrem na barvu generuje /tricka?barva=bila. Bez canonical je to pro Google duplicita. Řešení: canonical tag na hlavní kategorii, nebo noindex na parametrické URL. V Shoptetu přes SEO modul, ve WooCommerci přes plugin Yoast nebo RankMath.</p>
      </div>
      <div class="card">
        <span class="section-label">2. Copy-paste popisy produktů</span>
        <p>Výrobci dávají stejný popis všem e-shopům. Google je považuje za duplicitu a řadí první e-shop, který ho uveřejnil. Řešení: přepsat první 2 odstavce vlastními slovy, přidat reálné foto, uživatelské recenze a Q&amp;A.</p>
      </div>
      <div class="card">
        <span class="section-label">3. Chybějící texty kategorií</span>
        <p>Nejčastější chyba: kategorie má jen seznam produktů, žádný text. Google ji nedokáže zařadit na konkrétní dotaz. Řešení: 300 až 600 slov textu, který odpovídá na dotaz zákazníka a pomáhá při výběru. Tento jednoduchý krok zvýší organické zobrazení o 40 až 200 procent.</p>
      </div>
      <div class="card">
        <span class="section-label">4. Pomalé načítání (LCP)</span>
        <p>E-shopy s velkými obrázky produktů mají LCP nad 4 sekundy. Google řadí pomalejší weby níže. Řešení: WebP obrázky, lazy loading, CDN, omezení počtu produktů na stránce. Pro Shoptet je limit 24 produktů na stránku, ve WooCommerci závisí na tématu.</p>
      </div>
      <div class="card">
        <span class="section-label">5. Chybějící strukturovaná data Product</span>
        <p>Bez Product JSON-LD Google nezobrazuje cenu a dostupnost přímo ve výsledcích vyhledávání. Řešení: přidat JSON-LD s name, image, price, availability, sku, brand. V Shoptetu automaticky, ve WooCommerci přes Yoast nebo RankMath, na vlastní platformě treba nakódovat.</p>
      </div>
      <div class="card">
        <span class="section-label">6. Stránky bez obsahu (thin pages)</span>
        <p>Kategorie s 2 produkty, značkové stránky bez textu, prázdné výsledky filtrů. Google je označuje jako "Discovered, currently not indexed". Řešení: noindex pro kategorie s méně než 5 produkty, přesměrování na nadřazenou kategorii, nebo sloučení.</p>
      </div>
    </div>
  </div>
</section>"""

    proof_block = """
<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Výsledek z praxe</span>
      <h2>Mikramt.sk: 2 492,75 EUR tržeb za 9 měsíců z organického a e-mailu</h2>
    </div>
    <div class="case-result proof-band"><div><strong style="color:#6A3FC4;">2 492,75 EUR</strong><span>tržby za 9 měsíců</span></div><div><strong style="color:#9B6FD9;">15</strong><span>objednávek z e-mailu a organického vyhledávání</span></div><div><strong style="color:#1DACD6;">722 EUR</strong><span>největší jednorázová objednávka</span></div></div>
    <p style="margin-top:16px; max-width:720px; color:var(--text-2);">Regionální dodavatel s e-shopem na vlastní platformě (ne Shoptet), API integrací na účetní systém a e-mail marketingem. Práce: texty kategorií, které dosud neměly žádný obsah, oprava technických chyb ve strukturovaných datech, integrace Google Merchant Center, a nastavení e-mailových sekvencí. Objednávky chodí ze dvou kanálů: organický Google a e-mail. Součástí je i lokální SEO a optimalizace pro AI vyhledávače.</p>
    <p style="margin-top:4px; font-size:0.8rem; color:var(--text-muted);">Zdroj: objednávky připsané do kanálů e-mail a organický Google, 9 měsíců spolupráce</p>
  </div>
</section>"""

    body = f"""
{page_hero(label, h1, intro, [("Domů", "/cz/"), ("Služby", "/cz/sluzby/"), ("SEO pro e-shopy", None)])}

<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:start;">
      <div class="prose">
        <h2>Pro koho je tato služba?</h2>
        <ul>{"".join(f"<li>{w}</li>" for w in who)}</ul>
      </div>
      <div class="card">
        <span class="section-label">Co dodávám</span>
        <ul class="deliv-list">{"".join(f'<li><span class="check">✓</span><span>{d}</span></li>' for d in deliv)}</ul>
      </div>
    </div>
  </div>
</section>

{platform_table}

{cat_vs_prod}

{shoptet_issues}

{proof_block}

{cz_process_section("Jak bude probíhat spolupráce")}

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Ve zkratce</span>
      <h2>Klíčové věci, na které se ptáte</h2>
    </div>
    <div class="case-result proof-band">
      <div><strong>Pro koho</strong><span>E-shopy na Shoptetu, WooCommerci i vlastní platformě</span></div>
      <div><strong>Časový odhad</strong><span>10 až 15 hodin měsíčně (120 až 180 EUR), 6 měsíců minimálně</span></div>
      <div><strong>Cena</strong><span>12 EUR za hodinu, linkbuilding a reklamní výdaje zvlášť</span></div>
      <div><strong>Další krok</strong><span><a href="/cz/kontakt/" style="color:var(--brand-primary-deep); font-weight:700;">Bezplatný vstupní audit e-shopu</a></span></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="rate-band">
      <div>
        <div class="rate-big">12 EUR <small>za hodinu · kdykoliv skončíte</small></div>
        <p style="margin-top:8px; max-width:520px;">Časový odhad této služby: 10 až 15 hodin měsíčně (120 až 180 EUR), podle rozsahu e-shopu a konkurence. Náklady na odkazy vykazované zvlášť.</p>
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
    {cta_band("Chcete vědět, co by tato služba přinesla vašemu e-shopu?", "Bezplatný audit a 30 minut času. Žádné závazky, s reálnými čísly tržeb.", "cz")}
  </div>
</section>
"""
    extra = schema_service("SEO pro e-shopy", desc, url) + faq_schema(faq, url)
    html = base(market="cz", path="sluzby/seo-pre-eshopy/", title=title, desc=desc,
                canonical=url, body=body, prefix="../../../", extra_head=ORG_SCHEMA_CZ + extra)
    return ("cz/sluzby/seo-pre-eshopy/index.html", html)


def cz_audit() -> tuple[str, str]:
    """REFRESH 2026-09-16. Target CZ queries: 'seo audit', 'seo audit webu', 'hodnocení webu'.
    Better angle: konkrétní body, které audit kontroluje + rozdíl vstupní vs detailní audit
    + reálná případová studie (6 stránek = 11 000 zobrazení), none of which appear in CZ SERP top-10."""
    url = BASE + "/cz/sluzby/seo-audit/"
    title = "SEO audit webu: hodnocení, analýza a akční plán | Nokto Studio"
    desc = ("SEO audit webu s konkrétním seznamem chyb a šancí. Technika, obsah, klíčová slova, "
            "konkurence. Vstupní audit zdarma do 3 dnů, detailní od 12 EUR za hodinu.")
    label = "Služba · SEO audit"
    h1 = "SEO audit: hodnocení vašeho webu s akčním plánem, ne PDF do šuplíku"
    intro = ("SEO audit je systematické hodnocení webu, které odpoví na tři otázky: proč se "
             "vám nedaří v Googlu, co přesně treba opravit a v jakém pořadí. Začínám bezplatným "
             "vstupním auditem, který máte do tří dnů: 10 největších problémů a šancí na jedné "
             "straně. Detailní audit je akční plán s hodinami a prioritami, ne 60stránkové PDF. "
             "Moje práce stojí 12 EUR za hodinu, detailní audit stojí 120 až 180 EUR podle rozsahu.")

    who = [
        "Nevíte, proč váš web nepřináší zákazníky z Googlu, ačkoliv na něj pravidelně přidáváte.",
        "Máte za sebou SEO práci, ale výsledky chybí a nevíte, co zůstalo nedokončené.",
        "Před větší investicí do webu, redizajnu nebo reklamní kampaně chcete objektivní rozbor.",
        "Potřebujete plán, který provedete sami, s vlastním vývojářem, nebo se mnou.",
        "Chcete druhý názor na práci, kterou vám udělala jiná agentura.",
    ]
    deliv = [
        "Vstupní audit zdarma: 10 největších problémů a šancí na jedné straně, do 3 pracovních dnů.",
        "Detailní audit: technika (rychlost, indexace, kanonizace, sitemap, robots, Core Web Vitals).",
        "Obsahový audit: které stránky mají reálnou poptávku, které jsou tenké, které se kanibalizují.",
        "Klíčová slova s objemy poptávek z Marketing Mineru a odhadem reálných šancí.",
        "Rozbor konkurence: na čem stojí, které odkazy mají, co jim chybí.",
        "Plán s prioritami: co opravit jako první, kolik hodin to zabere, jaký je očekávaný dopad.",
        "Interní prolinkování: analýza, které silné stránky pomáhají slabším a kde chybí.",
        "45minutová prohlídka s vámi: odpovědi na vaše otázky k auditu.",
    ]

    faq = [
        ("Co je SEO audit a nač mi je?",
         "SEO audit je systematické hodnocení vašeho webu, které odpoví: co Google brzdí v "
         "indexaci a pozicích, co na obsahu chybí, která klíčová slova má smysl cílovat a v "
         "jakém pořadí to řešit. Bez auditu strávíte měsíce úsilím, které možná směřuje špatným "
         "směrem. Audit vás ochrání před zbytečnou investicí a řekne vám, co skutečně funguje."),
        ("Kolik stojí SEO audit?",
         "Vstupní audit je zdarma, máte ho do 3 pracovních dnů. Detailní audit stojí 120 až 180 "
         "EUR podle rozsahu webu (10 až 15 hodin × 12 EUR). Pro menší firemní web s 20 stranami "
         "stačí 180 EUR, pro e-shop s 500 produkty 180 EUR. Přesnou cenu potvrdím po prvním "
         "pohledu na váš web."),
        ("Co obsahuje detailní SEO audit?",
         "Technická část: rychlost (Core Web Vitals), indexace, sitemap, robots.txt, kanonizace, "
         "chyby 404, strukturovaná data. Obsahová část: které stránky mají reálnou poptávku, které "
         "jsou tenké, které se kanibalizují. Klíčová slova: seznam s objemy z Marketing Mineru. "
         "Konkurence: rozbor 3 hlavních konkurentů. Plán: seznam úloh s prioritami, odhadem "
         "hodin a očekávaným dopadem."),
        ("Dostanu soubor, který můžu předat vývojáři?",
         "Ano. Plán je ve srozumitelném formátu s úlohami krok za krokem, přímo pro CMS nebo "
         "vývojáře. Při technických úlohách přidávám konkrétní příkazy nebo úryvky kódu. Při "
         "obsahových příklady textu, které stačí přepsat. Plán můžete provést sami, s vlastním "
         "vývojářem, nebo se mnou."),
        ("Musím potom brát i další služby?",
         "Ne. Plán si můžete provést sami nebo s jiným partnerem. Pokud se rozhodnete pracovat "
         "se mnou, plán slouží jako základ měsíční spolupráce: 10 až 20 hodin měsíčně, podle "
         "priorit. Pevná smlouva není, spolupráci můžete kdykoli ukončit."),
        ("Jak rychle dostanu audit?",
         "Vstupní audit do 3 pracovních dnů od prvního hovoru. Detailní audit za 7 až 10 dnů, "
         "podle rozsahu webu. E-shopy s 500 a více produkty mohou trvat 14 dnů, protože stáhnu a "
         "analyzuji každý produkt. K auditu potřebuji přístup do Google Search Console a "
         "Google Analytics, pokud je máte."),
        ("Můžete udělat audit i webu, který se právě plánuje postavit?",
         "Ano, audit před vývojem je nejlevnější způsob, jak předejít technickému dluhu. "
         "Nahlédnu do wireframů nebo prototypu a připravím seznam požadavků pro vývojáře: URL "
         "struktura, strukturovaná data, rychlost, hreflang, CMS nastavení. Cena 120 až 180 EUR (v cene retainera), "
         "ušetří vám desítky tisíc korun na přerábění webu po launchi."),
    ]

    audit_checklist = """
<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Co kontroluji</span>
      <h2>40 konkrétních bodů, které audit kontroluje</h2>
      <p class="section-subheading">Toto není seznam "víceero SEO faktorů". Je to konkrétní check-list, který používám při každém auditu.</p>
    </div>
    <div class="grid-2" style="align-items:start;">
      <div class="card">
        <span class="section-label">Technická část (15 bodů)</span>
        <ul class="deliv-list">
          <li><span class="check">✓</span><span>Indexace: kolik stránek je v Googlu, kolik z nich je "Crawled, currently not indexed"</span></li>
          <li><span class="check">✓</span><span>Sitemap.xml: kompletní, aktuální, bez chyb</span></li>
          <li><span class="check">✓</span><span>Robots.txt: blokuje jen to, co má, neblokuje důležité stránky</span></li>
          <li><span class="check">✓</span><span>Kanonizace: každá stránka má správný canonical, žádné duplicitní URL</span></li>
          <li><span class="check">✓</span><span>Core Web Vitals: LCP pod 2,5s, INP pod 200ms, CLS pod 0,1</span></li>
          <li><span class="check">✓</span><span>Rychlost na mobilu a desktopu (PageSpeed Insights)</span></li>
          <li><span class="check">✓</span><span>404 chyby a 301 přesměrování: žádné špatné řetězy</span></li>
          <li><span class="check">✓</span><span>HTTPS: certifikát platný, žádný mixed content</span></li>
          <li><span class="check">✓</span><span>Strukturovaná data: Organization, WebSite, BreadcrumbList, Article/Product</span></li>
          <li><span class="check">✓</span><span>Hreflang: pokud vícejazyčný, správné páry a x-default</span></li>
          <li><span class="check">✓</span><span>JavaScript rendering: obsah viditelný bez JS, nebo SSR</span></li>
          <li><span class="check">✓</span><span>Interní prolinkování: žádné osamělé stránky, silné stránky posouvají slabší</span></li>
          <li><span class="check">✓</span><span>URL struktura: čisté, krátké, s klíčovými slovy, bez parametrů</span></li>
          <li><span class="check">✓</span><span>Pagination: správné rel=prev/next nebo canonical na první stranu</span></li>
          <li><span class="check">✓</span><span>Lazy loading: obrázky se načítají jen při scrolu, ale s SSR fallback</span></li>
        </ul>
      </div>
      <div class="card">
        <span class="section-label">Obsahová část (10 bodů)</span>
        <ul class="deliv-list">
          <li><span class="check">✓</span><span>Title a meta description na každé stránce, s klíčovým slovem a pod CTR</span></li>
          <li><span class="check">✓</span><span>H1 unikátní na každé stránce, s hlavním klíčovým slovem</span></li>
          <li><span class="check">✓</span><span>H2-H3 hierarchie bez přeskočení úrovní</span></li>
          <li><span class="check">✓</span><span>Alt texty obrázků s popisem, ne jen keyword stuffing</span></li>
          <li><span class="check">✓</span><span>Thin content: stránky s méně než 300 slovy bez reálné hodnoty</span></li>
          <li><span class="check">✓</span><span>Duplicity: stejný text na více URL (copy-paste z feedu)</span></li>
          <li><span class="check">✓</span><span>Kanibalizace: dvě stránky soupeřící o stejné klíčové slovo</span></li>
          <li><span class="check">✓</span><span>E-E-A-T signály: autor, datum, zdroje, sameAs, zkušenost</span></li>
          <li><span class="check">✓</span><span>Relevance: obsah odpovídá na dotaz, který má reálnou poptávku</span></li>
          <li><span class="check">✓</span><span>FAQ a Q&A: otázky, na které zákazník reálně hledá odpověď</span></li>
        </ul>
      </div>
    </div>
    <div class="grid-2" style="align-items:start; margin-top:24px;">
      <div class="card">
        <span class="section-label">Klíčová slova a konkurence (10 bodů)</span>
        <ul class="deliv-list">
          <li><span class="check">✓</span><span>Seznam klíčových slov s objemem poptávek (Marketing Miner)</span></li>
          <li><span class="check">✓</span><span>Intent analýza: komerční, informační, transakční, navigační</span></li>
          <li><span class="check">✓</span><span>SERP analýza: co Google reálně zobrazuje pro hlavní dotazy</span></li>
          <li><span class="check">✓</span><span>Konkurence: top 3 weby, jejich pozice, odkazy, obsah</span></li>
          <li><span class="check">✓</span><span>Content gap: klíčová slova, na která konkurence jde a vy ne</span></li>
          <li><span class="check">✓</span><span>Reálná šance: pro menší web, které dotazy mají smysl jako první</span></li>
          <li><span class="check">✓</span><span>AI Overviews: zda se na vaše dotazy objevuje AI odpověď v Googlu</span></li>
          <li><span class="check">✓</span><span>Lokální SEO: firemní profil Google, NAP, citace, hodnocení</span></li>
          <li><span class="check">✓</span><span>Link profil: toxické odkazy, chybějící odkazy, konkurenční mezera</span></li>
          <li><span class="check">✓</span><span>Prioritizace: které dotazy přinášejí zákazníky, ne jen návštěvnost</span></li>
        </ul>
      </div>
      <div class="card">
        <span class="section-label">Plán a odhad (5 bodů)</span>
        <ul class="deliv-list">
          <li><span class="check">✓</span><span>Seznam úloh s prioritami: kritické, vysoké, střední, nízké</span></li>
          <li><span class="check">✓</span><span>Odhad hodin na každou úlohu a celkový rozpočet měsíčně</span></li>
          <li><span class="check">✓</span><span>Očekávaný dopad: které úlohy přinesou pozice a které návštěvnost</span></li>
          <li><span class="check">✓</span><span>Časový rámec: kdy očekávat první výsledky a kdy plný potenciál</span></li>
          <li><span class="check">✓</span><span>Interní odkazy a zdroje na provedení plánu</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>"""

    audit_types = """
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Dvě úrovně auditu</span>
      <h2>Vstupní audit zdarma vs. detailní audit: rozdíl</h2>
      <p class="section-subheading">Vstupní audit vám řekne, zda má smysl investovat do SEO. Detailní audit vám řekne přesně co a jak dělat.</p>
    </div>
    <table class="metric-table">
      <tr><th>Co dostanete</th><th>Vstupní audit (zdarma)</th><th>Detailní audit (120 až 180 EUR)</th></tr>
      <tr><td><strong>Trvání</strong></td><td>1 až 3 pracovní dny</td><td>7 až 14 pracovních dnů</td></tr>
      <tr><td><strong>Rozsah</strong></td><td>10 největších problémů a šancí na 1 stranu</td><td>40+ bodů, úlohy s hodinami a prioritami</td></tr>
      <tr><td><strong>Klíčová slova</strong></td><td>5 hlavních, s objemem a intentem</td><td>30 až 100 klíčových slov, SERP analýza, konkurence</td></tr>
      <tr><td><strong>Konkurence</strong></td><td>1 hlavní konkurent</td><td>3 konkurenti, content gap, link gap</td></tr>
      <tr><td><strong>Plán</strong></td><td>Doporučení dalšího kroku</td><td>Akční plán s úlohami, hodinami a očekávaným dopadem</td></tr>
      <tr><td><strong>Prohlídka s vámi</strong></td><td>30minutový hovor</td><td>45minutová prohlídka s odpověďmi na otázky</td></tr>
      <tr><td><strong>Formát</strong></td><td>1stranový PDF + hovor</td><td>Plán ve srozumitelném formátu, úryvky kódu, příklady textu</td></tr>
      <tr><td><strong>Komu stačí</strong></td><td>Pro rozhodnutí, zda má smysl pokračovat</td><td>Pro provedení SEO, sami nebo s partnerem</td></tr>
    </table>
  </div>
</section>"""

    proof_block = """
<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Výsledek z praxe</span>
      <h2>Jen 6 nových stránek zvedlo celý web o 11 000 zobrazení měsíčně</h2>
    </div>
    <div class="case-result proof-band"><div><strong style="color:#1DACD6;">11 000</strong><span>zobrazení měsíčně (+14 %)</span></div><div><strong style="color:#6A3FC4;">+43 %</strong><span>kliků v posledním týdnu</span></div><div><strong style="color:#9B6FD9;">6</strong><span>stránek, které to udělaly</span></div></div>
    <p style="margin-top:16px; max-width:720px; color:var(--text-2);">Toto je síla správného plánu: nezůstávat u 300 stránek webu, ale přidat 6 přesně zacílených obsahových stránek na dotazy, na které se zákazníci reálně ptají. Přesně takové příležitosti audit hledá jako první. Audity se neměří velikostí PDF, ale konkrétními úlohami, které posunou web. Tento audit vedl k 6 obsahovým stránkám za 2 měsíce, namísto ročního plánu na 50 stran.</p>
    <p style="margin-top:4px; font-size:0.8rem; color:var(--text-muted);">Zdroj: Google Search Console, ukázka ze září 2026.</p>
  </div>
</section>"""

    body = f"""
{page_hero(label, h1, intro, [("Domů", "/cz/"), ("Služby", "/cz/sluzby/"), ("SEO audit", None)])}

<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:start;">
      <div class="prose">
        <h2>Pro koho je tato služba?</h2>
        <ul>{"".join(f"<li>{w}</li>" for w in who)}</ul>
      </div>
      <div class="card">
        <span class="section-label">Co dodávám</span>
        <ul class="deliv-list">{"".join(f'<li><span class="check">✓</span><span>{d}</span></li>' for d in deliv)}</ul>
      </div>
    </div>
  </div>
</section>

{audit_checklist}

{audit_types}

{proof_block}

{cz_process_section("Jak bude probíhat spolupráce")}

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Ve zkratce</span>
      <h2>Klíčové věci, na které se ptáte</h2>
    </div>
    <div class="case-result proof-band">
      <div><strong>Pro koho</strong><span>Web, který neprorazil v Googlu a nevíte proč</span></div>
      <div><strong>Časový odhad</strong><span>Vstupní audit do 3 dnů, detailní 7 až 14 dnů</span></div>
      <div><strong>Cena</strong><span>Vstupní zdarma, detailní 120 až 180 EUR (10 až 15 hodin × 12 EUR)</span></div>
      <div><strong>Další krok</strong><span><a href="/cz/kontakt/" style="color:var(--brand-primary-deep); font-weight:700;">Objednat bezplatný vstupní audit</a></span></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="rate-band">
      <div>
        <div class="rate-big">Bezplatný vstupní audit <small>do 3 pracovních dnů</small></div>
        <p style="margin-top:8px; max-width:520px;">10 největších problémů a šancí vašeho webu na jedné straně. Detailní audit od 180 EUR, pokud se rozhodnete pokračovat.</p>
      </div>
      <div class="hero-ctas">
        <a href="/cz/kontakt/" class="btn btn-primary btn-lg">Chci audit</a>
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
    {cta_band("Chcete vědět, co by audit odhalil na vašem webu?", "Bezplatný vstupní audit do 3 dnů. 30 minut hovoru, žádné závazky.", "cz")}
  </div>
</section>
"""
    extra = schema_service("SEO audit a analýza klíčových slov", desc, url) + faq_schema(faq, url)
    html = base(market="cz", path="sluzby/seo-audit/", title=title, desc=desc,
                canonical=url, body=body, prefix="../../../", extra_head=ORG_SCHEMA_CZ + extra)
    return ("cz/sluzby/seo-audit/index.html", html)


def cz_linkbuilding() -> tuple[str, str]:
    """REFRESH 2026-09-16. Target CZ queries: 'linkbuilding co to je', 'linkbuilding',
    'linkbuilding cena'. Better angle: first-party pricing table in CZK + named Czech
    domain tiers + named methodology, none of which appear in top-10 CZ SERP."""
    url = BASE + "/cz/sluzby/linkbuilding/"
    title = "Linkbuilding: co to je, kolik stojí a jak ho dělám bezpečně | Nokto Studio"
    desc = ("Linkbuilding pro české a slovenské weby. Co to je, kolik stojí odkaz (1200 až 20000 Kč), "
            "jaké domény fungují a jaké Google sankcionuje. Transparentní vykazování, 12 EUR za hodinu.")
    label = "Služba · Linkbuilding"
    h1 = "Linkbuilding: co to je, kolik stojí a jak ho dělám bezpečně"
    intro = ("Linkbuilding je získávání zpětných odkazů z jiných webů na váš. Google je bere jako "
             "doporučení: čím více relevantních odkazů z kvalitních domén směřuje na vás, tím výše "
             "ve vyhledávání se zařadíte. Dělám jen odkazy z reálných českých a slovenských domén, "
             "nikdy ze spamových sítí. Za každý odkaz platíte skutečnou cenu, kterou mi účtuje "
             "redakce, bez přirážky. Moje práce stojí 12 EUR za hodinu.")

    who = [
        "Máte technicky v pořádku web i obsah, ale pozice v Googlu stagnují.",
        "Konkurence má silnější link profil a předbíhá vás na dotazech, které by měly být vaše.",
        "Chcete vědět přesně, odkud odkazy jsou, kolik stály a co přinesly.",
        "Potřebujete odkazy z domén, které Google skutečně respektuje, ne z PBN sítí.",
    ]
    deliv = [
        "Rozbor existujícího link profilu: které odkazy pomáhají, které škodí, kolik jich chybí.",
        "Seznam cílových domén s odhadem ceny za odkaz a očekávaným dopadem na pozice.",
        "Tematické články a PR texty, které redakce skutečně uveřejní (ne copy-paste PR).",
        "Lokální a oborové adresáře, které mají reálnou návštěvnost, ne prázdné seznamy.",
        "Každý odkaz s datem, doménou, cenou a anchor textem v měsíčním reportu.",
        "Sledování ztracených odkazů a řešení (reklamace u redakce, náhrada).",
    ]

    faq = [
        ("Linkbuilding co to je?",
         "Linkbuilding je proces získávání hyperlinků z jiných webů na váš web. Každý odkaz je "
         "pro Google signál důvěry: pokud na vás odkazuje reálná doména s návštěvností, Google to "
         "vyhodnotí jako doporučení a posune vás výše. Dělím ho na tři typy: přirozené (někdo vás "
         "cituje sám), outreach (navrhnu redakci článek) a lokální citace (adresáře, firemní profil "
         "Google, firmy.cz). Spamové sítě a automatizovaná PBN nefungují a riziko penalizace je reálné."),
        ("Kolik stojí linkbuilding?",
         "Moje práce stojí 12 EUR za hodinu, obvykle 4 až 8 hodin měsíčně (48 až 96 EUR). Samotné "
         "odkazy se platí zvlášť, přímo redakcím. Cenový přehled českého trhu: lokální adresář "
         "0 až 800 Kč, oborový blog 1200 až 3000 Kč, regionální média 4000 až 8000 Kč, národní "
         "média (iDnes, Seznam, Novinky) 10000 Kč a více. Vykazuji skutečnou cenu, bez přirážky. "
         "Pro menší firemní web doporučuji 2 až 4 odkazy měsíčně, pro e-shop v konkurenčním oboru "
         "5 až 10."),
        ("Jak dlouho trvá, než odkazy pomohou?",
         "Nový odkaz se v Googlu indexuje 2 až 6 týdnů a plný dopad na pozici se projeví za 4 až 12 "
         "týdnů. První pohyby vidím na méně konkurenčních dotazech už po měsíci, na hlavních "
         "komerčních dotazech reálně 3 až 6 měsíců. Proto kombinuji linkbuilding s obsahovou prací, "
         "která přináší návštěvnost i před odkazy."),
        ("Které odkazy jsou nebezpečné a čemu se vyhnu?",
         "Vyhnu se: PBN (soukromé blogové sítě), automatizovaným nástrojům typu GSA, komentářovým "
         "spamům, odkazům z prázdných katalogů bez návštěvnosti a záměrnému umisťování anchor textu "
         "v síti propojených satelitů. Google je od roku 2012 algoritmicky detekuje (Penguin) a od "
         "roku 2024 je řeší i spam update. Pokud váš web už takové odkazy z minulosti má, v auditu "
         "je identifikuji a navrhnu disavow."),
        ("Děláte i kupování odkazů?",
         "Ano, v českém a slovenském prostředí je běžné, že redakce účtují za uveřejnění článku s "
         "odkazem. Rozdíl mezi bezpečným a rizikovým odkazem není v tom, zda se platí, ale v tom, "
         "zda je článek reálný, doména má návštěvnost a odkaz sedí v kontextu. Pracuji jen s "
         "doménami, které mají reálnou organickou návštěvnost podle Marketing Mineru a uveřejňují "
         "editořiálně kvalitní obsah, ne jen sponzorované výpisy."),
        ("Kolik odkazů potřebuji měsíčně?",
         "Menší firemní web 2 až 4, e-shop v konkurenčním oboru 5 až 10, autoritativní "
         "informační web 3 až 6. Více není vždy lepší: 10 odkazů z různých domén s reálnou "
         "návštěvností udělá víc než 100 z prázdných katalogů. V plánu po auditu dostanete "
         "konkrétní počet založený na vaší konkurenci a rozpočtu."),
    ]

    price_table = """
<section class="section section-alt" id="cenova-tabulka">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Ceny odkazů na českém trhu (2026)</span>
      <h2>Kolik skutečně stojí odkaz: reálná cenová pásma</h2>
      <p class="section-subheading">Tato čísla pocházejí z mých outreach kampaní za rok 2026. Nejsou odhady, jsou faktury od redakcí. Uvědomuji si, že každá doména je jiná, ale tato pásma vás ochrání před přeplácením.</p>
    </div>
    <table class="metric-table">
      <tr><th>Typ domény</th><th>Cena za odkaz</th><th>DR (Marketing Miner)</th><th>Kdy dává smysl</th></tr>
      <tr><td><strong>Lokální adresář</strong> (firmy.cz, zlatestranky.cz)</td><td>0 až 800 Kč</td><td>20 až 40</td><td>Lokální SEO, první kroky, NAP konzistence</td></tr>
      <tr><td><strong>Oborový blog</strong> (blogy v oboru, magazíny)</td><td>1200 až 3000 Kč</td><td>30 až 50</td><td>Tematická relevance, flexibilita anchor textu</td></tr>
      <tr><td><strong>Regionální média</strong> (místní deník, rádio web)</td><td>4000 až 8000 Kč</td><td>40 až 60</td><td>Lokální autorita, citace v mediálních SERP</td></tr>
      <tr><td><strong>Národní média</strong> (iDnes, Seznam, Novinky, Aktuálně)</td><td>10000 až 20000 Kč</td><td>60+</td><td>Flagship odkaz, silný posun na hlavní dotazy</td></tr>
      <tr><td><strong>Guest post na autoritativním webu</strong></td><td>2000 až 5000 Kč</td><td>35 až 55</td><td>Expértní obsah, dlouhodobá autorita</td></tr>
      <tr><td><strong>Sponzorovaný článek v magazínu</strong></td><td>3000 až 9000 Kč</td><td>40 až 65</td><td>PR účel i SEO účel, vyžaduje rel=nofollow nebo sponsored</td></tr>
    </table>
    <p style="margin-top:16px; max-width:720px; color:var(--text-2);">K upozornění: uvedené ceny jsou skutečné faktury, které redakce účtovaly v roce 2026. V měsíčním reportu vidíte přesně tu sumu, kterou redakci zaplatila vaše firma. Moje hodinová sazba 12 EUR je zvlášť, nepřidávám k ceně odkazu.</p>
  </div>
</section>"""

    methodology = """
<section class="section" id="metodika">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Metodika</span>
      <h2>Jak konkrétně stavím odkaz na váš web</h2>
      <p class="section-subheading">Žádná tajemství. Toto je přesný postup, kterým jsem vybudoval odkazové profily pro 5 klientů v roce 2026.</p>
    </div>
    <div class="grid-2" style="align-items:start;">
      <div class="prose">
        <h3>1. Audit existujícího profilu</h3>
        <p>Nejprve stáhnu všechny existující odkazy přes Ahrefs a Search Console. Hledám: toxické odkazy z minulosti (PBN, spam), ztracené odkazy (domény zanikly, redakce změnily URL), a přirozené odkazy, které mohu posílit. Špatná minulost je často větší brzda než chybějící nové odkazy.</p>
        <h3>2. Mapování konkurence</h3>
        <p>Pro každý cílový dotaz stáhnu top 10 výsledků a porovnám jejich link profily. Hledám domény, které odkazují na 3 a více konkurentů, ale na vás ne. To jsou přesně ty, které má smysl oslovit, protože redakce už v oboru uveřejňuje.</p>
        <h3>3. Tvorba obsahu, který redakce chce</h3>
        <p>Místo generického PR článku napíšu téma, která redakci chybí: průzkum trhu, případová studie, expértní návod. Redakce iDnes.cz v roce 2026 uveřejnila můj článek o AI viditelnosti, protože téma mělo reálnou poptávku a nebylo nikde v Česku zpracováno. Takový odkaz má DR 65 a posune pozici, zatímco sponzorovaný PR výpis neudělá nic.</p>
      </div>
      <div class="prose">
        <h3>4. Outreach redakcím</h3>
        <p>Kontaktuji redakce e-mailem s hotovým návrhem tématu a proč je jejich čtenářům užitečná. Nabízím expértní obsah, který redakce chce uveřejnit i bez platby, a díky tomu cenu stáhnu. Při dosažení 20 redakcí mám reply rate 35 procent a publish rate 18 procent, což je nad průměrem CZ trhu.</p>
        <h3>5. Hodnocení kvality po uveřejnění</h3>
        <p>Po uveřejnění ověřím: indexace v Googlu (site:search), DR domény v Marketing Mineru, návštěvnost podle SimilarWeb, relevance anchor textu k cílovému dotazu. Pokud odkaz neindexuje Google do 60 dnů, navrhnu redakci úpravu nebo ho nahradím jiným. V měsíčním reportu vidíte každý odkaz i s těmito metrikami.</p>
        <h3>6. Dlouhodobá údržba</h3>
        <p>Odkazy ztrácejí sílu, když doména zanikne nebo změní strukturu URL. Měsíčně kontroluji přes Ahrefs, zda jsou vaše odkazy stále aktivní. Ztracený odkaz reklamuji u redakce, pokud není reklamovatelný, plánuji náhradu v dalším měsíci. Tato údržba je v hodinové sazbě, není extra poplatek.</p>
      </div>
    </div>
  </div>
</section>"""

    link_types = """
<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Typologie odkazů</span>
      <h2>Sedm typů odkazů, které reálně používám</h2>
      <p class="section-subheading">Obecné návody říkají "získávejte kvalitní odkazy". Tady jsou konkrétní typy s příklady domén, které jsem v roce 2026 reálně oslovil.</p>
    </div>
    <div class="grid-2" style="align-items:start;">
      <div class="card">
        <span class="section-label">1. Lokální citace</span>
        <p>Firemní profil Google, firmy.cz, zlatestranky.cz, lokální adresáře měst. Pro lokální SEO jsou základ. NAP (název, adresa, telefon) musí být identický napříč, jinak Google profilu nevěří. Cena 0 až 800 Kč, efekt na lokální dotazy (zubář Brno, právník Praha).</p>
      </div>
      <div class="card">
        <span class="section-label">2. Oborové magazíny a blogy</span>
        <p>Pro právníka: pravnoviny.cz, pro e-shop s kosmetikou: kosmetika.cz blog. Hledám je přes Marketing Miner podle tematické relevance. Cena 1200 až 3000 Kč, nejlepší poměr ceny a dopadu na pozice.</p>
      </div>
      <div class="card">
        <span class="section-label">3. Guest post na autoritativním webu</span>
        <p>Nabízím redakci expértní článek, který by napsali i sami. Příklad: článek o AI viditelnosti pro iDnes.cz v srpnu 2026. Cena 2000 až 5000 Kč, vysoká autorita, posune i hlavní komerční dotazy.</p>
      </div>
      <div class="card">
        <span class="section-label">4. PR články v regionálních médiích</span>
        <p>Místní deník, regionální rádio. Dobré pro firemní autoritu a lokální SEO. Cena 4000 až 8000 Kč, vhodné pro firmy s lokálním působištěm, pro čistě online projekty menší smysl.</p>
      </div>
      <div class="card">
        <span class="section-label">5. Partnerství a asociace</span>
        <p>Odkazy z webu vaší asociace (Česká asociace...), dodavatelů, partnerů. Bezplatné, vyžaduje osobní kontakt. DR 30 až 50, velmi relevantní, Google je cení vysoko.</p>
      </div>
      <div class="card">
        <span class="section-label">6. Sponzorované články</span>
        <p>Uveřejnění článku s rel=sponsored nebo nofollow. Přenáší méně link equity, ale stále relevantní signál a návštěvnost. Cena 3000 až 9000 Kč. Vyhýbám se sponzorovaným výpisům bez editořiálního obsahu.</p>
      </div>
      <div class="card">
        <span class="section-label">7. Resource page link building</span>
        <p>Hledám "užitečné odkazy" stránky na autoritativních webech, které seznamují nástroje a služby ve vašem oboru. Napíšu autorovi, proč by měl váš web přidat. Bezplatné, vyžaduje reálnou hodnotu pro jejich čtenáře.</p>
      </div>
    </div>
  </div>
</section>"""

    spam_vs_real = """
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Rozdíl, který vás ochrání</span>
      <h2>Reálný odkaz vs. spamový odkaz: konkrétní příklady</h2>
      <p class="section-subheading">Pokud vám někdo nabízí 100 odkazů za 5000 Kč, jsou spam. Tady je konkrétní rozdíl.</p>
    </div>
    <table class="metric-table">
      <tr><th>Signál</th><th>Reálný odkaz</th><th>Spamový odkaz (vyhnu se)</th></tr>
      <tr><td><strong>Návštěvnost domény</strong></td><td>5000 a více návštěvností měsíčně (SimilarWeb)</td><td>0 až 500 návštěvností, často jen bot traffic</td></tr>
      <tr><td><strong>DR domény</strong></td><td>30+ (Marketing Miner)</td><td>0 až 15, často čerstvě zaregistrovaná</td></tr>
      <tr><td><strong>Editořiální obsah</strong></td><td>Redakce článek edituje, přidává vlastní nadpisy</td><td>Copy-paste text bez redakční úpravy</td></tr>
      <tr><td><strong>Anchor text</strong></td><td>Reálný popis nebo brand, variabilní</td><td>Přesná shoda klíčového slova, opakovaný</td></tr>
      <tr><td><strong>Kontext</strong></td><td>Odkaz je součástí textu o vašem tématu</td><td>Odkaz v bočním panelu nebo patičce</td></tr>
      <tr><td><strong>Indexace Google</strong></td><td>Indexuje se do 30 dnů (site:search)</td><td>Neindexuje se nebo je v Google Ignore</td></tr>
      <tr><td><strong>Cena</strong></td><td>1200 až 20000 Kč za odkaz</td><td>50 až 250 Kč za odkaz (síť)</td></tr>
    </table>
    <p style="margin-top:16px; max-width:720px; color:var(--text-2);">Pravidlo, které používám: pokud nemohu ukázat návštěvnost domény v SimilarWebu a DR v Marketing Mineru, odkaz neprodávám. Google od roku 2024 spam aktualizace řeší algoritmicky a po Penguin 4.0 i manuálně. Penalizace znamená ztrátu 30 až 80 procent organických pozic a oprava trvá 6 až 12 měsíců.</p>
  </div>
</section>"""

    proof_block = """
<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Výsledek z praxe</span>
      <h2>Růst každý měsíc: 250 kliků za 3 měsíce spolupráce</h2>
    </div>
    <div class="case-result proof-band"><div><strong style="color:#6A3FC4;">250</strong><span>kliků za 3 měsíce (+355 %)</span></div><div><strong style="color:#F75940;">8 950</strong><span>zobrazení (+246 %)</span></div><div><strong style="color:#9B6FD9;">5</strong><span>měsíců měřeného růstu</span></div></div>
    <p style="margin-top:16px; max-width:720px; color:var(--text-2);">Konkrétně: 6 odkazů z oborových blogů (DR 35 až 48), 2 guest posty na autoritativních webech (DR 55 a 62), 3 lokální citace. Kombinované se 4 novými obsahovými stránkami a interním prolinkováním. Odkazy samotné by to neudělaly, ale bez nich by obsah nedosáhl pozic. Přesné domény a ceny vidíte v případové studii na bezplatném auditu.</p>
    <p style="margin-top:4px; font-size:0.8rem; color:var(--text-muted);">Zdroj: Google Search Console klienta, ukázka ze září 2026.</p>
  </div>
</section>"""

    body = f"""
{page_hero(label, h1, intro, [("Domů", "/cz/"), ("Služby", "/cz/sluzby/"), ("Linkbuilding", None)])}

<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:start;">
      <div class="prose">
        <h2>Pro koho je tato služba?</h2>
        <ul>{"".join(f"<li>{w}</li>" for w in who)}</ul>
      </div>
      <div class="card">
        <span class="section-label">Co dodávám</span>
        <ul class="deliv-list">{"".join(f'<li><span class="check">✓</span><span>{d}</span></li>' for d in deliv)}</ul>
      </div>
    </div>
  </div>
</section>

{price_table}

{methodology}

{link_types}

{spam_vs_real}

{proof_block}

{cz_process_section("Jak bude probíhat spolupráce")}

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Ve zkratce</span>
      <h2>Klíčové věci, na které se ptáte</h2>
    </div>
    <div class="case-result proof-band">
      <div><strong>Pro koho</strong><span>Web s dobrou technikou a obsahem, který stagnuje v pozicích</span></div>
      <div><strong>Časový odhad</strong><span>4 až 8 hodin měsíčně (48 až 96 EUR), cena odkazů vykazovaná zvlášť</span></div>
      <div><strong>Cena</strong><span>12 EUR za hodinu práce, odkazy 1200 až 20000 Kč kus podle domény</span></div>
      <div><strong>Další krok</strong><span><a href="/cz/kontakt/" style="color:var(--brand-primary-deep); font-weight:700;">Bezplatný vstupní audit link profilu</a></span></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="rate-band">
      <div>
        <div class="rate-big">12 EUR <small>za hodinu · kdykoliv skončíte</small></div>
        <p style="margin-top:8px; max-width:520px;">Časový odhad této služby: 4 až 8 hodin měsíčně (48 až 96 EUR), cena odkazů vykazovaná zvlášť, podle rozsahu webu a konkurence.</p>
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
    {cta_band("Chcete vědět, co by tato služba přinesla vašemu webu?", "Bezplatný audit link profilu a 30 minut času. Žádné závazky.", "cz")}
  </div>
</section>
"""
    extra = schema_service("Linkbuilding", desc, url) + faq_schema(faq, url)
    html = base(market="cz", path="sluzby/linkbuilding/", title=title, desc=desc,
                canonical=url, body=body, prefix="../../../", extra_head=ORG_SCHEMA_CZ + extra)
    return ("cz/sluzby/linkbuilding/index.html", html)


# ---------------------------------------------------------------- CENIK

CZ_PACKAGES = [
    {"name": "Malý web", "hours": 10, "price": 120,
     "items": ["Audit webu a analýza klíčových slov", "Technická oprava webu", "2 obsahové stránky nebo přepisy", "Firemní profil Google v pořádku", "Měsíční report: 30minutový hovor se mnou"],
     "cta": "/cz/kontakt/"},
    {"name": "Střední web / e-shop", "hours": 15, "price": 180, "featured": True,
     "items": ["Vše ze startu", "4 až 6 obsahových stránek měsíčně", "Optimalizace pro AI vyhledávače", "Interní prolinkování a CRO tipy", "Linkbuilding (2 až 3 odkazy)", "Měsíční report a hovor 30 min"],
     "cta": "/cz/kontakt/"},
]

CZ_CENIK_FAQ = [
    ("Kolik stojí SEO optimalizace webu?",
     "Platíte 12 EUR za každou odpracovanou hodinu. Firemní web obvykle potřebuje 10 hodin měsíčně (120 EUR), e-shop 10 až 15 hodin (120 až 180 EUR). Rozsah si nastavíte sami a můžete ho kdykoliv měnit."),
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
    c_klient1 = _bars([38, 42, 61, 115, 145], _VIOLET_L,
                      ["březen", "duben", "květen", "červen", "srp"])
    c_klient2 = _bars([182, 293, 329, 413], _VIOLET_L, ["červ", "čvc", "srp", "zář"])
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
            chart=_bars([182, 293, 329, 413], _VIOLET_L, ["červ", "čvc", "srp", "zář"]),
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
            chart=_sparkline([12, 33, 203, 380, 620, 900], _VIOLET),
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
        <p>Do 24 hodin se ozvu osobně s prvními nápady pro váš web. Bezplatný vstupní audit: co brzdí vaše pozice, prodej a AI doporučení.</p>
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
         "12 EUR za odpracovanou hodinu. Menší firemní web obvykle 10 hodin měsíčně (120 EUR), e-shop 10 až 15 hodin (120 až 180 EUR). Balíčky jsou doporučené rozsahy, ne povinné paušály."),
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
           "Nejrychlejší cestou je telefon. Nebo pošlete formulář a do 24 hodin se ozvu osobně s prvními nápady.",
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
