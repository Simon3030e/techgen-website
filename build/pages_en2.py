# -*- coding: utf-8 -*-
"""Nokto Studio - EN blog (English versions of the content wave, secondary market).

Created 2026-10-01. The EN blog previously showed only "Coming soon" cards.
This module brings the first two real EN posts (E-commerce SEO, SEO audit) and
the listing. English posts pair with the SK originals in pages_sk2.py and the
CZ versions in pages_cz2.py through the EN_PAIR map in engine.py.
"""
from engine import (base, page_hero, cta_band, faq_block, faq_schema, article_schema,
                    ORG_SCHEMA, BASE)

# ---------------------------------------------------------------- META

_BLOG_META = {
    "ecommerce-seo": dict(
        title="E-commerce SEO: 9 settings that turn Google into orders | Nokto Studio",
        desc="E-commerce SEO from categories to Merchant Center: 9 settings that bring orders from Google. Real experience, costs, and the mistakes that hold shops back."),
    "seo-audit-guide": dict(
        title="SEO audit: what it is, what it costs and how it works | Nokto Studio",
        desc="SEO audit explained: what it covers, what it costs (from 180 EUR, entry audit free), and how to turn it into a prioritized plan. A real example."),
}


def blog_post(*, slug: str, label: str, h1: str, answer: str, sections: str,
              faq: list[tuple[str, str]], related: list[tuple[str, str]],
              services: list[tuple[str, str]] | None = None,
              date_iso: str = "2026-10-01", date_display: str = "1 October 2026") -> tuple[str, str]:
    """Render one EN blog post: direct answer first, sections, FAQ, related, CTA."""
    rel_cards = ""
    for u, n in related:
        rel_cards += (f'<div class="benefit-card card-hover related-card">'
                      f'<span class="project-tags"><span class="project-tag tag-violet">Article</span></span>'
                      f'<h3><a href="/en/blog/{u}/" style="color:var(--text);">{n}</a></h3></div>')
    for u, n in (services or []):
        rel_cards += (f'<div class="benefit-card card-hover related-card">'
                      f'<span class="project-tags"><span class="project-tag tag-cerulean">Service</span></span>'
                      f'<h3><a href="{u}" style="color:var(--text);">{n}</a></h3></div>')
    body = f"""
<section class="post-hero">
  <div class="container" style="max-width:820px;">
    <a href="/en/blog/" class="post-back">← Blog</a>
    <span class="section-label">{label}</span>
    <h1>{h1}</h1>
    <p class="post-meta">{date_display} · Simon Stremensky · Nokto Studio</p>
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
    <div class="section-head"><span class="section-label">FAQ</span><h2>Frequently asked questions</h2></div>
    {faq_block(faq)}
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container" style="max-width:820px;">
    <div class="section-head"><span class="section-label">Read next</span><h2>Related articles and services</h2></div>
    <div class="grid-2">{rel_cards}</div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="container">
    {cta_band("Want this done on your website?", "Start with a free audit. See what I would fix first, before the first invoice.", "en")}
  </div>
</section>
"""
    meta = _BLOG_META[slug]
    url = BASE + f"/en/blog/{slug}/"
    html = base(market="en", path=f"blog/{slug}/", title=meta["title"], desc=meta["desc"],
                canonical=url, body=body, prefix="../../../", og_type="article",
                extra_head=ORG_SCHEMA + article_schema(url=url, title=meta["title"],
                                                       desc=meta["desc"], date_iso=date_iso, lang="en")
                          + faq_schema(faq, url))
    return (f"en/blog/{slug}/index.html", html)


# ---------------------------------------------------------------- POSTS

