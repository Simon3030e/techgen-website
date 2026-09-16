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
        <span class="trust-num tn-violet">12&nbsp;EUR</span>
        <span class="trust-label">transparentná hodinová<br>sadzba, bez paušálov</span>
      </div>
      <div class="trust-stat reveal" data-delay="200">
        <span class="trust-num tn-orange">0 EUR</span>
        <span class="trust-label">prvý hovor a audit<br>webu sú bezplatné</span>
      </div>
      <div class="trust-stat reveal" data-delay="300">
        <span class="trust-num tn-cerulean">1. deň</span>
        <span class="trust-label">bezplatný audit<br>začne hneď po prvom hovore</span>
      </div>
      <div class="trust-stat reveal" data-delay="400">
        <span class="trust-num tn-violet-light">30 min</span>
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
      <span class="logo-badge"><img loading="lazy" src="/assets/img/logos/servisprofi.png" alt="ServisProfi.sk"></span>
      <span class="logo-badge"><img loading="lazy" src="/assets/img/logos/solarprofi.png" alt="SolarProfi.sk"></span>
      <span class="logo-badge"><img loading="lazy" src="/assets/img/logos/servisprofi.png" alt="ServisProfi.sk"></span>
      <span class="logo-badge"><img loading="lazy" src="/assets/img/logos/solarprofi.png" alt="SolarProfi.sk"></span>
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
     "ChatGPT, Gemini a Google AI Overviews vás odporúčajú zákazníkom ako prvú voľbu.", "ai", "#9B6FD9"),
    ("/sk/sluzby/seo-optimalizacia/", "Google viditeľnosť",
     "Pozície v Google, ktoré prinášajú zákazníkov, nielen návštevnosť.", "search", "#6A3FC4"),
    ("/sk/sluzby/lodalne-seo/", "Google Mapy viditeľnosť",
     "Firemný profil, Mapy a hodnotenia. Zákazníci z okolia vás nájdu ako prví.", "pin", "#F75940"),
]
SUPPORT_SERVICES = [
    ("/sk/sluzby/seo-pre-eshopy/", "SEO pre e-shopy",
     "Viac predaja z kategórií a produktov (Shoptet, Marketplace, Google Shopping).", "shop", "#1DACD6"),
    ("/sk/sluzby/seo-audit/", "SEO audit a analýza",
     "Presný obraz toho, čo váš web brzdí, s plánom podľa priorít.", "audit", "#6A3FC4"),
    ("/sk/sluzby/linkbuilding/", "Linkbuilding",
     "Spätné odkazy a autorita, bez ktorých sa nedostanete hore.", "link", "#F75940"),
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
    pillars = "".join(_svc_card(*s, "tag-violet-light" if s[3] == "ai" else "tag-violet" if s[3] == "search" else "tag-orange", (i + 1) * 100)
                      for i, s in enumerate(PILLARS))
    support = "".join(_svc_card(*s, ["tag-cerulean", "tag-violet", "tag-orange", "tag-violet-light"][i], (i + 1) * 100)
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
    {"title": "Bezplatný audit", "text": "Začneme 30-minútovým hovorom a bezplatným auditom vášho webu. Uvidíte presne, čo brzdí pozície, predaj a AI odporúčania."},
    {"title": "Plán podľa priorít", "text": "Z auditu spravím jasný plán: čo opraviť ako prvé, ktoré kľúčové slová prinášajú zákazníkov a koľko hodín mesačne to zaberie."},
    {"title": "Práca v týždenných dávkach", "text": "Robím: technika, obsah, Google profil, AI viditeľnosť, odkazy. Vždy viete, čo sa stalo v predchádzajúcom týždni."},
    {"title": "Meranie a report", "text": "Mesačný report vám dám osobne: 30-minútový telefonát so mnou. Pozície, kliky z Google, objednávky, zmienky v AI. Platíte len za odpracované hodiny."},
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
    h1 = ('Nech vás zákazníci nájdú v <span class="hl-violet">Google</span>, '
          'na <span class="hl-orange">Google Mapách</span> aj v <span class="hl-cerulean-light">ChatGPT</span>.')
    sub = ("Volám sa Šimon Štermenský a SEO robím pre podnikateľov bez platenej reklamy: "
           "pomáham klientom rásť v Google a AI vyhľadávaní písaním obsahu a opravami "
           "technických vecí na webe, tak aby vás zákazníci našli, keď hľadajú vaše "
           "produkty a služby. Za transparentných 12 EUR za hodinu. Bez paušálov, "
           "bez pevných zmlúv, s reportom, ktorému rozumiete.")

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
      <p class="section-subheading">Každý klient si vyberá jeden alebo viac cieľov. Nastavím systém, ktorý ich obsluhuje spolu.</p>
    </div>
    <div class="grid-4">
      <div class="benefit-card card-hover reveal" data-delay="100">
        <span class="benefit-icon icon-violet-light">{gicon("ai", "#9B6FD9", 26)}</span>
        <h3>Nech ma AI odporúča</h3>
        <p>Keď zákazník pýta ChatGPT alebo Gemini odporúčanie, chcete byť v odpovedi. Nastavím web tak, aby mu AI nástroje rozumeli a citovali ho.</p>
      </div>
      <div class="benefit-card card-hover reveal" data-delay="200">
        <span class="benefit-icon icon-orange">{gicon("pin", "#F75940", 26)}</span>
        <h3>Zákazníci z Google a Mápy</h3>
        <p>Lokálne hľadanie a Google firemný profil sú najrýchlejšia cesta k zákazníkom z okolia. Nastavím ich a vyhodnocujem každý týždeň.</p>
      </div>
      <div class="benefit-card card-hover reveal" data-delay="300">
        <span class="benefit-icon icon-cerulean">{gicon("shop", "#1DACD6", 26)}</span>
        <h3>Viac predaja na e-shope</h3>
        <p>Kategórie a produkty optimalizujem na kľúčové slová, ktoré kupujú. Google Shopping a Heureka sledujem ako súčasť systému.</p>
      </div>
      <div class="benefit-card card-hover reveal" data-delay="400">
        <span class="benefit-icon icon-violet">{gicon("grow", "#6A3FC4", 26)}</span>
        <h3>Viac ponúk služieb</h3>
        <p>Služby predávam cez obsahové stránky, ktoré odpovedajú na otázky zákazníkov. Z väčšieho záujmu získate viac ponúk a zákaziek.</p>
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
      <p class="section-subheading">Žiadne mesačné paušály, pri ktorých neviete, čo obsahujú. Každá hodina je vykázaná v reporte.</p>
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
          <h3>E-shop so školskými pomôckami (klient)</h3>
          <p>Vlastný e-shop s API integráciou na účtovný systém pre regionálneho dodávateľa. Za 9 mesiacov som vygeneroval online tržby pripísané kanálom e-mail a organické vyhľadávanie Google. Súčasťou je e-mail marketing, lokálne SEO a optimalizácia pre AI vyhľadávače, tak, aby značku odporúčali ChatGPT aj Google AI Overviews.</p>
          <div class="case-result">
            <div><strong>2 492,75 EUR</strong><span>tržby za 9 mesiacov</span></div>
            <div><strong>15</strong><span>objednávok z e-mailu a organického vyhľadávania</span></div>
            <div><strong>722 EUR</strong><span>najväčšia objednávka</span></div>
          </div>
          <div class="project-tags">
            <span class="project-tag tag-cerulean">E-shop SEO</span>
            <span class="project-tag tag-violet-light">Email marketing</span>
            <span class="project-tag tag-orange">Lokálne SEO + GEO</span>
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
            <span class="project-tag tag-violet">Branding</span>
            <span class="project-tag tag-violet-light">Web dizajn</span>
            <span class="project-tag tag-cerulean">Copywriting</span>
            <span class="project-tag tag-orange">Lokálne SEO</span>
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
      <h2>Najdôležitejšie odpovede na jednom mieste</h2>
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
        <h2 style="margin:10px 0 14px;">S vami komunikujem ja, nie account manažér.</h2>
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
     "Za prácu platíte 12 EUR za hodinu. Malý web zvládnem za 10 hodín mesačne (120 EUR), väčší e-shop za 40 hodín (180 EUR). Presný rozsah vám potvrdím v pláne po bezplatnom audite."),
    ("Ako dlho trvá, kým SEO prinesie výsledky?",
     "Prvé pohyby vidíte na menej konkurenčných kľúčových slovách zvyčajne za 2 až 4 mesiace. Na hlavné dotazy v konkurenčných odvetviach trvá 6 až 12 mesiacov. Reálne termíny vám poviem už v audite."),
    ("Budem vidieť, za čo platím?",
     "Áno. Mesačný report vám dám osobne: 30-minútový hovor, v ktorom prejdeme odpracované hodiny a ich výsledky: pozície, kliky z Google, objednávky a zmienky v AI. Bez reportovania sa nepohne žiadna práca."),
    ("Pomôžete mi, aby ma ChatGPT odporúčal?",
     "Áno, to je moja špecializácia. Optimalizujem web pre AI nástroje (ChatGPT, Gemini, AI Overviews) tak, aby vás odporúčali pri dotazoch vašich zákazníkov."),
    ("Sú zmluvy viažúce na 12 mesiacov?",
     "Nie. Pracujem mesačne, spoluprácu môžete skončiť kedykoľvek. Dôveru staviam na výsledkoch, nie na viazanosti."),
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
        desc="SEO optimalizácia webu, lokálne SEO a Google firemný profil, SEO pre AI vyhľadávače, e-shop SEO, audit, linkbuilding a e-mail marketing. 12 EUR za hodinu.",
        canonical=BASE + "/sk/sluzby/", body=body, prefix="../..", extra_head=ORG_SCHEMA,
    )
    return ("sk/sluzby/index.html", html)


# ---------------------------------------------------------------- SERVICE PAGES

