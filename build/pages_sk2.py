# -*- coding: utf-8 -*-
"""Nokto Studio - SK supporting pages."""
from engine import (base, page_hero, cta_band, faq_block, faq_schema,
                    steps_block, ORG_SCHEMA, CAL, EMAIL, BASE, gicon)

# ---------------------------------------------------------------- JAK PRACUJEME

def jak_pracujeme() -> tuple[str, str]:
    body = f"""
{page_hero("Proces", "Ako pracujeme: plán, práca, meranie",
           "Jasný proces bez čiernej skrinky. Viete, čo robíme, prečo a čo to prinieslo. Platíte za hodiny, ktoré sú vykazované.",
           [("Domov", "/"), ("Ako pracujeme", None)])}

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Proces</span>
      <h2>Od prvého hovoru po mesačný hovor so mnou</h2>
    </div>
    {steps_block([
        {"title": "1. Bezplatný hovor a audit", "text": "30 minút telefonátu, v ktorom si povieme ciele. Do 3 dní od neho dostanete bezplatný vstupný audit: 10 najväčších problémov a šancí vášho webu na jednej strane."},
        {"title": "2. Plán s číslami", "text": "Z auditu spravíme plán: ktoré kľúčové slová prinášajú zákazníkov, čo opraviť ako prvé, koľko hodín mesačne to zaberie a aké výsledky sú reálne. Bez nereálnych sľubov."},
        {"title": "3. Práca v týždenných dávkach", "text": "Každý týždeň odpracujeme dohodnutý rozsah: technika, obsah, Google profil, AI viditeľnosť, odkazy. Každú zmenu viete dohľadať."},
        {"title": "4. Meranie a report", "text": "Mesačný report vám dám osobne ako 30-minútový telefónát: čo sa odrobilo, čo to prinieslo (pozície, kliky, objednávky, zmienky v AI) a čo je ďalší krok."},
    ])}
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Dodávky</span>
      <h2>Čo presne dostanete každý mesiac</h2>
    </div>
    <div class="grid-2" style="align-items:start;">
      <div class="card">
        <span class="section-label">Práca</span>
        <ul class="deliv-list">
          <li><span class="check">✓</span><span>Technická údržba webu: rýchlosť, indexácia, opravy chýb.</span></li>
          <li><span class="check">✓</span><span>Obsahové stránky písané na reálne dopyty zákazníkov.</span></li>
          <li><span class="check">✓</span><span>Firemný Google profil: dáta, fotky, hodnotenia, Q&amp;A.</span></li>
          <li><span class="check">✓</span><span>Optimalizácia pre ChatGPT, Gemini a AI Overviews.</span></li>
          <li><span class="check">✓</span><span>Linkbuilding podľa dohody (cena odkazov vykazovaná zvlášť).</span></li>
        </ul>
      </div>
      <div class="card">
        <span class="section-label">Meranie</span>
        <ul class="deliv-list">
          <li><span class="check">✓</span><span>Pozície na sledovaných kľúčových slovách (trend, nie len číslo).</span></li>
          <li><span class="check">✓</span><span>Kliky a zobrazenia z Google (Search Console).</span></li>
          <li><span class="check">✓</span><span>Kontakty a objednávky (Google Analytics).</span></li>
          <li><span class="check">✓</span><span>Zobrazenia v Google Mapách: volania, trasy, recenzie.</span></li>
          <li><span class="check">✓</span><span>Zmienky v AI odpovediach (ChatGPT, Gemini, AI Overviews).</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Meranie</span>
      <h2>Ako meriame výsledky</h2>
      <p class="section-subheading">Nič nemeníme názormi. Každé tvrdenie má v reporte číslo a zdroj dáto.</p>
    </div>
    <table class="metric-table">
      <tr><th>Čo sledujeme</th><th>Nástroj</th><th>Čo to hovorí</th></tr>
      <tr><td><strong>Pozície</strong></td><td>Sledovanie kľúčových slov</td><td>Na ktorých dopytoch rastieme a kde sme uviazli.</td></tr>
      <tr><td><strong>Kliky z Google</strong></td><td>Search Console</td><td>Koľko ľudí nás vidí a koľko z nich klikne.</td></tr>
      <tr><td><strong>Kontakty a objednávky</strong></td><td>Google Analytics 4</td><td>Koľko návštevníkov sa stalo zákazníkmi.</td></tr>
      <tr><td><strong>Viditeľnosť v mápe</strong></td><td>Firemný profil Google</td><td>Koľko ľudí videlo firmu, zatelefonovalo, išlo na trasu.</td></tr>
      <tr><td><strong>AI odporúčania</strong></td><td>Pravidelné AI testy</td><td>Či vás ChatGPT, Gemini a AI Overviews citujú.</td></tr>
      <tr><td><strong>Tržby z organika</strong></td><td>Analytics + e-shop</td><td>Pre e-shopy: priamy vzťah SEO úsilia k predaju.</td></tr>
    </table>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    {cta_band("Chcete takýto proces pre svoj web?", "Začnite bezplatným auditom a 30 minútami času.", "sk")}
  </div>
</section>
"""
    html = base(market="sk", path="jak-pracujeme/", title="Ako pracujeme: proces, dodávky a meranie výsledkov | Nokto Studio",
                desc="Náš SEO proces: bezplatný audit, plán s číslami, týždenná práca, mesačné meranie. Pozície, kliky, objednávky a AI odporúčania v jednom reporte.",
                canonical=BASE + "/sk/jak-pracujeme/", body=body, prefix="../..", extra_head=ORG_SCHEMA)
    return ("sk/jak-pracujeme/index.html", html)


