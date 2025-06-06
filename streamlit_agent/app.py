import streamlit as st
import base64
import os
from kodey_widget import render_kodey_widget

# Set page configuration
st.set_page_config(page_title="Jacob 2.0", layout="wide")

# Function to encode image to base64
@st.cache_data
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Attempt to load background image
bg_image = ""
possible_paths = [
    "streamlit_agent/images/sec_jacob.png",
    "images/sec_jacob.png",
    "./streamlit_agent/images/sec_jacob.png",
    os.path.join(os.path.dirname(__file__), "images", "sec_jacob.png")
]

for path in possible_paths:
    if os.path.exists(path):
        bg_image = get_base64_image(path)
        break

# Inject custom CSS
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
    min-height: 100vh;
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
    position: sticky !important;
    top: 20px !important;
    background-color: rgba(14, 17, 23, 0.85) !important;
    backdrop-filter: blur(20px) !important;
    border-radius: 20px !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6) !important;
    padding: 1.5em !important;
    margin: 2em 0 !important;
    z-index: 50 !important;
    max-height: 70vh !important;
    overflow-y: auto !important;
}}

#kodey-chat-container .stChatMessage {{
    background-color: rgba(30, 30, 30, 0.7) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    margin: 8px 0 !important;
    padding: 12px !important;
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

/* Remove old music player styles - no longer needed */

/* Sticky Chat Input */
.stChatInput,
.stChatInputContainer,
[data-testid="stChatInput"],
[data-testid="stChatInputContainer"] {{
    position: sticky !important;
    bottom: 20px !important;
    z-index: 100 !important;
    background-color: rgba(14, 17, 23, 0.9) !important;
    backdrop-filter: blur(15px) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    margin: 10px 0 !important;
}}

/* Chat input text styling */
.stChatInput input,
[data-testid="stChatInput"] input {{
    background-color: rgba(30, 30, 30, 0.8) !important;
    color: #FFFFFF !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    border-radius: 10px !important;
}}

/* Sticky Chat Thread with Dark Translucent Background */
#kodey-chat-container {{
    position: sticky !important;
    top: 20px !important;
    background-color: rgba(14, 17, 23, 0.85) !important;
    backdrop-filter: blur(20px) !important;
    border-radius: 20px !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6) !important;
    padding: 1.5em !important;
    margin: 2em 0 !important;
    z-index: 50 !important;
    max-height: 70vh !important;
    overflow-y: auto !important;
}}

/* Chat messages styling for readability */
#kodey-chat-container .stChatMessage {{
    background-color: rgba(30, 30, 30, 0.7) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    margin: 8px 0 !important;
    padding: 12px !important;
}}

/* SoundCloud player styling */
#soundcloud-player {{
    position: fixed;
    bottom: 20px;
    left: 20px;
    width: 280px;
    height: 75px;
    opacity: 0.8;
    z-index: 100;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
}}

#soundcloud-player iframe {{
    border-radius: 12px;
}}

/* Responsive design for mobile */
@media (max-width: 768px) {{
    #soundcloud-player {{
        width: 240px;
        height: 60px;
        bottom: 10px;
        left: 10px;
    }}
}}
</style>
""", unsafe_allow_html=True)

# Main content
st.title("Jacob 2.0")
st.write("Welcome to your AI coding assistant! Chat with Kodey below:")

# Render the Kodey chat widget
render_kodey_widget()

# Embed SoundCloud player
st.markdown("""
<div id="soundcloud-player">
    <iframe width="100%" height="100%" scrolling="no" frameborder="no" allow="autoplay"
        src="https://w.soundcloud.com/player/?url=https%3A//soundcloud.com/rolando-jacinto-77409594/terminator-2-main-theme-joslin&color=%23000000&auto_play=true&hide_related=true&show_comments=false&show_user=false&show_reposts=false&show_teaser=false&visual=false">
    </iframe>
</div>
""", unsafe_allow_html=True) 