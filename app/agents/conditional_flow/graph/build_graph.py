from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from app.agents.conditional_flow.etc.complaint_state import ComplaintState
from app.agents.conditional_flow.node.classify_severity import classify_severity
from app.agents.conditional_flow.node.auto_response import auto_response
from app.agents.conditional_flow.node.escalate_to_support import escalate_to_support
from app.agents.conditional_flow.node.escalate_to_manager import escalate_to_manager

def build_complaint_graph():
    # Wrap nodes
    classifier = RunnableLambda(classify_severity)
    low_node = RunnableLambda(auto_response)
    medium_node = RunnableLambda(escalate_to_support)
    high_node = RunnableLambda(escalate_to_manager)

    # Build Graph
    builder = StateGraph(ComplaintState)    
    # Add nodes
    builder.add_node("classify", classifier)
    builder.add_node("low_flow", low_node)
    builder.add_node("medium_flow", medium_node)
    builder.add_node("high_flow", high_node)

    # Set entry
    builder.set_entry_point("classify")

    # Conditional branching from classify node
    builder.add_conditional_edges(
        "classify",
        lambda state: state["severity"],
        {
            "low": "low_flow",
            "medium": "medium_flow",
            "high": "high_flow",
        }
    )

    builder.add_edge("low_flow", END)
    builder.add_edge("medium_flow", END)
    builder.add_edge("high_flow", END)


    graph = builder.compile()
    return graph
