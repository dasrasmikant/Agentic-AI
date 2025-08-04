from app.crews.lang_graph_chatbot.graph.chat_state import ChatState
from app.crews.lang_graph_chatbot.nodes.chat_node import chat_node
from langgraph.graph import StateGraph, END


# Build the graph
builder = StateGraph(ChatState)

# Add the single node
builder.add_node("chat", chat_node)

# Define flow: START ➝ chat ➝ END
builder.set_entry_point("chat")
builder.add_edge("chat", END)

# Compile the graph
graph = builder.compile()
