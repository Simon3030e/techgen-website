# -*- coding: utf-8 -*-
"""Nokto Studio - EN core pages (secondary market; projects stay as legacy pages)."""
from engine import (base, page_hero, cta_band, faq_block, faq_schema,
                    steps_block, benefit_cards, ORG_SCHEMA, CAL, EMAIL, BASE)

EN_FAQ = [
    ("How much does SEO cost?",
     "You pay 12 EUR per hour of work. A small business website typically needs 10 hours per month (120 EUR), an e-shop 20 to 40 hours (240 to 480 EUR). Exact scope is confirmed in the plan after a free audit."),
    ("How long until SEO brings results?",
     "First movements on less competitive keywords usually appear within 2 to 4 months. Main competitive queries take 6 to 12 months. Realistic timelines are shared in the audit."),
    ("Do you guarantee first positions in Google?",
     "No, and no serious agency can. We guarantee a transparent process, realistic timelines and measurable progress reported every month."),
    ("Can you get my business recommended by ChatGPT?",
     "Yes, that is our specialty. We optimize your site so ChatGPT, Gemini and Google AI Overviews understand and cite it when customers ask for recommendations."),
    ("Are the contracts binding for 12 months?",
     "No. Work runs month to month and you can stop any time. We invoice for actual hours worked."),
]


def en_home() -> tuple[str, str]:
    h1 = ('Let customers find you in <span class="hl-blue">Google</span>, '
          'on <span class="hl-red">Google Maps</span> and in <span class="hl-green">ChatGPT</span>.')
    body = f"""
<section class="hero">
  <div class="container">
    <div class="hero-content">
      <span class="hero-label">SEO agency for business owners · Europe</span>
      <h1>{h1}</h1>
      <p class="hero-sub">Nokto Studio is an SEO agency for business owners. We bring you customers from organic search, Google Maps and AI tools, and grow your e-shop sales. At a transparent 12 EUR per hour. No retainers you cannot see through, no lock-in contracts.</p>
      <div class="hero-ctas">
        <a href="{CAL}" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg">Book a free call</a>
        <a href="/en/contact/?audit=1" class="btn btn-outline btn-lg">Get a free audit</a>
      </div>
      <p class="hero-scarcity">Capacity for new projects: open from October 2026.</p>
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
        <span class="benefit-icon icon-blue">🤖</span>
        <h3>Get recommended by AI</h3>
        <p>When a customer asks ChatGPT for a recommendation, you want to be in the answer. We build sites that AI tools understand and cite.</p>
      </div>
      <div class="benefit-card card-hover reveal" data-delay="200">
        <span class="benefit-icon icon-red">📍</span>
        <h3>Customers from Google and Maps</h3>
        <p>Local search and your Google Business Profile are the fastest path to nearby customers. We set them up and review them weekly.</p>
      </div>
      <div class="benefit-card card-hover reveal" data-delay="300">
        <span class="benefit-icon icon-yellow">🛒</span>
        <h3>More e-shop sales</h3>
        <p>Categories and products optimized for keywords that buy. Google Shopping and marketplaces tracked as part of the system.</p>
      </div>
      <div class="benefit-card card-hover reveal" data-delay="400">
        <span class="benefit-icon icon-green">📈</span>
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
        {"title": "Measure and report", "text": "A monthly report: hours worked and what they contained, positions, clicks, enquiries, orders and mentions in AI answers."},
    ])}
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="section-label">Pricing</span>
      <h2>12 EUR per hour. You pay for work, not retainer.</h2>
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
        ("/en/services/#seo", "SEO optimization", "Positions in Google that bring customers, not just traffic.", "🔍"),
        ("/en/services/#local", "Local SEO and Google profile", "Google Maps, Business Profile, reviews. Nearby customers find you first.", "📍"),
        ("/en/services/#ai", "SEO for AI search", "ChatGPT, Gemini and AI Overviews recommending you as the first choice.", "🤖"),
        ("/en/services/#eshop", "E-commerce SEO", "More sales from categories and products. Shoptet, marketplaces, Google Shopping.", "🛒"),
        ("/en/services/#audit", "SEO audit and analysis", "A precise picture of what holds your site back, with a prioritized plan.", "📋"),
        ("/en/services/#links", "Link building", "Backlinks and authority, without which the top is out of reach.", "🔗"),
        ("/en/services/#web", "Web design", "Fast, custom sites that rank and sell. WordPress and e-commerce.", "⚡"),
        ("/en/services/#ppc", "PPC advertising", "Google Ads for results now, while SEO builds up.", "🎯"),
    ]
    cards = "".join(f"""
