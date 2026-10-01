# -*- coding: utf-8 -*-
"""Nokto Studio - CZ blog (CZ translations of the SK content wave, 1:1 pairs).

Created 2026-10-01. The CZ blog previously showed only "Připravujeme" cards.
This module brings the first two real CZ posts (E-shop, SEO audit) and the
listing. New posts are added here together with their SK originals in
pages_sk2.py, so the hreflang pairs in engine.py stay in sync.
"""
from engine import (base, page_hero, cta_band, faq_block, faq_schema, article_schema,
                    ORG_SCHEMA_CZ, BASE)

# ---------------------------------------------------------------- META

_BLOG_META = {
    "seo-pro-eshop": dict(
        title="SEO pro e-shop: 9 nastavení, která přinášejí objednávky | Nokto Studio",
        desc="SEO pro e-shop od kategorií po Merchant Center: 9 nastavení, která přinášejí objednávky z Google. Reálné zkušenosti, ceny a časté chyby."),
    "seo-audit-co-to-je": dict(
        title="SEO audit: co to je, kolik stojí a jak probíhá | Nokto Studio",
        desc="SEO audit jednoduše: co obsahuje, kolik stojí (od 180 EUR, vstupní zdarma) a jak z auditu udělat plán s prioritami. Příklad z praxe."),
}


def blog_post(*, slug: str, label: str, h1: str, answer: str, sections: str,
              faq: list[tuple[str, str]], related: list[tuple[str, str]],
              services: list[tuple[str, str]] | None = None,
              date_iso: str = "2026-10-01", date_display: str = "1. 10. 2026") -> tuple[str, str]:
    """Render one CZ blog post: direct answer first, sections, FAQ, related, CTA."""
    rel_cards = ""
    for u, n in related:
        rel_cards += (f'<div class="benefit-card card-hover related-card">'
                      f'<span class="project-tags"><span class="project-tag tag-violet">Článek</span></span>'
                      f'<h3><a href="/cz/blog/{u}/" style="color:var(--text);">{n}</a></h3></div>')
    for u, n in (services or []):
        rel_cards += (f'<div class="benefit-card card-hover related-card">'
                      f'<span class="project-tags"><span class="project-tag tag-cerulean">Služba</span></span>'
                      f'<h3><a href="{u}" style="color:var(--text);">{n}</a></h3></div>')
    body = f"""
<section class="post-hero">
  <div class="container" style="max-width:820px;">
    <a href="/cz/blog/" class="post-back">← Blog</a>
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
    <div class="section-head"><span class="section-label">Přečtěte si také</span><h2>Související články a služby</h2></div>
    <div class="grid-2">{rel_cards}</div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    {cta_band("Chcete to udělat na svém webu?", "Začněme bezplatným auditem. Uvidíte, co bych řešil jako první, ještě před první fakturou.", "cz")}
  </div>
</section>
"""
    meta = _BLOG_META[slug]
    url = BASE + f"/cz/blog/{slug}/"
    html = base(market="cz", path=f"blog/{slug}/", title=meta["title"], desc=meta["desc"],
                canonical=url, body=body, prefix="../../../", og_type="article",
                extra_head=ORG_SCHEMA_CZ + article_schema(url=url, title=meta["title"],
                                                           desc=meta["desc"], date_iso=date_iso, lang="cz")
                          + faq_schema(faq, url))
    return (f"cz/blog/{slug}/index.html", html)


# ---------------------------------------------------------------- POSTS

