# -*- coding: utf-8 -*-
"""Nokto Studio - EN core pages (secondary market; projects stay as legacy pages)."""
from engine import (base, page_hero, cta_band, faq_block, faq_schema,
                    steps_block, benefit_cards, price_cards, results_slider, result_block,
                    partner_logo_card, ORG_SCHEMA, EMAIL, BASE, gicon, PHONE_TEL, PHONE_DISPLAY,
                    _bars, _sparkline, _VIOLET_L, _VIOLET, _ORANGE, _CERULEAN)

EN_FAQ = [
    ("How much does SEO cost?",
     "You pay 12 EUR per hour of work. A small business website typically needs 10 hours per month (120 EUR), an e-shop 15 hours (180 EUR). Larger scopes use the 220 EUR growth retainer (about 18 hours) or the 290 EUR authority retainer (about 24 hours). The exact scope is confirmed in the plan after a free audit."),
    ("How long until SEO brings results?",
     "Initial movements on less competitive keywords usually appear within 2 to 4 months. Main competitive queries take 6 to 12 months. Realistic timelines are shared in the audit."),
    ("Do you guarantee first positions in Google?",
     "No, and no serious agency can. We guarantee a transparent process, realistic timelines and measurable progress reported every month."),
    ("Can you get my business recommended by ChatGPT?",
     "Yes, that is our specialty. We optimize your site so ChatGPT, Gemini, and Google AI Overviews understand and cite it when customers ask for recommendations."),
    ("Are the contracts binding for 12 months?",
     "No. Work runs month to month and you can stop any time. We invoice for actual hours worked."),
]

EN_FAQ_SECTIONS = [
    ("General", [
        ("What exactly does Nokto Studio do?",
         "Website SEO, local SEO and Google Business Profile, AI search optimization (ChatGPT, Gemini, AI Overviews), e-commerce SEO, SEO audits, link building, web development and Google Ads PPC. Plus e-mail marketing for e-shops and companies."),
        ("Which companies do you work with?",
         "Mostly small and mid-sized companies: local services (trades, healthcare, law, car service), e-shops and companies offering professional services. I work in the Slovak, Czech and wider European markets."),
        ("Which platforms do you work with?",
         "WordPress, Shoptet, WooCommerce and custom solutions. In SEO the tool is secondary, the strategy and its execution matter."),
    ]),
    ("Pricing and contracts", [
        ("How much does SEO cost?",
         "12 EUR per hour worked. A small company website usually takes 10 hours per month (120 EUR), an e-shop 10 to 15 hours (120 to 180 EUR). Larger scopes use the 220 EUR retainer (about 18 hours) or 290 EUR (about 24 hours). Packages are recommended scopes, not mandatory fees."),
        ("Are the contracts binding?",
         "No. You can stop the cooperation at any time, without penalties. I invoice monthly for hours actually worked."),
        ("What if I need more hours in one month?",
         "Nothing changes, we simply move to a higher number of hours. The scope is agreed in the plan and you can change it at any time."),
        ("Is ad spend included in the price?",
         "No. Ads (Google Ads) are paid directly to Google. I manage campaigns for 12 EUR per hour. Link and PR costs are billed at cost."),
    ]),
    ("Process and results", [
        ("How long until SEO brings results?",
         "First movements on less competitive queries appear in 2 to 4 months, main queries take 6 to 12 months. Local SEO and the Google profile often improve within 4 to 8 weeks. Exact timelines are in the audit."),
        ("How will I see that the work was done?",
         "A monthly report in person: a 30-minute call with me. Hours worked, positions, clicks from Search Console, orders from Analytics, Maps visibility and AI mentions."),
        ("Do you offer guarantees of the first position?",
         "No. Nobody can honestly guarantee the first position in Google. Anyone promising it is selling fiction. I guarantee the process, transparency and measurable progress that leads to positions."),
        ("Can you help with a website migration?",
         "Yes, a migration is one of the tasks where positions are easily lost. I know what to do to prevent that."),
    ]),
    ("AI and new search", [
        ("Will ChatGPT replace Google?",
         "It will complement it, not destroy it. Customers search in both today. My work covers both: classic Google positions and visibility in AI answers."),
        ("How do I know whether AI recommends me?",
         "I regularly test sets of queries your customers use and record whether your name appears in the answers of ChatGPT, Gemini and Google AI Overviews. It is part of the monthly report."),
        ("Why is this specialization rare?",
         "AI optimization is new expert work that requires a different content and data-structure method. Most agencies are not preparing for it yet, which is an advantage for clients who start first."),
    ]),
]


EN_TRUST = """
<div class="trust-strip">
  <div class="container">
    <div class="trust-grid">
      <div class="trust-stat reveal" data-delay="100">
        <span class="trust-num tn-violet">12&nbsp;EUR</span>
        <span class="trust-label">transparent hourly<br>rate, no hidden fees</span>
      </div>
      <div class="trust-stat reveal" data-delay="200">
        <span class="trust-num tn-orange">0 EUR</span>
        <span class="trust-label">first call and website<br>audit are free</span>
      </div>
      <div class="trust-stat reveal" data-delay="300">
        <span class="trust-num tn-cerulean">1 day</span>
        <span class="trust-label">free audit starts<br>right after the first call</span>
      </div>
      <div class="trust-stat reveal" data-delay="400">
        <span class="trust-num tn-violet-light">30 min</span>
        <span class="trust-label">monthly report<br>as a call with me</span>
      </div>
    </div>
  </div>
</div>
"""

EN_LOGOS = """
<section class="logo-strip-section">
  <p class="logo-strip-heading">Brands I have worked with</p>
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

EN_PILLARS = [
    ("/en/services/#ai", "AI visibility",
     "ChatGPT, Gemini and Google AI Overviews recommend you to customers as the first choice.", "ai", "#9B6FD9"),
    ("/en/services/#seo", "Google visibility",
     "Positions in Google that bring customers, not just traffic.", "search", "#6A3FC4"),
    ("/en/services/#local", "Google Maps visibility",
     "Business Profile, Maps and reviews. Nearby customers find you first.", "pin", "#F75940"),
]
EN_SUPPORT = [
    ("/en/services/#eshop", "E-commerce SEO",
     "More sales from categories and products (Shoptet, marketplaces, Google Shopping).", "shop", "#1DACD6"),
    ("/en/services/#wordpress", "WordPress SEO",
     "Speed, plugins, schema and structure. A WordPress site Google ranks higher.", "code", "#6A3FC4"),
    ("/en/services/#audit", "SEO audit and analysis",
     "A precise picture of what holds your site back, with a prioritized plan.", "audit", "#6A3FC4"),
    ("/en/services/#links", "Link building",
     "Backlinks and authority, without which reaching the top is out of reach.", "link", "#F75940"),
]
EN_PARTNERS = [
    ("https://flamia.studio", "flamia.png", "Web design: Flamia Studio",
     "A custom website that gets found and sells. Design and development by our partner Flamia Studio."),
    ("https://peterkocur.sk", "peterkocur.png", "PPC advertising: Peter Kocur",
     "Google Ads for results now, while SEO gains momentum. Run by my partner Peter Kocur."),
]


def _en_card(href, title, text, icon, color, tag, delay, external=False):
    ext = ' target="_blank" rel="noopener noreferrer"' if external else ""
    return f"""
<div class="benefit-card card-hover reveal" data-delay="{delay}">
  <span class="benefit-icon">{gicon(icon, color, 26)}</span>
  <h3><a href="{href}"{ext} style="color:var(--text);">{title}</a></h3>
  <p>{text}</p>
  <div class="project-tags"><span class="project-tag {tag}">{'Partner' if external else 'Service'}</span></div>