<div class="benefit-card card-hover reveal" data-delay="150">
  <span class="benefit-icon icon-blue">{icon}</span>
  <h3><a href="{href}" style="color:var(--text);">{title}</a></h3>
  <p>{text}</p>
</div>""" for href, title, text, icon in services)
    body = f"""
{page_hero("Services", "Services that bring you customers",
           "From technical SEO to AI visibility. Every service costs 12 EUR per hour, scope agreed in the plan.",
           [("Home", "/en/"), ("Services", None)])}
<section class="section"><div class="container">{cards}</div></section>
<section class="section section-alt">
  <div class="container">
    <div class="section-head"><span class="section-label">Pricing</span><h2>Simple, transparent pricing</h2></div>
    <div class="rate-band">
      <div>
        <div class="rate-big">12 EUR <small>per hour · stop any time</small></div>
        <p style="margin-top:8px; max-width:520px;">Typical scopes: 10 hours/month for a small business site (120 EUR), 20 to 40 hours for an e-shop (240 to 480 EUR).</p>
      </div>
      <a href="{CAL}" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg">Get a quote</a>
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
                desc="SEO optimization, local SEO and Google Business Profile, SEO for AI search, e-commerce SEO, audits, link building, web design and PPC. 12 EUR per hour.",
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
        <p>I am not a big agency and I do not pretend to be one. The advantage: the same person who designs your strategy does the work with you. No forwarding between departments, no lost context.</p>
        <h2>How we work</h2>
        <p>We combine two worlds: expert SEO work (technical, content, authority, AI visibility) and automation that gets more out of the same effort. That is how we can work at 12 EUR per hour and still focus on results, not on padding hours.</p>
      </div>
      <div>
        <img src="/assets/img/simon.png" alt="Simon, founder of Nokto Studio" loading="lazy" style="border-radius:var(--radius-lg); border:1px solid var(--border-light);">
        <p style="text-align:center; margin-top:12px; font-size:0.85rem; color:var(--text-muted);">Simon, founder of Nokto Studio</p>
      </div>
    </div>
  </div>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="section-head"><span class="section-label">Values</span><h2>Three rules that always apply</h2></div>
    <div class="grid-3">
      <div class="benefit-card"><span class="benefit-icon icon-blue">🛡️</span><h3>No promises we cannot keep</h3><p>Nobody can guarantee the first position in Google. What we guarantee: a transparent process, realistic timelines and measurable progress.</p></div>
      <div class="benefit-card"><span class="benefit-icon icon-red">⚡</span><h3>Reply within 12 hours</h3><p>No ghosting, no forwarding. The client always knows what is happening and why.</p></div>
      <div class="benefit-card"><span class="benefit-icon icon-green">🧾</span><h3>Every hour reported</h3><p>You pay for work delivered. Every hour is in the report with its content and result.</p></div>
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
{page_hero("Contact", "Write to us. We reply within 12 hours.",
           "The fastest path is a free call through the calendar. If you prefer a form, use the one below.",
           [("Home", "/en/"), ("Contact", None)])}
<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:start;">
      <div class="card">
        <span class="section-label">Free call, 30 minutes</span>
        <p style="margin:14px 0 22px;">Pick a slot in the calendar. We talk about your goals and what we would do first. No pressure, no commitment.</p>
        <a href="{CAL}" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg" style="width:100%;">Open calendar</a>
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
          <p class="form-note">By sending you agree to the processing of your data for the purpose of a reply (see <a href="/en/privacy/">privacy</a>).</p>
        </form>
        <div class="form-success" style="display:none; margin-top:16px; background:#E6F4EA; color:var(--g-green-deep); padding:16px; border-radius:10px;">
          ✓ Thank you. We will reply within 12 hours.
        </div>
        <p style="margin-top:20px;">Or email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
    </div>
  </div>
</section>
"""
    html = base(market="en", path="contact/", title="Contact: free call and free audit | Nokto Studio",
                desc="Get in touch with Nokto Studio. Free 30-minute strategy call and a free initial website audit. Reply within 12 hours.",
                canonical=BASE + "/en/contact/", body=body, prefix="../..", extra_head=ORG_SCHEMA)
    return ("en/contact/index.html", html)


def en_faq() -> tuple[str, str]:
    body = f"""
{page_hero("FAQ", "Frequently asked questions", "Answers to what clients ask most. If your question is missing, ask directly.", [("Home", "/en/"), ("FAQ", None)])}
<section class="section">
  <div class="container" style="max-width:800px;">
    {faq_block(EN_FAQ)}
  </div>
