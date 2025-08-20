from app.agents.agent_streaming.etc.trip_state import TripState
from app.core.llm import gemini_llm as llm


def indoor_agent(state: TripState):
    dest = state["destination"]
    stream = llm.stream(f"Suggest fun indoor activities in {dest}.")
    for chunk in stream:
        if chunk.content:
            yield {"activities": [chunk.content]}