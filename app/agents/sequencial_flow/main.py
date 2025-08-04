from app.agents.sequencial_flow.graph.build_graph import build_email_graph

# Build the graph using the provided function
graph = build_email_graph()

from app.agents.saveGraph import GraphSaver
GraphSaver(graph, "app/agents/sequencial_flow/graph.png").save_png()

# Initial state
raw_email = input("Enter the raw email: ")
tone = input("Enter the desired tone (e.g., formal, informal): ")

initial_state = {
    "raw_email": raw_email,
    "tone": tone
}

# Run the graph
final_output = graph.invoke(initial_state)

print("\n=== Final Reviewed Email ===\n")
print(final_output["reviewed_email"])
