import streamlit as st
import base64
import os
from kodey_widget import render_kodey_widget

# Configure the Streamlit app layout
st.set_page_config(page_title="JACOB 2.0", layout="wide")

# Function to encode the background image file to base64 for embedding in CSS
@st.cache_data
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Load the uploaded background image
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "images", "sec_jacob.png")

try:
    bg_image = get_base64_image(image_path)
    print(f"Successfully loaded background image from: {image_path}")
except FileNotFoundError:
    print(f"Background image not found at: {image_path}")
    bg_image = ""

# Inject all styling and layout customization via HTML <style> tag
st.markdown(f"""
<style>
/* Import modern font */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

/* Add Omicron font face */
@font-face {{
    font-family: 'Omicron';
    src: url('/fonts/omicron.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
    font-display: swap;
}}

/* Apply custom font across all components */
html, body, [class*="css"] {{
    font-family: 'Omicron', 'Inter', sans-serif;
}}

/* Set the global background and text color */
.stApp {{
    background-color: #0e1117; /* deep dark background */
    color: #fafafa; /* light text for contrast */
}}

/* Apply background image styling on main content block - Multiple selectors for better targeting */
.stApp,
.main,
.main .block-container,
[data-testid="stAppViewContainer"],
.css-18e3th9,
.css-1d391kg {{
    {f'background-image: url("data:image/png;base64,{bg_image}") !important;' if bg_image else 'background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 50%, #16213e 100%) !important;'}
    background-size: cover !important;          /* ensure it covers full area */
    background-position: center !important;     /* center the image */
    background-repeat: no-repeat !important;    /* no tiling */
    background-attachment: fixed !important;    /* stay fixed on scroll */
    position: relative !important;              /* necessary for z-index layering */
    min-height: 100vh !important;
}}

/* Add a dark transparent overlay over background image for readability */
.stApp::before,
.main::before,
.main .block-container::before {{
    content: '';
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(14, 17, 23, 0.45); /* dark tint layer */
    backdrop-filter: blur(4px);        /* subtle blur to reduce noise */
    z-index: 0;
    pointer-events: none; /* Allow clicking through overlay */
}}

/* Style the main title text */
h1 {{
    font-size: 1.12rem !important;               /* reduced by ~20% from 1.4rem */
    font-weight: 500 !important;                /* medium weight */
    margin-top: 10px !important;                /* spacing from top */
    margin-bottom: 4px !important;
    padding: 0.5em 1em !important;
    background-color: rgba(14, 17, 23, 0.6);     /* semi-transparent background */
    border-radius: 12px;
    display: inline-block;
    position: relative;
    z-index: 2;
    backdrop-filter: blur(10px);                 /* background blur */
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);   /* subtle box shadow */
}}

/* Style subtitle or description */
p {{
    font-size: 0.85rem !important;
    color: #ccc;                                 /* lighter gray */
    margin-top: -10px !important;                /* pull closer to heading */
    margin-bottom: 20px !important;
    padding-left: 1em;
    position: relative;
    z-index: 2;
}}

/* Style the container that holds the chat widget */
#kodey-chat-container {{
    position: sticky !important;
    top: 10px !important;                        /* sticks near top on scroll */
    background-color: rgba(14, 17, 23, 0.75) !important; /* translucent black */
    backdrop-filter: blur(10px) !important;     /* blurred background */
    border-radius: 12px !important;             /* rounded corners */
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5) !important; /* subtle box shadow */
    padding: 1em !important;
    margin-top: 1em !important;
    max-height: 70vh !important;                /* responsive height */
    overflow-y: auto !important;                /* scroll within if overflow */
    z-index: 2;
}}

/* Style each chat message block (optional if needed) */
#kodey-chat-container .stChatMessage {{
    background-color: rgba(30, 30, 30, 0.7) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    margin: 8px 0 !important;
    padding: 12px !important;
}}

/* Make Kodey widget internal elements translucent */
#kodey-chat-container * {{
    background-color: transparent !important;
}}

/* Kodey widget specific styling for translucency */
#kodey-chat-container .chat-message,
#kodey-chat-container .message,
#kodey-chat-container .chat-input,
#kodey-chat-container input,
#kodey-chat-container textarea,
#kodey-chat-container .chat-bubble,
#kodey-chat-container .user-message,
#kodey-chat-container .bot-message,
#kodey-chat-container .ai-message {{
    background-color: rgba(30, 30, 30, 0.6) !important; /* translucent backgrounds */
    border-radius: 12px !important;             /* rounded corners */
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    color: #ffffff !important;
    backdrop-filter: blur(10px) !important;     /* blurred background */
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5) !important; /* subtle box shadows */
}}

/* Chat input field in Kodey widget */
#kodey-chat-container input[type="text"],
#kodey-chat-container textarea {{
    background-color: rgba(20, 20, 20, 0.8) !important; /* translucent backgrounds */
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    color: #ffffff !important;
    border-radius: 12px !important;             /* rounded corners */
    padding: 8px 12px !important;
    backdrop-filter: blur(10px) !important;     /* blurred background */
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5) !important; /* subtle box shadows */
}}

/* Kodey widget buttons */
#kodey-chat-container button {{
    background-color: rgba(30, 144, 255, 0.8) !important;
    border: none !important;
    border-radius: 8px !important;
    color: #ffffff !important;
    padding: 6px 12px !important;
    transition: all 0.3s ease !important;
}}

#kodey-chat-container button:hover {{
    background-color: rgba(30, 144, 255, 1) !important;
    box-shadow: 0 4px 12px rgba(30, 144, 255, 0.3) !important;
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

/* Button styling (i.e., submit/send) */
.stButton > button {{
    background-color: #1E90FF; /* Dodger Blue */
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

/* SoundCloud audio player: fixed and subtle */
iframe[src*="soundcloud"] {{
    position: fixed;                 /* float at screen bottom */
    bottom: 10px;
    left: 10px;
    width: 260px;
    height: 80px;
    opacity: 0.5;                   /* semi-transparent */
    z-index: 99;
    border-radius: 10px;
    border: none;
}}
</style>
""", unsafe_allow_html=True)

# ---------------------
# Page Body
# ---------------------

# Title and subtitle
st.markdown("# JACOB 2.0")
st.markdown("The Beginning of the Dawn of the Machines")

# Render the Kodey widget
render_kodey_widget()

# Embed the SoundCloud T2 theme song (auto-plays if browser allows)
st.markdown("""
<iframe width="100%" height="100" scrolling="no" frameborder="no" allow="autoplay"
    src="https://w.soundcloud.com/player/?url=https%3A//soundcloud.com/rolando-jacinto-77409594/terminator-2-main-theme-joslin&color=%23000000&auto_play=true&hide_related=true&show_comments=false&show_user=false&show_reposts=false&show_teaser=false&visual=false">
</iframe>
""", unsafe_allow_html=True) 