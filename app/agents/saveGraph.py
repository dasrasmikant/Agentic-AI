class GraphSaver:
    def __init__(self, graph, output_path):
        self.graph = graph
        self.output_path = output_path

    def save_png(self):
        png_data = self.graph.get_graph().draw_mermaid_png()
        with open(self.output_path, "wb") as f:
            f.write(png_data)
