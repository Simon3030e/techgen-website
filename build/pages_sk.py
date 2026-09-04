# -*- coding: utf-8 -*-
"""
Nokto Studio - SK page content.
Every function returns (rel_path, html) where rel_path is inside the repo.
"""
from engine import (base, page_hero, cta_band, faq_block, faq_schema,
                    price_cards, steps_block, benefit_cards, schema_service,
                    ORG_SCHEMA, CAL, EMAIL, LOGO, BASE)

SK_ROOT = "/sk/"

# ---------------------------------------------------------------- shared blocks

TRUST_STATS = """
<div class="trust-strip">
  <div class="container">
    <div class="trust-grid">
      <div class="trust-stat reveal" data-delay="100">
        <span class="trust-num">8+</span>
        <span class="trust-label">rokov skúseností<br>v online marketinge</span>
      </div>
      <div class="trust-stat reveal" data-delay="200">
        <span class="trust-num">12&nbsp;EUR</span>
        <span class="trust-label">transparentná hodinová<br>sadzba, bez paušálov</span>
      </div>
      <div class="trust-stat reveal" data-delay="300">
        <span class="trust-num">12h</span>
        <span class="trust-label">maximálna doba odpovede,<br>bez ghostingu</span>
      </div>
      <div class="trust-stat reveal" data-delay="400">
        <span class="trust-num">1. deň</span>
        <span class="trust-label">bezplatný audit<br>začne hneď po prvom hovore</span>
      </div>
    </div>
  </div>
</div>
"""

LOGOS = """
<section class="logo-strip-section">
  <p class="logo-strip-heading">Značky, s ktorými sme pracovali</p>
  <div class="marquee-viewport">
    <div class="marquee-track">
      <span class="logo-badge"><img loading="lazy" class="logo-inv" src="/assets/img/logos/kreisel.png" alt="Kreisel"></span>
      <span class="logo-badge"><img loading="lazy" src="/assets/img/logos/sirupo.webp" alt="Sirupo"></span>
      <span class="logo-badge"><img loading="lazy" src="/assets/img/logos/mikramt.png" alt="Mikramt.sk"></span>
      <span class="logo-badge"><img loading="lazy" class="logo-inv" src="/assets/img/logos/tvlux.png" alt="TV Lux"></span>
      <span class="logo-badge"><img loading="lazy" class="logo-inv" src="/assets/img/logos/speem.webp" alt="Speem"></span>
      <span class="logo-badge"><img loading="lazy" class="logo-inv" src="/assets/img/logos/epw.png" alt="EPW"></span>
      <span class="logo-badge"><img loading="lazy" src="/assets/img/logos/postoj.svg" alt="Postoj"></span>
      <a href="https://flamia.studio" target="_blank" rel="noopener noreferrer" class="logo-badge is-link"><img loading="lazy" src="/assets/img/logos/flamia.png" alt="Flamia Studio"></a>
      <a href="https://dolinajjr.sk" target="_blank" rel="noopener noreferrer" class="logo-badge is-link"><img loading="lazy" src="/assets/img/logos/dolinajjr.png" alt="Dolina JJR"></a>
      <span class="logo-badge"><img loading="lazy" class="logo-inv" src="/assets/img/logos/kreisel.png" alt="Kreisel"></span>
      <span class="logo-badge"><img loading="lazy" src="/assets/img/logos/sirupo.webp" alt="Sirupo"></span>
      <span class="logo-badge"><img loading="lazy" src="/assets/img/logos/mikramt.png" alt="Mikramt.sk"></span>
      <span class="logo-badge"><img loading="lazy" class="logo-inv" src="/assets/img/logos/tvlux.png" alt="TV Lux"></span>
      <span class="logo-badge"><img loading="lazy" class="logo-inv" src="/assets/img/logos/speem.webp" alt="Speem"></span>
      <span class="logo-badge"><img loading="lazy" class="logo-inv" src="/assets/img/logos/epw.png" alt="EPW"></span>
      <span class="logo-badge"><img loading="lazy" src="/assets/img/logos/postoj.svg" alt="Postoj"></span>
      <a href="https://flamia.studio" target="_blank" rel="noopener noreferrer" class="logo-badge is-link"><img loading="lazy" src="/assets/img/logos/flamia.png" alt="Flamia Studio"></a>
      <a href="https://dolinajjr.sk" target="_blank" rel="noopener noreferrer" class="logo-badge is-link"><img loading="lazy" src="/assets/img/logos/dolinajjr.png" alt="Dolina JJR"></a>
    </div>
  </div>
</section>
"""

SERVICES_LIST = [
    ("/sk/sluzby/seo-optimalizacia/", "SEO optimalizácia", "Pozície v Google, ktoré prinášajú zákazníkov, nie len návštevnosť.", "🔍", "tag-blue"),
    ("/sk/sluzby/lodalne-seo/", "Lokálne SEO a Google profil", "Google Mapy, firemný profil, hodnotenia. Zákazníci z okolia vás nájdu prví.", "📍", "tag-red"),
    ("/sk/sluzby/seo-pre-ai-vyhladavace/", "SEO pre AI vyhľadávače", "ChatGPT, Gemini a AI Overviews vás odporúčajú zákazníkom ako prvú voľbu.", "🤖", "tag-green"),
    ("/sk/sluzby/seo-pre-eshopy/", "SEO pre e-shopy", "Viac predaja z kategórií a produktov. Shoptet, Marketplace, Google Shopping.", "🛒", "tag-yellow"),
    ("/sk/sluzby/seo-audit/", "SEO audit a analýza", "Presný obraz toho, čo váš web brzdí, s plánom podľa priorít.", "📋", "tag-blue"),
    ("/sk/sluzby/linkbuilding/", "Linkbuilding", "Spätné odkazy a autorita, bez ktorých sa hore nedostanete.", "🔗", "tag-red"),
    ("/sk/sluzby/tvorba-webov/", "Tvorba webov", "Rýchly web na mieru, ktorý sa nájde a predáva. WordPress aj e-shop.", "⚡", "tag-green"),
    ("/sk/sluzby/ppc-reklama/", "PPC reklama", "Google Ads pre výsledky hneď, kým SEO naberá tempo.", "🎯", "tag-yellow"),
    ("/sk/sluzby/email-marketing/", "Email marketing", "Newsletter a automatizácie, ktoré zákazníkov vracajú späť.", "✉️", "tag-blue"),
]


