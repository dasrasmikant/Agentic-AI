from app.agents.iteration_flow.graph.build_graph import build_graph

# Build the graph using the provided function
workflow = build_graph()

from app.agents.saveGraph import GraphSaver
GraphSaver(workflow, "app/agents/iteration_flow/graph.png").save_png()

# Initial state
topic = input("Enter the topic: ")

initial_state = {
    "topic": topic,
    "iteration": 1,
    "max_iteration": 5
}
result = workflow.invoke(initial_state)

print(result)


