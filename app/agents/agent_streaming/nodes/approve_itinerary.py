from app.agents.agent_streaming.etc.trip_state import TripState


def approve_itinerary(state: TripState):
    print("\n📝 Proposed itinerary:")
    for line in state["itinerary"]:
        print(line)

    answer = input("Do you approve this itinerary? (yes/no): ").strip().lower()
    return {"approved": answer == "yes"}