from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt.tool_node import ToolNode

def get_tools():
    """
    return a list of tools that can be used in the chatbot. 
    """
    
    tools=[TavilySearchResults(max_results=1)]
    return tools

def create_tool_node(tools):
    """
    Create a ToolNode with the provided tools.
    """
    return ToolNode(
        tools=tools,
        
    )