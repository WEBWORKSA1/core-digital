"""Core pages: home, directory, free tools, videos, get matched, checklist."""
from layout import page, form, field, select, consent, ad, newsletter_inline, esc, INTEREST_URL
from articles import ARTICLES

SERVICES = [
    ("website", "🖥️ Website design & build", "New site or redesign"),
    ("seo", "🔎 SEO & content", "Rank and get organic traffic"),
    ("ads", "📈 Paid ads (Google/Meta)", "PPC, social ads, ROAS"),
    ("ai", "🤖 AI & automation", "Chatbots, agents, workflows"),
    ("ecommerce", "🛒 E-commerce", "Shopify, WooCommerce, CRO"),
    ("app", "📱 App / SaaS development", "Web or mobile product"),
    ("branding", "🎨 Branding & design", "Logo, identity, UI/UX"),
    ("social", "📣 Social & video", "Content, YouTube, creators"),
    ("other", "✨ Something else", "Tell us in the next steps"),
]
BUDGETS = [("under-2.5k", "Under $2,500"), ("2.5k-10k", "$2,500 – $10,000"), ("10k-25k", "$10,000 – $25,000"),
           ("25k-50k", "$25,000 – $50,000"), ("50k-plus", "$50,000+"), ("unsure", "Not sure yet")]


def article_cards(n=None):
    items = ARTICLES if n is None else ARTICLES[:n]
    return "".join(
        f'<a class="card reveal" href="{a["slug"]}"><span class="badge">{esc(a["cat"])}</span>'
        f'<h3 style="margin-top:12px">{esc(a["title"])}</h3><p>{esc(a["desc"])}</p>'
        f'<p class="result-count" style="margin-top:12px">{a["read"]} min read · Updated {a["date"]}</p></a>' for a in items)


def video_cards(limit=None, cat=None):
    # rendered at build time from the same list as config.js (kept in sync by build.py)
    from videos import VIDEOS
    vs = [v for v in VIDEOS if not cat or v["cat"] == cat]
    vs = vs[:limit] if limit else vs
    return "".join(
        f'<article class="reveal"><div class="video" data-yt="{v["id"]}" role="button" tabindex="0" aria-label="Play: {esc(v["title"])}">'
        f'<img loading="lazy" src="https://i.ytimg.com/vi/{v["id"]}/hqdefault.jpg" alt="" width="480" height="360"><div class="play"><span></span></div></div>'
        f'<h3 style="margin:12px 0 4px;font-size:1rem">{esc(v["title"])}</h3><p class="result-count">{esc(v["by"])} · {v["cat"]}</p></article>' for v in vs)


FAQ = [
    ("What is Core.Digital?", "Core.Digital is an independent hub for people building online: a curated directory of AI and digital tools, practical guides, free calculators, curated videos, and a free matching service that connects businesses with vetted digital specialists."),
    ("Is Get Matched really free?", "Yes. Businesses never pay us to be matched. We review your brief and introduce up to five relevant specialists. Specialists may pay for membership or introductions — that never changes whether we recommend them."),
    ("How do I get my tool listed?", "Submit it on the Submit a Tool page. Standard listings are free and reviewed in the queue; paid Fast-Track, Featured and Verified options speed things up and add visibility. Sponsored placements are always labelled."),
    ("How does Core.Digital make money?", "Display advertising (such as Google AdSense), clearly labelled sponsorships and featured listings, affiliate links, job posts, contest sponsors, and reader support. Editorial picks are never sold."),
    ("Can I sponsor, advertise or partner with Core.Digital?", "Yes — see the Advertise page for packages, or use the partnership link at the top of every page."),
]


def faq_html(items=FAQ):
    return "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in items)


def faq_schema(items=FAQ):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}


