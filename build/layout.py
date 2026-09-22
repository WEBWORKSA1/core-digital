"""Shared layout for Core.Digital static pages."""
import json, html

BASE_URL = "https://webworksa1.github.io/core-digital/"   # switch to https://core.digital/ after DNS
SITE = "Core.Digital"
INTEREST_URL = "https://web.works/contact"
TODAY = "2026-09-22"

NAV = [
    ("directory.html", "Directory"), ("guides.html", "Guides"), ("free-tools.html", "Free Tools"),
    ("videos.html", "Videos"), ("contests.html", "Contests"), ("careers.html", "Careers"), ("advertise.html", "Advertise"),
]

LOGO = ('<svg viewBox="0 0 40 40" aria-hidden="true"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#7c6cff"/><stop offset=".5" stop-color="#4f8bff"/><stop offset="1" stop-color="#22d3ee"/></linearGradient></defs>'
        '<circle cx="20" cy="20" r="17" fill="none" stroke="url(#lg)" stroke-width="4"/><circle cx="20" cy="20" r="9" fill="none" stroke="url(#lg)" stroke-width="3" opacity=".7"/>'
        '<circle cx="20" cy="20" r="4" fill="url(#lg)"/></svg>')

ICON_SUN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
ICON_MENU = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M3 12h18M3 18h18"/></svg>'


def esc(s):
    return html.escape(str(s), quote=True)


def form(name, inner, button="Send", success=None, extra_attrs="", cls="form"):
    """FormSubmit-backed form. Recipient is resolved at runtime from obfuscated config."""
    s = f' data-success="{esc(success)}"' if success else ""
    return (f'<form class="{cls}" data-form="{esc(name)}"{s} {extra_attrs} novalidate>'
            f'<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">'
            f'{inner}<button class="btn btn-primary" type="submit">{button}</button>'
            f'<div class="form-status" role="status" aria-live="polite"></div></form>')


def field(label, name, type_="text", required=True, placeholder="", attrs=""):
    req = " required" if required else ""
    ph = f' placeholder="{esc(placeholder)}"' if placeholder else ""
    if type_ == "textarea":
        ctl = f'<textarea name="{name}"{req}{ph} {attrs}></textarea>'
    else:
        ctl = f'<input type="{type_}" name="{name}"{req}{ph} {attrs}>'
    return f'<label class="fl">{label}{" *" if required else ""}{ctl}</label>'


def select(label, name, options, required=True):
    opts = '<option value="">Select…</option>' + "".join(
        f'<option value="{esc(o if isinstance(o, str) else o[0])}">{esc(o if isinstance(o, str) else o[1])}</option>' for o in options)
    return f'<label class="fl">{label}{" *" if required else ""}<select name="{name}"{" required" if required else ""}>{opts}</select></label>'


def consent(txt="I agree to be contacted about this request and accept the <a href=\"privacy.html\">Privacy Policy</a>."):
    return f'<label class="check"><input type="checkbox" name="Consent" value="Yes" required><span>{txt}</span></label>'


def ad(slot):
    return f'<div class="ad-slot container" data-ad="{slot}" aria-label="Advertisement"></div>'


def newsletter_inline(source="footer"):
    return form(f"Newsletter signup ({source})",
                '<div class="inline-form"><label class="sr-only" for="nl-' + source + '">Email</label>'
                f'<input id="nl-{source}" type="email" name="email" required placeholder="you@company.com">'
                f'<input type="hidden" name="Source" value="{source}"></div>',
                "Subscribe free", "You're in! Watch your inbox for the next Core Brief.", cls="form")


def header(active):
    cur = ' aria-current="page"'
    links = "".join(
        f'<a href="{h}"{cur if h == active else ""}>{t}</a>' for h, t in NAV)
    mobile = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV + [("get-matched.html", "Get Matched — free"),
                                                                ("submit.html", "Submit a Tool"), ("support.html", "Support Us"),
                                                                ("newsletter.html", "Newsletter"), ("contact.html", "Contact")])
    return f'''<a class="skip" href="#main">Skip to content</a>
<div class="topbar" role="note"><a href="{INTEREST_URL}" target="_blank" rel="noopener">Contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership</a></div>
<header class="site-header"><div class="container"><nav class="nav" aria-label="Main">
<a class="logo" href="index.html" aria-label="Core.Digital home">{LOGO}<span>Core<b>.Digital</b></span></a>
<div class="nav-links">{links}</div>
<div class="nav-cta"><a class="btn btn-sm btn-ghost hide-sm" href="submit.html">Submit tool</a>
<a class="btn btn-sm btn-primary hide-xs" href="get-matched.html">Get matched</a>
<button class="icon-btn" data-theme-toggle aria-label="Toggle light/dark theme">{ICON_SUN}</button>
<button class="icon-btn menu-btn" data-menu aria-label="Open menu" aria-expanded="false" aria-controls="mobile-nav">{ICON_MENU}</button></div>
</nav><div class="mobile-nav" id="mobile-nav">{mobile}</div></div></header>'''