# ---------------------------------------------------------------- PRIPADY

def pripady() -> tuple[str, str]:
    body = f"""
{page_hero("Prípadové štúdie", "Príklady práce, nie chvály samé",
           "Klienti, s ktorými sme pracovali, a to, čo sme pre nich stavali. Čísla dopĺňame podľa dohody s klientom.",
           [("Domov", "/"), ("Prípady", None)])}

<section class="section">
  <div class="container">
    <div class="grid-2">
      <div class="project-card card-hover">
        <div class="project-card-body">
          <h3>Villa Paris, Piešťany</h3>
          <p>Prémiové ubytovanie. Rebrand, nový web, hotelový copywriting a lokálne SEO v jednom systéme. Cieľ: viac priamych rezervácií bez provízií.</p>
          <div class="project-tags">
            <span class="project-tag tag-blue">Branding</span>
            <span class="project-tag tag-green">Web</span>
            <span class="project-tag tag-red">Lokálne SEO</span>
          </div>
          <a href="/sk/villa-paris/" class="btn btn-outline" style="margin-top:20px;">Čítať príbeh</a>
        </div>
      </div>
      <div class="project-card card-hover">
        <div class="project-card-body">
          <h3>Mikramt.sk, Martin</h3>
          <p>Vlastný e-shop s API integráciou na účtovný systém Sunsoft Ecosun pre regionálneho dodávateľa stolárskych potrieb. Za 9 mesiacov 2 492,75 EUR online tržieb z 15 objednávok (email + organický Google), najväčšia objednávka 722 EUR. Email marketing, lokálne SEO a GEO optimalizácia. Predaj v kamennej predajni do sumy nerátame.</p>
          <div class="case-result">
            <div><strong>2 492,75 EUR</strong><span>tržby / 9 mesiacov</span></div>
            <div><strong>15</strong><span>objednávok online</span></div>
          </div>
          <div class="project-tags">
            <span class="project-tag tag-yellow">E-shop SEO</span>
            <span class="project-tag tag-green">Email marketing</span>
            <span class="project-tag tag-red">Lokálne SEO + GEO</span>
          </div>
          <a href="{CAL}" target="_blank" rel="noopener noreferrer" class="btn btn-outline" style="margin-top:20px;">Povedať si viac</a>
        </div>
      </div>
    </div>
    <p style="text-align:center; margin-top:28px; color:var(--text-muted); font-size:0.9rem;">
      Ďalšie prípady a referencie na žiadosť, vrátane kontaktov na klientov. Klientov citujeme len s ich súhlasom.
    </p>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    {cta_band("Vaša firma môže byť ďalší príbeh", "Začnime bezplatným auditom. Vidíte, čo by sme u vás riešili, ešte pred prvou faktúrou.", "sk")}
  </div>
</section>
"""
    html = base(market="sk", path="pripady/", title="Prípadové štúdie SEO a tvorby webov | Nokto Studio",
                desc="Prípadové štúdie Nokto Studio: Villa Paris Piešťany (rebrand, web, lokálne SEO), e-shop SEO a ďalšie projekty.",
                canonical=BASE + "/sk/pripady/", body=body, prefix="../..", extra_head=ORG_SCHEMA)
    return ("sk/pripady/index.html", html)


