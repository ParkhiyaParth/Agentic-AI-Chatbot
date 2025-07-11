from configparser import ConfigParser

class Config:
    def __init__(self,config_file_path="srs/langgraphagenticai/ui/uiconfig.ini"):
        self.config_file_path=config_file_path
        self.config= ConfigParser()
        self.config.read(self.config_file_path)
    
    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")
    
    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")
    
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")
    
    def get_page_description(self):
        return self.config["DEFAULT"].get("PAGE_DESCRIPTION")
    
        