def home():
    svc_chips = "".join(f'<a class="chip" href="get-matched.html?service={k}">{t}</a>' for k, t, _ in SERVICES[:6])
    body = f'''
<section class="hero"><div class="container">
<span class="eyebrow">● The core of everything digital</span>
<h1>Find the right <span class="grad-text">AI &amp; digital tools</span> — and the experts to use them.</h1>
<p class="lead">Core.Digital is your independent index of AI tools, website and marketing software, no-fluff guides, free calculators — plus a free matching service that connects you with vetted digital specialists.</p>
<form class="search-xl" action="directory.html" role="search"><label class="sr-only" for="hero-q">Search tools</label>
<input id="hero-q" name="q" placeholder="Search tools: writing, video, SEO, website builder…" autocomplete="off"><span class="kbd hide-sm" style="align-self:center">⌘K</span>
<button class="btn btn-primary" type="submit">Search</button></form>
<div class="chips" id="home-cats" aria-label="Browse categories"></div>
<div class="stats">
<div class="stat"><b id="stat-tools">70+</b><span>Curated tools</span></div>
<div class="stat"><b id="stat-cats">14</b><span>Categories</span></div>
<div class="stat"><b>5</b><span>Free calculators</span></div>
<div class="stat"><b>$0</b><span>To get matched</span></div></div>
</div></section>
{ad("header")}
<section><div class="container">
<div class="section-head"><div><span class="eyebrow">Directory</span><h2>Tools worth knowing</h2><p class="lead">Hand-picked across every category. Save favourites, filter by price, compare.</p></div>
<a class="btn btn-ghost" href="directory.html">Browse all tools →</a></div>
<div class="grid g4" id="home-tools"></div>
<div class="card" style="margin-top:18px;display:flex;flex-wrap:wrap;gap:12px;align-items:center;justify-content:space-between">
<p><strong style="color:var(--text)">Built a tool?</strong> Get it in front of founders, marketers and builders. Free and paid listings available.</p>
<a class="btn btn-sm btn-primary" href="submit.html">Submit your tool</a></div>
</div></section>

<section class="section-alt" id="match"><div class="container split">
<div><span class="eyebrow">Free matching service</span><h2>Need it done for you? Get matched with vetted digital experts.</h2>
<p class="lead">Tell us what you need in under 2 minutes. We review every brief by hand and introduce up to 5 specialists who fit your budget and goals.</p>
<ul class="trust-list"><li>Free for businesses, no obligation</li><li>Website, SEO, ads, AI automation, e-commerce, apps, branding</li><li>Your details are shared only with specialists you approve</li><li>Budget-fit: from freelancers to full-service agencies</li></ul>
<div class="chips" style="margin-top:22px">{svc_chips}</div></div>
<div class="wizard"><h3>Start your free brief</h3><p class="form-note" style="margin-bottom:14px">Takes about 60 seconds.</p>
{form("Lead: Quick brief (home)", select("What do you need?", "service", [(k, t.split(" ", 1)[1]) for k, t, _ in SERVICES]) + select("Budget", "budget", BUDGETS) + '<div class="form-row">' + field("Name", "name") + field("Work email", "email", "email") + "</div>" + field("Website (optional)", "website", "url", False, "https://") + consent(), "Get my free matches →", "Brief received! We'll email you within 1 business day with next steps.")}
</div></div></section>

<section><div class="container">
<div class="section-head"><div><span class="eyebrow">Guides</span><h2>Practical playbooks, zero fluff</h2></div><a class="btn btn-ghost" href="guides.html">All guides →</a></div>
<div class="grid g3">{article_cards(6)}</div></div></section>
{ad("footer")}
<section class="section-alt"><div class="container">
<div class="section-head"><div><span class="eyebrow">Free tools</span><h2>Calculators that answer real questions</h2></div><a class="btn btn-ghost" href="free-tools.html">Open free tools →</a></div>
<div class="grid g3">
<a class="card reveal" href="free-tools.html#cost"><div class="icon">💸</div><h3>Website cost estimator</h3><p>Get a realistic build range by site type, pages and features.</p></a>
<a class="card reveal" href="free-tools.html#roas"><div class="icon">📈</div><h3>Ad ROI &amp; ROAS calculator</h3><p>Project clicks, conversions, CPA and break-even ROAS.</p></a>
<a class="card reveal" href="free-tools.html#serp"><div class="icon">🔎</div><h3>Google SERP preview</h3><p>Write titles and meta descriptions that fit and get clicked.</p></a>
<a class="card reveal" href="free-tools.html#utm"><div class="icon">🔗</div><h3>UTM link builder</h3><p>Tag campaigns properly so analytics tells the truth.</p></a>
<a class="card reveal" href="free-tools.html#ai"><div class="icon">🤖</div><h3>AI API cost estimator</h3><p>Forecast monthly token spend before you ship an AI feature.</p></a>
<a class="card reveal" href="checklist.html"><div class="icon">✅</div><h3>Growth checklist</h3><p>52 checks to audit any website, funnel and marketing stack.</p></a>
</div></div></section>

<section><div class="container">
<div class="section-head"><div><span class="eyebrow">Watch &amp; learn</span><h2>The best explainers on AI, code &amp; SEO</h2></div>
<div style="display:flex;gap:8px"><a class="btn btn-ghost" href="videos.html">Video library →</a><a class="btn btn-accent" data-yt-channel hidden target="_blank" rel="noopener">▶ Subscribe</a></div></div>
<div class="grid g3">{video_cards(3)}</div></div></section>

<section class="section-alt"><div class="container grid g3">
<div class="card reveal"><div class="icon">🏆</div><h3>Contests &amp; prizes</h3><p>Monthly challenges for builders, writers and designers. Enter, get featured, win prizes.</p><p style="margin-top:14px"><a href="contests.html">See open contests →</a></p></div>
<div class="card reveal"><div class="icon">🧑‍💻</div><h3>We're hiring talent</h3><p>Writers, video creators, SEO specialists and partnership leads — remote, flexible.</p><p style="margin-top:14px"><a href="careers.html">View roles →</a></p></div>
<div class="card reveal"><div class="icon">💜</div><h3>Support independent media</h3><p>Reader support keeps our reviews honest and our tools free for everyone.</p><p style="margin-top:14px"><a href="support.html">Become a supporter →</a></p></div>
</div></section>

<section><div class="container"><div class="cta-band">
<div class="split"><div><h2>Put your brand at the core of digital.</h2><p>Sponsored listings, newsletter placements, video integrations and contest sponsorships — to an audience of founders, marketers and builders.</p></div>
<div style="display:flex;flex-wrap:wrap;gap:10px"><a class="btn btn-ghost" href="advertise.html">See ad packages</a><a class="btn btn-ghost" href="{INTEREST_URL}" target="_blank" rel="noopener">Partnership inquiry ↗</a></div></div></div></div></section>

<section class="section-alt"><div class="container split">
<div><span class="eyebrow">The Core Brief</span><h2>One email. The week in AI &amp; digital, in 5 minutes.</h2><p class="lead">New tools worth your time, one tactic you can use today, and exclusive deals. Free.</p>{newsletter_inline("home")}</div>
<div><h3>Frequently asked</h3>{faq_html()}</div></div></section>
'''
    schema = [{"@context": "https://schema.org", "@type": "WebSite", "name": "Core.Digital", "url": "https://webworksa1.github.io/core-digital/",
               "potentialAction": {"@type": "SearchAction", "target": "https://webworksa1.github.io/core-digital/directory.html?q={search_term_string}", "query-input": "required name=search_term_string"}},
              faq_schema()]
    return page("index.html", "Core.Digital — AI & Digital Tools Directory, Guides and Expert Matching",
                "Discover the best AI and digital tools, read practical guides, use free calculators, and get matched free with vetted website, SEO, ads and AI experts.",
                body, "index.html", schema, ["tools-data.js", "directory.js"])


