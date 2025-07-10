import streamlit as st
import os
from ..uiconfigfile import Config

class LoadStreamLitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}
    
    def load_streamlit_ui(self):
        st.set_page_config(page_title="🤖"+self.config.get_page_title,layout="wide")
        st.header("🤖"+self.config.get_page_title())
        
        with st.sidebar:
            llm_options= self.config.get_llm_options()
            usecase_options= self.config.get_usecase_options()
            
            self.user_controls["llm"] = st.selectbox("Select LLM", llm_options, index=0)
            
            if self.user_controls["llm"] == "Groq":
                groq_model_options = self.config.get_groq_model_options()
                self.user_controls["groq_model"] = st.selectbox("Select Groq Model", groq_model_options, index=0)
                self.user_controls["GROQ_API_KEY"]=st.session_state["GROQ_API_KEY"]= st.text_input("Enter Groq API Key", type="password")
                
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your Groq API Key to use Groq models.")
            
            self.user_controls["usecase"] = st.selectbox("Select Use Case", usecase_options, index=0)
            
        print("User Controls:", self.user_controls)
        return self.user_controls           