</div>"""


def en_services_grid(cols: int = 3) -> str:
    pillars = "".join(_en_card(*s, ["tag-violet-light", "tag-violet", "tag-orange"][i], (i + 1) * 100)
                      for i, s in enumerate(EN_PILLARS))
    support = "".join(_en_card(*s, ["tag-cerulean", "tag-violet", "tag-orange", "tag-violet-light"][i], (i + 1) * 100)
                      for i, s in enumerate(EN_SUPPORT))
    partners = "".join(partner_logo_card(href, logo, title, text, (i + 1) * 100)
                       for i, (href, logo, title, text) in enumerate(EN_PARTNERS))
    return (f'<div class="grid-3">{pillars}</div>'
            f'<h3 style="margin:42px 0 22px;">Plus supporting services</h3>'
            f'<div class="grid-4">{support}</div>'
            f'<h3 style="margin:42px 0 22px;">Add-on services from partners</h3>'
            f'<p style="max-width:720px; margin:0 0 20px; color:var(--text-muted);">I do not build websites or run PPC myself. I offer them together with proven partners I work with on the same project.</p>'
            f'<div class="partner-band">{partners}</div>')


def en_home() -> tuple[str, str]:
    h1 = ('Let customers find you in <span class="hl-violet">Google</span>, '
          'on <span class="hl-orange">Google Maps</span> and in <span class="hl-cerulean-light">ChatGPT</span>.')
    body = f"""
<section class="hero">
  <div class="container">
    <div class="hero-flex">
      <div class="hero-content">
        <span class="hero-label">SEO agency for business owners · Europe</span>
        <h1>{h1}</h1>
        <p class="hero-sub">Nokto Studio is an SEO agency for business owners. We help clients grow in Google and AI search by writing content and fixing technical issues on the website, so customers find you when they search for your products and services. At a transparent 12 EUR per hour. Retainers from 120 EUR, no lock-in contracts.</p>
        <div class="hero-ctas">
          <a href="/en/contact/?audit=1" class="btn btn-primary btn-lg">Free website audit</a>
          <a href="/en/services/" class="btn btn-outline btn-lg">Services and pricing</a>
        </div>
        <p class="hero-scarcity">I deliver the audit to your e-mail within 1 to 2 business days. All I need is your website address.</p>
      </div>
      <div class="hero-photo">
        <img src="/assets/img/simon.png" alt="Šimon Štermenský, SEO specialist and founder of Nokto Studio" width="220" height="220" loading="eager">
        <span class="hero-photo-cap">Šimon Štermenský<br>SEO specialist · Nokto Studio</span>
      </div>
    </div>
  </div>
</section>

{EN_TRUST}
{EN_LOGOS}

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-label">What business owners ask us for</span>
      <h2>Four goals, one system</h2>
      <p class="section-subheading">Every client picks one or more goals. I build a system that serves them together.</p>
    </div>
    <div class="grid-4">
      <div class="benefit-card card-hover reveal" data-delay="100">
        <span class="benefit-icon icon-violet-light">{gicon("ai", "#9B6FD9", 26)}</span>
        <h3>Get recommended by AI</h3>
        <p>When a customer asks ChatGPT for a recommendation, you want to be in the answer. We build sites that AI tools understand and cite.</p>
      </div>
      <div class="benefit-card card-hover reveal" data-delay="200">
        <span class="benefit-icon icon-orange">{gicon("pin", "#F75940", 26)}</span>
        <h3>Customers from Google and Maps</h3>
        <p>Local search and your Google Business Profile are the fastest path to nearby customers. We set them up and review them weekly.</p>
      </div>
      <div class="benefit-card card-hover reveal" data-delay="300">
        <span class="benefit-icon icon-cerulean">{gicon("shop", "#1DACD6", 26)}</span>
        <h3>More e-shop sales</h3>
        <p>Categories and products optimized for keywords that convert. Google Shopping and marketplaces tracked as part of the system.</p>
      </div>
      <div class="benefit-card card-hover reveal" data-delay="400">
        <span class="benefit-icon icon-violet">{gicon("grow", "#6A3FC4", 26)}</span>
        <h3>More enquiries for services</h3>
        <p>Service pages that answer real customer questions turn interest into enquiries and bookings.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Services</span>
      <h2>Three visibility pillars I am best at</h2>
      <p class="section-subheading">AI visibility, Google visibility and Google Maps visibility. Plus supporting services and add-ons from proven partners.</p>
    </div>
    {en_services_grid(3)}
    <div style="text-align:center; margin-top:36px;">
      <a href="/en/services/" class="btn btn-outline">All services and hourly pricing</a>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">How we work</span>
      <h2>Four steps. No lock-in contracts.</h2>
      <p class="section-subheading">You always know what I am doing, why and what it brought. Every hour is reported.</p>
    </div>
    {steps_block([
        {"title": "Free audit", "text": "It starts with a 30-minute call and a free audit of your site. You see exactly what holds back your positions, sales and AI recommendations."},
        {"title": "A plan with numbers", "text": "The audit becomes a plan: which keywords bring customers, what to fix first, how many hours per month it takes, and what results are realistic."},
        {"title": "Weekly work", "text": "We do the work: technical fixes, content, Google profile, AI visibility, links. You always know what happened last week."},
        {"title": "Measure and report", "text": "Your monthly report is personal: a 30-minute call with me. Positions, clicks, orders and AI mentions. You pay only for hours worked."},
    ])}
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Pricing</span>
      <h2>12 EUR per hour. You pay for work, not a retainer fee.</h2>
      <p class="section-subheading">Retainers from 120 to 290 EUR depending on the scope. Every hour is reported.</p>
    </div>
    <div class="rate-band">
      <div>
        <div class="rate-big">12 EUR <small>per hour of work</small></div>
        <p style="margin-top:8px; max-width:520px;">Packages are recommended monthly retainers, not mandatory fees. Change them any time, no penalties.</p>
      </div>
      <a href="/en/pricing/" class="btn btn-primary btn-lg">See the full pricing</a>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Case study</span>
      <h2>Villa Paris: brand, website and local SEO from scratch</h2>
      <p class="section-subheading">Premium accommodation in Piestany with one goal: more direct bookings without portal commissions.</p>
    </div>
    <div class="grid-2">
      <div class="project-card card-hover">
        <div class="project-card-body">
          <h3>School supplies e-shop (client)</h3>
          <p>A custom e-shop with an API integration to the accounting system for a regional supplier. Over 9 months I generated online revenue credited to the e-mail and organic Google channels. The scope includes e-mail marketing, local SEO and AI search optimization, so ChatGPT and Google AI Overviews recommend the brand.</p>
          <div class="case-result">
            <div><strong>2,492.75 EUR</strong><span>revenue over 9 months</span></div>
            <div><strong>15</strong><span>orders from e-mail and organic search</span></div>
            <div><strong>722 EUR</strong><span>largest order</span></div>
          </div>
          <div class="project-tags">
            <span class="project-tag tag-cerulean">E-commerce SEO</span>
            <span class="project-tag tag-violet-light">E-mail marketing</span>
            <span class="project-tag tag-orange">Local SEO + GEO</span>
          </div>
          <a href="/en/contact/" class="btn btn-outline">Ask me about it</a>
        </div>
      </div>
      <div class="project-card card-hover">
        <div class="project-card-body">
          <h3>Villa Paris, Piestany</h3>
          <p>Rebrand, new website, hospitality copywriting and local SEO in one system. The goal: a guest understands the value of the stay before comparing competitors and books directly.</p>
          <div class="case-result">
            <div><strong>Rebrand</strong><span>identity + logo</span></div>
            <div><strong>Website</strong><span>new structure</span></div>
            <div><strong>Local SEO</strong><span>Google profile</span></div>
          </div>
          <div class="project-tags">
            <span class="project-tag tag-violet">Branding</span>
            <span class="project-tag tag-violet-light">Web design</span>
            <span class="project-tag tag-cerulean">Copywriting</span>
            <span class="project-tag tag-orange">Local SEO</span>
          </div>
          <a href="/en/villa-paris/" class="btn btn-outline">Read the full story</a>
        </div>
      </div>
    </div>
    <div style="text-align:center; margin-top:32px;">
      <a href="/en/portfolio/" class="btn btn-outline">All results</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head"><span class="section-label">FAQ</span><h2>Most asked questions</h2></div>
    {faq_block(EN_FAQ)}
    <div style="text-align:center; margin-top:28px;">
      <a href="/en/faq/" class="btn btn-outline">All frequently asked questions</a>
    </div>
  </div>
