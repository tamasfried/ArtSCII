# streamlit_Artscii.py
# A Streamlit app to generate ASCII art from images using the Artscii library.

from path import Path
import sys
import io

from PIL import Image, ImageOps
import streamlit as st

# Allow importing ascii_core.py from the parent directory.
sys.path.append(str(Path(__file__).resolve().parents[1]))
from ascii_core import to_ascii

# Set up the Streamlit app page
st.set_page_config(page_title = "Artscii", page_icon = "🎨", layout = "centered")

st.title("Artscii 🎨➡️🔡")
st.write("Convert images to ASCII art in your browser.")