def _service_page(*, path: str, title: str, desc: str, label: str, h1: str,
                  intro: str, for_who: list[str], deliverables: list[str],
                  faq: list[tuple[str, str]], slug: str, svc_name: str,
                  proof: dict | None = None, time_estimate: str = "8 až 20 hodín mesačne") -> tuple[str, str]:
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
    <div class="section-head">
      <span class="section-label">V skratke</span>
      <h2>Kľúčové veci, na ktoré sa pýtate</h2>
    </div>
    <div class="case-result proof-band">
      <div><strong>Pre koho</strong><span>{' '.join(for_who[:1]).split('.')[0][:80] or 'firmy a e-shopy'}</span></div>
      <div><strong>Časový odhad</strong><span>{time_estimate}</span></div>
      <div><strong>Cena</strong><span>12 EUR za hodinu, vykazované v reporte</span></div>
      <div><strong>Ďaľší krok</strong><span><a href="/sk/kontakt/" style="color:var(--brand-primary-deep); font-weight:700;">Bezplatný vstupný audit</a></span></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="rate-band">
      <div>
        <div class="rate-big">12 EUR <small>za hodinu · kedykoľvek skončíte</small></div>
        <p style="margin-top:8px; max-width:520px;">Časový odhad tejto služby: {time_estimate}, podľa rozsahu webu a konkurencie.</p>
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
        time_estimate="10 hodín mesačne pre firemný web (120 EUR), e-shop 10 až 15 hodín",
        h1="SEO optimalizácia, ktorá privedie zákazníkov",
        intro="Zákazník, ktorý vás hľadá v Google, je najlacnejší zákazník. Web postavím tak, aby mu Google rozumel a zaradil ho vyššie a návštevníci odchádzali s odpoveďou, nie s otáznikom.",
        for_who=[
            "Máte web, ktorý neprináša kontakty ani objednávky z vyhľadávania.",
            "Konkurencia vás predbieha na dotazoch, ktoré vás zaujímajú.",
            "Ste viditeľní len na názve firmy, nie na tom, čo predávate.",
            "Platíte reklamu a chceli by ste časť dopytov zachytiť zdarma.",
        ],
        deliverables=[
            "Kľúčová analýza: na čo zákazníci reálne hľadajú a čo to stojí za prácu.",
            "Technická oprava webu: rýchlosť, indexácia, kanonizácia, chyby 404, sitemap.",
            "Prepis titulkov a popisov na dotazy, ktoré majú reálny dopyt.",
            "Nové obsahové stránky na dopyty, kde konkurencia nie je silná.",
            "Interné prelinkovanie, ktoré posunie silné stránky vyššie.",
            "Mesačný report: 30-minútový hovor so mnou, pozície, kliky zo Search Console, objednávky.",
        ],
        faq=[
            ("Koľko hodín mesačne zaberie SEO optimalizácia?",
             "Firemný web zvládnem v 10 hodinách mesačne (120 EUR), e-shop v 10 až 15 hodinách (120 až 180 EUR). Rozsah potvrdím v pláne po audite."),
            ("Za aký čas sa objavia prvé výsledky?",
             "Prvé pohyby na menej konkurenčných dotazoch za 2 až 4 mesiace, na hlavné dotazy 6 až 12 mesiacov. Záleží na konkurencii a stave webu."),
            ("Robíte aj obsah? Nemám čas písať.",
             "Áno, písanie obsahu je súčasťou hodín. Sám navrhnem štruktúru, napíšem texty a pred publikovaním ich schválite."),
            ("Čo ak som už SEO robil a nič to neprinieslo?",
             "Bezplatný audit presne povie, čo predchádzajúca práca nechala nedokončené. Často chýbajú dva či tri kroky, nie celé SEO."),
        ],
        svc_name="SEO optimalizácia webu",
        proof={
            "title": "Kliky z Google: +355 % za 3 mesiace spolupráce",
            "numbers": [("250", "klikov za 3 mesiace", "#6A3FC4"),
                        ("+355 %", "rast oproti predchádzajúcemu obdobiu", "#F75940"),
                        ("8 950", "zobrazení mesačne (+246 %)", "#1DACD6")],
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
        time_estimate="8 hodín na nastavenie profilu, potom 4 hodiny mesačne",
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
            "Týždenný prehľad: volania, žiadosti o trasu, zobrazenia na mape.",
        ],
        faq=[
            ("Ako dlho trvá, kým Google profil začne fungovať?",
             "Prvé zlepšenia v mape viditeľné za 4 až 8 týždňov, stabilná pozícia trvá 3 až 6 mesiacov. Záleží na konkurencii v okolí."),
            ("Mám len jedno pôsobisko. Oplatí sa mi to?",
             "Práve pre jedno pôsobisko je lokálne SEO najúčinnejšie. Sústredíte všetku silu do vášho mesta a okresu, kde je konkurencia najmenšia."),
            ("Ako získam viac hodnotení na Google?",
             "Mám jednoduchý postup cez SMS a QR kód, ktorý zákazníkov vyzýva hneď po vykonaní služby. Zvyšuje mieru recenzií niekoľkonásobne."),
            ("Ako riešite zlé hodnotenia?",
             "Odpovedám profesionálne a na mieste. Zlé hodnotenia nemožno odstrániť, ale dobrý pomer a kultivované odpovede pôsobia na zákazníkov viac ako počet hviezd."),
        ],
        svc_name="Lokálne SEO a Google firemný profil",
        proof={
            "title": "359 ľudí videlo firemný profil klienta za jedno obdobie",
            "numbers": [("359", "zobrazení firemného profilu", "#6A3FC4"),
                        ("54 %", "zobrazení cez Google Mapy", "#F75940"),
                        ("46 %", "Zobrazení cez Google Vyhľadávanie", "#9B6FD9")],
            "caption": "Lokálny zákazník hľadá dvomi cestami: cez Mapy (54 % zobrazení) a cez bežné Google hľadanie (46 %). Preto drvíme obe: profil nastavený na doraz, hodnotenia prichádzajú pravidelne a web podporuje mapové pozície.",
            "source": "Zdroj: štatistiky Google firemného profilu klienta, ukážka zo septembra 2026",
        },
    )


def seo_ai() -> tuple[str, str]:
    return _service_page(
        path="sluzby/seo-pre-ai-vyhladavace/", slug="seo-pre-ai-vyhladavace",
        title="SEO pre AI vyhľadávače: ChatGPT a AI Overviews | Nokto Studio",
        desc="Optimalizácia pre AI vyhľadávače a AI Overviews. ChatGPT a Gemini vás odporúčajú zákazníkom. Prvá agentúra na Slovensku s touto špecializáciou.",
        label="Služba · SEO pre AI",
        time_estimate="6 až 12 hodín prvý mesiac, potom 4 až 8 hodín mesačne",
        h1="Aby vás ChatGPT odporúčal zákazníkom",
        intro="Zákazník dnes nepýta len Google. Pýta ChatGPT: \u201eOdporúč mi dobrého zubára v Nitre.\u201c AI nástroj odpovie dvomi až piatimi menami. Mojou úlohou je, aby vaše meno tam bolo.",
        for_who=[
            "Chcete, aby vás AI nástroje odporúčali ako prvú voľbu vo vašom odvetví.",
            "Vidíte, že zákazníci prichádzajú s vetou \u201enašiel ChatGPT, že...\u201c",
            "Konkurencia sa na AI odporúčania zatiaľ nepripravuje (to je výhoda).",
            "Máte expertízu a chcete ju mať viditeľnú aj pre AI, nielen pre Google.",
        ],
        deliverables=[
            "Audit AI viditeľnosti: ako vás dnes ChatGPT, Gemini a AI Overviews citujú a kde chýbate.",
            "Priame odpovede na stránkach: úvodné odseky vo formáte, z ktorého AI čerpá.",
            "Štruktúrované dáta (schema.org) pre ľahké čítanie AI nástrojmi.",
            "Obsahové stránky odpovedajúce na reálne otázky zákazníkov (People Also Ask, AI dotazy).",
            "Mesačné sledovanie: v ktorých AI odpovediach sa objavujete a čo sa zmenilo.",
            "Prevádzka rozšírení pre AI roboty (llms.txt, robots.txt, prístup pre GPTBot a PerplexityBot).",
        ],
        faq=[
            ("Je toto SEO alebo marketing?",
             "Je to priame pokračovanie SEO. Google aj ChatGPT čerpajú z webu, rozdiel je v tom, čo a ako čítajú. Nastavím oboje naraz."),
            ("Ako meriate, či ma AI odporúča?",
             "Pravidelne testujem sadu dotazov, ktoré vaši zákazníci vyhľadávajú, a zaznamenávam, či sa vaše meno v odpovediach objavuje. Výsledky máte v reporte."),
            ("To môže trvať dlho?",
             "Víťazstvo v AI odporúčaniach je zvyčajne rýchlejšie než klasické SEO pozície, pretože konkurencia tu len začína. Prvé zmienky vidím často do 2 až 3 mesiacov."),
            ("Pre koho to má zmysel?",
             "Pre služby, kde zákazník hľadá odporúčanie: zdravotníctvo, právo, servis, stavebníctvo, školenia. Pre e-shopy pomáha v dotazoch typu \u201ekto predáva...\" a v recenziách."),
        ],
        svc_name="Optimalizácia pre AI vyhľadávače",
        proof={
            "title": "13 AI citácií e-shopu v Google AI Mode za 3 mesiace",
            "numbers": [("13", "AI citácií webu v Google AI Mode", "#9B6FD9"),
                        ("8", "citácie jednej stránky /overaly/", "#6A3FC4"),
                        ("3", "citácie blogového článku", "#1DACD6")],
            "caption": "Po nasadení nášho obsahu cituje Google AI Mode konkrétne stránky e-shopu priamo v odpovediach zákazníkom. Najviac citovaná stránka dosiahla 8 citácií, blogový článok 3. Konkurencia v AI odpovediach na tieto dotazy ešte nie je, takže prvé mená tam ostávajú.",
            "source": "Zdroj: Google AI Mode (report citácií), ukážka z augusta 2026",
        },
    )


