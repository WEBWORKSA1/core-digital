"""Generate raster brand images (logo.png, og.png) — run in CI (pip install pillow)."""
import os, glob
from PIL import Image, ImageDraw, ImageFont
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
IMG = os.path.join(ROOT, "assets", "img"); os.makedirs(IMG, exist_ok=True)

def ring(d, cx, cy, r, wid, alpha=255):
    for i in range(wid):
        t = i / wid
        d.ellipse([cx - r + i, cy - r + i, cx + r - i, cy + r - i], outline=(int(124 - 100 * t), int(108 + 100 * t), 255, alpha))

def font(size, bold):
    pats = ["**/Poppins-Bold.ttf", "**/DejaVuSans-Bold.ttf"] if bold else ["**/Poppins-Regular.ttf", "**/DejaVuSans.ttf"]
    for p in pats:
        f = glob.glob("/usr/share/fonts/" + p, recursive=True)
        if f: return ImageFont.truetype(f[0], size)
    return ImageFont.load_default()

logo = Image.new("RGBA", (512, 512), (10, 14, 26, 255)); d = ImageDraw.Draw(logo)
ring(d, 256, 256, 210, 46); ring(d, 256, 256, 112, 30, 180); d.ellipse([206, 206, 306, 306], fill=(79, 139, 255, 255))
logo.save(os.path.join(IMG, "logo.png"))

og = Image.new("RGB", (1200, 630), "#0a0e1a"); d = ImageDraw.Draw(og)
for x in range(1200):
    t = x / 1200; d.line([(x, 0), (x, 10)], fill=(int(124 - 90 * t), int(108 + 103 * t), int(255 - 17 * t)))
s = logo.resize((220, 220)); og.paste(s, (90, 205), s)
d.text((350, 200), "Core.Digital", font=font(88, True), fill="#e8ecf7")
d.text((354, 335), "AI & digital tools · Guides · Free tools", font=font(34, False), fill="#9aa5c4")
d.text((354, 390), "Get matched with vetted experts — free", font=font(34, False), fill="#22d3ee")
og.save(os.path.join(IMG, "og.png"))
print("images ok")