# ---------------------------------------------------------------- VILLA PARIS (case study)

def villa_paris() -> tuple[str, str]:
    body = f"""
{page_hero("Prípadová štúdia · Branding &amp; Web", "Villa Paris: značka a web od nuly",
           "Prémiové ubytovanie v Piešťanoch malo skvelý produkt. Chýbala mu značka. Vyriešili sme to identitou, webom, copywritingom a lokálnym SEO ako jedným systémom.",
           [("Domov", "/"), ("Prípady", "/sk/pripady/"), ("Villa Paris", None)])}

<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:start;">
      <div class="prose">
        <span class="section-label">Problém</span>
        <h2 style="margin-top:8px;">Skvelá lokalita. Nulová prezentácia.</h2>
        <p>Villa Paris ponúka skutočnú hodnotu: pokojné prostredie v Piešťanoch, blízkosť kúpeľného centra aj ADELI Medical Center, pohodlné izby a rodinnú atmosféru. Vizuálna identita a digitálna prítomnosť však túto hodnotu nekomunikovali.</p>
        <p>Potenciálni hostia prichádzali na web a nedokázali rýchlo pochopiť, čo robí ubytovanie hodným rezervácie. Značka pôsobila genericky, texty neodpovedali na otázky, ktoré si ľudia kladú pred rezerváciou. Rezervácie sa strácali skôr, ako sa vôbec začal rozhovor.</p>
        <h2>Riešenie: jeden systém, štyri oblasti</h2>
        <h3>Redesign brand identity</h3>
        <p>Nový vizuálny systém: logo, farebná paleta, typografia. Postavené tak, aby značka pôsobila teplým, prémiovým a okamžite rozpoznateľným dojmom.</p>
        <h3>Rebuild webu</h3>
        <p>Prepracovaná štruktúra s dôrazom na prehľadnosť a konverziu rezervácií od prvého scrollovania. Rýchle načítanie, jednoduchá cesta k rezervácii, mobilná skúsenosť ako priorita.</p>
        <h3>Hotelový copywriting</h3>
        <p>Texty orientované na hosťa, ktoré odpovedajú na skutočné otázky pred rezerváciou: lokalita, komfort, čo očakávať po príchode.</p>
        <h3>Lokálne SEO</h3>
        <p>Firemný profil Google v poriadku, lokálne kľúčové slová pre Piešťany a kúpeľné hostiteľstvo, tak aby Villa Paris našli hostia, ktorí hľadajú presne toto ubytovanie.</p>
      </div>
      <div class="card">
        <span class="section-label">Rozsah projektu</span>
        <ul class="deliv-list">
          <li><span class="check">✓</span><span>Redesign značky: logo, farby, typografia.</span></li>
          <li><span class="check">✓</span><span>Nový web: štruktúra, dizajn, rýchlosť.</span></li>
          <li><span class="check">✓</span><span>Hotelový copywriting orientovaný na hosťa.</span></li>
          <li><span class="check">✓</span><span>Lokálne SEO: firemný profil Google, lokálne dopyty.</span></li>
          <li><span class="check">✓</span><span>Meranie: rezervácie a ich zdroje.</span></li>
        </ul>
        <div style="margin-top:22px;">
          <a href="{CAL}" target="_blank" rel="noopener noreferrer" class="btn btn-primary">Chcem podobný projekt</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    {cta_band("Chcete postaviť značku a web, ktoré predávajú?", "Bezplatný audit a 30 minút času. Bez záväzkov.", "sk")}
  </div>
</section>
"""
    html = base(market="sk", path="villa-paris/", title="Villa Paris, Piešťany: rebrand, web a lokálne SEO | Nokto Studio",
                desc="Prípadová štúdia: ako Nokto Studio postavilo Villa Paris od základov. Brand identita, nový web, hotelový copywriting a lokálne SEO pre prémiové ubytovanie v Piešťanoch.",
                canonical=BASE + "/sk/villa-paris/", body=body, prefix="../..", extra_head=ORG_SCHEMA)
    return ("sk/villa-paris/index.html", html)