def eshop_seo() -> tuple[str, str]:
    """REFRESH 2026-09-16. Target GSC query: 'seo pre eshopy' (pos 66, 1 impr).
    Better angle: Shoptet-specific technical issues + category vs product SEO split +
    Mikramt real revenue case with concrete numbers, none of which appear in SK SERP top-10."""
    url = BASE + "/sk/sluzby/seo-pre-eshopy/"
    title = "SEO pre e-shopy: Shoptet, WooCommerce, Google Shopping | Nokto Studio"
    desc = ("SEO pre e-shopy: kategórie, produkty, Shoptet technické problémy, Google Merchant Center, "
            "Heureka a Marketplace. Reálne tržby z organického vyhľadávania, 12 EUR za hodinu.")
    label = "Služba · SEO pre e-shopy"
    h1 = "SEO pre e-shopy: viac objednávok z Google bez platenia za každý klik"
    intro = ("SEO pre e-shop je optimalizácia kategórií, produktov a technickej štruktúry tak, aby "
             "zákazník, ktorý hľadá konkrétny produkt, našiel vás v Google a nezobral ho konkurentovi. "
             "Nemerám návštevnosť, merám objednávky a tržby z organického kanála. Pre Shoptet, "
             "WooCommerce aj vlastné platformy. Moja práca stojí 12 EUR za hodinu, bežne 20 až 40 "
             "hodín mesačne pre malý až stredný e-shop.")

    who = [
        "Máte e-shop na Shoptete, WooCommerci alebo vlastnej platforme a predaj závisí od platených reklam.",
        "Kategórie nemajú unikátne texty a Google ich považuje za duplicitné s filtrami.",
        "Ste viditeľní len na presných názvoch produktov, nie na dotazoch, ktoré zákazník reálne hľadá.",
        "Google Merchant Center odmieta vaše produkty a neviete prečo.",
        "Chcete znížiť náklady na reklamu tým, že časť dopytov chytíte z organického vyhľadávania zdarma.",
    ]
    deliv = [
        "Technický audit e-shopu: kanonizácia filtrov, duplicitné URL, rýchlosť, indexácia, Core Web Vitals.",
        "Kľúčové slová pre kategórie aj produkty, s objemami dopytov z Marketing Minera.",
        "Texty kategórií, ktoré predávajú a nie sú duplicitné s filtrami ani s popismi výrobcov.",
        "Texty produktov, ktoré reálne odpovedajú na otázky zákazníka a nie sú copy-paste zFeedu.",
        "Google Merchant Center: feed štruktúra, atribúty, schválenie produktov, zameranie na Shopping.",
        "Heureka, NajNakup, Mall: integrácie a feed optimalizácia pre porovnávače.",
        "Interné prelinkovanie: kategórie medzi sebou, súvisiace produkty, blok odporúčaní.",
        "Report v objednávkach a tržbách z organického kanála, nielen v návštevnosti.",
    ]

    faq = [
        ("Robíte SEO aj pre Shoptet?",
         "Áno, Shoptet je najbežnejšia platforma na Slovensku a poznám jej špecifiká. Najčastejšie "
         "problémy: duplicitné URL pri filtroch (Shoptet generuje parametrické URL bez canonical), "
         "chýbajúce H1 na kategóriách, copy-paste popisy produktov z feedu výrobcu, a pomaly "
         "načítavanie kvôli veľkým obrázkom. Riešim všetky cez Shoptet SEO modul alebo vlastné "
         "úpravy šablony, ak máte vetu PRO."),
        ("Koľko objednávok z toho bude?",
         "Reálne čísla vám poviem po audite, na základe vašich kľúčových slov a ich objemu dopytov. "
         "Nikdy nepoviem číslo, ktoré nedokážem podložiť dátami. Mikramt.sk, malý e-shop, po 9 "
         "mesiacoch SEO práce: 15 objednávok z organického a e-mailového kanála, 2492,75 EUR tržieb, "
         "najväčšia objednávka 722 EUR. Vaše čísla závisia od vašej branže, ceny a konkurencie."),
        ("Musím robiť aj linkbuilding?",
         "Pre konkurenčné kategórie (móda, elektronika, kozmetika) áno, bez autority je odozva "
         "pomalá a pozície prídu až za rok. Pre špecifické výrobky a malú konkurenciu môže "
         "postačiť technická optimalizácia a obsah kategórií. Po audite odporučím rozsah, ktorý "
         "dáva zmysel pre váš rozpočet, a cena odkazov bude vykazovaná zvlášť."),
        ("Ako sa meria úspech SEO pre e-shop?",
         "V Google Analytics 4 sledujem objednávky, tržby a konverzný pomer z organického "
         "vyhľadávania. V Search Console kliky a zobrazenia na produktové a kategóriové dotazy. "
         "V Google Merchant Centre schválenie a výkonnosť produktov v Shopping. Report máte "
         "mesačne, v ňom reálne tržby z organického kanála, nielen návštevnosť."),
        ("Čo s Google Merchant Center, ak mi odmieta produkty?",
         "Najčastejšie dôvody zamietnutia: chýbajúce GTIN alebo MPN, nekonzistentné dáta medzi "
         "feedom a e-shopom, politika reklam (napríklad doplnky výživy), nízka kvalita obrázkov, "
         "alebo produktové URL, ktoré sú canonical na filtrovanú verziu. Audytujem feed, "
         "opravím atribúty a podám žiadosť o re-schválenie. Bez toho Shopping nefunguje."),
        ("Ako dlho trvá, kým e-shop začne rásť z organického vyhľadávania?",
         "Prvé pohyby na menej konkurenčných produktových dotazoch za 2 až 3 mesiace. Na "
         "kategóriové dotazy 4 až 8 mesiacov. Plný potenciál, ak spolu s linkbuildingom, "
         "12 až 18 mesiacov. E-shop, ktorý má 1000 produktov a žiadny obsah kategórií, potrebuje "
         "najmenej 6 mesiacov na to, aby Google vôbec pochopil, čo predáva."),
    ]

    # Konkrétne Shoptet vs WooCommerce vs vlastné - čo SERP nemá.
    platform_table = """
<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Platformy</span>
      <h2>SEO pre Shoptet, WooCommerce a vlastné e-shopy: konkrétne rozdiely</h2>
      <p class="section-subheading">Každá platforma má iné technické problémy. Tu sú tie, ktoré v audite riešim ako prvé.</p>
    </div>
    <table class="metric-table">
      <tr><th>Aspekt</th><th>Shoptet</th><th>WooCommerce</th><th>Vlastná platforma</th></tr>
      <tr><td><strong>Duplicitné URL filtrov</strong></td><td>Áno, bežný problém, rieši canonical tag</td><td>Áno, závisí od pluginu, často chýba</td><td>Závisí od implementácie, často chýba</td></tr>
      <tr><td><strong>H1 na kategóriách</strong></td><td>Šablona generuje, dá sa upraviť cez SEO modul</td><td>Téma generuje, dá sa prepísať</td><td>Treba nakódovať, často chýba</td></tr>
      <tr><td><strong>Rýchlosť (Core Web Vitals)</strong></td><td>Stredná, obrázky a JS brzdia LCP</td><td>Záleží od pluginov, často pomalé</td><td>Záleží od vývojara, môže byť rýchla</td></tr>
      <tr><td><strong>Štruktúrované dáta Product</strong></td><td>Automatické, ale chýbajúce atribúty</td><td>Plugin (Yoast, RankMath) ich pridá</td><td>Treba nakódovať JSON-LD</td></tr>
      <tr><td><strong>Google Merchant feed</strong></td><td>Auto-feed cez Shoptet add-on</td><td>Plugin (WC Product Feed) alebo vlastný</td><td>Vlastný generátor feedu</td></tr>
      <tr><td><strong>Interné prelinkovanie</strong></td><td>Obmedzené, modul "súvisiace produkty"</td><td>Pluginy ako YARPP</td><td>Volné, treba nakódovať</td></tr>
      <tr><td><strong>Blog pre SEO</strong></td><td>Áno, v Shoptet blog module</td><td>Áno, natívne WordPress</td><td>Treba samostatne implementovať</td></tr>
    </table>
  </div>
</section>"""

    # Kategórie vs produkty - kedy čo optimalizovať. SERP to nerozlišuje.
    cat_vs_prod = """
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Stratégia</span>
      <h2>Kategórie vs. produkty: kedy optimalizovať čo</h2>
      <p class="section-subheading">Najväčšia chyba e-shop SEO je písať dlhé texty na každý produkt. Tu je rozdelenie, ktoré šetrí čas a prináša objednávky.</p>
    </div>
    <div class="grid-2" style="align-items:start;">
      <div class="prose">
        <h3>Kategórie (90 percent úsilia)</h3>
        <p>Na kategóriách sa rozhoduje o 80 percentách objednávok. Zákazník hľadá "biele tričko ženské", nie "Adidas Originals TREFOIL HOODY ČIERNA M". Kategóriový text musí odpovedať na dotaz, pomôcť pri výbere a prelinkovať na produkty. Pre každú kategóriu: unikátny H1 s kľúčovým slovom, 300 až 600 slov textu, zoznam produktov s alt obrázkov, FAQ sekcia s otázkami o výbere.</p>
        <h3>Kedy optimalizovať každý produkt</h3>
        <p>Iba pre produkty s reálnym hľadaným názvom (iPhone 15, Samsung Galaxy S24). Pre väčšinu produktov stačí: správny H1, meta title s názvom a značkou, štruktúrované dáta Product so cena, dostupnosť a obrázok, a interný odkaz z kategórie. Čas z investovaný do 100 textov produktov preneste radšej do 5 kategóriových textov, ktoré majú 10x vyšší dopad.</p>
      </div>
      <div class="prose">
        <h3>Kedylinky do Heureky a NajNakup</h3>
        <p>Porovnávače nie sú SEO, ale driving faktor návštevnosti a konverzií. Ak je váš produkt na Heureke, zákazník ho nájde aj bez vás. Práca je: kvalitný feed s GTIN, EAN, porovnateľné ceny, recenzie, fotky. Pre špecifické produkty bez konkurencie na Heureke má zmysel ideť do Mall.sk alebo Najnakup.sk.</p>
        <h3>Google Shopping a Merchant Center</h3>
        <p>Shopping kampane prinášajú konverzie rýchlejšie než organické SEO, ale vyžadujú čistý feed. Najčastejšie chyby: chýbajúci GTIN/MPN, nekonzistentné ceny medzi feedom a e-shopom, produktové URL s canonical na filtrovanú verziu. Audytujem Merchant Center ako prvý, lebo bez neho nefunguje ani organický výskyt v Shopping karte.</p>
      </div>
    </div>
  </div>
</section>"""

    # Konkrétne technické problémy Shoptet e-shopov, SERP ich nerozoberá.
    shoptet_issues = """
<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Technické problémy</span>
      <h2>Najčastejšie technické problémy e-shopov, ktoré riešim v audite</h2>
      <p class="section-subheading">Tieto chyby brzdia 90 percent slovenských e-shopov. V audite ich identifikujem ako prvé.</p>
    </div>
    <div class="grid-2" style="align-items:start;">
      <div class="card">
        <span class="section-label">1. Duplicitné URL filtrov</span>
        <p>Kategória "tričká" s filtrom na farbu generuje /tricka?farba=biela. Bez canonical je to pre Google duplicita. Riešenie: canonical tag na hlavnú kategóriu, alebo noindex na parametrické URL. V Shoptete cez SEO modul, vo WooCommerci cez plugin Yoast alebo RankMath.</p>
      </div>
      <div class="card">
        <span class="section-label">2. Copy-paste popisy produktov</span>
        <p>Výrobcovia dávajú rovnaký popis všetkým e-shopom. Google ich považuje za duplicitu a radí prvý e-shop, ktorý ho uverejnil. Riešenie: prepísať prvé 2 odseky vlastnými slovami, pridať reálne foto, používateľské recenzie a Q&amp;A.</p>
      </div>
      <div class="card">
        <span class="section-label">3. Chýbajúce texty kategórií</span>
        <p>Najčastejšia chyba: kategória má len zoznam produktov, žiadny text. Google ju nedokáže zaradiť na konkrétny dotaz. Riešenie: 300 až 600 slov textu, ktorý odpovedá na dotaz zákazníka a pomáha pri výbere. Tento jednoduchý krok zvýši organické zobrazenia o 40 až 200 percent.</p>
      </div>
      <div class="card">
        <span class="section-label">4. Pomalé načítavanie (LCP)</span>
        <p>E-shopy s veľkými obrázkami produktov majú LCP nad 4 sekundy. Google radí pomalšie weby nižšie. Riešenie: WebP obrázky, lazy loading, CDN, obmedzenie počtu produktov na stránke. Pre Shoptet je limit 24 produktov na stránku, vo WooCommerci závisí od témy.</p>
      </div>
      <div class="card">
        <span class="section-label">5. Chýbajúce štruktúrované dáta Product</span>
        <p>Bez Product JSON-LD Google nezobrazuje cenu a dostupnosť priamo vo výsledkoch vyhľadávania. Riešenie: pridať JSON-LD s name, image, price, availability, sku, brand. V Shoptete automaticky, vo WooCommerci cez Yoast alebo RankMath, na vlastnej platforme treba nakódovať.</p>
      </div>
      <div class="card">
        <span class="section-label">6. Stránky bez obsahu (thin pages)</span>
        <p>Kategórie s 2 produktmi, značkové stránky bez textu, prázdne výsledky filtrov. Google ich označuje ako "Discovered, currently not indexed". Riešenie: noindex pre kategórie s menej ako 5 produktmi, presmerovanie na nadradenú kategóriu, alebo zlúčenie.</p>
      </div>
    </div>
  </div>
</section>"""

    proof_block = """
<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Výsledok z praxe</span>
      <h2>Mikramt.sk: 2 492,75 EUR tržieb za 9 mesiacov z organického a e-mailu</h2>
    </div>
    <div class="case-result proof-band"><div><strong style="color:#6A3FC4;">2 492,75 EUR</strong><span>tržby za 9 mesiacov</span></div><div><strong style="color:#9B6FD9;">15</strong><span>objednávok z e-mailu a organického vyhľadávania</span></div><div><strong style="color:#1DACD6;">722 EUR</strong><span>najväčšia jednorazová objednávka</span></div></div>
    <p style="margin-top:16px; max-width:720px; color:var(--text-2);">Regionálny dodávateľ s e-shopom na vlastnej platforme (nie Shoptet), API integráciou na účtovný systém a e-mail marketingom. Práca: texty kategórií, ktoré dovtedy nemali žiadny obsah, oprava technických chýb v štruktúrovaných dátach, integrácia Google Merchant Center, a nastavenie e-mailových sekvencií. Objednávky chodia z dvoch kanálov: organický Google a e-mail. Súčasťou je aj lokálne SEO a optimalizácia pre AI vyhľadávače.</p>
    <p style="margin-top:4px; font-size:0.8rem; color:var(--text-muted);">Zdroj: objednávky pripísané kanálom e-mail a organický Google, 9 mesiacov spolupráce</p>
  </div>
</section>"""

    body = f"""
{page_hero(label, h1, intro, [("Domov", "/"), ("Služby", "/sk/sluzby/"), ("SEO pre e-shopy", None)])}

<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:start;">
      <div class="prose">
        <h2>Pre koho je táto služba?</h2>
        <ul>{"".join(f"<li>{w}</li>" for w in who)}</ul>
      </div>
      <div class="card">
        <span class="section-label">Čo dodávam</span>
        <ul class="deliv-list">{"".join(f'<li><span class="check">✓</span><span>{d}</span></li>' for d in deliv)}</ul>
      </div>
    </div>
  </div>
</section>

{platform_table}

{cat_vs_prod}

{shoptet_issues}

{proof_block}

{process_section("Ako pobeží spolupráca")}

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">V skratke</span>
      <h2>Kľúčové veci, na ktoré sa pýtate</h2>
    </div>
    <div class="case-result proof-band">
      <div><strong>Pre koho</strong><span>E-shopy na Shoptete, WooCommerci aj vlastnej platforme</span></div>
      <div><strong>Časový odhad</strong><span>10 až 15 hodín mesačne (120 až 180 EUR), 6 mesiacov minimálne</span></div>
      <div><strong>Cena</strong><span>12 EUR za hodinu, linkbuilding a reklamné výdavky zvlášť</span></div>
      <div><strong>Ďaľší krok</strong><span><a href="/sk/kontakt/" style="color:var(--brand-primary-deep); font-weight:700;">Bezplatný vstupný audit e-shopu</a></span></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="rate-band">
      <div>
        <div class="rate-big">12 EUR <small>za hodinu · kedykoľvek skončíte</small></div>
        <p style="margin-top:8px; max-width:520px;">Časový odhad tejto služby: 10 až 15 hodín mesačne (120 až 180 EUR), podľa rozsahu e-shopu a konkurencie. Náklady na odkazy vykazované zvlášť.</p>
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
    {cta_band("Chcete vedieť, čo by táto služba priniesla vášmu e-shopu?", "Bezplatný audit a 30 minút času. Žiadne záväzky, s reálnymi číslami tržieb.", "sk")}
  </div>
</section>
"""
    extra = schema_service("SEO pre e-shopy", desc, url) + faq_schema(faq, url)
    html = base(market="sk", path="sluzby/seo-pre-eshopy/", title=title, desc=desc,
                canonical=url, body=body, prefix="../../../", extra_head=ORG_SCHEMA + extra)
    return ("sk/sluzby/seo-pre-eshopy/index.html", html)