def blog_post_ecommerce() -> tuple[str, str]:
    """EN pair of /sk/blog/seo-pre-eshop/ and /cz/blog/seo-pro-eshop/."""
    sections = """
<h2>What e-commerce SEO is</h2>
<p>E-commerce SEO is the work that makes a customer searching for a specific product or category end up in your shop and order. It is not about traffic, it is about orders. The difference from a company website is scale: a shop has thousands of URLs (categories, products, filters, brands), and each one can either earn or cannibalize another. That is why e-commerce SEO stands on structure, data and content, not on a single trick.</p>

<h2>9 settings that decide whether you get orders</h2>
<h3>1. Categories: copy that answers buying intent</h3>
<p>The category is your strongest page: it collects "buy + product" demand and passes authority to products. Write 250 to 400 words: what the category contains, how to choose, what to watch out for. The first 60 words must be a direct answer for both the customer and AI search engines. Skip "we are the best" filler, write parameters and decision criteria.</p>
<h3>2. Products: titles and attributes on real queries</h3>
<p>Build product titles as brand + model + attribute. People search "chair 40 cm" or "tent for 4 people", not "chair super deal". Put attributes (dimensions, material, compatibility) into a table; Google builds long-tail matches from them. And beware of supplier descriptions copied by everyone: if ten shops have the same text, Google has no reason to show you.</p>
<h3>3. Filters and parameters: canonicals and indexing</h3>
<p>Filtered URLs (color, size, brand) create thousands of duplicates. The fix: canonical to the base category, noindex on combinations without demand, and index only where real search volume exists (for example "wooden chairs"). This single setting can save both crawl budget and rankings.</p>
<h3>4. Product schema and rich results</h3>
<p>Product schema (price, availability, ratings, shipping) pushes your result into rich results with price and stars. Higher CTR for the same budget. The schema must match the page content, otherwise a manual penalty is possible.</p>
<h3>5. Google Merchant Center and marketplaces</h3>
<p>A Merchant Center feed gets you into shopping results and Performance Max, marketplaces into comparison sites. Feed and SEO reinforce each other: a fixed product title helps both channels. The base is a clean feed: titles, GTINs, prices, availability, images.</p>
<h3>6. Internal linking</h3>
<p>Categories link to subcategories and top products, the blog links to products in the copy, and "related products" gets a second chance. Rule: every important page has at least 3 internal links from relevant context. Without internal links, products stay on page five even with perfect titles.</p>
<h3>7. Speed and Core Web Vitals</h3>
<p>Shops are heavy: many images, filters and scripts. Targets: LCP under 2.5s (hero image in WebP, lazy loading), INP under 200ms (minimize blocking JavaScript from filters), CLS under 0.1 (fixed image dimensions). Speed affects both conversion and rankings.</p>
<h3>8. Content for each buying stage</h3>
<p>Categories cover "buying", the blog covers "choosing" and "comparing". Guides like "how to choose", comparisons and FAQs catch the customer before the decision and send them to a product. This is exactly the content competitors often lack and AI tools like to cite.</p>
<h3>9. Measuring orders from organic</h3>
<p>The order and revenue from organic search is what counts. GA4 with e-commerce events, Search Console for queries and positions, the shop system for real orders. If the numbers cannot be matched, SEO has no proof. We measure orders, not feelings.</p>

<h2>A real result from practice</h2>
<p>For Mikramt (a smaller shop on a custom platform), nine months of work brought 15 orders and 2,492.75 EUR in revenue from organic and email channels, with the largest single order at 722 EUR. The work covered category copy (previously empty), structured data, Google Merchant Center, and email sequences. The number is not huge, but it is real and measurable, which matters more in SEO than promises.</p>

<h2>The mistakes that hold shops back</h2>
<ul>
<li>Supplier product descriptions copied without any original text.</li>
<li>Empty categories with no copy, which Google treats as thin content.</li>
<li>noindex accidentally left on categories, often after a migration.</li>
<li>Broken filter indexing: thousands of no-demand URLs in the index.</li>
<li>Measuring total traffic instead of orders from organic.</li>
</ul>

<h2>Timeline and cost</h2>
<p>Long-tail products and smaller categories move in 2 to 4 months, main categories in 6 to 12 months, depending on competition and site health. The work is 10 to 15 hours per month, which is 120 to 180 EUR per month at 12 EUR per hour, plus link and content costs. A free audit always confirms the exact scope.</p>
"""
    faq = [
        ("How much does e-commerce SEO cost?",
         "The work is 10 to 15 hours per month, which is 120 to 180 EUR at 12 EUR per hour. The initial setup (technical, structure, feed) is 6 to 10 hours one-off. Link and content costs are billed separately at cost, with no markup."),
        ("How long until the first orders from organic?",
         "Long-tail products and smaller categories in 2 to 4 months, main categories in 6 to 12 months. For a new shop without authority, the first month is about technical work and structure; orders arrive as Google indexes the pages."),
        ("Is the built-in SEO module of my platform enough?",
         "A built-in module handles titles, meta descriptions and the sitemap, which is a good base. It will not solve category copy, product descriptions, internal linking, buying-stage content, or measuring orders from organic. Those decide your positions against competitors."),
        ("My supplier descriptions are duplicated. Is that a problem?",
         "Yes. If ten shops share the same description, Google has no reason to prefer you. The fix: an original opening paragraph with parameters and decision criteria for every important product; the rest can stay from the supplier."),
        ("Should I invest in Google Shopping or in SEO?",
         "They complement each other. Shopping brings orders immediately, but you pay for every click. SEO grows slower, but an organic order is cheaper and stays yours. A healthy shop runs both channels, and a Merchant Center feed is the base for both."),
        ("How do I measure orders from organic search?",
         "GA4 with e-commerce events (purchase), Search Console for queries and positions, and the shop system for real orders. In the report we connect these three sources so you can see which pages and queries bring revenue, not just traffic."),
        ("Do you work with WooCommerce shops?",
         "Yes. I handle WooCommerce through WordPress SEO: speed, product schema, feed and structure. The principles are the same as with other platforms, only the technical environment differs."),
    ]
    return blog_post(slug="ecommerce-seo", label="E-commerce", h1="E-commerce SEO: 9 settings that turn Google into orders",
                     answer="E-commerce SEO comes down to 9 settings: category copy, product titles on real queries, filter canonicals, product schema, a clean Merchant Center feed, internal linking, Core Web Vitals, content for each buying stage, and measuring orders from organic. Orders matter, not traffic.",
                     sections=sections, faq=faq,
                     related=[("seo-audit-guide", "SEO audit: what it is, what it costs and how it works")],
                     services=[("/en/services/#eshop", "E-commerce SEO"), ("/en/services/#audit", "SEO audit and analysis")])


