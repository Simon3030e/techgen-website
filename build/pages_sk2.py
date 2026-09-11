# -*- coding: utf-8 -*-
"""Nokto Studio - SK supporting pages."""
import re

from engine import (base, page_hero, cta_band, faq_block, faq_schema,
                    article_schema, steps_block, results_slider, result_block,
                    ORG_SCHEMA, EMAIL, BASE, gicon, PHONE_TEL, PHONE_DISPLAY,
                    _bars, _sparkline, _VIOLET_L, _VIOLET, _ORANGE, _CERULEAN, _donut)

# ---------------------------------------------------------------- JAK PRACUJEME

def jak_pracujeme() -> tuple[str, str]:
    body = f"""
{page_hero("Proces", "Ako pracujem: plán, práca, meranie",
           "Jasný proces bez čiernej skrinky. Viete, čo robím, prečo a čo to prinieslo. Platíte za hodiny, ktoré sú vykazované.",
           [("Domov", "/"), ("Ako pracujem", None)])}

<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Dva piliere</span>
      <h2>Dva hlavné piliere mojej práce</h2>
      <p class="section-subheading">Takto klientom pomáham rásť v Google a AI vyhľadávaní. Jeden bez druhého nefunguje.</p>
    </div>
    <div class="grid-2">
      <div class="benefit-card card-hover">
        <span class="benefit-icon">{gicon("search", "#6A3FC4", 26)}</span>
        <h3>Písanie obsahu</h3>
        <p>Expertné články a texty stránok na dopyty, ktoré zákazníci reálne pýtajú. Obsah, ktorý Google cituje aj v AI odpovediach a odporúča zákazníkom.</p>
      </div>
      <div class="benefit-card card-hover">
        <span class="benefit-icon">{gicon("audit", "#9B6FD9", 26)}</span>
        <h3>Opravy technických vecí na webe</h3>
        <p>Technické SEO: rýchlosť, indexácia, kanonizácie, interné prelinkovanie a čistá štruktúra webu. Základ, na ktorom obsah funguje.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Proces</span>
      <h2>Od prvého hovoru po mesačný hovor so mnou</h2>
    </div>
    {steps_block([
        {"title": "1. Bezplatný hovor a audit", "text": "30 minút telefonátu, v ktorom si povieme vaše ciele. Do 3 dní od neho dostanete bezplatný vstupný audit: 10 najväčších problémov a šancí vášho webu na jednej strane."},
        {"title": "2. Plán s číslami", "text": "Z auditu spravím plán: ktoré kľúčové slová prinášajú zákazníkov, čo opraviť ako prvé, koľko hodín mesačne to zaberie a aké výsledky sú reálne. Bez nereálnych sľubov."},
        {"title": "3. Práca v týždenných dávkach", "text": "Každý týždeň odpracujem dohodnutý rozsah: technika, obsah, Google profil, AI viditeľnosť, odkazy. Každú zmenu viete dohľadať."},
        {"title": "4. Meranie a report", "text": "Mesačný report vám dám osobne ako 30-minútový telefonát: čo sa urobilo, čo to prinieslo (pozície, kliky, objednávky, zmienky v AI) a čo je ďalší krok."},
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
          <li><span class="check">✓</span><span>Pozície na sledovaných kľúčových slovách (trend, nielen čísla).</span></li>
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
      <h2>Ako meriam výsledky</h2>
      <p class="section-subheading">Nič nemeníme názormi. Každé tvrdenie má v reporte číslo a zdroj dát.</p>
    </div>
    <table class="metric-table">
      <tr><th>Čo sledujem</th><th>Nástroj</th><th>Čo to hovorí</th></tr>
      <tr><td><strong>Pozície</strong></td><td>Sledovanie kľúčových slov</td><td>Na ktorých dopytoch web rastie a kde stojí.</td></tr>
      <tr><td><strong>Kliky z Google</strong></td><td>Search Console</td><td>Koľko ľudí nás vidí a koľko z nich klikne.</td></tr>
      <tr><td><strong>Kontakty a objednávky</strong></td><td>Google Analytics 4</td><td>Koľko návštevníkov sa stalo zákazníkmi.</td></tr>
      <tr><td><strong>Viditeľnosť na mape</strong></td><td>Firemný profil Google</td><td>Koľko ľudí videlo firmu, zatelefonovalo, išlo na trasu.</td></tr>
      <tr><td><strong>AI odporúčania</strong></td><td>Pravidelné AI testy</td><td>Či vás ChatGPT, Gemini a AI Overviews citujú.</td></tr>
      <tr><td><strong>Tržby z organiky</strong></td><td>Analytics + e-shop</td><td>Pre e-shopy: priamy vzťah SEO úsilia k predaju.</td></tr>
    </table>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    {cta_band("Chcete takýto proces pre svoj web?", "Začnite bezplatným auditom a 30 minútami konzultácie.", "sk")}
  </div>
</section>
"""
    html = base(market="sk", path="jak-pracujeme/", title="Ako pracujem: proces, dodávky a meranie výsledkov | Nokto Studio",
                desc="Náš SEO proces: bezplatný audit, plán s číslami, týždenná práca, mesačné meranie. Pozície, kliky, objednávky a AI odporúčania v jednom reporte.",
                canonical=BASE + "/sk/jak-pracujeme/", body=body, prefix="../..", extra_head=ORG_SCHEMA)
    return ("sk/jak-pracujeme/index.html", html)


# ---------------------------------------------------------------- VYSLEDKY