def services_grid(cols: int = 3) -> str:
    items = []
    for href, title, text, icon, tag in SERVICES_LIST:
        items.append(f"""
<div class="benefit-card card-hover reveal" data-delay="150">
  <span class="benefit-icon icon-blue">{icon}</span>
  <h3><a href="{href}" style="color:var(--text);">{title}</a></h3>
  <p>{text}</p>
  <div class="project-tags"><span class="project-tag {tag}">Služba</span></div>
</div>""")
    return f'<div class="grid-{cols}">{"".join(items)}</div>'


def svc_page_faq(common_qa: list[tuple[str, str]]) -> list[tuple[str, str]]:
    return common_qa


PROCESS_STEPS = [
    {"title": "Bezplatný audit", "text": "Začneme 30-minútovým hovorom a bezplatným auditom vášho webu. Vidíte presne, čo brzdí pozície, predaj a AI odporúčania."},
    {"title": "Plán podľa priorít", "text": "Z auditu spravíme jasný plán: čo opraviť ako prvé, ktoré kľúčové slová prinášajú zákazníkov a koľko hodín mesačne to zaberie."},
    {"title": "Práca v týždenných dávkach", "text": "Robíme: technika, obsah, Google profil, AI viditeľnosť, odkazy. Vždy viete, čo sa stalo v predchádzajúcom týždni."},
    {"title": "Meranie a report", "text": "Mesačný report: pozície, kliky z Google, kontakty a objednávky, zmienky v AI. Platíte len za odpracované hodiny."},
]


def process_section(label: str = "Ako pracujeme") -> str:
    return f"""
<section class="section section-alt" id="proces">
  <div class="container">
    <div class="section-head">
      <span class="section-label">{label}</span>
      <h2>Štyri kroky. Žiadne pevné zmluvy.</h2>
      <p class="section-subheading">Viete vždy, čo robíme, prečo a čo to prinieslo. Každá hodina je vykazovaná.</p>
    </div>
    {steps_block(PROCESS_STEPS)}
  </div>
</section>
"""


# ---------------------------------------------------------------- HOME

def home() -> tuple[str, str]:
    h1 = ('Nech vás zákazníci nájdú v <span class="hl-blue">Google</span>, '
          'na <span class="hl-red">Google Mapách</span> aj v <span class="hl-green">ChatGPT</span>.')
    sub = ("Nokto Studio je SEO agentúra pre podnikateľov. Privedieme vám zákazníkov z organického "
           "vyhľadávania, Google Máp aj AI nástrojov a posunieme predaj vášho e-shopu. Za transparentných "
           "12 EUR za hodinu. Bez paušálov, bez pevných zmlúv, s reportom, ktorému rozumiete.")

    body = f"""
<!-- HERO -->
<section class="hero">
  <div class="container">
    <div class="hero-content">
      <span class="hero-label">SEO agentúra pre podnikateľov · SK a CZ</span>
      <h1>{h1}</h1>
      <p class="hero-sub">{sub}</p>
      <div class="hero-ctas">
        <a href="{CAL}" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg">Bezplatný strategický hovor</a>
        <a href="/sk/kontakt/?audit=1" class="btn btn-outline btn-lg">Chcem bezplatný audit webu</a>
      </div>
      <p class="hero-scarcity">Kapacita na nové projekty: otvorené od októbra 2026.</p>
    </div>
  </div>
</section>

{TRUST_STATS}
{LOGOS}

<!-- PRE KOHO SME -->
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Pre koho to robíme</span>
      <h2>Štyri veci, ktoré podnikatelia od nás chcú</h2>
      <p class="section-subheading">Každý klient si vyberá jeden alebo viac cielov. My staviame systém, ktorý ich obsluhuje spolu.</p>
    </div>
    <div class="grid-4">
      <div class="benefit-card card-hover reveal" data-delay="100">
        <span class="benefit-icon icon-blue">🤖</span>
        <h3>Nech ma AI odporúča</h3>
        <p>Keď zákazník pýta ChatGPT alebo Gemini odporúčanie, chcete byť v odpovedi. Stavíme web tak, aby mu AI nástroje rozumeli a citovali ho.</p>
      </div>
      <div class="benefit-card card-hover reveal" data-delay="200">
        <span class="benefit-icon icon-red">📍</span>
        <h3>Zákazníci z Google a Mápy</h3>
        <p>Lokálne hľadanie a Google firemný profil sú najrýchlejšia cesta k zákazníkom z okolia. Nastavíme ich a vyhodnocujeme každý týždeň.</p>
      </div>
      <div class="benefit-card card-hover reveal" data-delay="300">
        <span class="benefit-icon icon-yellow">🛒</span>
        <h3>Viac predaja na e-shope</h3>
        <p>Kategórie a produkty optimalizujeme na kľúčové slová, ktoré kupujú. Google Shopping a Heureka sledujeme ako súčasť systému.</p>
      </div>
      <div class="benefit-card card-hover reveal" data-delay="400">
        <span class="benefit-icon icon-green">📈</span>
        <h3>Viac ponúk pre služby</h3>
        <p>Služby predávame cez obsahové stránky, ktoré odpovedajú na otázky zákazníkov. Z väčšieho záujmu vyrobíte viac ponúk a zákazok.</p>
      </div>
    </div>
  </div>
</section>

<!-- SLUZBY -->
<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Služby</span>
      <h2>Jeden systém, deväť služieb</h2>
      <p class="section-subheading">Vyberiete si, čo potrebujete. Väčšina klientov začína auditom a SEO optimalizáciou.</p>
    </div>
    {services_grid(3)}
    <div style="text-align:center; margin-top:36px;">
      <a href="/sk/sluzby/" class="btn btn-outline">Všetky služby a ceny za hodinu</a>
    </div>
  </div>
</section>

{process_section()}

<!-- CENNIK TEASER -->
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Cenník</span>
      <h2>12 EUR za hodinu. Platíte len za prácu.</h2>
      <p class="section-subheading">Žiadne mesačné paušály, ktoré nevedíte, čo obsahujú. Každá hodina je vykazovaná v reporte.</p>
    </div>
    <div class="rate-band">
      <div>
        <div class="rate-big">12 EUR <small>za hodinu práce</small></div>
        <p style="margin-top:8px; max-width:520px;">Balíčky sú len odporúčané rozsahy. Kedykoľvek ich môžete meniť, bez sankcií.</p>
      </div>
      <a href="/sk/cennik/" class="btn btn-primary btn-lg">Pozrieť celý cenník</a>
    </div>
  </div>
</section>

<!-- CASE STUDY -->
<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Prípadová štúdia</span>
      <h2>Villa Paris: značka, web a lokálne SEO od nuly</h2>
      <p class="section-subheading">Prémiové ubytovanie v Piešťanoch s jedným cieľom: viac priamych rezervácií bez provízií portálov.</p>
    </div>
    <div class="grid-2">
      <div class="project-card card-hover">
        <div class="project-card-body">
          <h3>Mikramt.sk, Martin</h3>
          <p>Vlastný e-shop s API integráciou na účtovný systém Sunsoft Ecosun pre regionálneho dodávateľa stolárskych potrieb. Za 9 mesiacov sme vygenerovali online tržby pripísané do kanálov email a organický Google. Súčasťou je email marketing, lokálne SEO a optimalizácia pre AI vyhľadávače, tak aby značku odporúčali ChatGPT aj Google AI Overviews.</p>
          <div class="case-result">
            <div><strong>2 492,75 EUR</strong><span>tržby za 9 mesiacov</span></div>
            <div><strong>15</strong><span>objednávok z emailu a organika</span></div>
            <div><strong>722 EUR</strong><span>najväčšia objednávka</span></div>
          </div>
          <div class="project-tags">
            <span class="project-tag tag-yellow">E-shop SEO</span>
            <span class="project-tag tag-green">Email marketing</span>
            <span class="project-tag tag-red">Lokálne SEO + GEO</span>
          </div>
          <a href="{CAL}" target="_blank" rel="noopener noreferrer" class="btn btn-outline" style="margin-top:20px;">Povedať si viac</a>
        </div>
      </div>
      <div class="project-card card-hover">
        <div class="project-card-body">
          <h3>Villa Paris, Piešťany</h3>
          <p>Rebrand, nový web, hotelový copywriting a lokálne SEO v jednom systéme. Cieľom bolo, aby hosť pochopil hodnotu ubytovania skôr, ako porovná konkurenciu, a rezervoval priamo.</p>
          <div class="case-result">
            <div><strong>Rebrand</strong><span>identita + logo</span></div>
            <div><strong>Web</strong><span>nová štruktúra</span></div>
            <div><strong>Lokálne SEO</strong><span>Google profil</span></div>
          </div>
          <div class="project-tags">
            <span class="project-tag tag-blue">Branding</span>
            <span class="project-tag tag-green">Web dizajn</span>
            <span class="project-tag tag-yellow">Copywriting</span>
            <span class="project-tag tag-red">Lokálne SEO</span>
          </div>
          <a href="/sk/villa-paris/" class="btn btn-outline" style="margin-top:20px;">Čítať celý príbeh</a>
        </div>
      </div>
    </div>
    <div style="text-align:center; margin-top:32px;">
      <a href="/sk/pripady/" class="btn btn-outline">Všetky prípadové štúdie</a>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Časté otázky</span>
      <h2>Najdôležitejšie odpovede na jedno miesto</h2>
    </div>
    {faq_block(HOME_FAQ)}
    <div style="text-align:center; margin-top:28px;">
      <a href="/sk/faq/" class="btn btn-outline">Všetky časté otázky</a>
    </div>
  </div>
</section>

<!-- CTA -->
<section class="section" style="padding-top:0;">
  <div class="container">
    {cta_band("Začnite bezplatným auditom", "30 minút telefonátu a bezplatný audit vášho webu. Dozviete sa, čo brzdí vaše pozície a predaj, aj keď sa nakoniec rozhodnete inak.", "sk")}
  </div>
</section>
"""

    faq_schema_html = faq_schema(HOME_FAQ, BASE + "/")
    html = base(
        market="sk", path="", title="Nokto Studio | SEO agentúra pre podnikateľov: Google aj ChatGPT",
        desc="SEO agentúra pre podnikateľov. Zákazníci z Google a Google Mápy, odporúčania v ChatGPT a AI nástrojoch, viac predaja na e-shope. 12 EUR za hodinu, bezplatný audit.",
        canonical=BASE + "/", body=body, prefix="",
        extra_head=ORG_SCHEMA + faq_schema_html,
    )
    return ("index.html", html)


