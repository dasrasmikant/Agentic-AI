from app.crews.my_cube_query_agent.graph.workflow import build_graph

graph = build_graph()
# from IPython.display import Image, display

# try:
#     display(Image(graph.get_graph().draw_mermaid_png()))
# except Exception:
#     # This requires some extra dependencies and is optional
#     pass
print(graph.get_graph().draw_ascii())
question = input("Enter your question: ")
result = graph.invoke({"question": str(question)})
print("Result:\n", result['query_result'])
# print("Final Answer:\n", result["query_result"])