def directory():
    body = f'''
<section class="hero" style="padding-bottom:24px"><div class="container">
<div class="breadcrumbs"><a href="index.html">Home</a> / Directory</div>
<span class="eyebrow">Tool directory</span><h1>AI &amp; digital tools directory</h1>
<p class="lead">Curated software for writing, design, video, code, websites, SEO, marketing, automation and commerce. Filter by category and price, save your shortlist.</p></div></section>
<div class="container"><div class="dir-layout">
<aside class="filters" aria-label="Filters"><strong>Filters</strong> <button class="save-btn" id="f-reset" style="float:right">Reset</button>
<h4>Price</h4><div id="f-price">{"".join(f'<label><input type="checkbox" value="{p}"> {p}</label>' for p in ["Free","Freemium","Paid","Open source"])}</div>
<h4>Your list</h4><label><input type="checkbox" id="f-saved"> Saved only ♥</label>
<h4>Category</h4><div id="f-cats"></div>
<div class="card featured" style="margin-top:18px;padding:16px"><strong>List your tool</strong><p style="font-size:.9rem;margin:6px 0 10px">Free, Fast-Track and Featured options.</p><a class="btn btn-sm btn-primary btn-block" href="submit.html">Submit</a></div>
</aside>
<div><div class="toolbar"><label class="sr-only" for="q">Search</label><input id="q" type="search" placeholder="Search by name, use case or tag…  (⌘K)">
<label class="sr-only" for="sort">Sort</label><select id="sort" style="max-width:220px"><option value="rel">Sort: Recommended</option><option value="az">Name A–Z</option><option value="za">Name Z–A</option><option value="cat">Category</option><option value="free">Free first</option></select>
<span class="result-count" id="dir-count"></span></div>
<div class="grid g3" id="dir-grid"></div>
{ad("inArticle")}
<div class="card" style="margin-top:8px"><h3>Can't decide? Let an expert choose — and implement.</h3><p>Describe your goal and we'll match you with a specialist who has shipped it before. Free for businesses.</p><p style="margin-top:12px"><a class="btn btn-primary" href="get-matched.html">Get matched free</a></p></div>
</div></div></div>'''
    return page("directory.html", "AI & Digital Tools Directory", "Search and filter a curated directory of AI tools, website builders, SEO, marketing, design, automation and e-commerce software.",
                body, "directory.html", {"@context": "https://schema.org", "@type": "CollectionPage", "name": "AI & Digital Tools Directory"}, ["tools-data.js", "directory.js"])