HOME_FAQ = [
    ("Koľko stojí SEO optimalizácia webu?",
     "Za prácu platíte 12 EUR za hodinu. Malý web zvládneme v 10 hodinách mesačne (120 EUR), väčší e-shop v 40 hodinách (480 EUR). Presný rozsah vám potvrdíme v pláne po bezplatnom audite."),
    ("Ako dlho trvá, kým SEO prinesie výsledky?",
     "Prvé pohyby vidíte na menej konkurenčných kľúčových slovách zvyčajne za 2 až 4 mesiace. Na hlavné dotazy v konkurenčných odvetviach trvá 6 až 12 mesiacov. Reálne termíny vám povieme už v audite."),
    ("Budem vidieť, za čo platím?",
     "Áno. Každý mesiac dostanete report s odpracovanými hodinami, ich obsahom a výsledkami: pozície, kliky z Google, kontakty a objednávky. Bez reportovania sa nepohne žiadna práca."),
    ("Pomôžete mi, aby ma ChatGPT odporúčal?",
     "Áno, to je naša špecializácia. Optimalizujeme web pre AI nástroje (ChatGPT, Gemini, AI Overviews) tak, aby vás odporúčali pri dotazoch vašich zákazníkov."),
    ("Sú zmluvy viažúce na 12 mesiacov?",
     "Nie. Pracujeme mesačne, spoluprácu môžete skončiť kedykoľvek. Dôveru staviame na výsledkoch, nie na viazanosti."),
]


# ---------------------------------------------------------------- SERVICES HUB

def sluzby() -> tuple[str, str]:
    body = f"""
{page_hero("Služby", "Služby, ktoré vám privedú zákazníkov",
           "Od technického SEO po AI viditeľnosť. Každá služba stojí 12 EUR za hodinu, rozsah dohodnete v pláne.",
           [("Domov", "/"), ("Služby", None)])}
<section class="section">
  <div class="container">
    {services_grid(3)}
  </div>
</section>
{process_section()}
<section class="section" style="padding-top:0;">
  <div class="container">
    {cta_band("Neviete, čo potrebujete? Začnite auditom.", "Bezplatný audit vám povie, kde sú najväčšie šance na rast. Z neho vznikne plán aj odhad hodín.", "sk")}
  </div>
</section>
"""
    html = base(
        market="sk", path="sluzby/", title="Služby: SEO, Mapy, AI viditeľnosť, e-shopy | Nokto Studio",
        desc="SEO optimalizácia webu, lokálne SEO a Google firemný profil, SEO pre AI vyhľadávače, e-shop SEO, audit, linkbuilding, weby, PPC a email marketing. 12 EUR za hodinu.",
        canonical=BASE + "/sk/sluzby/", body=body, prefix="../..", extra_head=ORG_SCHEMA,
    )
    return ("sk/sluzby/index.html", html)


