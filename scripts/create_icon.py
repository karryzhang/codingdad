#!/usr/bin/env python3
"""Generate VocabLoop app icons in multiple sizes."""
import math, pathlib
from PIL import Image, ImageDraw

OUT = pathlib.Path(__file__).parent.parent / 'english' / 'icons'
OUT.mkdir(exist_ok=True)

# ── Colour palette ──────────────────────────────────────────────────────────
BG_TOP    = (37,  99, 235)   # #2563EB  vivid blue
BG_BOT    = (109, 40, 217)   # #6D28D9  deep purple
WHITE     = (255, 255, 255)
WHITE_80  = (255, 255, 255, 200)

def lerp_color(c1, c2, t):
    return tuple(int(c1[i] + (c2[i]-c1[i])*t) for i in range(3))

def make_icon(size):
    img  = Image.new('RGBA', (size, size), (0,0,0,0))
    draw = ImageDraw.Draw(img)

    # ── Gradient rounded-square background ──────────────────────────────────
    radius = size // 5          # iOS-style corner radius
    for y in range(size):
        t   = y / size
        col = lerp_color(BG_TOP, BG_BOT, t) + (255,)
        draw.line([(0, y), (size, y)], fill=col)

    # Mask to rounded rectangle
    mask = Image.new('L', (size, size), 0)
    md   = ImageDraw.Draw(mask)
    md.rounded_rectangle([0, 0, size-1, size-1], radius=radius, fill=255)
    img.putalpha(mask)

    # Re-draw gradient on clean rounded bg
    grad = Image.new('RGBA', (size, size), (0,0,0,0))
    gd   = ImageDraw.Draw(grad)
    for y in range(size):
        t   = y / size
        col = lerp_color(BG_TOP, BG_BOT, t) + (255,)
        gd.line([(0, y), (size, y)], fill=col)
    grad.putalpha(mask)

    # ── Inner glow circle (soft) ────────────────────────────────────────────
    cx, cy = size//2, size//2
    glow   = Image.new('RGBA', (size, size), (0,0,0,0))
    gd2    = ImageDraw.Draw(glow)
    gr     = int(size * 0.38)
    gd2.ellipse([cx-gr, cy-gr, cx+gr, cy+gr], fill=(255,255,255,22))
    grad   = Image.alpha_composite(grad, glow)

    # ── Loop arrow arc ──────────────────────────────────────────────────────
    draw2  = ImageDraw.Draw(grad)
    lw     = max(4, size // 28)      # line width scales with size
    ar     = int(size * 0.30)        # arc radius
    arc_bb = [cx-ar, cy-ar, cx+ar, cy+ar]
    # Arc: 210° → 510° (300° sweep, gap at bottom-right for arrow)
    draw2.arc(arc_bb, start=105, end=390, fill=WHITE, width=lw)

    # Arrowhead at end of arc (angle ≈ 390° = 30°)
    aend_deg = 30
    aend_rad = math.radians(aend_deg)
    tip_x = cx + ar * math.cos(aend_rad)
    tip_y = cy + ar * math.sin(aend_rad)

    tang_deg = aend_deg + 90          # tangent direction
    tang_rad = math.radians(tang_deg)
    ah = lw * 3.2                     # arrowhead size
    p1 = (tip_x + ah*math.cos(math.radians(tang_deg-150)),
          tip_y + ah*math.sin(math.radians(tang_deg-150)))
    p2 = (tip_x + ah*math.cos(math.radians(tang_deg+150)),
          tip_y + ah*math.sin(math.radians(tang_deg+150)))
    draw2.polygon([(tip_x, tip_y), p1, p2], fill=WHITE)

    # ── "V" lettermark ─────────────────────────────────────────────────────
    # Two thick strokes forming a V inside the loop
    vs   = int(size * 0.18)          # half-width of V
    vt   = cy - int(size * 0.14)     # top y of V
    vb   = cy + int(size * 0.14)     # bottom y of V
    vw   = max(3, lw - 1)
    draw2.line([(cx - vs, vt), (cx, vb)], fill=WHITE, width=vw)
    draw2.line([(cx + vs, vt), (cx, vb)], fill=WHITE, width=vw)

    return grad

# ── Generate all required sizes ─────────────────────────────────────────────
SIZES = {
    'icon-512.png':          512,
    'icon-192.png':          192,
    'apple-touch-icon.png':  180,
    'favicon-32.png':         32,
}

for filename, px in SIZES.items():
    icon = make_icon(px)
    icon.save(OUT / filename, 'PNG')
    print(f'  ✓ {filename}  ({px}×{px})')

# Also save a 32×32 favicon.ico
from PIL import Image as PILImage
icon32 = make_icon(32)
icon32.save(OUT / 'favicon.ico', format='ICO', sizes=[(32,32),(16,16)])
print('  ✓ favicon.ico')
print('Done.')
