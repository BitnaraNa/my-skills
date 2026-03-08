#!/usr/bin/env python3
"""Generate Android phone, 7-inch tablet, and 10-inch tablet mockup PNGs.

Style: Gold/champagne bezel frame with rounded corners and camera hole,
matching the included iPhone mockup aesthetic.

Usage: uv run generate-mockups.py
"""
# /// script
# requires-python = ">=3.10"
# dependencies = ["Pillow>=10.0"]
# ///

from PIL import Image, ImageDraw
from pathlib import Path

# Gold/champagne color palette (sampled from iPhone mockup)
BEZEL_OUTER = (191, 173, 138)      # outer edge
BEZEL_MAIN = (205, 190, 155)       # main bezel
BEZEL_INNER = (170, 155, 125)      # inner edge ring
BEZEL_HIGHLIGHT = (220, 208, 178)  # subtle highlight
CAMERA_RING = (60, 60, 65)         # camera hole outer
CAMERA_LENS = (30, 35, 50)         # camera hole inner
SCREEN_COLOR = (0, 0, 0)           # black screen


def rounded_rect(draw, bbox, radius, fill):
    """Draw a rounded rectangle."""
    x0, y0, x1, y1 = bbox
    # Clamp radius
    r = min(radius, (x1 - x0) // 2, (y1 - y0) // 2)
    # Corners
    draw.pieslice([x0, y0, x0 + 2 * r, y0 + 2 * r], 180, 270, fill=fill)
    draw.pieslice([x1 - 2 * r, y0, x1, y0 + 2 * r], 270, 360, fill=fill)
    draw.pieslice([x0, y1 - 2 * r, x0 + 2 * r, y1], 90, 180, fill=fill)
    draw.pieslice([x1 - 2 * r, y1 - 2 * r, x1, y1], 0, 90, fill=fill)
    # Rects to fill gaps
    draw.rectangle([x0 + r, y0, x1 - r, y0 + r], fill=fill)
    draw.rectangle([x0 + r, y1 - r, x1 - r, y1], fill=fill)
    draw.rectangle([x0, y0 + r, x0 + r, y1 - r], fill=fill)
    draw.rectangle([x1 - r, y0 + r, x1, y1 - r], fill=fill)
    draw.rectangle([x0 + r, y0 + r, x1 - r, y1 - r], fill=fill)


def draw_side_buttons(draw, w, h, bezel):
    """Draw subtle side buttons (power, volume) on the right/left edges."""
    btn_w = max(3, bezel // 8)

    # Power button - right side
    pw_h = int(h * 0.06)
    pw_top = int(h * 0.22)
    draw.rectangle([w - btn_w, pw_top, w, pw_top + pw_h], fill=BEZEL_OUTER)

    # Volume up - left side
    vu_h = int(h * 0.045)
    vu_top = int(h * 0.18)
    draw.rectangle([0, vu_top, btn_w, vu_top + vu_h], fill=BEZEL_OUTER)

    # Volume down - left side
    vd_h = int(h * 0.045)
    vd_top = int(h * 0.24)
    draw.rectangle([0, vd_top, btn_w, vd_top + vd_h], fill=BEZEL_OUTER)


def generate_mockup(width, height, corner_radius, bezel, screen_radius,
                    camera_y_ratio=0.022, camera_size=None, label="device"):
    """Generate a single device mockup.

    Returns (image, screen_measurements) where screen_measurements is a dict
    with keys: sc_l, sc_t, sc_w, sc_h, sc_rx, sc_ry (all in pixels).
    """
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Outer bezel (full device shape)
    rounded_rect(draw, (0, 0, width, height), corner_radius, BEZEL_OUTER)

    # Main bezel body (slightly inset)
    inset = max(2, bezel // 12)
    rounded_rect(draw, (inset, inset, width - inset, height - inset),
                 corner_radius - inset, BEZEL_MAIN)

    # Highlight strip on left edge for 3D feel
    hl_w = max(2, bezel // 6)
    for i in range(hl_w):
        alpha = int(40 * (1 - i / hl_w))
        r, g, b = BEZEL_HIGHLIGHT
        col = (r, g, b, alpha)
        draw.line([(inset + i, corner_radius), (inset + i, height - corner_radius)],
                  fill=col)

    # Side buttons
    draw_side_buttons(draw, width, height, bezel)

    # Inner bezel ring (around screen)
    inner_inset = bezel - max(3, bezel // 5)
    rounded_rect(draw,
                 (inner_inset, inner_inset, width - inner_inset, height - inner_inset),
                 screen_radius + max(2, bezel // 8), BEZEL_INNER)

    # Screen area
    sc_l = bezel
    sc_t = bezel
    sc_r = width - bezel
    sc_b = height - bezel
    sc_w = sc_r - sc_l
    sc_h = sc_b - sc_t
    rounded_rect(draw, (sc_l, sc_t, sc_r, sc_b), screen_radius, SCREEN_COLOR)

    # Camera hole (centered horizontally, near top)
    if camera_size is None:
        camera_size = max(16, int(width * 0.025))
    cam_x = width // 2
    cam_y = sc_t + int(sc_h * camera_y_ratio) + camera_size
    # Outer ring
    draw.ellipse([cam_x - camera_size - 3, cam_y - camera_size - 3,
                  cam_x + camera_size + 3, cam_y + camera_size + 3],
                 fill=CAMERA_RING)
    # Lens
    draw.ellipse([cam_x - camera_size, cam_y - camera_size,
                  cam_x + camera_size, cam_y + camera_size],
                 fill=CAMERA_LENS)
    # Lens highlight
    hl_size = max(3, camera_size // 3)
    hl_offset = max(2, camera_size // 4)
    draw.ellipse([cam_x - hl_offset - hl_size // 2, cam_y - hl_offset - hl_size // 2,
                  cam_x - hl_offset + hl_size // 2, cam_y - hl_offset + hl_size // 2],
                 fill=(80, 90, 120))

    measurements = {
        "label": label,
        "mk_w": width,
        "mk_h": height,
        "sc_l": sc_l,
        "sc_t": sc_t,
        "sc_w": sc_w,
        "sc_h": sc_h,
        "sc_rx": screen_radius,
        "sc_ry": screen_radius,
    }

    return img, measurements


def print_typescript(m):
    """Print TypeScript constants for the mockup measurements."""
    label = m["label"]
    mk_w, mk_h = m["mk_w"], m["mk_h"]
    print(f"// {label} mockup measurements")
    print(f"const {label.upper().replace('-', '_')}_MK = {{")
    print(f"  W: {mk_w}, H: {mk_h},")
    print(f"  SC_L: ({m['sc_l']} / {mk_w}) * 100,   // {m['sc_l'] / mk_w * 100:.2f}%")
    print(f"  SC_T: ({m['sc_t']} / {mk_h}) * 100,   // {m['sc_t'] / mk_h * 100:.2f}%")
    print(f"  SC_W: ({m['sc_w']} / {mk_w}) * 100,   // {m['sc_w'] / mk_w * 100:.2f}%")
    print(f"  SC_H: ({m['sc_h']} / {mk_h}) * 100,   // {m['sc_h'] / mk_h * 100:.2f}%")
    print(f"  SC_RX: ({m['sc_rx']} / {m['sc_w']}) * 100, // {m['sc_rx'] / m['sc_w'] * 100:.2f}%")
    print(f"  SC_RY: ({m['sc_ry']} / {m['sc_h']}) * 100, // {m['sc_ry'] / m['sc_h'] * 100:.2f}%")
    print(f"}};")
    print()


def main():
    out_dir = Path(__file__).parent

    # --- Android Phone ---
    # Similar proportions to iPhone mockup but slightly different aspect ratio
    # Screen: 1080x1920 => mockup adds bezel
    phone_bezel = 42
    phone_w = 920 + phone_bezel * 2   # 1004
    phone_h = 2000 + phone_bezel * 2  # 2084
    phone_img, phone_m = generate_mockup(
        width=phone_w, height=phone_h,
        corner_radius=110, bezel=phone_bezel, screen_radius=80,
        camera_y_ratio=0.018, camera_size=14,
        label="android-phone",
    )
    phone_img.save(out_dir / "mockup-android.png")
    print(f"Saved mockup-android.png ({phone_w}x{phone_h})")
    print_typescript(phone_m)

    # --- 7-inch Tablet ---
    # Screen: 1200x1920 => wider aspect ratio
    tab7_bezel = 48
    tab7_w = 1060 + tab7_bezel * 2   # 1156
    tab7_h = 1780 + tab7_bezel * 2   # 1876
    tab7_img, tab7_m = generate_mockup(
        width=tab7_w, height=tab7_h,
        corner_radius=70, bezel=tab7_bezel, screen_radius=40,
        camera_y_ratio=0.016, camera_size=12,
        label="7inch-tablet",
    )
    tab7_img.save(out_dir / "mockup-7inch.png")
    print(f"Saved mockup-7inch.png ({tab7_w}x{tab7_h})")
    print_typescript(tab7_m)

    # --- 10-inch Tablet ---
    # Screen: 1600x2560 => larger
    tab10_bezel = 56
    tab10_w = 1400 + tab10_bezel * 2   # 1512
    tab10_h = 2200 + tab10_bezel * 2   # 2312
    tab10_img, tab10_m = generate_mockup(
        width=tab10_w, height=tab10_h,
        corner_radius=80, bezel=tab10_bezel, screen_radius=44,
        camera_y_ratio=0.014, camera_size=14,
        label="10inch-tablet",
    )
    tab10_img.save(out_dir / "mockup-10inch.png")
    print(f"Saved mockup-10inch.png ({tab10_w}x{tab10_h})")
    print_typescript(tab10_m)

    print("Done! Copy these files to your project's public/ directory.")


if __name__ == "__main__":
    main()
