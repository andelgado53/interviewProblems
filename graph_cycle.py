import pprint 
class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()

with_cycle = []
a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')
d = GraphNode('d')
e = GraphNode('e')
f = GraphNode('f')
g = GraphNode('g')
h = GraphNode('h')
a.neighbors.add(b)
a.neighbors.add(c)
b.neighbors.add(e)
b.neighbors.add(f)
c.neighbors.add(g)
c.neighbors.add(h)
with_no_cycle_graph = [a, b, c, d, e, f, g, h]

def dfs(node):
    found = set()
    found.add(node)
    parents = {}
    parents['a'] = -1
    stack = []
    stack.append(node)
    while len(stack) > 0:
        current = stack.pop()
        for neighbor in current.neighbors:
            if neighbor not in found:
                parents[neighbor.label] = current.label
                stack.append(neighbor)
                found.add(neighbor)
            else:
                pprint.pprint(parents)
                return True
    pprint.pprint(parents)
    return False

# print(dfs(a))


with_cycle_graph = []
a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')
d = GraphNode('d')
e = GraphNode('e')
f = GraphNode('f')
g = GraphNode('g')
h = GraphNode('h')

a.neighbors.add(c)

d.neighbors.add(b)

b.neighbors.add(g)
b.neighbors.add(h)
b.neighbors.add(a)

c.neighbors.add(e)
e.neighbors.add(d)
e.neighbors.add(f)
with_cycle_graph = [a, b, c, d, e, f, g, h]
print(dfs(a))