</section>

<section class="section section-alt" id="about">
  <div class="container">
    <div class="about-simon">
      <div class="about-simon-photo reveal">
        <img src="/assets/img/simon.png" alt="Šimon Štermenský, SEO specialist and founder of Nokto Studio" width="300" height="300" loading="lazy">
      </div>
      <div class="reveal" data-delay="150">
        <span class="section-label">Who stands behind Nokto</span>
        <h2 style="margin:10px 0 14px;">You talk to me, not an account manager.</h2>
        <p style="color:var(--text-muted);">I am Simon, an SEO specialist. Over years in online marketing I have grown most fond of SEO and visibility in Google and AI tools, because I see how it really changes the sales of small companies. I work with a small team and with partners on web design and PPC, so the person who does the work is the one who answers you.</p>
        <p style="color:var(--text-muted);">Your first hour with me is a free call and website audit. If the numbers do not make sense to you, you pay nothing.</p>
        <a href="/en/contact/" class="btn btn-primary" style="margin-top:18px;">Book a call with me</a>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Blog</span>
      <h2>Latest practical guides</h2>
      <p class="section-subheading">New guides every week: e-commerce SEO, audits, WordPress and AI search.</p>
    </div>
    <div class="blog-grid">{en_home_blog_teaser()}</div>
    <div style="text-align:center; margin-top:28px;">
      <a href="/en/blog/" class="btn btn-outline">All articles</a>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    {cta_band("Start with a free audit", "A 30-minute call and a free audit of your website. You learn what holds your site back, even if you decide not to work with us.", "en")}
  </div>
</section>
"""
    html = base(market="en", path="", title="Nokto Studio | SEO agency: Google, Maps and ChatGPT visibility",
                desc="SEO agency for business owners. Customers from Google and Google Maps, recommendations in ChatGPT and AI tools, more e-shop sales. 12 EUR per hour, free audit.",
                canonical=BASE + "/en/", body=body, prefix="..",
                extra_head=ORG_SCHEMA + faq_schema(EN_FAQ, BASE + "/en/"))
    return ("en/index.html", html)


def en_home_blog_teaser() -> str:
    """Latest EN blog cards, injected into the homepage (lazy import)."""
    import pages_en2 as en2
    return en2.latest_cards(2)


def en_services() -> tuple[str, str]:
    # Info-rich sections for each service. SK/CZ have dedicated pages; EN hub expands inline.
    linkbuilding_section = """
<section class="section" id="links">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Link building</span>
      <h2>Link building: what it is, what it costs, how I do it safely</h2>
    </div>
    <p style="max-width:720px;">Link building is acquiring hyperlinks from other websites to yours. Google treats each link as a recommendation: the more relevant links from quality domains point to you, the higher you rank. I build links only from real Slovak and Czech domains with actual traffic, never from spam networks. You pay the real price the publication charges, with no markup. My work costs 12 EUR per hour.</p>
    <table class="metric-table" style="margin-top:24px;">
      <tr><th>Domain type</th><th>Price per link (EUR)</th><th>DR (Marketing Miner)</th><th>When it makes sense</th></tr>
      <tr><td><strong>Local directory</strong> (firmy.sk, firmy.cz)</td><td>0 to 30</td><td>20 to 40</td><td>Local SEO, first steps, NAP consistency</td></tr>
      <tr><td><strong>Industry blog</strong></td><td>50 to 120</td><td>30 to 50</td><td>Topical relevance, anchor flexibility</td></tr>
      <tr><td><strong>Regional media</strong></td><td>150 to 300</td><td>40 to 60</td><td>Local authority, media SERP citations</td></tr>
      <tr><td><strong>National media</strong> (SME, iDnes, Dennik N)</td><td>400 to 800</td><td>60+</td><td>Flagship link, strong push on main queries</td></tr>
      <tr><td><strong>Guest post on authority site</strong></td><td>80 to 200</td><td>35 to 55</td><td>Expert content, long-term authority</td></tr>
    </table>
    <p style="margin-top:16px; max-width:720px; color:var(--text-2);">Typical scope: 2 to 4 links per month for a small business site, 5 to 10 for an e-shop in a competitive niche. More is not always better: 10 links from real domains with traffic beat 100 from empty catalogs. I avoid PBNs, automated tools, comment spam, and links from directories with no traffic. Google has algorithmically detected these since 2012 (Penguin) and the 2024 spam updates reinforced it.</p>
  </div>
</section>"""

    eshop_section = """
<section class="section section-alt" id="eshop">
  <div class="container">
    <div class="section-head">
      <span class="section-label">E-commerce SEO</span>
      <h2>SEO for e-shops: more orders from Google, not just traffic</h2>
    </div>
    <p style="max-width:720px;">E-commerce SEO is optimizing categories, products, and technical structure so the customer searching for a specific product finds you in Google, not your competitor. I measure orders and revenue from the organic channel, not traffic. For Shoptet, WooCommerce, and custom platforms. My work costs 12 EUR per hour, typically 10 to 15 hours per month for a small to mid-size e-shop.</p>
    <table class="metric-table" style="margin-top:24px;">
      <tr><th>Aspect</th><th>Shoptet</th><th>WooCommerce</th><th>Custom platform</th></tr>
      <tr><td><strong>Duplicate filter URLs</strong></td><td>Common, needs canonical</td><td>Plugin-dependent, often missing</td><td>Implementation-dependent</td></tr>
      <tr><td><strong>H1 on categories</strong></td><td>Template, via SEO module</td><td>Theme, can be overridden</td><td>Must code, often missing</td></tr>
      <tr><td><strong>Core Web Vitals</strong></td><td>Medium, images slow LCP</td><td>Plugin-dependent, often slow</td><td>Developer-dependent</td></tr>
      <tr><td><strong>Product schema JSON-LD</strong></td><td>Automatic, attributes missing</td><td>Via Yoast or RankMath</td><td>Must code JSON-LD</td></tr>
      <tr><td><strong>Merchant Center feed</strong></td><td>Auto-feed via add-on</td><td>WC Product Feed plugin</td><td>Custom feed generator</td></tr>
    </table>
    <p style="margin-top:16px; max-width:720px; color:var(--text-2);">Real result: Mikramt.sk, a small e-shop on a custom platform, after 9 months of SEO work: 15 orders from organic and email channels, 2492.75 EUR revenue, largest single order 722 EUR. Work included category texts (previously empty), structured data fixes, Google Merchant Center integration, and email sequences. Most e-shops need 6 to 18 months to see full organic potential, depending on competition and existing authority.</p>
  </div>
</section>"""

    wordpress_section = """