def vysledky() -> tuple[str, str]:
    """Results page: real numbers from GSC exports, AI Mode and client reports."""
    c_servisprofi = _bars([145, 115, 61, 42, 38], _VIOLET_L,
                          ["vypínač", "ceny el.", "prípojka", "zásuvka", "vzduchom"])
    c_speem = _bars([413, 412, 407, 407, 385], _VIOLET,
                    ["pyžamo", "body", "tričká", "nohavice", "čelenky"])
    c_itc = _sparkline([40, 55, 48, 62, 58, 75, 70, 88, 95, 92, 110, 121], _VIOLET)
    blocks = "".join([
        result_block(
            title="ServisProfi.sk", period="marec až september 2026",
            nums=[{"big": "996", "color": _VIOLET, "label": "klikov z Google (+8 %)"},
                  {"big": "73 000", "color": _ORANGE, "label": "zobrazení (+5 %)"},
                  {"big": "96", "color": _VIOLET_L, "label": "citácií v AI odpovediach"}],
            chart=c_servisprofi,
            caption="Dva expertné články (nabíjanie elektromobilu, prepäťová ochrana) Google cituje v AI odpovediach a odporúča ServisProfi.sk zákazníkom. Web 69 stránok: 9 700 → 12 000 zobrazení za 28 dní (+24 %). Graf: rast hlavných stránok v percentách.",
            source="Google Search Console, report výkonnosti 9. 9. 2026",
            partner="", market="sk"),
        result_block(
            title="Mikramt.sk, Martin", period="prvý e-shop, teraz rework v priebehu",
            nums=[{"big": "2 492,75 EUR", "color": _VIOLET_L, "label": "tržieb z prvého e-shopu"},
                  {"big": "15", "color": _VIOLET, "label": "objednávok online"},
                  {"big": "722 EUR", "color": _CERULEAN, "label": "najväčšia objednávka"}],
            chart="",
            caption="Prvý e-shop Mikramt.sk s API integráciou na účtovný systém Sunsoft Ecosun. Zákazník bol spokojný, takže teraz robíme rework: viac produktov, väčšia kategorizácia a lepšie SEO. Web a dizajn v spolupráci s Flamia Studio, SEO a e-mail marketing robím sám. Predaj v kamennej predajni do sumy nerátame.",
            source="objednávky pripísané do kanálov email a organický Google",
            partner="flamia", market="sk"),
        result_block(
            title="Speem.sk", period="Search Console + AI Mode, jún až september 2026",
            nums=[{"big": "893", "color": _VIOLET_L, "label": "zobrazení v Google AI Mode za 3 mesiace"},
                  {"big": "+80 %", "color": _VIOLET, "label": "august oproti júnu (182 → 329)"},
                  {"big": "413", "color": _ORANGE, "label": "klikov na hlavnú kategóriu"}],
            chart=_bars([182, 293, 329, 89], _VIOLET_L, ["jún", "júl", "aug", "sep"]),
            caption="Google AI Mode cituje e-shop denne po nasadení nášho obsahu. Rast mesačne: jún 182, júl 293, august 329. Najviac citované: homepage a blogové články (174, 167 a 119 citácií). Kategórie majú desiatky tisíc organických zobrazení mesačne (čelenky 44 838). Konkurencia v AI odpovediach ešte nie je.",
            source="Google Search Console + Google AI Mode (report citácií), jún až september 2026",
            partner="own", market="sk"),
        result_block(
            title="InTheCity.app", period="posledných 28 dní",
            nums=[{"big": "121", "color": _VIOLET, "label": "klikov z Google (+49 %)"},
                  {"big": "4 390", "color": _ORANGE, "label": "zobrazení (+43 %)"},
                  {"big": "+142 %", "color": _VIOLET_L, "label": "rast hlavnej stránky"}],
            chart=c_itc,
            caption="SEO od nuly: technické SEO a obsah v prvom mesiaci spolupráce, Google začal prinášať zákazníkov hneď.",
            source="Google Search Console",
            partner="own", market="sk"),
        result_block(
            title="Villa Paris, Piešťany", period="rebrand + web + lokálne SEO",
            nums=[],
            chart="",
            caption="Prémiové ubytovanie. Rebrand, nový web, hotelový copywriting a lokálne SEO v jednom systéme. Značku a web robíme v spolupráci s Flamia Studio. Cieľ: viac priamych rezervácií bez provízií.",
            source="príbeh projektu na /sk/villa-paris/",
            partner="flamia", market="sk"),
        result_block(
            title="Energymonitor.tech", period="rework v priebehu",
            nums=[],
            chart="",
            caption="E-shop s produktmi na monitorovanie energie. Teraz rework webu: nová štruktúra, produktové dáta, kategorizácia a technika. Web v spolupráci s Flamia Studio. Čísla doplním po nasadení, keď budú reálne merateľné.",
            source="práca v priebehu, čísla po nasadení",
            partner="flamia", market="sk"),
    ])
    body = f"""
{page_hero("Výsledky", "Ako som pomohol klientom rásť v Google a AI vyhľadávaní",
           "Písaním obsahu a opravami technických vecí na webe. Výsledky z Google Search Console a Google AI Mode.",
           [("Domov", "/"), ("Výsledky", None)])}

<section class="section">
  <div class="container">
    <div class="grid-2">{blocks}</div>
    <p style="text-align:center; margin-top:28px; color:var(--text-muted); font-size:0.9rem;">
      Ďalšie výsledky a referencie na žiadosť, vrátane kontaktov na klientov. Klientov citujem len s ich súhlasom.
    </p>
  </div>
</section>

{results_slider("sk")}

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Spätná väzba</span>
      <h2>Čo hovorí pokračovanie spoluprác</h2>
      <p class="section-subheading">Najlepší testimonial je fakt, že klienti zostávajú. Kontakty na klientov poskytnem na žiadosť, citujem ich len s ich súhlasom.</p>
    </div>
    <div class="grid-3">
      <div class="benefit-card card-hover">
        <span class="benefit-icon">{gicon("grow", "#9B6FD9", 26)}</span>
        <h3>Mikramt.sk: spolupráca pokračuje</h3>
        <p>Zákazník bol spokojný s prvým e-shopom (2 492,75 EUR za 9 mesiacov), takže teraz robíme rework: viac produktov a lepšie SEO.</p>
      </div>
      <div class="benefit-card card-hover">
        <span class="benefit-icon">{gicon("ai", "#6A3FC4", 26)}</span>
        <h3>ServisProfi.sk: mesačná spolupráca beží</h3>
        <p>996 klikov (+8 %) a 96 citácií v AI odpovediach za 3 mesiace. Report vychádza každý mesiac s číslami.</p>
      </div>
      <div class="benefit-card card-hover">
        <span class="benefit-icon">{gicon("pin", "#F75940", 26)}</span>
        <h3>Villa Paris: projekt beží s Flamia Studio</h3>
        <p>Rebrand, web a lokálne SEO v jednom systéme. Značku a web robíme v spolupráci s Flamia Studio.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="grid-2" style="align-items:start;">
      <div class="prose">
        <span class="section-label">Ďaľší krok</span>
        <h2>Napíšte mi alebo zavolajte</h2>
        <p>Do 24 hodín vám odpoviem s prvými nápormi pre váš web. Bezplatný vstupný audit: čo brzdí vaše pozície, predaj a AI odporúčania.</p>
        <p style="margin-top:18px;"><a href="{PHONE_TEL}" class="btn btn-primary btn-lg" style="width:100%;">Zavolajte {PHONE_DISPLAY}</a></p>
        <p style="margin-top:12px;">Alebo email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
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
          <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off" aria-hidden="true">
          <input type="hidden" name="_subject" value="Dotaz zo stránky Výsledky - noktostudio.com">
          <button type="submit" class="btn btn-primary" style="margin-top:18px; width:100%;">Poslať správu</button>
          <p class="form-note">Odoslaním súhlasíte so spracovaním údajov na účel odpovede (pozrite <a href="/sk/privacy/">ochranu súkromia</a>).</p>
        </form>
        <div class="form-success" style="display:none; margin-top:16px; background:#F5F1FC; color:var(--brand-cool-deep); padding:16px; border-radius:10px;">
          ✓ Ďakujeme, správa odletela na {EMAIL}. Ozveme sa osobne do 24 hodín. Alebo zavolajte rovno: <a href="tel:+421917316105" style="font-weight:700;">+421 917 316 105</a>
        </div>
      </div>
    </div>
  </div>
</section>
"""
    html = base(market="sk", path="vysledky/", title="Výsledky SEO: ServisProfi, Mikramt, Speem, InTheCity | Nokto Studio",
                desc="Výsledky Nokto Studio: 996 klikov a 96 citácií v AI odpovediach pre ServisProfi.sk, 2 492,75 EUR tržieb pre Mikramt.sk, AI citácie pre Speem.sk. Výsledky z Google Search Console.",
                canonical=BASE + "/sk/vysledky/", body=body, prefix="../..", extra_head=ORG_SCHEMA)
    return ("sk/vysledky/index.html", html)


# ---------------------------------------------------------------- VILLA PARIS (case study)

