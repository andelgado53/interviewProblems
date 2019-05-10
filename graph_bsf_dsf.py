import pprint
network = {
    'Min'     : sorted(['William', 'Jayden', 'Omar']),
    'William' : sorted(['Min', 'Noam']),
    'Jayden'  : sorted(['Min', 'Amelia', 'Ren', 'Noam']),
    'Ren'     : sorted(['Jayden', 'Omar']),
    'Amelia'  : sorted(['Jayden', 'Adam', 'Miguel']),
    'Adam'    : sorted(['Amelia', 'Miguel']),
    'Miguel'  : sorted(['Amelia', 'Adam']),
    'Noam'    : sorted(['Jayden', 'William']),
    'Omar'    : sorted(['Ren', 'Min'])
}

class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set()

graph = []
nodes = {}
for a in network.keys():
    if network[a] not in nodes.keys():
        n = GraphNode(a)
        nodes[a] = n

for a in network.keys():
    adj = set()
    for n in network[a]:
        adj.add(nodes[n])
    nodes[a].neighbors = adj
    graph.append(nodes[n])

def bsf(node):
    found = set()
    queue = []
    parents = {}
    parents[node.label] = -1
    queue.insert(0, node)
    found.add(node)

    while len(queue) > 0:
        n = queue.pop()
        for neighbor in n.neighbors:
            if neighbor not in found:
                parents[neighbor.label] = n.label
                found.add(neighbor)
                queue.insert(0, neighbor)
    pprint.pprint(parents)

def dsf(node):
    found = set([node])
    parents = {}
    parents[node.label] = -1
    stack = [node]

    while len(stack) > 0:
        n = stack.pop()
        for neighbor in n.neighbors:
            if neighbor not in found:
                parents[neighbor.label] = n.label
                found.add(neighbor)
                stack.insert(0, neighbor)
    pprint.pprint(parents)


pprint.pprint(graph[0].label)

# 
# bsf(graph[0])
dsf(graph[0])

found = set([graph[0]])
parents = {}
parents[graph[0].label] = -1
processed = set()
def dsf_recursive(node):
    if node in processed:
        return
    for neighbor in node.neighbors:
        if neighbor not in found:
            parents[neighbor.label] = node.label
            found.add(neighbor)
            dsf_recursive(neighbor)
    processed.add(node)
dsf_recursive(graph[0])
pprint.pprint(parents)