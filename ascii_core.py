# ascii_core.py - Core ASCII Art Generation Module
# This module provides functions to generate ASCII art from text input.

from typing import List, Tuple
from PIL import Image

# define a simple ASCII character set as character ramps
# Simple ramp from light to dark. Simple is faster, dense is slower but more detailed.
RAMP_SIMPLE = " .:-=+*#%@"
RAMP_DENSE = " .'`^\",:;Il!i~+_-?][}{1)(|/\\tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

# Function to work out how to resize the image so it looks correct as ASCII
# Preseve aspect ratio, but account for the fact that characters are taller than they are wide
def _target_size(img: Image.Image, width: int, char_aspect: float = 0.5) -> Tuple[int, int]:
    if width <= 0:
        width = 100  # default width if invalid
    w, h = img.size
    aspect = h / max(1, w)  # avoid division by zero
    height = max(1, int(width * aspect * char_aspect))
    return width, height