def villa_paris() -> tuple[str, str]:
    body = f"""
{page_hero("Prípadová štúdia · Branding &amp; Web", "Villa Paris: značka a web od nuly",
           "Prémiové ubytovanie v Piešťanoch malo skvelý produkt. Chýbala mu značka. Vyriešil som to identitou, webom, copywritingom a lokálnym SEO ako jedným systémom.",
           [("Domov", "/"), ("Výsledky", "/sk/vysledky/"), ("Villa Paris", None)])}

<div class="partner-band" style="justify-content:center; padding:0 20px;">
  <span class="project-tag tag-violet"><a href="https://flamia.studio" target="_blank" rel="noopener noreferrer" style="color:inherit;">V spolupráci s Flamia Studio</a></span>
  <span class="project-tag tag-violet-light">Web dizajn a vývoj: Flamia Studio</span>
  <span class="project-tag tag-cerulean">SEO, copywriting a lokálne SEO: Nokto Studio</span>
</div>

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
        <p>Prepracovaná štruktúra s dôrazom na prehľadnosť a konverziu rezervácií od prvého posunutia. Rýchle načítanie, jednoduchá cesta k rezervácii, mobilná skúsenosť ako priorita.</p>
        <h3>Hotelový copywriting</h3>
        <p>Texty orientované na hosťa, ktoré odpovedajú na skutočné otázky pred rezerváciou: lokalita, komfort, čo očakávať po príchode.</p>
        <h3>Lokálne SEO</h3>
        <p>Firemný profil Google v poriadku, lokálne kľúčové slová pre Piešťany a kúpeľné hostiteľstvo tak, aby Villu Paris našli hostia, ktorí hľadajú presne toto ubytovanie.</p>
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
          <a href="/sk/kontakt/" class="btn btn-primary">Chcem podobný projekt</a>
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
         "SEO optimalizáciu webu, lokálne SEO a firemný profil Google, optimalizáciu pre AI vyhľadávače (ChatGPT, Gemini, AI Overviews), SEO pre e-shopy, SEO audity, linkbuilding, tvorbu webov a PPC reklamu Google Ads. K tomu e-mail marketing pre e-shopy a firmy."),
        ("Pre aké firmy pracujete?",
         "Predovšetkým pre menšie a stredné firmy: lokálne služby (remeselníci, zdravotníctvo, právo, autoservis), e-shopy a firmy, ktoré ponúkajú odborné služby. Pracujem na trhoch Slovenska a Česka."),
        ("S akými platformami pracujete?",
         "WordPress, Shoptet, WooCommerce a vlastné riešenia. Pri SEO má nástroj druhoradú úlohu, dôležitá je stratégia a jej vykonávanie."),
    ]),
    ("Cena a zmluvy", [
        ("Koľko stojí SEO?",
         "12 EUR za odpracovanú hodinu. Malý firemný web zvyčajne 10 hodín mesačne (120 EUR), e-shop 20 až 40 hodín (240 až 480 EUR). Balíčky sú odporúčané rozsahy, nie povinné paušály."),
        ("Sú zmluvy viažúce?",
         "Nie. Spoluprácu môžete skončiť kedykoľvek, bez sankcií. Fakturujem mesačne za skutočne odpracované hodiny."),
        ("Čo ak potrebujem viac hodín v jednom mesiaci?",
         "Nič sa nemení, ide sa len do väčšieho počtu hodín. Rozsah sa dohodne v pláne a môžete ho kedykoľvek zmeniť."),
        ("Sú v cene zahrnuté reklamné výdavky?",
         "Nie. Reklamu (Google Ads) platíte priamo Google. Riadim kampane za 12 EUR za hodinu. Náklady na odkazy a PR vykazujem v skutočnej cene."),
    ]),
    ("Proces a výsledky", [
        ("Ako dlho trvá, kým SEO prinesie výsledky?",
         "Prvé pohyby na menej konkurenčných dotazoch za 2 až 4 mesiace, na hlavné dotazy 6 až 12 mesiacov. Lokálne SEO a Google profil sa zlepšujú častejšie za 4 až 8 týždňov. Presné termíny poviem v audite."),
        ("Ako budem vidieť, že práca bola odvedená?",
         "Mesačný report osobne: 30-minútový hovor so mnou. Odpracované hodiny, pozície, kliky zo Search Console, objednávky z Analytics, viditeľnosť v Mapách a zmienky v AI."),
        ("Ponúkate záruky prvej pozície?",
         "Nie. Nikto reálne nevie zaručiť prvé miesto v Google. Kto to sľubuje, predáva fiktívne záruky. Zaručím proces, transparentnosť a merateľný postup, ktorý k pozíciám vedie."),
        ("Pomôžete aj s presunom alebo migráciou webu?",
         "Áno, migrácia webu je jedna z úloh, pri ktorej sa ľahko strácajú pozície. Viem, čo robiť, aby sa to nestalo."),
    ]),
    ("AI a nové vyhľadávanie", [
        ("Je to pravda, že ChatGPT nahradí Google?",
         "Nahradí ho, ale nezničí. Zákazníci dnes vyhľadávajú oboje. Moja práca pokrýva oboje: klasické Google pozície aj viditeľnosť v AI odpovediach."),
        ("Ako zistím, či ma AI odporúča?",
         "Pravidelne testujem súbory dotazov, ktoré vaši zákazníci vyhľadávajú, a zaznamenávam, či sa vaše meno objavuje v odpovediach ChatGPT, Gemini a Google AI Overviews. Zapisujem to v mesačnom reporte."),
        ("Prečo je táto špecializácia vzácna?",
         "Optimalizácia pre AI je nová odborná práca, ktorá si vyžaduje inú metódu obsahu a štruktúry dát. Väčšina agentúr na Slovensku sa na ňu zatiaľ nepripravuje, čo je výhoda pre klientov, ktorí začnú prví."),
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
{page_hero("FAQ", "Časté otázky", "Odpovede na to, čo sa ma klienti pýtajú najviac. Ak chýba vaša otázka, pýtajte sa priamo.", [("Domov", "/"), ("FAQ", None)])}
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
                desc="Časté otázky: koľko stojí SEO, ako dlho trvá, ako sa merajú výsledky, čo je SEO pre AI vyhľadávače. Nokto Studio, SEO agentúra.",
                canonical=BASE + "/sk/faq/", body=body, prefix="../..", extra_head=ORG_SCHEMA + faq_html)
    return ("sk/faq/index.html", html)


# ---------------------------------------------------------------- O NAS

def o_nas() -> tuple[str, str]:
    body = f"""
{page_hero("O nás", "Pracujeme v tieni.<br>Výsledky hovoria samy za seba.",
           "Nokto Studio je SEO agentúra jedného človeka s tímom spolupracovníkov. Pracujeme pre podnikateľov, ktorí chcú merateľný rast, nie marketingové tance.",
           [("Domov", "/"), ("O nás", None)])}
<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:center;">
      <div class="prose">
        <h2>Kto za Nokto stojí</h2>
        <p>Volám sa Šimon Štermenský a Nokto Studio je môj projekt. Za sebou mám roky práce na SEO a weboch pre slovenských aj zahraničných klientov: e-shopy, lokálne firmy, médiá aj prémiové značky. Postavil som automatizované systémy, ktoré zo SEO práce vytvárajú presne to, čo firma potrebuje: zákazníkov.</p>
        <p>Nie som veľká agentúra a nepredstieram to. Výhodou je, že s vami pracuje ten istý človek, ktorý navrhol stratégiu. Žiadne preposielanie medzi oddeleniami, žiadne strácanie kontextu.</p>
        <h2>Ako pracujem</h2>
        <p>Kombinujeme dva svety: odbornú SEO prácu (technika, obsah, autorita, AI viditeľnosť) a automatizáciu, ktorá z rovnakého úsilia vytiahne viac. Preto vieme pracovať za 12 EUR za hodinu a stále sa sústrediť na výsledok, nie na fakturovanie hodín na okraji.</p>
      </div>
      <div>
        <img src="/assets/img/simon.png" alt="Šimon Štermenský, zakladateľ Nokto Studio" loading="lazy" style="border-radius:var(--radius-lg); border:1px solid var(--border-light);">
        <p style="text-align:center; margin-top:12px; font-size:0.85rem; color:var(--text-muted);">Šimon Štermenský, zakladateľ Nokto Studio</p>
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
      <div class="benefit-card"><span class="benefit-icon">{gicon("shield", "#6A3FC4", 26)}</span><h3>Žiadne sľuby, ktoré sa nedodržia.</h3><p>Prvú pozíciu v Google nevie zaručiť nikto. Čo zaručíme: transparentný proces, reálne termíny a merateľný postup.</p></div>
      <div class="benefit-card"><span class="benefit-icon">{gicon("chart", "#F75940", 26)}</span><h3>Mesačný report so mnou</h3><p>30-minútový telefonát: čo som spravil, čo to prinieslo a čo ide ďalej. Bez preposielania.</p></div>
      <div class="benefit-card"><span class="benefit-icon">{gicon("check", "#9B6FD9", 26)}</span><h3>Každá hodina vykazovaná</h3><p>Platíte za odvedenú prácu. Každá hodina je v reporte s jej obsahom a výsledkom.</p></div>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0;">
  <div class="container">
    {cta_band("Spoznajme sa 30 minút", "Bezplatný hovor o vašich cieľoch. Ak sa nespárujeme, poviem vám to priamo.", "sk")}
  </div>
</section>
"""
    html = base(market="sk", path="o-nas/", title="O nás: SEO agentúra Nokto Studio | Šimon Štermenský",
                desc="Nokto Studio: SEO agentúra pre podnikateľov. Kto za nami stojí, ako pracujeme a prečo 12 EUR za hodinu stačí na merateľné výsledky.",
                canonical=BASE + "/sk/o-nas/", body=body, prefix="../..", extra_head=ORG_SCHEMA)
    return ("sk/o-nas/index.html", html)


# ---------------------------------------------------------------- KONTAKT

def kontakt() -> tuple[str, str]:
    body = f"""
{page_hero("Kontakt", "Zavolajte alebo napíšte. Ozveme sa osobne.",
           "Najrýchlejšia cesta je telefón. Alebo pošlite formulár a do 24 hodín máte odpoveď s prvými návrhmi.",
           [("Domov", "/"), ("Kontakt", None)])}
