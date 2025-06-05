# kodey_widget.py
import streamlit.components.v1 as components

def render_kodey_widget(user_id="streamlit_user_1"):
    components.html(f"""
    <div id="kodey-chat-container"></div>
    <script src="https://cdn.kodey.ai/chat-widget.bundle.js"></script>
    <script>
        function initChatWithUser(userId) {{
          ChatWidgetLibrary.initChatWidget('kodey-chat-container', {{
            connectionUrl: "wss://pooled.ws.kodey.ai",
            apiKey: "6WJmYkbWnv4I3AC432mM55r7hltLRlfU9WvxZjvM",
            serverUrl: 'https://pooled.api.kodey.ai',
            userId: userId
          }});
        }}
        initChatWithUser("{user_id}");
    </script>
    """, height=600)
