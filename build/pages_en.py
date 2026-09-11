# -*- coding: utf-8 -*-
"""Nokto Studio - EN core pages (secondary market; projects stay as legacy pages)."""
from engine import (base, page_hero, cta_band, faq_block, faq_schema,
                    steps_block, benefit_cards, results_slider, result_block,
                    ORG_SCHEMA, EMAIL, BASE, gicon, PHONE_TEL, PHONE_DISPLAY,
                    _bars, _sparkline, _VIOLET_L, _VIOLET, _ORANGE, _CERULEAN)

EN_FAQ = [
    ("How much does SEO cost?",
     "You pay 12 EUR per hour of work. A small business website typically needs 10 hours per month (120 EUR), an e-shop 20 to 40 hours (240 to 480 EUR). The exact scope is confirmed in the plan after a free audit."),
    ("How long until SEO brings results?",
     "Initial movements on less competitive keywords usually appear within 2 to 4 months. Main competitive queries take 6 to 12 months. Realistic timelines are shared in the audit."),
    ("Do you guarantee first positions in Google?",
     "No, and no serious agency can. We guarantee a transparent process, realistic timelines and measurable progress reported every month."),
    ("Can you get my business recommended by ChatGPT?",
     "Yes, that is our specialty. We optimize your site so ChatGPT, Gemini, and Google AI Overviews understand and cite it when customers ask for recommendations."),
    ("Are the contracts binding for 12 months?",
     "No. Work runs month to month and you can stop any time. We invoice for actual hours worked."),
]


def en_home() -> tuple[str, str]:
    h1 = ('Let customers find you in <span class="hl-violet">Google</span>, '
          'on <span class="hl-orange">Google Maps</span> and in <span class="hl-cerulean-light">ChatGPT</span>.')
    body = f"""
<section class="hero">
  <div class="container">
    <div class="hero-content">
      <span class="hero-label">SEO agency for business owners · Europe</span>
      <h1>{h1}</h1>
      <p class="hero-sub">Nokto Studio is an SEO agency for business owners. We help clients grow in Google and AI search by writing content and fixing technical issues on the website, so customers find you when they search for your products and services. At a transparent 12 EUR per hour. No retainers you cannot see through, no lock-in contracts.</p>
      <div class="hero-ctas">
        <a href="{PHONE_TEL}" class="btn btn-primary btn-lg">Call {PHONE_DISPLAY}</a>
        <a href="/en/contact/?audit=1" class="btn btn-outline btn-lg">Get a free audit</a>
      </div>
      <p class="hero-scarcity">Capacity for new projects: open from October 2026.</p>
    </div>
    <div class="hero-photo">
      <img src="/assets/img/simon.png" alt="Šimon Štermenský, SEO specialist and founder of Nokto Studio" width="220" height="220" loading="eager">
      <span class="hero-photo-cap">Šimon Štermenský<br>SEO specialist · Nokto Studio</span>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-label">What business owners ask us for</span>
      <h2>Four goals, one system</h2>
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
      <span class="section-label">How we work</span>
      <h2>Four steps. No lock-in contracts.</h2>
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
    </div>
    <div class="rate-band">
      <div>
        <div class="rate-big">12 EUR <small>per hour of work</small></div>
        <p style="margin-top:8px; max-width:520px;">Packages are recommended scopes, not mandatory retainers. Change them any time, no penalties.</p>
      </div>
      <a href="/en/services/" class="btn btn-primary btn-lg">See services and pricing</a>
    </div>
  </div>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="section-head"><span class="section-label">FAQ</span><h2>Most asked questions</h2></div>
    {faq_block(EN_FAQ)}
  </div>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Results in Google</span>
      <h2>How client websites and AI citations grow</h2>
      <p class="section-subheading">Samples from Google Search Console of our project and a client's from recent months. I always show you the numbers live before we start.</p>
    </div>
    <div class="grid-4">
      <div class="growth-card reveal" data-delay="100">
        <h3 style="color:#6A3FC4;">+355%</h3>
        <p>clicks from Google in 3 months since the start of cooperation</p>
        <div class="growth-bar" style="background:#6A3FC4; width:100%;"></div>
        <p>250 clicks per month, steady growth</p>
      </div>
      <div class="growth-card reveal" data-delay="200">
        <h3 style="color:#F75940;">+246%</h3>
        <p>impressions in Google over the same period</p>
        <div class="growth-bar" style="background:#F75940; width:85%;"></div>
        <p>8,950 impressions per month</p>
      </div>
      <div class="growth-card reveal" data-delay="300">
        <h3 style="color:#1DACD6;">+49%</h3>
        <p>clicks in the last 28 days versus the previous period</p>
        <div class="growth-bar" style="background:#1DACD6; width:70%;"></div>
        <p>121 clicks in 28 days</p>
      </div>
      <div class="growth-card reveal" data-delay="400">
        <h3 style="color:#9B6FD9;">13</h3>
        <p>AI citations of a client website in Google AI Overviews, after our content</p>
        <div class="growth-bar" style="background:#9B6FD9; width:55%;"></div>
        <p>most cited page: 8 times per month</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
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


def en_services() -> tuple[str, str]:
    services = [
        ("/en/services/#ai", "AI visibility", "ChatGPT, Gemini, and AI Overviews recommending you as the first choice.", "ai", "#9B6FD9"),
        ("/en/services/#seo", "Google visibility", "Positions in Google that bring customers, not just traffic.", "search", "#6A3FC4"),
        ("/en/services/#local", "Google Maps visibility", "Business Profile, Maps, and reviews. Nearby customers find you first.", "pin", "#F75940"),
        ("/en/services/#eshop", "E-commerce SEO", "More sales from categories and products. Shoptet, marketplaces, Google Shopping.", "shop", "#1DACD6"),
        ("/en/services/#audit", "SEO audit and analysis", "A precise picture of what holds your site back, with a prioritized plan.", "audit", "#6A3FC4"),
        ("/en/services/#links", "Link building", "Backlinks and authority, without which reaching the top is out of reach.", "link", "#F75940"),
    ]
    cards = "".join(f"""
