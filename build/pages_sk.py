# -*- coding: utf-8 -*-
"""
Nokto Studio - SK page content.
Every function returns (rel_path, html) where rel_path is inside the repo.
"""
from engine import (base, page_hero, cta_band, faq_block, faq_schema,
                    price_cards, steps_block, benefit_cards, schema_service,
                    results_slider, partner_logo_card, ORG_SCHEMA, EMAIL,
                    LOGO, BASE, gicon)

SK_ROOT = "/sk/"

# ---------------------------------------------------------------- shared blocks

TRUST_STATS = """
<div class="trust-strip">
  <div class="container">
    <div class="trust-grid">
      <div class="trust-stat reveal" data-delay="100">
        <span class="trust-num tn-blue">12&nbsp;EUR</span>
        <span class="trust-label">transparentná hodinová<br>sadzba, bez paušálov</span>
      </div>
      <div class="trust-stat reveal" data-delay="200">
        <span class="trust-num tn-red">0 EUR</span>
        <span class="trust-label">prvý hovor a audit<br>webu sú bezplatné</span>
      </div>
      <div class="trust-stat reveal" data-delay="300">
        <span class="trust-num tn-yellow">1. deň</span>
        <span class="trust-label">bezplatný audit<br>začne hneď po prvom hovore</span>
      </div>
      <div class="trust-stat reveal" data-delay="400">
        <span class="trust-num tn-green">30 min</span>
        <span class="trust-label">mesačný report<br>ako hovor so mnou</span>
      </div>
    </div>
  </div>
</div>
"""

LOGOS = """
<section class="logo-strip-section">
  <p class="logo-strip-heading">Značky, s ktorými som pracoval</p>
  <div class="marquee-viewport">
    <div class="marquee-track">
            <span class="logo-badge"><img loading="lazy" class="logo-inv" src="/assets/img/logos/mikramt.png" alt="Mikramt.sk"></span>
      <span class="logo-badge"><img loading="lazy" src="/assets/img/logos/inthecity.png" alt="InTheCity"></span>
      <span class="logo-badge"><img loading="lazy" class="logo-inv" src="/assets/img/logos/speem.webp" alt="Speem"></span>
      <span class="logo-badge"><img loading="lazy" src="/assets/img/logos/studioapp.png" alt="StudioApp"></span>
      <span class="logo-badge"><img loading="lazy" src="/assets/img/logos/energymonitor.png" alt="EnergyMonitor.tech"></span>
            <span class="logo-badge"><img loading="lazy" class="logo-inv" src="/assets/img/logos/mikramt.png" alt="Mikramt.sk"></span>
      <span class="logo-badge"><img loading="lazy" src="/assets/img/logos/inthecity.png" alt="InTheCity"></span>
      <span class="logo-badge"><img loading="lazy" class="logo-inv" src="/assets/img/logos/speem.webp" alt="Speem"></span>
      <span class="logo-badge"><img loading="lazy" src="/assets/img/logos/studioapp.png" alt="StudioApp"></span>
      <span class="logo-badge"><img loading="lazy" src="/assets/img/logos/energymonitor.png" alt="EnergyMonitor.tech"></span>
    </div>
  </div>
</section>
"""

# Tri piliere viditeľnosti + podporné služby + partnerské doplnky.
PILLARS = [
    ("/sk/sluzby/seo-pre-ai-vyhladavace/", "AI viditeľnosť",
     "ChatGPT, Gemini a Google AI Overviews vás odporúčajú zákazníkom ako prvú voľbu.", "ai", "#34A853"),
    ("/sk/sluzby/seo-optimalizacia/", "Google viditeľnosť",
     "Pozície v Google, ktoré prinášajú zákazníkov, nielen návštevnosť.", "search", "#1A73E8"),
    ("/sk/sluzby/lodalne-seo/", "Google Mapy viditeľnosť",
     "Firemný profil, Mapy a hodnotenia. Zákazníci z okolia vás nájdu ako prví.", "pin", "#EA4335"),
]
SUPPORT_SERVICES = [
    ("/sk/sluzby/seo-pre-eshopy/", "SEO pre e-shopy",
     "Viac predaja z kategórií a produktov. Shoptet, Marketplace, Google Shopping.", "shop", "#FBBC04"),
    ("/sk/sluzby/seo-audit/", "SEO audit a analýza",
     "Presný obraz toho, čo váš web brzdí, s plánom podľa priorít.", "audit", "#1A73E8"),
    ("/sk/sluzby/linkbuilding/", "Linkbuilding",
     "Spätné odkazy a autorita, bez ktorých sa hore nedostanete.", "link", "#EA4335"),
]
PARTNERS = [
    ("https://flamia.studio", "flamia.png", "Web dizajn: Flamia Studio",
     "Web na mieru, ktorý sa nájde a predáva. Dizajn a vývoj rieši náš partner Flamia Studio."),
    ("https://peterkocur.sk", "peterkocur.png", "PPC reklama: Peter Kocur",
     "Google Ads pre výsledky hneď, kým SEO naberá tempo. Vedie ho môj partner Peter Kocur."),
]


