"""Guides, monetisation, community, company and legal pages."""
import re
from layout import page, form, field, select, consent, ad, newsletter_inline, esc, INTEREST_URL, BASE_URL
from articles import ARTICLES
from pages_core import article_cards, faq_html, faq_schema


def hero(crumb, eyebrow, h1, lead, extra=""):
    return (f'<section class="hero" style="padding-bottom:28px"><div class="container"><div class="breadcrumbs"><a href="index.html">Home</a> / {crumb}</div>'
            f'<span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p class="lead">{lead}</p>{extra}</div></section>')


def guides():
    first = {}
    for a in ARTICLES: first.setdefault(a["cat"], a["slug"])
    body = hero("Guides", "Guides", "Guides &amp; playbooks for building online",
                "Practical, original how-tos on AI tools, websites, SEO, hiring and monetisation.",
                '<div class="chips">' + "".join(f'<a class="chip" href="{u}">{c}</a>' for c, u in first.items()) + "</div>")
    body += f'<div class="container"><div class="grid g3">{article_cards()}</div>{ad("inArticle")}'
    body += ('<div class="grid g2"><div class="card"><h3>Write for Core.Digital</h3><p>We pay contributors for original, experience-led guides.</p><p style="margin-top:12px"><a href="careers.html">See contributor roles →</a></p></div>'
             '<div class="card featured"><h3>Sponsored guides</h3><p>Educational content co-created with your team, clearly labelled and built to rank.</p><p style="margin-top:12px"><a href="advertise.html">Sponsor a guide →</a></p></div></div></div>')
    return page("guides.html", "Guides: AI Tools, Websites, SEO & Monetisation", "Original, practical guides on choosing AI tools, website costs, SEO, hiring agencies, newsletters and ad monetisation.", body, "guides.html")


def article(a):
    toc = re.findall(r'<h2 id="([^"]+)">([^<]+)</h2>', a["html"])
    html = a["html"]
    # insert an in-article ad after the 2nd h2 section
    parts = html.split("<h2", 3)
    if len(parts) == 4:
        html = parts[0] + "<h2" + parts[1] + "<h2" + parts[2] + ad("inArticle").replace("container", "") + "<h2" + parts[3]
    related = [x for x in ARTICLES if x["slug"] != a["slug"]][:3]
    rel = "".join(f'<li><a href="{r["slug"]}">{esc(r["title"])}</a></li>' for r in related)
    body = f'''<div class="container" style="padding-top:36px"><div class="breadcrumbs"><a href="index.html">Home</a> / <a href="guides.html">Guides</a> / {esc(a["cat"])}</div>
<div class="article-wrap"><article class="prose">
<span class="badge">{esc(a["cat"])}</span><h1 style="margin-top:14px;font-size:clamp(1.9rem,4.4vw,2.9rem)">{esc(a["title"])}</h1>
<div class="article-meta"><span>By Core.Digital Editorial</span><span>Updated <time datetime="{a["date"]}">{a["date"]}</time></span><span>{a["read"]} min read</span></div>
<p class="lead" style="font-size:1.12rem">{esc(a["desc"])}</p>
{html}
<div style="display:flex;flex-wrap:wrap;gap:8px;margin:28px 0"><strong style="align-self:center">Share:</strong>
<button class="btn btn-sm btn-ghost" data-share="x">X</button><button class="btn btn-sm btn-ghost" data-share="linkedin">LinkedIn</button><button class="btn btn-sm btn-ghost" data-share="facebook">Facebook</button><button class="btn btn-sm btn-ghost" data-share="whatsapp">WhatsApp</button><button class="btn btn-sm btn-ghost" data-share="copy">Copy link</button></div>
<div class="card"><h3>Get the Core Brief</h3><p>New tools, one tactic and exclusive deals — weekly, free.</p><div style="margin-top:12px">{newsletter_inline("article")}</div></div>
<p class="form-note" style="margin-top:18px">Editorial independence: this guide was not paid for. Some outbound links may be affiliate links; see our <a href="disclaimer.html">disclosure</a>.</p>
</article>
<aside class="sidebar"><nav class="toc" aria-label="On this page"><strong>On this page</strong><ol>{"".join(f'<li><a href="#{i}">{esc(t)}</a></li>' for i, t in toc)}</ol></nav>
<div class="card featured"><h3>Need an expert?</h3><p>Get matched free with up to 5 vetted specialists.</p><p style="margin-top:12px"><a class="btn btn-primary btn-block" href="get-matched.html">Get matched</a></p></div>
<div class="ad-slot" data-ad="sidebar"></div>
<div class="card"><strong>Related guides</strong><ul style="padding-left:1.1em;margin:10px 0 0">{rel}</ul></div></aside></div></div>'''
    schema = [{"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["desc"], "datePublished": a["date"], "dateModified": a["date"],
               "author": {"@type": "Organization", "name": "Core.Digital Editorial"}, "publisher": {"@type": "Organization", "name": "Core.Digital"}, "mainEntityOfPage": BASE_URL + a["slug"]},
              {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE_URL},
                  {"@type": "ListItem", "position": 2, "name": "Guides", "item": BASE_URL + "guides.html"},
                  {"@type": "ListItem", "position": 3, "name": a["title"]}]}]
    return page(a["slug"], a["title"], a["desc"], body, "guides.html", schema, og_type="article")


