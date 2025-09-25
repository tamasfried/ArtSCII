# ArtSCII 🎨➡️🔡

**ArtSCII** is a Python project that converts images into ASCII art.  
The goal is to build both a **command-line tool** and a simple **web app** where users can upload an image and see it transformed into ASCII characters.

---

## Project Goals
- Convert images to ASCII using a small set of characters.
- Preserve the aspect ratio so the ASCII "image" looks correct.
- Provide options like:
  - Width of the output
  - Dense or simple character sets
  - Inverted brightness mapping
- Make a web interface (using Streamlit) so it can be used easily without the terminal.

---

## Current Status
This is a work in progress.  
- [x] Set up project structure and environment  
- [x] Core conversion logic  
- [x] Command-line interface  
- [ ] Web app  

---

## Command-Line Interface (CLI)

You can run the ArtSCII CLI tool directly from the terminal to convert images into ASCII art.

### Basic Usage
```bash
python artSCII.py path/to/image.jpg
```
This will convert the image and display the ASCII art in the terminal.

### Saving Output
By default, the ASCII art output is saved to `./Output/ascii_art.txt`. You can specify a different output path if you want.

### Optional Flags
- `--width`: Set the width of the ASCII output (default uses your terminal width)
- `--invert`: Invert brightness mapping
- `--dense`: Use a denser character set for more detail
- `--char-aspect`: Adjust the character aspect ratio for better proportions
- `--output`: Specify a custom output file path

### Example Command
```bash
python artSCII.py path/to/image.jpg --width 100 --invert --dense --char-aspect 0.5 --output ./Output/my_ascii_art.txt
```

---

The web app implementation (using Streamlit) will come next to provide an easy-to-use graphical interface.
