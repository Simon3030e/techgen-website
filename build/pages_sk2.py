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
    c_klient1 = _bars([38, 42, 61, 115, 145], _VIOLET_L,
                      ["marec", "apríl", "máj", "jún", "aug"])
    c_klient2 = _bars([182, 293, 329, 413], _VIOLET_L, ["jún", "júl", "aug", "sep"])
    c_itc = _sparkline([40, 55, 48, 62, 58, 75, 70, 88, 95, 92, 110, 121], _VIOLET)
    blocks = "".join([
        result_block(
            title="Elektroservis (klient)", period="marec až september 2026",
            nums=[{"big": "991", "color": _VIOLET, "label": "klikov z Google za 28 dní (+6 %)"},
                  {"big": "72 873", "color": _ORANGE, "label": "zobrazení za 28 dní (+3 %)"},
                  {"big": "96", "color": _VIOLET_L, "label": "citácií v AI odpovediach"}],
            chart=c_klient1,
            caption="Dva expertné články, ktoré som napísal, Google cituje v AI odpovediach a odporúča klienta zákazníkom. Web 69 stránok: 9 700 → 12 000 zobrazení za 28 dní (+24 %). Graf: rast hlavných stránok v percentách.",
            source="Google Search Console, posledných 28 dní (k septembru 2026)",
            partner="", market="sk"),
        result_block(
            title="E-shop s oblečením (vlastný projekt)", period="Search Console + AI Mode, jún až september 2026",
            nums=[{"big": "893", "color": _VIOLET_L, "label": "zobrazení v Google AI Mode za 3 mesiace"},
                  {"big": "+80 %", "color": _VIOLET, "label": "august oproti júnu (182 → 329)"},
                  {"big": "413", "color": _ORANGE, "label": "klikov na hlavnú kategóriu"}],
            chart=c_klient2,
            caption="Google AI Mode cituje e-shop denne po nasadení môjho obsahu. Rast mesačne: jún 182, júl 293, august 329. Najviac citované: homepage a blogové články (174, 167 a 119 citácií). Kategórie majú desiatky tisíc organických zobrazení mesačne. Konkurencia v AI odpovediach ešte nie je.",
            source="Google Search Console + Google AI Mode (report citácií), jún až september 2026",
            partner="own", market="sk"),
        result_block(
            title="Aplikácia pre reality (klient)", period="posledných 28 dní",
            nums=[{"big": "121", "color": _VIOLET, "label": "klikov z Google (+49 %)"},
                  {"big": "4 390", "color": _ORANGE, "label": "zobrazení (+43 %)"},
                  {"big": "+142 %", "color": _VIOLET_L, "label": "rast hlavnej stránky"}],
            chart=c_itc,
            caption="SEO od nuly: technické SEO a obsah v prvom mesiaci spolupráce, Google začal prinášať zákazníkov hneď.",
            source="Google Search Console",
            partner="own", market="sk"),
        result_block(
            title="E-shop s meracími zariadeniami (klient)", period="január až september 2026, rework v priebehu",
            nums=[{"big": "203", "color": _VIOLET, "label": "klikov z Google od založenia"},
                  {"big": "3 266", "color": _ORANGE, "label": "zobrazení od založenia"},
                  {"big": "2", "color": _VIOLET_L, "label": "zákazky ešte pred dokončením projektu"}],
            chart=_sparkline([12, 33, 203, 380, 620, 900], _VIOLET),
            caption="E-shop s produktmi na monitorovanie energie. Zákazky prišli ešte pred dokončením one-time projektu: web dostáva objednávky z organického vyhľadávania aj napriek tomu, že rework sa tek prebieha. Pozícia v priemere 10,0, CTR 6,2 %. Po nasadení novej verzie očakávame násobný rast.",
            source="Google Search Console, január až september 2026",
            partner="flamia", market="sk"),
        result_block(
            title="Villa Paris, Piešťany", period="rebrand + web + lokálne SEO",
            nums=[],
            chart="",
            caption="Prémiové ubytovanie. Rebrand, nový web, hotelový copywriting a lokálne SEO v jednom systéme. Značku a web robíme v spolupráci s Flamia Studio. Cieľ: viac priamych rezervácií bez provízií.",
            source="príbeh projektu na /sk/villa-paris/",
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
        <h3>E-shop: spolupráca pokračuje</h3>
        <p>Zákazník bol spokojný s prvým e-shopom, takže teraz robíme rework: viac produktov a lepšie SEO.</p>
      </div>
      <div class="benefit-card card-hover">
        <span class="benefit-icon">{gicon("ai", "#6A3FC4", 26)}</span>
        <h3>Elektroservis: mesačná spolupráca beží</h3>
        <p>991 klikov a 96 citácií v AI odpovediach za posledných 28 dní. Report vychádza každý mesiac s číslami.</p>
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
        <p>Do 24 hodín sa ozvem osobne s prvými návrhmi pre váš web. Bezplatný vstupný audit: čo brzdí vaše pozície, predaj a AI odporúčania.</p>
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
    html = base(market="sk", path="vysledky/", title="Výsledky SEO: kliky, zobrazenia, AI citácie | Nokto Studio",
                desc="Reálne výsledky z Google Search Console: 991 klikov a 96 citácií v AI odpovediach pre elektroservis, 893 zobrazení v AI Mode pre e-shop, 203 klikov a zákazky ešte pred dokončením projektu. Čísla z praxe.",
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
         "12 EUR za odpracovanú hodinu. Malý firemný web zvyčajne 10 hodín mesačne (120 EUR), e-shop 10 až 15 hodín (120 až 180 EUR). Balíčky sú odporúčané rozsahy, nie povinné paušály."),
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
           "Najrýchlejšia cesta je telefón. Alebo pošlite formulár a do 24 hodín sa ozvem osobne s prvými návrhmi.",
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
    """REFRESH 2026-09-16. Target: 'seo optimalizacia navod' (1200 SV/mo, diff 27, +342% YoY).
    SERP: all CZ guides (dusansoucek, seoprakticky, mediaunit, eway-crm). No SK author with
    first-party GSC data. Angle: SK-first 4-step guide with real GSC screenshots + 2026 update."""
    sections = f"""
<h2>Stručná odpoveď</h2>
<p>SEO optimalizácia je oprava technickej stránky webu a písanie obsahu na dopyty, ktoré zákazníci reálne hľadajú. Funguje v štyroch krokoch: audit, plán s číslami, týždenná práca a mesačné meranie. Prvé pohyby na menej konkurenčných dopytoch vidíte za 2 až 4 mesiace, na hlavné dopyty 6 až 12 mesiacov. Na slovenskom trhu stojí od 120 EUR mesačne pri hodinovej spolupráci (12 EUR/hod, 10 hodín pre malý web).</p>
<figure class="blog-chart">{_flow_chart()}</figure>

<h2>Čo je SEO optimalizácia a ako Google hodnotí web</h2>
<p>SEO (Search Engine Optimization) je optimalizácia webu tak, aby ho Google a ďalšie vyhľadávače (Seznam, Bing) zaradili čo najvyššie vo výsledkoch vyhľadávania. Google hodnotí web podľa troch hlavných skupín faktorov: <strong>technika</strong> (rýchlosť, indexácia, štruktúrované dáta, mobilná verzia), <strong>obsah</strong> (relevantnosť k dopytu, kvalita, E-E-A-T signály), a <strong>autorita</strong> (spätné odkazy, brand mentions, Google profil). Žiadny jeden faktor nerozhoduje samostatne, ale bez techniky obsah nefunguje, a bez obsahu odkazy nemajú kam viesť.</p>
<p>Google od roku 2023 používa AI na hodnotenie obsahu (Helpful Content Update), od marca 2025 posilnil E-E-A-T signály (Experience, Expertise, Authoritativeness, Trustworthiness), a od augusta 2024 nahradil FID metriku INP (Interaction to Next Paint). V roku 2026 pridáva AI Overviews, ktoré citujú weby priamo v AI odpovediach. To znamená, že SEO už nie je len o pozíciách, ale aj o tom, či vás AI cituje.</p>

<h2>Ako som urobil SEO na slovenskom webe: 250 klikov za 3 mesiace</h2>
<p>Konkrétny prípad z mojej praxe v roku 2026: firemný web, ktorý som prevzal s minimálnou organickou návštevnosťou (niekoľko klikov mesačne). Po 3 mesiacoch SEO práce dosiahol 250 klikov z Google (+355 %) a 8 950 zobrazení mesačne (+246 %). Práca pozostávala z:</p>
<ul>
<li><strong>Audit</strong>: našiel som 15 technických chýb (pomaly LCP 4.2s, chýbajúce canonical, 404 chyby, bez schema)</li>
<li><strong>Technická oprava</strong>: LCP na 2.1s, canonical tagy, 301 redirecty, Organization + BreadcrumbList schema</li>
<li><strong>6 obsahových stránok</strong> na reálne dopyty zákazníkov (long-tail, nízka konkurencia, 50-200 SV/mo každý)</li>
<li><strong>Interné prelinkovanie</strong>: silné stránky posunuli nové obsahy</li>
<li><strong>Google firemný profil</strong>: kompletné nastavenie, 359 zobrazení profilu za mesiac</li>
</ul>
<p>Tento výsledok nie je jednorazový skok, ale mesačný rast: každý mesiac viac klikov, žiadny výkyv. Presné GSC screenshoty vám ukážem na bezplatnom audite.</p>
<p><em>Zdroj: Google Search Console klienta, ukážka zo septembra 2026.</em></p>

<h2>Krok 1: Audit webu a kľúčových slov</h2>
<p>Začnite auditom. Zistite tri veci: či Google váš web správne indexuje, akou rýchlosťou sa načítava, a na ktoré dopyty už máte zobrazenia (aj na pozícii 40+). Nástroje sú bezplatné:</p>
<ul>
<li><strong><a href="https://search.google.com/search-console" target="_blank" rel="noopener noreferrer">Google Search Console</a></strong>: indexácia, kliky, zobrazenia, pozície. Najdôležitejší nástroj, bezplatný.</li>
<li><strong><a href="https://pagespeed.web.dev/" target="_blank" rel="noopener noreferrer">PageSpeed Insights</a></strong>: rýchlosť, Core Web Vitals (LCP, INP, CLS).</li>
<li><strong><a href="https://marketingminer.com" target="_blank" rel="noopener noreferrer">Marketing Miner</a></strong>: objemy dopytov na slovenskom trhu, difficulty, SERP analýza.</li>
<li><strong><a href="https://developers.google.com/search/docs/fundamentals/seo-starter-guide" target="_blank" rel="noopener noreferrer">SEO Starter Guide od Google</a></strong>: oficiálna príručka pre začiatočníkov.</li>
</ul>
<p>V Search Console choďte do Reports > Performance: uvidíte, na ktoré dopyty sa už zobrazujete, aká je vaša pozícia a CTR. Potom choďte do Pages > Indexing: uvidíte, koľko strán je indexovaných a koľko je "Crawled, currently not indexed" (častý problém tenkých kategórií).</p>
<p>Bezplatný vstupný audit urobím za vás: 10 najväčších problémov a šancí webu na jednej strane do 3 dní. <a href="/sk/sluzby/seo-audit/">Detailný SEO audit</a> má akčný plán s hodinami a prioritami.</p>

<h2>Krok 2: Plán s číslami</h2>
<p>Z auditu spravte plán. Rozhodujúce je vybrať dopyty s nízkou konkurenciou a reálnym objemom. Nový web nevyhrá národné pozície na "SEO optimalizácia" (diff 44), ale vyhrá na "seo optimalizacia pre malu firmu" alebo "seo pre stolara Nitra" (long-tail, nízka konkurencia).</p>
<p>Plán obsahuje: zoznam 5-10 cieľových kľúčových slov s objemom a difficulty, zoznam technických úloh s prioritami, počet nových obsahových stránok mesačne, odhad hodín a očakávaný dopad. Bez plánu strávite mesiace úsilím, ktoré možno smeruje zlým smerom.</p>

<h2>Krok 3: Týždenná práca</h2>
<p>Práca ide v dávkach. Týždenňá dávka obsahuje:</p>
<h3>Technická optimalizácia</h3>
<p>Rýchlosť: LCP pod 2.5s, INP pod 200ms, CLS pod 0.1. Opravíte cez WebP obrázky, lazy loading, CDN, obmedzenie pluginov. Indexácia: sitemap.xml v Search Console, robots.txt umožňuje crawling, canonical tagy na každej stránke. Štruktúrované dáta: Organization, WebSite, BreadcrumbList, Article/Product JSON-LD. Core Web Vitals meriate cez PageSpeed Insights.</p>
<h3>Obsah na reálne dopyty</h3>
<p>Píšem <a href="/sk/sluzby/seo-optimalizacia/">obsahové stránky</a> na kľúčové slová, ktoré majú reálny dopyt podľa Marketing Minera. Každá stránka: H1 s kľúčovým slovom, 300-600 slov, priama odpoveď v prvých 60 slovách, H2-H3 hierarchia, alt texty obrázkov, interné odkazy. Nie copy-paste z AI, ale obsah s reálnou informačnou hodnotou.</p>
<h3>Google firemný profil a lokálne SEO</h3>
<p><a href="/sk/sluzby/lodalne-seo/">Google firemný profil</a>: kompletné dáta, fotky, hodnotenia, Q&A. Pre lokálne firmy je to najrýchlejší zdroj zákazníkov z Google.</p>
<h3>AI viditeľnosť</h3>
<p><a href="/sk/sluzby/seo-pre-ai-vyhladavace/">Optimalizácia pre AI vyhľadávače</a>: priame odpovede na otázky, ktoré zákazníci pýtajú v ChatGPT a Gemini. Štruktúrované dáta, ktoré AI číta. Prístup pre GPTBot a ClaudeBot (robots.txt).</p>

<h2>Krok 4: Meranie a report</h2>
<p>V Google Search Console sledujte: pozície na sledovaných kľúčových slovách, kliky a zobrazenia, CTR (ak je nízka, opravte title a meta description). V Google Analytics 4 sledujte: objednávky a konverzie z organického vyhľadávania, nie len návštevnosť.</p>
<p>Mesačný report obsahuje: čo sa urobilo, čo to prinieslo (pozície, kliky, objednávky), a čo je ďalší krok. Koľko to stojí rozoberá <a href="/sk/cennik/">cenník (12 EUR za hodinu)</a>. Príklad: firemný web, ktorý som prevzal s minimálnou návštevnosťou, dosiahol 250 klikov za 3 mesiace (+355 %) po technickej oprave a 6 obsahových stránkach.</p>

<h2>Za aký čas sa objavia výsledky</h2>
<p>Reálne časové rámce z mojich projektov:</p>
<ul>
<li><strong>Long-tail dopyty</strong> (nízka konkurencia, 50-200 SV/mo): 2-4 mesiace na pozíciu 1-10</li>
<li><strong>Lokálne dopyty</strong> (zubár Nitra, právnik Bratislava): 1-3 mesiace na map pack</li>
<li><strong>Komerčné dopyty</strong> (stredná konkurencia, 300-500 SV/mo): 4-8 mesiacov na pozíciu 5-15</li>
<li><strong>Hlavné dotazy</strong> (vysoká konkurencia, 500+ SV/mo): 6-12 mesiacov na pozíciu 5-10, s linkbuildingom</li>
</ul>
<p>Záleží na konkurencii v branži, stave webu, veku domény a množstve obsahu. Nový web (0 odkazov, 0 historie) potrebuje dlhší čas než existujúci web s autoritou.</p>

<h2>Čo zmenil rok 2026 v SEO</h2>
<p>Tri zmeny, ktoré ovplyvnili slovenský trh:</p>
<ol>
<li><strong>AI Overviews</strong>: Google zobrazuje AI odpovede priamo vo výsledkoch vyhľadávania. Cituje weby, ktoré majú priame odpovede v prvých 60 slovách a štruktúrované dáta. Pre SK trh je AI Overviews penetration zatiaľ nízka (pod 5 percent dotazov), ale rastie.</li>
<li><strong>INP nahradil FID</strong>: nová Core Web Vitals metrika pre interaktivitu. Cieľ pod 200ms. WordPress weby s mnohými pluginmi často zlyhávajú.</li>
<li><strong>March 2025 Core Update</strong>: posilnil E-E-A-T signály. Weby s autorom (Person schema, sameAs), dátumom a zdrojmi sa zaradili vyššie. Weby bez autora a s generickým obsahom klesli.</li>
</ol>

<h2>Čo nerobiť: 5 najčastejších chýb</h2>
<ol>
<li><strong>Optimalizovať na jedno kľúčové slovo</strong>: Google rozumie kontextu, nie presnej zhode. Píšte na tému, nie na jedno slovo.</li>
<li><strong>Kopírovať konkurenciu</strong>: ak skopírujete obsah konkurencie, Google ho zaradí pod nich, nie pod vás. Pridajte vlastné dáta, skúsenosti, prípady.</li>
<li><strong>Nepísať obsah</strong>: technická optimalizácia bez obsahu nefunguje. Bez obsahu Google nevie, na čo vás zaradiť.</li>
<li><strong>Kúpiť 100 odkazov za 200 EUR</strong>: spamové siete vás zničia. Jeden odkaz z SME.sk (DR 65) spraví viac než 100 z PBN.</li>
<li><strong>Ignorovať Google firemný profil</strong>: pre lokálne firmy je to najrýchlejší zdroj zákazníkov. Bez profilu chýbate v Mapách a v lokálnom pack.</li>
</ol>
"""
    faq = [
        ("Čo je SEO optimalizácia?",
         "SEO optimalizácia je úprava webu tak, aby ho Google a ďalšie vyhľadávače zaradili čo najvyššie vo výsledkoch vyhľadávania. Google hodnotí web podľa techniky (rýchlosť, indexácia), obsahu (relevantnosť, kvalita) a autority (odkazy, brand). Žiadny jeden faktor nerozhoduje samostatne."),
        ("Za aký čas uvidím výsledky?",
         "Prvé pohyby na menej konkurenčných dotazoch za 2-4 mesiace, na hlavné dotazy 6-12 mesiacov. Záleží na konkurencii, stave webu a veku domény. Nový web potrebuje dlhší čas než existujúci s autoritou."),
        ("Koľko hodín mesačne zaberie SEO?",
         "Firemný web zvládnem v 10 hodinách mesačne (120 EUR), e-shop v 10 až 15 hodinách (120 až 180 EUR). Rozsah potvrdím v pláne po audite. Detailnejšie v <a href='/sk/blog/kolko-stoji-seo/'>článku o cene SEO</a>."),
        ("Môžem robiť SEO sám?",
         "Áno, nástroje sú bezplatné (Search Console, PageSpeed, Marketing Miner). Ale SEO zaberie 10-20 hodín mesačne: audit, obsah, technika, meranie. Ak máte čas, skúste <a href='/sk/blog/seo-test-15-bodov/'>15-bodový SEO test</a> ako prvý krok."),
        ("Robíte aj obsah?",
         "Áno, písanie obsahu je súčasť hodín. Navrhnem štruktúru, napíšem texty na reálne dopyty a pred publikovaním ich schválite. Obsah nie je copy-paste z AI, má reálnu informačnú hodnotu."),
        ("Pomáha WordPress SEO plugin?",
         "Áno, Yoast alebo RankMath pridajú title/meta šablóny, schema, sitemap. Ale neopravia obsah a rýchlosť. Detailnejšie v <a href='/sk/blog/seo-wordpress/'>SEO pre WordPress návode</a>."),
        ("Ako zistím, na ktoré kľúčové slová už vidím?",
         "V Google Search Console choďte do Reports > Performance. Uvidíte, na ktoré dopyty sa už zobrazujete (aj na pozícii 40+), aká je vaša pozícia a CTR. Bezplatné."),
        ("Je SEO lepšie než PPC reklama?",
         "Nie je lepšie alebo horšie, je iné. PPC prináša okamžité výsledky, ale keď prestanete platiť, návštevnosť zmizne. SEO trvá mesiace, ale výsledky pretrvávajú roky. Ideálna kombinácia: PPC na okamžité výsledky, SEO na dlhodobú návštevnosť."),
    ]
    return blog_post(slug="seo-optimalizacia-navod", label="Návod", h1="SEO optimalizácia: kompletný návod 2026",
                     answer="SEO optimalizácia krok za krokom: audit, plán s číslami, týždenná práca a mesačné meranie. Návod pre malé firmy s reálnymi číslami z praxe: 250 klikov za 3 mesiace.",
                     sections=sections, faq=faq,
                     related=[("kolko-stoji-seo", "Koľko stojí SEO v roku 2026?"), ("seo-test-15-bodov", "SEO test: 15-bodový kontrolný zoznam")],
                     date_iso="2026-09-16", date_display="16. 9. 2026")


def blog_post_kolko_stoji() -> tuple[str, str]:
    """REFRESH 2026-09-16. Target: 'seo optimalizacia cena' (620 SV/mo, diff 20, +100% YoY).
    SERP: dejtonaweb, seolight, seoconsult, seoprakticky, mediaunit. All CZ, none with
    first-party ROI case. Angle: transparent 12 EUR/hod with real Mikramt ROI (1620 EUR
    input, 2492 EUR revenue in 9 months)."""
    price_chart = _bars([120, 180], _VIOLET, ["Štart 120 EUR", "Rast 180 EUR", "E-shop 180 EUR"])
    sections = f"""
<h2>Stručná odpoveď</h2>
<p>SEO na slovenskom trhu stojí od 120 do 180 EUR mesačne pri hodinovej spolupráci, alebo 300 až 1 500 EUR mesačne pri agentúrach s paušálmi. Ja účtujem 12 EUR za odpracovanú hodinu: malý firemný web zvládnem v 10 hodinách mesačne (120 EUR), e-shop v 10 až 15 hodinách (120 až 180 EUR). Neplatíte paušál, platíte za odpracovanú prácu. Detailný audit stojí 120 až 180 EUR jednorazovo, vstupný audit je bezplatný.</p>
<figure class="blog-chart">{price_chart}</figure>

<h2>Cenové modely SEO na slovenskom trhu</h2>
<p>Existujú tri cenové modely, každý má výhody a nevýhody:</p>
<table class="metric-table">
<tr><th>Model</th><th>Cena mesačne</th><th>Výhody</th><th>Nevýhody</th></tr>
<tr><td><strong>Hodinový</strong> (ja)</td><td>120 až 180 EUR</td><td>Transparentnosť, platíte za prácu, nie za paušál</td><td>Menej predvídateľné náklady</td></tr>
<tr><td><strong>Paušál agentúry</strong></td><td>300 až 1 500 EUR</td><td>Predvídateľnosť, fixný rozsah</td><td>Často neviditeľná práca, viazanosť 12 mesiacov</td></tr>
<tr><td><strong>Projektový</strong> (jednorazový)</td><td>120 až 180 EUR</td><td>Jasný rozsah, jednorazová platba</td><td>Bez priebežnej údržby a obsahu</td></tr>
</table>
<p>Väčšina slovenských agentúr účtuje paušál 300 až 1 500 EUR mesačne, často s 12-mesačnou zmluvou. Pri paušáli sa často nevie, čo za peniaze dostanete: koľko hodín reálne odpracujú, koľko obsahu napíšu, koľko odkazov kúpia. Preto fungujem na hodiny: každá hodina je vykazovaná v reporte s obsahom a výsledkom.</p>

<h2>Čo ovplyvňuje cenu SEO</h2>
<p>Tri veci rozhodujú o cene:</p>
<ol>
<li><strong>Rozsah webu</strong>: 5-stranový firemný web nie je 500-produktový e-shop. E-shop potrebuje texty kategórií, Merchant Center, feed optimalizáciu, viac času.</li>
<li><strong>Konkurencia na vašich dopytoch</strong>: "zubár Nitra" má nízku konkurenciu (2-3 mesiace na pozíciu), "seo optimalizacia" má vysokú (12+ mesiacov, linkbuilding).</li>
<li><strong>Rozsah obsahu</strong>: 2 obsahové stránky mesačne (Malý web (120 EUR)) nie sú 6 stránok (Stredný web (180 EUR)). Obsah je najviac času.</li>
</ol>
<p>Preto nefunguje univerzálna cena. Precením počty hodín v pláne po audite, s reálnymi číslami pre váš konkrétny web.</p>

<h2>Čo skutočne dostanete za 120 EUR mesačne (Malý web (120 EUR))</h2>
<p>10 hodín práce mesačne, rozdelených na:</p>
<ul>
<li>Audit webu a kľúčových slov (opakovanie, údržba)</li>
<li>Technická oprava webu: rýchlosť, indexácia, canonical, 404</li>
<li>2 obsahové stránky alebo prepisy existujúcich stránok</li>
<li>Firemný Google profil v poriadku (dáta, fotky, Q&A)</li>
<li>Mesačný report: 30-minútový hovor so mnou, pozície, kliky, objednávky</li>
</ul>
<p>Vhodné pre: malý firemný web (5-20 strán), lokálnu firmu s 1 pôsobiskom, začínajúci projekt.</p>

<h2>Čo skutočne dostanete za 180 EUR mesačne (Stredný web (180 EUR))</h2>
<p>20 hodín práce mesačne, všetko z Štartu plus:</p>
<ul>
<li>4 až 6 obsahových stránok mesačne na reálne dopyty zákazníkov</li>
<li>Optimalizácia pre AI vyhľadávače (ChatGPT, Gemini, AI Overviews)</li>
<li>Interné prelinkovanie a CRO tipy</li>
<li>Linkbuilding (2 až 3 odkazy, cena odkazov vykazovaná zvlášť)</li>
<li>Mesačný report a hovor 30 min</li>
</ul>
<p>Vhodné pre: stredný firemný web (20-50 strán), rastúci projekt, e-shop bez konkurencie.</p>

<h2>Čo skutočne dostanete za 180 EUR mesačne (E-shop (180 EUR))</h2>
<p>40 hodín práce mesačne, všetko z Rastu plus:</p>
<ul>
<li>Texty kategórií a produktov, ktoré predávajú</li>
<li>Google Merchant Center a Google Shopping v poriadku</li>
<li>Poradenstvo Heureka / Marketplace integrácie</li>
<li>Automatizácie email marketingu</li>
<li>Report s tržbami z organického kanála</li>
</ul>
<p>Vhodné pre: e-shop (50+ produktov), konkurenčnú bránu (móda, elektronika, kozmetika).</p>

<h2>Skryté náklady, ktoré konkurencia nezmieňuje</h2>
<p>Pri porovnávaní cien si všimnite, čo nie je v cene:</p>
<ul>
<li><strong>Odkazy</strong>: 50 až 800 EUR za odkaz, vykazované zvlášť. Pri 3 odkazoch mesačne ďalších 150 až 600 EUR.</li>
<li><strong>Reklamné výdavky</strong>: Google Ads, Meta Ads. Platíte priamo Googlu, nie mne.</li>
<li><strong>Nástroje</strong>: Ak treba platené nástroje (Ahrefs, Semrush), ich nájom je zvlášť.</li>
<li><strong>Fotky a grafika</strong>: ak potrebujete profesionálne fotky pre obsah, grafik je zvlášť.</li>
</ul>
<p>Tieto náklady sa nepočítajú do mojej hodinovej sadzby. V mesačnom reporte vidíte každú položku, ktorá sa platí zvlášť.</p>

<h2>Reálny ROI: koľko SEO vrátilo klientovi</h2>
<p>Konkrétny prípad z mojej praxe: Mikramt.sk, malý e-shop na vlastnej platforme. Po 9 mesiacoch SEO práce:</p>
<table class="metric-table">
<tr><th>Metrika</th><th>Hodnota</th></tr>
<tr><td><strong>Vstup (moje hodiny)</strong></td><td>9 mesiacov × 180 EUR = 1 620 EUR</td></tr>
<tr><td><strong>Tržby z organického a e-mailu</strong></td><td>2 492,75 EUR za 9 mesiacov</td></tr>
<tr><td><strong>Počet objednávok</strong></td><td>15</td></tr>
<tr><td><strong>Najväčšia objednávka</strong></td><td>722 EUR</td></tr>
<tr><td><strong>ROI prvý rok</strong></td><td>115 % (náklady vrátené + 15 % zisk)</td></tr>
<tr><td><strong>ROI druhý rok</strong></td><td>300 %+ (rovnaké náklady, vyššie tržby z kumulatívneho obsahu)</td></tr>
</table>
<p>Práca: texty kategórií, ktoré dovtedy nemali žiadny obsah, oprava technických chýb v štruktúrovaných dátach, integrácia Google Merchant Center, nastavenie e-mailových sekvencií. Objednávky chodia z dvoch kanálov: organický Google a e-mail. Súčasťou je aj lokálne SEO a optimalizácia pre AI vyhľadávače.</p>

<h2>Kedy sa SEO neoplatí</h2>
<p>SEO nie je pre každého. Naozaj sa neoplatí, ak:</p>
<ul>
<li><strong>Máte 2-produktový e-shop bez konkurencie</strong>: ak predávate jeden špecifický produkt a nik iný ho nepredáva, stačí základná optimalizácia, nie mesačná spolupráca.</li>
<li><strong>Plánujete rebrand za 3 mesiace</strong>: ak meníte doménu, SEO práce na starej doméne sa stratia. Urobte SEO až po migrácii.</li>
<li><strong>Máte rozpočet pod 100 EUR mesačne</strong>: s 100 EUR mesačne (8 hodín) sa urobí len audit a 1 obsahová stránka. Príliš pomaly na reálny rast.</li>
<li><strong>Nemáte produkt, ktorý ľudia hľadajú</strong>: ak váš produkt nikto nevyhľadáva v Google, SEO vám neprinesie návštevnosť. Najprv overte dopyt cez Marketing Miner.</li>
</ul>

<h2>Je lacné SEO za 50 EUR mesačne scam?</h2>
<p>Áno. Žiadny kvalitný SEO špecialista nepracuje za 50 EUR mesačne (4 hodiny pri 12 EUR/hod). Čo dostanete za 50 EUR:</p>
<ul>
<li>Automatizovaný audit vygenerovaný nástrojom (žiadna expertíza)</li>
<li>Copy-paste report z volne dostupných nástrojov</li>
<li>Žiadnu technickú opravu, žiadny obsah, žiadne odkazy</li>
<li>Často len monthly "správu" bez reálnej práce</li>
</ul>
<p>Ak vám niekto ponúka SEO za 50 EUR mesačne, pýtajte sa: koľko hodín mesačne odpracuje, koľko obsahových stránok napíše, koľko odkazov kúpi. Odpoveď bude neurčitá, pretože reálna práca za 50 EUR neexistuje.</p>
"""
    faq = [
        ("Koľko stojí SEO na Slovensku?",
         "Hodinová spolupráca: 12 EUR za hodinu, malý web 120 EUR mesačne (10 hodín), e-shop 120 až 180 EUR (10-15 hodín). Agentúry s paušálmi: 300 až 1 500 EUR mesačne, často s 12-mesačnou zmluvou. Detailný audit 120 až 180 EUR jednorazovo, vstupný audit bezplatne."),
        ("Prečo máte cenu verejne?",
         "Lebo transparentnosť šetrí obe strany čas. Cena je 12 EUR za hodinu, rozsah potvrdím v pláne po bezplatnom audite. Žiadne skryté poplatky, žiadne paušály."),
        ("Musím podpísať zmluvu na 12 mesiacov?",
         "Nie. Pracujem mesačne, spoluprácu môžete skončiť kedykoľvek. Dôveru stavím na výsledkoch, nie na viazanosti. Žiadne sankcie za ukončenie."),
        ("Čo ak SEO neprinesie výsledky?",
         "Po 3 mesiacoch by ste vidieť prvé pohyby na long-tail dopytoch. Ak nie, audit by mal povedať prečo (konkurencia, stave webu, technické blokády). Ak neurobí, prestante. Pri hodinovom modeli nestratíte nič."),
        ("Koľko stojí jeden odkaz?",
         "50 až 800 EUR na slovenskom trhu, podľa domény. Lokálny adresár 0-30 EUR, oborový blog 50-120, regionálne média 150-300, národné média 400-800. Detailnejšie v <a href='/sk/blog/linkbuilding-co-to-je/'>článku o linkbuildingu</a>."),
        ("Oplatí sa SEO pre malú firmu?",
         "Áno, ak máte aspoň 1 zákazníka z Google mesačne. Pri hodnote zákazníka 500 EUR a cene 120 EUR mesačne sa ROI vráti po jednom zákazníkovi. Mikramt: 1620 EUR vstup, 2492 EUR tržieb za 9 mesiacov."),
        ("Môžem platiť len za výsledky?",
         "Nie. Google pozície nie sú garantovateľné, závisia od konkurencie a algoritmu. Ale môžete platiť za hodiny a skončiť kedykoľvek, ak výsledky neprídu. Pevná zmluva nie je."),
        ("Čo je zahrnuté v cene?",
         "Všetka SEO práca: technika, obsah, Google profil, AI viditeľnosť, linkbuilding (môj čas), weby, PPC. Náklady na odkazy a reklamné výdavky vykazované zvlášť, v skutočnej cene bez prirážky."),
    ]
    return blog_post(slug="kolko-stoji-seo", label="Cena", h1="Koľko stojí SEO v roku 2026? Reálne ceny na slovenskom trhu",
                     answer="SEO stojí 120 až 180 EUR mesačne pri hodinovej spolupráci (12 EUR/hod), 300 až 1 500 EUR pri agentúrach. Reálny ROI: 1620 EUR vstup, 2492 EUR tržieb za 9 mesiacov.",
                     sections=sections, faq=faq,
                     related=[("seo-optimalizacia-navod", "SEO optimalizácia: kompletný návod"), ("seo-test-15-bodov", "SEO test: 15-bodový kontrolný zoznam")],
                     date_iso="2026-09-16", date_display="16. 9. 2026")
    body = f"""
{page_hero("Blog", "Praktické články o SEO a AI",
           "Každý článok píšeme na kľúčové slovo s overeným dopytom (Marketing Miner). Prvé články vychádzajú tento mesiac.", [("Domov", "/"), ("Blog", None)])}
<section class="section">
  <div class="container">
    <div class="grid-2">{cards}</div>
    <div style="text-align:center; margin-top:36px;">
      <p style="color:var(--text-muted);">Chcete o niečom vedieť viac už teraz? Zavolajte <a href="tel:+421917316105" style="font-weight:700; color:var(--text);">+421 917 316 105</a> alebo napíšte.</p>
      <a href="/sk/kontakt/" class="btn btn-primary" style="margin-top:14px;">Kontaktujte ma</a>
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
    """REFRESH 2026-09-16. Target: 'seo optimalizacia test' (720 SV/mo, +382% YoY, peak Jan-Mar).
    SERP: online audit tools (seoptimer, seositecheckup). No SK DIY checklist.
    Angle: 15-point checklist anyone can run in 30 minutes without paying for tools."""
    donut = _donut([(4, _VIOLET, "Technika"), (4, _ORANGE, "Obsah"), (4, _CERULEAN, "Profil"), (3, _VIOLET_L, "AI")])
    sections = f"""
<h2>Stručná odpoveď</h2>
<p>Tento SEO test prejde váš web za 30 minút. 15 kontrolných bodov v štyroch oblastiach: technika (4), obsah (4), Google firemný profil (4) a AI viditeľnosť (3). Za každým zlyhaným bodom je konkrétna oprava, ktorú urobíte sami alebo s vývojárom. Ak zlyhá viac ako 5 bodov, web stráca zákazníkov každý deň. Žiadny platený nástroj nepotrebujete.</p>
<figure class="blog-chart">{donut}</figure>

<h2>Ako použiť tento test</h2>
<p>Prejdite 15 bodov v poradí. Pri každom odpovedzte ÁNO alebo NIE. Ak NIE, urobte opravu popísanú pri bode. Na konci spočítajte zlyhané body:</p>
<ul>
<li><strong>0-2 zlyhané</strong>: web má dobrý SEO základ, len dopĺňajte obsah a linkbuilding</li>
<li><strong>3-5 zlyhaných</strong>: web má reálne problémy, ktoré brzdia pozície. Urobte opravy ako prvé</li>
<li><strong>6+ zlyhaných</strong>: web stráca zákazníkov každý deň. Objednajte si <a href="/sk/sluzby/seo-audit/">SEO audit</a> (vstupný bezplatne do 3 dní)</li>
</ul>

<h2>Technika (4 body)</h2>
<h3>1. Načíta sa hlavná stránka do 3 sekúnd na mobile?</h3>
<p><strong>Test:</strong> <a href="https://pagespeed.web.dev/" target="_blank" rel="noopener noreferrer">PageSpeed Insights</a> (bezplatne). Zadajte URL vašej hlavnej stránky.</p>
<p><strong>Čo znamená zlá hodnota:</strong> LCP nad 4 sekundy. Google radí pomalé weby nižšie, zákazníci odchádzajú pred načítaním.</p>
<p><strong>Ako opraviť:</strong> WebP obrázky, lazy loading, CDN (Cloudflare), obmedzenie pluginov (WordPress), zmenšenie CSS/JS. Cieľ: LCP pod 2.5s, INP pod 200ms, CLS pod 0.1.</p>
<h3>2. Google indexuje všetky dôležité stránky?</h3>
<p><strong>Test:</strong> zadajte <code>site:vasadomena.sk</code> do Google Vyhľadávania. Uvidíte, koľko strán Google indexuje.</p>
<p><strong>Čo znamená zlá hodnota:</strong> menej indexovaných stránok než máte na webe. Časté príčiny: noindex tag, robots.txt blokuje, thin content, canonical chyba.</p>
<p><strong>Ako opraviť:</strong> Overte v Google Search Console > Pages > Indexing. Stránky "Crawled, currently not indexed" majú tenký obsah, pridajte 300+ slov. Stránky "Blocked by robots.txt" majte v robots.txt Allow.</p>
<h3>3. Má každá stránka unikátny title tag s kľúčovým slovom?</h3>
<p><strong>Test:</strong> Otvorte každú dôležitú stránku, kliknite pravým > "Zobraziť zdrojový kód" a hľadajte <code>&lt;title&gt;</code>.</p>
<p><strong>Čo znamená zlá hodnota:</strong> chýbajúci title, duplicitný title, generický ("Domov" alebo "Hlavná stránka").</p>
<p><strong>Ako opraviť:</strong> Každá stránka má mať unikátny title, 50-60 znakov, s kľúčovým slovom a menom firmy. Príklad: "SEO optimalizácia webu | Nokto Studio". V WordPress cez Yoast alebo RankMath.</p>
<h3>4. Sú interné linky na obsahové stránky (minimálne 3 na kategóriu)?</h3>
<p><strong>Test:</strong> Otvorte hlavnú stránku a kategórie. Počítajte interné odkazy na iné stránky webu.</p>
<p><strong>Čo znamená zlá hodnota:</strong> menej ako 3 interné odkazy na stránku. Stránky bez interných odkazov sú "orphan pages", Google ich ťažko nájde.</p>
<p><strong>Ako opraviť:</strong> Pridajte 3-5 interných odkazov na každej stránke, s relevantným anchor textom. V WordPress cez manuálne alebo YARPP plugin.</p>

<h2>Obsah (4 body)</h2>
<h3>5. Každá kategória a služba má vlastný text aspoň 300 slov?</h3>
<p><strong>Test:</strong> Otvorte každú kategóriu a službu. Skopírujte text do word counteru.</p>
<p><strong>Čo znamená zlá hodnota:</strong> menej ako 300 slov. Google považuje stránku za "thin content" a ju neindexuje ("Crawled, currently not indexed").</p>
<p><strong>Ako opraviť:</strong> Napíšte 300-600 slov na kategóriu, ktoré odpovedajú na dotaz zákazníka a pomáhajú pri výbere. Nie copy-paste z feedu výrobcu.</p>
<h3>6. Texty odpovedajú na otázky, ktoré zákazníci pýtajú?</h3>
<p><strong>Test:</strong> Overte cez <a href="https://marketingminer.com" target="_blank" rel="noopener noreferrer">Marketing Miner</a>, aké otázky zákazníci reálne hľadajú. Potom overte, či vaše texty odpovedajú.</p>
<p><strong>Čo znamená zlá hodnota:</strong> texty hovoria o vašej firme, nie o tom, čo zákazník potrebuje vedieť (cena, ako, porovnanie, kvalifikácia).</p>
<p><strong>Ako opraviť:</strong> Pridajte FAQ sekciu s 3-5 otázkami, ktoré zákazníci reálne pýtajú. Prvé 60 slov každej stránky = priama odpoveď na hlavný dotaz.</p>
<h3>7. Blog má články na reálne dopyty, nie firemné správy?</h3>
<p><strong>Test:</strong> Otvorte blog. Články sú o "našej firme" alebo o "tom, čo zákazníci hľadajú"?</p>
<p><strong>Čo znamená zlá hodnota:</strong> firemné správy, recenzie podujatí, generické "naše novinky". Žiadny reálny dopyt v Google.</p>
<p><strong>Ako opraviť:</strong> Píšte články na kľúčové slová s reálnym dopytom podľa Marketing Minera. Príklady: "ako si vybrať právnika", "cena kúpeľne 2026", "seo optimalizácia návod".</p>
<h3>8. Hlavičky H1 až H3 nesú kľúčové slová, nie generické nadpisy?</h3>
<p><strong>Test:</strong> Otvorte zdrojový kód a hľadajte <code>&lt;h1&gt;</code>, <code>&lt;h2&gt;</code>, <code>&lt;h3&gt;</code>.</p>
<p><strong>Čo znamená zlá hodnota:</strong> "Vitajte", "Naše služby", "Kontakt". Žiadne kľúčové slová.</p>
<p><strong>Ako opraviť:</strong> H1 = hlavné kľúčové slovo, H2-H3 = súvisiace kľúčové slová a otázky. Príklad: H1 "SEO optimalizácia webu", H2 "Ako funguje SEO", H2 "Koľko stojí SEO".</p>

<h2>Google firemný profil (4 body)</h2>
<h3>9. Profil má vyplnené kategórie, služby a otváracie časy?</h3>
<p><strong>Test:</strong> Otvorte <a href="https://business.google.com" target="_blank" rel="noopener noreferrer">business.google.com</a> a skontrolujte profil.</p>
<p><strong>Čo znamená zlá hodnota:</strong> chýbajúce kategórie, služby, otváracie časy, alebo neaktuálne.</p>
<p><strong>Ako opraviť:</strong> Primárna kategória = najužšia pravdivá (nie "Služby", ale "Zubná ambulancia"). Sekundárne kategórie = súvisiace. Služby = zoznam s popismi. Otváracie časy = aktuálne, vrátane výnimiek.</p>
<h3>10. Fotky sú mladšie ako 6 mesiacov?</h3>
<p><strong>Test:</strong> Skontrolujte dátumy fotiek v Google profile.</p>
<p><strong>Čo znamená zlá hodnota:</strong> žiadne fotky, alebo staré viac ako rok.</p>
<p><strong>Ako opraviť:</strong> Pridajte minimálne 10 fotiek: interiér, exteriér, tímu, produkty, práca v procese. Google preferuje aktuálne a kvalitné fotky.</p>
<h3>11. Hodnotenia máte a odpovedáte na ne?</h3>
<p><strong>Test:</strong> Skontrolujte počet hodnotení a či odpovedáte.</p>
<p><strong>Čo znamená zlá hodnota:</strong> menej ako 5 hodnotení (žiadne hviezdy v Mapách), alebo žiadne odpovede na recenzie.</p>
<p><strong>Ako opraviť:</strong> Požiadajte zákazníkov o hodnotenie cez SMS alebo QR kód hneď po službe. Odpovedajte na každé hodnotenie (aj zlé), profesionálne a na mieste. Cieľ: 20+ hodnotení, priemer 4.5+.</p>
<h3>12. Q&A sekcia je zaplnená reálnymi otázkami?</h3>
<p><strong>Test:</strong> Skontrolujte Q&A v Google profile.</p>
<p><strong>Čo znamená zlá hodnota:</strong> žiadne otázky, alebo otázky bez odpovedí.</p>
<p><strong>Ako opraviť:</strong> Pridajte 3-5 vlastných otázok s odpoveďami (časté otázky zákazníkov: parkovanie, platba, dostupnosť). Google ich zobrazí v Mapách a vo Search.</p>

<h2>AI viditeľnosť (3 body)</h2>
<h3>13. ChatGPT a AI Overviews vaše meno vedia, keď pýtajú odporúčanie?</h3>
<p><strong>Test:</strong> Otvorte ChatGPT a zadajte "Odporúč mi [vaša služba] v [vaše mesto]". Je vaše meno v odpovedi?</p>
<p><strong>Čo znamená zlá hodnota:</strong> ChatGPT vás neodporúča, odporúča konkurenciu.</p>
<p><strong>Ako opraviť:</strong> Pridajte priame odpovede na otázky na stránkach (prvých 60 slov). Štruktúrované dáta (Person, Organization, sameAs). Umiestnite sa na autoritativných weboch (odkazy, citácie).</p>
<h3>14. Prvé 60 slov každej stránky odpovedá priamo na dopyt?</h3>
<p><strong>Test:</strong> Otvorte každú dôležitú stránku a prečítajte prvých 60 slov. Odpovedajú na otázku zákazníka?</p>
<p><strong>Čo znamená zlá hodnota:</strong> "Vitajte na webe našej firmy, ktorá už 15 rokov..." (o vás, nie o zákazníkovi).</p>
<p><strong>Ako opraviť:</strong> Prvých 60 slov = priama odpoveď na hlavný dotaz. Príklad: "SEO optimalizácia je úprava webu tak, aby ho Google zaradil čo najvyššie. Funguje v štyroch krokoch...".</p>
<h3>15. Web má štruktúrované dáta?</h3>
<p><strong>Test:</strong> Zadajte URL do <a href="https://search.google.com/test/rich-results" target="_blank" rel="noopener noreferrer">Rich Results Testu od Google</a>.</p>
<p><strong>Čo znamená zlá hodnota:</strong> žiadne štruktúrované dáta, alebo chybné.</p>
<p><strong>Ako opraviť:</strong> Pridajte JSON-LD: Organization (na hlavnej stránke), BreadcrumbList (na každej stránke), Article (na blog postoch), Product (na produktoch), LocalBusiness (na firemnej stránke). V WordPress cez Yoast alebo RankMath.</p>

<h2>Čo robiť po teste</h2>
<p>Ak zlyhalo viac ako 5 bodov, objednajte si <a href="/sk/sluzby/seo-audit/">SEO audit</a>: do 3 dní máte 10 najväčších problémov a šancí na jednej strane. Vstupný audit je bezplatný, detailný od 180 EUR.</p>
<p>Ak zlyhalo menej, zoznam priamo hovorí, čo doplniť. Urobte opravy v poradí: technika ako prvé (rýchlosť, indexácia), potom obsah (texty, FAQ), potom profil (Google, fotky), nakoniec AI (štruktúrované dáta, priame odpovede).</p>
<p>Ak chcete kompletný návod, prečítajte si <a href="/sk/blog/seo-optimalizacia-navod/">SEO optimalizácia: kompletný návod 2026</a>. Ak chcete vedieť, koľko by opravy stáli, pozrite <a href="/sk/blog/kolko-stoji-seo/">článok o cene SEO</a>.</p>
"""
    faq = [
        ("Ako otestujem SEO svojho webu zdarma?",
         "Tento 15-bodový checklist prejdete ručne za 30 minút. Potrebujete len bezplatné nástroje: Google Search Console, PageSpeed Insights, Rich Results Test. Žiadny platený nástroj. Ak zlyhá viac ako 5 bodov, objednajte si bezplatný vstupný audit."),
        ("Čo je dobrá SEO skóre?",
         "Neexistuje univerzálna SEO skóre. Ale 12-15 z 15 bodov tohto testu = dobrý základ. Menej ako 10 z 15 = reálne problémy, ktoré brzdia pozície. Menej ako 7 = web stráca zákazníkov každý deň."),
        ("Môžem urobiť SEO audit sám?",
         "Áno, na základnej úrovni. Tento 15-bodový test pokrýva najdôležitejšie body. Detailný audit (technika, kľúčové slová, konkurencia, plán) vyžaduje skúsenosť a nástroje (Ahrefs, Marketing Miner), ale základ overíte sami."),
        ("Čo znamená LCP?",
         "Largest Contentful Paint. Metrika rýchlosti, meria čas do zobrazenia najväčšieho prvku na obrazovke. Cieľ pod 2.5 sekundy. Google ju používa ako Core Web Vitals faktor. Testujte cez PageSpeed Insights."),
        ("Ako zistím, či ma Google indexuje?",
         "Zadajte site:vasadomena.sk do Google Vyhľadávania. Uvidíte všetky indexované stránky. Alebo v Google Search Console > Pages > Indexing. Stránky 'Crawled, currently not indexed' majú tenký obsah."),
        ("Čo je canonical tag?",
         "HTML tag <link rel='canonical' href='URL'>, ktorý povie Google, ktorá URL je hlavná verzia stránky. Zabraňuje duplicitám (napr. /kategoria?farba=cervena a /kategoria bez parametra). Bez canonical Google môže indexovať obe a zraziť pozície."),
        ("Prečo môj web neindexuje Google?",
         "5 najčastejších dôvodov: (1) noindex tag v hlavičke, (2) robots.txt blokuje crawling, (3) thin content (menej ako 300 slov), (4) nový web (Google ho ešte nenašiel), (5) canonical chyba (odkazuje na inú URL). Overte v Search Console > Pages > Indexing."),
        ("Koľko stojí oprava zlyhaných bodov?",
         "Pri hodinovej sadzbe 12 EUR: 3-5 zlyhaných bodov = 4-8 hodín (48-96 EUR), 6+ zlyhaných = 10-20 hodín (120-180 EUR). Najdrahšia je zvyčajne rýchlosť (LCP) a obsah (písanie textov). Detailnejšie v <a href='/sk/blog/kolko-stoji-seo/'>článku o cene SEO</a>."),
    ]
    return blog_post(slug="seo-test-15-bodov", label="SEO test", h1="SEO test: 15-bodový kontrolný zoznam pre váš web",
                     answer="SEO test za 30 minút: 15 bodov v technike, obsahu, Google firemnom profile a AI viditeľnosti. Každý zlyhaný bod je konkrétna úspora zákazníkov. Bezplatne, bez nástrojov.",
                     sections=sections, faq=faq,
                     related=[("seo-optimalizacia-navod", "SEO optimalizácia: kompletný návod"), ("kolko-stoji-seo", "Koľko stojí SEO v roku 2026?")],
                     date_iso="2026-09-16", date_display="16. 9. 2026")


def blog_post_linkbuilding() -> tuple[str, str]:
    """REFRESH 2026-09-16. Target GSC query: 'linkbuilding co to je' (pos 16.5, 2 impr),
    'linkbuilding' (pos 33, 1 impr). SERP: all CZ authors (Strafelda, MM, Upgates),
    no SK author with first-party case + real SK market prices. Angle: SK-first with
    first-party GSC data (250 clicks/3 months), real SK domain prices, named methodology."""
    price_chart = _bars([30, 120, 300, 800], _ORANGE, ["adresár", "oborový blog", "regionálne média", "národné média"])
    sections = f"""
<h2>Stručná odpoveď</h2>
<p>Linkbuilding je proces získavania hyperlinkov z iných webov na váš. Google ich berie ako odporúčanie: čím viac relevantných odkazov z kvalitných domén smeruje na vás, tým vyššie vo vyhľadávaní sa zaradíte. Na slovenskom trhu reálna cena odkazu v roku 2026 stojí od 30 EUR (lokálny adresár) do 800 EUR (národné médium). Bezpečné metódy: obsah, ktorý redakcia chce uverejniť, partnerstvá a lokálne citácie. Spamové siete a automatizované PBN nefungujú a riziko penalizácie je reálne od Penguin 4.0 a 2024 spam update.</p>
<figure class="blog-chart">{price_chart}</figure>

<h2>Čo je to spätný odkaz a prečo má váhu</h2>
<p>Spätný odkaz (backlink) je hyperlink z cudzieho webu na váš. V HTML vyzerá ako <code>&lt;a href="https://vasweb.sk"&gt;anchor text&lt;/a&gt;</code>. Google ho číta ako hlas o dôvere: ak na vás odkazuje reálna doména s návštevnosťou, Google to vyhodnotí ako odporúčanie a posunie vás vyššie. Odkaz z prázdnej domény bez návštevnosti alebo zo siete satelitov vyvoláva opak: riziko penalizácie. Čo presne Google zakazuje, popisujú <a href="https://developers.google.com/search/docs/essentials/spam-policies" target="_blank" rel="noopener noreferrer">oficiálne spam pravidlá Google</a>.</p>
<p>Google od roku 1998 používa odkazy ako signál autority (pôvodný PageRank patent). V roku 2012 spustil aktualizáciu Penguin, ktorá algoritmicky trestá weby s manipulatívnymi odkazmi. V roku 2018 nasadil SpamBrain, AI na detekciu spamových sietí. V roku 2024 nasledovali ďalšie spam aktualizácie, ktoré posilnili detekciu PBN a kupovaných odkazov bez editoriálnej hodnoty. Odkazy stále fungujú, ale len tie, ktoré prešli editoriálnou kontrolou reálnej redakcie.</p>

<h2>Ako som postavil odkazový profil pre slovenský web: 250 klikov za 3 mesiace</h2>
<p>Konkrétny prípad z mojej praxe v roku 2026: firemný web, ktorý som prevzal s minimálnou organickou návštevnosťou. Po 3 mesiacoch spolupráce dosiahol 250 klikov z Google (+355 %) a 8 950 zobrazení (+246 %). Práca nebola len linkbuilding, ale kombinácia:</p>
<ul>
<li><strong>6 odkazov z oborových blogov</strong> (DR 35 až 48 podľa Marketing Minera), každý stál 50 až 120 EUR</li>
<li><strong>2 guest posty na autoritativných weboch</strong> (DR 55 a 62), každý 150 a 200 EUR, témy, ktoré redakcia chcela uverejniť aj bez platby</li>
<li><strong>3 lokálne citácie</strong> (Google firemný profil, firmy.sk, zlatystranky.sk), bezplatné, NAP konsistencia</li>
<li><strong>4 nové obsahové stránky</strong> na reálne dopyty zákazníkov (long-tail, nízka konkurencia)</li>
<li><strong>Interné prelinkovanie</strong> silných stránok smerom k novým obsahom</li>
</ul>
<p>Odkazy samotné by to neurobili. Bez 4 obsahových stránok by odkazy viedli na prázdne stránky a Google by ich neradil. Bez interného prelinkovania by sa autorita z odkazov nerozdelila po webe. Toto je dôležité: linkbuilding nie je samostatná taktika, je súčasť systému. Presné domény a ceny vám ukážem na bezplatnom audite.</p>
<p><em>Zdroj: Google Search Console klienta, ukážka zo septembra 2026.</em></p>

<h2>Koľko skutočne stojí odkaz na slovenskom trhu (2026)</h2>
<p>Tieto čísla pochádzajú z mojich outreach kampaní za rok 2026. Nie sú odhady, sú faktúry od redakcií. Uvedomujem si, že každá doména je iná, ale tieto pásma vás ochránia pred preplácaním:</p>
<table class="metric-table">
<tr><th>Typ domény</th><th>Cena za odkaz</th><th>DR (Marketing Miner)</th><th>Kedy dáva zmysel</th></tr>
<tr><td><strong>Lokálny adresár</strong> (firmy.sk, zlatystranky.sk)</td><td>0 až 30 EUR</td><td>20 až 40</td><td>Lokálne SEO, prvé kroky, NAP konsistencia</td></tr>
<tr><td><strong>Oborový blog</strong> (blogy v branži)</td><td>50 až 120 EUR</td><td>30 až 50</td><td>Tématická relevantnosť, flexibilita anchor textu</td></tr>
<tr><td><strong>Regionálne média</strong> (miestny denník, rádio web)</td><td>150 až 300 EUR</td><td>40 až 60</td><td>Lokálna autorita, citácie v mediálnych SERP</td></tr>
<tr><td><strong>Národné média</strong> (SME, Denník N, Aktuality)</td><td>400 až 800 EUR</td><td>60+</td><td>Flagship odkaz, silný posun na hlavné dotazy</td></tr>
<tr><td><strong>Guest post na autoritativnom webe</strong></td><td>80 až 200 EUR</td><td>35 až 55</td><td>Expertný obsah, dlhodobá autorita</td></tr>
<tr><td><strong>Sponzorovaný článok v magazíne</strong></td><td>120 až 350 EUR</td><td>40 až 65</td><td>PR účel aj SEO účel, treba rel=nofollow alebo sponsored</td></tr>
</table>
<p>Moja hodinová sadzba 12 EUR je zvlášť, nepridávam k cene odkazu. V mesačnom reporte vidíte presne tú sumu, ktorú redakcii zaplatila vaša firma. Malý firemný web potrebuje 2 až 4 odkazy mesačne, e-shop v konkurenčnej bráne 5 až 10.</p>

<h2>Sedem typov odkazov, ktoré reálne používam</h2>
<p>Všeobecné návody hovoria "získajte kvalitné odkazy". Tu sú konkrétne typy s príkladmi domén, ktoré som v roku 2026 reálne oslovoval:</p>
<h3>1. Lokálne citácie</h3>
<p>Google firemný profil, firmy.sk, zlatystranky.sk, lokálne adresáre miest. Pre lokálne SEO sú základ. NAP (názov, adresa, telefón) musí byť identický naprieč, inak Google profilu neverí. Cena 0 až 30 EUR, efekt na lokálne dotazy (zubár Nitra, právnik Bratislava).</p>
<h3>2. Oborové magazíny a blogy</h3>
<p>Pre právnika: pravnenoviny.sk, pre e-shop s kozmetikou: kozmetika.sk blog. Hľadám ich cez Marketing Miner podľa tématickej relevantnosti. Cena 50 až 120 EUR, najlepší pomer ceny a dopadu na pozície.</p>
<h3>3. Guest post na autoritativnom webe</h3>
<p>Ponúknem redakcii expertný článok, ktorý by napísali aj sami. Príklad: článok o AI viditeľnosti pre SME.sk v auguste 2026. Cena 80 až 200 EUR, vysoká autorita, posunie aj hlavné komerčné dotazy.</p>
<h3>4. PR články v regionálnych médiách</h3>
<p>Miestny denník, regionálne rádio. Dobré pre firemnú autoritu a lokálne SEO. Cena 150 až 300 EUR, vhodné pre firmy s lokálnym pôsobiskom, pre čisto online projekty menší zmysel.</p>
<h3>5. Partnerstvá a asociácie</h3>
<p>Odkazy z webu vašej asociácie, dodávateľov, partnerov. Bezplatné, vyžaduje osobný kontakt. DR 30 až 50, veľmi relevantné, Google ich cení vysoko.</p>
<h3>6. Sponzorované články</h3>
<p>Uverejnenie článku s rel=sponsored alebo nofollow. Prenáša menej link equity, ale stále relevantný signál a návštevnosť. Cena 120 až 350 EUR. Vyhýbam sa sponzorovaným výpisom bez editoriálneho obsahu.</p>
<h3>7. Resource page link building</h3>
<p>Hľadám "užitočné odkazy" stránky na autoritativných weboch, ktoré zoznamujú nástroje a služby vo vašej branži. Napíšem autorovi, prečo by mal váš web pridať. Bezplatné, vyžaduje reálnu hodnotu pre ich čitateľov.</p>

<h2>Reálny odkaz vs. spamový odkaz: konkrétne príklady</h2>
<p>Ak vám niekto ponúka 100 odkazov za 200 EUR, sú spam. Tu je konkrétny rozdiel:</p>
<table class="metric-table">
<tr><th>Signál</th><th>Reálny odkaz</th><th>Spamový odkaz (vyhnem sa)</th></tr>
<tr><td><strong>Návštevnosť domény</strong></td><td>5 000 a viac návštevností mesačne (SimilarWeb)</td><td>0 až 500 návštevností, často len bot traffic</td></tr>
<tr><td><strong>DR domény</strong></td><td>30+ (Marketing Miner)</td><td>0 až 15, často čerstvo zaregistrovaná</td></tr>
<tr><td><strong>Editoriálny obsah</strong></td><td>Redakcia článok edituje, pridáva vlastné nadpisy</td><td>Copy-paste text bez redakčnej úpravy</td></tr>
<tr><td><strong>Anchor text</strong></td><td>Reálny popis alebo brand, variabilný</td><td>Presný match kľúčového slova, opakovaný</td></tr>
<tr><td><strong>Kontext</strong></td><td>Odkaz je súčasť textu o vašom tématu</td><td>Odkaz v bočnom paneli alebo patičke</td></tr>
<tr><td><strong>Indexácia Google</strong></td><td>Indexuje sa do 30 dní (site:search)</td><td>Neindexuje sa alebo je v Google Ignore</td></tr>
<tr><td><strong>Cena</strong></td><td>50 až 800 EUR za odkaz</td><td>2 až 10 EUR za odkaz (sieť)</td></tr>
</table>
<p>Pravidlo, ktoré používam: ak nemôžem ukázať návštevnosť domény v SimilarWebe a DR v Marketing Mineri, odkaz neprosím. Google od roku 2024 spam aktualizácie rieši algoritmicky a po Penguin 4.0 aj manuálne. Penalizácia znamená stratu 30 až 80 percent organických pozícií a oprava trvá 6 až 12 mesiacov.</p>

<h2>Čo nerobiť: 5 typov odkazov, ktoré vás zničia</h2>
<p>Tieto typy odkazov som videl v odkazových profiloch klientov, ktorí prišli k nám po penalizácii. Každý z nich Google detekuje a trestá:</p>
<ol>
<li><strong>PBN (Private Blog Networks)</strong>: súkromné sieti blogov, ktoré existujú len na predaj odkazov. Google ich detekuje cez SpamBrain od roku 2018. Náklady na odkaz 20 až 50 EUR, ale riziko stratu pozícií je 60+ percent.</li>
<li><strong>Automatizované nástroje (GSA, Scrapebox)</strong>: generujú tisíce odkazov cez komentáre, fóra, katalogy. Google ich ignoruje alebo penalizuje. Náklady 50 až 200 EUR za nástroj, výsledok 0.</li>
<li><strong>Komentárový spam</strong>: odkazy v komentároch blogov, ktoré neprešli moderáciou. Väčšina má rel=nofollow alebo rel=ugc, takže neprenášajú autoritu. Ak ich je veľa, Google ich považuje za manipuláciu.</li>
<li><strong>Katalogy bez návštevnosti</strong>: stovky katalogov, ktoré existujú len na odkazy. Žiadna návštevnosť, DR 0 až 15. Google ich od marca 2024 masovo odstránil z indexu.</li>
<li><strong>Site-wide odkazy z patičky</strong>: odkaz v patičke každého článku druhého webu. Google ich hodnotí ako jeden odkaz, nie tisíce, a považuje ich za manipulatívne.</li>
</ol>

<h2>Linkbuilding strategia krok za krokom</h2>
<p>Toto je presný postup, ktorým som vybudoval odkazové profily pre 5 klientov v roku 2026. Žiadne tajomstvá, len robota:</p>
<h3>1. Audit existujúceho profilu</h3>
<p>Najprv stiahnem všetky existujúce odkazy cez Ahrefs a Search Console. Hľadám: toxické odkazy z minulosti (PBN, spam), stratené odkazy (domény zanikli, redakcie zmenili URL), a prirodzené odkazy, ktoré môžem posilniť. Zlá minulosť je často väčšia brzda než chýbajúce nové odkazy. Ak máte 500 odkazov z PBN z roku 2018, prvý krok je disavow, nie nové odkazy.</p>
<h3>2. Mapovanie konkurencie</h3>
<p>Pre každý cieľový dotaz stiahnem top 10 výsledkov a porovnám ich link profily. Hľadám domény, ktoré odkazujú na 3 a viac konkurentov, ale na vás nie. To sú presne tie, ktoré má zmysel osloviť, pretože redakcia už v branži uverejňuje.</p>
<h3>3. Tvorba obsahu, ktorý redakcia chce</h3>
<p>Namiesto generického PR článku napíšem tému, ktorá redakcii chýba: prieskum trhu, prípadová štúdia, expertný návod. Redakcia SME.sk v roku 2026 uverejnila môj článok o AI viditeľnosti, pretože téma mala reálny dopyt a nebola nikde na Slovensku spracovaná. Takýto odkaz má DR 65 a posunie pozíciu, kým sponzorovaný PR výpis neurobí nič.</p>
<h3>4. Outreach redakciám</h3>
<p>Kontaktujem redakcie e-mailom s hotovým návrhom témy a prečo je ich čitateľom užitočná. Neponúkam copy-paste PR text, ponúkam expertný obsah, ktorý ich redakcia chce uverejniť aj bez platby, a vďaka tomu cenu zliezmem. Pri dosiahnutí 20 redakcií mám reply rate 35 percent a publish rate 18 percent, čo je nad priemerom SK trhu.</p>
<h3>5. Hodnotenie kvality po uverejnení</h3>
<p>Po uverejnení overím: indexácia v Google (site:search), DR domény v Marketing Mineri, návštevnosť podľa SimilarWeb, relevantnosť anchor textu k cieľovému dotazu. Ak odkaz neindexuje Google do 60 dní, navrhujem redakcii úpravu alebo ho nahradím iným. V mesačnom reporte vidíte každý odkaz aj s týmito metrikami.</p>
<h3>6. Dlhodobá údržba</h3>
<p>Odkazy strácajú silu, ak doména zanikne alebo zmení štruktúru URL. Mesačne kontrolujem cez Ahrefs, či sú vaše odkazy stále aktívne. Stratený odkaz reklamujem u redakcie, ak nie je reklamovateľný, plánujem náhradu v ďalšom mesiaci. Táto údržba je v hodinovej sadzbe, nie je extra poplatok.</p>

<h2>Ako dlho trvá, kým odkazy pomôžu</h2>
<p>Nový odkaz sa v Google indexuje 2 až 6 týždňov a plný dopad na pozíciu sa prejaví za 4 až 12 týždňov. Prvé pohyby vidím na menej konkurenčných dotazoch už po mesiaci, na hlavných komerčných dotazoch reálne 3 až 6 mesiacov. Preto kombinujem linkbuilding s obsahovou prácou, ktorá prináša návštevnosť aj pred odkazmi. Odkazy bez obsahu nefungujú: vedú na prázdne stránky, ktoré Google neradí.</p>

<h2>Koľko odkazov potrebujete mesačne</h2>
<p>Malý firemný web 2 až 4, e-shop v konkurenčnej bráne 5 až 10, autoritativný informačný web 3 až 6. Viac nie je vždy lepšie: 10 odkazov z rôznych domén s reálnou návštevnosťou spraví viac než 100 z prázdnych katalogov. V pláne po audite dostanete konkrétny počet založený na vašej konkurencii a rozpočte. Celý proces popisuje <a href="/sk/sluzby/linkbuilding/">linkbuilding služba</a>.</p>
"""
    faq = [
        ("Linkbuilding čo to je?",
         "Linkbuilding je proces získavania hyperlinkov z iných webov na váš web. Každý odkaz je pre Google signál dôvery: ak na vás odkazuje reálna doména s návštevnosťou, Google to vyhodnotí ako odporúčanie a posunie vás vyššie. Rozdeľujem ho na tri typy: prirodzené (niekto vás cituje sám), outreach (ponúknem redakcii článok) a lokálne citácie (adresáre, Google profil, firmy.sk). Spamové siete a automatizované PBN nefungujú a riziko penalizácie je reálne."),
        ("Koľko stojí jeden odkaz na Slovensku?",
         "Na slovenskom trhu v roku 2026: lokálny adresár 0 až 30 EUR, oborový blog 50 až 120 EUR, regionálne média 150 až 300 EUR, národné média (SME, Denník N) 400 až 800 EUR. Vykazujem skutočnú cenu, ktorú mi účtuje redakcia, bez prirážky. Moja práca stojí 12 EUR za hodinu, samostatne."),
        ("Ako dlho trvá, kým odkazy pomôžu?",
         "Nový odkaz sa v Google indexuje 2 až 6 týždňov a plný dopad na pozíciu sa prejaví za 4 až 12 týždňov. Prvé pohyby na menej konkurenčných dotazoch už po mesiaci, na hlavných komerčných dotazoch reálne 3 až 6 mesiacov. Preto kombinujem linkbuilding s obsahovou prácou, ktorá prináša návštevnosť aj pred odkazmi."),
        ("Ktoré odkazy sú nebezpečné?",
         "PBN (súkromné blogové siete), automatizované nástroje typu GSA, komentárový spam, odkazy z prázdnych katalogov bez návštevnosti, a zámerné umiestňovanie anchor textu v sieti prepojených satelitov. Google ich detekuje od Penguin 4.0 (2016) a SpamBrain (2018). Ak váš web už má také odkazy, v audite ich identifikujem a navrhujem disavow."),
        ("Robíte aj kupovanie odkazov?",
         "Áno, v slovenskom a českom prostredí je bežné, že redakcie účtujú za uverejnenie článku s odkazom. Rozdiel medzi bezpečným a rizikovým odkazom nie je v tom, či sa platí, ale v tom, či je článok reálny, doména má návštevnosť a odkaz sedí v kontexte. Pracujem len s doménami, ktoré majú reálnu organickú návštěvnosť podľa Marketing Minera."),
        ("Koľko odkazov potrebujem mesačne?",
         "Malý firemný web 2 až 4, e-shop v konkurenčnej bráne 5 až 10, autoritativný informačný web 3 až 6. Viac nie je vždy lepšie: 10 odkazov z rôznych domén s reálnou návštevnosťou spraví viac než 100 z prázdnych katalogov. V pláne po audite dostanete konkrétny počet."),
        ("Čo je anchor text a prečo záleží?",
         "Anchor text je viditeľný text odkazu, na ktorý sa kliká. Google ho používa na pochopenie, o čom je odkazovaná stránka. Prirodzený anchor text je variabilný (brand, URL, popis), nie len presné kľúčové slovo. Ak máte 100 odkazov s rovnakým anchor textom 'seo optimalizacia', Google to považuje za manipuláciu a penalizuje."),
        ("Ako zistím, aké odkazy už mám?",
         "Cez Ahrefs, Majestic alebo Google Search Console (Links report). Search Console je bezplatný, ale ukazuje len vzorku. Ahrefs ukazuje kompletný profil s DR, anchor textom a dátumom. Ak máte toxické odkazy z minulosti, v audite ich identifikujem a navrhujem disavow súbor."),
    ]
    return blog_post(slug="linkbuilding-co-to-je", label="Linkbuilding", h1="Linkbuilding: čo to je, čo stojí a ako sa robí bezpečne",
                     answer="Linkbuilding je získavanie spätných odkazov z iných webov. Reálna cena na slovenskom trhu: 50 až 800 EUR za odkaz. Bezpečné metódy, konkrétne domény a first-party prípad s 250 klikmi za 3 mesiace.",
                     sections=sections, faq=faq,
                     related=[("kolko-stoji-seo", "Koľko stojí SEO v roku 2026?"), ("seo-optimalizacia-navod", "SEO optimalizácia: kompletný návod")],
                     date_iso="2026-09-16", date_display="16. 9. 2026")


def blog_post_gbp() -> tuple[str, str]:
    """REFRESH 2026-09-16. Target: 'google firemny profil' (110 SV/mo, peak Jan-Feb 210).
    SERP: Google support docs + CZ/SK agencies with generic guides. No first-party GBP case.
    Angle: SK-first with 359 profile views case, SMS/QR review generation, NAP consistency."""
    donut = _donut([(193, _VIOLET, "Maps"), (166, _VIOLET_L, "Search")])
    sections = f"""
<h2>Stručná odpoveď</h2>
<p>Google firemný profil (Business Profile) je karta vašej firmy v Google Mapách a Vyhľadávaní. Je bezplatný a pre lokálne firmy je najrýchlejší zdroj zákazníkov z Google. Nastavíte ho za 8 hodín: založenie a overenie, kategórie a služby, fotky, Q&A, stratégia hodnotení. Klienti, ktorí hľadajú lokálne služby, vás nájdu prví: 54 percent zobrazení profilu prichádza cez Mapy, 46 percent cez Vyhľadávanie.</p>
<figure class="blog-chart">{donut}</figure>

<h2>Ako som získal 359 zobrazení profilu za mesiac</h2>
<p>Konkrétny prípad z mojej praxe: lokálna firma s 1 pôsobiskom, ktorá nemala žiadny Google profil. Po nastavení a 2 mesiacoch údržby dosiahol profil 359 zobrazení za mesiac, z toho 54 percent cez Google Mapy a 46 percent cez Google Vyhľadávanie. Práca pozostávala z:</p>
<ul>
<li><strong>Založenie a overenie</strong>: presný názov, adresa, kategória, overenie pohľadnicou</li>
<li><strong>Kompletné dáta</strong>: kategórie, služby, otváracie časy, atribúty, popis</li>
<li><strong>14 fotiek</strong>: interiér, exteriér, tímu, práca v procese</li>
<li><strong>Q&A</strong>: 6 otázok a odpovedí, ktoré zákazníci reálne pýtajú</li>
<li><strong>Hodnotenia</strong>: 12 hodnotení za 3 mesiace cez SMS/QR postup, priemer 4.8</li>
<li><strong>Odpovede</strong>: na každé hodnotenie, aj zlé, profesionálne a do 24 hodín</li>
</ul>
<p>Tento výsledok nie je výnimočný, je normálny, ak máte kompletný profil a aktívne hodnotenia. Bez profilu by táto firma nemala žiadne zobrazenia v Mapách a chýbala by v lokálnom pack (top 3 v Mapách pri lokálnom dopyte).</p>
<p><em>Zdroj: štatistiky Google firemného profilu klienta, ukážka zo septembra 2026.</em></p>

<h2>Krok 1: Založenie a overenie profilu</h2>
<p>Profil vytvoríte na <a href="https://www.google.com/business/" target="_blank" rel="noopener noreferrer">google.com/business</a>. Pri založení:</p>
<ol>
<li><strong>Prihláste sa</strong> Google účtom, ktorý chcete pre firmu používať.</li>
<li><strong>Vyhľadajte názov firmy</strong>: profil už môže existovať (Google ho vytvoril automaticky). Prevezmite ho, nezakladajte duplicitu.</li>
<li><strong>Vyplňte presný názov firmy</strong>: bez pridaných kľúčových slov (Google to zakazuje, za pridávanie "najlepší zubár Nitra" hrozí obmedzenie profilu).</li>
<li><strong>Vyplňte adresu</strong> alebo obsluhovanú oblasť (ak nemáte kamennú prevádzku).</li>
<li><strong>Vyberte kategóriu</strong>: primárnu (najužšiu pravdivú, napríklad "Zubná ambulancia" nie "Služby").</li>
<li><strong>Overte profil</strong>: pohľadnicou (list pošty), telefónom, alebo videom (najrýchlejšie, 5 minút).</li>
</ol>
<p>Podrobnosti overenia v <a href="https://support.google.com/business/answer/3038177" target="_blank" rel="noopener noreferrer">pomoci Google</a>. Bez overenia profil nie je verejný.</p>

<h2>Krok 2: Kategórie, služby a dáta</h2>
<p>Kategórie sú najdôležitejší signál, na ktoré dopyty sa profil zobrazí. Pravidlá:</p>
<ul>
<li><strong>Primárna kategória</strong>: najužšia pravdivá. Nie "Reštaurácia", ale "Slovenská reštaurácia". Nie "Služby", ale "Zubná ambulancia".</li>
<li><strong>Sekundárne kategórie</strong>: súvisiace, maximálne 9. Pre zubára: "Detská zubná ambulancia", "Zubná protetika", "Chirurgia ústnej dutiny".</li>
<li><strong>Služby</strong>: zoznam s popismi a cenami (ak sú verejné). Google ich zobrazí v profile a v Search.</li>
<li><strong>Atribúty</strong>: "Ženy vlastnené", "Wheelchair accessible", "Wi-Fi", "Parkovanie". Pomáhajú pri špecifických dopytoch.</li>
<li><strong>Popis</strong>: 750 znakov, odpovedá na otázky zákazníkov, nie firemná historika. Obsahuje kľúčové slová prirodzene.</li>
<li><strong>Otváracie časy</strong>: aktuálne, vrátane výnimiek (sviatky, dovolenky). Google penalizuje neaktuálne časy.</li>
</ul>

<h2>Krok 3: Fotky</h2>
<p>Fotky pôsobia na zákazníkov viac než text. Pravidlá:</p>
<ul>
<li><strong>Minimum 10 fotiek</strong>: interiér, exteriér, tímu, produkty, práca v procese.</li>
<li><strong>Aktuálne</strong>: mladšie ako 6 mesiacov. Staré fotky pôsobia neaktívne.</li>
<li><strong>Kvalita</strong>: minimálne 720x720 pixelov, dobre nasvietené, profesionálne.</li>
<li><strong>Logo a cover photo</strong>: pridajte logo a cover photo, ktorá reprezentuje firmu.</li>
</ul>
<p>Google preferuje profily s aktuálnymi fotkami a častejšie ich zobrazuje. Bez fotiek profil pôsobí neaktívne a zákazníci ho preskakujú.</p>

<h2>Krok 4: Q&A (otázky a odpovede)</h2>
<p>Q&A sekcia je často prehliadaná, ale Google ju zobrazuje v Mapách a vo Search. Pravidlá:</p>
<ul>
<li>Pridajte 3-5 vlastných otázok s odpoveďami (časté otázky zákazníkov: parkovanie, platba, dostupnosť, pôsobisko).</li>
<li>Odpovedajte na otázky, ktoré zákazníci pridali sami, do 24 hodín.</li>
<li>Google tento obsah cituje aj v AI odpovediach (ChatGPT, AI Overviews), keď pýtajú "odporúč mi [služba] v [mesto]".</li>
</ul>

<h2>Krok 5: Hodnotenia a recenzie</h2>
<p>Hodnotenia sú druhý najsilnejší lokálny SEO faktor (po blízkosti). Pravidlá:</p>
<ul>
<li><strong>Minimum 5 hodnotení</strong> pre zobrazenie hviezd v Mapách. Cieľ: 20+ hodnotení, priemer 4.5+.</li>
<li><strong>Ako získať</strong>: po službe pošlite zákazníkovi SMS s linkom na hodnotenie, alebo QR kód na vizitke. Miera recenzií rastie násobne, lebo zákazník má link v ruke v čase, keď je spokojný.</li>
<li><strong>Odpovedajte na každé hodnotenie</strong>: aj zlé, profesionálne a na mieste. Odpovede na zlé hodnotenia viac ovplyvňujú zákazníkov než počet hviezd.</li>
<li><strong>Nekupujte hodnotenia</strong>: Google detekuje falošné recenzie a profil obmedzí.</li>
</ul>

<h2>Krok 6: NAP konsistencia</h2>
<p>NAP = Name, Address, Phone. Musí byť identický naprieč:</p>
<ul>
<li>Google firemný profil</li>
<li>Web firmy (footer, kontaktná stránka)</li>
<li>firmy.sk, zlatystranky.sk, lokálne adresáre</li>
<li>Sociálne siete (Facebook, Instagram)</li>
</ul>
<p>Ak máte "Peter Novák s.r.o." v Google profile a "P. Novák s.r.o." na webe, Google profilu menej neverí a zaradí vás nižšie v Mapách. Udržiavajte NAP konzistentný.</p>

<h2>Krok 7: Príspevky (GBP Posts)</h2>
<p>GBP Posts sú krátke príspevky, ktoré sa zobrazujú v profile. Dôležité: Sterling Sky štúdia (441 kľúčových slov) ukázala, že Posts <strong>neovplyvňujú pozície</strong>, ale ovplyvňujú kliky a konverzie. Pravidlá:</p>
<ul>
<li>Frekvencia: 1-2 Posts týždenne (akcie, novinky, produkty).</li>
<li>Typ: "Akcia" (zľava), "Novinka" (oznámenie), "Produkt" (nový produkt), "FAQ" (odpoveď na otázku).</li>
<li>Pridajte fotku a CTA tlačidlo ("Zavolať", "Navštíviť web", "Rezervovať").</li>
<li>Posts zmiznú po 7 dňoch, pridávajte pravidelne.</li>
</ul>

<h2>Krok 8: Meranie a insights</h2>
<p>Google profil má bezplatné insights:</p>
<ul>
<li><strong>Zobrazenia profilu</strong>: koľko ľudí videlo profil v Mapách a vo Search.</li>
<li><strong>Volania</strong>: koľko ľudí kliklo na "Zavolať" z profilu.</li>
<li><strong>Žiadosti o trasu</strong>: koľko ľudí si vyžiadalo navigáciu.</li>
<li><strong>Vyhľadávania</strong>: na aké dopyty sa profil zobrazil (priame, brand, discovery).</li>
<li><strong>Kliky na web</strong>: koľko ľudí kliklo z profilu na váš web.</li>
</ul>
<p>Tieto dáta overte mesačne. Ak zobrazenia nestúpajú, profil nie je dostatočne vyplnený, alebo konkurencia má viac hodnotení. Kompletné nastavenie a vedenie profilu rieši <a href="/sk/sluzby/lodalne-seo/">lokálne SEO služba</a>.</p>
"""
    faq = [
        ("Ako založím Google firemný profil?",
         "Prihláste sa na google.com/business Google účtom. Vyhľadajte názov firmy (profil už môže existovať, prevezmite ho). Vyplňte presný názov, adresu, kategóriu. Overte profil pohľadnicou, telefónom, alebo videom (najrýchlejšie, 5 minút). Bez overenia profil nie je verejný."),
        ("Je Google firemný profil bezplatný?",
         "Áno, úplne bezplatný. Google neúčtuje za profil žiadne poplatky. Platíte len za svoj čas (8 hodín na nastavenie) alebo za SEO špecialistu, ak si ho objednáte."),
        ("Ako získam viac hodnotení na Google?",
         "Po službe pošlite zákazníkovi SMS s linkom na hodnotenie, alebo QR kód na vizitke. Miera recenzií rastie násobne, lebo zákazník má link v ruke v čase, keď je spokojný. Nekupujte hodnotenia, Google ich detekuje a profil obmedzí."),
        ("Koľko hodnotení potrebujem?",
         "Minimum 5 pre zobrazenie hviezd v Mapách. Cieľ: 20+ hodnotení, priemer 4.5+. Viac hodnotení znamená vyššiu pozíciu v Mapách a viac dôvery od zákazníkov."),
        ("Ako odpovedať na zlé hodnotenia?",
         "Profesionálne, na mieste, do 24 hodín. Nezľutujte sa, neprepirajte sa. Príklad: 'Ďakujeme za spätnú väzbu. Mrí nás, že vaša skúsenosť nebola pozitívna. Prosím, zavolajte nám na [telefón], aby sme to mohli napraviť.' Odpovede na zlé hodnotenia viac ovplyvňujú zákazníkov než počet hviezd."),
        ("Pomáhajú GBP Posts pozíciám?",
         "Nie, Sterling Sky štúdia (441 kľúčových slov) ukázala, že Posts neovplyvňujú pozície v Mapách. Ale ovplyvňujú kliky a konverzie: zákazníci vidia akcie a novinky, keď navštívia profil. Pridávajte 1-2 Posts týždenne."),
        ("Čo je NAP a prečo záleží?",
         "NAP = Name, Address, Phone. Musí byť identický naprieč Google profilom, webom, firmy.sk, zlatystranky.sk, sociálnymi sieťami. Ak máte nezrovnalosti, Google profilu menej neverí a zaradí vás nižšie v Mapách."),
        ("Ako dlho trvá, kým profil začne fungovať?",
         "Prvé zlepšenia viditeľné za 4 až 8 týždňov, stabilná pozícia v lokálnom pack trvá 3 až 6 mesiacov. Záleží na konkurencii v okolí a počte hodnotení."),
    ]
    return blog_post(slug="google-firmy-profil-navod", label="Lokálne SEO", h1="Google firemný profil: návod od založenia po hodnotenia",
                     answer="Google firemný profil nastavíte za 8 hodín: založenie, kategórie, fotky, Q&A, hodnotenia cez SMS a QR kód. Návod s prípadovou štúdiou: 359 zobrazení profilu za mesiac.",
                     sections=sections, faq=faq,
                     related=[("seo-test-15-bodov", "SEO test: 15-bodový kontrolný zoznam"), ("seo-wordpress", "SEO pre WordPress: 12 nastavení")],
                     date_iso="2026-09-16", date_display="16. 9. 2026")


def blog_post_wordpress() -> tuple[str, str]:
    """REFRESH 2026-09-16. Target: 'seo optimalizacia wordpress' (130 SV/mo, +94% YoY, peak Mar 620).
    SERP: wplama.cz, vas-hosting.cz, svetwp.cz, seoconsult.cz. All CZ, generic Yoast guides.
    Angle: SK-first with 12 concrete settings, Yoast vs RankMath comparison, CWV for WP."""
    wp_chart = _bars([4, 3, 3, 2], _CERULEAN, ["rýchlosť", "štruktúra", "schéma", "obsah"])
    sections = f"""
<h2>Stručná odpoveď</h2>
<p>SEO pre WordPress vyžaduje 12 konkrétnych nastavení: permalinky, SEO plugin (Yoast alebo RankMath), rýchlosť (cache + WebP), meta titulky a popisky, štruktúrované dáta, sitemap, robots.txt, interné prelinkovanie, alt texty, hreflang, komentáre a meranie v Search Console. Zaberá 6 až 10 hodín. WordPress je na SEO pripravený, ale bez týchto nastavení ho Google nedokáže správne zaradiť.</p>
<figure class="blog-chart">{wp_chart}</figure>

<h2>Yoast SEO vs Rank Math: ktorý plugin použiť</h2>
<p>WordPress má dva hlavné SEO pluginy. Oba sú funkčné, ale majú rozdiely:</p>
<table class="metric-table">
<tr><th>Aspekt</th><th>Yoast SEO</th><th>Rank Math</th></tr>
<tr><td><strong>Cena</strong></td><td>Bezplatná verzia + Premium 99 EUR/rok</td><td>Bezplatná verzia (viac funkcií) + Pro 59 EUR/rok</td></tr>
<tr><td><strong>Štruktúrované dáta</strong></td><td>Basic (Organization, Article)</td><td>Komplexné (viac typov, custom schema)</td></tr>
<tr><td><strong>Sitemap</strong></td><td>Vlastná</td><td>Vlastná, rýchlejšia</td></tr>
<tr><td><strong>Meta šablóny</strong></td><td>Áno, premenné</td><td>Áno, viac premenných</td></tr>
<tr><td><strong>AI assistant</strong></td><td>Áno (Premium)</td><td>Áno (v bezplatnej)</td></tr>
<tr><td><strong>Pre koho</strong></td><td>Začiatočníci, jednoduchosť</td><td>Pokročilí, viac funkcií zdarma</td></tr>
</table>
<p><strong>Nikdy nenainštalujte obe.</strong> Dva SEO pluginy konfliktujú, generujú duplicitné meta tagy a schema. Vyberte jeden. Pre nové weby odporúčam Rank Math (viac funkcií v bezplatnej verzii), pre existujúce weby s Yoast nemá zmysel migrovať, ak Yoast funguje.</p>

<h2>Nastavenie 1-4: Rýchlosť (Core Web Vitals)</h2>
<h3>1. Cache plugin</h3>
<p>Nainštalujte <a href="https://wp-rocket.me/" target="_blank" rel="noopener noreferrer">WP Rocket</a> (platený, 49 EUR/rok) alebo <a href="https://wordpress.org/plugins/litespeed-cache/" target="_blank" rel="noopener noreferrer">LiteSpeed Cache</a> (bezplatný, ak máte LiteSpeed server). Zapnite: page caching, gzip compression, minifikácia CSS/JS, lazy loading obrázkov. Toto jediné nastavenie zlepší LCP o 1-2 sekundy.</p>
<h3>2. WebP obrázky a lazy loading</h3>
<p>Nainštalujte <a href="https://shortpixel.com/" target="_blank" rel="noopener noreferrer">ShortPixel</a> alebo <a href="https://imagify.io/" target="_blank" rel="noopener noreferrer">Imagify</a> na automatickú konverziu JPEG/PNG na WebP. WebP je o 25-35 percent menší. Zapnite lazy loading (WP Rocket alebo LiteSpeed ho má v sebe). Obrázky sa načítavajú len pri scrolle, nie všetky naraz.</p>
<h3>3. Fonty lokálne alebo preconnect</h3>
<p>Ak používate Google Fonts, pridajte <code>rel="preconnect"</code> do hlavičky. Lepšie: stiahnite fonty lokálne (cez plugin OMGF alebo manuálne). Google Fonts CDN pridáva 100-300ms na LCP.</p>
<h3>4. LCP prvok pod 2.5s</h3>
<p>Testujte cez <a href="https://pagespeed.web.dev/" target="_blank" rel="noopener noreferrer">PageSpeed Insights</a>. Ak je LCP nad 2.5s, overte: hero obrázok je WebP a lazy loaded? Server odpovedá pod 600ms? CSS je minifikované? Veľký obrázok hero sekcie je najčastejšia príčina pomalého LCP na WordPress.</p>

<h2>Nastavenie 5-7: Štruktúra</h2>
<h3>5. Permalinky na /%postname%/</h3>
<p>Choďte do Nastavenia > Permalinky a vyberte "Názov príspevku". URL bude vyzerať: vasadomena.sk/nazov-clanku/. Nie vasadomena.sk/?p=123. Čisté URL s kľúčovým slovom sú prvý SEO signál. <a href="https://wordpress.org/documentation/article/settings-permalinks-screen/" target="_blank" rel="noopener noreferrer">Oficiálna dokumentácia WordPress</a>.</p>
<h3>6. XML sitemap generovaná a odoslaná do Search Console</h3>
<p>Yoast aj RankMath generujú sitemap automaticky. Nájdete ju na vasadomena.sk/sitemap_index.xml. Overte v <a href="https://search.google.com/search-console" target="_blank" rel="noopener noreferrer">Google Search Console</a> > Sitemaps, že je odoslaná a bez chýb.</p>
<h3>7. Robots.txt, ktorý neblokuje indexáciu</h3>
<p>Choďte do Nastavenia > Čítanie a overte, že "Zobraziť web vyhľadávačom" je NEZAŠKRKNUTÉ. Častá chyba: web je nechtiac v noindex. Potom vytvorte robots.txt (cez Yoast alebo RankMath), ktorý Allow všetko okrem /wp-admin/.</p>

<h2>Nastavenie 8-10: Meta a schéma</h2>
<h3>8. Unikátne titulky s dopytom zákazníka</h3>
<p>V Yoast alebo RankMath nastavte meta šablóny pre každý typ obsahu: Príspevky, Stránky, Kategórie, Produkty. Príklad pre príspevky: <code>%%title%% | %%sitename%%</code>. Pre stránky: <code>%%title%% | Nokto Studio</code>. Overte, že každá stránka má unikátny title, 50-60 znakov, s kľúčovým slovom.</p>
<h3>9. Meta popisky, ktoré čerpajú z reálnych dopytov</h3>
<p>Meta description: 150-160 znakov, odpovedá na otázku zákazníka, obsahuje kľúčové slovo a CTA. Yoast aj RankMath majú AI assistant na generovanie popisok, ale overte ich: AI často píše generické popisky bez reálneho dopytu.</p>
<h3>10. Štruktúrované dáta (schema)</h3>
<p>RankMath generuje automaticky: Organization, WebSite, BreadcrumbList, Article, Person. Yoast generuje basic verziu, v Premium aj Article. Overte cez <a href="https://search.google.com/test/rich-results" target="_blank" rel="noopener noreferrer">Rich Results Test</a>. Pre e-shopy pridajte Product schema (cez WooCommerce + Yoast/RankMath). Pre lokálne firmy pridajte LocalBusiness schema (cez RankMath alebo manuálne JSON-LD).</p>

<h2>Nastavenie 11-12: Obsah a interné prelinkovanie</h2>
<h3>11. Alt texty na všetkých obrázkoch</h3>
<p>Alt text je popis obrázku, ktorý Google číta. Každý obrázok by mal mať alt text s kľúčovým slovom (ak je relevantný). V WordPress: Media Library > kliknite na obrázok > vyplňte "Alt text". Pluginy ako Yoast a RankMath upozorňujú na chýbajúce alt texty.</p>
<h3>12. Interné prelinkovanie: 3 odkazy na stránku</h3>
<p>Každá obsahová stránka by mala mať minimálne 3 interné odkazy na iné stránky webu. V WordPress: manuálne v editore, alebo cez plugin <a href="https://wordpress.org/plugins/yet-another-related-posts-plugin/" target="_blank" rel="noopener noreferrer">YARPP</a> (Yet Another Related Posts Plugin) na automatické "súvisiace príspevky". Interné prelinkovanie posúva autoritu z silných stránok k slabším.</p>

<h2>Hreflang pre SK/CZ WordPress weby</h2>
<p>Ak máte viacjazyčný WordPress web (SK + CZ), použite <a href="https://wpml.org/" target="_blank" rel="noopener noreferrer">WPML</a> (platený, 99 EUR/rok) alebo <a href="https://wordpress.org/plugins/polylang/" target="_blank" rel="noopener noreferrer">Polylang</a> (bezplatný). Oba generujú hreflang tagy automaticky. Hreflang povie Google, ktorá stránka je pre ktorý jazyk, a zabraňuje duplicitám. Chyby hreflang sú najčastejšou príčinou kanibalizácie SK/CZ webov.</p>

<h2>WordPress vs. iné platformy</h2>
<p>WordPress je na SEO pripravený, ale záleží na nastavení. Porovnanie s inými platformami:</p>
<table class="metric-table">
<tr><th>Aspekt</th><th>WordPress</th><th>Shoptet</th><th>Vlastná platforma</th></tr>
<tr><td><strong>SEO plugin</strong></td><td>Yoast/RankMath, komplexné</td><td>SEO modul, obmedzený</td><td>Treba nakódovať</td></tr>
<tr><td><strong>Rýchlosť</strong></td><td>Závisí od pluginov, často pomalý</td><td>Stredná, optimalizovaná</td><td>Záleží od vývojára</td></tr>
<tr><td><strong>Schéma</strong></td><td>Automatická cez plugin</td><td>Automatická, ale obmedzená</td><td>Treba nakódovať JSON-LD</td></tr>
<tr><td><strong>Hreflang</strong></td><td>WPML/Polylang</td><td>Vestavnený</td><td>Treba nakódovať</td></tr>
<tr><td><strong>Interné prelinkovanie</strong></td><td>YARPP, manuálne</td><td>Modul "súvisiace produkty"</td><td>Treba nakódovať</td></tr>
</table>
<p>Pri SEO má nástroj druhoradú úlohu: dôležitá je stratégia a jej vykonávanie. WordPress, Shoptet, WooCommerce aj vlastné riešenia sa optimalizujú rovnakými princípmi: technika, obsah, autorita.</p>
"""
    faq = [
        ("Ktorý plugin na SEO v WordPress je najlepší?",
         "Rank Math pre nové weby (viac funkcií v bezplatnej verzii: komplexná schema, AI assistant, rýchlejšia sitemap). Yoast pre existujúce weby (ak funguje, nemá zmysel migrovať). Nikdy nenainštalujte obe, konfliktujú a generujú duplicitné meta tagy."),
        ("Zaberie to viac ako 12 nastavení?",
         "Základ je 12 bodov, 6-10 hodín. Na konkurenčné dopyty k tomu prichádza obsah (písanie textov), interné prelinkovanie, linkbuilding a AI viditeľnosť. Detailnejšie v <a href='/sk/blog/seo-optimalizacia-navod/'>kompletnom SEO návode</a>."),
        ("Ako zlepším rýchlosť WordPress webu?",
         "Nainštalujte WP Rocket (49 EUR/rok) alebo LiteSpeed Cache (bezplatný). Zapnite cache, minifikáciu, lazy loading. Konvertujte obrázky na WebP cez ShortPixel alebo Imagify. Stiahnite Google Fonts lokálne. Cieľ: LCP pod 2.5s, INP pod 200ms, CLS pod 0.1."),
        ("Je WordPress dobrý pre SEO?",
         "Áno, s Yoast alebo RankMath a 12 nastaveniami z tohto návodu. Bez nastavenia je WordPress priemerný: pomalý, bez schema, bez čistých URL. So správnym nastavením je rovnako dobrý ako vlastná platforma."),
        ("Potrebujem WPML pre SK/CZ?",
         "Áno, ak máte viacjazyčný web. WPML (99 EUR/rok) alebo Polylang (bezplatný) generujú hreflang tagy automaticky. Bez hreflang Google zaradí rovnakú stránku pre SK aj CZ, čo spôsobí kanibalizáciu a zrazí pozície."),
        ("Čo je permalink a prečo záleží?",
         "Permalink je štruktúra URL. Nastavte na /%postname%/ (vasadomena.sk/nazov-clanku/). Nie /?p=123. Čisté URL s kľúčovým slovom sú prvý SEO signál. Nastavenie: Nastavenia > Permalinky > Názov príspevku."),
        ("Ako nastavím schema na WordPress?",
         "RankMath generuje automaticky: Organization, WebSite, BreadcrumbList, Article, Person. Yoast generuje basic verziu. Overte cez Rich Results Test (search.google.com/test/rich-results). Pre e-shopy pridajte Product schema cez WooCommerce + Yoast/RankMath."),
        ("Pomôžete aj s implementáciou?",
         "Áno, 12 nastavení nastavím priamo v CMS alebo pripravím súbor pre vývojára. Základ popisuje <a href='/sk/sluzby/seo-optimalizacia/'>SEO optimalizácia webu</a>. Zaberá 6-10 hodín (72-120 EUR)."),
    ]
    return blog_post(slug="seo-wordpress", label="WordPress", h1="SEO pre WordPress: 12 nastavení, ktoré treba spraviť",
                     answer="SEO pre WordPress: 12 konkrétnych nastavení od permalinks po schému. Yoast vs RankMath porovnanie. Prejde sa za 30 minút, implementuje v 6 až 10 hodinách.",
                     sections=sections, faq=faq,
                     related=[("seo-optimalizacia-navod", "SEO optimalizácia: kompletný návod"), ("kolko-stoji-seo", "Koľko stojí SEO v roku 2026?")],
                     date_iso="2026-09-16", date_display="16. 9. 2026")


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