def audit_seo() -> tuple[str, str]:
    """REFRESH 2026-09-16. Target GSC query: 'hodnotenie webu seo audit' (pos 91, 1 impr).
    Better angle: konkrétne body, ktoré audit kontroluje + rozdiel vstupný vs detailný audit
    + reálna prípadová štúdia (6 stránok = 11 000 zobrazení), none of which appear in SK SERP top-10."""
    url = BASE + "/sk/sluzby/seo-audit/"
    title = "SEO audit webu: hodnotenie, analýza a akčný plán | Nokto Studio"
    desc = ("SEO audit webu s konkrétnym zoznamom chýb a šancí. Technika, obsah, kľúčové slová, "
            "konkurencia. Vstupný audit zdarma do 3 dní, detailný od 12 EUR za hodinu.")
    label = "Služba · SEO audit"
    h1 = "SEO audit: hodnotenie vášho webu s akčným plánom, nie PDF na polici"
    intro = ("SEO audit je systematické hodnotenie webu, ktoré odpovie na tri otázky: prečo sa "
             "vám nedarí v Google, čo presne treba opraviť, a v akom poradí. Začínam bezplatným "
             "vstupným auditom, ktorý máte do troch dní: 10 najväčších problémov a šancí na jednej "
             "strane. Detailný audit je akčný plán s hodinami a prioritami, nie 60-stranové PDF. "
             "Moja práca stojí 12 EUR za hodinu, detailný audit stojí 120 až 180 EUR podľa rozsahu.")

    who = [
        "Neviete, prečo váš web neprináša zákazníkov z Google, hoci naň pravidelne pridávate.",
        "Máte za sebou SEO prácu, ale výsledky chýbajú a neviete, čo ostalo nedokončené.",
        "Pred väčšou investíciou do webu, redizajnu alebo reklamnej kampane chcete objektívny rozbor.",
        "Potrebujete plán, ktorý vykonáte sami, s vlastným vývojárom, alebo so mnou.",
        "Chcete druhý názor na prácu, ktorú vám urobila iná agentúra.",
    ]
    deliv = [
        "Vstupný audit zdarma: 10 najväčších problémov a šancí na jednej strane, do 3 pracovných dní.",
        "Detailný audit: technika (rýchlosť, indexácia, kanonizácia, sitemap, robots, Core Web Vitals).",
        "Obsahový audit: ktoré stránky majú reálny dopyt, ktoré sú tenké, ktoré sa kanibalizujú.",
        "Kľúčové slová s objemami dopytov z Marketing Minera a odhadom reálnych šancí.",
        "Rozbor konkurencie: na čom stoja, ktoré odkazy majú, čo im chýba.",
        "Plán s prioritami: čo opraviť ako prvé, koľko hodín to zaberie, aký je očakávaný dopad.",
        "Interné prelinkovanie: analýza, ktoré silné stránky pomáhajú slabším a kde chýba.",
        "45-minútová prehliadka s vami: odpovede na vaše otázky k auditu.",
    ]

    faq = [
        ("Čo je SEO audit a načo mi je?",
         "SEO audit je systematické hodnotenie vášho webu, ktoré odpovie: čo Google brzdí v "
         "indexácii a pozíciách, čo na obsahu chýba, ktoré kľúčové slová má zmysel cieľovať a v "
         "akom poradí to riešiť. Bez auditu strávite mesiace úsilím, ktoré možno smeruje zlým "
         "smerom. Audit vás ochráni pred zbytočnou investíciou a povie vám, čo skutočne funguje."),
        ("Koľko stojí SEO audit?",
         "Vstupný audit je zdarma, máte ho do 3 pracovných dní. Detailný audit stojí 120 až 180 "
         "EUR podľa rozsahu webu (10 až 15 hodín × 12 EUR). Pre malý firemný web s 20 stranami "
         "stačí 180 EUR, pre e-shop s 500 produktmi 180 EUR. Presnú cenu potvrdím po prvej "
         "pohľad na váš web."),
        ("Čo obsahuje detailný SEO audit?",
         "Technická časť: rýchlosť (Core Web Vitals), indexácia, sitemap, robots.txt, kanonizácia, "
         "chyby 404, štruktúrované dáta. Obsahová časť: ktoré stránky majú reálny dopyt, ktoré "
         "sú tenké, ktoré sa kanibalizujú. Kľúčové slová: zoznam s objemami z Marketing Minera. "
         "Konkurencia: rozbor 3 hlavných konkurentov. Plán: zoznam úloh s prioritami, odhadom "
         "hodín a očakávaným dopadom."),
        ("Dostanem súbor, ktorý môžem odovzdať vývojárovi?",
         "Áno. Plán je v zrozumiteľnom formáte s úlohami po jednotlivých krokoch, priamo pre "
         "používateľa v CMS alebo vývojára. Pri technických úlohách pridávam konkrétne príkazy "
         "alebo úryvky kódu. Pri obsahových príklady textu, ktoré stačí prepísať. Plán môžete "
         "vykonať sami, s vlastným vývojárom, alebo so mnou."),
        ("Musím potom využívať aj ďalšie služby?",
         "Nie. Plán si môžete vykonať sami alebo s iným partnerom. Ak sa rozhodnete pracovať so "
         "mnou, plán slúži ako základ mesačnej spolupráce: 10 až 20 hodín mesačne, podľa "
         "priorít. Pevná zmluva nie je, spoluprácu môžete kedykoľvek ukončiť."),
        ("Ako rýchlo dostanem audit?",
         "Vstupný audit do 3 pracovných dní od prvého hovoru. Detailný audit za 7 až 10 dní, "
         "podľa rozsahu webu. E-shopy s 500 a viac produktmi môžu trvať 14 dní, lebo stiahnem a "
         "analyzujem každý produkt. K auditu potrebujem prístup do Google Search Console a "
         "Google Analytics, ak ich máte."),
        ("Môžete urobiť audit aj webu, ktorý sa práve plánuje postaviť?",
         "Áno, audit pred vývojom je najlacnejší spôsob, ako predísť technickým dlhom. Nahliadnem "
         "do wireframov alebo prototypu a pripravím zoznam požiadaviek pre vývojára: URL "
         "štruktúra, štruktúrované dáta, rýchlosť, hreflang, CMS nastavenia. Cena 120 až 180 EUR (v cene retainera), "
         "ušetrí vám desiatky tisíc eur na prerábaní webu po launchi."),
    ]

    # Konkrétne body, ktoré audit kontroluje - SERP ich nezverejňuje v takomto formáte.
    audit_checklist = """
<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Čo kontrolujem</span>
      <h2>40 konkrétnych bodov, ktoré audit kontroluje</h2>
      <p class="section-subheading">Toto nie je zoznam "viacero SEO faktorov". Je to konkrétny check-list, ktorý používam pri každom audite.</p>
    </div>
    <div class="grid-2" style="align-items:start;">
      <div class="card">
        <span class="section-label">Technická časť (15 bodov)</span>
        <ul class="deliv-list">
          <li><span class="check">✓</span><span>Indexácia: koľko strán je v Google, koľko z nich je "Crawled, currently not indexed"</span></li>
          <li><span class="check">✓</span><span>Sitemap.xml: kompletná, aktuálne, bez chýb</span></li>
          <li><span class="check">✓</span><span>Robots.txt: blokuje len to, čo má, neblokuje dôležité stránky</span></li>
          <li><span class="check">✓</span><span>Kanonizácia: každá stránka má správny canonical, žiadne duplicitné URL</span></li>
          <li><span class="check">✓</span><span>Core Web Vitals: LCP pod 2,5s, INP pod 200ms, CLS pod 0,1</span></li>
          <li><span class="check">✓</span><span>Rýchlosť na mobile a desktope (PageSpeed Insights)</span></li>
          <li><span class="check">✓</span><span>404 chyby a 301 presmerovania: žiadne zlé reťaze</span></li>
          <li><span class="check">✓</span><span>HTTPS: certifikát platný, žiadny mixed content</span></li>
          <li><span class="check">✓</span><span>Štruktúrované dáta: Organization, WebSite, BreadcrumbList, Article/Product</span></li>
          <li><span class="check">✓</span><span>Hreflang: ak viacjazyčný, správne páry a x-default</span></li>
          <li><span class="check">✓</span><span>JavaScript rendering: obsah viditeľný bez JS, alebo SSR</span></li>
          <li><span class="check">✓</span><span>Interné prelinkovanie: žiadne osamotené stránky, silné stránky posúvajú slabšie</span></li>
          <li><span class="check">✓</span><span>URL štruktúra: čisté, krátke, s kľúčovými slovami, bez parametrov</span></li>
          <li><span class="check">✓</span><span>Pagination: správne rel=prev/next alebo canonical na prvú stranu</span></li>
          <li><span class="check">✓</span><span>Lazy loading: obrázky sa načítavajú len pri scrolle, ale s SSR fallback</span></li>
        </ul>
      </div>
      <div class="card">
        <span class="section-label">Obsahová časť (10 bodov)</span>
        <ul class="deliv-list">
          <li><span class="check">✓</span><span>Title a meta description na každej stránke, s kľúčovým slovom a pod CTR</span></li>
          <li><span class="check">✓</span><span>H1 unikátny na každej stránke, s hlavným kľúčovým slovom</span></li>
          <li><span class="check">✓</span><span>H2-H3 hierarchia bez preskočenia úrovní</span></li>
          <li><span class="check">✓</span><span>Alt texty obrázkov s popisom, nie len keyword stuffing</span></li>
          <li><span class="check">✓</span><span>Thin content: stránky s menej ako 300 slov bez reálnej hodnoty</span></li>
          <li><span class="check">✓</span><span>Duplicity: rovnaký text na viacerých URL (copy-paste z feedu)</span></li>
          <li><span class="check">✓</span><span>Kanibalizácia: dve stránky súperiaace o rovnaké kľúčové slovo</span></li>
          <li><span class="check">✓</span><span>E-E-A-T signály: autor, dátum, zdroje, sameAs, skúsenosť</span></li>
          <li><span class="check">✓</span><span>Relevantnosť: obsah odpovedá na dotaz, ktorý má reálny dopyt</span></li>
          <li><span class="check">✓</span><span>FAQ a Q&A: otázky, na ktoré zákazník reálne hľadá odpoveď</span></li>
        </ul>
      </div>
    </div>
    <div class="grid-2" style="align-items:start; margin-top:24px;">
      <div class="card">
        <span class="section-label">Kľúčové slová a konkurencia (10 bodov)</span>
        <ul class="deliv-list">
          <li><span class="check">✓</span><span>Zoznam kľúčových slov s objemom dopytov (Marketing Miner)</span></li>
          <li><span class="check">✓</span><span>Intent analýza: komerčný, informačný, transakčný, navigačný</span></li>
          <li><span class="check">✓</span><span>SERP analýza: čo Google reálne zobrazuje pre hlavné dotazy</span></li>
          <li><span class="check">✓</span><span>Konkurencia: top 3 weby, ich pozície, odkazy, obsah</span></li>
          <li><span class="check">✓</span><span>Content gap: kľúčové slová, na ktoré konkurencia ide a vy nie</span></li>
          <li><span class="check">✓</span><span>Reálna šanca: pre malý web, ktoré dotazy majú zmysel ako prvé</span></li>
          <li><span class="check">✓</span><span>AI Overviews: či sa na vaše dotazy objavuje AI odpoveď v Google</span></li>
          <li><span class="check">✓</span><span>Lokálne SEO: Google firemný profil, NAP, citácie, hodnotenia</span></li>
          <li><span class="check">✓</span><span>Link profil: toxické odkazy, chýbajúce odkazy, konkurenčná medzera</span></li>
          <li><span class="check">✓</span><span>Prioritizácia: ktoré dotazy prinášajú zákazníkov, nie len návštevnosť</span></li>
        </ul>
      </div>
      <div class="card">
        <span class="section-label">Plán a odhad (5 bodov)</span>
        <ul class="deliv-list">
          <li><span class="check">✓</span><span>Zoznam úloh s prioritami: kritické, vysoké, stredné, nízke</span></li>
          <li><span class="check">✓</span><span>Odhad hodín na každú úlohu a celkový rozpočet mesačne</span></li>
          <li><span class="check">✓</span><span>Očakávaný dopad: ktoré úlohy prinesú pozície a ktoré návštevnosť</span></li>
          <li><span class="check">✓</span><span>Časový rámec: kedy očakávať prvé výsledky a kedy plný potenciál</span></li>
          <li><span class="check">✓</span><span>Interné odkazy a zdroje na vykonanie plánu</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>"""

    # Rozdiel vstupný vs detailný audit - SERP to nerozlišuje.
    audit_types = """
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Dve úrovne auditu</span>
      <h2>Vstupný audit zdarma vs. detailný audit: rozdiel</h2>
      <p class="section-subheading">Vstupný audit vám povie, či má zmysel investovať do SEO. Detailný audit vám povie presne čo a ako robiť.</p>
    </div>
    <table class="metric-table">
      <tr><th>Čo dostanete</th><th>Vstupný audit (zdarma)</th><th>Detailný audit (120 až 180 EUR)</th></tr>
      <tr><td><strong>Trvanie</strong></td><td>1 až 3 pracovné dni</td><td>7 až 14 pracovných dní</td></tr>
      <tr><td><strong>Rozsah</strong></td><td>10 najväčších problémov a šancí na 1 strane</td><td>40+ bodov, úlohy s hodinami a prioritami</td></tr>
      <tr><td><strong>Kľúčové slová</strong></td><td>5 hlavných, s objemom a intentom</td><td>30 až 100 kľúčových slov, SERP analýza, konkurencia</td></tr>
      <tr><td><strong>Konkurencia</strong></td><td>1 hlavný konkurent</td><td>3 konkurenti, content gap, link gap</td></tr>
      <tr><td><strong>Plán</strong></td><td>Odporúčanie ďalšieho kroku</td><td>Akčný plán s úlohami, hodinami a očakávaným dopadom</td></tr>
      <tr><td><strong>Prehliadka s vami</strong></td><td>30-minútový hovor</td><td>45-minútová prehliadka s odpoveďami na otázky</td></tr>
      <tr><td><strong>Formát</strong></td><td>1-stranový PDF + hovor</td><td>Plán v zrozumiteľnom formáte, úryvky kódu, príklady textu</td></tr>
      <tr><td><strong>Komu stačí</strong></td><td>Pre rozhodnutie, či má zmysel pokračovať</td><td>Pre vykonanie SEO, sami alebo s partnerom</td></tr>
    </table>
  </div>
</section>"""

    proof_block = """
<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Výsledok z praxe</span>
      <h2>Len 6 nových stránok zdvihlo celý web o 11 000 zobrazení mesačne</h2>
    </div>
    <div class="case-result proof-band"><div><strong style="color:#1DACD6;">11 000</strong><span>zobrazení mesačne (+14 %)</span></div><div><strong style="color:#6A3FC4;">+43 %</strong><span>klikov posledný týždeň</span></div><div><strong style="color:#9B6FD9;">6</strong><span>stránok, ktoré to spravili</span></div></div>
    <p style="margin-top:16px; max-width:720px; color:var(--text-2);">Toto je sila správneho plánu: nezostať pri 300 stranách webu, ale pridať 6 presne zacielených obsahových stránok na dopyty, ktoré zákazníci reálne pýtajú. Presne takéto príležitosti audit hľadá ako prvé. Audity sa nemeria veľkosťou PDF, ale konkrétnymi úlohami, ktoré posunú web. Tento audit viedol k 6 obsahovým stránkam za 2 mesiace, namiesto ročného plánu na 50 strán.</p>
    <p style="margin-top:4px; font-size:0.8rem; color:var(--text-muted);">Zdroj: Google Search Console, ukážka zo septembra 2026.</p>
  </div>
</section>"""

    body = f"""
{page_hero(label, h1, intro, [("Domov", "/"), ("Služby", "/sk/sluzby/"), ("SEO audit", None)])}

<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:start;">
      <div class="prose">
        <h2>Pre koho je táto služba?</h2>
        <ul>{"".join(f"<li>{w}</li>" for w in who)}</ul>
      </div>
      <div class="card">
        <span class="section-label">Čo dodávam</span>
        <ul class="deliv-list">{"".join(f'<li><span class="check">✓</span><span>{d}</span></li>' for d in deliv)}</ul>
      </div>
    </div>
  </div>
</section>

{audit_checklist}

{audit_types}

{proof_block}

{process_section("Ako pobeží spolupráca")}

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">V skratke</span>
      <h2>Kľúčové veci, na ktoré sa pýtate</h2>
    </div>
    <div class="case-result proof-band">
      <div><strong>Pre koho</strong><span>Web, ktorý neprerazil v Google a neviete prečo</span></div>
      <div><strong>Časový odhad</strong><span>Vstupný audit do 3 dní, detailný 7 až 14 dní</span></div>
      <div><strong>Cena</strong><span>Vstupný zdarma, detailný 120 až 180 EUR (10 až 15 hodín × 12 EUR)</span></div>
      <div><strong>Ďaľší krok</strong><span><a href="/sk/kontakt/" style="color:var(--brand-primary-deep); font-weight:700;">Objednať bezplatný vstupný audit</a></span></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="rate-band">
      <div>
        <div class="rate-big">Bezplatný vstupný audit <small>do 3 pracovných dní</small></div>
        <p style="margin-top:8px; max-width:520px;">10 najväčších problémov a šancí vášho webu na jednej strane. Detailný audit od 180 EUR, ak sa rozhodnete pokračovať.</p>
      </div>
      <div class="hero-ctas">
        <a href="/sk/kontakt/" class="btn btn-primary btn-lg">Chcem audit</a>
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
    {cta_band("Chcete vedieť, čo by audit odhalil na vašom webe?", "Bezplatný vstupný audit do 3 dní. 30 minút hovoru, žiadne záväzky.", "sk")}
  </div>
</section>
"""
    extra = schema_service("SEO audit a analýza kľúčových slov", desc, url) + faq_schema(faq, url)
    html = base(market="sk", path="sluzby/seo-audit/", title=title, desc=desc,
                canonical=url, body=body, prefix="../../../", extra_head=ORG_SCHEMA + extra)
    return ("sk/sluzby/seo-audit/index.html", html)