# ---------------------------------------------------------------- FAQ

FAQ_SECTIONS = [
    ("Všeobecné", [
        ("Čo presne Nokto Studio robí?",
         "SEO optimalizáciu webu, lokálne SEO a firemný profil Google, optimalizáciu pre AI vyhľadávače (ChatGPT, Gemini, AI Overviews), SEO pre e-shopy, SEO audity, linkbuilding, tvorbu webov a PPC reklamu Google Ads. K tomu email marketing pre e-shopy a firmy."),
        ("Pre aké firmy pracujete?",
         "Predovšetkým pre menšie a stredné firmy: lokálne služby (remeselníci, zdravotníctvo, právo, auto-servis), e-shopy a firmy, ktoré ponúkajú odborné služby. Pracujeme na trhoch Slovenska a Česka."),
        ("S akými platformami pracujete?",
         "WordPress, Shoptet, WooCommerce a vlastné riešenia. Pri SEO má nástroj druhoradú rolu, dôležitá je stratégia a jej vykonávanie."),
    ]),
    ("Cena a zmluvy", [
        ("Koľko stojí SEO?",
         "12 EUR za odpracovanú hodinu. Malý firemný web zvyčajne 10 hodín mesačne (120 EUR), e-shop 20 až 40 hodín (240 až 480 EUR). Balíčky sú odporúčané rozsahy, nie povinné paušály."),
        ("Sú zmluvy viažúce?",
         "Nie. Spoluprácu môžete skončiť kedykoľvek, bez sankcií. Fakturujeme mesačne za skutočne odpracované hodiny."),
        ("Čo ak potrebujem viac hodín v jednom mesiaci?",
         "Nič sa nemení, pracujete len viac hodín. Rozsah sa dohodne v pláne a môžete ho kedykoľvek zmeniť."),
        ("Sú v cene zahrnuté reklamné výdavky?",
         "Nie. Reklamu (Google Ads) platíte priamo Google. My riadime kampane za 12 EUR za hodinu. Náklady na odkazy a PR vykazujeme v skutočnej cene."),
    ]),
    ("Proces a výsledky", [
        ("Ako dlho trvá, kým SEO prinesie výsledky?",
         "Prvé pohyby na menej konkurenčných dotazoch za 2 až 4 mesiace, na hlavné dotazy 6 až 12 mesiacov. Lokálne SEO a Google profil sa zlepšujú častejšie za 4 až 8 týždňov. Presné termíny vami povieme v audite."),
        ("Ako budem vidieť, že práca sa odviedla?",
         "Mesačný report osobne: 30-minútový hovor so mnou. Odpracované hodiny, pozície, kliky z Search Console, objednávky z Analytics, viditeľnosť v Mapách a zmienky v AI."),
        ("Ponúkate záruky prvej pozície?",
         "Nie. Nikto reálne nevie zaručiť prvé miesto v Google, kto to sľubuje, predáva fiktívne záruky. Zaručujeme proces, transparentnosť a merateľný postup, ktorý k pozíciám vedie."),
        ("Pomôžete aj s prestávkou alebo migráciou webu?",
         "Áno, migrácia webu je jedna z úloh, kde sa ľahko strácajú pozície. Vieme, čo robiť, aby sa to nestalo."),
    ]),
    ("AI a nové vyhľadávanie", [
        ("Je to pravda, že ChatGPT nahradí Google?",
         "Nahradí ho, ale nie zničí. Zákazníci dnes vyhľadávajú oboje. Naša práca pokrýva obe: klasické Google pozície aj viditeľnosť v AI odpovediach."),
        ("Ako zistím, či ma AI odporúča?",
         "Pravidelne testujeme súbory dotazov, ktoré vaši zákazníci pýtajú, a zaznamenávame, či sa vaše meno objavuje v odpovediach ChatGPT, Gemini a Google AI Overviews. Zaznamenáme to v mesačnom reporte."),
        ("Prečo je táto špecializácia zriedkavá?",
         "Optimalizácia pre AI je nová odborná práca, ktorá si vyžaduje inú metódu obsahu a štruktúry dát. Väčšina agentúr na Slovensku sa na ňu zatiaľ nepripravuje, čo je výhoda klientov, ktorí začnú prví."),
    ]),
]


