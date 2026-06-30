from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public' / 'assets' / 'wedding-og-card.png'
W, H = 1200, 630

FONT_MYUNGJO = '/System/Library/Fonts/Supplemental/AppleMyungjo.ttf'

def font(size):
    return ImageFont.truetype(FONT_MYUNGJO, size)

title_font = font(66)
date_font = font(43)

img = Image.new('RGB', (W, H), '#ffffff')
d = ImageDraw.Draw(img)
cx = W // 2

# Exactly the requested elements: Korean title, date, and the dotted envelope.
for text, y, f in [
    ('송형우와 강혜진의 결혼식', 38, title_font),
    ('2026.10.24 토요일 낮 12시', 122, date_font),
]:
    bbox = d.textbbox((0, 0), text, font=f)
    d.text((cx - (bbox[2]-bbox[0]) / 2, y), text, font=f, fill='#111111')

# Envelope, scaled and positioned like the provided reference.
ex0, ey0, ex1, ey1 = 175, 250, 1025, 475
line = '#111111'

# subtle bottom shadow only, matching the reference
shadow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.rectangle((ex0 + 18, ey1 - 2, ex1 - 18, ey1 + 18), fill=(0, 0, 0, 40))
shadow = shadow.filter(ImageFilter.GaussianBlur(18))
img = Image.alpha_composite(img.convert('RGBA'), shadow)
d = ImageDraw.Draw(img)

# Envelope outline
paper = '#fffefa'
d.rectangle((ex0, ey0, ex1, ey1), fill=paper, outline=line, width=3)

# Folds: diagonals and a soft curved flap edge.
mid_x = (ex0 + ex1) // 2
flap_y = ey0 + 126
d.line((ex0, ey0, mid_x, flap_y, ex1, ey0), fill=line, width=2)
d.line((ex0, ey1, ex0 + 305, ey0 + 96), fill=line, width=2)
d.line((ex1, ey1, ex1 - 305, ey0 + 96), fill=line, width=2)
d.line([(ex0 + 195, ey0 + 90), (ex0 + 320, ey0 + 125), (mid_x, ey0 + 146), (ex1 - 320, ey0 + 125), (ex1 - 195, ey0 + 90)], fill=line, width=2, joint='curve')

# Dot pattern using the current invitation's black-dot language, placed like the reference.
for x, y, r in [
    (ex0 + 96, ey0 + 60, 27),
    (ex0 + 235, ey0 + 48, 30),
    (ex0 + 420, ey0 + 76, 31),
    (ex0 + 625, ey0 + 47, 30),
    (ex0 + 755, ey0 + 112, 27),
    (ex0 + 180, ey0 + 143, 28),
    (ex0 + 510, ey0 + 151, 31),
    (ex0 + 735, ey0 + 171, 28),
    (ex0 + 105, ey0 + 195, 24),
]:
    d.ellipse((x-r, y-r, x+r, y+r), fill='#111111')

OUT.parent.mkdir(parents=True, exist_ok=True)
img.convert('RGB').save(OUT, quality=95)
print(OUT)
print(img.size)