def plan(name, price, per, feats, cta, href, featured=False, pay=None, group="checkout"):
    p = f' data-pay="{pay}" data-group="{group}"' if pay else ""
    return (f'<div class="card{" featured" if featured else ""}">{"<span class=badge style=float:right>Most popular</span>" if featured else ""}<h3>{name}</h3>'
            f'<div class="price">{price}<small>{per}</small></div><ul class="features">{"".join(f"<li>{f}</li>" for f in feats)}</ul>'
            f'<a class="btn {"btn-primary" if featured else "btn-ghost"} btn-block" href="{href}"{p}>{cta}</a></div>')


def submit():
    plans = "".join([
        plan("Standard", "Free", "", ["Reviewed in the queue (typically 2–4 weeks)", "Directory listing & category page", "Save / bookmark by users"], "Submit free", "#form"),
        plan("Fast-Track", "$49", " one-time", ["Reviewed within 72 hours", "Listing + category placement", "Newsletter ‘New tools’ mention", "Refund if not approved"], "Choose Fast-Track", "#form", pay="fastTrack"),
        plan("Featured", "$149", " / month", ["Everything in Fast-Track", "Top-of-category placement (labelled Sponsored)", "Homepage rotation", "Highlighted card"], "Get Featured", "#form", True, "featured"),
        plan("Verified + Review", "$299", " one-time", ["Verified ✓ badge", "Hands-on editorial review", "Short video walkthrough in library", "Permanent listing"], "Get Verified", "#form", pay="verified")])
    inner = ('<div class="form-row">' + field("Tool name", "tool_name") + field("Website", "tool_url", "url", placeholder="https://") + "</div>" +
             '<div class="form-row">' + select("Category", "category", ["AI Assistants", "AI Writing", "AI Image", "AI Video", "AI Audio", "Developer Tools", "Website Builders", "Hosting & Domains", "SEO", "Marketing & CRM", "Design", "Productivity", "Automation", "Analytics", "E-commerce", "Other"]) +
             select("Pricing model", "pricing", ["Free", "Freemium", "Paid", "Open source"]) + "</div>" +
             field("One-line description (max 140 chars)", "tagline", attrs='maxlength="140"') +
             select("Listing plan", "plan", ["Standard (free)", "Fast-Track ($49)", "Featured ($149/mo)", "Verified + Review ($299)"]) +
             '<div class="form-row">' + field("Your name", "name") + field("Email", "email", "email") + "</div>" +
             field("Anything else? (launch date, deals for our readers…)", "notes", "textarea", False) +
             consent("I confirm I represent this product and accept the <a href=\"terms.html\">Terms</a>."))
    body = hero("Submit a tool", "For makers", "Submit your AI or digital tool",
                "Reach founders, marketers, creators and developers actively looking for tools. Every listing is reviewed by a human.")
    body += f'''<div class="container"><div class="grid g4">{plans}</div>
<p class="form-note" style="margin-top:10px">Launch pricing. Paid placements are always labelled “Sponsored” and never affect editorial reviews. Payment links are sent after approval.</p>
<div class="split" style="margin-top:40px;align-items:start" id="form"><div class="card">{form("Tool submission", inner, "Submit tool", "Submitted! We'll confirm by email and share next steps for your plan.")}</div>
<div><h2>Listing guidelines</h2><ul class="trust-list"><li>Working product with a public website</li><li>Clear pricing information</li><li>No malware, scraping of personal data, or deceptive claims</li><li>We may edit descriptions for clarity and neutrality</li></ul>
<h3 style="margin-top:24px">Want more?</h3><p style="color:var(--muted)">Newsletter sponsorships, video reviews and contest sponsorships are on the <a href="advertise.html">advertise page</a>.</p>
{faq_html([("How long does review take?", "Standard submissions are reviewed in order (typically 2–4 weeks). Fast-Track is reviewed within 72 hours."), ("Do you guarantee approval?", "No. Every listing is reviewed for quality and safety. Paid Fast-Track is refunded if a tool is not approved."), ("Can I update my listing later?", "Yes — reply to your confirmation email with changes.")])}</div></div></div>'''
    return page("submit.html", "Submit Your AI or Digital Tool", "List your AI or digital tool on Core.Digital. Free listing, Fast-Track review, Featured placement and Verified reviews available.", body, "submit.html")


