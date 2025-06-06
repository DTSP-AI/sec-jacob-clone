import streamlit as st
from kodey_widget import render_kodey_widget
import base64
from streamlit_player import st_player

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
try:
    bg_image = get_base64_image("streamlit_agent/images/sec_jacob.png")
except FileNotFoundError:
    # Fallback: use a dark gradient instead of background image
    bg_image = ""

# Add custom CSS for ultra-modern dark theme with background image
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
}}

.stApp {{
    background-color: #0e1117;
    color: #fafafa;
}}

.main .block-container,
.main {{
    {f'background-image: url("data:image/png;base64,{bg_image}");' if bg_image else 'background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 50%, #16213e 100%);'}
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

.main .block-container::before {{
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(14, 17, 23, 0.35);
    backdrop-filter: blur(4px);
    z-index: 0;
}}

.main h1, .main p {{
    background-color: rgba(14, 17, 23, 0.8);
    color: #fafafa;
    padding: 1em;
    border-radius: 12px;
    margin: 1em 0;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    position: relative;
    z-index: 2;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
}}

#kodey-chat-container {{
    background-color: rgba(14, 17, 23, 0.65) !important;
    backdrop-filter: blur(20px) !important;
    border-radius: 20px !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5) !important;
    position: relative !important;
    z-index: 2 !important;
    padding: 1.5em !important;
    margin-top: 2em !important;
}}

.css-1d391kg {{
    background-color: rgba(14, 17, 23, 0.9);
}}

/* Apply rounded corners and shadows to widgets */
.stButton > button,
.stTextInput > div > input,
.stSelectbox > div > div,
.stSlider > div,
.stCheckbox > div {{
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}}

/* Customize buttons */
.stButton > button {{
    background-color: #1E90FF;
    color: #FFFFFF;
    border: none;
    padding: 0.5em 1em;
    transition: background-color 0.3s ease;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
}}

.stButton > button:hover {{
    background-color: #1C86EE;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
}}

/* Customize text inputs */
.stTextInput > div > input {{
    background-color: #1E1E1E;
    color: #FFFFFF;
    border: 1px solid #333333;
    padding: 0.5em;
    border-radius: 12px;
}}

/* Customize select boxes */
.stSelectbox > div > div {{
    background-color: #1E1E1E;
    color: #FFFFFF;
    border: 1px solid #333333;
    padding: 0.5em;
    border-radius: 12px;
}}

/* Customize sliders */
.stSlider > div {{
    background-color: #1E1E1E;
    padding: 0.5em;
    border-radius: 12px;
}}

/* Customize checkboxes */
.stCheckbox > div {{
    background-color: #1E1E1E;
    padding: 0.5em;
    border-radius: 12px;
}}

/* Structured output styling - Tables, DataFrames, Charts */
.stDataFrame {{
    background-color: rgba(30, 30, 30, 0.9) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    backdrop-filter: blur(10px) !important;
}}

.stTable {{
    background-color: rgba(30, 30, 30, 0.9) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    backdrop-filter: blur(10px) !important;
}}

/* Table headers and cells */
.stDataFrame table th,
.stTable table th {{
    background-color: rgba(30, 144, 255, 0.2) !important;
    color: #FFFFFF !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
}}

.stDataFrame table td,
.stTable table td {{
    background-color: rgba(30, 30, 30, 0.8) !important;
    color: #FFFFFF !important;
    border: 1px solid rgba(255, 255, 255, 0.05) !important;
}}

/* Charts and plots */
.stPlotlyChart,
.stPyplot,
.stAltairChart {{
    background-color: rgba(30, 30, 30, 0.9) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    backdrop-filter: blur(10px) !important;
    padding: 1em !important;
}}

/* Code blocks */
.stCode {{
    background-color: rgba(30, 30, 30, 0.9) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    backdrop-filter: blur(10px) !important;
}}

/* JSON display */
.stJson {{
    background-color: rgba(30, 30, 30, 0.9) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    backdrop-filter: blur(10px) !important;
}}

/* Metrics */
.stMetric {{
    background-color: rgba(30, 30, 30, 0.8) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    backdrop-filter: blur(10px) !important;
    padding: 1em !important;
}}

/* Music player expander - keep it minimal */
.streamlit-expanderHeader {{
    background-color: rgba(30, 30, 30, 0.6) !important;
    border-radius: 8px !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    font-size: 0.9em !important;
}}

.streamlit-expanderContent {{
    background-color: rgba(30, 30, 30, 0.8) !important;
    border-radius: 8px !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    padding: 0.5em !important;
}}

/* Minimize iframe styling for SoundCloud */
iframe[src*="soundcloud"] {{
    border-radius: 8px !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
}}
</style>
""", unsafe_allow_html=True)

# Main app
st.title("🤖 Kodey AI Chat Assistant")
st.write("Welcome to your AI coding assistant! Chat with Kodey below:")

# --- Music Toggle and Playback ---
st.markdown("## 🎶 Theme Music")
play_music = st.toggle("🔊 Play T2 Theme Music", value=False)

if play_music:
    # Minimalist music player
    with st.expander("🎵 T2 Theme (Click to expand player)", expanded=False):
        st_player(
            "https://soundcloud.com/rolando-jacinto-77409594/terminator-2-main-theme-joslin",
            config={
                'repeat': True,
                'autoPlay': True
            },
            height=166  # Minimal height for SoundCloud player
        )

# Render the Kodey chat widget
render_kodey_widget() 