def free_tools():
    feats = [("500-2000", "CMS / blog"), ("1500-5000", "Online payments / store"), ("1000-4000", "Multilingual"),
             ("1500-6000", "Fully custom design"), ("500-2000", "SEO setup & analytics"), ("1000-6000", "Integrations / API"),
             ("1000-5000", "AI chatbot or assistant"), ("800-3000", "Copywriting")]
    fb = "".join(f'<label class="check"><input type="checkbox" data-add="{r}"> {t}</label>' for r, t in feats)
    body = f'''
<section class="hero" style="padding-bottom:24px"><div class="container"><div class="breadcrumbs"><a href="index.html">Home</a> / Free tools</div>
<span class="eyebrow">Free tools</span><h1>Free digital business calculators</h1><p class="lead">Private, instant, no sign-up. Everything runs in your browser.</p>
<div class="chips"><a class="chip" href="#cost">Website cost</a><a class="chip" href="#roas">Ad ROI / ROAS</a><a class="chip" href="#serp">SERP preview</a><a class="chip" href="#utm">UTM builder</a><a class="chip" href="#ai">AI API cost</a></div></div></section>
<div class="container grid" style="gap:28px">
<div class="card" id="cost"><h2>Website cost estimator</h2><p>Indicative 2026 ranges based on typical freelancer, studio and agency pricing. Use it to set a realistic budget before you brief anyone.</p>
<div class="split" style="margin-top:18px;align-items:start"><form class="form" id="calc-cost" onsubmit="return false">
<div class="form-row"><label class="fl">Site type<select id="cc-type"><option value="landing">Landing page</option><option value="business" selected>Business website</option><option value="content">Content / media site</option><option value="store">E-commerce store</option><option value="app">Web app / SaaS</option></select></label>
<label class="fl">Who builds it<select id="cc-who"><option value="freelancer">Freelancer</option><option value="studio" selected>Small studio</option><option value="agency">Full-service agency</option></select></label></div>
<label class="fl">Number of pages<input id="cc-pages" type="number" min="1" max="500" value="8"></label>
<fieldset style="border:0;padding:0;display:grid;gap:8px"><legend class="fl" style="margin-bottom:8px">Features</legend>{fb}</fieldset></form>
<div><div class="calc-out" id="cc-out"></div><a class="btn btn-primary btn-block" id="cc-cta" href="get-matched.html?service=website" style="margin-top:14px">Get quotes in this range — free</a></div></div></div>
{ad("inArticle")}
<div class="card" id="roas"><h2>Ad ROI &amp; ROAS calculator</h2><p>Model a Google, Meta or TikTok campaign before you spend.</p>
<div class="split" style="margin-top:18px;align-items:start"><form class="form" id="calc-roas" onsubmit="return false">
<div class="form-row"><label class="fl">Monthly ad spend ($)<input id="r-spend" type="number" value="3000" min="0"></label><label class="fl">Avg. cost per click ($)<input id="r-cpc" type="number" value="1.8" step="0.01" min="0"></label></div>
<div class="form-row"><label class="fl">Conversion rate (%)<input id="r-cr" type="number" value="2.5" step="0.1" min="0"></label><label class="fl">Avg. order / lead value ($)<input id="r-aov" type="number" value="120" min="0"></label></div>
<label class="fl">Gross margin (%)<input id="r-margin" type="number" value="45" min="1" max="100"></label></form>
<div><div class="calc-out" id="r-out"></div><a class="btn btn-primary btn-block" href="get-matched.html?service=ads" style="margin-top:14px">Get a PPC specialist to beat these numbers</a></div></div></div>
<div class="card" id="serp"><h2>Google SERP snippet preview</h2><p>Preview how your title and meta description may appear in search results.</p>
<div class="split" style="margin-top:18px;align-items:start"><form class="form" id="calc-serp" onsubmit="return false">
<label class="fl">Page URL<input id="s-url" type="url" value="https://example.com/ai-tools"></label>
<label class="fl">Title tag<input id="s-title" value="Best AI Tools for Small Business (2026 Guide)"><span id="s-tm" class="meter"></span></label>
<label class="fl">Meta description<textarea id="s-desc" style="min-height:90px">Compare the most useful AI tools for writing, design, video and automation — with pricing, pros and cons, and who each one is best for.</textarea><span id="s-dm" class="meter"></span></label></form>
<div><div class="serp" id="s-prev"></div><p class="form-note" style="margin-top:10px">Google may rewrite snippets. Length guidance is approximate (display is pixel-based).</p></div></div></div>
<div class="card" id="utm"><h2>UTM campaign link builder</h2>
<form class="form" id="calc-utm" onsubmit="return false" style="margin-top:14px"><label class="fl">Destination URL<input id="u-url" type="url" value="https://example.com/landing"></label>
<div class="form-row"><label class="fl">Source<input id="u-source" value="newsletter"></label><label class="fl">Medium<input id="u-medium" value="email"></label></div>
<div class="form-row"><label class="fl">Campaign<input id="u-campaign" value="spring launch"></label><label class="fl">Term (optional)<input id="u-term"></label></div>
<label class="fl">Content (optional)<input id="u-content" placeholder="cta-button"></label>
<label class="fl">Your tagged link<input id="u-out" readonly></label><button type="button" class="btn btn-ghost" id="u-copy">Copy link</button></form></div>
<div class="card" id="ai"><h2>AI API cost estimator</h2><p>Enter your provider's current per-million-token prices (check their pricing page — defaults are examples only).</p>
<div class="split" style="margin-top:18px;align-items:start"><form class="form" id="calc-ai" onsubmit="return false">
<div class="form-row"><label class="fl">Input tokens / request<input id="a-in" type="number" value="1500" min="0"></label><label class="fl">Output tokens / request<input id="a-out" type="number" value="500" min="0"></label></div>
<label class="fl">Requests per day<input id="a-req" type="number" value="1000" min="0"></label>
<div class="form-row"><label class="fl">Price per 1M input tokens ($)<input id="a-pin" type="number" value="3" step="0.01" min="0"></label><label class="fl">Price per 1M output tokens ($)<input id="a-pout" type="number" value="15" step="0.01" min="0"></label></div></form>
<div><div class="calc-out" id="a-res"></div><a class="btn btn-primary btn-block" href="get-matched.html?service=ai" style="margin-top:14px">Get an AI automation expert</a></div></div></div>
<div class="card featured"><h3>Want a tool built for your audience?</h3><p>Sponsor a branded calculator on Core.Digital — it's one of our highest-engagement placements.</p><p style="margin-top:12px"><a class="btn btn-primary" href="advertise.html">Sponsor a tool</a></p></div>
</div>'''
    schema = {"@context": "https://schema.org", "@type": "WebApplication", "name": "Core.Digital Free Tools", "applicationCategory": "BusinessApplication", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}}
    return page("free-tools.html", "Free Website Cost, ROAS, SERP, UTM & AI Cost Calculators", "Free calculators: website cost estimator, ad ROI/ROAS calculator, Google SERP preview, UTM builder and AI API cost estimator.",
                body, "free-tools.html", schema, ["calculators.js"])


