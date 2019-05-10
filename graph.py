
class Vertex:

    def __init__(self, vertex_id):
        self.vertex_id = vertex_id
        self.adjacent_vertices = []
        self.found = False
        self.processed = False
    
    def add_adjacent_vertex(self, vertex):
        self.adjacent_vertices.append(vertex)
    

class Graph:
    
    def __init__(self):
        self.vertices = {}
        self.parents = {}
    
    def add_pair_of_vertices(self, vertex1, vertex2):
        if vertex1.vertex_id not in self.vertices.keys():
            self.vertices[vertex1.vertex_id] = vertex1
        self.vertices[vertex1.vertex_id].add_adjacent_vertex(vertex2)
        
        if vertex2.vertex_id not in self.vertices.keys():
            self.vertices[vertex2.vertex_id] = vertex2
        self.vertices[vertex2.vertex_id].add_adjacent_vertex(vertex1)
    
    def reset_search_flags(self):
        for key in self.vertices:
            self.vertices[key].found = False
            self.vertices[key].processed = False
    
    def bfs(self, start_vertex_id):
        parents = {}
        self.reset_search_flags()
        q = []
        start_vertex = self.vertices[start_vertex_id]
        start_vertex.found = True
        q.insert(0, start_vertex)

        while len(q) > 0:
            v = q.pop()
            if v.processed == False:
                for ver in v.adjacent_vertices:
                    if ver.found != True:
                        parents[ver.vertex_id] = v.vertex_id
                        ver.found = True
                        q.insert(0, ver)
                        print(ver.vertex_id)
            v.processed = True
        return parents
    
    def dfs(self, start_vertex_id):
        parents = {}
        self.reset_search_flags()
        stack = []
        start_vertex = self.vertices[start_vertex_id]
        start_vertex.found = True
        stack.append(start_vertex)

        while len(stack) > 0:
            v = stack.pop()
            if v.processed == False:
                for ver in v.adjacent_vertices:
                    if ver.found != True:
                        parents[ver.vertex_id] = v.vertex_id
                        ver.found = True
                        stack.insert(0, ver)
                        print(ver.vertex_id)
            v.processed = True
        return parents
    
    def dfs_recursive(self, start_vertex_id):
        start_vertex = self.vertices[start_vertex_id]
        start_vertex.found = True

        if start_vertex.processed == True:
            return
        else:
            for ver in start_vertex.adjacent_vertices:
                if ver.found != True:
                    self.parents[ver.vertex_id] = start_vertex.vertex_id
                    ver.found = True
                    print(ver.vertex_id)
                    self.dfs_recursive(ver.vertex_id)
            start_vertex.processed = True
        return self.parents







andres = Vertex('andres')
keli = Vertex("keli")
sameem = Vertex('sameem')
lisa = Vertex("lisa")
sally = Vertex('sally')
john = Vertex('john')
cara = Vertex('cara')

celina = Vertex('celina')
matilde = Vertex('matilde')

G = Graph()

G.add_pair_of_vertices(andres, keli)
G.add_pair_of_vertices(andres, sally)
G.add_pair_of_vertices(andres, john)
G.add_pair_of_vertices(keli, lisa)
G.add_pair_of_vertices(keli, sally)
G.add_pair_of_vertices(keli, john)
G.add_pair_of_vertices(sally, john)
G.add_pair_of_vertices(sameem, andres)
G.add_pair_of_vertices(keli, cara)
G.add_pair_of_vertices(celina, matilde)
G.add_pair_of_vertices(celina, andres)

# for key in G.vertices:
#     print('These are the friends of: ' + key)
#     for e in G.vertices[key].adjacent_vertices:
#         print(e.vertex_id)

# print(G.bfs('cara'))
print('+++++++++++++++++')
print(G.dfs('cara'))
print('+++++++++++++++++')
G.reset_search_flags()
print(G.dfs_recursive('cara'))