def blog_post_audit() -> tuple[str, str]:
    """EN pair of /sk/blog/seo-audit-co-to-je/ and /cz/blog/seo-audit-co-to-je/."""
    sections = """
<h2>What an SEO audit is</h2>
<p>An SEO audit is a systematic review of a website that answers three questions: why the site is not winning in Google, what exactly to fix, and in what order. It covers technical aspects (indexing, speed, duplicates, structure), content (titles, keywords, gaps against competitors) and authority (backlinks, E-E-A-T signals). The output is not a PDF for a drawer, it is a prioritized plan with hour estimates.</p>

<h2>Entry, technical and complex audit: the difference</h2>
<table class="metric-table">
<tr><th>Type</th><th>What it covers</th><th>Price</th><th>When you want it</th></tr>
<tr><td><strong>Entry audit</strong></td><td>10 biggest problems and opportunities on one page</td><td>free</td><td>first contact, quick orientation</td></tr>
<tr><td><strong>Technical audit</strong></td><td>indexing, speed, duplicates, URL structure</td><td>from 180 EUR</td><td>before a migration or during a drop</td></tr>
<tr><td><strong>Complex SEO audit</strong></td><td>technical + content + keywords + competitors + plan</td><td>240 to 480 EUR</td><td>before an annual plan and budget</td></tr>
</table>

<h2>How it runs: 5 steps</h2>
<ol>
<li>Data collection: Search Console, GA4, sitemap and access.</li>
<li>Site crawl: indexing, errors, duplicates, speed (Screaming Frog and PageSpeed Insights).</li>
<li>Demand analysis: what people search, where you are visible and where you are not.</li>
<li>Priorities: impact on orders and enquiries versus effort.</li>
<li>Plan: what, when and for how many hours, with measurable goals.</li>
</ol>

<h2>What the audit covers</h2>
<h3>Technical (12 points)</h3>
<p>Indexing, sitemap, robots.txt, canonicals, duplicates, speed (LCP, INP, CLS), HTTPS, structured data, hreflang, internal linking, 404s and redirects, mobile version.</p>
<h3>Content and keywords (10 points)</h3>
<p>Titles and descriptions, H1 and hierarchy, thin content, cannibalization, keywords with volumes, SERP analysis, content gaps against competitors, alt texts, E-E-A-T signals, content for AI answers.</p>
<h3>Authority (5 points)</h3>
<p>Backlink profile, toxic links, competitor link gap, citations and mentions, local profiles.</p>

<h2>How to read the results</h2>
<p>A good audit has priorities: P1 (do now, biggest impact), P2 (within a month) and P3 (ongoing). Every item shows impact and an hour estimate. If you receive 60 pages without an order, you did not get an audit, you got a wish list. Ask for two numbers: how many hours it takes and what it will bring.</p>

<h2>What an SEO audit costs</h2>
<p>The entry audit is free and arrives within 3 working days: the 10 biggest problems and opportunities on one page. A detailed audit is 180 EUR (technical) up to 480 EUR (complex), billed at 12 EUR per hour. With ongoing cooperation, the detailed audit is part of the first month, so you do not pay twice.</p>

<h2>A real example</h2>
<p>A website with about 300 pages: the audit found 6 specific content pages that were missing. After publishing them, impressions grew by 11,000 per month (+14 percent) and clicks by 43 percent within a week. The audit did not hunt for 50 things, it found 6 that move the whole site. That is what an audit result should look like.</p>

<h2>When you do not need an audit</h2>
<p>If your site is brand new with five pages, an audit is pointless; set up the basics instead: titles, structure, Search Console and your Google profile. If the site is healthy and growing, a quarterly check is enough. An audit makes sense during a drop, before a migration, during stagnation, and before a large budget.</p>
"""
    faq = [
        ("What is an SEO audit?",
         "A systematic review that answers three questions: why the site is not winning in Google, what exactly to fix, and in what order. It covers technical, content and authority aspects, and the output is a prioritized plan with hour estimates, not a PDF for a drawer."),
        ("How much does an SEO audit cost?",
         "The entry audit (10 biggest problems on one page) is free within 3 working days. A technical audit starts at 180 EUR, a complex audit with content and a plan is 240 to 480 EUR. With ongoing cooperation, the audit is part of the first month."),
        ("How long does an audit take?",
         "The entry audit within 3 working days. A detailed audit takes 5 to 10 working days depending on site size and available access. Large e-shops with thousands of URLs can take two weeks."),
        ("Is a free online audit tool enough?",
         "Automated tools find part of the technical problems: speed, meta tags, missing alt texts. They do not find content gaps, cannibalization, priorities or your market context. Free tools are a good start, not an audit."),
        ("What is the difference between an SEO audit and a technical audit?",
         "A technical audit covers only the machine part: indexing, speed, duplicates, structure. A complex SEO audit adds content, keywords, competitors and a plan. If your site is not indexed or dropped, technical is enough. If it stagnates, you need the complex one."),
        ("Does an audit guarantee first positions in Google?",
         "No, and nobody serious will guarantee that. An audit guarantees that you will know exactly what holds your site back and what to fix first. That is the best base for results, but results also depend on competition and budget."),
        ("What do you need from me for an audit?",
         "Access to Google Search Console (granting permission is enough), your website address, and GA4 access if you have it. The entry audit works even without access, from public data and a crawl."),
    ]
    return blog_post(slug="seo-audit-guide", label="SEO audit", h1="SEO audit: what it is, what it costs and how it works",
                     answer="An SEO audit is a systematic review that answers three questions: why your site is not winning in Google, what exactly to fix, and in what order. Entry audit free within 3 days, technical from 180 EUR, complex 240 to 480 EUR.",
                     sections=sections, faq=faq,
                     related=[("ecommerce-seo", "E-commerce SEO: 9 settings that turn Google into orders")],
                     services=[("/en/services/#audit", "SEO audit and analysis"), ("/en/services/#seo", "Google visibility")])