def blog_post_eshop() -> tuple[str, str]:
    """CZ pair of /sk/blog/seo-pre-eshop/. Target: 'seo optimalizace eshopu'
    (460 SV/mo, diff 34, +42 % YoY), 'seo optimalizace e-shopu' (130)."""
    sections = """
<h2>Co je SEO pro e-shop</h2>
<p>SEO pro e-shop je práce na tom, aby zákazník, který hledá konkrétní produkt nebo kategorii, skončil ve vašem obchodě a objednal. Nejde o návštěvnost, ale o objednávky. Rozdíl proti firemnímu webu je v rozsahu: e-shop má tisíce URL (kategorie, produkty, filtry, značky) a každá z nich může buď vydělávat, nebo kanibalizovat jinou. Proto e-shop SEO stojí na struktuře, datech a obsahu, ne na jednom triku.</p>

<h2>9 nastavení, která rozhodují o objednávkách</h2>
<h3>1. Kategorie: texty, které odpovídají nákupní poptávce</h3>
<p>Kategorie je nejsilnější stránka e-shopu: sbírá poptávku typu "koupit + produkt" a rozděluje autoritu produktům. Text kategorie pište v rozsahu 250 až 400 slov: co kategorie obsahuje, jak vybírat, na co si dát pozor. Prvních 60 slov musí být přímá odpověď pro zákazníka i pro AI vyhledávače. Vyhněte se frázím typu "jsme nejlepší", pište parametry a rozhodovací kritéria.</p>
<h3>2. Produkty: titulky a parametry na reálné dotazy</h3>
<p>Produktový titulek skládejte jako značka + model + parametr. Lidé hledají "židle 40 cm" nebo "stan pro 4 osoby", ne "židle super nabídka". Parametry (rozměry, materiál, kompatibilita) dejte do tabulky, Google z nich skládá long-tail shody. A pozor na duplicitní popisy od dodavatele: pokud má stejný text deset dalších e-shopů, Google nemá důvod ukázat právě vás.</p>
<h3>3. Filtry a parametry: canonical a indexace</h3>
<p>Filtrované URL (barva, velikost, značka) vytvářejí tisíce duplicit. Řešení: canonical na základní kategorii, noindex na kombinace bez poptávky a index jen tam, kde existuje reálné hledání (například "dřevěné židle"). Toto jedno nastavení umí zachránit crawl budget i pozice.</p>
<h3>4. Produktové schéma a rich results</h3>
<p>Product schema (cena, dostupnost, hodnocení, doprava) posouvá výsledek do rich results s cenou a hvězdičkami. Vyšší CTR při stejném rozpočtu. Schéma musí sedět s obsahem stránky, jinak hrozí manuální penalizace.</p>
<h3>5. Google Merchant Center a Heureka</h3>
<p>Feed do Google Merchant Center vás pustí do nákupních výsledků a Performance Max, Heureka do porovnávačů. Feed a SEO se doplňují: opravený produktový titulek pomůže oběma kanálům. Základ je čistý produktový feed: titulky, GTIN, ceny, dostupnost, obrázky.</p>
<h3>6. Interní prolinkování</h3>
<p>Kategorie odkazuje na podkategorie a top produkty, blog odkazuje na produkty v textu, "související produkty" dostanou druhou šanci. Pravidlo: každá důležitá stránka má alespoň 3 interní odkazy z relevantního kontextu. Bez prolinkování zůstanou produkty na páté stránce, i když mají nejlepší titulky.</p>
<h3>7. Rychlost a Core Web Vitals</h3>
<p>E-shopy jsou těžké: hodně obrázků, filtrů a skriptů. Cíl: LCP pod 2,5 s (hero obrázek ve WebP, lazy loading), INP pod 200 ms (minimalizovat blokující JavaScript z filtrů), CLS pod 0,1 (fixní rozměry obrázků). Rychlost přímo ovlivňuje konverzi i pozice.</p>
<h3>8. Obsah podle nákupní fáze</h3>
<p>Kategorie pokrývají "kupuji", blog pokrývá "vybírám" a "porovnávám". Návody typu "jak si vybrat", porovnání a FAQ zachytávají zákazníka před rozhodnutím a přivádějí ho na produkt. Přesně tento obsah vaše konkurence často nemá a AI nástroje ho rády citují.</p>
<h3>9. Měření objednávek z organiky</h3>
<p>Rozhoduje objednávka a tržba z organického vyhledávání. GA4 s e-commerce eventy, Search Console pro dotazy a pozice, e-shopový systém pro reálné objednávky. Pokud se čísla nedají spárovat, SEO nemá důkaz. Měříme objednávky, ne pocity.</p>

<h2>Reálný výsledek z praxe</h2>
<p>Na projektu Mikramt (menší e-shop na vlastní platformě) přinesla devítiměsíční práce 15 objednávek a 2 492,75 EUR tržeb z organického a emailového kanálu, s největší objednávkou 722 EUR. Pracovali jsme na kategoriích (předtím prázdné texty), strukturovaných datech, Google Merchant Center a emailových sekvencích. Číslo není obrovské, ale je reálné a měřitelné, což je u SEO důležitější než sliby.</p>

<h2>Časté chyby, které brzdí e-shopy</h2>
<ul>
<li>Duplicitní produktové popisy od dodavatele bez vlastního textu.</li>
<li>Prázdné kategorie bez textu, které Google vyhodnotí jako tenký obsah.</li>
<li>noindex omylem nasazený na kategorie, často po migraci.</li>
<li>Rozbitá indexace filtrů: tisíce URL v indexu bez poptávky.</li>
<li>Měření jen přes celkovou návštěvnost, bez objednávek z organiky.</li>
</ul>

<h2>Za jak dlouho a co to stojí</h2>
<p>Long-tail produkty a menší kategorie se hýbou za 2 až 4 měsíce, hlavní kategorie za 6 až 12 měsíců, podle konkurence a stavu webu. Práce je 10 až 15 hodin měsíčně, tedy 120 až 180 EUR měsíčně při sazbě 12 EUR za hodinu, plus náklady na odkazy a případný obsah. Přesný rozsah vždy potvrzuje bezplatný audit.</p>
"""
    faq = [
        ("Kolik stojí SEO pro e-shop?",
         "Práce je 10 až 15 hodin měsíčně, tedy 120 až 180 EUR při sazbě 12 EUR za hodinu. Vstupní nastavení (technika, struktura, feed) je 6 až 10 hodin jednorázově. Náklady na odkazy a obsah se vykazují zvlášť, bez přirážky."),
        ("Jak dlouho trvá, než přijdou první objednávky z organiky?",
         "Long-tail produkty a menší kategorie za 2 až 4 měsíce, hlavní kategorie za 6 až 12 měsíců. U nového e-shopu bez autority je první měsíc o technice a struktuře, objednávky přicházejí postupně s tím, jak Google stránky zaindexuje."),
        ("Stačí mi SEO modul ve Shoptetu?",
         "SEO modul zvládne titulky, popisky a sitemap, to je dobrý základ. Nevyřeší texty kategorií, produktové popisy, interní prolinkování, obsah podle nákupní fáze ani měření objednávek z organiky. Přesně tyto věci rozhodují o pozicích v konkurenci."),
        ("Mám duplicitní popisy od dodavatele. Je to problém?",
         "Ano. Pokud má stejný popis deset e-shopů, Google nemá důvod upřednostnit právě vás. Řešení: vlastní úvodní odstavec s parametry a rozhodovacími kritérii u každého důležitého produktu, zbytek může zůstat od dodavatele."),
        ("Je lepší investovat do Google Shopping, nebo do SEO?",
         "Doplňují se. Shopping přináší objednávky hned, ale platíte za každý klik. SEO roste pomaleji, ale objednávka z organiky je levnější a zůstává vám. Zdravý e-shop má oba kanály a feed do Merchant Center je základ pro oba."),
        ("Jak změřím objednávky z organického vyhledávání?",
         "GA4 s e-commerce eventy (purchase), Search Console pro dotazy a pozice a e-shopový systém pro reálné objednávky. V reportu spojujeme tyto tři zdroje, abyste viděli, které stránky a dotazy přinášejí tržby, ne jen návštěvnost."),
        ("Děláte i WooCommerce e-shopy?",
         "Ano. WooCommerce řeším přes <a href='/cz/sluzby/seo-pre-wordpress/'>SEO pro WordPress</a>: rychlost, produktové schéma, feed a struktura. Principy jsou stejné jako u Shoptetu, liší se jen technické prostředí."),
        ("Pro koho má e-shop SEO největší smysl?",
         "Pro e-shopy, které už prodávají a mají co optimalizovat: existující kategorie, produkty a alespoň základní tržby. U úplně nového e-shopu bez produktů a bez rozpočtu na obsah doporučuji nejprve vyřešit nabídku a potom SEO."),
    ]
    return blog_post(slug="seo-pro-eshop", label="E-shop", h1="SEO pro e-shop: 9 nastavení, která přinášejí objednávky",
                     answer="SEO pro e-shop stojí na 9 nastaveních: texty kategorií, produktové titulky na reálné dotazy, filtrace a canonical, produktové schéma, feed do Merchant Center, interní prolinkování, rychlost, obsah podle nákupní fáze a měření objednávek. Rozhodují objednávky, ne návštěvnost.",
                     sections=sections, faq=faq,
                     related=[("seo-audit-co-to-je", "SEO audit: co to je, kolik stojí a jak probíhá")],
                     services=[("/cz/sluzby/seo-pre-eshopy/", "SEO pro e-shopy"), ("/cz/sluzby/seo-audit/", "SEO audit a analýza")])