# ---------------------------------------------------------------- SERVICE PAGES

def _service_page(*, path: str, title: str, desc: str, label: str, h1: str,
                  intro: str, for_who: list[str], deliverables: list[str],
                  faq: list[tuple[str, str]], slug: str, svc_name: str) -> tuple[str, str]:
    url = BASE + f"/sk/sluzby/{slug}/"
    who = "".join(f"<li>{w}</li>" for w in for_who)
    deliv = "".join(f'<li><span class="check">✓</span><span>{d}</span></li>' for d in deliverables)
    body = f"""
{page_hero(label, h1, intro, [("Domov", "/"), ("Služby", "/sk/sluzby/"), (label.replace("Služba · ", ""), None)])}

<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:start;">
      <div class="prose">
        <h2>Pre koho je táto služba</h2>
        <ul>{who}</ul>
      </div>
      <div class="card">
        <span class="section-label">Čo dodávame</span>
        <ul class="deliv-list">{deliv}</ul>
      </div>
    </div>
  </div>
</section>

{process_section("Ako pobeží spolupráca")}

<section class="section section-alt">
  <div class="container">
    <div class="rate-band">
      <div>
        <div class="rate-big">12 EUR <small>za hodinu · kedykoľvek skončíte</small></div>
        <p style="margin-top:8px; max-width:520px;">Táto služba zvyčajne potrebuje 8 až 20 hodín mesačne, podľa rozsahu webu a konkurencie.</p>
      </div>
      <div class="hero-ctas">
        <a href="{CAL}" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg">Bezplatný hovor</a>
        <a href="/sk/cennik/" class="btn btn-outline btn-lg">Cenník</a>
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
    {cta_band("Chcete vedieť, čo by táto služba priniesla vášmu webu?", "Bezplatný audit a 30 minút času. Žiadne záväzky.", "sk")}
  </div>
</section>
"""
    extra = schema_service(svc_name, desc, url) + faq_schema(faq, url)
    html = base(market="sk", path=f"sluzby/{slug}/", title=title, desc=desc,
                canonical=url, body=body, prefix="../../../", extra_head=ORG_SCHEMA + extra)
    return (f"sk/sluzby/{slug}/index.html", html)


def seo_optimalizacia() -> tuple[str, str]:
    return _service_page(
        path="sluzby/seo-optimalizacia/", slug="seo-optimalizacia",
        title="SEO optimalizácia webu a web stránok | Nokto Studio",
        desc="SEO optimalizácia web stránok: technika, obsah, kľúčové slová. Pozície v Google, ktoré privedú zákazníkov. 12 EUR za hodinu, bezplatný audit.",
        label="Služba · SEO optimalizácia",
        h1="SEO optimalizácia, ktorá privedie zákazníkov",
        intro="Zákazník, ktorý vás hľadá v Google, je najlacnejší zákazník. Postavíme web tak, aby mu Google rozumel a zaradil ho hore a návštevníci z neho chodili s otázkou, nie s otáznikom.",
        for_who=[
            "Máte web, ktorý neprináša kontakty ani objednávky z vyhľadávania.",
            "Konkurencia vás predbieha na dotazoch, ktoré vás zaujímajú.",
            "Ste viditeľní len na názve firmy, nie na tom, čo predávate.",
            "Platíte reklamu a chceli by ste časť dopytov zachytiť zdarma.",
        ],
        deliverables=[
            "Kľúčová analýza: na čo zákazníci reálne hľadajú a čo to stojí za prácu.",
            "Technická oprava webu: rýchlosť, indexácia, kanonizácia, chyby 404, sitemap.",
            "Prepis titulkov a popiskov na dotazy, ktoré majú reálny dopyt.",
            "Nové obsahové stránky na dopyty, kde konkurencia nie je silná.",
            "Interné prelinkovanie, ktoré posunie silné stránky vyššie.",
            "Mesačný report: pozície, kliky z Search Console, kontakty.",
        ],
        faq=[
            ("Koľko hodín mesačne zaberie SEO optimalizácia?",
             "Firemný web zvládneme v 10 hodinách mesačne (120 EUR), e-shop v 20 až 40 hodinách (240 až 480 EUR). Rozsah potvrdíme v pláne po audite."),
            ("Na ako dlho sa stanovujú výsledky?",
             "Prvé pohyby na menej konkurenčných dotazoch za 2 až 4 mesiace, na hlavné dotazy 6 až 12 mesiacov. Záleží na konkurencii a stave webu."),
            ("Robíte aj obsah? Nemám čas písať.",
             "Áno, písanie obsahu je súčasť hodín. Sami navrhneme štruktúru, vypíšeme texty a pred publikovaním ich schválite."),
            ("Čo ak som už SEO robil a nič to neprinieslo?",
             "Bezplatný audit presne povie, čo predchádzajúca práca nechala nedokončené. Často chýbajú dva či tri kroky, nie celé SEO."),
        ],
        svc_name="SEO optimalizácia webu",
    )


def lodalne_seo() -> tuple[str, str]:
    return _service_page(
        path="sluzby/lodalne-seo/", slug="lodalne-seo",
        title="Lokálne SEO a firemný profil Google Mapy | Nokto Studio",
        desc="Lokálne SEO: Google firemný profil, Google Mapy, hodnotenia a lokálne kľúčové slová. Zákazníci z okolia vás nájdu prví. 12 EUR za hodinu.",
        label="Služba · Lokálne SEO",
        h1="Lokálne SEO: zákazníci z okolia vás nájdu prví",
        intro="Keď si niekto vyhľadá zubára, autoservisu, kuchýň alebo strech vo svojom meste, rozhodnú tri veci: Google Mapy, hodnotenia a web. Nastavíme všetky tri a držíme ich v poriadku.",
        for_who=[
            "Prevádzkujete firmu s pôsobiskom: služby, reštaurácia, ordinácia, workshop.",
            "Na Google Mapách ste chýbali, máte chýbajúce dáta alebo žiadne hodnotenia.",
            "Konkurencia je v mápe hore, hoci má horšiu ponuku.",
            "Chcete telefón a kontakty z okolia, nie z celého Slovenska.",
        ],
        deliverables=[
            "Kompletné nastavenie a čiistenie Google firemného profilu (My Business).",
            "Kategórie, služby, otváracie časy, fotky a Q&A, ktoré Google ocení.",
            "Stratégia na získavanie hodnotení a odpovede na ne.",
            "Lokálne kľúčové slová: mesto + služba, okres + služba.",
            "Lokálne citácie v adresároch a branžových weboch (firmy.sk a podobné).",
            "Týždenný prehľad: volania, požiadavky o trasy, zobrazenia v mápe.",
        ],
        faq=[
            ("Koľko trvá, kým Google profil začne fungovať?",
             "Prvé zlepšenia v mápe viditeľné za 4 až 8 týždňov, stabilná pozícia trvá 3 až 6 mesiacov. Záleží na konkurencii v okolí."),
            ("Vlastním len jeden pôsob. Nahrá mi to?",
             "Práve pre jedno pôsobisko je lokálne SEO najúčinnejšie. Sústredíte všetku silu do vášho mesta a okresu, kde je konkurencia najmenšia."),
            ("Ako získam viac hodnotení na Google?",
             "Máme jednoduchý postup cez SMS a QR kód, ktorý zákazníkov vyzýva hneď po vykonaní služby. Zvyšuje mieru recenzií niekoľkonásobne."),
            ("Ako riešite zlé hodnotenia?",
             "Odpovedáme profesionálne a na mieste. Zlé hodnotenia nemožno odstrániť, ale dobrý pomer a kultivované odpovede pôsobia na zákazníkov viac ako počty hviezd."),
        ],
        svc_name="Lokálne SEO a Google firemný profil",
    )


