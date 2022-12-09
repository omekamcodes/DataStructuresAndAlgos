class Graph:
    def __init__(self, vertices=[]):
        # Initialize the graph with the given list of vertices.
        # Use a dictionary to store the edges of the graph,
        # where the keys are the vertices and the values are the lists of vertices that are connected to the key vertex.
        self.edges = {vertex: [] for vertex in vertices}

    def add_vertex(self, vertex):
        # Add a new vertex to the graph.
        if vertex not in self.edges:
            self.edges[vertex] = []

    def add_edge(self, source, destination):
        # Add a new edge to the graph from the source vertex to the destination vertex.
        self.edges[source].append(destination)

    def remove_vertex(self, vertex):
        # Remove the given vertex from the graph.
        if vertex in self.edges:
            del self.edges[vertex]
        for vertices in self.edges.values():
            if vertex in vertices:
                vertices.remove(vertex)

    def __str__(self):
        # Generate a string representation of the graph.
        result = ""
        for source, destinations in self.edges.items():
            result += f"{source} -> {destinations}\n"
        return result

    def remove_edge(self, source, destination):
        # Remove the edge from the source vertex to the destination vertex from the graph.
        if source in self.edges and destination in self.edges[source]:
            self.edges[source].remove(destination)


# To use the Graph class, you can initialize a new instance of the class with a list of vertices:

vertices = ["A", "B", "C", "D"]
graph = Graph(vertices)
# You can then add edges to the graph using the add_edge method, passing in the source and destination vertices:
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")

# You can also add new vertices to the graph using the add_vertex method:
graph.add_vertex("E")


# Remove vertex 'E' from the graph.
graph.remove_vertex("E")

# Remove the edge from 'A' to 'C' from the graph.
graph.remove_edge("A", "C")