def faq() -> tuple[str, str]:
    sections_html = ""
    all_qa = []
    for sec_title, qas in FAQ_SECTIONS:
        qas_html = "".join(
            f'<div class="faq-item"><button class="faq-question" type="button">{q}</button>'
            f'<div class="faq-answer"><p>{a}</p></div></div>' for q, a in qas
        )
        sections_html += f'<h2 style="margin-top:36px;">{sec_title}</h2>{qas_html}'
        all_qa += qas
    body = f"""
{page_hero("FAQ", "Časté otázky", "Odpovede na to, čo nás klienti pýtajú najviac. Ak chýba vaša otázka, pýtajte priamo.", [("Domov", "/"), ("FAQ", None)])}
<section class="section">
  <div class="container" style="max-width:800px;">
    {sections_html}
  </div>
</section>
<section class="section" style="padding-top:0;">
  <div class="container">
    {cta_band("Chýba vám otázka?", "Napíšte alebo zavolajte. Bez záväzkov.", "sk")}
  </div>
</section>
"""
    faq_html = faq_schema(all_qa, BASE + "/sk/faq/")
    html = base(market="sk", path="faq/", title="FAQ: časté otázky k SEO, cene a procesu | Nokto Studio",
                desc="Časté otázky: koľko stojí SEO, ako dlho trvá, ako meriame výsledky, čo je SEO pre AI vyhľadávače. Nokto Studio, SEO agentúra.",
                canonical=BASE + "/sk/faq/", body=body, prefix="../..", extra_head=ORG_SCHEMA + faq_html)
    return ("sk/faq/index.html", html)


# ---------------------------------------------------------------- O NAS

def o_nas() -> tuple[str, str]:
    body = f"""
{page_hero("O nás", "Pracujeme v tieni.<br>Výsledky hovoria na svetle.",
           "Nokto Studio je SEO agentúra jedného človeka s tímom spolupracovníkov. Pracujeme pre podnikateľov, ktorí chcú merateľný rast, nie marketingové tance.",
           [("Domov", "/"), ("O nás", None)])}
<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:center;">
      <div class="prose">
        <h2>Kto za Nokto stojí</h2>
        <p>Volám sa Simon a Nokto Studio je moje projekt. Za sebou mám roky práce na SEO a weboch pre slovenské aj zahraničné klienty: e-shopy, lokálne firmy, média aj prémiové značky. Postavil som automatizované systémy, ktoré z SEO práce vyrábajú presne to, čo firma potrebuje: zákazníkov.</p>
        <p>Nie som veľká agentúra a nepredstieram to. Výhodou je, že s vami pracuje ten istý človek, ktorý navrhol stratégiu. Žiadne preposielanie medzi oddeleniami, žiadne strácanie kontextu.</p>
        <h2>Ako pracujeme</h2>
        <p>Kombinujeme dva svety: odbornú SEO prácu (technika, obsah, autorita, AI viditeľnosť) a automatizáciu, ktorá z rovnakého úsilia vytiahne viac. Preto vieme pracovať za 12 EUR za hodinu a stále sa sústrediť na výsledok, nie na fakturovanie hodín na okraji.</p>
      </div>
      <div>
        <img src="/assets/img/simon.png" alt="Simon, zakladateľ Nokto Studio" loading="lazy" style="border-radius:var(--radius-lg); border:1px solid var(--border-light);">
        <p style="text-align:center; margin-top:12px; font-size:0.85rem; color:var(--text-muted);">Simon, zakladateľ Nokto Studio</p>
      </div>
    </div>
  </div>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Hodnoty</span>
      <h2>Tri pravidlá, ktoré platia vždy</h2>
    </div>
    <div class="grid-3">
      <div class="benefit-card"><span class="benefit-icon">{gicon("shield", "#1A73E8", 26)}</span><h3>Žiadne sľuby, ktoré nedržia</h3><p>Prvú pozíciu v Google nevie zaručiť nikto. Čo zaručíme: transparentný proces, reálne termíny a merateľný postup.</p></div>
      <div class="benefit-card"><span class="benefit-icon">{gicon("chart", "#EA4335", 26)}</span><h3>Mesačný report so mnou</h3><p>30-minútový telefónát: čo sme spravili, čo to prinieslo a čo ide dalej. Bez preposielania.</p></div>
      <div class="benefit-card"><span class="benefit-icon">{gicon("check", "#34A853", 26)}</span><h3>Každá hodina vykazovaná</h3><p>Platíte za odvedenú prácu. Každá hodina je v reporte s jej obsahom a výsledkom.</p></div>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0;">
  <div class="container">
    {cta_band("Spoznajme sa 30 minút", "Bezplatný hovor o vašich cieľoch. Ak sa nespárujeme, povieme vám to čelom.", "sk")}
  </div>
</section>
"""
    html = base(market="sk", path="o-nas/", title="O nás: SEO agentúra Nokto Studio | Simon a tím",
                desc="Nokto Studio: SEO agentúra pre podnikateľov. Kto za nami stojí, ako pracujeme a prečo 12 EUR za hodinu stačí na merateľné výsledky.",
                canonical=BASE + "/sk/o-nas/", body=body, prefix="../..", extra_head=ORG_SCHEMA)
    return ("sk/o-nas/index.html", html)