def videos():
    body = f'''
<section class="hero" style="padding-bottom:24px"><div class="container"><div class="breadcrumbs"><a href="index.html">Home</a> / Videos</div>
<span class="eyebrow">Video library</span><h1>Learn AI, code &amp; SEO — the best explainers in one place</h1>
<p class="lead">A curated library of the clearest videos on the internet. Click to play (privacy-enhanced mode, nothing loads until you press play).</p>
<div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-accent" data-yt-channel hidden target="_blank" rel="noopener">▶ Subscribe on YouTube</a><a class="btn btn-ghost" href="advertise.html#video">Sponsor a video</a></div></div></section>
<div class="container">
<h2>Artificial intelligence</h2><div class="grid g3">{video_cards(cat="AI")}</div>
{ad("inArticle")}
<h2 style="margin-top:40px">Code &amp; web development</h2><div class="grid g3">{video_cards(cat="Code")}</div>
<h2 style="margin-top:40px">SEO &amp; search</h2><div class="grid g3">{video_cards(cat="SEO")}</div>
<div class="grid g2" style="margin-top:40px">
<div class="card"><h3>Creators: get your video featured</h3><p>Made a great tutorial on AI, websites or marketing? Suggest it for the library.</p>
{form("Video suggestion", field("Video URL", "video_url", "url", placeholder="https://www.youtube.com/watch?v=…") + field("Your email", "email", "email") + field("Why it's great", "notes", "textarea", False), "Suggest video", "Thanks! We review suggestions weekly.")}</div>
<div class="card featured"><h3>Brands: sponsored video integrations</h3><p>Dedicated reviews, walkthroughs and tutorial integrations in our video library and on our channel.</p><p style="margin-top:12px"><a class="btn btn-primary" href="advertise.html#video">See video packages</a></p></div>
</div></div>'''
    return page("videos.html", "Video Library: AI, Coding & SEO Explainers", "Curated videos explaining AI, large language models, web development and SEO — hand-picked from the best educators.", body, "videos.html")