def advertise():
    pk = "".join([
        plan("Directory Featured", "$149", " / month", ["Top-of-category placement", "Homepage rotation", "Sponsored label + highlighted card"], "Book placement", "#inquiry"),
        plan("Newsletter Sponsor", "from $250", " / issue", ["Primary slot in the Core Brief", "Logo, 60-word copy, CTA link", "Click report after send"], "Book a send", "#inquiry", True),
        plan("Sitewide Banner", "$499", " / month", ["Rotating banner in header, article and footer slots", "Desktop + mobile", "Monthly impression report"], "Book banner", "#inquiry"),
        plan("Sponsored Guide", "$750", " one-time", ["Educational guide co-created with you", "Clearly labelled, permanent URL", "Newsletter + social promotion"], "Commission a guide", "#inquiry"),
        plan("Video Integration", "$600", " / video", ["Dedicated walkthrough or tutorial", "Library placement + embed on your tool page", "Rights to reuse clip"], "Book video", "#inquiry"),
        plan("Contest Title Sponsor", "$1,500", " / contest", ["Naming rights + logo on contest page", "Prize announcement & winner feature", "Lead list of opted-in entrants"], "Sponsor a contest", "#inquiry")])
    inner = ('<div class="form-row">' + field("Name", "name") + field("Work email", "email", "email") + "</div>" +
             '<div class="form-row">' + field("Company", "company") + field("Website", "website", "url", False, "https://") + "</div>" +
             '<div class="form-row">' + select("Interested in", "package", ["Directory Featured", "Newsletter Sponsor", "Sitewide Banner", "Sponsored Guide", "Video Integration", "Contest Sponsor", "Custom / bundle", "Domain / website acquisition"]) +
             select("Monthly budget", "budget", ["Under $500", "$500 – $1,500", "$1,500 – $5,000", "$5,000+"]) + "</div>" +
             field("Goals & target audience", "goals", "textarea") + consent())
    body = hero("Advertise", "Media kit", "Advertise &amp; sponsor on Core.Digital",
                "Put your product in front of founders, marketers, creators and developers at the moment they're choosing tools and hiring experts.",
                f'<div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-primary" href="#inquiry">Request media kit</a><a class="btn btn-ghost" href="{INTEREST_URL}" target="_blank" rel="noopener">Partnership / domain inquiry ↗</a></div>')
    body += f'''<div class="container">
<div class="grid g4" style="margin-bottom:36px"><div class="stat"><b>High-intent</b><span>Readers comparing &amp; buying tools</span></div><div class="stat"><b>B2B</b><span>Founders, marketers, developers</span></div><div class="stat"><b>6</b><span>Ad formats</span></div><div class="stat"><b>100%</b><span>Labelled, brand-safe placements</span></div></div>
<h2>Packages</h2><div class="grid g3" id="video">{pk}</div>
<p class="form-note" style="margin-top:10px">Launch rates — early sponsors lock pricing for 6 months. Bundles save up to 25%. Audience metrics are shared in the media kit on request.</p>
<div class="split" style="margin-top:48px;align-items:start" id="inquiry"><div><h2>Request the media kit</h2><p class="lead">Tell us about your goals. We reply within 1 business day with availability, audience data and a proposal.</p>
<ul class="trust-list"><li>Contextual placements next to relevant categories and guides</li><li>Transparent reporting (impressions, clicks)</li><li>No pop-unders, no auto-play audio, no deceptive formats</li></ul></div>
<div class="card">{form("Advertising inquiry", inner, "Request media kit", "Thanks! We'll send the media kit and availability within 1 business day.")}</div></div></div>'''
    return page("advertise.html", "Advertise & Sponsor — Media Kit", "Sponsor Core.Digital: featured directory listings, newsletter sponsorships, banners, sponsored guides, video integrations and contest sponsorships.", body, "advertise.html")


def support():
    tiers = [("☕ Supporter", "$5", "/mo", "supporter", ["Name on the supporters wall", "Supporter-only monthly roundup"]),
             ("🚀 Builder", "$25", "/mo", "builder", ["All Supporter perks", "Early access to new free tools", "Vote on the next guides"]),
             ("🏆 Patron", "$100", "/mo", "patron", ["All Builder perks", "Logo on the supporters page", "Quarterly strategy call"]),
             ("💜 One-time", "Any", " amount", "onetime", ["Fund contests, content and hosting", "Every contribution is acknowledged"])]
    t = "".join(f'<div class="card{" featured" if k == "builder" else ""}"><h3>{n}</h3><div class="price">{p}<small>{per}</small></div><ul class="features">{"".join(f"<li>{x}</li>" for x in f)}</ul>'
                f'<a class="btn {"btn-primary" if k == "builder" else "btn-ghost"} btn-block" href="#pledge" data-tier="{k}">Support</a></div>' for n, p, per, k, f in tiers)
    alloc = [("Operations & hosting", 30), ("Original content", 25), ("Marketing & promotion", 15), ("Hiring talent", 15), ("Contests & prizes", 15)]
    bars = "".join(f'<div class="bar-row"><span>{a}</span><div class="bar"><i style="width:{v}%"></i></div><b>{v}%</b></div>' for a, v in alloc)
    pay = "".join(f'<a class="btn btn-ghost" data-pay="{k}" data-group="donate" data-hide-empty>{n}</a>' for k, n in
                  [("stripe", "💳 Card (Stripe)"), ("paypal", "PayPal"), ("buymeacoffee", "☕ Buy Me a Coffee"), ("kofi", "Ko-fi"), ("githubSponsors", "GitHub Sponsors")])
    inner = ('<div class="form-row">' + field("Name", "name") + field("Email", "email", "email") + "</div>" +
             '<div class="form-row">' + select("Support type", "tier", [("supporter", "Supporter $5/mo"), ("builder", "Builder $25/mo"), ("patron", "Patron $100/mo"), ("onetime", "One-time")]) + field("Amount (USD)", "amount", "number", False, "e.g. 50", 'min="1"') + "</div>" +
             select("Direct my support to", "allocation", ["Wherever needed most", "Operations & hosting", "Original content", "Marketing & promotion", "Hiring talent", "Contests & prizes"]) +
             select("Preferred payment method", "method", ["Card", "PayPal", "Bank transfer", "UPI", "Crypto", "Other"]) +
             field("Message (optional)", "message", "textarea", False) +
             '<label class="check"><input type="checkbox" name="Show on wall" value="Yes"> List my name on the supporters wall</label>')
    body = hero("Support", "Reader-supported", "Keep Core.Digital free, independent &amp; growing",
                "Your support funds hosting, honest reviews, free tools, new talent and prize pools for our community contests.")
    body += f'''<div class="container"><div class="grid g4">{t}</div>
<div id="paylinks" style="display:flex;flex-wrap:wrap;gap:10px;margin-top:22px">{pay}</div>
<div class="split" style="margin-top:48px;align-items:start"><div><h2>Where your money goes</h2><p class="lead">We publish how support is allocated.</p><div class="bars">{bars}</div>
<h3 style="margin-top:32px">Other ways to help</h3><ul class="trust-list"><li>Share a guide with a friend or team</li><li><a href="submit.html">Suggest a tool</a> we should review</li><li>Sponsor a contest prize — <a href="advertise.html">see packages</a></li><li>Become a partner — <a href="{INTEREST_URL}" target="_blank" rel="noopener">contact us</a></li></ul></div>
<div class="card" id="pledge"><h3>Pledge your support</h3><p>We'll reply with a secure payment link for your chosen method within 24 hours.</p><div style="margin-top:14px">{form("Donation / support pledge", inner, "Pledge support 💜", "Thank you! We'll email your secure payment link shortly.")}</div></div></div>
<p class="form-note" style="margin-top:20px">Contributions support a for-profit publication and are not tax-deductible charitable donations.</p></div>
<script>document.querySelectorAll("[data-tier]").forEach(function(b){{b.addEventListener("click",function(){{var s=document.querySelector("#pledge select[name=tier]");if(s)s.value=b.getAttribute("data-tier");}});}});</script>'''
    return page("support.html", "Support Core.Digital — Donate & Become a Supporter", "Support independent digital media. Monthly and one-time contributions fund operations, content, marketing, hiring and contest prizes.", body, "support.html")