def blog_post_audit() -> tuple[str, str]:
    """CZ pair of /sk/blog/seo-audit-co-to-je/. Target: 'seo audit' (610 SV/mo),
    'audit seo' (230), 'seo audity' (210), 'seo online audit' (140, +408 %)."""
    sections = """
<h2>Co je SEO audit</h2>
<p>SEO audit je systematická kontrola webu, která odpovídá na tři otázky: proč web neuspěje v Google, co přesně opravit a v jakém pořadí. Obsahuje technickou část (indexace, rychlost, duplicity, struktura), obsahovou (titulky, klíčová slova, mezery proti konkurenci) a autoritu (zpětné odkazy, signály E-E-A-T). Výstupem není PDF do šuplíku, ale plán s prioritami a odhadem hodin.</p>

<h2>Vstupní, technický a komplexní audit: jaký je rozdíl</h2>
<table class="metric-table">
<tr><th>Typ</th><th>Co řeší</th><th>Cena</th><th>Kdy ho chcete</th></tr>
<tr><td><strong>Vstupní audit</strong></td><td>10 největších problémů a šancí na jedné stránce</td><td>zdarma</td><td>první kontakt, rychlá orientace</td></tr>
<tr><td><strong>Technický audit</strong></td><td>indexace, rychlost, duplicity, struktura URL</td><td>od 180 EUR</td><td>před migrací nebo při propadu</td></tr>
<tr><td><strong>Komplexní SEO audit</strong></td><td>technika + obsah + klíčová slova + konkurence + plán</td><td>240 až 480 EUR</td><td>před ročním plánem a rozpočtem</td></tr>
</table>

<h2>Jak probíhá: 5 kroků</h2>
<ol>
<li>Sběr dat: Search Console, GA4, sitemap a přístupy.</li>
<li>Crawl webu: indexace, chyby, duplicity, rychlost (Screaming Frog a PageSpeed Insights).</li>
<li>Analýza poptávky: na co lidé hledají, kde jste viditelní a kde ne.</li>
<li>Pořadí priorit: dopad na objednávky a poptávky proti pracnosti.</li>
<li>Plán: co, kdy a za kolik hodin, s měřitelnými cíli.</li>
</ol>

<h2>Co audit obsahuje</h2>
<h3>Technika (12 bodů)</h3>
<p>Indexace, sitemap, robots.txt, canonical, duplicity, rychlost (LCP, INP, CLS), HTTPS, strukturovaná data, hreflang, interní prolinkování, 404 a přesměrování, mobilní verze.</p>
<h3>Obsah a klíčová slova (10 bodů)</h3>
<p>Titulky a popisky, H1 a hierarchie, tenký obsah, kanibalizace, klíčová slova s objemy, SERP analýza, obsahové mezery proti konkurenci, alt texty, signály E-E-A-T, obsah pro AI odpovědi.</p>
<h3>Autorita (5 bodů)</h3>
<p>Profil zpětných odkazů, toxické odkazy, odkazový náskok konkurence, citace a zmínky, lokální profily.</p>

<h2>Jak číst výsledek auditu</h2>
<p>Dobrý audit má priority P1 (udělejte hned, největší dopad), P2 (do měsíce) a P3 (průběžně). U každé položky je dopad a odhad práce. Pokud dostanete 60 stránek bez pořadí, nedostali jste audit, ale seznam přání. Ptejte se na dvě čísla: kolik hodin to zabere a co to přinese.</p>

<h2>Kolik stojí SEO audit v Česku</h2>
<p>Vstupní audit je u nás zdarma a dostanete ho do 3 pracovních dnů: 10 největších problémů a šancí na jedné stránce. Detailní audit je od 180 EUR (technický) do 480 EUR (komplexní), počítá se hodinovou sazbou 12 EUR. Při pokračující spolupráci je detailní audit součástí prvního měsíce, takže neplatíte dvakrát.</p>

<h2>Příklad z praxe</h2>
<p>Web s přibližně 300 stránkami: audit našel 6 konkrétních obsahových stránek, které na webu chyběly. Po jejich nasazení vzrostly zobrazení o 11 000 měsíčně (+14 %) a kliky o 43 % za týden. Audit nehledal 50 věcí, našel 6, které pohnou celým webem. Tak má vypadat výsledek auditu.</p>

<h2>Kdy audit nepotřebujete</h2>
<p>Máte-li úplně nový web s pěti stránkami, audit je zbytečný, rovnou nastavte základy: titulky, strukturu, Search Console a firemní profil Google. Pokud je web zdravý a roste, stačí čtvrtletní kontrola. Audit má smysl při propadu, před migrací, při stagnaci a před velkým rozpočtem.</p>
"""
    faq = [
        ("Co je SEO audit?",
         "Systematická kontrola webu, která odpovídá na tři otázky: proč web neuspěje v Google, co přesně opravit a v jakém pořadí. Zahrnuje techniku, obsah a autoritu, výstupem je plán s prioritami a odhadem hodin, ne PDF do šuplíku."),
        ("Kolik stojí SEO audit?",
         "Vstupní audit (10 největších problémů na jedné stránce) je zdarma do 3 pracovních dnů. Technický audit od 180 EUR, komplexní audit s obsahem a plánem 240 až 480 EUR. Při pokračující spolupráci je audit součástí prvního měsíce."),
        ("Jak dlouho audit trvá?",
         "Vstupní audit do 3 pracovních dnů. Detailní audit 5 až 10 pracovních dnů podle rozsahu webu a dostupnosti přístupů. U velkých e-shopů s tisíci URL i dva týdny."),
        ("Stačí mi online audit zdarma z internetu?",
         "Automatické nástroje najdou část technických problémů: rychlost, meta tagy, chybějící alt texty. Nenajdou obsahové mezery, kanibalizaci, priority ani kontext vašeho trhu. Bezplatné nástroje jsou dobrý start, ne audit."),
        ("Jaký je rozdíl mezi SEO auditem a technickým auditem?",
         "Technický audit řeší jen strojovou část: indexace, rychlost, duplicity, struktura. Komplexní SEO audit k tomu přidává obsah, klíčová slova, konkurenci a plán. Pokud web neindexuje nebo se propadl, stačí vám technický. Pokud stagnuje, potřebujete komplexní."),
        ("Zaručí audit první pozice v Google?",
         "Ne a nikdo seriózní to nezaručí. Audit zaručí, že budete přesně vědět, co brzdí váš web a co opravit jako první. To je nejlepší základ pro výsledky, ale výsledky závisí i na konkurenci a rozpočtu."),
        ("Co potřebujete ode mě pro audit?",
         "Přístup do Google Search Console (stačí přidělit oprávnění), adresu webu a pokud máte, přístup do GA4. Vstupní audit zvládnu i bez přístupů, jen z veřejných dat a crawlu."),
        ("Co když audit najde hodně chyb?",
         "To je normální, každý web má desítky menších chyb. Podstatné je pořadí: 20 % oprav přináší 80 % výsledků. Přesně proto má audit priority P1 až P3 a u každé položky dopad i odhad hodin."),
    ]
    return blog_post(slug="seo-audit-co-to-je", label="SEO audit", h1="SEO audit: co to je, kolik stojí a jak probíhá",
                     answer="SEO audit je systematická kontrola webu, která odpovídá na tři otázky: proč web neuspěje v Google, co opravit a v jakém pořadí. Vstupní audit je zdarma do 3 dnů, technický od 180 EUR, komplexní 240 až 480 EUR.",
                     sections=sections, faq=faq,
                     related=[("seo-pro-eshop", "SEO pro e-shop: 9 nastavení, která přinášejí objednávky")],
                     services=[("/cz/sluzby/seo-audit/", "SEO audit a analýza"), ("/cz/sluzby/seo-optimalizace/", "SEO optimalizace webu")])


