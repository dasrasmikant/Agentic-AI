import operator
from typing import Annotated, Literal, TypedDict
from langgraph.graph import StateGraph,START, END

from app.agents.iteration_flow.nodes.generate_tweet import generate_tweet
from app.agents.iteration_flow.nodes.evaluate_tweet import evaluate_tweet
from app.agents.iteration_flow.nodes.optimize_tweet import optimize_tweet
from app.agents.iteration_flow.etc.tweet_state import TweetState

def route_evaluation(state: TweetState):

    if state['evaluation'] == 'approved' or state['iteration'] >= state['max_iteration']:
        return 'approved'
    else:
        return 'needs_improvement'
        
def build_graph():
    graph = StateGraph(TweetState)

    graph.add_node('generate', generate_tweet)
    graph.add_node('evaluate', evaluate_tweet)
    graph.add_node('optimize', optimize_tweet)

    graph.add_edge(START, 'generate')
    graph.add_edge('generate', 'evaluate')

    graph.add_conditional_edges('evaluate', route_evaluation, {'approved': END, 'needs_improvement': 'optimize'})
    graph.add_edge('optimize', 'evaluate')

    workflow = graph.compile()
    return workflow

def invoke_graph(topic,lang):
    workflow = build_graph()

    initial_state = {
        "topic": topic,
        "lang":lang,
        "iteration": 1,
        "max_iteration": 5
    }

    # Run the graph
    final_output = workflow.invoke(initial_state)
    return final_output