def contests():
    cs = [("🧠 AI Tool Review Challenge", "Write an honest, hands-on review of an AI tool you use every week. Best reviews are published with a byline.", "Writers, marketers", "1st: $300 · 2nd: $150 · 3rd: $50 + publication"),
          ("🎨 Landing Page Design Sprint", "Design a landing page for a fictional AI startup (brief provided on registration). Judged on clarity, conversion and craft.", "Designers, developers", "1st: $400 · 2nd: $200 · 3rd: $100"),
          ("🚀 Side-Project Showcase", "Show us something you built online — a site, tool, newsletter or channel — and what you learned.", "Makers, founders", "Featured placement + $250 grand prize")]
    cards = "".join(f'<div class="card"><h3>{n}</h3><p>{d}</p><p style="margin-top:10px"><span class="badge">For: {w}</span></p><p style="margin-top:10px;color:var(--text)"><strong>Planned prizes:</strong> {p}</p></div>' for n, d, w, p in cs)
    inner = ('<div class="form-row">' + field("Name", "name") + field("Email", "email", "email") + "</div>" +
             select("Contest", "contest", [c[0][2:].strip() for c in cs]) +
             field("Link to your entry (optional now)", "entry_url", "url", False, "https://") +
             field("Short pitch", "pitch", "textarea", False) +
             '<div class="form-row">' + field("Country", "country") + select("How did you hear about us?", "source", ["Search", "Social", "Newsletter", "Friend", "YouTube", "Other"], False) + "</div>" +
             consent("I am 18+ (or have guardian consent), accept the <a href=\"#rules\">contest rules</a> and agree to be contacted about this contest."))
    body = hero("Contests", "Build · Win · Get featured", "Contests &amp; prizes for digital creators",
                "Monthly challenges that reward skill, not luck. Winners get cash prizes, publication and exposure to our audience.",
                '<p style="color:var(--muted);margin-bottom:8px">Current round closes in:</p><div class="countdown" data-countdown></div>')
    body += f'''<div class="container"><div class="grid g3">{cards}</div>
<div class="split" style="margin-top:48px;align-items:start"><div class="card" id="enter"><h2>Register / submit an entry</h2>{form("Contest entry", inner, "Enter contest", "You're registered! Watch your inbox for the brief and deadlines.")}</div>
<div><h2>How it works</h2><ol style="color:var(--muted)"><li>Register for a contest (free to enter — no purchase necessary).</li><li>Receive the brief and submission guidelines by email.</li><li>Submit before the deadline.</li><li>A judging panel scores entries on published criteria.</li><li>Winners are announced on this page and in the newsletter.</li></ol>
<div class="card featured" style="margin-top:20px"><h3>Sponsor a contest</h3><p>Put your brand on the prize pool and connect with skilled, engaged entrants.</p><p style="margin-top:12px"><a class="btn btn-primary" href="advertise.html#inquiry">Become a sponsor</a></p></div></div></div>
<div id="rules" style="margin-top:48px"><h2>Official rules (summary)</h2>{faq_html([
("Eligibility", "Open to individuals 18+ (or with guardian consent) where permitted by law. Void where prohibited. Core.Digital staff and their families are not eligible."),
("No purchase necessary", "Entry is free. Paying for any product or service does not improve your chances."),
("Prizes", "Prizes listed are planned amounts for each round and are confirmed in the round's brief before entries open. Prizes are paid via PayPal, bank transfer or equivalent within 30 days of winner verification. Winners are responsible for any taxes."),
("Judging", "Entries are judged on originality, quality, usefulness and adherence to the brief by a panel chosen by Core.Digital. Decisions are final."),
("Rights", "You keep ownership of your entry. By entering you grant Core.Digital a non-exclusive licence to display and promote it with credit."),
("Privacy", "We use entrant details only to run the contest and, if you opt in, to send updates. See our Privacy Policy."),
])}</div></div>'''
    schema = {"@context": "https://schema.org", "@type": "Event", "name": "Core.Digital Creator Contests", "eventAttendanceMode": "https://schema.org/OnlineEventAttendanceMode",
              "eventStatus": "https://schema.org/EventScheduled", "startDate": "2026-10-01", "endDate": "2026-11-30",
              "location": {"@type": "VirtualLocation", "url": BASE_URL + "contests.html"}, "organizer": {"@type": "Organization", "name": "Core.Digital", "url": BASE_URL}}
    return page("contests.html", "Contests & Prizes for Digital Creators", "Enter Core.Digital contests: AI tool reviews, landing page design and side-project showcases. Win prizes and get featured.", body, "contests.html", schema)