def seo_ai() -> tuple[str, str]:
    return _service_page(
        path="sluzby/seo-pre-ai-vyhladavace/", slug="seo-pre-ai-vyhladavace",
        title="SEO pre AI vyhľadávače: ChatGPT a AI Overviews | Nokto Studio",
        desc="Optimalizácia pre AI vyhľadávače a AI Overviews. ChatGPT a Gemini vás odporúčajú zákazníkom. Prvá agentúra na Slovensku s touto špecializáciou.",
        label="Služba · SEO pre AI",
        h1="Aby vás ChatGPT odporúčal zákazníkom",
        intro="Zákazník dnes nepýta len Google. Pýta ChatGPT: \u201eOdporúč mi dobrú zubačku v Nitre.\u201c AI nástroj odpovie dvomi až piatimi menami. Našou úlohou je, aby vaše meno tam bolo.",
        for_who=[
            "Chcete, aby vás AI nástroje odporúčali ako prvú voľbu vo vašom odvetví.",
            "Vidíte, že zákazníci prichádzajú s vetou \u201enajol ChatGPT, že...\u201c",
            "Konkurencia sa na AI odporúčania zatiaľ nepripravuje (to je výhoda).",
            "Máte expertízu a chcete ju viditeľnú aj pre AI, nie len pre Google.",
        ],
        deliverables=[
            "Audit AI viditeľnosti: kto vás dnes ChatGPT, Gemini a AI Overviews citujú a kto vás chýba.",
            "Priame odpovede na stránkach: úvodné odseky vo formáte, ktorý AI čerpá.",
            "Štruktúrované dáta (schema.org) pre ľahké čítanie AI nástrojmi.",
            "Obsahové stránky odpovedajúce na reálne otázky zákazníkov (People Also Ask, AI dotazy).",
            "Mesačné sledovanie: v ktorých AI odpovediach sa objavujete a čo sa zmenilo.",
            "Prevádzka rozšírení pre AI roboty (llms.txt, robots.txt, prístup pre GPTBot a PerplexityBot).",
        ],
        faq=[
            ("Je toto SEO alebo marketing?",
             "Je to priame pokračovanie SEO. Google aj ChatGPT čerpajú z webu, rozdiel je v tom, čo a ako čítajú. Nastavíme oboje naraz."),
            ("Ako meriate, či ma AI odporúča?",
             "Pravidelne testujeme sadu dotazov, ktoré vaši zákazníci pýtajú, a zaznamenávame, či sa vaše meno v odpovediach objavuje. Výsledky máte v reporte."),
            ("To môže trvať dlho?",
             "Víťazstvo v AI odporúčaniach je zvyčajne rýchlejšie než klasicke SEO pozície, pretože konkurencia tu len začíná. Prvé menovanie vidíme často do 2 až 3 mesiacov."),
            ("Pre koho to má zmysel?",
             "Pre služby, kde zákazník hľadá odporúčanie: zdravotníctvo, právo, servis, stavebníctvo, školenia. Pre e-shopy pomáha v dotazoch typu \u201eko predáva...\" a v recenziách."),
        ],
        svc_name="Optimalizácia pre AI vyhľadávače",
    )


def eshop_seo() -> tuple[str, str]:
    return _service_page(
        path="sluzby/seo-pre-eshopy/", slug="seo-pre-eshopy",
        title="SEO pre e-shopy: Shoptet a Google Shopping | Nokto Studio",
        desc="SEO optimalizácia e-shopu: kategórie, produkty, Shoptet, Marketplace aj Google Shopping. Viac predaja z organického vyhľadávania. 12 EUR za hodinu.",
        label="Služba · SEO pre e-shopy",
        h1="E-shop SEO: viac objednávok z Google",
        intro="E-shop má jedinú reálnu metru úspechu: objednávky. Optimalizujeme kategórie a produkty na dotazy, ktoré kupujú, aby vás Google aj Marketplace našli bez nutnosti platiť za každý klik.",
        for_who=[
            "Máte e-shop (Shoptet, WooCommerce, vlastné riešenie) a predaj závisí od reklamy.",
            "Kategórie nemajú vlastné texty a nepredávajú sa samy.",
            "Ste viditeľní len na názvoch produktov, nie na tom, čo zákazník reálne hľadá.",
            "Chcete znížiť náklady na reklamu tým, že časť dopytov chytíte zdarma.",
        ],
        deliverables=[
            "Analýza kľúčových slov pre kategórie a hlavné produkty.",
            "Texty kategórií a produktov, ktoré predávajú a nie len opisujú.",
            "Technická hygiena: kanonizácie, filtrované URL, rýchlosť, produktové dáta.",
            "Google Merchant Center a Google Shopping v poriadku.",
            "Poradenstvo pre Heureka a Marketplace integrácie.",
            "Report v objednávkach a tržbe z organického kanála.",
        ],
        faq=[
            ("Robíte SEO aj pre Shoptet?",
             "Áno, Shoptet je na Slovensku najbežnejšia platforma a poznáme jej špecifiká (filtry, varianty, SEO moduly)."),
            ("Koľko objednávok z toho bude?",
             "Reálne čísla vám povieme po audite, na základe vašich kľúčových slov a ich dopytu. Nikdy nepoviem číslo, ktoré nedokážem podporiť dáta."),
            ("Musím robiť aj linkbuilding?",
             "Pre konkurenčné kategórie áno, odozva bez autority je pomalá. Doporučíme rozsah, ktorý dava zmysel pre váš rozpočet."),
            ("Ako meriame úspech?",
             "V Google Analytics a Search Console sledujeme objednávky a tržbu z organického vyhľadávania. Report máte mesačne."),
        ],
        svc_name="SEO pre e-shopy",
    )


