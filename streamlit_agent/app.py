import streamlit as st
from kodey_widget import render_kodey_widget
import base64

# Set page config
st.set_page_config(
    page_title="Kodey AI Chat",
    page_icon="🤖",
    layout="wide"
)

# Function to encode image to base64
@st.cache_data
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Get the background image
bg_image = get_base64_image("sec_jacob.png")

# Add custom CSS for background image
st.markdown(f"""
<style>
.main .block-container {{
    background-image: url("data:image/png;base64,{bg_image}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    min-height: 100vh;
}}

.main {{
    background-image: url("data:image/png;base64,{bg_image}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* Make text more readable with background */
.main h1, .main p {{
    background-color: rgba(255, 255, 255, 0.8);
    padding: 10px;
    border-radius: 5px;
    margin: 10px 0;
}}
</style>
""", unsafe_allow_html=True)

# Main app
st.title("🤖 Kodey AI Chat Assistant")
st.write("Welcome to your AI coding assistant! Chat with Kodey below:")

# Render the Kodey chat widget
render_kodey_widget() 