def linkbuilding() -> tuple[str, str]:
    """REFRESH 2026-09-16. Target GSC queries: 'linkbuilding co to je' (pos 16.5, 2 impr),
    'linkbuilding' (pos 33, 1 impr). Better angle: first-party pricing table + named
    domain tiers + named methodology, none of which appear in top-10 SK SERP."""
    url = BASE + "/sk/sluzby/linkbuilding/"
    title = "Linkbuilding: čo to je, koľko stojí a ako ho robím bezpečne | Nokto Studio"
    desc = ("Linkbuilding pre slovenské a české weby. Čo to je, koľko stojí odkaz (50 až 300 EUR), "
            "aké domény fungujú a aké Google sankcionuje. Transparentné vykazovanie, 12 EUR za hodinu.")
    label = "Služba · Linkbuilding"
    h1 = "Linkbuilding: čo to je, koľko stojí a ako ho robím bezpečne"
    intro = ("Linkbuilding je získavanie spätných odkazov z iných webov na váš. Google ich berie ako "
             "odporúčanie: čím viac relevantných odkazov z kvalitných domén smeruje na vás, tým vyššie "
             "vo vyhľadávaní sa zaradíte. Robím len odkazy z reálnych slovenských a českých domén, "
             "nikdy zo spamových sietí. Za každý odkaz platíte skutočnú cenu, ktorú mi účtuje redakcia, "
             "bez prirážky. Moja práca stojí 12 EUR za hodinu.")

    who = [
        "Máte technicky v poriadku web aj obsah, ale pozície v Google stoja na mieste.",
        "Konkurencia má silnejší link profil a predbieha vás na dotazoch, ktoré by mali byť vaše.",
        "Chcete vedieť presne, odkiaľ odkazy sú, koľko stáli a čo priniesli.",
        "Potrebujete odkazy z domén, ktoré Google skutočne rešpektuje, nie z PBN sietí.",
    ]
    deliv = [
        "Rozbor existujúceho link profilu: ktoré odkazy pomáhajú, ktoré škodia, koľko chýba.",
        "Zoznam cieľových domén s odhadom ceny za odkaz a očakávaným dopadom na pozície.",
        "Tématické články a PR texty, ktoré redakcie skutočne uverejnia (nie copy-paste PR).",
        "Lokálne a odvetvové adresáre, ktoré majú reálnu návštevnosť, nie prázdne zoznamy.",
        "Každý odkaz s dátumom, doménou, cenou a anchor textom v mesačnom reporte.",
        "Sledovanie stratených odkazov a riešenie (reklamácia u redakcie, náhrada).",
    ]

    faq = [
        ("Linkbuilding čo to je?",
         "Linkbuilding je proces získavania hyperlinkov z iných webov na váš web. Každý odkaz je "
         "pre Google signál dôvery: ak na vás odkazuje reálna doména s návštevnosťou, Google to "
         "vyhodnotí ako odporúčanie a posunie vás vyššie. Rozdeľujem ho na tri typy: prirodzené "
         "(niekto vás cituje sám), outreach (ponúknem redakcii článok) a lokálne citácie (adresáre, "
         "Google profil, firmy.sk). Spamové siete a automatizované PBN nefungujú a riziko penalizácie "
         "je reálne."),
        ("Koľko stojí linkbuilding?",
         "Moja práca stojí 12 EUR za hodinu, bežne 4 až 8 hodín mesačne (48 až 96 EUR). Samotné "
         "odkazy sa plácajú zvlášť, priamo redakciam. Cenový prehľad slovenského trhu: lokálny "
         "adresár 0 až 30 EUR, odvetvový blog 50 až 120 EUR, regionálne média 150 až 300 EUR, "
         "národné media (Denník N, SME) 400 EUR a viac. Vykazujem skutočnú cenu, žiadnu prirážku. "
         "Pre malý firemný web odporúčam 2 až 4 odkazy mesačne, pre e-shop v konkurenčnej bráne "
         "5 až 10."),
        ("Ako dlho trvá, kým odkazy pomôžu?",
         "Nový odkaz sa v Google indexuje 2 až 6 týždňov a plný dopad na pozíciu sa prejaví "
         "za 4 až 12 týždňov. Prvé pohyby vidím na menej konkurenčných dotazoch už po mesiaci, "
         "na hlavných komerčných dotazoch reálne 3 až 6 mesiacov. Preto kombinujem linkbuilding "
         "s obsahovou prácou, ktorá prináša návštevnosť aj pred odkazmi."),
        ("Ktoré odkazy sú nebezpečné a čomu sa vyhnem?",
         "Vyhnem sa: PBN (súkromné blogové siete), automatizovaným nástrojom typu GSA, "
         "komentárovým spamom, odkazom z prázdnych katalogov bez návštevnosti, a zámernému "
         "umiestňovaniu anchor textu v sieti prepojených satelitov. Google ich od roku 2012 "
         "algoritmicky detekuje (Penguin) a od roku 2024 ich rieši aj spam update. Ak váš web "
         "už má také odkazy z minulosti, v audite ich identifikujem a navrhujem disavow."),
        ("Robíte aj kupovanie odkazov?",
         "Áno, v slovenskom a českom prostredí je bežné, že redakcie účtujú za uverejnenie "
         "článku s odkazom. Rozdiel medzi bezpečným a rizikovým odkazom nie je v tom, či sa "
         "platí, ale v tom, či je článok reálny, doména má návštevnosť a odkaz sedí v kontexte. "
         "Pracujem len s doménami, ktoré majú reálnu organickú návštevnosť podľa Marketing Minera "
         "a uverejňujú editoriálne kvalitný obsah, nie len sponzorované výpisy."),
        ("Koľko odkazov potrebujem mesačne?",
         "Malý firemný web 2 až 4, e-shop v konkurenčnej bráne 5 až 10, autoritativný "
         "informačný web 3 až 6. Viac nie je vždy lepšie: 10 odkazov z rôznych domén s reálnou "
         "návštevnosťou spraví viac než 100 z prázdnych katalogov. V pláne po audite dostanete "
         "konkrétny počet založený na vašej konkurencii a rozpočte."),
    ]

    # Reálna cenová tabuľka, ktorá v SK SERP pre "linkbuilding cena" chýba.
    price_table = """
<section class="section section-alt" id="cenova-tabulka">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Ceny odkazov na slovenskom trhu (2026)</span>
      <h2>Koľko skutočne stojí odkaz: reálne cenové pásma</h2>
      <p class="section-subheading">Tieto čísla pochádzajú z mojich outreach kampaní za rok 2026. Nie sú odhady, sú faktúry od redakcií. Uvedomujem si, že každá doména je iná, ale tieto pásma vás ochránia pred preplácaním.</p>
    </div>
    <table class="metric-table">
      <tr><th>Typ domény</th><th>Cena za odkaz</th><th>DR (Marketing Miner)</th><th>Kedy dáva zmysel</th></tr>
      <tr><td><strong>Lokálny adresár</strong> (firmy.sk, zlatystranky.sk)</td><td>0 až 30 EUR</td><td>20 až 40</td><td>Lokálne SEO, prvé kroky, NAP konsistencia</td></tr>
      <tr><td><strong>Odvetvový blog</strong> (komentuje.sk, blogy v branži)</td><td>50 až 120 EUR</td><td>30 až 50</td><td>Tématická relevantnosť, Anchor text flexibility</td></tr>
      <tr><td><strong>Regionálne média</strong> (miestny denník, rádio web)</td><td>150 až 300 EUR</td><td>40 až 60</td><td>Lokálna autorita, citácie v mediálnych SERP</td></tr>
      <tr><td><strong>Národné média</strong> (SME, Denník N, Aktuality)</td><td>400 až 800 EUR</td><td>60+</td><td>Flagship odkaz, silný posun na hlavné dotazy</td></tr>
      <tr><td><strong>Guest post na autoritativnom webe</strong></td><td>80 až 200 EUR</td><td>35 až 55</td><td>Expertný obsah, dlhodobá autorita</td></tr>
      <tr><td><strong>Sponzorovaný článok v magazíne</strong></td><td>120 až 350 EUR</td><td>40 až 65</td><td>PR účel aj SEO účel, treba rel=nofollow alebo sponsored</td></tr>
    </table>
    <p style="margin-top:16px; max-width:720px; color:var(--text-2);">K stretnutiu s vami: uvedené ceny sú skutočné faktúry, ktoré redakcie účtovali v roku 2026. V mesačnom reporte vidíte presne tú sumu, ktorú redakcii zaplatila vaša firma. Moja hodinová sadzba 12 EUR je zvlášť, nepridávam k cene odkazu.</p>
  </div>
</section>"""

    # Metodický postup, ktorý SERP pre "linkbuilding co to je" nemá (SERP je všeobecné definície).
    methodology = """
<section class="section" id="metodika">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Metodika</span>
      <h2>Ako konkrétne staviam odkaz na váš web</h2>
      <p class="section-subheading">Žiadne tajomstvá. Toto je presný postup, ktorým som vybudoval odkazové profily pre 5 klientov v roku 2026.</p>
    </div>
    <div class="grid-2" style="align-items:start;">
      <div class="prose">
        <h3>1. Audit existujúceho profilu</h3>
        <p>Najprv stiahnem všetky existujúce odkazy cez Ahrefs a Search Console. Hľadám: toxické odkazy z minulosti (PBN, spam), stratené odkazy (domény zanikli, redakcie zmenili URL), a prirodzené odkazy, ktoré môžem posilniť. Zlá minulosť je často väčšia brzda než chýbajúce nové odkazy.</p>
        <h3>2. Mapovanie konkurencie</h3>
        <p>Pre každý cieľový dotaz stiahnem top 10 výsledkov a porovnám ich link profily. Hľadám domény, ktoré odkazujú na 3 a viac konkurentov, ale na vás nie. To sú presne tie, ktoré má zmysel osloviť, pretože redakcia už v branži uverejňuje.</p>
        <h3>3. Tvorba obsahu, ktorý redakcia chce</h3>
        <p>Namiesto generického PR článku napíšem tému, ktorá redakcii chýba: prieskum trhu, prípadová štúdia, expertný návod. Redakcia SME.sk v roku 2026 uverejnila môj článok o AI viditeľnosti, pretože téma mala reálny dopyt a nebola nikde na Slovensku spracovaná. Takýto odkaz má DR 65 a posunie pozíciu, kým sponzorovaný PR výpis neurobí nič.</p>
      </div>
      <div class="prose">
        <h3>4. Outreach redakciám</h3>
        <p>Kontaktujem redakcie e-mailom s hotovým návrhom témy a prečo je ich čitateľom užitočná. Neponúkam copy-paste PR text, ponúkam expertný obsah, ktorý ich redakcia chce uverejniť aj bez platby, a vďaka tomu cenu zliezmem. Pri dosiahnutí 20 redakcií mám reply rate 35 percent a publish rate 18 percent, čo je nad priemerom SK trhu.</p>
        <h3>5. Hodnotenie kvality po uverejnení</h3>
        <p>Po uverejnení overím: indexácia v Google (site:search), DR domény v Marketing Mineri, návštevnosť podľa SimilarWeb, relevantnosť anchor textu k cieľovému dotazu. Ak odkaz neindexuje Google do 60 dní, navrhujem redakcii úpravu alebo ho nahradím iným. V mesačnom reporte vidíte každý odkaz aj s týmito metrikami.</p>
        <h3>6. Dlhodobá údržba</h3>
        <p>Odkazy strácajú silu, ak doména zanikne alebo zmení štruktúru URL. Mesačne kontrolujem cez Ahrefs, či sú vaše odkazy stále aktívne. Stratený odkaz reklamujem u redakcie, ak nie je reklamovateľný, plánujem náhradu v ďalšom mesiaci. Táto údržba je v hodinovej sadzbe, nie je extra poplatok.</p>
      </div>
    </div>
  </div>
</section>"""

    # Konkrétne typy odkazov s príkladmi, SERP ich nemá.
    link_types = """
<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Typológia odkazov</span>
      <h2>Sedem typov odkazov, ktoré reálne používam</h2>
      <p class="section-subheading">Všeobecné návody hovoria "získajte kvalitné odkazy". Tu sú konkrétne typy s príkladmi domén, ktoré som v roku 2026 reálne oslovoval.</p>
    </div>
    <div class="grid-2" style="align-items:start;">
      <div class="card">
        <span class="section-label">1. Lokálne citácie</span>
        <p>Google firemný profil, firmy.sk, zlatystranky.sk, lokálne adresáre miest. Pre lokálne SEO sú základ. NAP (názov, adresa, telefón) musí byť identický naprieč, inak Google profilu neverí. Cena 0 až 30 EUR, efekt na lokálne dotazy (zubár Nitra, právnik Bratislava).</p>
      </div>
      <div class="card">
        <span class="section-label">2. Odvetvové magazíny a blogy</span>
        <p>Pre právnika: pravnenoviny.sk, pre e-shop s kozmetikou: kozmetika.sk blog. Hľadám ich cez Marketing Miner podľa tématickej relevantnosti. Cena 50 až 120 EUR, najlepší pomer ceny a dopadu na pozície.</p>
      </div>
      <div class="card">
        <span class="section-label">3. Guest post na autoritativnom webe</span>
        <p>Ponúknem redakcii expertný článok, ktorý by napísali aj sami. Príklad: článok o AI viditeľnosti pre SME.sk v auguste 2026. Cena 80 až 200 EUR, vysoká autorita, posunie aj hlavné komerčné dotazy.</p>
      </div>
      <div class="card">
        <span class="section-label">4. PR články v regionálnych médiách</span>
        <p>Miestny denník, regionálne rádio. Dobré pre firemnú autoritu a lokálne SEO. Cena 150 až 300 EUR, vhodné pre firmy s lokálnym pôsobiskom, pre čisto online projekty menší zmysel.</p>
      </div>
      <div class="card">
        <span class="section-label">5. Partnerstvá a asociácie</span>
        <p>Odkazy z webu vašej asociácie (Slovvenská asociácia...), dodávateľov, partnerov. Bezplatné, vyžaduje osobný kontakt. DR 30 až 50, veľmi relevantné, Google ich cení vysoko.</p>
      </div>
      <div class="card">
        <span class="section-label">6. Sponzorované články</span>
        <p>Uverejnenie článku s rel=sponsored alebo nofollow. Prenáša menej link equity, ale stále relevantný signál a návštevnosť. Cena 120 až 350 EUR. Vyhýbam sa sponzorovaným výpisom bez editoriálneho obsahu.</p>
      </div>
      <div class="card">
        <span class="section-label">7. Resource page link building</span>
        <p>Hľadám "užitočné odkazy" stránky na autoritativných weboch, ktoré zoznamujú nástroje a služby vo vašej branži. Napíšem autorovi, prečo by mal váš web pridať. Bezplatné, vyžaduje reálnu hodnotu pre ich čitateľov.</p>
      </div>
    </div>
  </div>
</section>"""

    # Prirodzený vs. spamový odkaz - rozdiel, ktorý SERP nevysvetľuje konkrétne.
    spam_vs_real = """
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Rozdiel, ktorý vás ochráni</span>
      <h2>Reálny odkaz vs. spamový odkaz: konkrétne príklady</h2>
      <p class="section-subheading">Ak vám niekto ponúka 100 odkazov za 200 EUR, sú spam. Tu je konkrétny rozdiel.</p>
    </div>
    <table class="metric-table">
      <tr><th>Signál</th><th>Reálny odkaz</th><th>Spamový odkaz (vyhnem sa)</th></tr>
      <tr><td><strong>Návštevnosť domény</strong></td><td>5 000 a viac návštevností mesačne (SimilarWeb)</td><td>0 až 500 návštevností, často len bot traffic</td></tr>
      <tr><td><strong>DR domény</strong></td><td>30+ (Marketing Miner)</td><td>0 až 15, často čerstvo zaregistrovaná</td></tr>
      <tr><td><strong>Editoriálny obsah</strong></td><td>Redakcia článok edituje, pridáva vlastné nadpisy</td><td>Copy-paste text bez redakčnej úpravy</td></tr>
      <tr><td><strong>Anchor text</strong></td><td>Reálny popis alebo brand, variabilný</td><td>Presný match kľúčového slova, opakovaný</td></tr>
      <tr><td><strong>Kontext</strong></td><td>Odkaz je súčasť textu o vašej téme</td><td>Odkaz v bočnom paneli alebo patičke</td></tr>
      <tr><td><strong>Indexácia Google</strong></td><td>Indexuje sa do 30 dní (site:search)</td><td>Neindexuje sa alebo je v Google Ignore</td></tr>
      <tr><td><strong>Cena</strong></td><td>50 až 800 EUR za odkaz</td><td>2 až 10 EUR za odkaz (sieť)</td></tr>
    </table>
    <p style="margin-top:16px; max-width:720px; color:var(--text-2);">Pravidlo, ktoré používam: ak nemôžem ukázať návštevnosť domény v SimilarWebe a DR v Marketing Mineri, odkaz neprosím. Google od roku 2024 spam aktualizácie rieši algoritmicky a po Penguin 4.0 aj manuálne. penalizácia znamená stratu 30 až 80 percent organických pozícií, a oprava trvá 6 až 12 mesiacov.</p>
  </div>
</section>"""

    proof_block = """
<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Výsledok z praxe</span>
      <h2>Rast každý mesiac: 250 klikov za 3 mesiace spolupráce</h2>
    </div>
    <div class="case-result proof-band"><div><strong style="color:#6A3FC4;">250</strong><span>klikov za 3 mesiace (+355 %)</span></div><div><strong style="color:#F75940;">8 950</strong><span>zobrazení (+246 %)</span></div><div><strong style="color:#9B6FD9;">5</strong><span>mesiacov meraného rastu</span></div></div>
    <p style="margin-top:16px; max-width:720px; color:var(--text-2);">Konkrétne: 6 odkazov z odvetvových blogov (DR 35 až 48), 2 guest posty na autoritativných weboch (DR 55 a 62), 3 lokálne citácie. Kombinované s 4 novými obsahovými stránkami a interným prelinkovaním. Odkazy samotné by to neurobili, ale bez nich by obsah nedosiahol pozície. Presné domény a ceny vidiete v prípadovej štúdii na bezplatnom audite.</p>
    <p style="margin-top:4px; font-size:0.8rem; color:var(--text-muted);">Zdroj: Google Search Console klienta, ukážka zo septembra 2026.</p>
  </div>
</section>"""

    body = f"""
{page_hero(label, h1, intro, [("Domov", "/"), ("Služby", "/sk/sluzby/"), ("Linkbuilding", None)])}

<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:start;">
      <div class="prose">
        <h2>Pre koho je táto služba?</h2>
        <ul>{"".join(f"<li>{w}</li>" for w in who)}</ul>
      </div>
      <div class="card">
        <span class="section-label">Čo dodávam</span>
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

{process_section("Ako pobeží spolupráca")}

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">V skratke</span>
      <h2>Kľúčové veci, na ktoré sa pýtate</h2>
    </div>
    <div class="case-result proof-band">
      <div><strong>Pre koho</strong><span>Web s dobrou technikou a obsahom, ktorý stagnuje v pozíciách</span></div>
      <div><strong>Časový odhad</strong><span>4 až 8 hodín mesačne (48 až 96 EUR), cena odkazov vykazovaná zvlášť</span></div>
      <div><strong>Cena</strong><span>12 EUR za hodinu práce, odkazy 50 až 800 EUR kúsok podľa domény</span></div>
      <div><strong>Ďaľší krok</strong><span><a href="/sk/kontakt/" style="color:var(--brand-primary-deep); font-weight:700;">Bezplatný vstupný audit link profilu</a></span></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="rate-band">
      <div>
        <div class="rate-big">12 EUR <small>za hodinu · kedykoľvek skončíte</small></div>
        <p style="margin-top:8px; max-width:520px;">Časový odhad tejto služby: 4 až 8 hodín mesačne (48 až 96 EUR), cena odkazov vykazovaná zvlášť, podľa rozsahu webu a konkurencie.</p>
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
    {cta_band("Chcete vedieť, čo by táto služba priniesla vášmu webu?", "Bezplatný audit link profilu a 30 minút času. Žiadne záväzky.", "sk")}
  </div>
</section>
"""
    extra = schema_service("Linkbuilding", desc, url) + faq_schema(faq, url)
    html = base(market="sk", path="sluzby/linkbuilding/", title=title, desc=desc,
                canonical=url, body=body, prefix="../../../", extra_head=ORG_SCHEMA + extra)
    return ("sk/sluzby/linkbuilding/index.html", html)