<section class="section" id="wordpress">
  <div class="container">
    <div class="section-head">
      <span class="section-label">WordPress SEO</span>
      <h2>WordPress SEO: from a slow blog to a lead machine</h2>
    </div>
    <p style="max-width:720px;">WordPress is SEO-ready, but only when it is set up. I fix speed (LCP under 2.5s), configure one SEO plugin (Rank Math or Yoast, never both), fix the structure (permalinks, sitemap, canonicals), add schema (Organization, Article, Product for WooCommerce), and wire internal links so every page passes equity. Typical setup is 6 to 10 hours (72 to 120 EUR at 12 EUR per hour), then 2 to 4 hours per month for content and maintenance.</p>
    <table class="metric-table" style="margin-top:24px;">
      <tr><th>Area</th><th>Common WordPress problem</th><th>Fix</th></tr>
      <tr><td><strong>Speed</strong></td><td>No cache, unoptimized images, slow LCP</td><td>Cache plugin, WebP, lazy loading</td></tr>
      <tr><td><strong>SEO plugin</strong></td><td>Yoast and Rank Math installed together</td><td>Keep one, remove the other, set meta templates</td></tr>
      <tr><td><strong>Structure</strong></td><td>/?p=123 URLs, missing sitemap, duplicates</td><td>Permalinks, sitemap, canonicals</td></tr>
      <tr><td><strong>Schema</strong></td><td>No structured data at all</td><td>Organization, Article, Product, LocalBusiness</td></tr>
      <tr><td><strong>Internal links</strong></td><td>Orphan posts, no links to services</td><td>At least 3 internal links per page</td></tr>
    </table>
    <p style="margin-top:16px; max-width:720px; color:var(--text-2);">For WooCommerce stores I treat the shop as an e-commerce project: product schema, category copy and a Google Merchant Center feed (see E-commerce SEO above).</p>
  </div>
</section>"""

    audit_section = """
<section class="section section-alt" id="audit">
  <div class="container">
    <div class="section-head">
      <span class="section-label">SEO audit</span>
      <h2>SEO audit: 40 specific points, not a PDF for the drawer</h2>
    </div>
    <p style="max-width:720px;">An SEO audit is a systematic evaluation that answers three questions: why you are not succeeding in Google, what exactly needs fixing, and in what order. I start with a free initial audit delivered within 3 business days: the 10 biggest problems and opportunities on one page. A detailed audit is an action plan with hours and priorities, not a 60-page PDF. My work costs 12 EUR per hour; a detailed audit is included in the first month retainer (120 to 180 EUR).</p>
    <div class="grid-2" style="align-items:start; margin-top:24px;">
      <div class="card">
        <span class="section-label">Technical (15 points)</span>
        <ul class="deliv-list">
          <li><span class="check">✓</span><span>Indexation: how many pages are in Google, how many are "Crawled, currently not indexed"</span></li>
          <li><span class="check">✓</span><span>Sitemap.xml: complete, current, no errors</span></li>
          <li><span class="check">✓</span><span>Robots.txt: blocks only what it should</span></li>
          <li><span class="check">✓</span><span>Canonicalization: correct on every page, no duplicate URLs</span></li>
          <li><span class="check">✓</span><span>Core Web Vitals: LCP under 2.5s, INP under 200ms, CLS under 0.1</span></li>
          <li><span class="check">✓</span><span>HTTPS: valid cert, no mixed content</span></li>
          <li><span class="check">✓</span><span>Structured data: Organization, WebSite, BreadcrumbList, Article/Product</span></li>
          <li><span class="check">✓</span><span>Hreflang: correct pairs and x-default if multilingual</span></li>
          <li><span class="check">✓</span><span>Internal linking: no orphan pages, strong pages pass equity</span></li>
        </ul>
      </div>
      <div class="card">
        <span class="section-label">Content and keywords (15 points)</span>
        <ul class="deliv-list">
          <li><span class="check">✓</span><span>Title and meta description on every page, keyword and CTR-optimized</span></li>
          <li><span class="check">✓</span><span>H1 unique on every page, with main keyword</span></li>
          <li><span class="check">✓</span><span>Alt text on images, descriptive not stuffed</span></li>
          <li><span class="check">✓</span><span>Thin content: pages under 300 words without real value</span></li>
          <li><span class="check">✓</span><span>Duplications: same text on multiple URLs</span></li>
          <li><span class="check">✓</span><span>Cannibalization: two pages competing for one keyword</span></li>
          <li><span class="check">✓</span><span>E-E-A-T signals: author, date, sources, sameAs, experience</span></li>
          <li><span class="check">✓</span><span>Keyword list with search volumes from Marketing Miner</span></li>
          <li><span class="check">✓</span><span>SERP analysis: what Google actually shows for main queries</span></li>
          <li><span class="check">✓</span><span>Competitor analysis: top 3, content gap, link gap</span></li>
        </ul>
      </div>
    </div>
    <p style="margin-top:16px; max-width:720px; color:var(--text-2);">Real result: a 300-page website where adding just 6 targeted content pages on real customer queries lifted monthly impressions by 11 000 (+14 percent) and clicks by 43 percent in the last week. This is what a good audit finds first: not 50 things to do, but the 6 that actually move the needle.</p>
  </div>
</section>"""

    body = f"""
{page_hero("Services", "Services that bring you customers",
           "From technical SEO to AI visibility. Every service costs 12 EUR per hour; scope is agreed upon in the plan.",
           [("Home", "/en/"), ("Services", None)])}
<section class="section"><div class="container">{en_services_grid(3)}</div></section>
    <section class="section section-alt" id="ai">
      <div class="container">
        <div class="section-head">
          <span class="section-label">AI visibility</span>
          <h2>AI visibility: get recommended by ChatGPT and Gemini</h2>
        </div>
        <p style="max-width:720px;">AI visibility means your company appears in answers from ChatGPT, Gemini, Perplexity and Google AI Overviews when a customer asks for a recommendation. I structure content so language models understand who you are, what you do and where you operate, and so they cite you. The work covers entity data, direct answers, structured data, consistent brand mentions and content that answers real buying questions. Typically 4 to 8 hours per month at 12 EUR per hour.</p>
      </div>
    </section>

    <section class="section" id="seo">
      <div class="container">
        <div class="section-head">
          <span class="section-label">Google visibility</span>
          <h2>Google visibility: customers, not vanity traffic</h2>
        </div>
        <p style="max-width:720px;">Google visibility means ranking for the queries your customers actually use. I start from Search Console and keyword research, fix technical blockers and write pages that answer the query better than the current top results. Typical scope is 10 to 15 hours per month depending on competition, at 12 EUR per hour. Every hour is reported with its result.</p>
      </div>
    </section>

    <section class="section section-alt" id="local">
      <div class="container">
        <div class="section-head">
          <span class="section-label">Google Maps visibility</span>
          <h2>Google Maps visibility: the local pack</h2>
        </div>
        <p style="max-width:720px;">Google Maps visibility is the local pack: your Business Profile, categories, services, photos, reviews, NAP consistency and local pages. For local services this is often the fastest channel to new customers. Setup takes about 8 hours, then 4 hours per month at 12 EUR per hour.</p>
      </div>
    </section>

    {linkbuilding_section}
    {eshop_section}
    {wordpress_section}
    {audit_section}
<section class="section" id="pricing">
  <div class="container">
    <div class="section-head"><span class="section-label">Pricing</span><h2>Simple, transparent pricing</h2></div>
    <div class="rate-band">
      <div>
        <div class="rate-big">12 EUR <small>per hour · stop any time</small></div>
        <p style="margin-top:8px; max-width:520px;">Retainers: 120 EUR for a small site (10 hours), 180 EUR for a mid-size site or e-shop (15 hours), 220 EUR growth (about 18 hours) and 290 EUR authority (about 24 hours). Link costs and ad spend billed separately at cost.</p>
      </div>
      <a href="/en/pricing/" class="btn btn-primary btn-lg">See the full pricing</a>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    {cta_band("Not sure what you need? Start with the audit.", "The free audit tells you where the biggest growth chances are. It becomes the plan.", "en")}
  </div>
