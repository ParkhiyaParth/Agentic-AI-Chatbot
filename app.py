from srs.langgraphagenticai.ui.uiconfigfile import Config
import streamlit as st

# ✅ Must be the first Streamlit call
config = Config()
page_title = config.get_page_title() or "Agentic AI"
st.set_page_config(page_title="🤖 " + page_title, layout="wide")

# ✅ Load the UI
from srs.langgraphagenticai.main import load_agentic
load_agentic.load_agentic_ai_ui()
