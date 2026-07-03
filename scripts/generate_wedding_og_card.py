from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public' / 'assets' / 'wedding-og-card.png'
W, H = 1200, 630

FONT_MYUNGJO = '/System/Library/Fonts/Supplemental/AppleMyungjo.ttf'
DOTS = [
    (420.0, -7.2, 7.4), (327.4, 8.9, 7.4), (55.9, 16.6, 7.5),
    (252.7, 16.7, 7.9), (171.9, 29.5, 7.9), (227.3, 35.0, 8.1),
    (124.0, 44.4, 7.7), (288.3, 60.8, 7.3), (379.9, 61.9, 7.5),
    (24.0, 66.6, 7.2), (161.4, 88.4, 7.3), (20.1, 93.6, 7.4),
    (101.5, 101.9, 7.2), (164.2, 107.9, 7.5), (432.4, 125.5, 7.1),
    (124.1, 139.1, 7.0), (317.8, 154.3, 7.2), (222.2, 158.0, 7.9),
    (260.5, 189.2, 7.3), (33.6, 194.4, 7.6), (5.7, 205.5, 6.9),
    (97.9, 207.4, 7.4), (344.1, 209.0, 7.1), (186.2, 219.5, 7.2),
    (265.7, 224.4, 7.4), (132.9, 228.9, 7.4), (22.2, 251.2, 7.1),
    (305.3, 265.7, 7.1), (182.8, 273.3, 7.0), (227.5, 274.2, 7.0),
    (426.9, 280.0, 7.3), (215.1, 289.1, 7.5), (16.0, 300.8, 7.0),
    (73.6, 318.3, 7.6), (34.8, 323.6, 7.3), (388.6, 342.7, 7.1),
]

def font(size):
    return ImageFont.truetype(FONT_MYUNGJO, size)

date_font = font(58)
place_font = font(42)
img = Image.new('RGB', (W, H), '#ffffff')
d = ImageDraw.Draw(img)
cx = W // 2

for text, y, f in [
    ('2026년 10월 24일 토요일 낮 12시', 48, date_font),
    ('천주교 도림동성당', 132, place_font),
]:
    bbox = d.textbbox((0, 0), text, font=f)
    d.text((cx - (bbox[2]-bbox[0]) / 2, y), text, font=f, fill='#111111')

ex0, ey0, ex1, ey1 = 175, 250, 1025, 475
line = '#111111'
cream = '#fbf7e8'
blue = '#607f99'

shadow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.rectangle((ex0 + 18, ey1 - 2, ex1 - 18, ey1 + 18), fill=(0, 0, 0, 36))
shadow = shadow.filter(ImageFilter.GaussianBlur(18))
img = Image.alpha_composite(img.convert('RGBA'), shadow)
d = ImageDraw.Draw(img)

d.rectangle((ex0, ey0, ex1, ey1), fill=cream, outline=line, width=3)
# Draw every dot as its own true circle: no stretched raster texture.
# Clip dots to the envelope body so edge dots do not spill outside the paper.
sx = (ex1 - ex0) / 440
sy = (ey1 - ey0) / 330
s = min(sx, sy)
dot_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
dot_draw = ImageDraw.Draw(dot_layer)
for x, y, r in DOTS:
    px = ex0 + x * sx
    py = ey0 + y * sy
    rr = r * s
    dot_draw.ellipse((px-rr, py-rr, px+rr, py+rr), fill=blue)
# Composite only the blue dots over the cream envelope. Do not replace the whole
# envelope rectangle with the transparent dot layer, or transparent pixels become
# black after RGB conversion.
img = Image.alpha_composite(img.convert('RGBA'), dot_layer)
d = ImageDraw.Draw(img)

mid_x = (ex0 + ex1) // 2
flap_y = ey0 + 126
d.line((ex0, ey0, mid_x, flap_y, ex1, ey0), fill=line, width=2)
d.line((ex0, ey1, ex0 + 305, ey0 + 96), fill=line, width=2)
d.line((ex1, ey1, ex1 - 305, ey0 + 96), fill=line, width=2)
d.line([(ex0 + 195, ey0 + 90), (ex0 + 320, ey0 + 125), (mid_x, ey0 + 146), (ex1 - 320, ey0 + 125), (ex1 - 195, ey0 + 90)], fill=line, width=2, joint='curve')

OUT.parent.mkdir(parents=True, exist_ok=True)
img.convert('RGB').save(OUT, quality=95)
print(OUT)
print(img.size)