def careers():
    roles = [("Contributing Writer — AI & SaaS", "Remote · Freelance · Per article", "Hands-on reviews and guides on AI and digital tools."),
             ("Video Creator / Editor", "Remote · Freelance · Per video", "Short tutorials, tool walkthroughs and YouTube content."),
             ("SEO & Content Strategist", "Remote · Part-time contract", "Keyword research, content briefs, internal linking and technical SEO."),
             ("Partnerships & Ad Sales", "Remote · Commission-based", "Sell sponsorships, featured listings and contest sponsorships."),
             ("Community & Contest Manager", "Remote · Part-time", "Run contests, moderate submissions and grow our creator community."),
             ("Front-end Developer (HTML/CSS/JS)", "Remote · Project-based", "Build new free tools, calculators and interactive features.")]
    rc = "".join(f'<div class="card"><h3>{n}</h3><p class="result-count">{m}</p><p style="margin-top:8px">{d}</p><p style="margin-top:14px"><a class="btn btn-sm btn-primary" href="#apply" data-role="{esc(n)}">Apply</a></p></div>' for n, m, d in roles)
    apply_inner = ('<div class="form-row">' + field("Full name", "name") + field("Email", "email", "email") + "</div>" +
                   select("Role", "role", [r[0] for r in roles] + ["Open application"]) +
                   '<div class="form-row">' + field("Portfolio / LinkedIn / CV link", "portfolio", "url", True, "https://") + field("Location & time zone", "location") + "</div>" +
                   select("Availability", "availability", ["< 10 hrs/week", "10–20 hrs/week", "20–40 hrs/week", "Project-based"]) +
                   field("Why you? (2–3 examples of your best work)", "pitch", "textarea") + consent())
    talent_inner = ('<div class="form-row">' + field("Name / Agency name", "name") + field("Email", "email", "email") + "</div>" +
                    '<div class="form-row">' + field("Website / portfolio", "portfolio", "url", True, "https://") + select("Type", "type", ["Freelancer", "Studio (2–10)", "Agency (11+)"]) + "</div>" +
                    select("Primary service", "service", ["Website design & build", "SEO & content", "Paid ads", "AI & automation", "E-commerce", "App / SaaS development", "Branding & design", "Social & video"]) +
                    '<div class="form-row">' + select("Typical project size", "min_project", ["Under $2,500", "$2,500 – $10,000", "$10,000 – $25,000", "$25,000+"]) + field("Country", "country") + "</div>" +
                    field("2–3 case studies (links + results)", "case_studies", "textarea") + consent())
    job_inner = ('<div class="form-row">' + field("Company", "company") + field("Job title", "job_title") + "</div>" +
                 '<div class="form-row">' + select("Type", "job_type", ["Full-time", "Part-time", "Contract", "Freelance"]) + field("Salary / rate range", "salary", placeholder="e.g. $60k–80k or $40/hr") + "</div>" +
                 '<div class="form-row">' + field("Location / Remote", "job_location") + select("Package", "job_package", ["Standard post — $99 / 30 days", "Featured post — $149 / 30 days"]) + "</div>" +
                 field("Job description or link", "job_desc", "textarea") + '<div class="form-row">' + field("Your name", "name") + field("Email", "email", "email") + "</div>" + consent())
    body = hero("Careers", "We're hiring", "Work with Core.Digital",
                "We're building a world-class, remote team of writers, creators, strategists and builders. Also: join our Talent Network to receive paid client projects.",
                '<div class="chips"><a class="chip" href="#roles">Open roles</a><a class="chip" href="#talent">Talent Network</a><a class="chip" href="#post-job">Post a job</a></div>')
    body += f'''<div class="container" id="roles"><div class="grid g3">{rc}</div>
<div class="split" style="margin-top:48px;align-items:start"><div class="card" id="apply"><h2>Apply</h2>{form("Job application", apply_inner, "Send application", "Application received! We reply to every applicant within 7 days.")}</div>
<div><h2>Why Core.Digital</h2><ul class="trust-list"><li>100% remote, async-first</li><li>Paid per piece or per project — on time</li><li>Your name on your work; build a public portfolio</li><li>Access to tools, briefs and editors who care</li></ul></div></div>
<div class="split" style="margin-top:56px;align-items:start" id="talent"><div><span class="eyebrow">For freelancers &amp; agencies</span><h2>Join the Talent Network</h2><p class="lead">Receive hand-matched project introductions from businesses that submitted a brief through <a href="get-matched.html">Get Matched</a>.</p>
<ul class="trust-list"><li>Pre-qualified briefs with budget &amp; timeline</li><li>Only projects in your niche and size</li><li>Reviewed network — quality over volume</li></ul></div>
<div class="card">{form("Talent Network application", talent_inner, "Apply to network", "Thanks! Our team reviews applications weekly and will be in touch.")}</div></div>
<div class="split" style="margin-top:56px;align-items:start" id="post-job"><div><span class="eyebrow">For employers</span><h2>Post a job to digital talent</h2><p class="lead">Reach developers, marketers, designers and AI builders.</p>
<div class="grid g2">{plan("Standard", "$99", " / 30 days", ["Listed on careers page", "Included in newsletter jobs block"], "Post a job", "#post-job", pay="jobPost")}{plan("Featured", "$149", " / 30 days", ["Pinned &amp; highlighted", "Social promotion", "Newsletter top slot"], "Feature a job", "#post-job", True, "jobFeatured")}</div></div>
<div class="card">{form("Job post request", job_inner, "Submit job post", "Received! We'll review and send a payment link to publish your post.")}</div></div></div>
<script>document.querySelectorAll("[data-role]").forEach(function(b){{b.addEventListener("click",function(){{var s=document.querySelector("#apply select[name=role]");if(s)s.value=b.getAttribute("data-role");}});}});</script>'''
    return page("careers.html", "Careers, Talent Network & Job Posts", "Join Core.Digital: remote roles for writers, video creators, SEO strategists and developers. Agencies and freelancers can join our Talent Network.", body, "careers.html")