</section>
<section class="section" style="padding-top:0;">
  <div class="container">
    {cta_band("Still have a question?", "Write or call. Reply within 12 hours, no strings attached.", "en")}
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
        ("How to choose an SEO agency (and what to watch for)", "Pricing, guarantees, reports. 8 questions to ask before signing.", "tag-blue"),
        ("How much does SEO optimization cost in 2026?", "A look at market prices and why you pay retainers for invisible work.", "tag-yellow"),
        ("How to get recommended by ChatGPT", "A first guide for businesses: how AI tools decide who to recommend.", "tag-green"),
        ("Google Business Profile: a complete guide", "From setup to reviews. What Google values and what it ignores.", "tag-red"),
    ]
    cards = "".join(f"""
<div class="benefit-card card-hover">
  <span class="project-tag {tag}">Article in progress</span>
  <h3 style="margin-top:12px;">{t}</h3>
  <p>{d}</p>
</div>""" for t, d, tag in topics)
    body = f"""
{page_hero("Blog", "Practical articles on SEO and AI",
           "We write what we can verify in practice. First articles out this month.", [("Home", "/en/"), ("Blog", None)])}
<section class="section">
  <div class="container">
    <div class="grid-2">{cards}</div>
    <div style="text-align:center; margin-top:36px;">
      <a href="{CAL}" target="_blank" rel="noopener noreferrer" class="btn btn-primary">Free call</a>
    </div>
  </div>
</section>
"""
    html = base(market="en", path="blog/", title="Blog on SEO, Google Maps and AI search | Nokto Studio",
                desc="Practical articles: how to choose an SEO agency, SEO pricing, getting recommended by ChatGPT, Google Business Profile.",
                canonical=BASE + "/en/blog/", body=body, prefix="../..", extra_head=ORG_SCHEMA)
    return ("en/blog/index.html", html)


def en_portfolio() -> tuple[str, str]:
    body = f"""
{page_hero("Portfolio", "Work examples, not just praise",
           "Selected projects. Detailed case studies on request, respecting client confidentiality.",
           [("Home", "/en/"), ("Portfolio", None)])}
<section class="section">
  <div class="container">
    <div class="grid-2">
      <div class="project-card card-hover">
        <div class="project-card-body">
          <h3>Villa Paris, Piestany (SK)</h3>
          <p>Premium accommodation. Rebrand, new website, hospitality copywriting and local SEO in one system. Goal: more direct bookings without portal commissions.</p>
          <div class="project-tags">
            <span class="project-tag tag-blue">Branding</span>
            <span class="project-tag tag-green">Web</span>
            <span class="project-tag tag-red">Local SEO</span>
          </div>
          <a href="/en/villa-paris/" class="btn btn-outline" style="margin-top:20px;">Read the story</a>
        </div>
      </div>
      <div class="project-card card-hover">
        <div class="project-card-body">
          <h3>E-commerce SEO</h3>
          <p>Technical optimization, category and product content, visibility in Google and AI tools for Slovak e-shops.</p>
          <div class="project-tags">
            <span class="project-tag tag-yellow">E-shop SEO</span>
            <span class="project-tag tag-green">Content</span>
          </div>
          <a href="{CAL}" target="_blank" rel="noopener noreferrer" class="btn btn-outline" style="margin-top:20px;">Ask about it</a>
        </div>
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
    html = base(market="en", path="portfolio/", title="Portfolio: SEO and web design projects | Nokto Studio",
                desc="Selected Nokto Studio projects: Villa Paris Piestany (rebrand, web, local SEO), e-commerce SEO and more.",
                canonical=BASE + "/en/portfolio/", body=body, prefix="../..", extra_head=ORG_SCHEMA)
    return ("en/portfolio/index.html", html)


ALL = [en_home(), en_services(), en_about(), en_contact(), en_faq(), en_blog(), en_portfolio()]


def en_villa_paris() -> tuple[str, str]:
    body = f"""
{page_hero("Case study · Branding &amp; Web", "Villa Paris: a brand and website built from zero",
           "Premium accommodation in Piestany had a great product but no brand. We solved it with identity, website, hospitality copywriting and local SEO as one system.",
           [("Home", "/en/"), ("Portfolio", "/en/portfolio/"), ("Villa Paris", None)])}