def audit_seo() -> tuple[str, str]:
    return _service_page(
        path="sluzby/seo-audit/", slug="seo-audit",
        title="SEO audit webu a analýza kľúčových slov | Nokto Studio",
        desc="SEO audit webu s akčným plánom: technika, obsah, kľúčové slová, konkurencia. Bezplatný vstupný audit, detailný od 12 EUR za hodinu.",
        label="Služba · SEO audit",
        h1="SEO audit: presný obraz toho, čo váš web brzdí",
        intro="Audit nie je PDF na police. Je to zoznam úloh s prioritami a odhadom hodín. Začína sa bezplatným vstupným auditom, ktorý máte do troch dní.",
        for_who=[
            "Neviete, prečo web neprináša zákazníkov.",
            "SEO ste urobili, ale výsledky chýbajú.",
            "Pred veľkou investíciou do webu chcete objektívny rozbor.",
            "Potrebujete plán, ktorý vykonáte sami alebo s nami.",
        ],
        deliverables=[
            "Vstupný audit zdarma: 10 najväčších problémov na 1 strane.",
            "Detailný audit: technika, indexácia, obsah, interné prelinkovanie.",
            "Analýza kľúčových slov s objemami dopytov a odhadom reálnych šancí.",
            "Rozbor konkurencie: čo robiť, aby vás dobehli.",
            "Plán s prioritami a odhadom hodín na každú položku.",
            "Prehliadka s vami: 45 minút odpovedí na vaše otázky.",
        ],
        faq=[
            ("Koľko stojí SEO audit?",
             "Vstupný audit je zdarma. Detailný audit stojí 240 až 480 EUR podľa rozsahu webu (20 až 40 hodín × 12 EUR)."),
            ("Dostanem aj súbor, ktorý môžem odovzdať vývojárovi?",
             "Áno. Plán je v zrozumiteľnom formáte s úlohami po jednotlivých krokoch, priamo pre používateľa v CMS alebo vývojáru."),
            ("Musím potom brať aj ďalšie služby?",
             "Nie. Plán si môžete vykonať sami alebo s iným partnerom. Ak sa rozhodnete pracovať s nami, plán slúži ako základ spolupráce."),
            ("Ako rýchlo dostanem audit?",
             "Vstupný audit do 3 pracovných dní od prvého hovoru. Detailný audit za 7 až 10 dní."),
        ],
        svc_name="SEO audit a analýza kľúčových slov",
    )


def linkbuilding() -> tuple[str, str]:
    return _service_page(
        path="sluzby/linkbuilding/", slug="linkbuilding",
        title="Linkbuilding a spätné odkazy | Nokto Studio",
        desc="Linkbuilding: spätné odkazy a autorita webu. Bezpečné metódy, reálne domény, transparentné vykazovanie. 12 EUR za hodinu.",
        label="Služba · Linkbuilding",
        h1="Linkbuilding: autorita, ktorá drží pozície",
        intro="Technika a obsah vás dovedú do stredu výsledkov, autorita vás posunie hore. Staviame odkazy, ktoré Google akceptuje a zákazníci aj citujú.",
        for_who=[
            "Máte technicky v poriadku web a obsah, ale pozície stoja.",
            "Konkurencia má silnejší link profil a predbieha vás.",
            "Chcete odkazy z reálnych slovenských a českých domén, nie zo spamových sietí.",
            "Chcete transparentné vykazovanie, kde odkazy vznikli a čo stoja.",
        ],
        deliverables=[
            "Rozbor link profilu: čo vás brzdí, ktoré odkazy chýbajú.",
            "Tématické a lokálne odkazy: adresáre, branže, média, partnéri.",
            "Pripravené obsahy a PR články, ktoré odkazy nesú.",
            "Sledovanie nových odkazov a stratených odkazov.",
            "Jasná cena za odkaz, bez prirážky.",
            "Mesačný prehľad: nové domény, posun pozícií.",
        ],
        faq=[
            ("Kolko stoja odkazy?",
             "Cena odkazu závisí od domény. Väčšina slovenských odkazov stojí 50 až 300 EUR, mediálne PR články viac. Vykazujeme skutočné ceny, žiadna medzifenekcia."),
            ("Ako dlho trvá, kým odkazy pomôžu?",
             "Nové odkazy sa uplatnia v 4 až 12 týždňoch. Preto kombinujeme linkbuilding s obsahovou prácou, ktorá už teraz niečo prináša."),
            ("Robíte aj kupovanie odkazov?",
             "Pracujeme len s reálnymi, viditeľnými miestami. Nikdy nepoužívame siete automatizovaných spamov, ktoré skôr alebo neskôr Google sankcionuje."),
            ("Koľko odkazov potrebujem mesačne?",
             "Malý firemný web 2 až 5, e-shop v konkurenčnej bráne 5 až 10. Väčšie čísla nie vždy znamenajú lepší výsledok."),
        ],
        svc_name="Linkbuilding",
    )


