# Kodey AI Streamlit Chat App

A Streamlit web application featuring an embedded Kodey AI chat widget with a custom background.

## Features

- 🤖 Kodey AI chat widget integration
- 🎨 Custom background image (sec_jacob.png)
- 📱 Responsive design with wide layout
- ☁️ Ready for cloud deployment

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the app:
```bash
cd streamlit_agent
streamlit run app.py
```

3. Open your browser and navigate to `http://localhost:8501`

## Deployment on Render

This app is configured for easy deployment on Render using the included `render.yaml` configuration.

### Deploy Steps:

1. Push your code to GitHub
2. Connect your GitHub repo to Render
3. Render will automatically detect the `render.yaml` file and deploy

### Manual Deploy:

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Use these settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run streamlit_agent/app.py --server.port $PORT --server.address 0.0.0.0 --server.headless true --server.enableCORS false --server.enableXsrfProtection false`

## Files Structure

```
├── streamlit_agent/
│   ├── app.py              # Main Streamlit application
│   ├── kodey_widget.py     # Kodey AI widget component
│   └── sec_jacob.png       # Background image
├── requirements.txt        # Python dependencies
├── render.yaml            # Render deployment configuration
└── README.md              # This file
``` 