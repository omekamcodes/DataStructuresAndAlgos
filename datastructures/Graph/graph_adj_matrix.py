class Graph:
    def __init__(self, num_nodes):
        # Initialize the adjacency matrix with all zeros.
        self.adj_matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
        self.num_nodes = num_nodes

    def add_edge(self, i, j):
        # Set the value at index [i, j] to 1 to indicate that there is an edge from node i to node j.
        self.adj_matrix[i][j] = 1

    def remove_edge(self, i, j):
        # Set the value at index [i, j] to 0 to indicate that there is no longer an edge from node i to node j.
        self.adj_matrix[i][j] = 0

    def has_edge(self, i, j):
        # Return the value at index [i, j] to check if there is an edge from node i to node j.
        return self.adj_matrix[i][j] == 1


"""
This implementation uses a two-dimensional array to represent the adjacency matrix, 
and provides methods for adding and removing edges, as well as checking if an edge exists between two nodes. Note that this implementation only supports directed edges, so adding an edge from node i to node j 
does not automatically add an edge from node j to node i. 
To support undirected edges, you can add an additional line of code in 
the add_edge method to set the value at index [j, i] in the adjacency matrix to 1.
"""
