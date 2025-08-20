from langgraph.graph import StateGraph, START, END
from langchain_core.runnables import RunnableLambda
from app.agents.agent_streaming.etc.trip_state import TripState
from app.agents.agent_streaming.nodes.approve_itinerary import approve_itinerary
from app.agents.agent_streaming.nodes.beach_agent import beach_agent
from app.agents.agent_streaming.nodes.budget_estimator import budget_estimator
from app.agents.agent_streaming.nodes.gather_trip_info import gather_trip_info
from app.agents.agent_streaming.nodes.indoor_agent import indoor_agent
from app.agents.agent_streaming.nodes.itinerary_planner import itinerary_planner
from app.agents.agent_streaming.nodes.local_events import local_events
from app.agents.agent_streaming.nodes.weather_agent import weather_agent

def choose_activity_branch(state: TripState):
    if "sunny" in state["weather"].lower():
        return "beach_agent"
    else:
        return "indoor_agent"

def itinerary_feedback_branch(state: TripState):
    if state.get("approved", False):
        return "budget_estimator"
    else:
        return "itinerary_planner"  # Rerun itinerary until approved
              
def build_graph():
    # --- Build Graph ---
    builder = StateGraph(TripState)

    builder.add_node("gather_trip_info", RunnableLambda(gather_trip_info))
    builder.add_node("weather_agent", RunnableLambda(weather_agent))
    builder.add_node("local_events", RunnableLambda(local_events))
    builder.add_node("beach_agent", RunnableLambda(beach_agent))
    builder.add_node("indoor_agent", RunnableLambda(indoor_agent))
    builder.add_node("itinerary_planner", RunnableLambda(itinerary_planner))
    builder.add_node("approve_itinerary", RunnableLambda(approve_itinerary))
    builder.add_node("budget_estimator", RunnableLambda(budget_estimator))

    # Edges
    builder.add_edge(START, "gather_trip_info")
    builder.add_edge("gather_trip_info", "weather_agent")
    # Choose activity branch based on weather
    builder.add_conditional_edges(
        "weather_agent",
        choose_activity_branch,
        {"beach_agent": "beach_agent", "indoor_agent": "indoor_agent"},
    )
    # After activities are proposed, fetch local events, then plan itinerary
    builder.add_edge("beach_agent", "local_events")
    builder.add_edge("indoor_agent", "local_events")
    builder.add_edge("local_events", "itinerary_planner")
    builder.add_edge("itinerary_planner", "approve_itinerary")
    builder.add_conditional_edges(
        "approve_itinerary",
        itinerary_feedback_branch,
        {"budget_estimator": "budget_estimator", "itinerary_planner": "itinerary_planner"},
    )
    builder.add_edge("budget_estimator", END)
    workflow = builder.compile()
    return workflow

def run_workflow():
    # --- Run Streaming ---
    workflow=build_graph()
    initial_state = {
        "destination": "Bali",
        "dates": "2025-09-10 to 2025-09-13",
        "weather": "",
        "events": [],
        "activities": [],
        "itinerary": [],
        "budget": [],
        "approved": False
    }

    print("📡 Streaming travel planner updates:\n")
    for event in workflow.stream(initial_state):
        print(event)