<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:start;">
      <div class="card" style="text-align:center;">
        <span class="section-label">Zavolajte priamo</span>
        <a href="tel:+421917316105" class="btn btn-primary btn-lg contact-phone-btn" style="width:100%; margin-top:14px; font-size:1.25rem;">+421 917 316 105</a>
        <p style="margin:14px 0 6px; color:var(--text-muted);">Šimon Štermenský, SEO špecialista. Väčšinou dvíham hneď, inak volám späť do pár hodín.</p>
        <ul class="deliv-list" style="text-align:left; margin-top:20px;">
          <li><span class="check">✓</span><span>30 minút bezplatnej konzultácie o vašom webe</span></li>
          <li><span class="check">✓</span><span>Bezplatný vstupný audit webu po hovore</span></li>
          <li><span class="check">✓</span><span>Reálne čísla: čo by SEO mohlo u vás znamenať</span></li>
          <li><span class="check">✓</span><span>Nezáväzné. Rozhodnete sa, kedy a či.</span></li>
        </ul>
        <p style="margin-top:22px; border-top:1px solid var(--border-light); padding-top:18px;">
          Email: <a href="mailto:{EMAIL}" style="font-weight:700; color:var(--text);">{EMAIL}</a>
        </p>
        <a href="mailto:{EMAIL}" class="btn btn-outline" style="width:100%; margin-top:10px;">Napísať email</a>
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
          <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off" aria-hidden="true">
          <input type="hidden" name="_subject" value="Nový dotaz z webu noktostudio.com">
          <button type="submit" class="btn btn-primary" style="margin-top:18px; width:100%;">Poslať správu</button>
          <p class="form-note">Odoslaním súhlasíte so spracovaním údajov na účel odpovede (pozrite <a href="/sk/privacy/">ochranu súkromia</a>).</p>
        </form>
        <div class="form-success" style="display:none; margin-top:16px; background:#F5F1FC; color:var(--brand-cool-deep); padding:16px; border-radius:10px;">
          ✓ Ďakujeme, správa odletela na {EMAIL}. Ozveme sa osobne do 24 hodín. Alebo zavolajte rovno: <a href="tel:+421917316105" style="font-weight:700;">+421 917 316 105</a>
        </div>
      </div>
    </div>
  </div>
</section>
"""
    html = base(market="sk", path="kontakt/", title="Kontakt: telefón +421 917 316 105, e-mail a formulár | Nokto Studio",
                desc="Spojte sa s Nokto Studio. Zavolajte +421 917 316 105, napíšte e-mail alebo pošlite kontaktný formulár. Bezplatný vstupný audit webu.",
                canonical=BASE + "/sk/kontakt/", body=body, prefix="../..", extra_head=ORG_SCHEMA)
    return ("sk/kontakt/index.html", html)


# ---------------------------------------------------------------- BLOG POSTY (KW-researched, MM data)

_BLOG_META = {
    "seo-optimalizacia-navod": dict(
        title="SEO optimalizácia: kompletný návod 2026 | Nokto Studio",
        desc="SEO optimalizácia krok za krokom: audit, plán, obsah, technika a meranie. Návod pre malé firmy s reálnymi číslami z Google Search Console."),
    "kolko-stoji-seo": dict(
        title="Koľko stojí SEO v roku 2026? Ceny na slovenskom trhu | Nokto Studio",
        desc="Koľko stojí SEO optimalizácia: ceny od 60 do 1 200 EUR mesačne, čo za ne dostanete a prečo publikujeme cenu 12 EUR za hodinu. Bezplatný audit."),
    "seo-test-15-bodov": dict(
        title="SEO test: 15-bodový kontrolný zoznam pre váš web | Nokto Studio",
        desc="SEO test webu za 30 minút: 15 kontrolných bodov z techniky, obsahu, Google profilu a AI viditeľnosti. Zistite, čo brzdí vaše pozície."),
    "linkbuilding-co-to-je": dict(
        title="Linkbuilding: čo to je, čo stojí a ako sa robí bezpečne | Nokto Studio",
        desc="Linkbuilding jednoducho: čo sú spätné odkazy, reálne ceny 50 až 300 EUR, bezpečné metódy a čo Google sankcionuje. Návod s príkladmi."),
    "google-firmy-profil-navod": dict(
        title="Google firemný profil: návod od založenia po hodnotenia | Nokto Studio",
        desc="Kompletný návod na Google firemný profil: založenie, overenie, kategórie, fotky, hodnotenia cez SMS a QR kód. Prípadová štúdia z praxe."),
    "seo-wordpress": dict(
        title="SEO pre WordPress: 12 nastavení, ktoré treba spraviť | Nokto Studio",
        desc="SEO pre WordPress: permalinky, rýchlosť, schéma, sitemap a pluginy. 12 konkrétnych nastavení, ktoré posunú vaše pozície."),
}


def blog_post(*, slug: str, label: str, h1: str, answer: str, sections: str,
              faq: list[tuple[str, str]], related: list[tuple[str, str]],
              date_iso: str = "2026-09-10", date_display: str = "10. 9. 2026") -> tuple[str, str]:
    """Render one blog post page: direct answer first, sections, FAQ, CTA."""
    related_html = "".join(
        f'<div class="benefit-card card-hover related-card"><h3><a href="/sk/blog/{u}/" style="color:var(--text);">{n}</a></h3></div>'
        for u, n in related)
    # answer goes to the takeaway box; drop the duplicated in-body section
    sections = re.sub(r"<h2>Stručná odpoveď</h2>\s*<p>.*?</p>", "", sections, count=1, flags=re.S)
    body = f"""
<section class="post-hero">
  <div class="container" style="max-width:820px;">
    <a href="/sk/blog/" class="post-back">← Blog</a>
    <span class="section-label">{label}</span>
    <h1>{h1}</h1>
    <p class="post-meta">{date_display} · Šimon Štermenský · Nokto Studio</p>
  </div>
</section>

<article class="section" style="padding-top:16px;">
  <div class="container" style="max-width:820px;">
    <div class="prose">
      <div class="post-answer"><p>{answer}</p></div>
{sections}
    </div>
  </div>
</article>

<section class="section" style="padding-top:0;">
  <div class="container" style="max-width:820px;">
    <div class="section-head"><span class="section-label">FAQ</span><h2>Časté otázky</h2></div>
    {faq_block(faq)}
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container" style="max-width:820px;">
    <div class="section-head"><span class="section-label">Prečítať aj</span><h2>Súvisiace články</h2></div>
    <div class="grid-2">{related_html}</div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    {cta_band("Chcete toto urobiť na svojom webe?", "Začnime bezplatným auditom. Vidíte, čo by som riešil ako prvé, ešte pred prvou faktúrou.", "sk")}
  </div>
</section>
"""
    meta = _BLOG_META[slug]
    url = BASE + f"/sk/blog/{slug}/"
    html = base(market="sk", path=f"blog/{slug}/", title=meta["title"], desc=meta["desc"],
                canonical=url, body=body, prefix="../../../", og_type="article",
                extra_head=ORG_SCHEMA + article_schema(url=url, title=meta["title"],
                                                       desc=meta["desc"], date_iso=date_iso)
                          + faq_schema(faq, url))
    return (f"sk/blog/{slug}/index.html", html)


def _flow_chart() -> str:
    """Infographic: 4-step SEO process flow."""
    steps = [("Hovor", "30 min + audit", "#6A3FC4"),
             ("Plán", "číslo a priority", "#9B6FD9"),
             ("Práca", "týždenné dávky", "#1DACD6"),
             ("Meranie", "report mesačne", "#F75940")]
    boxes, arrows = "", ""
    x = 10
    for i, (t, s, c) in enumerate(steps):
        boxes += (f'<rect x="{x}" y="30" width="120" height="64" rx="10" fill="#fff" '
                  f'stroke="{c}" stroke-width="2"/>'
                  f'<text x="{x+60}" y="58" text-anchor="middle" font-size="15" font-weight="700" '
                  f'fill="{c}" font-family="Inter,sans-serif">{t}</text>'
                  f'<text x="{x+60}" y="78" text-anchor="middle" font-size="11" '
                  f'fill="#5F6368" font-family="Inter,sans-serif">{s}</text>')
        if i < 3:
            arrows += (f'<path d="M{x+124} 62 l18 0" stroke="#5F6368" stroke-width="2" '
                       f'marker-end="url(#arr)"/>')
        x += 150
    return (f'<svg viewBox="0 0 590 124" role="img" aria-label="Schéma procesu SEO: hovor, plán, práca, meranie" '
            f'style="width:100%;height:auto;margin:10px 0;">'
            f'<defs><marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">'
            f'<path d="M0 0 L8 4 L0 8 z" fill="#5F6368"/></marker></defs>{boxes}{arrows}</svg>')


def blog_post_navod() -> tuple[str, str]:
    sections = f"""
