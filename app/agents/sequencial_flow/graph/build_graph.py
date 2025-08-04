from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from app.agents.sequencial_flow.tool.email_state import EmailState
from app.agents.sequencial_flow.node.rewrite_mail import rewrite_email
from app.agents.sequencial_flow.node.review_email import review_email

def build_email_graph():
    """
    Constructs and returns the LangGraph object for the email rewriting and review flow.
    """
    rewrite_node = RunnableLambda(rewrite_email)
    review_node = RunnableLambda(review_email)

    builder = StateGraph(EmailState)
    builder.add_node("rewrite_email", rewrite_node)
    builder.add_node("review_email", review_node)

    builder.set_entry_point("rewrite_email")
    builder.add_edge("rewrite_email", "review_email")
    builder.add_edge("review_email", END)

    graph = builder.compile()
    return graph