</section>
"""
    html = base(market="en", path="services/", title="Services: SEO, Maps, AI visibility, e-shop SEO | Nokto Studio",
                desc="AI visibility, Google visibility, Google Maps visibility, e-commerce SEO, audits, link building, and email marketing. Web design and PPC with our partners. 12 EUR per hour.",
                canonical=BASE + "/en/services/", body=body, prefix="../..", extra_head=ORG_SCHEMA)
    return ("en/services/index.html", html)


EN_PACKAGES = [
    {"name": "Small website", "hours": 10, "price": 120,
     "items": ["Website audit and keyword review", "Technical fixes", "2 content pages or rewrites", "Google Business Profile in order", "Monthly report"],
     "cta": "/en/contact/"},
    {"name": "Mid-size site / e-shop", "hours": 15, "price": 180,
     "items": ["Everything from Small website", "4 to 6 content pages per month", "AI search optimization", "Internal linking and CRO tips", "Link building (2 to 3 links)", "Monthly report and 30-minute call"],
     "cta": "/en/contact/"},
    {"name": "Growth", "hours": 18, "price": 220, "featured": True,
     "badge": "Recommended retainer",
     "items": ["Everything from Mid-size site", "6 to 8 content pages or blog posts per month", "2 competitor analyses per month", "AI visibility: ChatGPT, Gemini and AI Overviews monitoring", "Link building (4 links)", "Monthly report and 30-minute call"],
     "cta": "/en/contact/"},
    {"name": "Authority", "hours": 24, "price": 290,
     "items": ["Everything from Growth", "8 to 12 content pages or blog posts per month", "In-depth analysis and quarterly content plan", "AI visibility: query tracking and recommendations", "Link building (6 links)", "Priority communication and 60-minute call"],
     "cta": "/en/contact/"},
]

EN_PRICING_FAQ = [
    ("How much does SEO cost?",
     "Retainers from 120 to 290 EUR per month depending on the scope. A small business website is 120 EUR (10 hours), a mid-size site or e-shop 180 EUR (15 hours), the growth retainer 220 EUR (about 18 hours) and the authority retainer 290 EUR (about 24 hours). The exact scope is confirmed in the plan after a free audit."),
    ("Why is it cheaper than other agencies?",
     "I have no offices or management layers. A large part of the work is done by automation I built myself, and expert time goes where it counts. The savings go to you."),
    ("What is included in the price?",
     "Everything except ad spend and the cost of links or third-party tools. Those are billed at cost, with no markup."),
    ("Do I pay monthly in advance?",
     "I invoice monthly in arrears for hours actually worked, with an invoice. A retainer is a recommended scope, not a commitment."),
    ("Can I stop the cooperation at any time?",
     "Yes, the monthly cycle can be ended at any time, without penalties or lock-in. Trust is earned through results."),
    ("How do I know the work was done?",
     "Every month you get a list of tasks with hours and their result. You are the one who checks."),
]


def en_pricing() -> tuple[str, str]:
    body = f"""
{page_hero("Pricing", "Pricing: 12 EUR per hour, retainers from 120 EUR",
           "You pay for hours worked. A retainer is a recommended monthly scope you can change or stop at any time.",
           [("Home", "/en/"), ("Pricing", None)])}

<section class="section">
  <div class="container">
    <div class="rate-band">
      <div>
        <div class="rate-big">12 EUR <small>per hour of work</small></div>
        <p style="margin-top:8px; max-width:560px;">SEO, local SEO, AI visibility, content, link building, websites and PPC. One rate, simple maths.</p>
      </div>
      <a href="/en/contact/" class="btn btn-primary btn-lg">Get a quote</a>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Packages</span>
      <h2>Recommended monthly retainers</h2>
      <p class="section-subheading">A retainer is a recommended monthly scope. You can change, pause or stop it at any time, without penalties.</p>
    </div>
    {price_cards(EN_PACKAGES, "en")}
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:start;">
      <div class="prose">
        <h2>What is included</h2>
        <ul class="deliv-list">
          <li><span class="check">✓</span><span>All work: technical SEO, content, Google Business Profile, AI visibility, links, websites, PPC management.</span></li>
          <li><span class="check">✓</span><span>Measurement and reporting: Search Console, Analytics, positions, conversions, AI mentions.</span></li>
          <li><span class="check">✓</span><span>Communication: a monthly 30-minute call with me, unlimited questions in between.</span></li>
        </ul>
        <h2>What is not included</h2>
        <ul class="deliv-list">
          <li><span class="check" style="background:#FDEBE8;color:var(--brand-warm-deep);">×</span><span>Ad spend (Google Ads, Meta Ads). You pay Google directly, not me.</span></li>
          <li><span class="check" style="background:#FDEBE8;color:var(--brand-warm-deep);">×</span><span>Cost of links and PR articles. Billed at the real price of the publication.</span></li>
          <li><span class="check" style="background:#FDEBE8;color:var(--brand-warm-deep);">×</span><span>Paid third-party tools, if needed (for example a payment gateway or hosting).</span></li>
        </ul>
      </div>
      <div class="card">
        <span class="section-label">Example from practice</span>
        <p style="margin-bottom:14px;">A law firm website in a town of 50,000 people:</p>
        <ul class="deliv-list">
          <li><span class="check">✓</span><span><strong>Month 1:</strong> audit + technical fixes + Google profile (12 h = 144 EUR)</span></li>
          <li><span class="check">✓</span><span><strong>Months 2 to 4:</strong> content pages for customer questions (10 h = 120 EUR)</span></li>
          <li><span class="check">✓</span><span><strong>Months 5+:</strong> maintenance, link building, AI visibility (8 h = 96 EUR)</span></li>
        </ul>
        <p style="margin-top:14px; font-size:0.9rem; color:var(--text-muted);">I confirm the real numbers for your website in the free audit.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head"><span class="section-label">Pricing FAQ</span><h2>Frequently asked questions about pricing</h2></div>
    {faq_block(EN_PRICING_FAQ)}
  </div>
</section>

<section class="section">
  <div class="container">
    {cta_band("What would it cost for you?", "A free audit and an hour estimate for your specific website. No commitment, real numbers.", "en")}
  </div>
</section>
"""
    faq_html = faq_schema(EN_PRICING_FAQ, BASE + "/en/pricing/")
    html = base(market="en", path="pricing/", title="Pricing: 12 EUR/hour and retainers from 120 EUR | Nokto Studio",
                desc="Transparent SEO pricing at 12 EUR per hour. Retainers of 120, 180, 220 and 290 EUR per month depending on scope, no lock-in. Free audit.",
                canonical=BASE + "/en/pricing/", body=body, prefix="../..", extra_head=ORG_SCHEMA + faq_html)
    return ("en/pricing/index.html", html)


def en_about() -> tuple[str, str]:
    body = f"""
{page_hero("How we work", "We work in the dark.<br>Results speak in the light.",
           "Nokto Studio is an SEO studio run by one specialist with a network of collaborators. We work for owners who want measurable growth, not marketing theatre.",
           [("Home", "/en/"), ("How we work", None)])}
