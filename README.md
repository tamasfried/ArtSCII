# ArtSCII 🎨➡️🔡

ArtSCII is a Python project that converts images into ASCII art. It takes an input image and transforms it into a text representation using ASCII characters, allowing you to visualize images in a unique and artistic way using only text.

## Project Goals

- Convert images to ASCII art with customizable width and character sets.
- Provide options to invert brightness and adjust character aspect ratio.
- Allow saving the ASCII art output to a text file.
- Create a simple and user-friendly command-line interface (CLI).

## Current Status

- [x] Basic image to ASCII conversion
- [x] Width adjustment
- [x] Brightness inversion
- [x] Dense character set option
- [x] Character aspect ratio adjustment
- [x] Output to file option
- [ ] Web app interface (coming soon)

## CLI Usage

```bash
python artSCII.py path/to/image.jpg --width 100 --invert --dense --char-aspect 0.6 --output output.txt
```

### Optional Flags

- `--width` or `-w`: Specify the width of the ASCII output. Defaults to terminal width if not set.
- `--invert` or `-i`: Invert brightness mapping.
- `--dense` or `-d`: Use a denser character set for more detail.
- `--char-aspect` or `-c`: Adjust the character aspect ratio for better proportions (default 0.5).
- `--output` or `-o`: Save ASCII art to a text file instead of printing to the console.

## Note

A web app version of ArtSCII is in development and will be released soon!
