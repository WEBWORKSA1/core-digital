"""Optional: convert the generated full HTML pages into a compact Jekyll source tree
(_layouts/default.html + _includes/header.html + _includes/footer.html + front-matter pages).
GitHub Pages renders it back into byte-identical HTML. Usage: python3 build/jekyllify.py OUTDIR"""
import os, re, sys, glob, json
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "_jekyll"))
P0 = '<!doctype html>\n<html lang="en" data-theme="dark"><head>'
P1 = '\n<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">\n'
FIX_START = '<meta name="twitter:card"'
TOAST = '<div class="toast" id="toast" role="status" aria-live="polite"></div>'
CORE_JS = '\n<script src="assets/js/config.js" defer></script><script src="assets/js/app.js" defer></script>'

def split(s):
    assert s.startswith(P0)
    rest = s[len(P0):]
    base, rest = rest.split(P1, 1)
    f = rest.index(FIX_START); head = rest[:f]
    ld_i = rest.index('<script type="application/ld+json">'); fixed = rest[f:ld_i]
    e = rest.index('</head><body>\n'); ld = rest[ld_i:e]
    h1 = rest.index('<a class="skip"'); h2 = rest.index('<main id="main">')
    header = rest[h1:h2]
    a = rest.index("\n</main>\n"); b = rest.index(TOAST)
    body = rest[h2 + len('<main id="main">'):a]; footer = rest[a:b]
    tail = rest[b + len(TOAST):]
    assert tail.startswith(CORE_JS) and tail.endswith("\n</body></html>")
    js = tail[len(CORE_JS):-len("\n</body></html>")]
    m = re.search(r'<a href="([^"]+)" aria-current="page">', header)
    return dict(base=base, head=head, fixed=fixed, ld=ld, header=header, body=body, footer=footer, js=js, active=m.group(1) if m else "")

def yblock(key, v):
    if v == "": return f'{key}: ""\n'
    if "\n" not in v: return f"{key}: {json.dumps(v, ensure_ascii=False)}\n"
    ind = "|" if v.endswith("\n") and not v.endswith("\n\n") else "|-"
    assert not v.endswith("\n\n")
    return f"{key}: {ind}\n" + "".join("  " + ln + "\n" if ln else "\n" for ln in v.rstrip("\n").split("\n"))

def main():
    pages = sorted(glob.glob(os.path.join(ROOT, "*.html")))
    parts = {os.path.basename(p): split(open(p, encoding="utf-8").read()) for p in pages}
    ref = parts["index.html"]
    hdr = re.sub(r' aria-current="page"', "", ref["header"])
    hdr = re.sub(r'(<div class="nav-links">)(.*?)(</div>)', lambda m: m.group(1) + re.sub(
        r'<a href="([^"]+)">', lambda n: f'<a href="{n.group(1)}"{{% if page.active == "{n.group(1)}" %}} aria-current="page"{{% endif %}}>', m.group(2)) + m.group(3), hdr, count=1, flags=re.S)
    for n, p in parts.items():
        assert p["fixed"] == ref["fixed"] and p["footer"] == ref["footer"], n
    os.makedirs(os.path.join(OUT, "_layouts"), exist_ok=True); os.makedirs(os.path.join(OUT, "_includes"), exist_ok=True)
    layout = (P0 + "{{ page.base }}" + P1 + "{{ page.head }}" + ref["fixed"] + "{{ page.ld }}" + "</head><body>\n"
              + "{% include header.html %}" + '<main id="main">' + "{{ content }}" + "{% include footer.html %}" + TOAST + CORE_JS + "{{ page.js }}" + "\n</body></html>")
    open(os.path.join(OUT, "_layouts", "default.html"), "w").write(layout)
    open(os.path.join(OUT, "_includes", "header.html"), "w").write(hdr)
    open(os.path.join(OUT, "_includes", "footer.html"), "w").write(ref["footer"])
    open(os.path.join(OUT, "_config.yml"), "w").write("# GitHub Pages (Jekyll) settings\nexclude: [build, README.md, _jekyll]\n")
    for n, p in parts.items():
        fm = "---\nlayout: default\n" + yblock("active", p["active"]) + yblock("base", p["base"]) + yblock("head", p["head"]) + yblock("ld", p["ld"]) + yblock("js", p["js"]) + "---\n"
        open(os.path.join(OUT, n), "w").write(fm + p["body"])
    print("jekyll tree written to", OUT, len(parts), "pages")

if __name__ == "__main__":
    main()
