from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from typing import Annotated

class State(TypedDict):
    """
    Represents the state of the Agentic AI application.
    
    """
    messages :Annotated[list,add_messages]