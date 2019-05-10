import pprint
network = {
    'Min'     : ['William', 'Jayden', 'Omar'],
    'William' : ['Min', 'Noam'],
    'Jayden'  : ['Min', 'Amelia', 'Ren', 'Noam'],
    'Ren'     : ['Jayden', 'Omar'],
    'Amelia'  : ['Jayden', 'Adam', 'Miguel'],
    'Adam'    : ['Amelia', 'Miguel'],
    'Miguel'  : ['Amelia', 'Adam'],
    'Noam'    : ['Jayden', 'William'],
    'Omar'    : ['Ren', 'Min']
}

class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None

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

# print(graph)
# print(graph[0].neighbors)
# # print(nodes)
# for g in graph:
#     print(g)
#     print(g.label)
#     print(g.neighbors)
#     for n in g.neighbors:
#         print(n.label)
#     print('**************')

def bsf(node):
    parents = {}
    queue = []
    found = set()
    processed = set()
    queue.insert(0, node)
    parents[node.label] = -1
    found.add(node)
    while len(queue) > 0:
        n = queue.pop()
        if n not in processed:
            for child in n.neighbors:
                if child not in found:
                    queue.insert(0, child)
                    parents[child.label] = n.label
                    found.add(child)
        processed.add(n)
    pprint.pprint(parents)
    return parents


def find_shortest_path(start_node, end_node):
    parents = bsf(nodes[start_node])
    parent  = parents[end_node]
    stack = [end_node]
    stack.append(parent)
    while parent != -1:
        parent = parents[parent]
        if parent != -1:
            stack.append(parent)
    # pprint.pprint(parents)
    while len(stack) > 0:
        print(stack.pop())

find_shortest_path('Min', 'Adam')
pprint.pprint(bsf(nodes['Min']))