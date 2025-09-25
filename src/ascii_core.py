# ascii_core.py - Core ASCII Art Generation Module
# This module provides functions to generate ASCII art from text input.

from typing import List, Tuple
from PIL import Image

# define a simple ASCII character set as character ramps
# Simple ramp from light to dark. Simple is faster, dense is slower but more detailed.
RAMP_SIMPLE = " .:-=+*#%@"
RAMP_DENSE = " .'`^\",:;Il!i~+_-?][}{1)(|/\\tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

# Function to work out how to resize the image so it looks correct as ASCII
# Preserve aspect ratio, but account for the fact that characters are taller than they are wide
def _target_size(img: Image.Image, width: int, char_aspect: float = 0.5) -> Tuple[int, int]:
    if width <= 0:
        width = 100  # default width if invalid
    w, h = img.size
    aspect = h / max(1, w)  # avoid division by zero
    height = max(1, int(width * aspect * char_aspect))
    return width, height

# Work out how bright a pixel is. (Black == 0, white == 255)
def _luminance(r: int, g: int, b: int) -> int:
    # Weighted sum to match how human eyes perceive brightness (green is more sensitive, then red, then blue)
    return int(0.2126 * r + 0.7152 * g + 0.0722 * b)

# Pick the correct from the ramp based on brightness
def _pick_char(lum: int, ramp: str) -> str:
    idx = int((lum / 255) * (len(ramp) - 1 )) # scale 0-255 to ramp length
    return ramp[idx] # return the character at that index

# Convert the image to ASCII (returns a list of strings, one per line)
def to_ascii(img: Image.Image, width: int = 100, invert: bool = False, dense: bool = False) -> List[str]:
    # Choose which ramp to use
    ramp = RAMP_DENSE if dense else RAMP_SIMPLE
    if invert:
        ramp = ramp[::-1] # reverse the ramp for inversion (flipped light/dark)
    
    # Work out target size and create a resized greyscale version of the image
    W, H = _target_size(img, width)
    grey = img.convert("L").resize((W, H), Image.BICUBIC)  # convert to greyscale and resize
    px = grey.load()  # load pixel data

    # Generate ASCII art line by line
    lines: List[str] = []
    for y in range(H):
        row_chars = []
        for x in range(W):
            lum = px[x, y]  # get luminance (0-255)
            row_chars.append(_pick_char(lum, ramp))  # pick corresponding ASCII character
        lines.append("".join(row_chars))  # join characters into a string for the line
    return lines  # return the list of lines representing the ASCII art