def get_matched():
    svc = "".join(f'<label class="opt"><input type="radio" name="service" value="{k}" required><span>{t}<small>{d}</small></span></label>' for k, t, d in SERVICES)
    bud = "".join(f'<label class="opt"><input type="radio" name="budget" value="{k}" required><span>{t}</span></label>' for k, t in BUDGETS)
    tl = "".join(f'<label class="opt"><input type="radio" name="timeline" value="{t}" required><span>{t}</span></label>' for t in ["ASAP (this month)", "1–3 months", "3–6 months", "Just researching"])
    wiz = f'''
<div class="step" data-title="Service" data-auto><h3>What do you need help with?</h3><div class="opt-grid">{svc}</div></div>
<div class="step" data-title="Budget" data-auto><h3>What's your budget?</h3><p class="form-note">A range helps us match you with the right tier — from freelancers to agencies.</p><div class="opt-grid">{bud}</div></div>
<div class="step" data-title="Timeline" data-auto><h3>When do you want to start?</h3><div class="opt-grid">{tl}</div></div>
<div class="step" data-title="Project"><h3>Tell us about the project</h3><div class="form">
{field("Project description", "project", "textarea", True, "Goals, current situation, must-haves, links to examples…")}
<div class="form-row">{field("Company", "company", required=False)}{field("Website", "website", "url", False, "https://")}</div>
<div class="form-row">{select("Company size", "company_size", ["Just me", "2–10", "11–50", "51–200", "200+"], False)}{select("Preferred provider", "provider", ["Freelancer", "Small studio", "Agency", "No preference"], False)}</div></div></div>
<div class="step" data-title="Contact"><h3>Where should we send your matches?</h3><div class="form">
<div class="form-row">{field("Full name", "name")}{field("Work email", "email", "email")}</div>
<div class="form-row">{field("Phone / WhatsApp", "phone", "tel", False)}{field("Country", "country")}</div>
{select("Preferred contact", "contact_pref", ["Email", "Phone", "WhatsApp", "Video call"], False)}
{consent("I agree that Core.Digital may share my brief with up to 5 matched specialists and contact me about it. See our <a href=\"privacy.html\">Privacy Policy</a>.")}</div></div>'''
    body = f'''
<section class="hero" style="padding-bottom:40px"><div class="container split" style="align-items:start">
<div><div class="breadcrumbs"><a href="index.html">Home</a> / Get matched</div><span class="eyebrow">Free for businesses</span>
<h1>Get matched with vetted digital experts</h1>
<p class="lead">Websites, SEO, paid ads, AI automation, e-commerce, apps and branding. Answer 5 quick questions — we hand-review every brief and introduce up to 5 specialists who fit.</p>
<ul class="trust-list" style="margin:24px 0"><li><span><strong>Free &amp; no obligation.</strong> You never pay Core.Digital.</span></li><li><span><strong>Hand-reviewed.</strong> A human reads every brief — no auto-spam blasts.</span></li><li><span><strong>Budget-fit.</strong> From $500 fixes to $50k+ builds.</span></li><li><span><strong>Private.</strong> Your details go only to the specialists we introduce.</span></li><li><span><strong>Fast.</strong> First reply within 1 business day.</span></li></ul>
<div class="card"><h3>How it works</h3><ol style="color:var(--muted);padding-left:1.2em;margin:0"><li>Share your brief (≈2 minutes)</li><li>We shortlist specialists by skill, budget &amp; track record</li><li>You receive up to 5 introductions and proposals</li><li>Choose who to hire — or none at all</li></ol></div></div>
<div class="wizard" id="brief"><div class="progress"><span></span></div><div class="step-label"></div>
{form("Lead: Get Matched brief", wiz + '<div class="wizard-nav"><button type="button" class="btn btn-ghost" data-prev>← Back</button><button type="button" class="btn btn-primary" data-next-step>Continue →</button></div>', "Get my free matches →", "Brief received! We're reviewing it now and will email you within 1 business day.", cls="form").replace('<button class="btn btn-primary" type="submit">', '<button class="btn btn-primary btn-block" type="submit" data-submit>')}
<p class="form-note center" style="margin-top:12px">🔒 Secured submission · No spam · Unsubscribe anytime</p></div>
</div></section>
<section class="section-alt"><div class="container"><div class="center"><span class="eyebrow">For specialists</span><h2>Are you an agency or freelancer?</h2>
<p class="lead">Join the Core.Digital Talent Network to receive pre-qualified project introductions in your niche.</p><p style="margin-top:18px"><a class="btn btn-primary" href="careers.html#talent">Apply to the network</a></p></div></div></section>
<section><div class="container" style="max-width:860px"><h2>Questions</h2>{faq_html([FAQ[1], ("Who are the specialists?", "Independent freelancers, studios and agencies who apply to our Talent Network and are reviewed for portfolio quality, references and communication before they receive introductions."), ("What happens after I submit?", "We read your brief, may ask one or two clarifying questions, and then introduce matched specialists by email. You decide who to talk to."), ("Can I get matched for a small job?", "Yes. Many briefs are fixes, audits or small builds. Choose 'Under $2,500' and we'll match you with a suitable freelancer.")])}</div></section>'''
    return page("get-matched.html", "Get Matched Free with Vetted Website, SEO, Ads & AI Experts",
                "Tell us your project in 2 minutes and get introduced to up to 5 vetted digital specialists — websites, SEO, PPC, AI automation, e-commerce. Free for businesses.",
                body, "get-matched.html", faq_schema([FAQ[1]]))


