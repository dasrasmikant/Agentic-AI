# llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
from app.core.llm import gemini_llm as llm
from app.crews.lang_graph_chatbot.graph.chat_state import ChatState
from langchain.schema import HumanMessage


def chat_node(state: ChatState) -> ChatState:
    # Inject tool result if available
    if state.get("tool_result"):
        state["messages"].append(HumanMessage(content=f"Tool result: {state['tool_result']}"))
    
    response = llm.invoke(state["messages"])
    state["messages"].append(response)
    return {"messages": state["messages"]}
