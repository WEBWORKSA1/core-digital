/* Core.Digital directory data. Add entries here — the directory, category counts and
   homepage stats update automatically. Fields:
   n name · u url · c category · p pricing (Free|Freemium|Paid|Open source) · d description · t tags
   f: true = Featured (paid placement → shows "Sponsored" badge) · v: true = Verified listing · a: date added */
window.CD_TOOLS = [
  // AI assistants
  {n:"ChatGPT",u:"https://chatgpt.com",c:"AI Assistants",p:"Freemium",d:"OpenAI's general-purpose AI assistant for writing, analysis, coding and research.",t:["chat","writing","research"]},
  {n:"Claude",u:"https://claude.ai",c:"AI Assistants",p:"Freemium",d:"Anthropic's AI assistant for long documents, writing, analysis and coding.",t:["chat","writing","coding"]},
  {n:"Gemini",u:"https://gemini.google.com",c:"AI Assistants",p:"Freemium",d:"Google's multimodal AI assistant connected to Google apps.",t:["chat","google","multimodal"]},
  {n:"Microsoft Copilot",u:"https://copilot.microsoft.com",c:"AI Assistants",p:"Freemium",d:"Microsoft's AI companion across the web, Windows and Microsoft 365.",t:["chat","office"]},
  {n:"Perplexity",u:"https://www.perplexity.ai",c:"AI Assistants",p:"Freemium",d:"Answer engine that searches the web and cites its sources.",t:["search","research"]},
  {n:"Mistral Le Chat",u:"https://chat.mistral.ai",c:"AI Assistants",p:"Freemium",d:"Assistant from French AI lab Mistral with fast responses.",t:["chat","europe"]},
  // Writing
  {n:"Grammarly",u:"https://www.grammarly.com",c:"AI Writing",p:"Freemium",d:"Grammar, clarity and tone suggestions everywhere you write.",t:["editing","grammar"]},
  {n:"Jasper",u:"https://www.jasper.ai",c:"AI Writing",p:"Paid",d:"AI content platform for marketing teams and brand voice.",t:["marketing","copy"]},
  {n:"Copy.ai",u:"https://www.copy.ai",c:"AI Writing",p:"Freemium",d:"AI workflows for go-to-market copy and sales content.",t:["copy","sales"]},
  {n:"QuillBot",u:"https://quillbot.com",c:"AI Writing",p:"Freemium",d:"Paraphrasing, summarising and grammar checking.",t:["paraphrase","students"]},
  {n:"Notion AI",u:"https://www.notion.com/product/ai",c:"AI Writing",p:"Paid",d:"AI writing, search and summaries inside Notion workspaces.",t:["docs","notes"]},
  // Image
  {n:"Midjourney",u:"https://www.midjourney.com",c:"AI Image",p:"Paid",d:"High-aesthetic AI image generation from text prompts.",t:["art","images"]},
  {n:"Adobe Firefly",u:"https://firefly.adobe.com",c:"AI Image",p:"Freemium",d:"Adobe's generative AI for images and design, built for commercial use.",t:["design","images"]},
  {n:"Leonardo.Ai",u:"https://leonardo.ai",c:"AI Image",p:"Freemium",d:"Image generation and editing for game assets and creative work.",t:["art","assets"]},
  {n:"Ideogram",u:"https://ideogram.ai",c:"AI Image",p:"Freemium",d:"Text-to-image model known for rendering typography in images.",t:["typography","images"]},
  {n:"Remove.bg",u:"https://www.remove.bg",c:"AI Image",p:"Freemium",d:"Removes image backgrounds automatically in seconds.",t:["editing","ecommerce"]},
  // Video
  {n:"Runway",u:"https://runwayml.com",c:"AI Video",p:"Freemium",d:"Generative video and AI editing tools for creators.",t:["video","generation"]},
  {n:"Synthesia",u:"https://www.synthesia.io",c:"AI Video",p:"Paid",d:"AI avatar videos for training, sales and communication.",t:["avatars","training"]},
  {n:"HeyGen",u:"https://www.heygen.com",c:"AI Video",p:"Freemium",d:"AI avatars, video translation and talking-head videos.",t:["avatars","translation"]},
  {n:"Descript",u:"https://www.descript.com",c:"AI Video",p:"Freemium",d:"Edit video and podcasts by editing the transcript.",t:["podcast","editing"]},
  {n:"CapCut",u:"https://www.capcut.com",c:"AI Video",p:"Freemium",d:"Video editor with templates and AI effects for social content.",t:["social","editing"]},
  {n:"OpusClip",u:"https://www.opus.pro",c:"AI Video",p:"Freemium",d:"Turns long videos into short, shareable clips.",t:["shorts","repurpose"]},
  // Audio
  {n:"ElevenLabs",u:"https://elevenlabs.io",c:"AI Audio",p:"Freemium",d:"Realistic AI voices, dubbing and text-to-speech.",t:["voice","tts"]},
  {n:"Suno",u:"https://suno.com",c:"AI Audio",p:"Freemium",d:"Generates songs with vocals from text prompts.",t:["music"]},
  {n:"Otter.ai",u:"https://otter.ai",c:"AI Audio",p:"Freemium",d:"Meeting transcription, notes and summaries.",t:["meetings","transcription"]},
  // Coding
  {n:"GitHub Copilot",u:"https://github.com/features/copilot",c:"Developer Tools",p:"Freemium",d:"AI pair programmer inside your editor and GitHub.",t:["coding","ide"]},
  {n:"Cursor",u:"https://cursor.com",c:"Developer Tools",p:"Freemium",d:"AI-first code editor built on VS Code.",t:["coding","ide"]},
  {n:"Replit",u:"https://replit.com",c:"Developer Tools",p:"Freemium",d:"Build, run and deploy apps in the browser with an AI agent.",t:["coding","hosting"]},
  {n:"v0",u:"https://v0.app",c:"Developer Tools",p:"Freemium",d:"Generates React/Next.js UI and apps from prompts.",t:["ui","react"]},
  {n:"Bolt.new",u:"https://bolt.new",c:"Developer Tools",p:"Freemium",d:"Prompt, run and deploy full-stack web apps in the browser.",t:["apps","no-code"]},
  {n:"Lovable",u:"https://lovable.dev",c:"Developer Tools",p:"Freemium",d:"Build web apps by chatting with AI.",t:["apps","no-code"]},
  {n:"VS Code",u:"https://code.visualstudio.com",c:"Developer Tools",p:"Free",d:"Free, extensible source-code editor from Microsoft.",t:["ide"]},
  // Website builders & hosting
  {n:"WordPress.org",u:"https://wordpress.org",c:"Website Builders",p:"Open source",d:"The open-source CMS powering a large share of the web.",t:["cms","blog"]},
  {n:"Webflow",u:"https://webflow.com",c:"Website Builders",p:"Freemium",d:"Visual website builder with a CMS for designers.",t:["design","cms"]},
  {n:"Framer",u:"https://www.framer.com",c:"Website Builders",p:"Freemium",d:"Design and publish fast marketing sites with AI help.",t:["landing","design"]},
  {n:"Wix",u:"https://www.wix.com",c:"Website Builders",p:"Freemium",d:"Drag-and-drop website builder for small businesses.",t:["smb","builder"]},
  {n:"Squarespace",u:"https://www.squarespace.com",c:"Website Builders",p:"Paid",d:"Template-driven sites, stores and domains.",t:["templates","smb"]},
  {n:"GitHub Pages",u:"https://pages.github.com",c:"Hosting & Domains",p:"Free",d:"Free static site hosting straight from a GitHub repository.",t:["static","free"]},
  {n:"Netlify",u:"https://www.netlify.com",c:"Hosting & Domains",p:"Freemium",d:"Deploy platform for static and Jamstack sites.",t:["static","deploy"]},
  {n:"Vercel",u:"https://vercel.com",c:"Hosting & Domains",p:"Freemium",d:"Frontend cloud for Next.js and modern web apps.",t:["nextjs","deploy"]},
  {n:"Cloudflare",u:"https://www.cloudflare.com",c:"Hosting & Domains",p:"Freemium",d:"CDN, DNS, security and Pages hosting.",t:["cdn","dns","security"]},
  {n:"Namecheap",u:"https://www.namecheap.com",c:"Hosting & Domains",p:"Paid",d:"Domain registrar with hosting and SSL.",t:["domains"]},
  {n:"Porkbun",u:"https://porkbun.com",c:"Hosting & Domains",p:"Paid",d:"Domain registrar known for low pricing and free WHOIS privacy.",t:["domains"]},
  // SEO
  {n:"Google Search Console",u:"https://search.google.com/search-console",c:"SEO",p:"Free",d:"Monitor indexing, queries and performance in Google Search.",t:["google","indexing"]},
  {n:"Ahrefs",u:"https://ahrefs.com",c:"SEO",p:"Freemium",d:"Backlink, keyword and site audit toolset.",t:["backlinks","keywords"]},
  {n:"Semrush",u:"https://www.semrush.com",c:"SEO",p:"Paid",d:"SEO, PPC and competitive research suite.",t:["keywords","competitors"]},
  {n:"Screaming Frog",u:"https://www.screamingfrog.co.uk/seo-spider/",c:"SEO",p:"Freemium",d:"Desktop crawler for technical SEO audits.",t:["audit","technical"]},
  {n:"Yoast SEO",u:"https://yoast.com",c:"SEO",p:"Freemium",d:"On-page SEO plugin for WordPress.",t:["wordpress","on-page"]},
  {n:"PageSpeed Insights",u:"https://pagespeed.web.dev",c:"SEO",p:"Free",d:"Measure Core Web Vitals and page performance.",t:["speed","cwv"]},
  // Marketing & email
  {n:"HubSpot",u:"https://www.hubspot.com",c:"Marketing & CRM",p:"Freemium",d:"CRM with marketing, sales and service hubs.",t:["crm","email"]},
  {n:"Mailchimp",u:"https://mailchimp.com",c:"Marketing & CRM",p:"Freemium",d:"Email marketing and automation for small businesses.",t:["email"]},
  {n:"beehiiv",u:"https://www.beehiiv.com",c:"Marketing & CRM",p:"Freemium",d:"Newsletter platform with growth and monetisation tools.",t:["newsletter","ads"]},
  {n:"Kit",u:"https://kit.com",c:"Marketing & CRM",p:"Freemium",d:"Email marketing for creators (formerly ConvertKit).",t:["newsletter","creators"]},
  {n:"Buffer",u:"https://buffer.com",c:"Marketing & CRM",p:"Freemium",d:"Plan and schedule social media posts.",t:["social","scheduling"]},
  {n:"Google Ads",u:"https://ads.google.com",c:"Marketing & CRM",p:"Paid",d:"Search, display and YouTube advertising.",t:["ppc","ads"]},
  // Design
  {n:"Figma",u:"https://www.figma.com",c:"Design",p:"Freemium",d:"Collaborative interface design and prototyping.",t:["ui","prototype"]},
  {n:"Canva",u:"https://www.canva.com",c:"Design",p:"Freemium",d:"Easy graphic design with templates and AI features.",t:["graphics","social"]},
  {n:"Photopea",u:"https://www.photopea.com",c:"Design",p:"Free",d:"Browser-based image editor supporting PSD files.",t:["photo","editor"]},
  {n:"Coolors",u:"https://coolors.co",c:"Design",p:"Freemium",d:"Fast colour palette generator.",t:["colour"]},
  // Productivity & automation
  {n:"Notion",u:"https://www.notion.com",c:"Productivity",p:"Freemium",d:"All-in-one workspace for docs, wikis and projects.",t:["docs","wiki"]},
  {n:"Trello",u:"https://trello.com",c:"Productivity",p:"Freemium",d:"Kanban boards for simple project management.",t:["kanban"]},
  {n:"Asana",u:"https://asana.com",c:"Productivity",p:"Freemium",d:"Work management for teams.",t:["projects"]},
  {n:"Calendly",u:"https://calendly.com",c:"Productivity",p:"Freemium",d:"Scheduling links that end back-and-forth emails.",t:["scheduling"]},
  {n:"Zapier",u:"https://zapier.com",c:"Automation",p:"Freemium",d:"Connect apps and automate workflows without code.",t:["no-code","integrations"]},
  {n:"Make",u:"https://www.make.com",c:"Automation",p:"Freemium",d:"Visual automation builder for complex scenarios.",t:["no-code","integrations"]},
  {n:"n8n",u:"https://n8n.io",c:"Automation",p:"Open source",d:"Fair-code workflow automation you can self-host.",t:["self-host","ai-agents"]},
  // Analytics
  {n:"Google Analytics",u:"https://marketingplatform.google.com/about/analytics/",c:"Analytics",p:"Free",d:"Website and app analytics (GA4).",t:["web","google"]},
  {n:"Microsoft Clarity",u:"https://clarity.microsoft.com",c:"Analytics",p:"Free",d:"Free heatmaps and session recordings.",t:["heatmaps","ux"]},
  {n:"Plausible",u:"https://plausible.io",c:"Analytics",p:"Paid",d:"Lightweight, privacy-friendly web analytics.",t:["privacy"]},
  {n:"Hotjar",u:"https://www.hotjar.com",c:"Analytics",p:"Freemium",d:"Heatmaps, recordings and on-site surveys.",t:["heatmaps","feedback"]},
  // E-commerce
  {n:"Shopify",u:"https://www.shopify.com",c:"E-commerce",p:"Paid",d:"Hosted platform to build and run an online store.",t:["store"]},
  {n:"WooCommerce",u:"https://woocommerce.com",c:"E-commerce",p:"Open source",d:"E-commerce plugin for WordPress.",t:["wordpress","store"]},
  {n:"Gumroad",u:"https://gumroad.com",c:"E-commerce",p:"Freemium",d:"Sell digital products, memberships and courses.",t:["creators","digital products"]},
  {n:"Stripe",u:"https://stripe.com",c:"E-commerce",p:"Paid",d:"Online payments, subscriptions and payment links.",t:["payments"]},
  {n:"Lemon Squeezy",u:"https://www.lemonsqueezy.com",c:"E-commerce",p:"Paid",d:"Merchant of record for selling software and digital goods.",t:["saas","tax"]}
];
