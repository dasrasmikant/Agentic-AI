from app.agents.parallel_flow.graph.build_graph import build_idea_graph

# Build the graph using the provided function
graph = build_idea_graph()

from app.agents.saveGraph import GraphSaver
GraphSaver(graph, "app/agents/parallel_flow/graph.png").save_png()

# Initial state
topic = input("Enter the Topic: ")

initial_state = {
    "topic": topic
}

# Run the graph
final_output = graph.invoke(initial_state)

print("\n=== Final Content ===\n")
print(final_output["summary"])