<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:center;">
      <div class="prose">
        <h2>Who stands behind Nokto</h2>
        <p>My name is Simon and Nokto Studio is my studio. Years of SEO and web work for Slovak and international clients: e-shops, local businesses, media and premium brands. I built automation systems that turn SEO work into exactly what a business needs: customers.</p>
        <p>I am not a big agency, and I do not pretend to be one. The advantage: the same person who designs your strategy does the work with you. No forwarding between departments, no lost context.</p>
        <h2>How we work</h2>
        <p>We combine two worlds: expert SEO work (technical, content, authority, AI visibility) and automation that gets more out of the same effort. That is how we can work at 12 EUR per hour and still focus on results, not on padding hours.</p>
      </div>
      <div>
        <img src="/assets/img/simon.png" alt="Šimon Štermenský, SEO specialist and founder of Nokto Studio" width="300" height="300" loading="lazy" style="border-radius:var(--radius-lg); border:1px solid var(--border-light);">
        <p style="text-align:center; margin-top:12px; font-size:0.85rem; color:var(--text-muted);">Šimon Štermenský, SEO specialist · Nokto Studio</p>
      </div>
    </div>
  </div>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Process</span>
      <h2>From the first call to the monthly call with me</h2>
    </div>
    {steps_block([
        {"title": "1. Free call and audit", "text": "A 30-minute call about your goals. Within 3 days you get a free initial audit: the 10 biggest problems and opportunities on one page."},
        {"title": "2. A plan with numbers", "text": "The audit becomes a plan: which keywords bring customers, what to fix first, how many hours per month it takes and what results are realistic. No unrealistic promises."},
        {"title": "3. Weekly work", "text": "Every week I deliver the agreed scope: technical work, content, Google profile, AI visibility, links. Every change is traceable."},
        {"title": "4. Measurement and report", "text": "A monthly report in person as a 30-minute call: what was done, what it brought (positions, clicks, orders, AI mentions) and what comes next."},
    ])}
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Deliverables</span>
      <h2>What exactly you get every month</h2>
    </div>
    <div class="grid-2" style="align-items:start;">
      <div class="card">
        <span class="section-label">Work</span>
        <ul class="deliv-list">
          <li><span class="check">✓</span><span>Technical website maintenance: speed, indexing, bug fixes.</span></li>
          <li><span class="check">✓</span><span>Content pages written for real customer queries.</span></li>
          <li><span class="check">✓</span><span>Google Business Profile: data, photos, reviews, Q&amp;A.</span></li>
          <li><span class="check">✓</span><span>Optimization for ChatGPT, Gemini and AI Overviews.</span></li>
          <li><span class="check">✓</span><span>Link building as agreed (link costs billed separately).</span></li>
        </ul>
      </div>
      <div class="card">
        <span class="section-label">Measurement</span>
        <ul class="deliv-list">
          <li><span class="check">✓</span><span>Positions on tracked keywords (trend, not just numbers).</span></li>
          <li><span class="check">✓</span><span>Clicks and impressions from Google (Search Console).</span></li>
          <li><span class="check">✓</span><span>Enquiries and orders (Google Analytics).</span></li>
          <li><span class="check">✓</span><span>Google Maps visibility: calls, routes, reviews.</span></li>
          <li><span class="check">✓</span><span>Mentions in AI answers (ChatGPT, Gemini, AI Overviews).</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Measurement</span>
      <h2>How I measure results</h2>
      <p class="section-subheading">Nothing changes by opinion. Every claim in the report has a number and a data source.</p>
    </div>
    <table class="metric-table">
      <tr><th>What I track</th><th>Tool</th><th>What it tells us</th></tr>
      <tr><td><strong>Positions</strong></td><td>Keyword tracking</td><td>Which queries grow and where the site is stuck.</td></tr>
      <tr><td><strong>Clicks from Google</strong></td><td>Search Console</td><td>How many people see us and how many click.</td></tr>
      <tr><td><strong>Enquiries and orders</strong></td><td>Google Analytics 4</td><td>How many visitors became customers.</td></tr>
      <tr><td><strong>Maps visibility</strong></td><td>Google Business Profile</td><td>How many people saw the business, called or asked for directions.</td></tr>
      <tr><td><strong>AI recommendations</strong></td><td>Regular AI tests</td><td>Whether ChatGPT, Gemini and AI Overviews cite you.</td></tr>
      <tr><td><strong>Organic revenue</strong></td><td>Analytics + e-shop</td><td>For e-shops: the direct link between SEO effort and sales.</td></tr>
    </table>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head"><span class="section-label">Values</span><h2>Three rules that always apply</h2></div>
    <div class="grid-3">
      <div class="benefit-card"><span class="benefit-icon">{gicon("shield", "#6A3FC4", 26)}</span><h3>No promises we cannot keep</h3><p>Nobody can guarantee the first position in Google. What we guarantee: a transparent process, realistic timelines and measurable progress.</p></div>
      <div class="benefit-card"><span class="benefit-icon">{gicon("chart", "#F75940", 26)}</span><h3>Monthly report: a 30-minute call with me</h3><p>What we did, what it brought, and what comes next. No forwarding, no account managers.</p></div>
      <div class="benefit-card"><span class="benefit-icon">{gicon("check", "#9B6FD9", 26)}</span><h3>Every hour reported</h3><p>You pay for work delivered. Every hour is in the report with its content and result.</p></div>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0;">
  <div class="container">
    {cta_band("Let's talk for 30 minutes", "A free call about your goals. If we are not a fit, we say so straight.", "en")}
  </div>
</section>
"""
    html = base(market="en", path="about/", title="About: SEO agency Nokto Studio | Simon",
                desc="Nokto Studio: SEO agency for business owners. Who stands behind it, how we work, and why 12 EUR per hour is enough for measurable results.",
                canonical=BASE + "/en/about/", body=body, prefix="../..", extra_head=ORG_SCHEMA)
    return ("en/about/index.html", html)


def en_contact() -> tuple[str, str]:
    body = f"""
{page_hero("Contact", "Free website audit. Delivered in 1 to 2 business days.",
           "Send your website address and e-mail. I will send you a free initial audit: what holds your site back in Google and what SEO could mean. Mobile friendly, no commitment.",
           [("Home", "/en/"), ("Contact", None)])}
<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:start;">
      <div class="card" style="text-align:center; border:2px solid var(--brand-primary);">
        <span class="section-label">Free website audit</span>
        <form class="contact-form-el" style="margin-top:16px;">
          <div class="form-grid">
            <div class="form-field full"><label class="form-label" for="url">Your website address *</label><input class="form-input" id="url" name="url" type="url" placeholder="https://" required></div>
            <div class="form-field full"><label class="form-label" for="email">Your e-mail *</label><input class="form-input" id="email" name="email" type="email" required></div>
          </div>
          <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off" aria-hidden="true">
          <input type="hidden" name="_subject" value="Free website audit request - noktostudio.com">
          <button type="submit" class="btn btn-primary" style="margin-top:14px; width:100%;">Get my free website audit</button>
          <p class="form-note">By submitting you agree to receive the audit by e-mail (see <a href="/en/privacy/">privacy</a>). No spam.</p>
        </form>
        <div class="form-success" style="display:none; margin-top:16px; background:#F5F1FC; color:var(--brand-cool-deep); padding:16px; border-radius:10px;">
          ✓ Thank you! Your audit will arrive within 1 to 2 business days.
        </div>
        <ul class="deliv-list" style="text-align:left; margin-top:20px;">
          <li><span class="check">✓</span><span>Just your website and e-mail, nothing else</span></li>
          <li><span class="check">✓</span><span>Audit arrives within 1 to 2 business days</span></li>
          <li><span class="check">✓</span><span>Mobile friendly, easy to read</span></li>
          <li><span class="check">✓</span><span>Free, no commitment</span></li>
        </ul>
      </div>
      <div class="card" style="text-align:center;">
        <span class="section-label">Or call me directly</span>
        <a href="{PHONE_TEL}" class="btn btn-primary btn-lg contact-phone-btn" style="width:100%; margin-top:14px; font-size:1.25rem;">{PHONE_DISPLAY}</a>
        <p style="margin:14px 0 6px; color:var(--text-muted);">Šimon Štermenský, SEO specialist. I usually pick up right away, otherwise I call back within a few hours.</p>
        <ul class="deliv-list" style="margin-top:20px; text-align:left;">
          <li><span class="check">✓</span><span>Free 30-minute consultation about your site</span></li>
          <li><span class="check">✓</span><span>Real numbers: what SEO could mean for you</span></li>
          <li><span class="check">✓</span><span>No commitment. You decide when, and whether.</span></li>
        </ul>
        <p style="margin-top:22px; border-top:1px solid var(--border-light); padding-top:18px;">Or email: <a href="mailto:{EMAIL}" style="font-weight:700; color:var(--text);">{EMAIL}</a></p>
        <a href="mailto:{EMAIL}" class="btn btn-outline" style="width:100%; margin-top:10px;">Write an e-mail</a>
      </div>
    </div>
  </div>