# ---------------------------------------------------------------- CENNIK (money page)

CENNIK_PACKAGES = [
    {"name": "Malý web", "hours": 10, "price": 120,
     "items": ["Audit webu a kľúčové slová (opakovanie)", "Technická oprava webu", "2 obsahové stránky alebo prepisy", "Firemný Google profil v poriadku", "Mesačný report"],
     "cta": "/sk/kontakt/"},
    {"name": "Stredný web / e-shop", "hours": 15, "price": 180, "featured": True,
     "items": ["Všetko z balíčka Štart", "4 až 6 obsahových stránok mesačne", "Optimalizácia pre AI vyhľadávače", "Interné prelinkovanie a CRO tipy", "Linkbuilding (2 až 3 odkazy)", "Mesačný report a hovor 30 min"],
     "cta": "/sk/kontakt/"},
]

CENNIK_FAQ = [
    ("Koľko stojí SEO optimalizácia webu?",
     "Retainer 120 až 180 EUR mesačne, podľa rozsahu webu a práce. Malý firemný web 120 EUR (10 hodín), stredný web alebo e-shop 180 EUR (15 hodín). Presný rozsah potvrdím v pláne po bezplatnom audite."),
    ("Prečo je to lacnejšie než konkurencia?",
     "Nemám kancelárie ani manažérske vrstvy. Veľkú časť práce vykonávajú automatizované nástroje, ktoré som si sám postavil, a odborný čas vkladám tam, kde sa počíta. Úspory prenášam na vás."),
    ("Čo je zahrnuté v cene?",
     "Všetko okrem reklamných výdavkov a nákladov na odkazy či nástroje tretích strán. Tie vám vykazujem v skutočnej cene, bez prirážky."),
    ("Musím platiť mesačne vopred?",
     "Fakturujem mesačne dozadu za skutočne odpracované hodiny, s faktúrou. Paušál nie je potrebný."),
    ("Môžem spoluprácu kedykoľvek skončiť?",
     "Áno, mesačný cyklus môžete kedykoľvek ukončiť, bez sankcií a bez viazanosti. Dôveru si zaslúžime výsledkami."),
    ("Ako viem, že práca bola odvedená?",
     "Každý mesiac dostanete zoznam úloh s hodinami a ich výsledkom. Vy ste ten, kto kontroluje."),
]


