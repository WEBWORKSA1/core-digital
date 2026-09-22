# Core.Digital

**The core of everything digital.** An AI & digital tools directory with guides, free calculators, videos, and a free "Get Matched" lead-generation service. Monetised through AdSense, sponsorships, paid listings, job posts, contests and reader support.

- Static HTML, CSS and vanilla JS. No framework and nothing to compile before serving.
- Hosted free on GitHub Pages.
- Strategy and the phase-wise build prompt are in [`docs/BUILD-PROMPT.md`](docs/BUILD-PROMPT.md).

## Go-live checklist (edit `assets/js/config.js` only)

| Setting | What to paste |
|---|---|
| `adsenseClient`, `adsenseSlots` | AdSense publisher ID and ad-unit slot IDs. Also update `ads.txt`. |
| `ga4` | GA4 measurement ID. It loads only after the visitor accepts cookies. |
| `youtubeChannel` | Channel URL. The Subscribe buttons appear automatically. |
| `donate.*` | Stripe, PayPal, Buy Me a Coffee, Ko-fi or GitHub Sponsors links. The buttons appear automatically. |
| `checkout.*` | Stripe Payment Links for listings and job posts. |
| `formAlias` | Optional: the FormSubmit random alias, which hardens email privacy (see below). |

## Forms and inbox

- Every form posts over AJAX to FormSubmit.
- The inbox address is stored obfuscated in `config.js`. It is assembled only when a form is submitted, so it never appears in any page.
- **First submission:** FormSubmit sends a one-time activation email to the inbox. Click it, or forms won't deliver.
- After activation, FormSubmit gives you a random alias string. Paste it into `formAlias` and the real address is no longer used on the client at all.

## Edit and rebuild

Pages are generated from `build/`:

- `layout.py`: header, footer and shared parts
- `pages_core.py` and `pages_more.py`: page content
- `articles.py`: the guides

To rebuild, run `python3 build/build.py` (Python 3.12+), commit the generated `.html` files, and push to both `main` and `gh-pages`. `build/make_images.py` (Pillow) regenerates `assets/img/og.png` and `logo.png`. The directory data lives in `assets/js/tools-data.js`. Add tools there; no rebuild is needed.

## Hosting

- GitHub Pages serves the `gh-pages` branch at https://webworksa1.github.io/core-digital/
- If the site isn't live, open **Settings → Pages** and set Source to *Deploy from a branch*, branch `gh-pages` (or `main`), folder `/ (root)`.
- To use a custom domain:
  1. Add a `CNAME` file containing `core.digital`.
  2. Point DNS to GitHub Pages.
  3. Set `BASE_URL` in `build/layout.py` to `https://core.digital/`.
  4. Rebuild.

## Legal

© 2026 Core.Digital. All rights reserved.

Core.Digital is independent. It is not affiliated with any company named "Core Digital" or "CoreDigital". Third-party names belong to their owners. See `trademark.html`.