def tvorba_webov() -> tuple[str, str]:
    return _service_page(
        path="sluzby/tvorba-webov/", slug="tvorba-webov",
        title="Tvorba web stránok optimalizovaných pre SEO | Nokto Studio",
        desc="Tvorba web stránok a e-shopov, ktoré sú rýchle, na mieru a rovno optimalizované pre Google aj AI nástroje. Cena 12 EUR za hodinu práce.",
        label="Služba · Tvorba webov",
        h1="Tvorba web stránok, ktoré sa nájdu a predávajú",
        intro="Krásny web bez zákazníkov je drahý doplnok. Staviame weby, ktoré sú rýchle, zrozumiteľné a rovno postavené na kľúčových slovách, o ktoré sa vás zaujímajú.",
        for_who=[
            "Máte web, ktorý je pomalý, starý alebo neprináša kontakty.",
            "Chcete nový web alebo e-shop, ktorý bude hneď SEO v poriadku.",
            "Potrebujete, aby AI nástroje webu rozumeli od prvého dňa.",
            "Chcete web, ktorý sami dokážete upravovať (WordPress, Shoptet).",
        ],
        deliverables=[
            "Struktúra postavená na kľúčových slovách, nie na vnútorných predstah.",
            "Rýchly web: optimalizované obrázky, čistý HTML, PageSpeed zelený.",
            "SEO rovné od štartu: kanonizácie, sitemap, schema.org, odpovede pre AI.",
            "E-shop na Shoptet alebo WooCommerce s nastaveným Merchant Centrom.",
            "Jednoduchá úprava obsahu pre vás (návody, podpora).",
            "Po spustení: sledovanie a prvá mesačná SEO kontrola zdarma.",
        ],
        faq=[
            ("Koľko stojí nový web?",
             "Firemný web 30 až 50 hodín práce (360 až 600 EUR), e-shop od 60 hodín (720 EUR). Vysvetlíme si to po hovore, bezplatne."),
            ("Kde budete weby hostiť?",
             "Webhosting si vyberáme podľa výkonnosti a ceny (Websupport, VPS). Svoje práva si držíte, web je váš."),
            ("Budem môcť upravovať obsah sám?",
             "Áno, všetko staviame v systémoch, v ktorých si obsah dokážete upraviť sami. K tomu dostanete návod."),
            ("Robíte aj redesign existujúceho webu?",
             "Áno, redesign je častá úloha. Zabezpečíme, že staré URL a pozície sa nestrácajú."),
        ],
        svc_name="Tvorba webov a e-shopov",
    )


def ppc_reklama() -> tuple[str, str]:
    return _service_page(
        path="sluzby/ppc-reklama/", slug="ppc-reklama",
        title="PPC reklama a Google Ads | Nokto Studio",
        desc="Správa Google Ads kampaní: výkonnostné aj značkové. Zákazníci hneď, kým SEO naberá tempo. 12 EUR za hodinu, transparentné vykazovanie.",
        label="Služba · PPC reklama",
        h1="PPC reklama: zákazníci hneď, kým SEO naberá tempo",
        intro="SEO trvá mesiace. Reklama funguje od prvého dňa. Preto mnohým klientom spúšťame Google Ads súbežne a postupne ich premeňme na organickú trať.",
        for_who=[
            "Chcete zákazníkov a objednávky hneď, nie o šesť mesiacov.",
            "Platíte za reklamu, ale nevedíte, čo jej prináša.",
            "Vedenie kampaní vyzerá ako čierna skrinka.",
            "Chcete reklamu, ktorá spolupracuje s SEO, nie proti nemu.",
        ],
        deliverables=[
            "Nastavenie a štruktúra Google Ads kampaní podľa rozpočtu.",
            "Výber kľúčových slov a negatív, ktoré nepremrhajú rozpočet.",
            "Reklamné texty, ktoré predávajú a neznevažujú značku.",
            "Prevádzka konverzií v Google Analytics a Tag Manageri.",
            "Týždenná kontrola a mesačný report s reálnymi číslami.",
            "Poradenstvo, kedy kampaň stiahnuť a ustúpiť organickému rastu.",
        ],
        faq=[
            ("Koľko mám minúť na reklamu?",
             "Malý firemný web 300 až 600 EUR mesačne na reklamných výdavkov, e-shop 600 až 1500 EUR. Kampaň riadime podľa vašich možností."),
            ("Aký je rozdiel medzi PPC a SEO?",
             "PPC je platená reklama, výsledky hneď, platíte za každý klik. SEO je organické, trvá dlhšie, ale nezastaví sa, keď prestanete platiť."),
            ("Vidím, že mi reklama neprináša objednávky. Pomôžete?",
             "Áno. Najčastejšie je problém v sledovaní konverzií, v relevancii dopytov alebo v landing page. Zanalyzujeme to a opravíme."),
            ("Môžem mať len PPC bez SEO?",
             "Áno, ale dlhodobo je to najdrahší model. Reklamné ceny rastú, organické dopyty sú zdarma. Doporučíme kombináciu."),
        ],
        svc_name="PPC reklama (Google Ads)",
    )


def email_marketing() -> tuple[str, str]:
    return _service_page(
        path="sluzby/email-marketing/", slug="email-marketing",
        title="Email marketing a automatizácie | Nokto Studio",
        desc="Email marketing pre e-shopy aj firmy: newslettery, automatizácie, abandoned cart. Klaviyo a Brevo. 12 EUR za hodinu.",
        label="Služba · Email marketing",
        h1="Email marketing: zákazníkov vracajte späť",
        intro="Nový zákazník stojí viac než ten existujúci. Emaily a automatizácie predajov zvyšujú tržbu zo súčasnej základne bez ďalších nákladov na reklamu.",
        for_who=[
            "Máte e-shop a zákazníci nevracajú.",
            "Opúšťajú vás košíky (abandoned cart) bez opravenej hodnoty.",
            "Zber emailov nie je nastavený alebo neprináša kontakt.",
            "Chcete newsletter, ktorý sa dá napísať raz a posielať systematicky.",
        ],
        deliverables=[
            "Nastavenie zberu kontaktov a GDPR v poriadku.",
            "Základné automatizácie: víťazstvo série, opustený košík, post-purchase.",
            "Šablóny newsletterov v obojživenej forme (Klaviyo, Brevo).",
            "Segmentácia zákazníkov podľa správania.",
            "Mesačný plán kampaní a správa odosielania.",
            "Report: open rate, click rate, tržba z emailov.",
        ],
        faq=[
            ("Ktorý nástroj používate?",
             "Klaviyo pre e-shopy, Brevo pre firmy. Obe sú podľa nášho názoru najlepšie podľa ceny a výkonu."),
            ("Koľko emailov mesačne posielať?",
             "E-shop 4 až 8, firma 1 až 2. Viac nie je vždy lepšie, dôležité je správne časovanie a obsah."),
            ("Ako riešite GDPR a spam?",
             "Všetko cez súhlas, s možnosťou odhlásenia, bez nakupovania listín. Zásady sú na webe a v každému emaile."),
            ("Je toto drahé na správu?",
             "Nastavenie automatizácií trvá 10 až 20 hodín, potom mesiace 4 až 8 hodín (48 až 96 EUR)."),
        ],
        svc_name="Email marketing a automatizácie",
    )


# ---------------------------------------------------------------- CENNIK (money page)