def footer():
    return f'''<footer class="site-footer"><div class="container">
<div class="footer-grid">
<div class="footer-brand"><a class="logo" href="index.html">{LOGO}<span>Core<b>.Digital</b></span></a>
<p style="color:var(--muted);margin:14px 0">The core of everything digital — tools, guides, experts and opportunities for people building online.</p>
{newsletter_inline("footer")}</div>
<div><h4>Explore</h4><ul><li><a href="directory.html">Tool Directory</a></li><li><a href="guides.html">Guides</a></li><li><a href="free-tools.html">Free Tools</a></li><li><a href="videos.html">Videos</a></li><li><a href="checklist.html">Growth Checklist</a></li></ul></div>
<div><h4>Grow</h4><ul><li><a href="get-matched.html">Get Matched</a></li><li><a href="submit.html">Submit a Tool</a></li><li><a href="advertise.html">Advertise</a></li><li><a href="{INTEREST_URL}" target="_blank" rel="noopener">Partnerships</a></li><li><a href="careers.html#talent">Join Talent Network</a></li></ul></div>
<div><h4>Community</h4><ul><li><a href="contests.html">Contests</a></li><li><a href="careers.html">Careers</a></li><li><a href="support.html">Support Us</a></li><li><a href="newsletter.html">Newsletter</a></li><li><a href="about.html">About</a></li></ul></div>
<div><h4>Legal</h4><ul><li><a href="contact.html">Contact</a></li><li><a href="privacy.html">Privacy</a></li><li><a href="terms.html">Terms</a></li><li><a href="disclaimer.html">Disclaimer &amp; Disclosure</a></li><li><a href="trademark.html">Trademark &amp; Copyright</a></li><li><a href="cookies.html">Cookies</a></li></ul></div>
</div>
<div class="legal-line"><span>© <span data-year>2026</span> Core.Digital. All rights reserved. Original content, design and code are protected by copyright.</span>
<span>Core.Digital is an independent publication and is not affiliated with, endorsed by, or sponsored by any company or brand using the words “Core” or “Digital” (including any entity named “Core Digital” or “CoreDigital”). Third-party names and logos belong to their owners and are used for identification only. <a href="trademark.html">Read the full trademark &amp; copyright notice</a>.</span>
<span>Some links are affiliate or sponsored links; sponsored placements are always labelled. <a href="disclaimer.html">Disclosure</a>.</span></div>
</div></footer>
<a class="btn btn-primary sticky-cta" href="get-matched.html">⚡ Get matched free</a>
<div class="cookie" id="cookie" role="dialog" aria-label="Cookie consent"><p>We use essential cookies, and — with your OK — analytics and advertising cookies to keep Core.Digital free. <a href="cookies.html">Learn more</a>.</p>
<button class="btn btn-sm btn-ghost" data-consent="essential">Essential only</button><button class="btn btn-sm btn-primary" data-consent="all">Accept all</button></div>
<div class="modal" id="leadmagnet" role="dialog" aria-modal="true" aria-labelledby="lm-title"><div class="modal-box">
<button class="icon-btn modal-close" aria-label="Close">✕</button>
<span class="eyebrow">Free download</span><h3 id="lm-title" style="font-size:1.6rem">The 2026 Digital Growth Checklist</h3>
<p style="color:var(--muted)">52 checks across website, SEO, ads, email and AI that we use to audit online businesses. Free, instant access.</p>
{form("Lead magnet: Growth Checklist", field("Name", "name", placeholder="Your name") + field("Email", "email", "email", placeholder="you@company.com") + '<input type="hidden" name="Magnet" value="Growth Checklist">', "Send me the checklist", "Done! Opening your checklist…", 'data-next="checklist.html"')}
<p class="form-note" style="margin-top:10px">No spam. Unsubscribe anytime.</p></div></div>
<div class="toast" id="toast" role="status" aria-live="polite"></div>'''


def page(slug, title, desc, body, active=None, schema=None, scripts=(), og_type="website", noindex=False):
    url = BASE_URL + ("" if slug == "index.html" else slug)
    full_title = title if slug == "index.html" else f"{title} | {SITE}"
    ld = [{"@context": "https://schema.org", "@type": "Organization", "name": SITE, "url": BASE_URL,
           "logo": BASE_URL + "assets/img/logo.png"}]
    if schema:
        ld += schema if isinstance(schema, list) else [schema]
    ld_html = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    js = "".join(f'<script src="assets/js/{s}" defer></script>' for s in scripts)
    robots = '<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'
    return f'''<!doctype html>
<html lang="en" data-theme="dark"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(full_title)}</title><meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">{robots}
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="{SITE}"><meta property="og:title" content="{esc(full_title)}">
<meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{BASE_URL}assets/img/og.png">
<meta name="twitter:card" content="summary_large_image"><meta name="theme-color" content="#0a0e1a">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="assets/img/logo.png"><link rel="manifest" href="manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
<script>try{{var t=JSON.parse(localStorage.getItem("cd-theme"));if(t)document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
{ld_html}
</head><body>
{header(active)}
<main id="main">
{body}
</main>
{footer()}
<script src="assets/js/config.js" defer></script><script src="assets/js/app.js" defer></script>{js}
</body></html>'''