<h2>Stručná odpoveď</h2>
<p>SEO optimalizácia je oprava technickej stránky webu a písanie obsahu na dopyty, ktoré zákazníci reálne pýtajú. Funguje v štyroch krokoch: audit, plán s číslami, týždenná práca a mesačné meranie. Prvé pohyby na menej konkurenčných dopytoch vidíte za 2 až 4 mesiace, na hlavné dopyty 6 až 12 mesiacov.</p>
<figure class="blog-chart">{_flow_chart()}</figure>
<h2>Krok 1: Bezplatný audit a analýza</h2>
<p>Začnite auditom webu a kľúčových slov. Zistite: či Google váš web správne indexuje, akou rýchlosťou sa načítava, na ktoré dopyty už vidíte (aj na pozícii 40), a čo pýtajú zákazníci. Nástroje sú zdarma: <a href="https://pagespeed.web.dev/" target="_blank" rel="noopener noreferrer">PageSpeed Insights</a> na rýchlosť a <a href="https://search.google.com/search-console" target="_blank" rel="noopener noreferrer">Google Search Console</a> na indexáciu a dopyty. Základný postup popisuje aj <a href="https://developers.google.com/search/docs/fundamentals/seo-starter-guide" target="_blank" rel="noopener noreferrer">príručka pre začiatočníkov od Google</a>. Bezplatný vstupný audit urobím za vás: 10 najväčších problémov a šancí webu na jednej strane do 3 dní, <a href="/sk/sluzby/seo-audit/">detailný SEO audit</a> má akčný plán s hodinami.</p>
<h2>Krok 2: Plán s číslami</h2>
<p>Z auditu spravíte plán: ktoré kľúčové slová prinášajú zákazníkov, čo opraviť ako prvé a koľko hodín mesačne to zaberie. Rozhodujúce je vybrať dopyty s nízkou konkurenciou: nový web nevyhrá národné pozície, ale lokálne a dlhé dopyty („cena nabíjania elektromobilu doma") áno.</p>
<h2>Krok 3: Týždenná práca</h2>
<p>Práca ide v dávkach: technika (rýchlosť, kanonizácie, interné prelinkovanie), <a href="/sk/sluzby/seo-optimalizacia/">obsahové stránky na reálne dopyty</a>, <a href="/sk/sluzby/lodalne-seo/">Google firemný profil</a> a <a href="/sk/sluzby/seo-pre-ai-vyhladavace/">AI viditeľnosť</a>. Každý týždeň odrobený rozsah, každú zmenu viete dohľadať.</p>
<h2>Krok 4: Meranie</h2>
<p>V Google Search Console sledujte pozície a kliky, v Analytics objednávky. Mesačný report: čo sa urobilo, čo to prinieslo a čo je ďalší krok. Koľko to stojí rozoberá <a href="/sk/cennik/">cenník (12 EUR za hodinu)</a>. Príklad z praxe: web, ktorý som prevzal s minimálnou návštevnosťou, dosiahol 250 klikov za 3 mesiace (+355 %) po technickej oprave a 6 obsahových stránkach.</p>
"""
    faq = [
        ("Ako dlho trvá SEO optimalizácia?",
         "Prvé pohyby na menej konkurenčných dotazoch za 2 až 4 mesiace, na hlavné dotazy 6 až 12 mesiacov. Záleží na konkurencii a stave webu."),
        ("Koľko hodín mesačne zaberie SEO?",
         "Firemný web zvládnem v 10 hodinách mesačne (120 EUR), e-shop v 20 až 40 hodinách (240 až 480 EUR). Rozsah potvrdím v pláne po audite."),
        ("Robíte aj obsah?",
         "Áno, písanie obsahu je súčasť hodín. Navrhnem štruktúru, napíšem texty a pred publikovaním ich schválite."),
    ]
    return blog_post(slug="seo-optimalizacia-navod", label="Návod", h1="SEO optimalizácia: kompletný návod 2026",
                     answer="SEO optimalizácia krok za krokom: audit, plán s číslami, týždenná práca a mesačné meranie. Návod pre malé firmy s reálnymi číslami z praxe.",
                     sections=sections, faq=faq,
                     related=[("kolko-stoji-seo", "Koľko stojí SEO v roku 2026?"), ("seo-test-15-bodov", "SEO test: 15-bodový kontrolný zoznam")])


def blog_post_kolko_stoji() -> tuple[str, str]:
    price_chart = _bars([120, 240, 480], _VIOLET, ["Štart 120 EUR", "Rast 240 EUR", "E-shop 480 EUR"])
    sections = f"""
<h2>Stručná odpoveď</h2>
<p>SEO na slovenskom trhu stojí od 300 do 1 500 EUR mesačne pri agenciách s paušálmi, alebo od 60 EUR mesačne pri hodinovej spolupráci. Ja účtujem 12 EUR za odpracovanú hodinu: malý firemný web zvládnem v 10 hodinách mesačne (120 EUR), e-shop v 20 až 40 hodinách (240 až 480 EUR). Neplatíte paušál, platíte za odpracovanú prácu.</p>
<figure class="blog-chart">{price_chart}</figure>
<h2>Čo ovplyvňuje cenu SEO</h2>
<p>Tri veci: rozsah webu (69 stránok e-shopu nie je 5 stránok firemného webu), konkurencia na vašich dopytoch a rozsah obsahu, ktorý treba napísať. Preto nefunguje univerzálna cena: precením počty hodín v pláne po audite.</p>
<h2>Referenčné ceny na trhu (2026)</h2>
<p>Menšie agentúry: 300 až 600 EUR mesačne. Stredné: 600 až 1 500 EUR. Veľké s paušálmi: 1 500 EUR a viac, často na 12-mesačné zmluvy. Pri paušáli sa často nevie, čo za peniaze dostanete. Preto fungujem na hodiny: každá hodina je vykazovaná v reporte s obsahom a výsledkom. Balíčky a rozsahy nájdete v <a href="/sk/cennik/">cenníku</a>.</p>
<h2>Čo dostanete za 120 EUR mesačne</h2>
<p>Balíček Štart: audit webu a kľúčové slová, technická oprava webu, 2 obsahové stránky alebo prepisy, firemný Google profil v poriadku a mesačný report. Za 240 EUR (Rast) k tomu 4 až 6 obsahových stránok mesačne, optimalizácia pre AI vyhľadávače a linkbuilding (2 až 3 odkazy). Za 480 EUR plný e-shop predaj: texty kategórií, Merchant Center a report s tržbami z organiky.</p>
<h2>Kedy SEO oplatí</h2>
<p>Ak jeden zákazník má pre vás hodnotu 500 EUR, 120 EUR mesačne za web, ktorý ich privádza opakovane, sa vráti po jednom zákazníkovi. Prvý e-shop <a href="/sk/sluzby/seo-pre-eshopy/">Mikramt.sk</a> vygeneroval za 9 mesiacov 2 492,75 EUR online tržieb.</p>
"""
    faq = [
        ("Koľko stojí SEO na Slovensku?",
         "Agentúry s paušálmi: 300 až 1 500 EUR mesačne. Hodinová spolupráca: 12 EUR za hodinu, malý web 120 EUR mesačne, e-shop 240 až 480 EUR."),
        ("Prečo máte cenu verejne?",
         "Lebo transparentnosť šetrí obe strany čas. Cena je 12 EUR za hodinu, rozsah potvrdím v pláne po bezplatnom audite."),
        ("Musím podpísať zmluvu na 12 mesiacov?",
         "Nie. Pracujem mesačne, spoluprácu môžete skončiť kedykoľvek. Dôveru stavím na výsledkoch, nie na viazanosti."),
    ]
    return blog_post(slug="kolko-stoji-seo", label="Cenník", h1="Koľko stojí SEO v roku 2026?",
                     answer="SEO stojí 300 až 1 500 EUR mesačne pri paušáloch, pri hodinovej spolupráci od 120 EUR mesačne. Prečo je cena 12 EUR za hodinu verejná a čo za ňu dostanete.",
                     sections=sections, faq=faq,
                     related=[("seo-optimalizacia-navod", "SEO optimalizácia: kompletný návod"), ("seo-test-15-bodov", "SEO test: 15-bodový kontrolný zoznam")])
    body = f"""
{page_hero("Blog", "Praktické články o SEO a AI",
           "Každý článok píšeme na kľúčové slovo s overeným dopytom (Marketing Miner). Prvé články vychádzajú tento mesiac.", [("Domov", "/"), ("Blog", None)])}
<section class="section">
  <div class="container">
    <div class="grid-2">{cards}</div>
    <div style="text-align:center; margin-top:36px;">
      <p style="color:var(--text-muted);">Chcete o niečom vedieť viac už teraz? Zavolajte <a href="tel:+421917316105" style="font-weight:700; color:var(--text);">+421 917 316 105</a> alebo napíšte.</p>
      <a href="/sk/kontakt/" class="btn btn-primary" style="margin-top:14px;">Kontaktovať</a>
    </div>
  </div>
</section>
"""
    html = base(market="sk", path="blog/", title="Blog o SEO, Google Mapách a AI vyhľadávačoch | Nokto Studio",
                desc="Praktické články: SEO návod krok za krokom, koľko stojí SEO v 2026, SEO test webu, linkbuilding, Google firemný profil a SEO pre WordPress.",
                canonical=BASE + "/sk/blog/", body=body, prefix="../..", extra_head=ORG_SCHEMA)
    return ("sk/blog/index.html", html)


# ---------------------------------------------------------------- SK ROOT REDIRECT STUB

def sk_redirect() -> tuple[str, str]:
    html = """<!DOCTYPE html>
<html lang="sk">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
           "Spracovávam len dáta, ktoré potrebujem na odpoveď a spoluprácu. Žiadny predaj dát tretím stranám.",
           [("Domov", "/"), ("Ochrana súkromia", None)])}