# ---------------------------------------------------------------- KONTAKT

def kontakt() -> tuple[str, str]:
    body = f"""
{page_hero("Kontakt", "Napíšte. Ozveme sa osobne.",
           "Najrýchlejšia cesta je bezplatný hovor cez kalendár. Ak uprednostníte formulár, využite ho nižšie.",
           [("Domov", "/"), ("Kontakt", None)])}
<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:start;">
      <div class="card">
        <span class="section-label">Bezplatný hovor 30 minút</span>
        <p style="margin:14px 0 22px;">Vyberte si termín priamo v kalendári. Preberieme ciele vašej firmy a na mieste povieme, čo by sme robili prví. Žiadne tlak, žiadne záväzky.</p>
        <a href="{CAL}" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg" style="width:100%;">Otvoriť kalendár</a>
        <ul class="deliv-list" style="margin-top:24px;">
          <li><span class="check">✓</span><span>Bezplatný vstupný audit webu po hovore</span></li>
          <li><span class="check">✓</span><span>Reálne čísla: čo by SEO mohlo u vás znamenať</span></li>
          <li><span class="check">✓</span><span>Nezáväzné. Rozhodnete sa, kedy a či.</span></li>
        </ul>
      </div>
      <div class="card contact-form-wrap">
        <span class="section-label">Alebo formulár</span>
        <form class="contact-form-el" style="margin-top:16px;">
          <div class="form-grid">
            <div class="form-field"><label class="form-label" for="name">Meno a firma *</label><input class="form-input" id="name" name="name" type="text" required></div>
            <div class="form-field"><label class="form-label" for="email">Email *</label><input class="form-input" id="email" name="email" type="email" required></div>
            <div class="form-field full"><label class="form-label" for="url">Adresa webu (ak máte)</label><input class="form-input" id="url" name="url" type="url" placeholder="https://"></div>
            <div class="form-field full"><label class="form-label" for="goal">Čo je váš cieľ? *</label>
              <select class="form-select" id="goal" name="goal" required>
                <option value="">Vyberte...</option>
                <option>Viac zákazníkov z Google</option>
                <option>Lepšia viditeľnosť na Google Mapách</option>
                <option>Odporúčania v ChatGPT / AI</option>
                <option>Viac predaja na e-shope</option>
                <option>Nový web alebo redesign</option>
                <option>Niečo iné</option>
              </select>
            </div>
            <div class="form-field full"><label class="form-label" for="msg">Správa</label><textarea class="form-textarea" id="msg" name="msg" placeholder="Pár slov o vašej firme a čo by ste chceli dosiahnuť."></textarea></div>
          </div>
          <button type="submit" class="btn btn-primary" style="margin-top:18px; width:100%;">Poslať správu</button>
          <p class="form-note">Odoslaním súhlasíte so spracovaním údajov pre účel odpovede (pozrite <a href="/sk/privacy/">ochranu súkromia</a>).</p>
        </form>
        <div class="form-success" style="display:none; margin-top:16px; background:#E6F4EA; color:var(--g-green-deep); padding:16px; border-radius:10px;">
          ✓ Ďakujeme. Ozveme sa osobne.
        </div>
        <p style="margin-top:20px;">Alebo email: <a href="mailto:{EMAIL}">{EMAIL}</a> · telefonujte: <a href="tel:+421917316105" style="font-weight:700; color:var(--text); text-decoration:none;">+421 917 316 105</a></p>
      </div>
    </div>
  </div>
</section>
"""
    html = base(market="sk", path="kontakt/", title="Kontakt: bezplatný hovor a audit | Nokto Studio",
                desc="Spojte sa s Nokto Studio. Bezplatný strategický hovor 30 minút a bezplatný vstupný audit webu.",
                canonical=BASE + "/sk/kontakt/", body=body, prefix="../..", extra_head=ORG_SCHEMA)
    return ("sk/kontakt/index.html", html)


