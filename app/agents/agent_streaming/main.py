from app.agents.agent_streaming.graph.build_graph import build_graph

# Build the graph using the provided function
workflow = build_graph()

from app.agents.saveGraph import GraphSaver
GraphSaver(workflow, "app/agents/agent_streaming/graph.png").save_png()

# Initial state
destination = input("Enter the destination: ")
from_date = input("Enter the from date: ")
to_date = input("Enter the to date: ")

initial_state = {
    "destination": destination,
    "dates": f"{from_date} to {to_date}",
    "weather": "",
    "events": [],
    "activities": [],
    "itinerary": [],
        "budget": [],
        "approved": False
    }

print("📡 Streaming travel planner updates:\n")
result = None
for event in workflow.stream(initial_state):
    print(event)
    result = event  # The last event is the final result

print("\n✅ Final workflow result:")
print(result)
