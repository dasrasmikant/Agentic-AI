
from app.agents.agent_streaming.etc.trip_state import TripState
from app.core.llm import gemini_llm as llm

def local_events(state: TripState):
    dest = state["destination"]
    stream = llm.stream(f"List 3 interesting local events happening in {dest} soon.")
    events = ""
    for chunk in stream:
        if chunk.content:
            events += chunk.content
            yield {"events": [chunk.content]}
    yield {"events": [events.strip()]}