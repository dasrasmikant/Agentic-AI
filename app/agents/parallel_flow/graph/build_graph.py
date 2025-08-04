from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from app.agents.parallel_flow.etc.idea_state import IdeaState
from app.agents.parallel_flow.nodes.analytical_agent import analytical_agent
from app.agents.parallel_flow.nodes.creative_agent import creative_agent
from app.agents.parallel_flow.nodes.critical_agent import critical_agent
from app.agents.parallel_flow.nodes.summarize_agent import summarize_thoughts

def build_idea_graph():
    """
    Constructs and returns the LangGraph object for the email rewriting and review flow.
    """
    # Wrap nodes
    analytical = RunnableLambda(analytical_agent)
    creative = RunnableLambda(creative_agent)
    critical = RunnableLambda(critical_agent)
    summarizer = RunnableLambda(summarize_thoughts)

    # Create the LangGraph
    builder = StateGraph(IdeaState)

    def start_node(state): return state

    # Add nodes
    builder.add_node("analytical", analytical)
    builder.add_node("creative", creative)
    builder.add_node("critical", critical)
    builder.add_node("summarize", summarizer)

    builder.add_node("Initiation", RunnableLambda(start_node))

    builder.set_entry_point("Initiation")
    builder.add_edge("Initiation", "analytical")
    builder.add_edge("Initiation", "creative")
    builder.add_edge("Initiation", "critical")

    builder.add_edge("analytical", "summarize")
    builder.add_edge("creative", "summarize")
    builder.add_edge("critical", "summarize")

    builder.add_edge("summarize", END)

    graph = builder.compile()
    return graph
