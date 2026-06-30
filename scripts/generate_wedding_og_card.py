from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public' / 'assets' / 'wedding-og-card.png'
W, H = 1200, 630

FONT_GOTHIC = '/System/Library/Fonts/AppleSDGothicNeo.ttc'
FONT_MYUNGJO = '/System/Library/Fonts/Supplemental/AppleMyungjo.ttf'

def font(path, size, index=0):
    return ImageFont.truetype(path, size, index=index)

serif_title = font(FONT_MYUNGJO, 48)
serif_date = font(FONT_MYUNGJO, 32)

img = Image.new('RGB', (W, H), '#eaf0f4')

# Rounded white preview card, like a clean messenger thumbnail.
card = (230, 34, 970, 596)
shadow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.rounded_rectangle((card[0]+8, card[1]+10, card[2]+8, card[3]+10), radius=30, fill=(0, 0, 0, 34))
shadow = shadow.filter(ImageFilter.GaussianBlur(16))
img = Image.alpha_composite(img.convert('RGBA'), shadow)
d = ImageDraw.Draw(img)
d.rounded_rectangle(card, radius=30, fill='#ffffff')
d.rounded_rectangle(card, radius=30, outline='#dce1e5', width=2)

cx = W // 2
for text, y, f, fill in [
    ('송형우와 강혜진의 결혼식', 88, serif_title, '#202020'),
    ('2026.10.24 토요일 낮 12시', 154, serif_date, '#333333'),
]:
    bbox = d.textbbox((0, 0), text, font=f)
    d.text((cx - (bbox[2]-bbox[0]) / 2, y), text, font=f, fill=fill)

# Use the same black-dot envelope language as the invitation cover.
ex0, ey0, ex1, ey1 = 316, 244, 884, 442
paper = '#fffefa'
line = '#171717'
# Envelope shadow
env_shadow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
esd = ImageDraw.Draw(env_shadow)
esd.rectangle((ex0+6, ey0+10, ex1+6, ey1+10), fill=(0, 0, 0, 38))
env_shadow = env_shadow.filter(ImageFilter.GaussianBlur(13))
img = Image.alpha_composite(img, env_shadow)
d = ImageDraw.Draw(img)

d.rectangle((ex0, ey0, ex1, ey1), fill=paper, outline=line, width=2)
# Dot pattern
for x, y, r in [
    (ex0+66, ey0+42, 18), (ex0+156, ey0+34, 20), (ex0+282, ey0+52, 19),
    (ex0+414, ey0+38, 20), (ex0+506, ey0+86, 18), (ex0+122, ey0+128, 18),
    (ex0+342, ey0+134, 20), (ex0+488, ey0+146, 18), (ex0+72, ey0+174, 16),
]:
    d.ellipse((x-r, y-r, x+r, y+r), fill='#111111')

mid_x = (ex0 + ex1) // 2
# Fold lines: simple, close to the real invitation envelope.
d.line((ex0, ey0, mid_x, ey0+126, ex1, ey0), fill=line, width=2)
d.line((ex0, ey1, ex0+205, ey0+96), fill=line, width=2)
d.line((ex1, ey1, ex1-205, ey0+96), fill=line, width=2)
d.line([(ex0+128, ey0+92), (ex0+225, ey0+126), (mid_x, ey0+136), (ex1-225, ey0+126), (ex1-128, ey0+92)], fill='#202020', width=2, joint='curve')

OUT.parent.mkdir(parents=True, exist_ok=True)
img.convert('RGB').save(OUT, quality=95)
print(OUT)
print(img.size)
