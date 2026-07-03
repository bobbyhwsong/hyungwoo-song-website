from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public' / 'assets' / 'wedding-og-card.png'
DOT_SVG = ROOT / 'public' / 'assets' / 'wedding-envelope-dots.svg'
W, H = 1200, 630

FONT_MYUNGJO = '/System/Library/Fonts/Supplemental/AppleMyungjo.ttf'
ENVELOPE_RATIO = 154 / 110

def font(size):
    return ImageFont.truetype(FONT_MYUNGJO, size)

def load_dots():
    """Read the same cropped dot artwork used by the first-screen envelope."""
    svg = DOT_SVG.read_text()
    circles = re.findall(r'<circle cx="([\d.\-]+)" cy="([\d.\-]+)" r="([\d.\-]+)" fill="([^"]+)"', svg)
    return [(float(x), float(y), float(r), fill) for x, y, r, fill in circles]

img = Image.new('RGBA', (W, H), '#ffffff')
d = ImageDraw.Draw(img)
cx = W // 2

for text, y, f in [
    ('2026년 10월 24일 토요일 낮 12시', 48, font(58)),
    ('천주교 도림동성당', 132, font(42)),
]:
    bbox = d.textbbox((0, 0), text, font=f)
    d.text((cx - (bbox[2] - bbox[0]) / 2, y), text, font=f, fill='#111111')

# Same 154:110 envelope proportion as the mobile invitation cover.
env_w = 610
env_h = round(env_w / ENVELOPE_RATIO)
ex0 = (W - env_w) // 2
ex1 = ex0 + env_w
ey0 = 186
ey1 = ey0 + env_h
line = '#111111'
cream = '#fbf7e8'
blue_default = '#607f99'

# Soft paper shadow.
shadow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.rounded_rectangle((ex0 + 24, ey1 - 8, ex1 - 24, ey1 + 24), radius=18, fill=(0, 0, 0, 28))
shadow = shadow.filter(ImageFilter.GaussianBlur(20))
img = Image.alpha_composite(img, shadow)
d = ImageDraw.Draw(img)

# Envelope paper base.
d.rectangle((ex0, ey0, ex1, ey1), fill=cream, outline=(17, 17, 17, 70), width=3)

# Dot pattern: use the exact 154x110 SVG coordinates so the thumbnail matches the first screen.
dot_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
dot_draw = ImageDraw.Draw(dot_layer)
sx = env_w / 154
sy = env_h / 110
for x, y, r, fill in load_dots():
    px = ex0 + x * sx
    py = ey0 + y * sy
    rr = r * min(sx, sy)
    color = fill if fill else blue_default
    dot_draw.ellipse((px - rr, py - rr, px + rr, py + rr), fill=color)
# Clip dots to the envelope bounds.
mask = Image.new('L', (W, H), 0)
ImageDraw.Draw(mask).rectangle((ex0, ey0, ex1, ey1), fill=255)
clipped = Image.new('RGBA', (W, H), (0, 0, 0, 0))
clipped.paste(dot_layer, (0, 0), mask)
img = Image.alpha_composite(img, clipped)
d = ImageDraw.Draw(img)

# Match the first-screen closed envelope: keep only the quiet hinge line.
# Avoid explanatory X/triangle fold lines; they made the thumbnail look like a diagram.
hinge_y = ey0 + env_h * 0.32
subtle = (17, 17, 17, 48)
d.line((ex0, hinge_y, ex1, hinge_y), fill=subtle, width=2)
# Outer outline again on top.
d.rectangle((ex0, ey0, ex1, ey1), outline=(17, 17, 17, 70), width=3)

OUT.parent.mkdir(parents=True, exist_ok=True)
img.convert('RGB').save(OUT, quality=95)
print(OUT)
print(img.size)
print('envelope', (env_w, env_h), 'ratio', round(env_w / env_h, 4))
