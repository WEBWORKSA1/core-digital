"""Original editorial guides. Each: slug, title, desc, cat, read, date, toc [(id, heading)], html."""

ARTICLES = [
{
"slug": "guide-choose-ai-tools.html", "cat": "AI", "read": 7, "date": "2026-09-22",
"title": "How to Choose AI Tools for Your Business: A 7-Point Scorecard",
"desc": "Stop collecting AI subscriptions. Use this seven-point scorecard to pick tools that actually save time and money.",
"html": """
<p>Most teams don't have an AI problem — they have an AI <em>subscription</em> problem. A dozen tools, overlapping features, and no one can say which ones pay for themselves. The fix is a simple scoring habit applied before anyone enters a card number.</p>
<h2 id="job">1. Start with the job, not the tool</h2>
<p>Write the task in one sentence: <em>“Turn a 45-minute sales call into a CRM note and follow-up email.”</em> If you can't write the sentence, you're not ready to buy. Tools bought for vague goals (“use AI for marketing”) are the ones that get cancelled three months later.</p>
<h2 id="score">2. Score every candidate on 7 criteria</h2>
<table><thead><tr><th>Criterion</th><th>Question to ask</th><th>Weight</th></tr></thead><tbody>
<tr><td>Output quality</td><td>Does it beat your current process on 5 real examples?</td><td>25%</td></tr>
<tr><td>Time saved</td><td>Minutes saved per task × tasks per month</td><td>20%</td></tr>
<tr><td>Integration</td><td>Does it plug into the apps you already use?</td><td>15%</td></tr>
<tr><td>Data &amp; privacy</td><td>Is your data used for training? Can you opt out? Where is it stored?</td><td>15%</td></tr>
<tr><td>Total cost</td><td>Seats + usage + setup time at your real volume</td><td>10%</td></tr>
<tr><td>Learning curve</td><td>Can a new teammate get value in a day?</td><td>10%</td></tr>
<tr><td>Vendor risk</td><td>Export options, pricing stability, company track record</td><td>5%</td></tr></tbody></table>
<p>Score each 1–5, multiply by weight, and only adopt tools scoring 3.5 or higher. It takes 20 minutes and prevents most bad purchases.</p>
<h2 id="test">3. Run a 7-day real-work trial</h2>
<p>Demos are designed to impress. Use the free tier or trial on <strong>real, messy work</strong> — your own documents, your own customers' questions. Keep a simple log: task, minutes before, minutes after, quality (good/fix/redo).</p>
<h2 id="overlap">4. Kill overlap ruthlessly</h2>
<p>General assistants now cover writing, summarising, brainstorming and light analysis. Before adding a specialist writing or summarising tool, check whether the assistant you already pay for does 80% of it. Specialists earn their place on depth: video editing, voice, design, code, SEO data.</p>
<h2 id="roi">5. Calculate ROI in one line</h2>
<blockquote>Monthly value = (minutes saved per task ÷ 60) × tasks per month × loaded hourly cost. If value is under 3× the monthly price, it's a “nice to have”.</blockquote>
<p>Example: saving 20 minutes on 60 tasks at a $40/hour loaded cost is worth $800/month. A $30 tool clears the bar easily; a $400 seat bundle might not.</p>
<h2 id="govern">6. Set three simple rules</h2>
<ul><li><strong>Approved list:</strong> one page listing which tools are allowed for which data.</li><li><strong>Human in the loop:</strong> anything customer-facing gets a human review.</li><li><strong>Quarterly review:</strong> cancel anything nobody used last month.</li></ul>
<h2 id="next">7. Where to start</h2>
<p>Browse the <a href="directory.html">Core.Digital directory</a> by category and save a shortlist, then run the scorecard. If you'd rather have a specialist design and implement your AI workflows, <a href="get-matched.html?service=ai">get matched with an AI automation expert</a> — it's free.</p>
"""},
{
"slug": "guide-website-cost.html", "cat": "Websites", "read": 8, "date": "2026-09-22",
"title": "What Does a Website Really Cost in 2026? (And Where the Money Goes)",
"desc": "Realistic price ranges for landing pages, business sites, stores and web apps — plus the hidden costs nobody quotes.",
"html": """
<p>“How much does a website cost?” has the same answer as “how much does a vehicle cost?” — it depends on whether you need a scooter or a truck. Here's how to size it properly so quotes stop surprising you.</p>
<h2 id="ranges">Typical build ranges</h2>
<table><thead><tr><th>Type</th><th>Freelancer</th><th>Studio</th><th>Agency</th></tr></thead><tbody>
<tr><td>Landing page</td><td>$300–1,600</td><td>$500–2,500</td><td>$800–4,000</td></tr>
<tr><td>Business site (5–15 pages)</td><td>$1,300–5,000</td><td>$2,000–8,000</td><td>$3,000–12,000+</td></tr>
<tr><td>Content / media site</td><td>$2,000–8,000</td><td>$3,000–12,000</td><td>$4,500–18,000+</td></tr>
<tr><td>E-commerce store</td><td>$3,000–16,000</td><td>$5,000–25,000</td><td>$7,500–40,000+</td></tr>
<tr><td>Web app / SaaS MVP</td><td>$10,000–50,000</td><td>$15,000–80,000</td><td>$25,000–150,000+</td></tr></tbody></table>
<p>These are indicative ranges we use in our <a href="free-tools.html#cost">website cost estimator</a>; your market, region and scope will move them.</p>
<h2 id="drivers">What actually drives the price</h2>
<ul><li><strong>Custom design vs template.</strong> A bespoke design system can double design hours.</li><li><strong>Content.</strong> Copywriting, photography and video are often the most underestimated line items.</li><li><strong>Integrations.</strong> CRM, payments, booking, inventory and APIs add testing time.</li><li><strong>Multilingual.</strong> Every language multiplies content and QA.</li><li><strong>Revisions and decision speed.</strong> Slow approvals cost real money.</li></ul>
<h2 id="hidden">The hidden, recurring costs</h2>
<ul><li>Domain renewal and email</li><li>Hosting, CDN and backups</li><li>Plugin/theme or SaaS licences</li><li>Security updates and maintenance (budget roughly 15–20% of build cost per year)</li><li>Content updates, SEO and analytics</li></ul>
<h2 id="save">How to spend less without getting burned</h2>
<ol><li>Write a one-page brief: goals, audience, must-have pages, examples you like, budget range.</li><li>Launch a smaller version first; add features once traffic proves demand.</li><li>Use proven platforms (WordPress, Webflow, Shopify, or a static site) unless you truly need custom.</li><li>Ask for fixed-price milestones with clear acceptance criteria.</li><li>Get 3–5 comparable quotes against the same brief.</li></ol>
<div class="callout"><strong>Shortcut:</strong> send one brief, get matched with up to 5 vetted builders in your budget. <a href="get-matched.html?service=website">Get matched free →</a></div>
"""},
{
"slug": "guide-seo-checklist.html", "cat": "SEO", "read": 9, "date": "2026-09-22",
"title": "SEO Basics That Still Work: A No-Fluff Checklist",
"desc": "Search keeps changing, but these fundamentals keep compounding. A practical checklist for new and growing sites.",
"html": """
<p>Search engines and AI answers change every year, yet the sites that keep winning share the same boring fundamentals: they're crawlable, fast, genuinely useful and clearly structured. Start here before chasing any trick.</p>
<h2 id="found">1. Make sure you can be found</h2>
<ul><li>Verify the site in Google Search Console and Bing Webmaster Tools.</li><li>Submit an XML sitemap; keep robots.txt from blocking important pages.</li><li>Check the Pages/Indexing report for “Crawled – currently not indexed” patterns.</li><li>Use one canonical URL per page (https, with or without www — pick one).</li></ul>
<h2 id="intent">2. Match search intent, page by page</h2>
<p>Every important page should target one main query and satisfy the intent behind it: learn (guide), compare (list or table), do (tool or calculator), or buy (product/service page). If the top results are all comparison tables, a 3,000-word essay won't win.</p>
<h2 id="onpage">3. On-page essentials</h2>
<ul><li>Unique title (roughly 30–60 characters) and meta description (roughly 70–155) — test them in our <a href="free-tools.html#serp">SERP preview tool</a>.</li><li>One descriptive H1, logical H2/H3 structure.</li><li>Descriptive alt text on meaningful images.</li><li>Structured data where it fits: Organization, Article, FAQ, Product, LocalBusiness.</li></ul>
<h2 id="helpful">4. Write content people would bookmark</h2>
<p>Show first-hand experience: screenshots, real numbers, original templates, clear opinions. Put the answer early, then the depth. Update important pages at least yearly and show the date.</p>
<h2 id="speed">5. Speed and experience</h2>
<p>Aim for passing Core Web Vitals: fast Largest Contentful Paint, minimal layout shift and responsive interactions. Compress images, lazy-load below-the-fold media, and avoid heavy scripts you don't need. Check with <a href="https://pagespeed.web.dev" rel="noopener" target="_blank">PageSpeed Insights</a>.</p>
<h2 id="links">6. Internal links and earned links</h2>
<ul><li>Link from your most-visited posts to your money pages with descriptive anchor text.</li><li>Create “linkable” assets: free tools, original data, checklists.</li><li>Pitch those assets to newsletters, communities and journalists — not random link sellers.</li></ul>
<h2 id="measure">7. Measure what matters</h2>
<p>Track queries and clicks in Search Console, conversions in analytics, and review monthly. Tag campaigns with our <a href="free-tools.html#utm">UTM builder</a> so organic and paid traffic stay distinct.</p>
<div class="callout">Want this done for you? <a href="get-matched.html?service=seo">Get matched with a vetted SEO specialist</a> — free for businesses.</div>
"""},
{
"slug": "guide-agency-vs-freelancer.html", "cat": "Hiring", "read": 6, "date": "2026-09-22",
"title": "Digital Agency vs. Freelancer: A Decision Framework",
"desc": "When to hire a freelancer, a small studio or a full-service agency — with the questions that expose the right choice fast.",
"html": """
<p>The wrong hire costs more than money: it costs months. The right choice depends less on budget than on how many skills the project needs and how much management you can give it.</p>
<h2 id="compare">Side-by-side</h2>
<table><thead><tr><th></th><th>Freelancer</th><th>Small studio</th><th>Agency</th></tr></thead><tbody>
<tr><td>Best for</td><td>One clear skill, defined scope</td><td>2–4 skills, mid-size builds</td><td>Multi-channel, ongoing programmes</td></tr>
<tr><td>Cost</td><td>Lowest</td><td>Medium</td><td>Highest</td></tr>
<tr><td>Your management load</td><td>High</td><td>Medium</td><td>Low</td></tr>
<tr><td>Continuity risk</td><td>Single point of failure</td><td>Moderate</td><td>Low</td></tr>
<tr><td>Speed to start</td><td>Fast</td><td>Fast–medium</td><td>Slower (onboarding)</td></tr></tbody></table>
<h2 id="questions">Five questions that decide it</h2>
<ol><li><strong>How many distinct skills does the project need?</strong> One → freelancer. Three or more → studio or agency.</li><li><strong>Who will project-manage?</strong> If nobody on your side has time, pay for an agency's PM layer.</li><li><strong>Is it a project or a programme?</strong> One-off builds suit freelancers; always-on SEO/ads suit teams.</li><li><strong>What happens if they disappear?</strong> Ask for documentation and admin access from day one.</li><li><strong>What does success look like in 90 days?</strong> Anyone who can't answer this in the proposal is guessing.</li></ol>
<h2 id="red">Red flags in proposals</h2>
<ul><li>Guaranteed rankings or “#1 on Google”.</li><li>No named person responsible for your account.</li><li>They keep ownership of your domain, ad accounts or analytics.</li><li>Vague deliverables (“SEO optimisation”) with no measurable outputs.</li></ul>
<h2 id="green">Green flags</h2>
<ul><li>Relevant case studies with real numbers and references you can call.</li><li>A paid discovery phase for complex projects.</li><li>Clear milestones, acceptance criteria and a handover plan.</li></ul>
<div class="callout">Describe your project once and we'll match you with the right tier — freelancer, studio or agency. <a href="get-matched.html">Start your free brief →</a></div>
"""},
{
"slug": "guide-newsletter-playbook.html", "cat": "Growth", "read": 7, "date": "2026-09-22",
"title": "Building a Newsletter That Pays: The Practical Playbook",
"desc": "How to grow an email list from zero and turn it into sponsorship, affiliate and product revenue.",
"html": """
<p>An email list is the one audience channel you own. Algorithms change; your list comes with you. Here's a pragmatic path from zero subscribers to a newsletter that funds itself.</p>
<h2 id="position">1. Position it in one line</h2>
<p>“A 5-minute Tuesday briefing on AI tools for small agencies” beats “my thoughts on tech”. Specific audience + specific promise + specific cadence.</p>
<h2 id="platform">2. Pick a platform with monetisation built in</h2>
<p>Platforms like beehiiv, Kit, Substack and Mailchimp differ on ad networks, referral programmes, paid subscriptions and pricing. Choose based on how you plan to earn, not just the editor.</p>
<h2 id="grow">3. Growth loops that work</h2>
<ul><li><strong>Lead magnets:</strong> a checklist, template or calculator offered on relevant pages (like our <a href="checklist.html">Growth Checklist</a>).</li><li><strong>Content upgrades:</strong> a bonus resource inside your best-performing articles.</li><li><strong>Referrals:</strong> reward subscribers for sharing.</li><li><strong>Cross-promotions:</strong> swap recommendations with newsletters of similar size.</li><li><strong>Exit-intent and inline forms</strong> on high-traffic pages.</li></ul>
<h2 id="money">4. Five ways a newsletter earns</h2>
<table><thead><tr><th>Model</th><th>When it works</th></tr></thead><tbody>
<tr><td>Direct sponsorships</td><td>Clear niche audience; sold per issue or per month</td></tr>
<tr><td>Ad networks</td><td>Early stage, when you don't have time to sell</td></tr>
<tr><td>Affiliate recommendations</td><td>You genuinely use and review the products</td></tr>
<tr><td>Paid tier</td><td>Premium data, templates or community</td></tr>
<tr><td>Your own products/services</td><td>Highest margin — the list is your sales channel</td></tr></tbody></table>
<h2 id="metrics">5. Metrics sponsors will ask for</h2>
<p>Subscribers, open rate, click rate, audience composition (roles, industries, regions) and past sponsor results. Publish them on a simple media kit page — like our <a href="advertise.html">advertise page</a>.</p>
<h2 id="trust">6. Protect trust</h2>
<p>Label sponsored content, disclose affiliate links, keep the unsubscribe link obvious, and never sell the list. Trust is the asset sponsors are paying for.</p>
<div class="callout">Get the <a href="newsletter.html">Core Brief</a> free — and see how we do it.</div>
"""},
{
"slug": "guide-adsense-rpm.html", "cat": "Monetisation", "read": 8, "date": "2026-09-22",
"title": "Ad-Supported Websites: How AdSense Revenue Works and How to Raise RPM",
"desc": "RPM, CPC, CTR and viewability explained — plus the levers that raise ad revenue without wrecking user experience.",
"html": """
<p>Display ads remain the simplest way to monetise traffic, but most sites leave money on the table because they misunderstand the maths. Here's the model and the levers.</p>
<h2 id="terms">The vocabulary</h2>
<ul><li><strong>Page RPM</strong> — estimated earnings per 1,000 page views. The number that matters most.</li><li><strong>CPC</strong> — what advertisers pay per click; driven by the value of your topic and audience.</li><li><strong>CTR</strong> — percentage of ad impressions that get clicked.</li><li><strong>Viewability</strong> — share of ads actually seen on screen.</li></ul>
<blockquote>Revenue ≈ page views ÷ 1,000 × page RPM. Double RPM or double traffic — the effect is the same, but RPM is often the faster lever.</blockquote>
<h2 id="levers">Levers that raise RPM</h2>
<ol><li><strong>Topic value.</strong> Business software, finance, marketing, insurance and B2B services attract higher-bidding advertisers than entertainment topics.</li><li><strong>Audience geography.</strong> Advertisers in some markets bid more; content for those markets tends to earn more per view.</li><li><strong>Engagement.</strong> Longer sessions and more pages per visit mean more viewable impressions.</li><li><strong>Placement.</strong> In-content and sticky placements usually outperform footer banners; test, don't guess.</li><li><strong>Page speed.</strong> Slow pages lose visitors before ads render; lazy-load below-the-fold units.</li><li><strong>Consent.</strong> In regions that require consent, a compliant consent tool lets personalised ads serve.</li></ol>
<h2 id="policy">Stay policy-safe</h2>
<ul><li>Never click your own ads or ask others to.</li><li>Publish original, substantial content before applying.</li><li>Keep an accurate <code>ads.txt</code> file at your domain root.</li><li>Label ads clearly and don't disguise them as navigation.</li></ul>
<h2 id="beyond">Go beyond display</h2>
<p>The highest-earning content sites stack revenue: display ads + affiliate reviews + sponsorships + lead generation + their own products. A single B2B lead can be worth more than thousands of ad impressions — which is exactly why Core.Digital pairs ads with a <a href="get-matched.html">free matching service</a>.</p>
<div class="callout">Want to reach this audience? <a href="advertise.html">See Core.Digital sponsorship packages →</a></div>
"""},
]
