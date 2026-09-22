"""Build Core.Digital static site (requires Python 3.12+):  python3 build/build.py"""
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from layout import BASE_URL, TODAY
import pages_core as C, pages_more as M
from articles import ARTICLES

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
out = {}
out["index.html"] = C.home(); out["directory.html"] = C.directory(); out["free-tools.html"] = C.free_tools()
out["videos.html"] = C.videos(); out["get-matched.html"] = C.get_matched(); out["checklist.html"] = C.checklist()
out["guides.html"] = M.guides()
for a in ARTICLES: out[a["slug"]] = M.article(a)
for fn in ["submit", "advertise", "support", "contests", "careers", "newsletter", "about", "contact",
           "privacy", "terms", "disclaimer", "trademark", "cookies"]:
    out[fn + ".html"] = getattr(M, fn)()
out["404.html"] = M.notfound()
for name, htmltext in out.items():
    open(os.path.join(ROOT, name), "w", encoding="utf-8").write(htmltext)

prio = {"index.html": "1.0", "get-matched.html": "0.9", "directory.html": "0.9", "free-tools.html": "0.8", "guides.html": "0.8"}
urls = "".join(f"<url><loc>{BASE_URL}{'' if n == 'index.html' else n}</loc><lastmod>{TODAY}</lastmod><priority>{prio.get(n, '0.6')}</priority></url>"
               for n in out if n != "404.html")
open(os.path.join(ROOT, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE_URL}sitemap.xml\n")
if not os.path.exists(os.path.join(ROOT, "ads.txt")):
    open(os.path.join(ROOT, "ads.txt"), "w").write("# Replace pub-0000000000000000 with your AdSense publisher ID, then uncomment.\n# google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0\n")
open(os.path.join(ROOT, "manifest.webmanifest"), "w").write(json.dumps({
    "name": "Core.Digital", "short_name": "Core.Digital", "start_url": "./index.html", "display": "standalone",
    "background_color": "#0a0e1a", "theme_color": "#0a0e1a",
    "icons": [{"src": "assets/img/logo.svg", "sizes": "any", "type": "image/svg+xml"}]}, indent=2))
open(os.path.join(ROOT, ".nojekyll"), "w").write("")
print(f"Built {len(out)} pages")
