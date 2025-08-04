from typing import TypedDict, List,Optional
from langgraph.graph import StateGraph, END
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

class ChatState(TypedDict):
    messages: List  # Holds the conversation
    tool_result: Optional[str] 