def newsletter():
    inner = ('<div class="form-row">' + field("First name", "name", required=False) + field("Email", "email", "email") + "</div>" +
             '<fieldset style="border:0;padding:0"><legend class="fl" style="margin-bottom:8px">Topics you care about</legend><div class="opt-grid">' +
             "".join(f'<label class="opt"><input type="checkbox" name="topics" value="{t}"><span>{t}</span></label>' for t in ["AI tools", "Websites", "SEO", "Ads & growth", "Monetisation", "Jobs & contests"]) +
             "</div></fieldset>" + select("I am a…", "role", ["Founder / business owner", "Marketer", "Developer", "Designer", "Creator", "Student", "Other"], False))
    body = hero("Newsletter", "The Core Brief", "The week in AI &amp; digital — in 5 minutes",
                "Every week: new tools worth your time, one tactic you can use today, jobs, contests and exclusive deals. Free. Unsubscribe anytime.")
    body += f'''<div class="container split" style="align-items:start"><div class="card">{form("Newsletter signup (page)", inner, "Subscribe free", "You're in! Check your inbox for a welcome email.")}</div>
<div><h2>What's inside</h2><ul class="trust-list"><li>🧰 5 new tools, tested and summarised</li><li>🎯 One tactic: SEO, ads, AI or monetisation</li><li>🎁 Reader-only deals from partners</li><li>🏆 Open contests &amp; new remote roles</li></ul>
<div class="card featured" style="margin-top:22px"><h3>Sponsor the Core Brief</h3><p>Reach a high-intent audience of builders and buyers.</p><p style="margin-top:12px"><a class="btn btn-primary" href="advertise.html">See sponsorship</a></p></div></div></div>'''
    return page("newsletter.html", "The Core Brief Newsletter", "Subscribe to the Core Brief: weekly AI and digital tools, tactics, deals, jobs and contests in 5 minutes.", body, "newsletter.html")


def about():
    body = hero("About", "About us", "The core of everything digital",
                "Core.Digital helps people build and grow online — by finding the right tools, learning what works, and connecting with the right experts.")
    body += f'''<div class="container"><div class="grid g3">
<div class="card"><div class="icon">🧭</div><h3>Mission</h3><p>Cut through digital noise. We curate, test and explain — so you spend less time searching and more time building.</p></div>
<div class="card"><div class="icon">⚖️</div><h3>Independence</h3><p>Editorial picks aren't for sale. Sponsored placements are always labelled and kept separate from reviews.</p></div>
<div class="card"><div class="icon">🤝</div><h3>Community</h3><p>Contests, a talent network and free tools — built with and for the people who make the internet work.</p></div></div>
<div class="split" style="margin-top:48px"><div><h2>What we do</h2><ul class="trust-list"><li>Curate the <a href="directory.html">AI &amp; digital tools directory</a></li><li>Publish practical <a href="guides.html">guides</a> and <a href="videos.html">video explainers</a></li><li>Build <a href="free-tools.html">free calculators</a></li><li>Match businesses with <a href="get-matched.html">vetted specialists</a></li><li>Run <a href="contests.html">contests</a> and hire <a href="careers.html">talent</a></li></ul></div>
<div class="card"><h3>How we make money</h3><p>Display ads, labelled sponsorships and featured listings, affiliate links, job posts, contest sponsors and reader support. Details in our <a href="disclaimer.html">disclosure</a>.</p>
<p style="margin-top:14px"><a class="btn btn-primary" href="{INTEREST_URL}" target="_blank" rel="noopener">Partner with us ↗</a></p></div></div></div>'''
    return page("about.html", "About Core.Digital", "Core.Digital is an independent hub for AI and digital tools, guides, free calculators and expert matching.", body, "about.html")