CHECK = {
    "Website & UX": ["Loads in under 2.5s on mobile (LCP)", "Clear headline says who it's for and what it does", "One primary call-to-action per page", "Mobile layout tested on a real phone", "Contact / lead form works and sends confirmations", "HTTPS everywhere, no mixed content", "404 page links back to key pages", "Accessible colour contrast and alt text", "Trust signals: reviews, logos, guarantees", "Privacy policy and terms present"],
    "SEO": ["Search Console verified and sitemap submitted", "Unique title (30–60 chars) and meta description per page", "One H1 per page matching search intent", "Internal links to money pages from high-traffic posts", "Structured data (Organization, Article, FAQ, Product)", "No accidental noindex / blocked resources", "Core Web Vitals passing", "Content updated in the last 12 months", "Image file sizes compressed, lazy-loaded", "Target keyword clusters mapped to pages", "Backlink profile reviewed for toxic links"],
    "Analytics & tracking": ["GA4 installed with consent", "Conversions (leads, sales) configured as key events", "UTM tags on every campaign link", "Heatmaps on key landing pages", "Monthly dashboard of traffic → leads → revenue"],
    "Ads & acquisition": ["Break-even ROAS / CPA known", "Separate campaigns for brand vs non-brand", "Negative keyword lists maintained", "Landing page matches ad promise", "Retargeting audiences built", "Creative refreshed every 4–6 weeks", "Budget moved weekly to top performers"],
    "Email & retention": ["Lead magnet offered on key pages", "Welcome sequence (3–5 emails)", "Double opt-in or verified list hygiene", "Segments by interest or behaviour", "Clear unsubscribe and sender identity", "Monthly newsletter or content digest"],
    "Monetisation": ["Ads placed where they don't hurt UX (above fold ≤1)", "ads.txt published and correct", "Affiliate links disclosed", "Sponsor / media kit page live", "Donation or membership option", "Upsell from free tool → paid service"],
    "AI & automation": ["Repetitive tasks listed and scored for automation", "Chatbot or FAQ assistant on support pages", "AI content reviewed by a human before publishing", "API costs forecast and capped", "Data privacy reviewed for AI tools", "Team trained on approved AI tools", "Forms auto-routed to CRM"],
}


