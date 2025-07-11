from srs.langgraphagenticai.states.state import State

class ChatBotWithTool:
    """
    ChatBotWithTool is a chatbot that can use tools to respond to user input.
    """
    
    def __init__(self, model):
        self.llm = model
    
    def process(self, state: State) -> dict:
        """
        Processes the input and generates a response using tools if available.
        """
        user_input=state['messages'][-1] if state['messages'] else ""
        llm_response=self.llm.invoke({"role":"user","content":user_input})
        
        tools_response=f"Tools response based on input: {user_input}"
        
        return {"messages":[llm_response, tools_response]}
    
    def create_chatbot(self,tools):
        """
        Returns a chatbot node function
        """
        
        llm_with_tools =self.llm.bind_tools(tools)
        
        def chatbot_node(state: State):
            """
            Chatbot logic for processing user input and generating a response.
            """
            
            return {"messages":[llm_with_tools.invoke(state['messages'])]}
        
        return chatbot_node