# ---------------------------------------------------------------- LISTING

_BLOG_CARDS = [
    dict(slug="ecommerce-seo", cat="E-commerce", tag="tag-cerulean", date="1 October 2026",
         title="E-commerce SEO: 9 settings that turn Google into orders",
         excerpt="Categories, products, filters, schema, Merchant Center, internal links, speed and order measurement. What actually decides orders from Google."),
    dict(slug="seo-audit-guide", cat="SEO audit", tag="tag-violet", date="1 October 2026",
         title="SEO audit: what it is, what it costs and how it works",
         excerpt="Entry, technical and complex audits: differences, prices (from 180 EUR, entry free), 5 steps, and how to read the P1 to P3 priorities."),
]


def _blog_card(c: dict, featured: bool = False) -> str:
    href = f"/en/blog/{c['slug']}/"
    return f"""
<a href="{href}" class="blog-card{' blog-featured' if featured else ''}">
  <div><span class="project-tag {c['tag']}">{c['cat']}</span></div>
  <h3>{c['title']}</h3>
  <p>{c['excerpt']}</p>
  <div class="blog-card-foot"><span class="blog-date">{c.get('date', '')}</span><span class="blog-read">Read article →</span></div>
</a>"""


def latest_cards(n: int = 2) -> str:
    """Latest EN blog cards, used by the EN homepage teaser."""
    return "".join(_blog_card(c) for c in _BLOG_CARDS[:n])


def en_blog() -> tuple[str, str]:
    featured = _BLOG_CARDS[0]
    cards = "".join(_blog_card(c) for c in _BLOG_CARDS[1:])
    body = f"""
{page_hero("Blog", "Practical articles on SEO and AI",
           "Guides, pricing and checklists from practice. Every article targets questions real customers ask. New guides every week.", [("Home", "/en/"), ("Blog", None)])}
<section class="section">
  <div class="container">
    <div class="blog-grid">{_blog_card(featured, featured=True)}{cards}</div>
    <p style="text-align:center; margin-top:32px; color:var(--text-muted);">More guides are coming every week: local SEO, Google Business Profile, AI search, link building and more.</p>
    <div style="text-align:center; margin-top:18px;">
      <a href="/en/contact/?audit=1" class="btn btn-primary">Free website audit</a>
    </div>
  </div>
</section>
"""
    html = base(market="en", path="blog/", title="Blog on SEO, Google Maps, and AI Search | Nokto Studio",
                desc="Practical articles: e-commerce SEO, SEO audits with prices and process. New guides every week. Nokto Studio.",
                canonical=BASE + "/en/blog/", body=body, prefix="../..", extra_head=ORG_SCHEMA)
    return ("en/blog/index.html", html)
