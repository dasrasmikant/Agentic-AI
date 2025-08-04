from langgraph.graph import StateGraph, END
from app.crews.my_cube_query_agent.nodes.parse_question import parse_question_node
from app.crews.my_cube_query_agent.nodes.generate_query import generate_query_node
from app.crews.my_cube_query_agent.nodes.run_cube_query import run_cube_query_node
from app.crews.my_cube_query_agent.nodes.summarize_answer import summarize_answer_node
from pydantic import BaseModel
from typing import Optional

class StateSchema(BaseModel):
    question: Optional[str] = None
    cube_query: Optional[str] = None
    query_result: Optional[str] = None
    summary: Optional[str] = None

def build_graph():
 
    builder = StateGraph(StateSchema)

    builder.add_node("parse_question", parse_question_node)
    builder.add_node("generate_query", generate_query_node)
    builder.add_node("run_query", run_cube_query_node)
    builder.add_node("summarize_result", summarize_answer_node)

    builder.set_entry_point("parse_question")
    builder.add_edge("parse_question", "generate_query")
    builder.add_edge("generate_query", "run_query")
    builder.add_edge("run_query", "summarize_result")
    builder.add_edge("run_query", END)

    return builder.compile()
