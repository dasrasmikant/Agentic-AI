from app.agents.conditional_flow.graph.build_graph import build_complaint_graph

# Build the graph using the provided function
graph = build_complaint_graph()

from app.agents.saveGraph import GraphSaver
GraphSaver(graph, "app/agents/conditional_flow/graph.png").save_png()

# Initial state
complaint = input("Enter the complaint: ")

initial_state = {
    "complaint": complaint
}

# Run the graph
final_output = graph.invoke(initial_state)

print("\n=== Final Content ===\n")
print(final_output["response"])