<section class="section">
  <div class="container">
    <div class="grid-2" style="align-items:start;">
      <div class="prose">
        <span class="section-label">Problem</span>
        <h2 style="margin-top:8px;">Great location. Zero presentation.</h2>
        <p>Villa Paris offers real value: a peaceful setting in Piestany, closeness to the spa center and ADELI Medical Center, comfortable rooms and a family atmosphere. But the visual identity and digital presence communicated none of it.</p>
        <p>Visitors arrived on the website and could not quickly understand what makes the property worth a booking. The brand looked generic, the texts did not answer the questions people ask before reserving. Reservations were lost before a conversation even started.</p>
        <h2>Solution: one system, four areas</h2>
        <h3>Brand identity redesign</h3>
        <p>A new visual system: logo, color palette, typography. Built to feel warm, premium and instantly recognizable.</p>
        <h3>Website rebuild</h3>
        <p>A reworked structure focused on clarity and booking conversion from the first scroll. Fast loading, a simple path to reservation, mobile experience as a priority.</p>
        <h3>Hospitality copywriting</h3>
        <p>Guest-oriented texts that answer real pre-booking questions: location, comfort, what to expect on arrival.</p>
        <h3>Local SEO</h3>
        <p>Google Business Profile set up properly, local keywords for Piestany and spa stays, so guests searching for exactly this kind of accommodation find Villa Paris.</p>
      </div>
      <div class="card">
        <span class="section-label">Project scope</span>
        <ul class="deliv-list">
          <li><span class="check">✓</span><span>Brand redesign: logo, colors, typography.</span></li>
          <li><span class="check">✓</span><span>New website: structure, design, speed.</span></li>
          <li><span class="check">✓</span><span>Guest-oriented hospitality copywriting.</span></li>
          <li><span class="check">✓</span><span>Local SEO: Google Business Profile, local queries.</span></li>
          <li><span class="check">✓</span><span>Measurement: bookings and their sources.</span></li>
        </ul>
        <div style="margin-top:22px;">
          <a href="{CAL}" target="_blank" rel="noopener noreferrer" class="btn btn-primary">I want a project like this</a>
        </div>
      </div>
    </div>
  </div>
</section>
<section class="section section-alt">
  <div class="container">
    {cta_band("Want a brand and website that sell?", "Free audit and 30 minutes of time. We reply within 12 hours.", "en")}
  </div>
</section>
"""
    html = base(market="en", path="villa-paris/", title="Villa Paris Piestany: rebrand, web and local SEO | Nokto Studio",
                desc="Case study: how Nokto Studio built Villa Paris from the ground up. Brand identity, new website, hospitality copywriting and local SEO for premium accommodation in Piestany.",
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
    <p>The data controller is Nokto Studio (Simon, operator of noktostudio.com). Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    <h2>What data and why</h2>
    <ul>
      <li>Contact form: name, email, website address and message. Purpose: to answer your enquiry.</li>
      <li>Calendar (Calendly): name, email and meeting slot. Purpose: to hold the call.</li>
      <li>Analytics: anonymized visitor data (Google Analytics 4, Microsoft Clarity) to improve the website.</li>
    </ul>
    <h2>How long we keep data</h2>
    <p>Contacts from forms and the calendar are kept for up to 24 months from the last communication, unless a collaboration begins.</p>
    <h2>Your rights</h2>
    <p>You have the right to access, correct, delete and transfer your data. Send requests to <a href="mailto:{EMAIL}">{EMAIL}</a>. You may also file a complaint with your national data protection authority.</p>
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
    <p>These terms govern the collaboration between Nokto Studio ("the provider") and the client for marketing services: SEO optimization, web design, PPC campaigns, email marketing and related consulting.</p>
    <h2>2. Price and invoicing</h2>
    <p>Services are billed at an hourly rate of 12 EUR for hours worked. Invoicing runs monthly, in arrears, based on the hours report. Ad spend and link or third-party tool costs are passed through at actual price, without markup.</p>
    <h2>3. Term</h2>
    <p>Collaboration runs month to month. Either party can end it at the end of a calendar month, in writing, without penalties.</p>
    <h2>4. Responsibility and results</h2>
    <p>The provider does not guarantee specific positions in search engines or specific traffic volumes. The provider guarantees delivered work, transparent reporting and execution according to the agreed plan. Guarantees of specific positions are not possible and are not offered.</p>
    <h2>5. Content rights</h2>
    <p>Content created for the client within paid collaboration transfers to the client once the invoice is paid. The provider may show the work in its portfolio by agreement with the client.</p>
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