CENNIK_PACKAGES = [
    {"name": "Štart", "hours": 10, "price": 120,
     "items": ["Audit webu a kľúčové slová (opakovanie)", "Technická oprava webu", "2 obsahové stránky alebo prepisy", "Firemný Google profil v poriadku", "Mesačný report"],
     "cta": "/sk/kontakt/"},
    {"name": "Rast", "hours": 20, "price": 240, "featured": True,
     "items": ["Všetko z balíčka Štart", "4 až 6 obsahových stránok mesačne", "Optimalizácia pre AI vyhľadávače", "Interné prelinkovanie a CRO tipy", "Linkbuilding (2 až 3 odkazy)", "Mesačný report a hovor 30 min"],
     "cta": "/sk/kontakt/"},
    {"name": "E-shop", "hours": 40, "price": 480,
     "items": ["Všetko z balíčka Rast", "Texty kategórií a produktov", "Google Merchant Center a Shopping", "Poradenstvo Heureka / Marketplace", "Automatizácie email marketingu", "Report s tržbami z organika"],
     "cta": "/sk/kontakt/"},
]

CENNIK_FAQ = [
    ("Koľko stojí SEO optimalizácia webu?",
     "Platíte 12 EUR za každú odpracovanú hodinu. Firemný web zvyčajne potrebuje 10 hodín mesačne (120 EUR), e-shop 20 až 40 hodín (240 až 480 EUR). Rozsah si nastavíte sami a môžete ho kedykoľvek meniť."),
    ("Prečo je to lacnejšie než konkurencia?",
     "Nemáme kancelárie ani manažérske vrstvy. Veľkú časť práce vykonávajú automatizované nástroje, ktoré sme si sami postavili, a odborný čas vkladáme tam, kde sa počíta. Úspory prenášame na vás."),
    ("Čo je v cene zahrnuté?",
     "Všetko okrem reklamných výdavkov a nákladov na odkazy či nástroje tretích strán. Tie vám vykazujeme v skutočnej cene, bez medzipozícií."),
    ("Musím platiť mesačne vopred?",
     "Fakturujeme mesačne dozadu za skutočne odpracované hodiny, s faktúrou. Paušál nie je potrebný."),
    ("Môžem spoluprácu kedykoľvek skončiť?",
     "Áno, kedykoľvek mesačný cyklus skončíte, bez sankcií a bez viazanosti. Dôveru si zaslúžime výsledkami."),
    ("Ako viem, že práca sa odviedla?",
     "Každý mesiac dostanete zoznam úloh s hodinami a ich výsledkom. Vy ste ten, kto kontroluje."),
]


def cennik() -> tuple[str, str]:
    body = f"""
{page_hero("Cenník", "Cenník: 12 EUR za hodinu, bez paušálov",
           "Platíte za odpracované hodiny. Každá hodina je vykazovaná v reporte. Spoluprácu skončíte kedykoľvek.",
           [("Domov", "/"), ("Cenník", None)])}

<section class="section">
  <div class="container">
    <div class="rate-band">
      <div>
        <div class="rate-big">12 EUR <small>za hodinu práce</small></div>
        <p style="margin-top:8px; max-width:560px;">SEO optimalizácia, lokálne SEO, AI viditeľnosť, obsah, linkbuilding, weby aj PPC. Jedna sadzba, jednoduché počty.</p>
      </div>
      <a href="{CAL}" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg">Nezáväzná ponuka</a>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Balíčky</span>
      <h2>Odporúčané rozsahy, nie povinné paušály</h2>
      <p class="section-subheading">Balíček je odporúčaný rozsah hodín na mesiac. Môžete ho kedykoľvek zmeniť, pozastaviť alebo skončiť.</p>
    </div>
    {price_cards(CENNIK_PACKAGES, "sk")}
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:start;">
      <div class="prose">
        <h2>Čo je v cene</h2>
        <ul class="deliv-list">
          <li><span class="check">✓</span><span>Všetka práca: technika, obsah, Google profil, AI viditeľnosť, odkazy, weby, PPC riadenie.</span></li>
          <li><span class="check">✓</span><span>Meranie a reporting: Search Console, Analytics, pozície, konverzie, zmienky v AI.</span></li>
          <li><span class="check">✓</span><span>Komunikácia: odpoveď do 12 hodín, mesačný hovor, neobmedzené otázky medzi tým.</span></li>
        </ul>
        <h2>Čo nie je v cene</h2>
        <ul class="deliv-list">
          <li><span class="check" style="background:#FCE8E6;color:var(--g-red-deep);">×</span><span>Reklamné výdavky (Google Ads, Meta Ads). Platíte priamo Google, nie nám.</span></li>
          <li><span class="check" style="background:#FCE8E6;color:var(--g-red-deep);">×</span><span>Náklady na odkazy a PR články. Vykazujeme skutočnú cenu od médí.</span></li>
          <li><span class="check" style="background:#FCE8E6;color:var(--g-red-deep);">×</span><span>Nájom nástrojov tretích strán, ak je potrebný (kurzy, platby, hosting).</span></li>
        </ul>
      </div>
      <div class="card">
        <span class="section-label">Príklad z praxe</span>
        <p style="margin-bottom:14px;">Firemný web právnej kancelárie v meste s 50 000 obyvateľov:</p>
        <ul class="deliv-list">
          <li><span class="check">✓</span><span><strong>Mesiac 1:</strong> audit + technická oprava + firemný profil (12 h = 144 EUR)</span></li>
          <li><span class="check">✓</span><span><strong>Mesiace 2 až 4:</strong> obsahové stránky na dotazy zákazníkov (10 h = 120 EUR)</span></li>
          <li><span class="check">✓</span><span><strong>Mesiace 5+</strong>: udržiavanie, linkbuilding, AI viditeľnosť (8 h = 96 EUR)</span></li>
        </ul>
        <p style="margin-top:14px; font-size:0.9rem; color:var(--text-muted);">Reálne čísla pre váš web vami potvrdíme v bezplatnom audite.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head"><span class="section-label">FAQ k cene</span><h2>Časté otázky k cenníku</h2></div>
    {faq_block(CENNIK_FAQ)}
  </div>
</section>

<section class="section">
  <div class="container">
    {cta_band("Koľko by to stálo vás?", "Bezplatný audit a odhad hodín pre váš konkrétny web. Bez záväzkov, s reálnymi číslami.", "sk")}
  </div>
</section>
"""
    faq_html = faq_schema(CENNIK_FAQ, BASE + "/sk/cennik/")
    html = base(market="sk", path="cennik/", title="Cenník SEO: 12 EUR za hodinu, bez paušálov | Nokto Studio",
                desc="SEO cenník s transparentnou hodinovou sadzbou 12 EUR. Balíčky od 120 EUR mesačne, bez pevných zmlúv. Bezplatný audit.",
                canonical=BASE + "/sk/cennik/", body=body, prefix="../..", extra_head=ORG_SCHEMA + faq_html)
    return ("sk/cennik/index.html", html)
