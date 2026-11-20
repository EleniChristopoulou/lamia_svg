#!/usr/bin/env python3
"""
Recolor an SVG's embedded PNG image to one solid color.

The SVG structure and the image's transparency are preserved.
Requires: pip install pillow

Usage:
    python recolor_svg.py input.svg output.svg
    python recolor_svg.py input.svg output.svg --color "#87CEEB"
"""

import argparse
import base64
import io
import re
import sys
from pathlib import Path

from PIL import Image


def recolor_embedded_png(svg_text: str, color: str) -> str:
    """Recolor every visible pixel in an embedded PNG, preserving its alpha."""
    match = re.search(
        r'(data:image/png;base64,)([A-Za-z0-9+/=\s]+)',
        svg_text,
        flags=re.IGNORECASE,
    )
    if not match:
        raise ValueError("No embedded PNG (data:image/png;base64,...) was found.")

    color = color.lstrip("#")
    if not re.fullmatch(r"[0-9a-fA-F]{6}", color):
        raise ValueError("Color must be a 6-digit hex value, e.g. #87CEEB.")

    red, green, blue = (int(color[i:i + 2], 16) for i in (0, 2, 4))

    encoded_png = re.sub(r"\s+", "", match.group(2))
    image_bytes = base64.b64decode(encoded_png)

    with Image.open(io.BytesIO(image_bytes)) as image:
        image = image.convert("RGBA")
        alpha = image.getchannel("A")

        # Apply the same RGB color to every pixel; retain original transparency.
        recolored = Image.new("RGBA", image.size, (red, green, blue, 0))
        recolored.putalpha(alpha)

        output = io.BytesIO()
        recolored.save(output, format="PNG")

    new_base64 = base64.b64encode(output.getvalue()).decode("ascii")
    return (
        svg_text[:match.start(2)]
        + new_base64
        + svg_text[match.end(2):]
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Make an SVG's embedded PNG one solid color."
    )
    parser.add_argument("input", help="Path to the original SVG file")
    parser.add_argument("output", help="Path for the recolored SVG file")
    parser.add_argument(
        "--color",
        default="#87CEEB",
        help="Target color in hex (default: #87CEEB, sky blue)",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    try:
        svg_text = input_path.read_text(encoding="utf-8")
        result = recolor_embedded_png(svg_text, args.color)
        output_path.write_text(result, encoding="utf-8")
    except (OSError, ValueError, base64.binascii.Error) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"Recolored SVG saved to: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
