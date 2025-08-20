from app.agents.agent_streaming.etc.trip_state import TripState
from app.core.llm import gemini_llm as llm

def weather_agent(state: TripState):
    dest = state["destination"]
    stream = llm.stream(f"Give a 3-day weather forecast for {dest}. Keep it short.")
    forecast = ""
    for chunk in stream:
        if chunk.content:
            forecast += chunk.content
            yield {"weather": forecast}
    yield {"weather": forecast.strip()}