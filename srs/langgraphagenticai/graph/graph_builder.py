from langgraph.graph import StateGraph
from srs.langgraphagenticai.states.state import State
from srs.langgraphagenticai.llms.groqlllm import GroqLLM
from langgraph.graph import START, END
from srs.langgraphagenticai.nodes.basic_chatbot_node import BasicChatBot
from srs.langgraphagenticai.tools.search import get_tools,create_tool_node
from langgraph.prebuilt.tool_node import tools_condition
from srs.langgraphagenticai.nodes.chatbot_with_tool_node import ChatBotWithTool

class GraphBuilder():
    def __init__(self, use_controls_input):
        # Create GroqLLM instance first
        groq_llm = GroqLLM(use_controls_input)
        # Then get the LLM model
        self.llm = groq_llm.get_llm_model()
        self.graphbuilder = StateGraph(State)
        self.use_controls_input = use_controls_input
        
    def basic_chatbot_build_graph(self):
        """
        builds a basic chatbot graph with a single node that responds to user input.
        This graph can be used to create a simple chatbot that responds to user input.
        """
        self.basic_chatbot_node = BasicChatBot(self.llm)
        
        self.graphbuilder.add_node("chatbot", self.basic_chatbot_node.procecss)
        
        self.graphbuilder.add_edge(START, "chatbot")
        self.graphbuilder.add_edge("chatbot", END)
    
    def chat_with_tool(self):
        """
        builds a chatbot with tool use case graph.and also implements the tool node
        """
        
        tools=get_tools()
        tool_node=create_tool_node(tools)
        
        llm= GroqLLM(self.use_controls_input).get_llm_model()
        
        ChatBotWithToolNode = ChatBotWithTool(llm)
        chatbot_node=ChatBotWithToolNode.create_chatbot(tools=tools)
        
        
        self.graphbuilder.add_node("chatbot",chatbot_node)
        self.graphbuilder.add_node("tools", tool_node)
        
        self.graphbuilder.add_edge(START, "chatbot")
        self.graphbuilder.add_conditional_edges("chatbot",tools_condition)
        self.graphbuilder.add_edge("tools", "chatbot")
        
    
    def setup_graph(self, use_case):
        if use_case == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        if use_case == "Chatbot with Tool":
            self.chat_with_tool()    
        return self.graphbuilder.compile()