</section>
"""
    html = base(market="en", path="contact/", title="Free website audit: send your site and e-mail | Nokto Studio",
                desc="Free initial website audit. Send your website address and e-mail, I deliver the audit within 1 to 2 business days. Or call +421 917 316 105.",
                canonical=BASE + "/en/contact/", body=body, prefix="../..", extra_head=ORG_SCHEMA)
    return ("en/contact/index.html", html)


def en_faq() -> tuple[str, str]:
    sections_html = ""
    all_qa = []
    for sec_title, qas in EN_FAQ_SECTIONS:
        qas_html = "".join(
            f'<div class="faq-item"><button class="faq-question" type="button">{q}</button>'
            f'<div class="faq-answer"><p>{a}</p></div></div>' for q, a in qas
        )
        sections_html += f'<h2 style="margin-top:36px;">{sec_title}</h2>{qas_html}'
        all_qa += qas
    body = f"""
{page_hero("FAQ", "Frequently asked questions", "Answers to what clients ask most. If your question is missing, please ask directly.", [("Home", "/en/"), ("FAQ", None)])}
<section class="section">
  <div class="container" style="max-width:800px;">
    {sections_html}
  </div>
</section>
<section class="section" style="padding-top:0;">
  <div class="container">
    {cta_band("Still have a question?", "Write or call. I reply personally within 24 hours, no strings attached.", "en")}
  </div>
</section>
"""
    faq_html = faq_schema(all_qa, BASE + "/en/faq/")
    html = base(market="en", path="faq/", title="FAQ: SEO pricing, process and AI visibility | Nokto Studio",
                desc="FAQ: how much SEO costs, how long it takes, how we measure results, what SEO for AI search means. Nokto Studio.",
                canonical=BASE + "/en/faq/", body=body, prefix="../..", extra_head=ORG_SCHEMA + faq_html)
    return ("en/faq/index.html", html)


def en_portfolio() -> tuple[str, str]:
    """Results: real numbers from GSC exports, AI Mode and client reports."""
    c_klient1 = _bars([38, 42, 61, 115, 145], _VIOLET_L,
                      ["Mar", "Apr", "May", "Jun", "Aug"])
    c_klient2 = _bars([182, 293, 329, 413], _VIOLET_L, ["Jun", "Jul", "Aug", "Sep"])
    c_itc = _sparkline([40, 55, 48, 62, 58, 75, 70, 88, 95, 92, 110, 121], _VIOLET)
    blocks = "".join([
        result_block(
            title="Electrical service company (client)", period="March to September 2026",
            nums=[{"big": "991", "color": _VIOLET, "label": "clicks from Google in 28 days (+6%)"},
                  {"big": "72 873", "color": _ORANGE, "label": "impressions in 28 days (+3%)"},
                  {"big": "96", "color": _VIOLET_L, "label": "citations in AI answers"}],
            chart=c_klient1,
            caption="Two expert articles I wrote are cited by Google in AI answers, recommending the client to customers. A 69-page website: 9,700 to 12,000 impressions per 28 days (+24%). Chart: growth of main pages in percent.",
            source="Google Search Console, last 28 days (to September 2026)",
            partner="", market="en"),
        result_block(
            title="Clothing e-shop (own project)", period="Search Console + AI Mode, June to September 2026",
            nums=[{"big": "893", "color": _VIOLET_L, "label": "impressions in Google AI Mode in 3 months"},
                  {"big": "+80 %", "color": _VIOLET, "label": "August vs June (182 → 329)"},
                  {"big": "413", "color": _ORANGE, "label": "clicks on the main category"}],
            chart=c_klient2,
            caption="Google AI Mode cites the shop daily after deploying my content. Monthly growth: June 182, July 293, August 329. Most cited: homepage and blog articles (174, 167 and 119 citations). Categories get tens of thousands of organic impressions per month. Competitors are not in AI answers yet.",
            source="Google Search Console + Google AI Mode (citation report), June to September 2026",
            partner="own", market="en"),
        result_block(
            title="Real estate app (client)", period="last 28 days",
            nums=[{"big": "121", "color": _VIOLET, "label": "clicks from Google (+49%)"},
                  {"big": "4 390", "color": _ORANGE, "label": "impressions (+43%)"},
                  {"big": "+142 %", "color": _VIOLET_L, "label": "top page growth"}],
            chart=c_itc,
            caption="SEO from scratch: technical SEO and content in the first month of work, and Google started bringing customers right away.",
            source="Google Search Console",
            partner="own", market="en"),
        result_block(
            title="Measurement devices e-shop (client)", period="January to September 2026, rework in progress",
            nums=[{"big": "203", "color": _VIOLET, "label": "clicks from Google since launch"},
                  {"big": "3 266", "color": _ORANGE, "label": "impressions since launch"},
                  {"big": "2", "color": _VIOLET_L, "label": "orders even before project completion"}],
            chart=_sparkline([12, 33, 203, 380, 620, 900], _VIOLET),
            caption="E-shop with energy monitoring products. Orders came in even before the one-time project was finished: the site gets orders from organic search while the rework is still running. Average position 10.0, CTR 6.2 %. After the new version launches, we expect multiplied growth.",
            source="Google Search Console, January to September 2026",
            partner="flamia", market="en"),
        result_block(
            title="Villa Paris, Piestany (SK)", period="rebrand + web + local SEO",
            nums=[],
            chart="",
            caption="Premium accommodation. Rebrand, new website, hospitality copywriting and local SEO in one system. Brand and website delivered in cooperation with Flamia Studio. Goal: more direct bookings without portal commissions.",
            source="project story at /en/villa-paris/",
            partner="flamia", market="en"),
    ])
    body = f"""
{page_hero("Portfolio", "How I helped clients grow in Google and AI search",
           "By writing content and fixing technical issues on the website. Results from Google Search Console and Google AI Mode.",
           [("Home", "/en/"), ("Portfolio", None)])}
<section class="section">
  <div class="container">
    <div class="grid-2">{blocks}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Feedback</span>
      <h2>What continuing cooperation says</h2>
      <p class="section-subheading">The best testimonial is the fact that clients stay. I provide client contacts on request and quote them only with their consent.</p>
    </div>
    <div class="grid-3">
      <div class="benefit-card card-hover">
        <span class="benefit-icon">{gicon("grow", "#9B6FD9", 26)}</span>
        <h3>E-shop: cooperation continues</h3>
        <p>The client was happy with the first e-shop, so we are now doing a rework: more products and better SEO.</p>
      </div>
      <div class="benefit-card card-hover">
        <span class="benefit-icon">{gicon("ai", "#6A3FC4", 26)}</span>
        <h3>Electrical service: monthly cooperation runs</h3>
        <p>991 clicks and 96 citations in AI answers in the last 28 days. The report comes out every month with numbers.</p>
      </div>
      <div class="benefit-card card-hover">
        <span class="benefit-icon">{gicon("pin", "#F75940", 26)}</span>
        <h3>Villa Paris: project runs with Flamia Studio</h3>
        <p>Rebrand, website and local SEO in one system. We do the brand and website together with Flamia Studio.</p>
      </div>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0;">
  <div class="container">
    {cta_band("Your business could be the next story", "Start with a free audit. See what we would solve for you, before the first invoice.", "en")}
  </div>
