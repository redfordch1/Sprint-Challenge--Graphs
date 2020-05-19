from util import Queue, Stack

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set() # set of edges
        # print("vertex added!")

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices:
            self.vertices[v1] = v2
        else:
            raise IndexError("Vertex does not exist in graph")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        directions = self.vertices[vertex_id]
        # for direction in directions:
        #     if directions[direction] != '?':

        # return self.vertices[vertex_id]

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()
        while stack.size() > 0:
            current_vertex = stack.pop()
            # print(current_vertex)
            if current_vertex not in visited:
                visited.add(current_vertex)
                print(current_vertex)
                for next_vertex in self.get_neighbors(current_vertex):
                    stack.push(next_vertex)
        # for vertex in visited:
        #     print(vertex)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()
        path = []
        while stack.size() > 0:
            current_vertex = stack.pop()
            if current_vertex == destination_vertex:
                path.append(current_vertex)
                return path
            if current_vertex not in visited:
                visited.add(current_vertex)
                path.append(current_vertex)
                for next_vertex in self.get_neighbors(current_vertex):
                    stack.push(next_vertex)