# ---------------------------------------------------------------- BLOG (stub with planned topics)

def blog() -> tuple[str, str]:
    topics = [
        ("Ako vybrať SEO agentúru (a na čo si dať pozor)", "Cenník, záruky, reporty. 8 otázok, ktoré treba položiť pred podpisom.", "tag-blue"),
        ("Koľko stojí SEO optimalizácia webu v 2026?", "Prehľad cien na slovenskom trhu a prečo platíme paušálmi za prácu, ktorá sa neodviedza.", "tag-yellow"),
        ("Ako sa dostať do odporúčaní ChatGPT", "Prvá príručka pre slovenské firmy: ako AI nástroje vyberajú, koho odporučiť.", "tag-green"),
        ("Google firemný profil: kompletný návod pre firmy", "Od založenia po hodnotenia. Čo Google ocení a čo ignoruje.", "tag-red"),
    ]
    cards = "".join(f"""
<div class="benefit-card card-hover">
  <span class="project-tag {tag}">Článok v príprave</span>
  <h3 style="margin-top:12px;">{t}</h3>
  <p>{d}</p>
</div>""" for t, d, tag in topics)
    body = f"""
{page_hero("Blog", "Praktické články o SEO a AI",
           "Píšeme, čo vieme overiť v praxi. Prvé články vychádzajú tento mesiac.", [("Domov", "/"), ("Blog", None)])}
<section class="section">
  <div class="container">
    <div class="grid-2">{cards}</div>
    <div style="text-align:center; margin-top:36px;">
      <p style="color:var(--text-muted);">Chcete o niečom vedieť viac už teraz? Spýtajte sa priamo, radi poradíme aj bez zmluvy.</p>
      <a href="{CAL}" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="margin-top:14px;">Bezplatný hovor</a>
    </div>
  </div>
</section>
"""
    html = base(market="sk", path="blog/", title="Blog o SEO, Google Mapách a AI vyhľadávačoch | Nokto Studio",
                desc="Praktické články: ako vybrať SEO agentúru, koľko stojí SEO, ako sa dostať do odporúčaní ChatGPT, Google firemný profil od základov.",
                canonical=BASE + "/sk/blog/", body=body, prefix="../..", extra_head=ORG_SCHEMA)
    return ("sk/blog/index.html", html)


# ---------------------------------------------------------------- SK ROOT REDIRECT STUB

def sk_redirect() -> tuple[str, str]:
    html = """<!DOCTYPE html>
<html lang="sk">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="noindex, follow">
  <title>Nokto Studio | SEO agentúra</title>
  <link rel="canonical" href="https://noktostudio.com/">
  <meta http-equiv="refresh" content="0; url=/">
</head>
<body>
<p>Pokračujte na <a href="/">noktostudio.com</a>.</p>
</body>
</html>
"""
    return ("sk/index.html", html)


# ---------------------------------------------------------------- SK LEGAL