# ---------------------------------------------------------------- LISTING

_BLOG_CARDS = [
    dict(slug="seo-pro-eshop", cat="E-shop", tag="tag-cerulean", date="1. 10. 2026",
         title="SEO pro e-shop: 9 nastavení, která přinášejí objednávky",
         excerpt="Kategorie, produkty, filtry, schéma, Merchant Center, prolinkování, rychlost a měření objednávek. Co skutečně rozhoduje o objednávkách z Google."),
    dict(slug="seo-audit-co-to-je", cat="SEO audit", tag="tag-violet", date="1. 10. 2026",
         title="SEO audit: co to je, kolik stojí a jak probíhá",
         excerpt="Vstupní, technický a komplexní audit: rozdíly, ceny (od 180 EUR, vstupní zdarma), 5 kroků a jak číst priority P1 až P3."),
]


def _blog_card(c: dict, featured: bool = False) -> str:
    href = f"/cz/blog/{c['slug']}/"
    return f"""
<a href="{href}" class="blog-card{' blog-featured' if featured else ''}">
  <div><span class="project-tag {c['tag']}">{c['cat']}</span></div>
  <h3>{c['title']}</h3>
  <p>{c['excerpt']}</p>
  <div class="blog-card-foot"><span class="blog-date">{c.get('date', '')}</span><span class="blog-read">Číst článek →</span></div>
</a>"""