<section class="section">
  <div class="container prose">
    <h2>Kto spracováva údaje</h2>
    <p>Operátorom osobných údajov je Nokto Studio (Šimon Štermenský, prevádzkovateľ webu noktostudio.com). Kontakt: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    <h2>Aké údaje a načo</h2>
    <ul>
      <li>Kontaktný formulár: meno, e-mail, adresa webu a správa. Účelom je odpovedať na váš dotaz. Formulár odosiela oznámenie na náš e-mail.</li>
      <li>Telefonát: číslo, z ktorého voláte, ak si ho zapisujeme na spätné doplnenie informácií. Účelom je uskutočniť hovor.</li>
      <li>Analytika: anonymizované dáta o návštevnosti (Google Analytics 4, Microsoft Clarity) na zlepšovanie webu.</li>
    </ul>
    <h2>Ako dlho údaje uchovávam</h2>
    <p>Kontakty z formulárov a telefonátov uchovávam maximálne 24 mesiacov od poslednej komunikácie, pokiaľ nevznikne spolupráca.</p>
    <h2>Vaše práva</h2>
    <p>Máte právo na prístup k údajom, ich opravu, výmaz a prenos. Požiadavku pošlite na <a href="mailto:{EMAIL}">{EMAIL}</a>. Máte tiež právo podať sťažnosť na Úrad na ochranu osobných údajov SR.</p>
    <h2>Cookies</h2>
    <p>Web používa analytické cookies po vašom súhlase (cookie banner). Technické cookies nevyhnutné pre prevádzku webu sú povolené vždy.</p>
  </div>
</section>
"""
    html = base(market="sk", path="privacy/", title="Zásady ochrany súkromia | Nokto Studio",
                desc="Zásady ochrany súkromia webu noktostudio.com: aké údaje spracovávame, na čo a aké máte práva.",
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
    <p>Tieto podmienky upravujú spoluprácu medzi Nokto Studio (ďalej „poskytovateľ“) a klientom pri poskytovaní marketingových služieb: SEO optimalizácia, tvorba webov, PPC kampane, e-mail marketing a súvisiace poradenstvo.</p>
    <h2>2. Cena a fakturácia</h2>
    <p>Služby sa účtujú hodinovou sadzbou 12 EUR za odpracovanú hodinu. Fakturácia prebieha mesačne spätne na základe reportu odpracovaných hodín. Reklamné výdavky a náklady na odkazy či nástroje tretích strán sa účtujú v skutočnej cene bez prirážky.</p>
    <h2>3. Doba spolupráce</h2>
    <p>Spolupráca je dohodnutá na dobu neurčitú s mesačným cyklom. Klient aj poskytovateľ môžu spoluprácu ukončiť ku koncu kalendárneho mesiaca, písomne a bez sankcií.</p>
    <h2>4. Zodpovednosť a výsledky</h2>
    <p>Poskytovateľ nezaručuje konkrétne pozície vo vyhľadávačoch ani konkrétne objemy návštevnosti. Zaručuje odvedenú prácu, transparentné vykazovanie a postup podľa dohodnutého plánu. Záruky konkrétnych pozícií nie sú možné a ani nie sú poskytované.</p>
    <h2>5. Práva k obsahu</h2>
    <p>Obsah vytvorený pre klienta v rámci platenej spolupráce prechádza na klienta po zaplatení faktúry. Poskytovateľ môže prácu ukázať v portfóliu po dohode s klientom.</p>
    <h2>6. Zakázané praktiky</h2>
    <p>Poskytovateľ nepoužíva praktiky porušujúce pokyny vyhľadávačov (nákup odkazov zo sietí automatizovaného spamu, skryté texty, duplicitný obsah). Sankcie za porušenie pokynov sú skutočné riziko, preto sa im zásadovo vyhýbame.</p>
  </div>
</section>
"""
    html = base(market="sk", path="terms/", title="Obchodné podmienky | Nokto Studio",
                desc="Obchodné podmienky Nokto Studio: hodinová sadzba 12 EUR, mesačná fakturácia, bez viazanosti, transparentné vykazovanie.",
                canonical=BASE + "/sk/terms/", body=body, prefix="../..", extra_head=ORG_SCHEMA)
    return ("sk/terms/index.html", html)


# ---------------------------------------------------------------- /SK/PRIPADY REDIRECT STUB

def vysledky_redirect() -> tuple[str, str]:
    html = """<!DOCTYPE html>
<html lang="sk">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Nokto Studio | Výsledky</title>
  <link rel="canonical" href="https://noktostudio.com/sk/vysledky/">
  <meta http-equiv="refresh" content="0; url=/sk/vysledky/">
</head>
<body>
<p>Pokračujte na <a href="/sk/vysledky/">výsledky</a>.</p>
</body>
</html>
"""
    return ("sk/pripady/index.html", html)


def blog_post_seo_test() -> tuple[str, str]:
    donut = _donut([(4, _VIOLET, "Technika"), (4, _ORANGE, "Obsah"), (4, _CERULEAN, "Profil"), (3, _VIOLET_L, "AI")])
    sections = f"""
<h2>Stručná odpoveď</h2>
<p>Tento SEO test prejde váš web za 30 minút. 15 kontrolných bodov v štyroch oblastiach: technika (4), obsah (4), Google firemný profil (4) a AI viditeľnosť (3). Za každým zlyhaným bodom je konkrétna oprava. Ak zlyhá viac ako 5 bodov, web stráca zákazníkov každý deň.</p>
<figure class="blog-chart">{donut}</figure>
<h2>Technika (4 body)</h2>
<p>1. Načíta sa hlavná stránka do 3 sekúnd na mobile? Test: <a href="https://pagespeed.web.dev/" target="_blank" rel="noopener noreferrer">PageSpeed Insights</a> (zdarma). 2. Google indexuje všetky dôležité stránky? Test: zadajte site:vasadomena.sk do Google Vyhľadávania. 3. Má každá stránka unikátny titulok s dopytom zákazníka? 4. Sú interné linky na obsahové stránky (minimálne 3 na kategóriu)?</p>
<h2>Obsah (4 body)</h2>
<p>5. Každá kategória a služba má vlastný text aspoň na 3 odseky? 6. Texty odpovedajú na otázky, ktoré zákazníci pýtajú (cena, ako, porovnanie)? 7. Blog má články na reálne dopyty, nie firemné správy? 8. Hlavičky H1 až H3 nesú kľúčové slová, nie generické nadpisy?</p>
<h2>Google firemný profil (4 body)</h2>
<p>9. Profil má vyplnené kategórie, služby a otváracie časy? 10. Fotky sú mladšie ako 6 mesiacov? 11. Hodnotenia máte a odpovedáte na ne? 12. Q&A sekcia je zaplnená reálnymi otázkami?</p>
<h2>AI viditeľnosť (3 body)</h2>
<p>13. ChatGPT a AI Overviews vaše meno vedia, keď pýtajú odporúčanie? Testujte: „Odporúč mi [služba] v [mesto]". 14. Prvé 60 slov každej stránky odpovedá priamo na dopyt? 15. Web má štruktúrované dáta? Overte ich <a href="https://search.google.com/test/rich-results" target="_blank" rel="noopener noreferrer">Rich Results Testom od Google</a>.</p>
<h2>Čo ďalej</h2>
<p>Ak zlyhalo viac ako 5 bodov, objednajte si <a href="/sk/sluzby/seo-audit/">SEO audit</a>: do 3 dní máte 10 najväčších problémov a šancí na jednej strane. Ak zlyhalo menej, zoznam priamo hovorí, čo doplniť.</p>
"""
    faq = [
        ("Ako dlho trvá SEO test?",
         "Kontrolný zoznam prejde ručne za 30 minút. Detailný audit s prioritami a odhadom hodín trvá 20 až 40 hodín podľa rozsahu webu."),
        ("Je test zdarma?",
         "Tento zoznam áno. Bezplatný vstupný audit urobím tiež zdarma: 10 problémov a šancí do 3 dní."),
        ("Čo ak zlyhá veľa bodov?",
         "To je dobrá správa: viete, kde sú šance. Audit zoradí opravy podľa vplyvu na zákazníkov, nie podľa ľahkosti."),
    ]
    return blog_post(slug="seo-test-15-bodov", label="SEO test", h1="SEO test: 15-bodový kontrolný zoznam pre váš web",
                     answer="SEO test za 30 minút: 15 bodov v technike, obsahu, Google firemnom profile a AI viditeľnosti. Každý zlyhaný bod je konkrétna úspora zákazníkov.",
                     sections=sections, faq=faq,
                     related=[("seo-optimalizacia-navod", "SEO optimalizácia: kompletný návod"), ("kolko-stoji-seo", "Koľko stojí SEO v roku 2026?")])


