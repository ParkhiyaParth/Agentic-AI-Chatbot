from srs.langgraphagenticai.states.state import State


class BasicChatBot:
    """
    BasicChatBot is a simple chatbot that can respond to user input.
    """
    
    def __init__(self, model):
        self.llm = model
    
    def procecss(self,state:State)->dict:
        """
        Processes the input and generates a response.
        """
        return {"messages":self.llm.invoke(state['messages'])}