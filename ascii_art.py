# ascii_art.py - CLI for ASCII Art Generation
# This script loads an image file and converts it to ASCII art using the ascii_core module.

from pathlib import Path        # for file path handling
import argparse                 # for command line argument parsing
from PIL import Image, ImageOps # for image processing
from ascii_core import to_ascii # import the core ASCII conversion function
import shutil                   # for terminal size detection

# Set up command line argument parsing
def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="ArtSCII",
        description="Convert an image to greyscale ASCII art."
    )

    # Get terminal size for default width
    term_width = shutil.get_terminal_size((100, 20)).columns
    p.add_argument("--width", type=int, default=term_width,
                help=f"Output width in characters (default: {term_width})")
    p.add_argument("image", help="Path to the input image (jpg, png, etc.)") 
    p.add_argument("--invert", action="store_true", help="Invert brightness mapping (better for dark terminals)")
    p.add_argument("--dense", action="store_true", help="Use a denser character set for more detail")
    p.add_argument("--output", "-o", default=None, help="Save ASCII to a text file instead of printing")
    return p

def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()

    # Validate the input image path
    img_path = Path(args.image)
    if not img_path.exists() or not img_path.is_file():
        parser.error(f"Image file '{img_path}' does not exist or is not a file.")

    # Try to open the image
    try:
        img = Image.open(img_path)
        img = ImageOps.exif_transpose(img)  # correct orientation using EXIF data
    except Exception as e:
        parser.error(f"Failed to open image: {e}")
    
    # Convert the image to ASCII art with core function
    lines = to_ascii(
        img = img,
        width = args.width,
        invert = args.invert,
        dense = args.dense,
    )

    # Output the result to console or file
    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        try: 
            out_path.write_text("\n".join(lines), encoding = "utf-8")
        except Exception as e:
            parser.error(f"Failed to write to output file: {e}")
        else:
            print(f"Saved ASCII art to '{out_path}'.")
    else:
        print("\n".join(lines))

if __name__ == "__main__":
    main()