def _svc_card(href, title, text, icon, color, tag, delay, external=False):
    ext = ' target="_blank" rel="noopener noreferrer"' if external else ""
    return f"""
<div class="benefit-card card-hover reveal" data-delay="{delay}">
  <span class="benefit-icon">{gicon(icon, color, 26)}</span>
  <h3><a href="{href}"{ext} style="color:var(--text);">{title}</a></h3>
  <p>{text}</p>
  <div class="project-tags"><span class="project-tag {tag}">{'Partner' if external else 'Služba'}</span></div>
</div>"""


def services_grid(cols: int = 3) -> str:
    """Piliere + podporné služby + partneri v jednej sekcii."""
    pillars = "".join(_svc_card(*s, "tag-green" if s[3] == "ai" else "tag-blue" if s[3] == "search" else "tag-red", (i + 1) * 100)
                      for i, s in enumerate(PILLARS))
    support = "".join(_svc_card(*s, ["tag-yellow", "tag-blue", "tag-red", "tag-green"][i], (i + 1) * 100)
                      for i, s in enumerate(SUPPORT_SERVICES))
    partners = "".join(partner_logo_card(href, logo, title, text, (i + 1) * 100)
                       for i, (href, logo, title, text) in enumerate(PARTNERS))
    return (f'<div class="grid-3">{pillars}</div>'
            f'<h3 class="svc-subhead" style="margin:42px 0 22px;">K tomu aj podporné služby</h3>'
            f'<div class="grid-4">{support}</div>'
            f'<h3 class="svc-subhead" style="margin:42px 0 22px;">Doplnkové služby od partnerov</h3>'
            f'<p style="max-width:720px; margin:0 0 20px; color:var(--text-muted);">Tvorbu webu a PPC reklamu neriešim sám. Ponúkam ju v tandeme s overenými partnermi, s ktorými pracujem na jednom projekte.</p>'
            f'<div class="partner-band">{partners}</div>')


def svc_page_faq(common_qa: list[tuple[str, str]]) -> list[tuple[str, str]]:
    return common_qa


PROCESS_STEPS = [
    {"title": "Bezplatný audit", "text": "Začneme 30-minútovým hovorom a bezplatným auditom vášho webu. Vidíte presne, čo brzdí pozície, predaj a AI odporúčania."},
    {"title": "Plán podľa priorít", "text": "Z auditu spravím jasný plán: čo opraviť ako prvé, ktoré kľúčové slová prinášajú zákazníkov a koľko hodín mesačne to zaberie."},
    {"title": "Práca v týždenných dávkach", "text": "Robím: technika, obsah, Google profil, AI viditeľnosť, odkazy. Vždy viete, čo sa stalo v predchádzajúcom týždni."},
    {"title": "Meranie a report", "text": "Mesačný report vám dám osobne: 30-minútový telefónát so mnou. Pozície, kliky z Google, objednávky, zmienky v AI. Platíte len za odpracované hodiny."},
]


def process_section(label: str = "Ako pracujem") -> str:
    return f"""
<section class="section section-alt" id="proces">
  <div class="container">
    <div class="section-head">
      <span class="section-label">{label}</span>
      <h2>Štyri kroky. Žiadne pevné zmluvy.</h2>
      <p class="section-subheading">Viete vždy, čo robím, prečo a čo to prinieslo. Každá hodina je vykazovaná.</p>
    </div>
    {steps_block(PROCESS_STEPS)}
  </div>
</section>
"""


# ---------------------------------------------------------------- HOME