def blog_post_linkbuilding() -> tuple[str, str]:
    price_chart = _bars([50, 80, 150, 300], _ORANGE, ["adresár", "branza", "mediálne PR", "silná doména"])
    sections = f"""
<h2>Stručná odpoveď</h2>
<p>Linkbuilding je získavanie spätných odkazov z iných webov. Google ich číta ako hlasovanie o vašej autorite. Realná cena odkazu na slovenskom trhu je 50 až 300 EUR, mediálne PR články stojí viac. Bezpečné metódy: obsah, ktorý odkazy nesie, partneri a branžové weby. Google sankcionuje siete automatického spamu.</p>
<figure class="blog-chart">{price_chart}</figure>
<h2>Čo je to spätný odkaz a prečo má váhu</h2>
<p>Spätný odkaz (backlink) je odkaz z cudzieho webu na váš. Google ho číta ako hlas: odkaz z reálnej, tematicky zodpovedajúcej domény prenáša autoritu. Odkaz z siete spamových domén vyvoláva opak: riziko sankcie. Čo presne Google zakazuje, popisujú <a href="https://developers.google.com/search/docs/essentials/spam-policies" target="_blank" rel="noopener noreferrer">oficiálne spam pravidlá Google</a>.</p>
<h2>Čo stojí odkaz v 2026</h2>
<p>Adresáre a základné branže: 50 až 80 EUR. Odvetvové weby a regionálne média: 80 až 150 EUR. Silné mediálne PR články: 150 až 300 EUR a viac. Cena závisí od domény, temy a čitateľnosti. Každý odkaz vykazujem so skutočnou cenou od média, bez prirážky.</p>
<h2>Bezpečný linkbuilding krok za krokom</h2>
<p>1. Rozbor link profilu: čo vás brzdí a ktoré odkazy chýbajú. 2. Tématické a lokálne odkazy: adresáre, branže, média, partneri. 3. Obsah a PR články, ktoré odkazy nesú: obsah musí stáť za odkaz, nielen kotva. 4. Sledovanie nových a stratených odkazov. Celý proces popisuje <a href="/sk/sluzby/linkbuilding/">linkbuilding služba</a>.</p>
<h2>Čo nerobiť</h2>
<p>Nákup zo sietí automatizovaného spamu, skryté texty a duplicitný obsah. Porušenie pravidiel hrozí sankciou, preto sa im vyhýbam zásadne. Odkazy bez obsahu a techniky nefungujú: len v kombinácii s obsahom prinášajú pozície.</p>
<h2>Príklad z praxe</h2>
<p>E-shop, ktorý som posilnil obsahom a odkazmi z reálnych slovenských domén: 8 950 zobrazení (+246 %) a 5 násobný rast klikov za 5 mesiacov. Odkazy fungujú len v kombinácii s obsahom a technikou.</p>
"""
    faq = [
        ("Koľko stojí jeden odkaz?",
         "Väčšina slovenských odkazov stojí 50 až 300 EUR, mediálne PR články viac. Vykazujem skutočné ceny od média, bez prirážky."),
        ("Ako dlho trvá, kým odkazy pomôžu?",
         "Nové odkazy sa uplatnia v 4 až 12 týždňoch. Preto kombinujeme linkbuilding s obsahovou prácou, ktorá už teraz niečo prináša."),
        ("Robíte kupovanie odkazov?",
         "Odkazy z reálnych domén áno, siete automatického spamu nie. Porušenie pravidiel hrozí sankciou, preto sa im vyhýbám."),
    ]
    return blog_post(slug="linkbuilding-co-to-je", label="Linkbuilding", h1="Linkbuilding: čo to je, čo stojí a ako sa robí bezpečne",
                     answer="Linkbuilding je získavanie spätných odkazov. Realná cena odkazu: 50 až 300 EUR, PR články viac. Bezpečné metódy a čo Google sankcionuje.",
                     sections=sections, faq=faq,
                     related=[("kolko-stoji-seo", "Koľko stojí SEO v roku 2026?"), ("seo-optimalizacia-navod", "SEO optimalizácia: kompletný návod")])


def blog_post_gbp() -> tuple[str, str]:
    donut = _donut([(193, _VIOLET, "Maps"), (166, _VIOLET_L, "Search")])
    sections = f"""
<h2>Stručná odpoveď</h2>
<p>Google firemný profil (Business Profile) je kart vašej firmy v Google Mapách a Vyhľadávaní. Nastavíte ho za 8 hodín: založenie a overenie, kategórie a služby, fotky, Q&A a stratégiu hodnotení. Klienti, ktorí hľadajú lokálne služby, vás nájdu prví: 54 % zobrazení profilu prichádza cez Mapy, 46 % cez Vyhľadávanie.</p>
<figure class="blog-chart">{donut}</figure>
<h2>Krok 1: Založenie a overenie</h2>
<p>Profil vytvoríte na <a href="https://www.google.com/business/" target="_blank" rel="noopener noreferrer">google.com/business</a>. Dôležité je presné meno (bez doplnených kľúčových slov, Google to zakazuje), adresa pôsobiska a kategória. Overenie bežne prebehne listom alebo telefónom, <a href="https://support.google.com/business/answer/3038177" target="_blank" rel="noopener noreferrer">podrobnosti v pomoci Google</a>.</p>
<h2>Krok 2: Kategórie a služby</h2>
<p>Primárna kategória je najdôležitejší signál: rozhodne, na ktoré dopyty sa profil zobrazí. Doplní sekundárne kategórie, služby s cenami a popis, ktorý odpovedá na otázky zákazníkov.</p>
<h2>Krok 3: Fotky a Q&A</h2>
<p>Fotky mladšie ako 6 mesiacov pôsobia aktívne. Q&A doplním otázkami, ktoré zákazníci reálne pýtajú (parkovanie, platba, pôsobisko), a odpoveďami. Google tento obsah cituje aj v AI odpovediach.</p>
<h2>Krok 4: Hodnotenia cez SMS a QR kód</h2>
<p>Postup cez SMS a QR kód vyzve zákazníka hneď po vykonanej službe. Miera recenzií rastie násobne, lebo zákazník má link v ruke v čase, keď je spokojný. Na hodnotenia odpovedám profesionálne a na mieste.</p>
<h2>Krok 5: Týždenné vyhodnotenie</h2>
<p>Prehľad: volania, žiadosti o trasu, zobrazenia v mape. Príklad z praxe: 359 ľudí videlo firemný profil klienta za jedno obdobie, 54 % cez Mapy a 46 % cez Vyhľadávanie. Nastavenie a vedenie profilu rieši <a href="/sk/sluzby/lodalne-seo/">lokálne SEO</a>.</p>
"""
    faq = [
        ("Koľko trvá, kým Google profil začne fungovať?",
         "Prvé zlepšenia viditeľné za 4 až 8 týždňov, stabilná pozícia trvá 3 až 6 mesiacov. Záleží na konkurencii v okolí."),
        ("Mám len jedno pôsobisko. Oplatí sa mi to?",
         "Práve pre jedno pôsobisko je lokálne SEO najúčinnejšie. Sústredíte všetku silu do vášho mesta a okresu, kde je konkurencia najmenšia."),
        ("Ako získam viac hodnotení na Google?",
         "Postup cez SMS a QR kód hneď po vykonanej službe. Zákazník má link v ruke v čase, keď je spokojný."),
    ]
    return blog_post(slug="google-firmy-profil-navod", label="Lokálne SEO", h1="Google firemný profil: návod od založenia po hodnotenia",
                     answer="Google firemný profil nastavíte za 8 hodín: založenie, kategórie, fotky, hodnotenia cez SMS a QR kód. Návod s prípadovou štúdiou z praxe.",
                     sections=sections, faq=faq,
                     related=[("seo-test-15-bodov", "SEO test: 15-bodový kontrolný zoznam"), ("seo-wordpress", "SEO pre WordPress: 12 nastavení")])


