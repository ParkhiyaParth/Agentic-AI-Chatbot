import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from langgraphagenticai.ui.streamlit.loadui import LoadStreamLitUI
from langgraphagenticai.llms.groqlllm import GroqLLM

def load_agentic_ai_ui():
    """
    Loads and runs the Agentic AI UI using Streamlit.
    This function initializes the UI components and sets up the sidebar for user input.
    
    """
    
    ui=LoadStreamLitUI()
    user_input= ui.load_streamlit_ui()
    
    if not user_input:
        st.error("⚠️ Please select an LLM and Use Case to proceed.")
        
    user_message= st.chat_input("Enter your message:")
    
    
    if user_message:
        try:
            obj_config_model = GroqLLM(user_input)
            model= obj_config_model.get_llm_model()            
            
            
        except Exception as e:
            
        
    