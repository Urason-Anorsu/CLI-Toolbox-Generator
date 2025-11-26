# ASCII Art Helpers
# Lightweight banner + block text utilities
# Simple Block Letters (A–Z, 0–9)
# Minimal alphabet, enough to make banners stand out

_SIMPLE_FONT = {
    "A": ["  ##  ",
          " #  # ",
          "#### ",
          "#  # ",
          "#  # "],
    "B": ["###  ",
          "#  # ",
          "###  ",
          "#  # ",
          "###  "],
    "C": [" ### ",
          "#    ",
          "#    ",
          "#    ",
          " ### "],
    # You can expand the dictionary as needed…
}

# fallback for unsupported chars
def _default_char(c):
    return [c * 4] * 5

def ascii_banner(text):
    """
    Render a block-letter ASCII banner.
    Only A-Z/0-9 are stylized; everything else prints simple blocks.
    """
    text = text.upper()
    rows = ["", "", "", "", ""]

    for ch in text:
        glyph = _SIMPLE_FONT.get(ch, _default_char(ch))
        for i in range(5):
            rows[i] += glyph[i] + "  "

    banner = "\n".join(rows)
    print(banner)
    return banner

def big_bar(text, width=60):
    """
    Draw a big section divider banner.
    """
    pad = (width - len(text) - 2)
    if pad < 0:
        pad = 2

    print("=" * width)
    print(f"= {text}{' ' * pad}=")
    print("=" * width)

def boxed(text):
    """
    Simple single-line box around text.
    """
    line = "+" + "-" * (len(text) + 2) + "+"
    print(line)
    print(f"| {text} |")
    print(line)