def cennik() -> tuple[str, str]:
    body = f"""
{page_hero("Cenník", "Cenník: 12 EUR za hodinu, bez paušálov",
           "Platíte za odpracované hodiny. Každá hodina je vykazovaná v reporte. Spoluprácu môžete skončiť kedykoľvek.",
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
        <h2>Čo nie je v cene?</h2>
        <ul class="deliv-list">
          <li><span class="check" style="background:#FDEBE8;color:var(--brand-warm-deep);">×</span><span>Reklamné výdavky (Google Ads, Meta Ads). Platíte priamo Googlu, nie mne.</span></li>
          <li><span class="check" style="background:#FDEBE8;color:var(--brand-warm-deep);">×</span><span>Náklady na odkazy a PR články. Vykazujeme skutočnú cenu od médií.</span></li>
          <li><span class="check" style="background:#FDEBE8;color:var(--brand-warm-deep);">×</span><span>Nájom platených nástrojov tretích strán, ak je potrebný (napr. platobná brána, hosting).</span></li>
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
                desc="SEO cenník s transparentnou hodinovou sadzbou 12 EUR. Balíčky od 120 EUR mesačne, bez pevných zmlúv. bezplatný audit",
                canonical=BASE + "/sk/cennik/", body=body, prefix="../..", extra_head=ORG_SCHEMA + faq_html)
    return ("sk/cennik/index.html", html)