def home() -> tuple[str, str]:
    h1 = ('Nech vás zákazníci nájdú v <span class="hl-blue">Google</span>, '
          'na <span class="hl-red">Google Mapách</span> aj v <span class="hl-green">ChatGPT</span>.')
    sub = ("Volám sa Šimon Štermenský a SEO robím pre podnikateľov bez platenej reklamy: "
           "pracujem na obsahu webu, technickej stránke webu a profile na Google Mapách, "
           "aby vás zákazníci našli, keď hľadajú vaše produkty a služby. Za transparentných "
           "12 EUR za hodinu. Bez paušálov, bez pevných zmlúv, s reportom, ktorému rozumiete.")

    body = f"""
<!-- HERO -->
<section class="hero">
  <div class="container">
    <div class="hero-flex">
      <div class="hero-content">
        <span class="hero-label">SEO bez platenej reklamy · SK a CZ</span>
        <h1>{h1}</h1>
        <p class="hero-sub">{sub}</p>
        <div class="hero-ctas">
          <a href="tel:+421917316105" class="btn btn-primary btn-lg">Zavolajte +421 917 316 105</a>
          <a href="/sk/kontakt/" class="btn btn-outline btn-lg">Chcem bezplatný audit webu</a>
        </div>
        <p class="hero-scarcity">Alebo napíšte: <a href="/sk/kontakt/" style="font-weight:700; color:var(--text); text-decoration:none;">kontaktný formulár</a> · <a href="mailto:hello@noktostudio.com" style="font-weight:700; color:var(--text); text-decoration:none;">hello@noktostudio.com</a></p>
        <p class="hero-scarcity" style="margin-top:6px;">Kapacita na nové projekty: otvorené od októbra 2026.</p>
      </div>
      <div class="hero-photo">
        <img src="/assets/img/simon.png" alt="Šimon Štermenský, SEO špecialista a majiteľ Nokto Studio" width="220" height="220" loading="eager">
        <span class="hero-photo-cap">Šimon Štermenský<br>SEO špecialista · Nokto Studio</span>
      </div>
    </div>
  </div>
</section>

{TRUST_STATS}
{LOGOS}

{results_slider("sk")}

<!-- PRE KOHO -->
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Pre koho to robím</span>
      <h2>Štyri veci, ktoré podnikatelia chcú odo mňa</h2>
      <p class="section-subheading">Každý klient si vyberá jeden alebo viac cieľov. Stavím systém, ktorý ich obsluhuje spolu.</p>
    </div>
    <div class="grid-4">
      <div class="benefit-card card-hover reveal" data-delay="100">
        <span class="benefit-icon icon-green">{gicon("ai", "#34A853", 26)}</span>
        <h3>Nech ma AI odporúča</h3>
        <p>Keď zákazník pýta ChatGPT alebo Gemini odporúčanie, chcete byť v odpovedi. Stavím web tak, aby mu AI nástroje rozumeli a citovali ho.</p>
      </div>
      <div class="benefit-card card-hover reveal" data-delay="200">
        <span class="benefit-icon icon-red">{gicon("pin", "#EA4335", 26)}</span>
        <h3>Zákazníci z Google a Mápy</h3>
        <p>Lokálne hľadanie a Google firemný profil sú najrýchlejšia cesta k zákazníkom z okolia. Nastavím ich a vyhodnocujem každý týždeň.</p>
      </div>
      <div class="benefit-card card-hover reveal" data-delay="300">
        <span class="benefit-icon icon-yellow">{gicon("shop", "#FBBC04", 26)}</span>
        <h3>Viac predaja na e-shope</h3>
        <p>Kategórie a produkty optimalizujem na kľúčové slová, ktoré kupujú. Google Shopping a Heureka sledujem ako súčasť systému.</p>
      </div>
      <div class="benefit-card card-hover reveal" data-delay="400">
        <span class="benefit-icon icon-blue">{gicon("grow", "#1A73E8", 26)}</span>
        <h3>Viac ponúk pre služby</h3>
        <p>Služby predávam cez obsahové stránky, ktoré odpovedajú na otázky zákazníkov. Z väčšieho záujmu vyrobíte viac ponúk a zákaziek.</p>
      </div>
    </div>
  </div>
</section>

<!-- SLUZBY -->
<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Služby</span>
      <h2>Tri piliere viditeľnosti, v ktorých som najlepší</h2>
      <p class="section-subheading">AI viditeľnosť, Google viditeľnosť a viditeľnosť v Google Mapách. K tomu podporné služby a doplnky od overených partnerov.</p>
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
      <p class="section-subheading">Žiadne mesačné paušály, pri ktorých neviete, čo obsahujú. Každá hodina je vykazovaná v reporte.</p>
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
          <p>Vlastný e-shop s API integráciou na účtovný systém Sunsoft Ecosun pre regionálneho dodávateľa stolárskych potrieb. Za 9 mesiacov som vygeneroval online tržby pripísané do kanálov email a organický Google. Súčasťou je email marketing, lokálne SEO a optimalizácia pre AI vyhľadávače, tak, aby značku odporúčali ChatGPT aj Google AI Overviews.</p>
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
          <a href="/sk/kontakt/" class="btn btn-outline" style="margin-top:20px;">Povedať si viac</a>
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
      <a href="/sk/vysledky/" class="btn btn-outline">Všetky výsledky</a>
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

<!-- KTO ZA TYM STOJI -->
<section class="section section-alt" id="o-mne">
  <div class="container">
    <div class="about-simon">
      <div class="about-simon-photo reveal">
        <img src="/assets/img/simon.png" alt="Šimon Štermenský, SEO špecialista a majiteľ Nokto Studio" width="300" height="300" loading="lazy">
      </div>
      <div class="reveal" data-delay="150">
        <span class="section-label">Kto za Nokto stojí</span>
        <h2 style="margin:10px 0 14px;">S vami komunikujem ja, nie account manager.</h2>
        <p style="color:var(--text-muted);">Som Šimon, SEO špecialista. Rokmi praxe v online marketingu som si najviac obľúbil SEO a viditeľnosť v Google aj AI nástrojoch, lebo vidím, ako reálne mení predaj malých firiem. Pracujem s malým tímom a s partnermi na web dizajne a PPC reklame, takže vám vždy odpovie ten, kto prácu robí.</p>
        <p style="color:var(--text-muted);">Prvá hodina s vami je bezplatný hovor a audit. Ak vám čísla nebudú dávať zmysel, nič neplatíte.</p>
        <a href="/sk/kontakt/" class="btn btn-primary" style="margin-top:18px;">Dohodnúť si hovor so mnou</a>
      </div>
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
        desc="SEO agentúra pre podnikateľov. Zákazníci z Google a Google Mapy, odporúčania v ChatGPT a AI nástrojoch, viac predaja na e-shope. 12 EUR za hodinu, bezplatný audit.",
        canonical=BASE + "/", body=body, prefix="",
        extra_head=ORG_SCHEMA + faq_schema_html,
    )
    return ("index.html", html)


HOME_FAQ = [
    ("Koľko stojí SEO optimalizácia webu?",
     "Za prácu platíte 12 EUR za hodinu. Malý web zvládnem v 10 hodinách mesačne (120 EUR), väčší e-shop v 40 hodinách (480 EUR). Presný rozsah vám potvrdím v pláne po bezplatnom audite."),
    ("Ako dlho trvá, kým SEO prinesie výsledky?",
     "Prvé pohyby vidíte na menej konkurenčných kľúčových slovách zvyčajne za 2 až 4 mesiace. Na hlavné dotazy v konkurenčných odvetviach trvá 6 až 12 mesiacov. Reálne termíny vám poviem už v audite."),
    ("Budem vidieť, za čo platím?",
     "Áno. Mesačný report vám dám osobne: 30-minútový hovor, v ktorom prejdeme odpracované hodiny a ich výsledky: pozície, kliky z Google, objednávky a zmienky v AI. Bez reportovania sa nepohne žiadna práca."),
    ("Pomôžete mi, aby ma ChatGPT odporúčal?",
     "Áno, to je moja špecializácia. Optimalizujem web pre AI nástroje (ChatGPT, Gemini, AI Overviews) tak, aby vás odporúčali pri dotazoch vašich zákazníkov."),
    ("Sú zmluvy viažúce na 12 mesiacov?",
     "Nie. Pracujem mesačne, spoluprácu môžete skončiť kedykoľvek. Dôveru stavím na výsledkoch, nie na viazanosti."),
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
        desc="SEO optimalizácia webu, lokálne SEO a Google firemný profil, SEO pre AI vyhľadávače, e-shop SEO, audit, linkbuilding a email marketing. 12 EUR za hodinu.",
        canonical=BASE + "/sk/sluzby/", body=body, prefix="../..", extra_head=ORG_SCHEMA,
    )
    return ("sk/sluzby/index.html", html)


# ---------------------------------------------------------------- SERVICE PAGES

def _service_page(*, path: str, title: str, desc: str, label: str, h1: str,
                  intro: str, for_who: list[str], deliverables: list[str],
                  faq: list[tuple[str, str]], slug: str, svc_name: str,
                  proof: dict | None = None) -> tuple[str, str]:
    url = BASE + f"/sk/sluzby/{slug}/"
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
      <span class="section-label">Výsledok z praxe</span>
      <h2>{proof['title']}</h2>
    </div>
    <div class="case-result proof-band">{nums}</div>
    <p style="margin-top:16px; max-width:720px; color:var(--text-2);">{proof['caption']}</p>
    <p style="margin-top:4px; font-size:0.8rem; color:var(--text-muted);">{proof['source']}</p>
  </div>
</section>"""
    body = f"""
{page_hero(label, h1, intro, [("Domov", "/"), ("Služby", "/sk/sluzby/"), (label.replace("Služba · ", ""), None)])}

<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:start;">
      <div class="prose">
        <h2>Pre koho je táto služba?</h2>
        <ul>{who}</ul>
      </div>
      <div class="card">
        <span class="section-label">Čo dodávam</span>
        <ul class="deliv-list">{deliv}</ul>
      </div>
    </div>
  </div>
</section>

{proof_html}

{process_section("Ako pobeží spolupráca")}

<section class="section section-alt">
  <div class="container">
    <div class="rate-band">
      <div>
        <div class="rate-big">12 EUR <small>za hodinu · kedykoľvek skončíte</small></div>
        <p style="margin-top:8px; max-width:520px;">Táto služba zvyčajne potrebuje 8 až 20 hodín mesačne, podľa rozsahu webu a konkurencie.</p>
      </div>
      <div class="hero-ctas">
        <a href="/sk/kontakt/" class="btn btn-primary btn-lg">Bezplatný hovor</a>
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
        title="SEO optimalizácia webu a webstránok | Nokto Studio",
        desc="SEO optimalizácia webstránok: technika, obsah, kľúčové slová. Pozície v Google, ktoré privedú zákazníkov. 12 EUR za hodinu, bezplatný audit.",
        label="Služba · SEO optimalizácia",
        h1="SEO optimalizácia, ktorá privedie zákazníkov",
        intro="Zákazník, ktorý vás hľadá v Google, je najlacnejší zákazník. Postavím web tak, aby mu Google rozumel a zaradil ho hore a návštevníci odchádzali s odpoveďou, nie s otáznikom.",
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
            "Mesačný report: 30-minútový hovor so mnou, pozície, kliky z Search Console, objednávky.",
        ],
        faq=[
            ("Koľko hodín mesačne zaberie SEO optimalizácia?",
             "Firemný web zvládnem v 10 hodinách mesačne (120 EUR), e-shop v 20 až 40 hodinách (240 až 480 EUR). Rozsah potvrdím v pláne po audite."),
            ("Za aký čas sa objavia prvé výsledky?",
             "Prvé pohyby na menej konkurenčných dotazoch za 2 až 4 mesiace, na hlavné dotazy 6 až 12 mesiacov. Záleží na konkurencii a stave webu."),
            ("Robíte aj obsah? Nemám čas písať.",
             "Áno, písanie obsahu je súčasť hodín. Sám navrhnem štruktúru, vypíšem texty a pred publikovaním ich schválite."),
            ("Čo ak som už SEO robil a nič to neprinieslo?",
             "Bezplatný audit presne povie, čo predchádzajúca práca nechala nedokončené. Často chýbajú dva či tri kroky, nie celé SEO."),
        ],
        svc_name="SEO optimalizácia webu",
        proof={
            "title": "Kliky z Google: +355 % za 3 mesiace spolupráce",
            "numbers": [("250", "klikov za 3 mesiace", "#1A73E8"),
                        ("+355 %", "rast oproti predchádzajúcemu obdobiu", "#EA4335"),
                        ("8 950", "zobrazení mesačne (+246 %)", "#F9AB00")],
            "caption": "Firemný web, ktorý som prevzal s minimálnou organickou návštevnosťou. Práca: technická oprava, obsahové stránky na reálne dopyty zákazníkov a mesačné vyhodnotenie. Rast prišiel každý mesiac, bez jednorazového skoku.",
            "source": "Zdroj: Google Search Console klienta, ukážka zo septembra 2026.",
        },
    )


def lodalne_seo() -> tuple[str, str]:
    return _service_page(
        path="sluzby/lodalne-seo/", slug="lodalne-seo",
        title="Lokálne SEO a firemný profil Google Mapy | Nokto Studio",
        desc="Lokálne SEO: Google firemný profil, Google Mapy, hodnotenia a lokálne kľúčové slová. Zákazníci z okolia vás nájdu prví. 12 EUR za hodinu.",
        label="Služba · Lokálne SEO",
        h1="Lokálne SEO: zákazníci z okolia vás nájdu prví",
        intro="Keď si niekto vyhľadá zubára, autoservis alebo kuchyne vo svojom meste, rozhodnú tri veci: Google Mapy, hodnotenia a web. Nastavím všetky tri a držím ich v poriadku.",
        for_who=[
            "Prevádzkujete firmu s pôsobiskom: služby, reštaurácia, ordinácia, workshop.",
            "Na Google Mapách ste chýbali, máte chýbajúce dáta alebo žiadne hodnotenia.",
            "Konkurencia je v mape hore, hoci má horšiu ponuku.",
            "Chcete telefón a kontakty z okolia, nie z celého Slovenska.",
        ],
        deliverables=[
            "Kompletné nastavenie a čistenie Google firemného profilu (My Business).",
            "Kategórie, služby, otváracie časy, fotky a Q&A, ktoré Google ocení.",
            "Stratégia na získavanie hodnotení a odpovede na ne.",
            "Lokálne kľúčové slová: mesto + služba, okres + služba.",
            "Lokálne citácie v adresároch a odvetvových weboch (firmy.sk a podobné).",
            "Týždenný prehľad: volania, žiadosti o trasu, zobrazenia v mape.",
        ],
        faq=[
            ("Koľko trvá, kým Google profil začne fungovať?",
             "Prvé zlepšenia v mape viditeľné za 4 až 8 týždňov, stabilná pozícia trvá 3 až 6 mesiacov. Záleží na konkurencii v okolí."),
            ("Mám len jedno pôsobisko. Oplatí sa mi to?",
             "Práve pre jedno pôsobisko je lokálne SEO najúčinnejšie. Sústredíte všetku silu do vášho mesta a okresu, kde je konkurencia najmenšia."),
            ("Ako získam viac hodnotení na Google?",
             "Mám jednoduchý postup cez SMS a QR kód, ktorý zákazníkov vyzýva hneď po vykonaní služby. Zvyšuje mieru recenzií niekoľkonásobne."),
            ("Ako riešite zlé hodnotenia?",
             "Odpovedám profesionálne a na mieste. Zlé hodnotenia nemožno odstrániť, ale dobrý pomer a kultivované odpovede pôsobia na zákazníkov viac ako počty hviezd."),
        ],
        svc_name="Lokálne SEO a Google firemný profil",
        proof={
            "title": "359 ľudí videlo firemný profil klienta za jedno obdobie",
            "numbers": [("359", "zobrazení firemného profilu", "#1A73E8"),
                        ("54 %", "zobrazení cez Google Mapy", "#EA4335"),
                        ("46 %", "zobrazení cez Google Search", "#34A853")],
            "caption": "Lokálny zákazník hľadá dvomi cestami: cez Mapy (54 % zobrazení) a cez bežné Google hľadanie (46 %). Preto drvíme obe: profil nastavený na doraz, hodnotenia prichádzajú pravidelne a web podporuje mapové pozície.",
            "source": "Zdroj: štatistiky Google firemného profilu klienta, ukážka zo septembra 2026.",
        },
    )


def seo_ai() -> tuple[str, str]:
    return _service_page(
        path="sluzby/seo-pre-ai-vyhladavace/", slug="seo-pre-ai-vyhladavace",
        title="SEO pre AI vyhľadávače: ChatGPT a AI Overviews | Nokto Studio",
        desc="Optimalizácia pre AI vyhľadávače a AI Overviews. ChatGPT a Gemini vás odporúčajú zákazníkom. Prvá agentúra na Slovensku s touto špecializáciou.",
        label="Služba · SEO pre AI",
        h1="Aby vás ChatGPT odporúčal zákazníkom",
        intro="Zákazník dnes nepýta len Google. Pýta ChatGPT: \u201eOdporúč mi dobrého zubára v Nitre.\u201c AI nástroj odpovie dvomi až piatimi menami. Mojou úlohou je, aby vaše meno tam bolo.",
        for_who=[
            "Chcete, aby vás AI nástroje odporúčali ako prvú voľbu vo vašom odvetví.",
            "Vidíte, že zákazníci prichádzajú s vetou \u201enašiel ChatGPT, že...\u201c",
            "Konkurencia sa na AI odporúčania zatiaľ nepripravuje (to je výhoda).",
            "Máte expertízu a chcete ju viditeľnú aj pre AI, nie len pre Google.",
        ],
        deliverables=[
            "Audit AI viditeľnosti: ako vás dnes ChatGPT, Gemini a AI Overviews citujú a kde chýbate.",
            "Priame odpovede na stránkach: úvodné odseky vo formáte, ktorý AI čerpá.",
            "Štruktúrované dáta (schema.org) pre ľahké čítanie AI nástrojmi.",
            "Obsahové stránky odpovedajúce na reálne otázky zákazníkov (People Also Ask, AI dotazy).",
            "Mesačné sledovanie: v ktorých AI odpovediach sa objavujete a čo sa zmenilo.",
            "Prevádzka rozšírení pre AI roboty (llms.txt, robots.txt, prístup pre GPTBot a PerplexityBot).",
        ],
        faq=[
            ("Je toto SEO alebo marketing?",
             "Je to priame pokračovanie SEO. Google aj ChatGPT čerpajú z webu, rozdiel je v tom, čo a ako čítajú. Nastavím oboje naraz."),
            ("Ako meriate, či ma AI odporúča?",
             "Pravidelne testujem sadu dotazov, ktoré vaši zákazníci pýtajú, a zaznamenávam, či sa vaše meno v odpovediach objavuje. Výsledky máte v reporte."),
            ("To môže trvať dlho?",
             "Víťazstvo v AI odporúčaniach je zvyčajne rýchlejšie než klasické SEO pozície, pretože konkurencia tu len začína. Prvé menovanie vidím často do 2 až 3 mesiacov."),
            ("Pre koho to má zmysel?",
             "Pre služby, kde zákazník hľadá odporúčanie: zdravotníctvo, právo, servis, stavebníctvo, školenia. Pre e-shopy pomáha v dotazoch typu \u201ekto predáva...\" a v recenziách."),
        ],
        svc_name="Optimalizácia pre AI vyhľadávače",
        proof={
            "title": "13 AI citácií e-shopu v Google AI Mode za 3 mesiace",
            "numbers": [("13", "AI citácií webu v Google AI Mode", "#34A853"),
                        ("8", "citácií jednej stránky /overaly/", "#1A73E8"),
                        ("3", "citácií blogového článku", "#F9AB00")],
            "caption": "Po nasadení nášho obsahu cituje Google AI Mode konkrétne stránky e-shopu priamo v odpovediach zákazníkom. Najviac citovaná stránka prišla na 8 citácií, blogový článok na 3. Konkurencia v AI odpovediach na tieto dotazy ešte nie je, takže prvé mená tam ostávajú.",
            "source": "Zdroj: Google AI Mode (report citácií), ukážka z augusta 2026.",
        },
    )


def eshop_seo() -> tuple[str, str]:
    return _service_page(
        path="sluzby/seo-pre-eshopy/", slug="seo-pre-eshopy",
        title="SEO pre e-shopy: Shoptet a Google Shopping | Nokto Studio",
        desc="SEO optimalizácia e-shopu: kategórie, produkty, Shoptet, Marketplace aj Google Shopping. Viac predaja z organického vyhľadávania. 12 EUR za hodinu.",
        label="Služba · SEO pre e-shopy",
        h1="E-shop SEO: viac objednávok z Google",
        intro="E-shop má jediné reálne meradlo úspechu: objednávky. Optimalizujem kategórie a produkty na dotazy, ktoré kupujú, aby vás Google aj Marketplace našli bez nutnosti platiť za každý klik.",
        for_who=[
            "Máte e-shop (Shoptet, WooCommerce, vlastné riešenie) a predaj závisí od reklamy.",
            "Kategórie nemajú vlastné texty a nepredávajú sa samy.",
            "Ste viditeľní len na názvoch produktov, nie na tom, čo zákazník reálne hľadá.",
            "Chcete znížiť náklady na reklamu tým, že časť dopytov chytíte zdarma.",
        ],
        deliverables=[
            "Analýza kľúčových slov pre kategórie a hlavné produkty.",
            "Texty kategórií a produktov, ktoré predávajú a nielen opisujú.",
            "Technická hygiena: kanonizácie, filtrované URL, rýchlosť, produktové dáta.",
            "Google Merchant Center a Google Shopping v poriadku.",
            "Poradenstvo pre Heureka a Marketplace integrácie.",
            "Report v objednávkach a tržbe z organického kanála.",
        ],
        faq=[
            ("Robíte SEO aj pre Shoptet?",
             "Áno, Shoptet je na Slovensku najbežnejšia platforma a poznáme jej špecifiká (filtre, varianty, SEO moduly)."),
            ("Koľko objednávok z toho bude?",
             "Reálne čísla vám poviem po audite, na základe vašich kľúčových slov a ich dopytu. Nikdy nepoviem číslo, ktoré nedokážem podložiť dátami."),
            ("Musím robiť aj linkbuilding?",
             "Pre konkurenčné kategórie áno, odozva bez autority je pomalá. Odporučím rozsah, ktorý dáva zmysel pre váš rozpočet."),
            ("Ako sa meria úspech?",
             "V Google Analytics a Search Console sledujem objednávky a tržbu z organického vyhľadávania. Report máte mesačne."),
        ],
        svc_name="SEO pre e-shopy",
        proof={
            "title": "E-shop Mikramt.sk: 2 492,75 EUR tržieb za 9 mesiacov",
            "numbers": [("2 492,75 EUR", "tržby za 9 mesiacov", "#1A73E8"),
                        ("15", "objednávok z emailu a organika", "#34A853"),
                        ("722 EUR", "najväčšia objednávka", "#F9AB00")],
            "caption": "Regionálny dodávateľ stolárskych potrieb s e-shopom na vlastnej platforme, API integráciou na účtovný systém a email marketingom. Objednávky chodia z kanálov email a organický Google. Súčasťou je aj lokálne SEO a optimalizácia pre AI vyhľadávače.",
            "source": "Zdroj: objednávky pripísané do kanálov email a organický Google, 9 mesiacov spolupráce.",
        },
    )


def audit_seo() -> tuple[str, str]:
    return _service_page(
        path="sluzby/seo-audit/", slug="seo-audit",
        title="SEO audit webu a analýza kľúčových slov | Nokto Studio",
        desc="SEO audit webu s akčným plánom: technika, obsah, kľúčové slová, konkurencia. Bezplatný vstupný audit, detailný od 12 EUR za hodinu.",
        label="Služba · SEO audit",
        h1="SEO audit: presný obraz toho, čo váš web brzdí",
        intro="Audit nie je PDF na polici. Je to zoznam úloh s prioritami a odhadom hodín. Začína sa bezplatným vstupným auditom, ktorý máte do troch dní.",
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
             "Áno. Plán je v zrozumiteľnom formáte s úlohami po jednotlivých krokoch, priamo pre používateľa v CMS alebo vývojára."),
            ("Musím potom brať aj ďalšie služby?",
             "Nie. Plán si môžete vykonať sami alebo s iným partnerom. Ak sa rozhodnete pracovať s nami, plán slúži ako základ spolupráce."),
            ("Ako rýchlo dostanem audit?",
             "Vstupný audit do 3 pracovných dní od prvého hovoru. Detailný audit za 7 až 10 dní."),
        ],
        svc_name="SEO audit a analýza kľúčových slov",
        proof={
            "title": "Len 6 nových stránok zdvihlo celý web o 11 000 zobrazení",
            "numbers": [("11 000", "zobrazení mesačne (+14 %)", "#F9AB00"),
                        ("+43 %", "klikov v poslednom týždni", "#1A73E8"),
                        ("6", "stránok, ktoré to spravili", "#34A853")],
            "caption": "Toto je sila správneho plánu: nezostávať pri 300 stránkach webu, ale pridať 6 presne zacielených obsahových stránok na dopyty, ktoré zákazníci reálne pýtajú. Presne takéto príležitosti audit hľadá ako prvé.",
            "source": "Zdroj: Google Search Console, ukážka zo septembra 2026.",
        },
    )


def linkbuilding() -> tuple[str, str]:
    return _service_page(
        path="sluzby/linkbuilding/", slug="linkbuilding",
        title="Linkbuilding a spätné odkazy | Nokto Studio",
        desc="Linkbuilding: spätné odkazy a autorita webu. Bezpečné metódy, reálne domény, transparentné vykazovanie. 12 EUR za hodinu.",
        label="Služba · Linkbuilding",
        h1="Linkbuilding: autorita, ktorá drží pozície",
        intro="Technika a obsah vás dovedú do stredu výsledkov, autorita vás posunie hore. Staviam odkazy, ktoré Google akceptuje a zákazníci aj citujú.",
        for_who=[
            "Máte technicky v poriadku web a obsah, ale pozície stoja.",
            "Konkurencia má silnejší link profil a predbieha vás.",
            "Chcete odkazy z reálnych slovenských a českých domén, nie zo spamových sietí.",
            "Chcete transparentné vykazovanie, kde odkazy vznikli a čo stoja.",
        ],
        deliverables=[
            "Rozbor link profilu: čo vás brzdí, ktoré odkazy chýbajú.",
            "Tématické a lokálne odkazy: adresáre, brandže, médiá, partneri.",
            "Pripravené obsahy a PR články, ktoré odkazy nesú.",
            "Sledovanie nových odkazov a stratených odkazov.",
            "Jasná cena za odkaz, bez prirážky.",
            "Mesačný prehľad: nové domény, posun pozícií.",
        ],
        faq=[
            ("Koľko stoja odkazy?",
             "Cena odkazu závisí od domény. Väčšina slovenských odkazov stojí 50 až 300 EUR, mediálne PR články viac. Vykazujeme skutočné ceny, žiadna prirážka."),
            ("Ako dlho trvá, kým odkazy pomôžu?",
             "Nové odkazy sa uplatnia v 4 až 12 týždňoch. Preto kombinujeme linkbuilding s obsahovou prácou, ktorá už teraz niečo prináša."),
            ("Robíte aj kupovanie odkazov?",
             "Pracujem len s reálnymi, viditeľnými miestami. Nikdy nepoužívam siete automatizovaných spamov, ktoré skôr alebo neskôr Google sankcionuje."),
            ("Koľko odkazov potrebujem mesačne?",
             "Malý firemný web 2 až 5, e-shop v konkurenčnej bráne 5 až 10. Väčšie čísla nie vždy znamenajú lepší výsledok."),
        ],
        svc_name="Linkbuilding",
        proof={
            "title": "Rast každý mesiac: 250 klikov za 3 mesiace spolupráce",
            "numbers": [("250", "klikov za 3 mesiace (+355 %)", "#1A73E8"),
                        ("8 950", "zobrazení (+246 %)", "#EA4335"),
                        ("5", "mesiacov meraného rastu", "#34A853")],
            "caption": "Odkazy fungujú len v kombinácii s obsahom a technikou. Toto je výsledok celého systému: obsahové stránky na reálne dopyty, interné prelinkovanie a odkazy z reálnych slovenských domén. Posun prichádzal každý mesiac.",
            "source": "Zdroj: Google Search Console klienta, ukážka zo septembra 2026.",
        },
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
     "items": ["Všetko z balíčka Rast", "Texty kategórií a produktov", "Google Merchant Center a Shopping", "Poradenstvo Heureka / Marketplace", "Automatizácie email marketingu", "Report s tržbami z organiky"],
     "cta": "/sk/kontakt/"},
]

CENNIK_FAQ = [
    ("Koľko stojí SEO optimalizácia webu?",
     "Platíte 12 EUR za každú odpracovanú hodinu. Firemný web zvyčajne potrebuje 10 hodín mesačne (120 EUR), e-shop 20 až 40 hodín (240 až 480 EUR). Rozsah si nastavíte sami a môžete ho kedykoľvek meniť."),
    ("Prečo je to lacnejšie než konkurencia?",
     "Nemám kancelárie ani manažérske vrstvy. Veľkú časť práce vykonávajú automatizované nástroje, ktoré som si sám postavil, a odborný čas vkladám tam, kde sa počíta. Úspory prenášam na vás."),
    ("Čo je v cene zahrnuté?",
     "Všetko okrem reklamných výdavkov a nákladov na odkazy či nástroje tretích strán. Tie vám vykazujem v skutočnej cene, bez prirážky."),
    ("Musím platiť mesačne vopred?",
     "Fakturujem mesačne dozadu za skutočne odpracované hodiny, s faktúrou. Paušál nie je potrebný."),
    ("Môžem spoluprácu kedykoľvek skončiť?",
     "Áno, kedykoľvek mesačný cyklus skončíte, bez sankcií a bez viazanosti. Dôveru si zaslúžime výsledkami."),
    ("Ako viem, že práca bola odvedená?",
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
      <a href="/sk/kontakt/" class="btn btn-primary btn-lg">Nezáväzná ponuka</a>
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
          <li><span class="check">✓</span><span>Komunikácia: mesačný 30-minútový hovor so mnou, neobmedzené otázky medzitým.</span></li>
        </ul>
        <h2>Čo nie je v cene</h2>
        <ul class="deliv-list">
          <li><span class="check" style="background:#FCE8E6;color:var(--g-red-deep);">×</span><span>Reklamné výdavky (Google Ads, Meta Ads). Platíte priamo Googlu, nie mne.</span></li>
          <li><span class="check" style="background:#FCE8E6;color:var(--g-red-deep);">×</span><span>Náklady na odkazy a PR články. Vykazujeme skutočnú cenu od médií.</span></li>
          <li><span class="check" style="background:#FCE8E6;color:var(--g-red-deep);">×</span><span>Nájom platených nástrojov tretích strán, ak je potrebný (napr. platobná brána, hosting).</span></li>
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
        <p style="margin-top:14px; font-size:0.9rem; color:var(--text-muted);">Reálne čísla pre váš web potvrdím v bezplatnom audite.</p>
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
