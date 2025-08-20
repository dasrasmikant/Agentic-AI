from app.agents.agent_streaming.etc.trip_state import TripState


def gather_trip_info(state: TripState):
    dest = state["destination"]
    dates = state["dates"]
    for msg in [f"Planning your trip to {dest}...", f"Dates confirmed: {dates}"]:
        yield {"activities": [msg]}