def blog_post_wordpress() -> tuple[str, str]:
    wp_chart = _bars([4, 3, 3, 2], _CERULEAN, ["rýchlosť", "štruktúra", "schéma", "obsah"])
    sections = f"""
<h2>Stručná odpoveď</h2>
<p>SEO pre WordPress vyžaduje 12 konkrétnych nastavení: permalinky, sitemap, rýchlosť (cache + WebP), meta titulky a popisky, štruktúrované dáta, interné prelinkovanie, robots.txt, alt texty, mobilná verzia, kanonizácie, ďaľší plugin na SEO a meranie v Search Console. Zaberá to 6 až 10 hodín.</p>
<figure class="blog-chart">{wp_chart}</figure>
<h2>Rýchlosť (4 body)</h2>
<p>1. Cache plugin (WP Rocket alebo LiteSpeed Cache) zapnutý a nakonfigurovaný. 2. Obrázky vo WebP a lazy loading. 3. Fonty lokálne alebo preconnect na Google Fonts. 4. LCP prvok pod 2,5 s na mobile: PageSpeed Insights test.</p>
<h2>Štruktúra (3 body)</h2>
<p>5. <a href="https://wordpress.org/documentation/article/settings-permalinks-screen/" target="_blank" rel="noopener noreferrer">Permalinky</a> na „/%postname%/". 6. XML sitemap generovaná a odoslaná do Search Console. 7. Robots.txt, ktorý neblokuje indexáciu dôležitých stránok.</p>
<h2>Meta a schéma (3 body)</h2>
<p>8. Yoast alebo RankMath: unikátne titulky s dopytom zákazníka na každej stránke. 9. Meta popisky, ktoré čerpajú z reálnych dopytov. 10. Štruktúrované dáta: LocalBusiness, FAQPage, Service podľa typu stránky.</p>
<h2>Obsah (2 body)</h2>
<p>11. Alt texty na všetkých obrázkoch, ktoré nesú kľúčové slovo. 12. Interné prelinkovanie: každá obsahová stránka má 3 interné odkazy.</p>
<h2>WordPress vs. iné platformy</h2>
<p>Pri SEO má nástroj druhoradú úlohu: dôležitá je stratégia a jej vykonávanie. WordPress, Shoptet, WooCommerce aj vlastné riešenia sa optimalizujú rovnakými princípmi.</p>
"""
    faq = [
        ("Ktorý plugin na SEO v WordPress je najlepší?",
         "<a href=\"https://yoast.com/\" target=\"_blank\" rel=\"noopener noreferrer\">Yoast</a> aj <a href=\"https://rankmath.com/\" target=\"_blank\" rel=\"noopener noreferrer\">RankMath</a> sú v poriadku. Dôležitý nie je plugin, ale to, že ste nastavenia vyplnili: titulky, schéma, sitemap."),
        ("Zaberie to viac ako 12 nastavení?",
         "Základ je 12 bodov. Na konkurenčných dopytoch k tomu prichádza obsah, interné prelinkovanie a AI viditeľnosť."),
        ("Pomôžete aj s implementáciou?",
         "Áno, 12 bodov nastavím priamo v CMS alebo pripravím súbor pre vývojára. Základ popisuje <a href=\"/sk/sluzby/seo-optimalizacia/\">SEO optimalizácia webu</a>."),
    ]
    return blog_post(slug="seo-wordpress", label="WordPress", h1="SEO pre WordPress: 12 nastavení, ktoré treba spraviť",
                     answer="SEO pre WordPress: 12 konkrétnych nastavení od permalinks po schému. Prejde sa za 30 minút, implementuje v 6 až 10 hodinách.",
                     sections=sections, faq=faq,
                     related=[("seo-optimalizacia-navod", "SEO optimalizácia: kompletný návod"), ("kolko-stoji-seo", "Koľko stojí SEO v roku 2026?")])


# ---------------------------------------------------------------- BLOG LISTING

# Blog card data. Excerpts are the direct answers of each article, read dates
# match the launch date. No search-volume badges on the public page.
_BLOG_CARDS = [
    dict(slug="seo-optimalizacia-navod", cat="Návod", tag="tag-violet",
         title="SEO optimalizácia: kompletný návod 2026",
         excerpt="SEO optimalizácia krok za krokom: audit, plán s číslami, týždenná práca a mesačné meranie. Postup pre malé firmy, s reálnymi číslami z praxe."),
    dict(slug="kolko-stoji-seo", cat="Cenník", tag="tag-cerulean",
         title="Koľko stojí SEO v roku 2026?",
         excerpt="Ceny od 300 do 1 500 EUR mesačne pri paušáloch, pri hodinovej spolupráci od 120 EUR mesačne. Prečo je cena 12 EUR za hodinu verejná a čo za ňu dostanete."),
    dict(slug="seo-test-15-bodov", cat="SEO test", tag="tag-violet-light",
         title="SEO test: 15-bodový kontrolný zoznam pre váš web",
         excerpt="Prejdite si web sami za 30 minút: 15 bodov v technike, obsahu, Google firemnom profile a AI viditeľnosti. Za každým zlyhaným bodom je konkrétna oprava."),
    dict(slug="linkbuilding-co-to-je", cat="Linkbuilding", tag="tag-orange",
         title="Linkbuilding: čo to je, čo stojí a ako sa robí bezpečne",
         excerpt="Čo sú spätné odkazy, reálna cena 50 až 300 EUR, bezpečné metódy a čo Google sankcionuje. Návod s príkladmi z praxe."),
    dict(slug="google-firmy-profil-navod", cat="Lokálne SEO", tag="tag-violet",
         title="Google firemný profil: návod od založenia po hodnotenia",
         excerpt="Založenie, overenie, kategórie, fotky a hodnotenia cez SMS a QR kód. Profil nastavíte za 8 hodín, návod s prípadovou štúdiou."),
    dict(slug="seo-wordpress", cat="WordPress", tag="tag-cerulean",
         title="SEO pre WordPress: 12 nastavení, ktoré treba spraviť",
         excerpt="Permalinky, sitemap, rýchlosť, meta titulky a schéma. 12 konkrétnych nastavení, ktoré posunú pozície WordPress webu."),
]


def _blog_card(c: dict, featured: bool = False) -> str:
    href = f"/sk/blog/{c['slug']}/"
    return f"""
<a href="{href}" class="blog-card{' blog-featured' if featured else ''}">
  <div><span class="project-tag {c['tag']}">{c['cat']}</span></div>
  <h3>{c['title']}</h3>
  <p>{c['excerpt']}</p>
  <div class="blog-card-foot"><span class="blog-date">10. 9. 2026</span><span class="blog-read">Čítať článok →</span></div>
</a>"""


def blog() -> tuple[str, str]:
    featured = _BLOG_CARDS[0]
    cards = "".join(_blog_card(c) for c in _BLOG_CARDS[1:])
    body = f"""
{page_hero("Blog", "Praktické články o SEO a AI",
           "Návody, ceny a kontrolné zoznamy z praxe. Každý článok vychádza z dopytov, ktoré zákazníci reálne pýtajú.", [("Domov", "/"), ("Blog", None)])}
<section class="section">
  <div class="container">
    <div class="blog-grid">{_blog_card(featured, featured=True)}{cards}</div>
  </div>
</section>
<section class="section" style="padding-top:0;">
  <div class="container">
    {cta_band("Chcete článok ako prvý?", "Začnime bezplatným auditom, z neho vychádza aj obsahový plán.", "sk")}
  </div>
</section>
"""
    html = base(market="sk", path="blog/", title="Blog o SEO, Google Mapách a AI vyhľadávaní | Nokto Studio",
                desc="Praktické články: SEO návod krok za krokom, koľko stojí SEO v 2026, SEO test webu, linkbuilding, Google firemný profil a SEO pre WordPress.",
                canonical=BASE + "/sk/blog/", body=body, prefix="../..", extra_head=ORG_SCHEMA)
    return ("sk/blog/index.html", html)