<div class="benefit-card card-hover reveal" data-delay="150">
  <span class="benefit-icon">{gicon(icon, color, 26)}</span>
  <h3><a href="{href}" style="color:var(--text);">{title}</a></h3>
  <p>{text}</p>
</div>""" for href, title, text, icon, color in services)
    body = f"""
{page_hero("Services", "Services that bring you customers",
           "From technical SEO to AI visibility. Every service costs 12 EUR per hour; scope is agreed upon in the plan.",
           [("Home", "/en/"), ("Services", None)])}
<section class="section"><div class="container">{cards}</div>
  <div class="container" style="margin-top:34px;">
    <h3 style="margin-bottom:14px;">Supplementary services from our partners</h3>
    <p style="max-width:720px; color:var(--text-muted);">Web design and PPC advertising are delivered together with trusted partners, so the whole project stays in one pair of hands: <a href="https://flamia.studio" target="_blank" rel="noopener noreferrer">Flamia Studio</a> (web design) and <a href="https://peterkocur.sk" target="_blank" rel="noopener noreferrer">Peter Kocur</a> (PPC advertising).</p>
  </div>
</section>
<section class="section section-alt" id="pricing">
  <div class="container">
    <div class="section-head"><span class="section-label">Pricing</span><h2>Simple, transparent pricing</h2></div>
    <div class="rate-band">
      <div>
        <div class="rate-big">12 EUR <small>per hour · stop any time</small></div>
        <p style="margin-top:8px; max-width:520px;">Typical scopes: 10 hours/month for a small business site (120 EUR), 20 to 40 hours for an e-shop (240 to 480 EUR).</p>
      </div>
      <a href="/en/contact/?audit=1" class="btn btn-primary btn-lg">Get a quote</a>
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
{page_hero("Contact", "Write to us. I reply personally.",
           "The fastest way is by phone. Or submit the form, and I will get back to you personally within 24 hours with the first steps.",
           [("Home", "/en/"), ("Contact", None)])}
<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:start;">
      <div class="card">
        <span class="section-label">Free call, 30 minutes</span>
        <p style="margin:14px 0 22px;">Call me directly. We talk about your goals and what we would do first. No pressure, no commitment.</p>
        <a href="{PHONE_TEL}" class="btn btn-primary btn-lg" style="width:100%;">Call {PHONE_DISPLAY}</a>
        <ul class="deliv-list" style="margin-top:24px;">
          <li><span class="check">✓</span><span>Free initial audit after the call</span></li>
          <li><span class="check">✓</span><span>Real numbers: what SEO could mean for you</span></li>
          <li><span class="check">✓</span><span>No commitment. You decide when, and whether.</span></li>
        </ul>
      </div>
      <div class="card contact-form-wrap">
        <span class="section-label">Or the form</span>
        <form class="contact-form-el" style="margin-top:16px;">
          <div class="form-grid">
            <div class="form-field"><label class="form-label" for="name">Name and company *</label><input class="form-input" id="name" name="name" type="text" required></div>
            <div class="form-field"><label class="form-label" for="email">Email *</label><input class="form-input" id="email" name="email" type="email" required></div>
            <div class="form-field full"><label class="form-label" for="url">Website address (if you have one)</label><input class="form-input" id="url" name="url" type="url" placeholder="https://"></div>
            <div class="form-field full"><label class="form-label" for="goal">What is your goal? *</label>
              <select class="form-select" id="goal" name="goal" required>
                <option value="">Choose...</option>
                <option>More customers from Google</option>
                <option>Better visibility on Google Maps</option>
                <option>ChatGPT / AI recommendations</option>
                <option>More e-shop sales</option>
                <option>New website or redesign</option>
                <option>Something else</option>
              </select>
            </div>
            <div class="form-field full"><label class="form-label" for="msg">Message</label><textarea class="form-textarea" id="msg" name="msg" placeholder="A few words about your business and what you want to achieve."></textarea></div>
          </div>
          <button type="submit" class="btn btn-primary" style="margin-top:18px; width:100%;">Send message</button>
          <p class="form-note">By sending, you agree to the processing of your data for the purpose of a reply (see <a href="/en/privacy/">privacy</a>).</p>
        </form>
        <div class="form-success" style="display:none; margin-top:16px; background:#F5F1FC; color:var(--brand-cool-deep); padding:16px; border-radius:10px;">
          ✓ Thank you. I will reply personally within 24 hours.
        </div>
        <p style="margin-top:20px;">Or email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
    </div>
  </div>
