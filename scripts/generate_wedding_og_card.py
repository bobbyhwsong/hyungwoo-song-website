from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public' / 'assets' / 'wedding-og-card.png'
W, H = 1200, 630

FONT_GOTHIC = '/System/Library/Fonts/AppleSDGothicNeo.ttc'
FONT_MYUNGJO = '/System/Library/Fonts/Supplemental/AppleMyungjo.ttf'

def font(path, size, index=0):
    return ImageFont.truetype(path, size, index=index)

# AppleSDGothicNeo.ttc indices vary by system; index 0 is safely readable.
regular = font(FONT_GOTHIC, 28)
medium = font(FONT_GOTHIC, 34)
small = font(FONT_GOTHIC, 23)
button_font = font(FONT_GOTHIC, 31)
serif_title = font(FONT_MYUNGJO, 40)
serif_date = font(FONT_MYUNGJO, 29)

img = Image.new('RGB', (W, H), '#eaf0f4')
d = ImageDraw.Draw(img)

# Card shadow and body
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
# Top text, centered like a mobile share preview card
for text, y, f, fill in [
    ('송형우와 강혜진의 결혼식', 72, serif_title, '#202020'),
    ('2026.10.24 토요일 낮 12시', 126, serif_date, '#333333'),
]:
    bbox = d.textbbox((0, 0), text, font=f)
    d.text((cx - (bbox[2]-bbox[0]) / 2, y), text, font=f, fill=fill)

# Our envelope: white paper + black dot pattern, thin black lines.
ex0, ey0, ex1, ey1 = 342, 176, 858, 356
env_w, env_h = ex1-ex0, ey1-ey0
# slight warm paper base so it does not feel sterile
paper = '#fffefa'
line = '#171717'
d.rounded_rectangle((ex0, ey0, ex1, ey1), radius=2, fill=paper, outline=line, width=2)
# dot pattern from invitation envelope
for x, y, r in [
    (ex0+62, ey0+38, 17), (ex0+142, ey0+30, 20), (ex0+255, ey0+48, 18),
    (ex0+374, ey0+34, 19), (ex0+454, ey0+78, 18), (ex0+112, ey0+116, 18),
    (ex0+314, ey0+122, 19), (ex0+438, ey0+132, 17)
]:
    d.ellipse((x-r, y-r, x+r, y+r), fill='#111111')
# envelope folds
mid_x = (ex0 + ex1) // 2
mid_y = ey0 + 114
d.line((ex0, ey0, mid_x, mid_y, ex1, ey0), fill=line, width=2)
d.line((ex0, ey1, ex0+190, ey0+88), fill=line, width=2)
d.line((ex1, ey1, ex1-190, ey0+88), fill=line, width=2)
# soft flap curve overlay for the familiar invitation shape
curve = [(ex0+120, ey0+82), (ex0+205, ey0+120), (mid_x, ey0+128), (ex1-205, ey0+120), (ex1-120, ey0+82)]
d.line(curve, fill='#202020', width=2, joint='curve')

# Lower message block
left = 315
headline = '저희 결혼합니다'
d.text((left, 394), headline, font=medium, fill='#111111')
# small floral-like mark, understated
hb = d.textbbox((left, 394), headline, font=medium)
d.text((hb[2] + 8, 394), '✿', font=small, fill='#777777')
body = '소중한 분들을 모시고\n혼인의 예를 올리고자 합니다.'
d.multiline_text((left, 444), body, font=small, fill='#555555', spacing=8)

# Button
btn = (315, 514, 885, 566)
d.rounded_rectangle(btn, radius=8, fill='#f3f4f5')
btn_text = '청첩장 보기'
b = d.textbbox((0, 0), btn_text, font=button_font)
d.text((cx - (b[2]-b[0])/2, btn[1] + 9), btn_text, font=button_font, fill='#111111')

# Small footer line, matching Kakao-style preview source row without English.
footer = '천주교 도림동성당'
d.text((315, 574), footer, font=font(FONT_GOTHIC, 18), fill='#8a8a8a')
# subtle chevron
chev_x = 870
d.line((chev_x, 579, chev_x+8, 587, chev_x, 595), fill='#b8b8b8', width=2)

OUT.parent.mkdir(parents=True, exist_ok=True)
img.convert('RGB').save(OUT, quality=95)
print(OUT)
print(img.size)
