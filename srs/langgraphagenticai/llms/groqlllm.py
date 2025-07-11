import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, use_controls_input):
        self.use_controls_input = use_controls_input

    def get_llm_model(self):
        try:
            groq_api_key = self.use_controls_input["GROQ_API_KEY"]
            groq_model = self.use_controls_input["groq_model"]

            if not groq_api_key:
                st.error("⚠️ Please enter your Groq API Key to use Groq models.")
                return None

            # Optional: validate model
            # valid_models = [
            #     "llama-3-70b",
            #     "llama-3-8b",
            #     "llama-3-70b-chat",
            #     "llama-3-8b-chat"
            # ]
            # if groq_model not in valid_models:
            #     st.error(f"❌ Invalid model selected: {groq_model}")
            #     return None

            return ChatGroq(api_key=groq_api_key, model=groq_model)

        except Exception as e:
            st.error(f"⚠️ Error initializing Groq LLM: {e}")
            return None
