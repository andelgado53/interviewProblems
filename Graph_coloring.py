class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None


a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')
d = GraphNode('d')
e = GraphNode('e')
f = GraphNode('f')

a.neighbors.add(b)
a.neighbors.add(c)
a.neighbors.add(d)
b.neighbors.add(a)
b.neighbors.add(e)
c.neighbors.add(a)
c.neighbors.add(e)
c.neighbors.add(f)
d.neighbors.add(a)
d.neighbors.add(e)
e.neighbors.add(d)
e.neighbors.add(b)
e.neighbors.add(c)
e.neighbors.add(f)
f.neighbors.add(e)
f.neighbors.add(c)


graph = [a, b, c, d, e, f]

def oposite_color(color):
    if color == "Male":
        return "Female"
    else:
        return "Male"

def bsf(node):
    parents  = {}
    colors = []
    node.color = "Male"
    colors.append((node.label, node.color))
    found = set()
    processed = set()
    queue = []
    queue.insert(0, node)
    found.add(node)
    parents[node.label] = -1
    while len(queue) > 0:
        n = queue.pop()
        if n not in processed:
            for child in n.neighbors:
                if child not in found:
                    parents[child.label] = n.label
                    child.color = oposite_color(n.color)
                    colors.append((child.label, child.color))
                    queue.insert(0, child)
                    found.add(child)
        processed.add(n)
   
    print(parents)
    print(colors)

def bsf_check_colors(node):
    found = set()
    processed = set()
    queue = []
    queue.insert(0, node)
    found.add(node)
    while len(queue) > 0:
        n = queue.pop()
        if n not in processed:
            for child in n.neighbors:
                if child not in found:
                    if child.color == n.color:
                        return False
                    queue.insert(0, child)
                    found.add(child)
        processed.add(n)
    return True

bsf(e)
for n in graph:
    print(bsf_check_colors(n))

colors = [1,2,3,4]
def color_graph(graph, colors):
    used_colors = [n.color for n in graph.neighbors if n.color]
    for color in colors:
        if color not in used_colors:
            graph.color = color
            break

for g in graph:
    color_graph(g, colors)
    print(g.label +  '  ' + str(g.color))