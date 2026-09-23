from PIL import Image, ImageDraw, ImageFont
import os

width = 1200
height = 630

# Background - dark theme matching website --black: #0B0B0A
bg_color = (11, 11, 10)  # #0B0B0A
img = Image.new('RGBA', (width, height), bg_color)
draw = ImageDraw.Draw(img)

# Subtle background texture / grid or border
# Elegant framing border 32px from edges
border_box = [32, 32, width - 32, height - 32]
draw.rounded_rectangle(border_box, radius=16, outline=(34, 34, 32), width=1)

# Subtle inner ambient glow / gradient card in the center
card_box = [48, 48, width - 48, height - 48]
draw.rounded_rectangle(card_box, radius=12, fill=(16, 16, 15), outline=(28, 28, 26), width=1)

# Subtle corner accent tick marks (mimicking receipt / precision design)
tick_len = 16
for (x, y) in [(48, 48), (width - 48, 48), (48, height - 48), (width - 48, height - 48)]:
    dx = 1 if x == 48 else -1
    dy = 1 if y == 48 else -1
    draw.line([(x, y), (x + dx * tick_len, y)], fill=(60, 60, 56), width=2)
    draw.line([(x, y), (x, y + dy * tick_len)], fill=(60, 60, 56), width=2)

# Load Logo
logo_path = 'assets/White_logo.png'
if os.path.exists(logo_path):
    logo = Image.open(logo_path).convert('RGBA')
    # Crop transparent borders
    bbox = logo.getbbox()
    if bbox:
        logo = logo.crop(bbox)
    
    # Scale logo: height around 64px
    target_height = 60
    aspect = logo.width / logo.height
    target_width = int(target_height * aspect)
    logo_resized = logo.resize((target_width, target_height), Image.Resampling.LANCZOS)
    
    # Place logo top center or top-left
    logo_x = (width - target_width) // 2
    logo_y = 100
    img.paste(logo_resized, (logo_x, logo_y), logo_resized)

# Fonts
font_dir = 'C:/Windows/Fonts'
title_font = ImageFont.truetype(os.path.join(font_dir, 'georgia.ttf'), 56)
subtitle_font = ImageFont.truetype(os.path.join(font_dir, 'georgia.ttf'), 38)
mono_font = ImageFont.truetype(os.path.join(font_dir, 'consolab.ttf'), 20)
url_font = ImageFont.truetype(os.path.join(font_dir, 'consola.ttf'), 18)
badge_font = ImageFont.truetype(os.path.join(font_dir, 'segoeuib.ttf'), 14)

# Headline: "Your bills, simplified."
headline = "Your bills, simplified."
h_bbox = draw.textbbox((0, 0), headline, font=title_font)
h_w = h_bbox[2] - h_bbox[0]
h_x = (width - h_w) // 2
h_y = 215
draw.text((h_x, h_y), headline, fill=(255, 255, 255), font=title_font)

# Feature badge / pill: "Split • Track • Settle"
pill_text = "SPLIT   •   TRACK   •   SETTLE"
p_bbox = draw.textbbox((0, 0), pill_text, font=mono_font)
p_w = p_bbox[2] - p_bbox[0]
p_h = p_bbox[3] - p_bbox[1]

pill_pad_x = 28
pill_pad_y = 12
pill_x0 = (width - p_w) // 2 - pill_pad_x
pill_y0 = 330
pill_x1 = pill_x0 + p_w + pill_pad_x * 2
pill_y1 = pill_y0 + p_h + pill_pad_y * 2

draw.rounded_rectangle([pill_x0, pill_y0, pill_x1, pill_y1], radius=24, fill=(24, 24, 22), outline=(48, 48, 45), width=1)
draw.text((pill_x0 + pill_pad_x, pill_y0 + pill_pad_y), pill_text, fill=(200, 200, 195), font=mono_font)

# Subtle separator line
sep_y = 445
draw.line([(width // 2 - 180, sep_y), (width // 2 + 180, sep_y)], fill=(38, 38, 35), width=1)

# URL bar & Product Overview indicator at bottom
# "●  what.is.billbreaker.in  |  Product Overview"
url_text = "what.is.billbreaker.in"
sub_label = "PRODUCT OVERVIEW"

u_bbox = draw.textbbox((0, 0), url_text, font=url_font)
u_w = u_bbox[2] - u_bbox[0]

# Green live dot + url + badge
dot_radius = 4
total_bottom_width = dot_radius * 2 + 12 + u_w + 24 + 130
start_bx = (width - total_bottom_width) // 2
bottom_y = 485

# Green live dot
dot_cx = start_bx + dot_radius
dot_cy = bottom_y + (u_bbox[3] - u_bbox[1]) // 2 + 2
draw.ellipse([dot_cx - dot_radius, dot_cy - dot_radius, dot_cx + dot_radius, dot_cy + dot_radius], fill=(34, 197, 94))

# URL text
draw.text((start_bx + dot_radius * 2 + 12, bottom_y), url_text, fill=(163, 163, 158), font=url_font)

# Divider
div_x = start_bx + dot_radius * 2 + 12 + u_w + 14
draw.line([(div_x, bottom_y + 2), (div_x, bottom_y + 18)], fill=(55, 55, 52), width=1)

# Badge
draw.text((div_x + 16, bottom_y + 2), sub_label, fill=(110, 110, 106), font=badge_font)

# Save final image
img_rgb = img.convert('RGB')
img_rgb.save('og-image.png', 'PNG', optimize=True)
print("Saved og-image.png successfully with size:", img_rgb.size)
