# Core.Digital — Concept, Strategy & Phase-wise Build Prompt

## 1. The idea (and why it wins)

**Core.Digital = "The core of everything digital."**
An AI & digital tools directory, practical guides, free calculators and videos (the traffic engine), plus a **free "Get Matched" service** that sends businesses to vetted website, SEO, ads, AI and e-commerce specialists (the money engine).

### Why this beats the alternatives for this domain

| Option | Traffic potential | Revenue per visitor | Moat | Verdict |
|---|---|---|---|---|
| Pure digital-marketing blog | High, crowded | Low (AdSense only) | Weak | ❌ |
| Agency site (sell services yourself) | Low | High | Needs a team | ❌ solo |
| **Tools directory + guides + matching (chosen)** | **High (programmatic + evergreen)** | **High (ads + listings + leads)** | **Data, reviews, supply network** | ✅ |
| SaaS product | Uncertain | High | Build cost | Later, as an add-on |

**The core logic:** one visitor can pay you five ways — AdSense impression → affiliate click → newsletter signup → lead-gen brief → sponsor exposure. B2B/software/marketing topics carry some of the highest AdSense CPCs, and a single qualified agency lead typically sells for far more than thousands of ad impressions.

### Revenue model (launch pricing benchmarked against the 46 sites reviewed)

| Stream | Launch price | Benchmarks observed |
|---|---|---|
| Fast-Track listing | $49 one-time | topai.tools $47 · Toolify $99 |
| Featured listing | $149/mo | TAAFT Highlight $99/mo · topai $229/7 days · BetaList $199/mo |
| Verified + Review | $299 one-time | Futurepedia $247–$497 · TAAFT $437 |
| Newsletter sponsor | from $250/issue | Rundown / Superhuman sell main, secondary and takeover slots |
| Job post | $99–$149 / 30 days | WWR $299 · RemoteOK $447 |
| Lead-gen matching | $50–$300 per qualified lead, or agency membership | Clutch, DesignRush, Sortlist models |
| Display ads | AdSense (config switch) | — |
| Donations / supporters | $5 / $25 / $100 monthly | Buy Me a Coffee, Ko-fi, Open Collective |
| Contest sponsorship | $1,500 / contest | DEV challenges, Devpost |

### 12-month target model (conservative, to validate)

| Month | Monthly visits | AdSense ($8 RPM) | Listings | Leads sold | Sponsors | Total/mo |
|---|---|---|---|---|---|---|
| 3 | 5k | $40 | 4 × $49 | 5 × $75 | $0 | ~$611 |
| 6 | 25k | $200 | 10 Fast-Track + 3 Featured | 20 × $100 | $500 | ~$3.6k |
| 12 | 100k | $800 | 25 Fast-Track + 10 Featured | 60 × $120 | $2,500 | ~$13.2k |

The model depends on the lead-gen side. AdSense alone at 100k visits is under $1k/month; the leads carry the rest. The single metric that decides success is **qualified briefs per month**.

---

## 2. Benchmark summary (sites reviewed)

We fetched and reviewed 46 of the 50 sites attempted. The Verge, Wired and Moz blocked fetching, and AI Tools Directory returned an empty JS page. Reviewed sites include:

- **AI tool directories:** TAAFT, Futurepedia, Toolify, topai.tools
- **Launch and review platforms:** Product Hunt, G2, Capterra, GetApp, TrustRadius, AlternativeTo, SaaSworthy, SaaSHub, StackShare, BuiltWith
- **Agency marketplaces:** Clutch, DesignRush, UpCity, GoodFirms, Sortlist, The Manifest, TechBehemoths
- **Media, blogs and newsletters:** TechCrunch, Zapier, HubSpot, Neil Patel, Backlinko, SEJ, Semrush, MarketingProfs, Smashing, CSS-Tricks, DEV, HackerNoon, Indie Hackers, The Rundown, Ben's Bites, Superhuman
- **Deals and launches:** AppSumo, BetaList
- **Job boards:** WWR, RemoteOK
- **Competitions:** Kaggle, Devpost
- **Donation platforms:** Buy Me a Coffee, Ko-fi, Open Collective