def sk_privacy() -> tuple[str, str]:
    body = f"""
{page_hero("Súkromie", "Zásady ochrany súkromia",
           "Spracovávame len dáta, ktoré potrebujeme na odpoveď a spoluprácu. Žiadny predaj dát tretím stranám.",
           [("Domov", "/"), ("Ochrana súkromia", None)])}
<section class="section">
  <div class="container prose">
    <h2>Kto spracováva údaje</h2>
    <p>Operátorom osobných údajov je Nokto Studio (Simon, prevádzkovateľ webu noktostudio.com). Kontakt: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    <h2>Aké údaje a načo</h2>
    <ul>
      <li>Kontaktný formulár: meno, email, adresa webu a správa. Účelom je odpovedať na váš dotaz.</li>
      <li>Kalendár (Calendly): meno, email a termín hovoru. Účelom je uskutočniť hovor.</li>
      <li>Analitika: anonymizované dáta o návštevnosti (Google Analytics 4, Microsoft Clarity) na zlepšovanie webu.</li>
    </ul>
    <h2>Ako dlho údaje uchovávame</h2>
    <p>Kontakty z formulárov a kalendára uchovávame maximálne 24 mesiacov od poslednej komunikácie, pokiaľ nevznikne spolupráca.</p>
    <h2>Vaše práva</h2>
    <p>Máte právo na prístup k údajom, ich opravu, výmaz a prenos. Požiadavku pošlite na <a href="mailto:{EMAIL}">{EMAIL}</a>. Máte tiež právo podať sťažnosť u Úradu na ochranu osobných údajov SR.</p>
    <h2>Cookies</h2>
    <p>Web používa analytické cookies po vašom súhlase (cookie banner). Technické cookies nevyhnutné pre prevádzku webu sú povolené vždy.</p>
  </div>
</section>
"""
    html = base(market="sk", path="privacy/", title="Zásady ochrany súkromia | Nokto Studio",
                desc="Zásady ochrany súkromia webu noktostudio.com: aké údaje spracovávame, načo a aké máte práva.",
                canonical=BASE + "/sk/privacy/", body=body, prefix="../..", extra_head=ORG_SCHEMA)
    return ("sk/privacy/index.html", html)


def sk_terms() -> tuple[str, str]:
    body = f"""
{page_hero("Podmienky", "Obchodné podmienky",
           "Jednoduché podmienky bez právnickej španielčiny: hodinová sadzba, mesačná fakturácia, bez viazanosti.",
           [("Domov", "/"), ("Obchodné podmienky", None)])}
<section class="section">
  <div class="container prose">
    <h2>1. Predmet</h2>
    <p>Tieto podmienky upravujú spoluprácu medzi Nokto Studio (ďalej „poskytovateľ") a klientom pri poskytovaní marketingových služieb: SEO optimalizácia, tvorba webov, PPC kampane, email marketing a súvisiace poradenstvo.</p>
    <h2>2. Cena a fakturácia</h2>
    <p>Služby sa účtujú hodinovou sadzbou 12 EUR za odpracovanú hodinu. Fakturácia prebieha mesačne dozadu na základe reportu odpracovaných hodín. Reklamné výdavky a náklady na odkazy či nástroje tretích strán sa účtujú v skutočnej cene bez prirážky.</p>
    <h2>3. Doba spolupráce</h2>
    <p>Spolupráca je dohodnutá na dobu neurčitú s mesačným cyklom. Klient aj poskytovateľ môžu spoluprácu ukončiť ku koncu kalendárneho mesiaca, písomne, bez sankcií.</p>
    <h2>4. Zodpovednosť a výsledky</h2>
    <p>Poskytovateľ nezaručuje konkrétne pozície vo vyhľadávačoch ani konkrétne objemy návštevnosti. Zaručuje odvedenú prácu, transparentné vykazovanie a postup podľa dohodnutého plánu. Záruky konkrétnych pozícií nie sú možné a ani nie sú poskytované.</p>
    <h2>5. Práva k obsahu</h2>
    <p>Obsah vytvorený pre klienta v rámci platenej spolupráce prechádza na klienta po zaplatení faktúry. Poskytovateľ môže prácu ukázať v portfóliu po dohode s klientom.</p>
    <h2>6. Zakázané praktiky</h2>
    <p>Poskytovateľ nepoužíva praktiky porušujúce pokyny vyhľadávačov (nákup odkazov zo sietí automatizovaného spamu, skryté texty, duplicitný obsah). Sankcie z porušenia pokynov sú skutočné riziko, preto sa im vyhýbame zásadovo.</p>
  </div>
</section>
"""
    html = base(market="sk", path="terms/", title="Obchodné podmienky | Nokto Studio",
                desc="Obchodné podmienky Nokto Studio: hodinová sadzba 12 EUR, mesačná fakturácia, bez viazanosti, transparentné vykazovanie.",
                canonical=BASE + "/sk/terms/", body=body, prefix="../..", extra_head=ORG_SCHEMA)
    return ("sk/terms/index.html", html)