def latest_cards(n: int = 2) -> str:
    """Latest CZ blog cards, used by the CZ homepage teaser."""
    return "".join(_blog_card(c) for c in _BLOG_CARDS[:n])


def cz_blog() -> tuple[str, str]:
    featured = _BLOG_CARDS[0]
    cards = "".join(_blog_card(c) for c in _BLOG_CARDS[1:])
    body = f"""
{page_hero("Blog", "Praktické články o SEO a AI",
           "Návody, ceny a kontrolní seznamy z praxe. Každý článek vychází z dotazů, které zákazníci reálně hledají. Nové články vycházejí každý týden.", [("Domů", "/cz/"), ("Blog", None)])}
<section class="section">
  <div class="container">
    <div class="blog-grid">{_blog_card(featured, featured=True)}{cards}</div>
    <p style="text-align:center; margin-top:32px; color:var(--text-muted);">Další články vycházejí každý týden: lokální SEO, firemní profil Google, AI vyhledávání, Shoptet a další.</p>
    <div style="text-align:center; margin-top:18px;">
      <a href="/cz/kontakt/?audit=1" class="btn btn-primary">Audit webu zdarma</a>
    </div>
  </div>
</section>
"""
    html = base(market="cz", path="blog/", title="Blog o SEO, Mapách Google a AI vyhledávačích | Nokto Studio",
                desc="Praktické články: SEO pro e-shop, SEO audit s cenami a postupem. Nové návody každý týden. Nokto Studio.",
                canonical=BASE + "/cz/blog/", body=body, prefix="../..", extra_head=ORG_SCHEMA_CZ)
    return ("cz/blog/index.html", html)