def checklist():
    n = sum(len(v) for v in CHECK.values())
    blocks = "".join(f'<div class="card"><h3>{esc(k)}</h3>' + "".join(f'<label class="check" style="padding:6px 0"><input type="checkbox"> {esc(i)}</label>' for i in v) + "</div>" for k, v in CHECK.items())
    body = f'''<section class="hero" style="padding-bottom:24px"><div class="container"><div class="breadcrumbs"><a href="index.html">Home</a> / Checklist</div>
<span class="eyebrow">Free resource</span><h1>The Digital Growth Checklist</h1><p class="lead">{n} checks across website, SEO, analytics, ads, email, monetisation and AI. Tick through it, print it, or hand it to your team.</p>
<button class="btn btn-ghost" onclick="window.print()">🖨 Print / save as PDF</button></div></section>
<div class="container grid g2">{blocks}</div>
<div class="container" style="margin-top:28px"><div class="cta-band"><h2>Failed more than 10 checks?</h2><p>Get a specialist to fix them for you. Free matching, no obligation.</p><a class="btn btn-ghost" href="get-matched.html">Get matched free</a></div></div>'''
    return page("checklist.html", "The Digital Growth Checklist (Free)", f"A free {n}-point checklist to audit your website, SEO, analytics, ads, email, monetisation and AI stack.", body)
