# streamlit_Artscii.py
# A Streamlit app to generate ASCII art from images using the Artscii library.

from pathlib import Path
import sys
import io

from PIL import Image, ImageOps
import streamlit as st

# Allow importing ascii_core.py from the parent directory.
# Add ../src (where ascii_core.py lives) to the import path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_DIR))

from ascii_core import to_ascii

# Set up the Streamlit app page
st.set_page_config(
    page_title = "Artscii",
    page_icon = "🎨",
    layout = "centered")

st.title("Artscii 🎨➡️🔡")
st.write("Convert images to ASCII art in your browser.")

with st.expander("Options", expanded=True):
    width = st.slider(
        "Width (Characters)",
        min_value = 40,
        max_value = 200,
        value = 100,
        step = 5
    )
    invert = st.checkbox(
        "Invert (Better for dark images)",
        value = False
    )
    dense = st.checkbox(
        "Dense (More characters, more detail)",
        value = False
    )

# File uploader interface
uploaded = st.file_uploader(
    "Upload an image to convert to ASCII art (PNG or JPG)",
    type = ["png", "jpg", "jpeg"]
)

# Convert image on upload
if uploaded is not None:
    # Read uploaded file into a PIL Image
    img_bytes = uploaded.read()
    img = Image.open(io.BytesIO(img_bytes))
    img = ImageOps.exif_transpose(img) # Correct orientation using EXIF data

    st.subheader("Preview")
    st.image(img, width = "stretch")

    # Convert to ASCII using shared core
    lines = to_ascii(img=img,
                     width=width,
                     invert=invert,
                     dense=dense
                     )
    ascii_text = "\n".join(lines)

    st.subheader("ASCII Output")
    st.code(ascii_text, language="text")

    # Download button for output
    st.download_button(
        label = "Download ASCII as .txt",
        data = ascii_text.encode("utf-8"),
        file_name = f"{Path(uploaded.name).stem}_ascii.txt",
        mime = "text/plain",
    )
else:
    st.info("Please upload an image file to get started.")