</section>
"""
    html = base(market="en", path="contact/", title="Contact: free call and free audit | Nokto Studio",
                desc="Get in touch with Nokto Studio. Free 30-minute strategy call and a free initial website audit. I reply personally within 24 hours.",
                canonical=BASE + "/en/contact/", body=body, prefix="../..", extra_head=ORG_SCHEMA)
    return ("en/contact/index.html", html)


def en_faq() -> tuple[str, str]:
    body = f"""
{page_hero("FAQ", "Frequently asked questions", "Answers to what clients ask most. If your question is missing, please ask directly.", [("Home", "/en/"), ("FAQ", None)])}
<section class="section">
  <div class="container" style="max-width:800px;">
    {faq_block(EN_FAQ)}
  </div>
</section>
<section class="section" style="padding-top:0;">
  <div class="container">
    {cta_band("Still have a question?", "Write or call. I reply personally within 24 hours, no strings attached.", "en")}
  </div>
</section>
"""
    faq_html = faq_schema(EN_FAQ, BASE + "/en/faq/")
    html = base(market="en", path="faq/", title="FAQ: SEO pricing, process and AI visibility | Nokto Studio",
                desc="FAQ: how much SEO costs, how long it takes, how we measure results, what SEO for AI search means. Nokto Studio.",
                canonical=BASE + "/en/faq/", body=body, prefix="../..", extra_head=ORG_SCHEMA + faq_html)
    return ("en/faq/index.html", html)


def en_blog() -> tuple[str, str]:
    topics = [
        ("Guide", "tag-violet", "How to choose an SEO agency (and what to watch for)",
         "Pricing, guarantees, reports. 8 questions to ask before signing."),
        ("Pricing", "tag-cerulean", "How much does SEO optimization cost in 2026?",
         "A look at market prices and why you pay retainers for invisible work."),
        ("AI search", "tag-violet-light", "How to get recommended by ChatGPT",
         "A first guide for businesses: how AI tools decide who to recommend."),
        ("Local SEO", "tag-violet", "Google Business Profile: a complete guide",
         "From setup to reviews. What Google values and what it ignores."),
    ]
    cards = "".join(f"""
<div class="blog-card">
  <div><span class="project-tag {tag}">{cat}</span></div>
  <h3>{t}</h3>
  <p>{d}</p>
  <div class="blog-card-foot"><span class="project-tag tag-muted">Coming soon</span><span class="blog-read" style="color:var(--text-muted);">Out soon</span></div>
</div>""" for cat, tag, t, d in topics)
    body = f"""
{page_hero("Blog", "Practical articles on SEO and AI",
           "Guides, pricing and checklists from practice. Every article targets questions real customers ask.", [("Home", "/en/"), ("Blog", None)])}
<section class="section">
  <div class="container">
    <div class="blog-grid">{cards}</div>
    <div style="text-align:center; margin-top:36px;">
      <a href="{PHONE_TEL}" class="btn btn-primary">Free call</a>
    </div>
  </div>
</section>
"""
    html = base(market="en", path="blog/", title="Blog on SEO, Google Maps, and AI Search | Nokto Studio",
                desc="Practical articles: how to choose an SEO agency, SEO pricing, getting recommended by ChatGPT, Google Business Profile.",
                canonical=BASE + "/en/blog/", body=body, prefix="../..", extra_head=ORG_SCHEMA)
    return ("en/blog/index.html", html)


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
{results_slider("en")}
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


ALL = [en_home(), en_services(), en_about(), en_contact(), en_faq(), en_blog(), en_portfolio()]


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
          <a href="/en/contact/?audit=1" class="btn btn-primary">I want a project like this</a>
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