def contact():
    inner = ('<div class="form-row">' + field("Name", "name") + field("Email", "email", "email") + "</div>" +
             select("Topic", "topic", ["General question", "Get matched / project help", "Advertising & sponsorship", "Partnership", "Domain / website acquisition", "Tool listing", "Contest", "Careers", "Press", "Report an issue", "Privacy request"]) +
             field("Subject", "subject_line") + field("Message", "message", "textarea") + consent())
    body = hero("Contact", "Contact", "Talk to Core.Digital", "Questions, partnerships, sponsorships, press or privacy requests — we reply within 1–2 business days.")
    body += f'''<div class="container split" style="align-items:start"><div class="card">{form("Contact form", inner, "Send message")}</div>
<div class="grid"><div class="card"><h3>🤝 Interested in this website or domain?</h3><p>Sponsorship, advertising, partnership or acquisition of Core.Digital.</p><p style="margin-top:12px"><a class="btn btn-primary" href="{INTEREST_URL}" target="_blank" rel="noopener">Contact via web.works ↗</a></p></div>
<div class="card"><h3>✉️ Prefer email?</h3><p>Open a pre-addressed message in your email app.</p><p style="margin-top:12px"><a class="btn btn-ghost" href="contact.html" data-mail="Core.Digital inquiry">Email us</a></p></div>
<div class="card"><h3>⚡ Need a specialist?</h3><p>The fastest route is a free brief.</p><p style="margin-top:12px"><a href="get-matched.html">Get matched →</a></p></div></div></div>'''
    return page("contact.html", "Contact Core.Digital", "Contact Core.Digital for questions, partnerships, advertising, press and privacy requests.", body, "contact.html",
                {"@context": "https://schema.org", "@type": "ContactPage", "name": "Contact Core.Digital"})


LEGAL_DATE = "September 22, 2026"


def legal(slug, title, desc, sections):
    body = hero(title, "Legal", title, f"Last updated: {LEGAL_DATE}")
    body += '<div class="container"><div class="prose">' + "".join(f"<h2>{h}</h2>{c}" for h, c in sections) + \
            '<p>Questions? Use our <a href="contact.html">contact form</a>.</p></div></div>'
    return page(slug, title, desc, body)


def privacy():
    return legal("privacy.html", "Privacy Policy", "How Core.Digital collects, uses and protects personal information.", [
        ("Who we are", "<p>Core.Digital (“we”, “us”) operates this website. For privacy requests, use the <a href=\"contact.html\">contact form</a> and choose “Privacy request”.</p>"),
        ("What we collect", "<ul><li><strong>Information you submit</strong> in forms: name, email, phone, company, project details, applications, pledges and messages.</li><li><strong>Usage data</strong> (only with consent): pages viewed, device and approximate location via analytics.</li><li><strong>Advertising data</strong>: ad partners such as Google may use cookies to serve and measure ads.</li><li><strong>Local preferences</strong> stored in your browser (theme, saved tools, consent choice).</li></ul>"),
        ("How we use it", "<ul><li>To respond to inquiries and deliver requested services (e.g., matching you with specialists).</li><li>To send newsletters you subscribed to (unsubscribe anytime).</li><li>To run contests, process applications and sponsorships.</li><li>To improve the site and measure performance.</li></ul>"),
        ("Sharing", "<p>We do not sell personal information. If you request matching, we share your brief with up to five specialists for that purpose. Form submissions are processed by our form-delivery provider (FormSubmit). Analytics (Google Analytics) and advertising (Google AdSense) providers process data under their own policies. We may disclose information where required by law.</p>"),
        ("Google advertising", "<p>Third-party vendors, including Google, use cookies to serve ads based on prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on visits to this site and/or other sites. You can opt out of personalised advertising at <a href=\"https://adssettings.google.com\" target=\"_blank\" rel=\"noopener\">Google Ads Settings</a> or <a href=\"https://www.aboutads.info/choices/\" target=\"_blank\" rel=\"noopener\">aboutads.info</a>. See <a href=\"https://policies.google.com/technologies/partner-sites\" target=\"_blank\" rel=\"noopener\">how Google uses data from partner sites</a>.</p>"),
        ("Your rights", "<p>Depending on where you live (e.g., GDPR, UK GDPR, CCPA/CPRA, PIPEDA, Quebec Law 25, India DPDP Act), you may request access, correction, deletion or portability of your data, or object to processing. We respond within applicable legal timeframes.</p>"),
        ("Retention & security", "<p>We keep submissions only as long as needed for the purpose collected or as required by law, and use reasonable safeguards. No method of transmission is 100% secure.</p>"),
        ("Children", "<p>This site is not directed to children under 13 (or the minimum age in your jurisdiction), and we do not knowingly collect their data.</p>"),
        ("Changes", "<p>We may update this policy and will revise the date above.</p>")])


