#!/bin/bash

# Create .streamlit directory if it doesn't exist
mkdir -p .streamlit

# Start the Streamlit app
streamlit run streamlit_agent/app.py --server.port $PORT --server.address 0.0.0.0 --server.headless true --server.enableCORS false --server.enableXsrfProtection false 