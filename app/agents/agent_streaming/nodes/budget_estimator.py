from app.agents.agent_streaming.etc.trip_state import TripState
from app.core.llm import gemini_llm as llm


def budget_estimator(state: TripState):
    dest = state["destination"]
    stream = llm.stream(f"Estimate the budget for a trip to {dest} with these activities: {state['activities']}")
    for chunk in stream:
        if chunk.content:
            yield {"budget": [chunk.content]}