</section>
"""
    html = base(market="en", path="portfolio/", title="Results: SEO, Maps and AI visibility numbers | Nokto Studio",
                desc="Real results from Google Search Console: 991 clicks and 96 AI citations for an electrical service client, 893 AI Mode impressions for a clothing e-shop, 203 clicks and orders before project completion. Numbers from practice.",
                canonical=BASE + "/en/portfolio/", body=body, prefix="../..", extra_head=ORG_SCHEMA)
    return ("en/portfolio/index.html", html)


ALL = [en_home(), en_services(), en_pricing(), en_about(), en_contact(), en_faq(), en_portfolio()]


def en_villa_paris() -> tuple[str, str]:
    body = f"""
{page_hero("Case study · Branding &amp; Web", "Villa Paris: a brand and website built from scratch",
           "Premium accommodation in Piestany had a great product but no brand. We solved it with identity, website, hospitality copywriting and local SEO as one system.",
           [("Home", "/en/"), ("Portfolio", "/en/portfolio/"), ("Villa Paris", None)])}

<div class="partner-band" style="justify-content:center; padding:0 20px;">
  <span class="project-tag tag-violet"><a href="https://flamia.studio" target="_blank" rel="noopener noreferrer" style="color:inherit;">In cooperation with Flamia Studio</a></span>
  <span class="project-tag tag-violet-light">Web design and development: Flamia Studio</span>
  <span class="project-tag tag-cerulean">SEO, copywriting and local SEO: Nokto Studio</span>
</div>
<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:start;">
      <div class="prose">
        <span class="section-label">Problem</span>
        <h2 style="margin-top:8px;">Great location. Zero presentation.</h2>
        <p>Villa Paris offers real value: a peaceful setting in Piestany, proximity to the spa center and ADELI Medical Center, comfortable rooms, and a family atmosphere. But the visual identity and digital presence communicated none of it.</p>
        <p>Visitors arrived on the website and could not quickly understand what made the property worth booking. The brand looked generic, and the copy did not answer the questions people ask before booking. Reservations were lost before a conversation even started.</p>
        <h2>Solution: one system, four areas</h2>
        <h3>Brand identity redesign</h3>
        <p>A new visual system: logo, color palette, typography. Built to feel warm, premium, and instantly recognizable.</p>
        <h3>Website rebuild</h3>
        <p>A reworked structure focused on clarity and booking conversion from the first scroll. Fast loading, a simple path to reservation, with mobile experience as a priority.</p>
        <h3>Hospitality copywriting</h3>
        <p>Guest-oriented texts that answer real pre-booking questions: location, comfort, and what to expect on arrival.</p>
        <h3>Local SEO</h3>
        <p>Google Business Profile set up properly, local keywords for Piestany and spa stays, so guests searching for exactly this kind of accommodation find Villa Paris.</p>
      </div>
      <div class="card">
        <span class="section-label">Project scope</span>
        <ul class="deliv-list">
          <li><span class="check">✓</span><span>Brand redesign: logo, colors, and typography.</span></li>
          <li><span class="check">✓</span><span>New website: structure, design, speed.</span></li>
          <li><span class="check">✓</span><span>Guest-oriented hospitality copywriting.</span></li>
          <li><span class="check">✓</span><span>Local SEO: Google Business Profile, local queries.</span></li>
          <li><span class="check">✓</span><span>Measurement: bookings and their sources.</span></li>
        </ul>
        <div style="margin-top:22px;">
          <a href="/en/contact/?audit=1" class="btn btn-primary">Free website audit</a>
        </div>
      </div>
    </div>
  </div>
</section>
<section class="section section-alt">
  <div class="container">
    {cta_band("Want a brand and website that sell?", "Free audit and 30 minutes of time. I reply personally within 24 hours.", "en")}
  </div>
</section>
"""
    html = base(market="en", path="villa-paris/", title="Villa Paris Piestany: rebrand, web and local SEO | Nokto Studio",
                desc="Case study: how Nokto Studio built Villa Paris from the ground up. Brand identity, new website, hospitality copywriting, and local SEO for premium accommodation in Piestany.",
                canonical=BASE + "/en/villa-paris/", body=body, prefix="../..", extra_head=ORG_SCHEMA)
    return ("en/villa-paris/index.html", html)


def en_privacy() -> tuple[str, str]:
    body = f"""
{page_hero("Privacy", "Privacy policy",
           "We process only the data we need to reply and work together. No selling data to third parties.",
           [("Home", "/en/"), ("Privacy", None)])}
<section class="section">
  <div class="container prose">
    <h2>Who processes the data</h2>
    <p>The data controller is Nokto Studio (Šimon Štermenský, operator of noktostudio.com). Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    <h2>What data and why</h2>
    <ul>
      <li>Contact form: name, email, website address, and message. Purpose: to answer your inquiry. The form sends a notification to our email.</li>
      <li>Analytics: anonymized visitor data (Google Analytics 4, Microsoft Clarity) to improve the website.</li>
    </ul>
    <h2>How long we keep data</h2>
    <p>Contacts from forms and phone calls are kept for up to 24 months from the last communication, unless collaboration begins.</p>
    <h2>Your rights</h2>
    <p>You have the right to access, correct, delete, and transfer your data. Send requests to <a href="mailto:{EMAIL}">{EMAIL}</a>. You may also file a complaint with your national data protection authority.</p>
    <h2>Cookies</h2>
    <p>The site uses analytics cookies after your consent (cookie banner). Strictly necessary cookies are always on.</p>
  </div>
</section>
"""
    html = base(market="en", path="privacy/", title="Privacy policy | Nokto Studio",
                desc="Privacy policy of noktostudio.com: what data we process, why, and what rights you have.",
                canonical=BASE + "/en/privacy/", body=body, prefix="../..", extra_head=ORG_SCHEMA)
    return ("en/privacy/index.html", html)


def en_terms() -> tuple[str, str]:
    body = f"""
{page_hero("Terms", "Terms of service",
           "Simple terms without legal gymnastics: an hourly rate, monthly invoicing, no lock-in.",
           [("Home", "/en/"), ("Terms", None)])}
<section class="section">
  <div class="container prose">
    <h2>1. Scope</h2>
    <p>These terms govern the collaboration between Nokto Studio ("the provider") and the client for marketing services: SEO optimization, local SEO, AI visibility, link building, email marketing and related consulting. Web design and PPC are delivered with our partners.</p>
    <h2>2. Price and invoicing</h2>
    <p>Services are billed at an hourly rate of 12 EUR for hours worked. Invoicing runs monthly, in arrears, based on the hours report. Ad spend and link or third-party tool costs are passed through at the actual price, without markup.</p>
    <h2>3. Term</h2>
    <p>Collaboration runs month-to-month. Either party can end it at the end of a calendar month, in writing, without penalties.</p>
    <h2>4. Responsibility and results</h2>
    <p>The provider does not guarantee specific positions in search engines or specific traffic volumes. The provider guarantees delivered work, transparent reporting and execution according to the agreed plan. Guarantees of specific positions are not possible and are not offered.</p>
    <h2>5. Content rights</h2>
    <p>Content created for the client within a paid collaboration transfers to the client once the invoice is paid. The provider may show the work in its portfolio by agreement with the client.</p>
    <h2>6. Spam and forbidden practices</h2>
    <p>The provider does not use practices that violate search engine guidelines (buying links from automated spam networks, hidden text, duplicate content). Guideline violations risk penalties, so we avoid them on principle.</p>
  </div>
</section>
"""
    html = base(market="en", path="terms/", title="Terms of service | Nokto Studio",
                desc="Terms of service of Nokto Studio: 12 EUR hourly rate, monthly invoicing, no lock-in, transparent reporting.",
                canonical=BASE + "/en/terms/", body=body, prefix="../..", extra_head=ORG_SCHEMA)
    return ("en/terms/index.html", html)


ALL = ALL + [en_villa_paris(), en_privacy(), en_terms()]
