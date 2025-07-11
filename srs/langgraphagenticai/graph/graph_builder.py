from langgraph.graph import StateGraph
from srs.langgraphagenticai.states.state import State
from srs.langgraphagenticai.llms.groqlllm import GroqLLM
from langgraph.graph import START, END
from srs.langgraphagenticai.nodes.basic_chatbot_node import BasicChatBot

class GraphBuilder():
    def __init__(self, use_controls_input):
        # Create GroqLLM instance first
        groq_llm = GroqLLM(use_controls_input)
        # Then get the LLM model
        self.llm = groq_llm.get_llm_model()
        self.graphbuilder = StateGraph(State)
        
    def basic_chatbot_build_graph(self):
        """
        builds a basic chatbot graph with a single node that responds to user input.
        This graph can be used to create a simple chatbot that responds to user input.
        """
        self.basic_chatbot_node = BasicChatBot(self.llm)
        
        self.graphbuilder.add_node("chatbot", self.basic_chatbot_node.procecss)
        
        self.graphbuilder.add_edge(START, "chatbot")
        self.graphbuilder.add_edge("chatbot", END)
    
    def setup_graph(self, use_case):
        if use_case == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        return self.graphbuilder.compile()