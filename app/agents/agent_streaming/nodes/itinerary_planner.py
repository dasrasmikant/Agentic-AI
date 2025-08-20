from app.agents.agent_streaming.etc.trip_state import TripState
from app.core.llm import gemini_llm as llm


def itinerary_planner(state: TripState):
    dest = state["destination"]
    stream = llm.stream(f"Plan a 3-day itinerary for {dest} based on activities: {state['activities']}")
    for chunk in stream:
        if chunk.content:
            yield {"itinerary": [chunk.content]}