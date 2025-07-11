import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from srs.langgraphagenticai.ui.streamlit.loadui import LoadStreamLitUI
from srs.langgraphagenticai.llms.groqlllm import GroqLLM
from srs.langgraphagenticai.graph.graph_builder import GraphBuilder
from srs.langgraphagenticai.ui.streamlit.display_result import DisplayResultStreamlit

class load_agentic:
    def __init__(self):
        """
        Initializes the Agentic AI UI loader.
        This class is responsible for loading the UI components and handling user input.
        
        """
        pass
    
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
                
                if not model:
                    st.error("Error: LLM model could not be initialized. Please check your API key and model selection.")
                    return
                
                use_case=user_input.get("usecase")
                
                if not use_case:
                    st.error("⚠️ Please select a use case to proceed.")
                    return
                
                graph_builder=GraphBuilder(user_input)
                
                try:
                    graph=graph_builder.setup_graph(use_case)
                    DisplayResultStreamlit(use_case, graph, user_message).display_result()
                except Exception as e:
                    st.error(f"⚠️ Error setting up graph for use case '{use_case}': {e}")
                    return
                    
                    
            except Exception as e:
                st.error(f"⚠️ Error initializing Agentic AI: {e}")
                return
            
            