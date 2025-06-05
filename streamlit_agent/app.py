import streamlit as st
from kodey_widget import render_kodey_widget

# Set page config
st.set_page_config(
    page_title="Kodey AI Chat",
    page_icon="🤖",
    layout="wide"
)

# Main app
st.title("🤖 Kodey AI Chat Assistant")
st.write("Welcome to your AI coding assistant! Chat with Kodey below:")

# Render the Kodey chat widget
render_kodey_widget() 