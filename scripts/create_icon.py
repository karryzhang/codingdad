#!/usr/bin/env python3
"""Generate VocabLoop app icons – smooth antialiased rendering via supersampling."""
import math, pathlib
from PIL import Image, ImageDraw

OUT = pathlib.Path(__file__).parent.parent / 'english' / 'icons'
OUT.mkdir(exist_ok=True)

# ── Brand colours ────────────────────────────────────────────────────────────
# Bright cartoon-style gradient: sky-blue → app-brand-blue
# Thick white strokes stay clearly visible (3:1+ contrast on graphic elements)
BG_TOP  = (74, 144, 255)   # #4a90ff  bright sky-blue (playful, modern)
BG_BOT  = (37,  99, 235)   # #2563eb  brand blue (grounding)
WHITE   = (255, 255, 255)

SCALE = 4   # supersampling factor for smooth edges

def make_icon(size):
    S      = size * SCALE          # render at 4× resolution
    radius = (size // 5) * SCALE   # iOS-style corner radius

    # ── Gradient background (top-to-bottom) ─────────────────────────────────
    grad = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    gd   = ImageDraw.Draw(grad)
    for y in range(S):
        t   = y / S
        col = tuple(int(BG_TOP[i] + (BG_BOT[i] - BG_TOP[i]) * t) for i in range(3)) + (255,)
        gd.line([(0, y), (S, y)], fill=col)

    # ── Rounded-rect mask ────────────────────────────────────────────────────
    mask = Image.new('L', (S, S), 0)
    md   = ImageDraw.Draw(mask)
    md.rounded_rectangle([0, 0, S - 1, S - 1], radius=radius, fill=255)
    grad.putalpha(mask)

    draw = ImageDraw.Draw(grad)
    cx, cy = S // 2, S // 2
    lw = max(5, size // 20) * SCALE      # line width, scaled

    # ── Loop arrow arc (300° sweep, gap at bottom-right) ────────────────────
    ar     = int(S * 0.341)
    arc_bb = [cx - ar, cy - ar, cx + ar, cy + ar]
    draw.arc(arc_bb, start=105, end=390, fill=WHITE, width=lw)

    # Arrowhead at arc END (30°) – symmetric about tangent, centred on arc line
    aend_rad = math.radians(30)
    td       = 30 + 90          # 120° – forward tangent direction
    ah       = lw * 2.6         # arrow height (along tangent)
    aw       = lw * 0.95        # arrow half-width (along radial / perp to tangent)

    fwd_x  = math.cos(math.radians(td))      # tangent forward  (−0.5, +0.866)
    fwd_y  = math.sin(math.radians(td))
    prp_x  = math.cos(math.radians(td - 90)) # radial outward at 30° (+0.866, +0.5)
    prp_y  = math.sin(math.radians(td - 90))

    # Arc endpoint on the arc centre-line
    arc_px = cx + ar * math.cos(aend_rad)
    arc_py = cy + ar * math.sin(aend_rad)

    # Shift slightly inward (toward circle centre) for visual alignment
    inward = lw * 0.35
    ix = -math.cos(aend_rad) * inward
    iy = -math.sin(aend_rad) * inward

    # Triangle: centroid sits at (arc_px+ix, arc_py+iy)
    #   → tip  = centroid + (2/3)*ah*forward
    #   → base = centroid − (1/3)*ah*forward  ± aw*perpendicular
    cx0, cy0 = arc_px + ix, arc_py + iy
    tip_x  = cx0 + (2 * ah / 3) * fwd_x
    tip_y  = cy0 + (2 * ah / 3) * fwd_y
    base_x = cx0 - (ah / 3) * fwd_x
    base_y = cy0 - (ah / 3) * fwd_y
    p1 = (base_x + aw * prp_x, base_y + aw * prp_y)
    p2 = (base_x - aw * prp_x, base_y - aw * prp_y)
    draw.polygon([(tip_x, tip_y), p1, p2], fill=WHITE)

    # ── "V" lettermark – thicker polyline with curved joint ─────────────────
    vs  = int(S * 0.17)           # half-width of V
    vt  = cy - int(S * 0.13)     # top y (open ends)
    vb  = cy + int(S * 0.14)     # bottom y (tip)
    vlw = int(lw * 1.4)          # V strokes noticeably bolder than arc
    pts = [(cx - vs, vt), (cx, vb), (cx + vs, vt)]
    draw.line(pts, fill=WHITE, width=vlw, joint='curve')

    # Round caps at the two open top ends of V
    r = vlw // 2
    draw.ellipse([cx - vs - r, vt - r, cx - vs + r, vt + r], fill=WHITE)
    draw.ellipse([cx + vs - r, vt - r, cx + vs + r, vt + r], fill=WHITE)

    # ── Downsample with LANCZOS for smooth antialiasing ──────────────────────
    return grad.resize((size, size), Image.LANCZOS)

def make_favicon(size):
    """Small-size icon: V lettermark only, no arc (too small to read)."""
    S      = size * SCALE
    radius = (size // 5) * SCALE

    grad = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    gd   = ImageDraw.Draw(grad)
    for y in range(S):
        t   = y / S
        col = tuple(int(BG_TOP[i] + (BG_BOT[i] - BG_TOP[i]) * t) for i in range(3)) + (255,)
        gd.line([(0, y), (S, y)], fill=col)

    mask = Image.new('L', (S, S), 0)
    md   = ImageDraw.Draw(mask)
    md.rounded_rectangle([0, 0, S - 1, S - 1], radius=radius, fill=255)
    grad.putalpha(mask)

    draw = ImageDraw.Draw(grad)
    cx, cy = S // 2, S // 2
    lw = max(5, size // 20) * SCALE
    vlw = int(lw * 1.4)

    # V centred and slightly larger to fill the space
    vs  = int(S * 0.28)
    vt  = cy - int(S * 0.20)
    vb  = cy + int(S * 0.20)
    pts = [(cx - vs, vt), (cx, vb), (cx + vs, vt)]
    draw.line(pts, fill=WHITE, width=vlw, joint='curve')
    r = vlw // 2
    draw.ellipse([cx - vs - r, vt - r, cx - vs + r, vt + r], fill=WHITE)
    draw.ellipse([cx + vs - r, vt - r, cx + vs + r, vt + r], fill=WHITE)

    return grad.resize((size, size), Image.LANCZOS)

# ── Generate all sizes ───────────────────────────────────────────────────────
for filename, px in [('icon-512.png', 512), ('icon-192.png', 192), ('apple-touch-icon.png', 180)]:
    make_icon(px).save(OUT / filename, 'PNG')
    print(f'  ✓ {filename}  ({px}×{px})')

# Small favicons: V only
make_favicon(32).save(OUT / 'favicon-32.png', 'PNG')
print('  ✓ favicon-32.png  (32×32, V only)')

make_favicon(32).save(OUT / 'favicon.ico', format='ICO', sizes=[(32, 32), (16, 16)])
print('  ✓ favicon.ico  (V only)')
print('Done.')
