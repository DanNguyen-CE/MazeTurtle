class Graph():
    def __init__(self):
        self.vertex_count = 0
        self.graph = {}

    def __getattribute__(self, attr):
        return super(Graph, self).__getattribute__(attr)

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []
            self.vertex_count += 1

    def add_edge(self, v, w):
        if v not in self.graph:
            self.add_vertex(v)
        if w not in self.graph:
            self.add_vertex(w)

        self.graph[v].append(w)
