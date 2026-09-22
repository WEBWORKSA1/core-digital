/* ============================================================
   Core.Digital — SITE CONFIG (edit this one file to go live)
   ============================================================ */
window.CD_CONFIG = {
  siteName: "Core.Digital",

  /* Inbox routing — stored obfuscated so the address never appears on the site.
     Forms are delivered through FormSubmit (free). After the very first form submission,
     FormSubmit emails an activation link to the inbox — click it once.
     Optional hardening: FormSubmit then shows a random alias string; paste it in
     `formAlias` and the address is no longer used on the client at all. */
  _m: ["d2Vid29ya3NhMQ==", "Z21haWwuY29t"],
  formAlias: "",

  /* Google AdSense — paste your publisher id (e.g. "ca-pub-1234567890123456").
     Empty = house ads promoting direct sponsorship are shown in every ad slot. */
  adsenseClient: "",
  adsenseSlots: { header: "", inArticle: "", sidebar: "", footer: "" },

  /* Google Analytics 4 measurement id, e.g. "G-XXXXXXX" (loads only after cookie consent) */
  ga4: "",

  /* YouTube channel URL for the Subscribe buttons (empty = buttons hidden) */
  youtubeChannel: "",

  /* Donation / payment links. Leave empty to fall back to the pledge form. */
  donate: {
    stripe: "",        // Stripe Payment Link
    paypal: "",        // https://www.paypal.com/donate/?hosted_button_id=XXXX
    buymeacoffee: "",  // https://buymeacoffee.com/yourname
    kofi: "",          // https://ko-fi.com/yourname
    githubSponsors: "" // https://github.com/sponsors/yourname
  },

  /* Paid listing / job checkout links (Stripe Payment Links). Empty = inquiry form. */
  checkout: { fastTrack: "", featured: "", verified: "", jobPost: "", jobFeatured: "" },

  /* Next contest deadline (ISO date) for countdowns */
  contestDeadline: "2026-11-30T23:59:00Z",

  /* Curated videos (IDs verified). Add your own channel's videos here. */
  videos: [
    { id: "zjkBMFhNj_g", title: "[1hr Talk] Intro to Large Language Models", by: "Andrej Karpathy", cat: "AI" },
    { id: "aircAruvnKk", title: "But what is a neural network? | Deep learning chapter 1", by: "3Blue1Brown", cat: "AI" },
    { id: "wjZofJX0v4M", title: "Transformers, the tech behind LLMs", by: "3Blue1Brown", cat: "AI" },
    { id: "7xTGNNLPyMI", title: "Deep Dive into LLMs like ChatGPT", by: "Andrej Karpathy", cat: "AI" },
    { id: "kCc8FmEb1nY", title: "Let's build GPT: from scratch, in code, spelled out.", by: "Andrej Karpathy", cat: "Code" },
    { id: "lutawRrVTHw", title: "Welcome to Google Search Central", by: "Google Search Central", cat: "SEO" },
    { id: "xtVMbfX9lbI", title: "The Official Google SEO Starter Guide — Walkthrough", by: "David Quaid", cat: "SEO" },
    { id: "zQnBQ4tB3ZA", title: "TypeScript in 100 Seconds", by: "Fireship", cat: "Code" },
    { id: "cbB3QEwWMlA", title: "Web Assembly (WASM) in 100 Seconds", by: "Fireship", cat: "Code" }
  ]
};