**Patterns adopted:**

- ⌘K search
- Category, price and saved filters
- Free, Freemium, Paid and Sponsored badges
- Save/bookmark
- Multi-step lead brief (service → budget → timeline → project → contact) with conversion promises ("free", "hand-reviewed", "up to 5 matches")
- URL-hero lead magnet
- Exit-intent checklist
- Tiered listing pricing
- Media kit with an inquiry form (product, budget, goals)
- Contests with countdown and rules
- Job board with salary field
- Transparent donation allocation
- Labelled sponsored placements
- Dark-first UI with a single gradient accent
- FAQ, Article, Breadcrumb and SearchAction schema

---

## 3. Phase-wise build prompt

Paste each phase into your AI builder in order. Every phase must keep the **global rules**.

### GLOBAL RULES (include with every phase)
```
Project: Core.Digital — static, responsive website (HTML/CSS/vanilla JS), hosted free on GitHub Pages.
- Brand: "Core.Digital" (always with the dot). Never write "CoreDigital" as one word. Tagline: "The core of everything digital."
- Every page, very top: a full-width bar reading exactly
  "Contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership"
  linked to https://web.works/contact (new tab).
- ONE inbox for all forms: [OWNER_EMAIL]. It must NEVER appear in HTML, text, or links.
  Store it obfuscated (base64 parts) in assets/js/config.js; build the FormSubmit AJAX endpoint
  and any mailto only at runtime on click/submit. Every form: honeypot, consent checkbox, inline success state.
- No frameworks, no build step required to serve. Relative links only (works under /core-digital/ and on a custom domain).
- Dark-first design with light toggle; WCAG AA contrast; mobile-first with no horizontal scroll at 360px.
- All monetisation IDs (AdSense, GA4, Stripe/PayPal/BMC/Ko-fi links, YouTube channel) live in config.js; empty = graceful fallback.
- Include trademark/copyright disclosure in the footer and a full /trademark.html page.
```

### Phase 1 — Foundation & design system
```
Create the repo structure: /assets/css/style.css, /assets/js/{config,app}.js, /assets/img, /build (Python generator).
Design tokens: bg #0a0e1a, surface #131a2e, brand #7c6cff→#22d3ee gradient, accent #ff6b8b; Inter + Space Grotesk.
Components: top interest bar, sticky header (logo, 7 nav links, Submit tool, Get matched, theme toggle, mobile menu),
buttons, cards, badges (free/freemium/paid/sponsored), chips, forms, multi-step wizard, pricing cards,
FAQ accordion, ad slots, video facade, modal, cookie banner, toast, footer (4 link columns + newsletter + legal lines).
A Python generator (build/build.py) renders all pages from shared header/footer so every page stays consistent.
```

### Phase 2 — Traffic engine
```
1. Homepage: hero + ⌘K search → directory, category chips with counts, live stats, featured tools grid,
   quick lead brief, latest guides, free-tools strip, 3 videos, contests/careers/support cards,
   sponsor CTA band, newsletter + FAQ (FAQPage schema), WebSite SearchAction schema.
2. Directory: data file (tools-data.js) with 75+ real tools across 15 categories; filters (price, category, saved),
   sort (recommended/A–Z/category/free-first), search with URL sync, save to localStorage,
   sponsored-first but always labelled, outbound links with ?ref=core.digital and rel="nofollow noopener (sponsored)".
3. Guides hub + 6 original long-form guides with TOC, in-article ad, share buttons, newsletter box,
   related guides, Article + Breadcrumb schema.
4. Free tools: website cost estimator, ad ROI/ROAS, SERP preview, UTM builder, AI API cost estimator —
   each ends with a prefilled Get Matched CTA (e.g. ?service=website&budget=10k-25k).
5. Video library: curated YouTube facades (thumbnail until click, youtube-nocookie), categories, suggestion form,
   sponsor CTA, Subscribe button driven by config.
6. Growth Checklist (52 checks, printable) as lead magnet + exit-intent modal.
```