def terms():
    return legal("terms.html", "Terms of Use", "Terms governing use of Core.Digital.", [
        ("Acceptance", "<p>By using Core.Digital you agree to these Terms. If you do not agree, please do not use the site.</p>"),
        ("Content", "<p>Content is provided for general information only and may change without notice. It is not professional, legal, financial or tax advice.</p>"),
        ("Directory & third parties", "<p>Listings describe third-party products we don't control. Prices, features and availability change; verify on the vendor's site. We are not responsible for third-party products, sites or services.</p>"),
        ("Matching service", "<p>Get Matched introduces businesses and independent specialists. Any agreement is solely between you and the specialist. We don't guarantee outcomes, quality or pricing, and are not a party to those contracts.</p>"),
        ("Paid listings & advertising", "<p>Paid placements are subject to editorial review and may be declined. Sponsored placements are labelled. Fees for services already delivered are non-refundable except where stated (e.g., Fast-Track refund if not approved).</p>"),
        ("Contests", "<p>Each contest is governed by its official rules on the contests page and its brief.</p>"),
        ("User submissions", "<p>You're responsible for what you submit and must have the right to share it. You grant us a non-exclusive licence to use submitted listings and entries to operate and promote the site.</p>"),
        ("Acceptable use", "<p>No scraping that burdens the site, spam, malware, unlawful content or attempts to disrupt the service.</p>"),
        ("Intellectual property", "<p>See our <a href=\"trademark.html\">Trademark &amp; Copyright notice</a>.</p>"),
        ("Liability", "<p>To the maximum extent permitted by law, the site is provided “as is” without warranties, and we are not liable for indirect or consequential damages arising from its use.</p>"),
        ("Changes", "<p>We may update these Terms; continued use means acceptance.</p>")])


def disclaimer():
    return legal("disclaimer.html", "Disclaimer & Disclosure", "Editorial, affiliate, advertising and sponsorship disclosure for Core.Digital.", [
        ("Advertising disclosure", "<p>Core.Digital is supported by display advertising (such as Google AdSense), sponsorships, featured listings, affiliate commissions, job posts and reader contributions. Sponsored placements are clearly labelled “Sponsored”.</p>"),
        ("Affiliate links", "<p>Some outbound links may be affiliate links. If you buy through them we may earn a commission at no extra cost to you. Affiliate relationships never determine our editorial opinions.</p>"),
        ("Editorial independence", "<p>Guides and reviews are written independently. Sponsored content is labelled as such and kept separate from editorial rankings.</p>"),
        ("No professional advice", "<p>Content is for information and education only. Consult qualified professionals for legal, financial, tax or security decisions.</p>"),
        ("Calculator estimates", "<p>Free tool outputs are indicative estimates based on stated assumptions, not quotes or guarantees.</p>"),
        ("Contributions", "<p>Reader contributions support a for-profit publication and are not tax-deductible charitable donations.</p>")])


def trademark():
    return legal("trademark.html", "Trademark & Copyright Notice", "Trademark and copyright disclosure for Core.Digital.", [
        ("Copyright", "<p>© 2026 Core.Digital. All original text, graphics, layout, code and compilations on this website are protected by copyright and may not be reproduced without permission, except for brief quotations with attribution and a link.</p>"),
        ("Our name", "<p>“Core.Digital” is the name of this independent website and the domain it operates on. It is used descriptively, as a combination of the ordinary English words “core” and “digital”. We do not claim exclusive rights over those common words.</p>"),
        ("No affiliation", "<p>Core.Digital is <strong>not affiliated with, endorsed by, sponsored by, or connected to</strong> any company, product or brand that uses “Core Digital”, “CoreDigital” or similar names — including, without limitation, any business named Core Digital Media, Core Digital Network, Core Digital Marketing or Core Digital Brands. Any similarity in name is coincidental. If you are looking for one of those companies, please visit their official channels.</p>"),
        ("Third-party marks", "<p>All product names, logos, brands and trademarks shown in the directory, guides and videos are the property of their respective owners. Their use is for identification and commentary only (nominative fair use) and does not imply endorsement. Tool initials shown in the directory are generic placeholders, not the owners' logos.</p>"),
        ("Embedded videos", "<p>Videos are embedded using YouTube's official player and remain the property of their creators; they are shown under YouTube's Terms of Service.</p>"),
        ("Takedown / concerns", "<p>If you believe content on this site infringes your rights, send a notice via the <a href=\"contact.html\">contact form</a> (topic: “Report an issue”) with the URL, your rights, and your contact details. We review notices promptly and remove infringing material where appropriate.</p>")])


def cookies():
    return legal("cookies.html", "Cookie Policy", "How Core.Digital uses cookies and local storage.", [
        ("Essential", "<p>Local storage keeps your theme, saved tools and consent choice. These never leave your browser.</p>"),
        ("Analytics (optional)", "<p>With your consent, Google Analytics 4 measures traffic with IP anonymisation.</p>"),
        ("Advertising (optional)", "<p>When ads are enabled, Google and partners may set cookies to serve and measure ads. In the EEA/UK/Switzerland, a Google-certified consent management platform is used for personalised ads.</p>"),
        ("Manage", "<p>Clear your browser's site data to reset your choice, or adjust cookies in browser settings. Opt out of personalised ads at <a href=\"https://adssettings.google.com\" target=\"_blank\" rel=\"noopener\">Google Ads Settings</a>.</p>")])


def notfound():
    body = hero("404", "404", "This page drifted out of orbit", "It may have moved. Try the directory search or head home.",
                '<div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-primary" href="index.html">Home</a><a class="btn btn-ghost" href="directory.html">Search tools</a><a class="btn btn-ghost" href="get-matched.html">Get matched</a></div>')
    p = page("404.html", "Page not found", "Page not found.", body, noindex=True)
    # GitHub Pages serves 404.html for any missing path (possibly nested) — use absolute base for assets/links.
    from urllib.parse import urlparse
    return p.replace("<head>", f'<head><base href="{urlparse(BASE_URL).path}">', 1)