### Phase 3 — Lead generation (the money engine)
```
Get Matched page: 5-step wizard (Service cards → Budget → Timeline → Project details → Contact + consent),
progress bar, auto-advance on single-choice steps, URL prefill, trust list, "How it works", FAQ,
success message, GA4 generate_lead event. Mirror a compact quick-brief on the homepage.
Supply side: Talent Network application (freelancers/agencies: service, project size, case studies).
Route every submission to the single hidden inbox via FormSubmit AJAX with _subject tags
("[Core.Digital] Lead: …") so the inbox can be filtered by form type.
```

### Phase 4 — Monetisation surfaces
```
- Submit a Tool: Free / Fast-Track $49 / Featured $149 mo / Verified $299; submission form; guidelines; FAQ.
- Advertise: media kit — 6 packages (Directory Featured, Newsletter, Sitewide Banner, Sponsored Guide,
  Video Integration, Contest Title Sponsor) + inquiry form (package, budget, goals).
- Support/Donate: $5/$25/$100 monthly + one-time; allocation bars (operations, content, marketing, hiring,
  contests); payment buttons auto-appear when links are set in config; pledge form fallback.
- Contests: 3 contest cards with planned prizes, live countdown, entry form, official rules, Event schema.
- Careers: 6 remote roles + application form, Talent Network, paid job posts ($99/$149).
- AdSense: data-ad slots render real units when publisher + slot IDs are set; otherwise house ads that sell
  sponsorship. ads.txt template at the root.
```

### Phase 5 — Trust, legal, SEO
```
Pages: About, Contact (form + web.works button + click-to-email that never renders the address), Newsletter,
Privacy (GDPR/CCPA/PIPEDA/Law 25/DPDP + Google ads cookie wording), Terms, Disclaimer & Affiliate Disclosure,
Trademark & Copyright (no affiliation with any "Core Digital"/"CoreDigital" entity), Cookies, 404.
SEO: unique titles/descriptions, canonical, OG/Twitter image, sitemap.xml, robots.txt, manifest,
JSON-LD everywhere, fast (no framework, lazy video), cookie consent gating GA4.
```

### Phase 6 — Deploy, verify, launch
```
- Verify: no occurrence of the inbox address in any served file; no broken internal links; no horizontal
  overflow at 390px; zero console errors; wizard submits the correct payload.
- Push to github.com/webworksa1/core-digital (main + gh-pages); GitHub Pages serves from gh-pages root.
- Submit the first form yourself → click FormSubmit's activation email → optionally paste its random alias
  into config.formAlias.
- Custom domain: add a CNAME file containing core.digital, point DNS (4 A records to GitHub Pages IPs:
  185.199.108.153 / .109.153 / .110.153 / .111.153, plus CNAME www → webworksa1.github.io), enable HTTPS,
  set BASE_URL in build/layout.py to https://core.digital/ and rebuild.
- Apply for AdSense after ~20–30 quality pages and steady traffic; add GA4; submit sitemap to Search Console.
```

### Phase 7 — Scale (post-launch roadmap)
```
- Programmatic SEO: /alternatives/{tool}, /compare/{a}-vs-{b}, /best/{category}, /hire/{service}-{city}.
- Tool detail pages with reviews/ratings; upvotes & monthly leaderboard; deals section (affiliate).
- Stripe Payment Links for listings/jobs/donations; beehiiv newsletter with ad network.
- Agency profiles + paid membership; lead scoring and per-lead pricing.
- YouTube channel: weekly "5 tools in 5 minutes" → embed on tool pages (dual monetisation).
- Localised hubs (India, Canada, UK) for high-intent "hire X in {city}" queries.
```
