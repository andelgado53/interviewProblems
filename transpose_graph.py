import pprint 
class Node:
    def __init__(self, val):
        self.val = val
        self.neighbours = []
    
    def __str__(self):
        return str(self.val) + " " + str(self.neighbours)


# Sample Input:
# Any node of the graph where:

# For n = 3
# nodes = [1 2 3]
# edges = [(1 -> 2), (2 -> 3), (3 -> 1)]

three = Node(3)
one = Node(1)
two = Node(2)
three.neighbours = [one]
one.neighbours = [two]
two.neighbours = [three]


def recreate_graph(node):
    q = [] 
    seen = set()
    q.append(node)
    seen.add(node)
    g = {}
    while len(q) > 0:
        current = q.pop(0)
        g[current.val] = []
        for n in current.neighbours:
            temp = g.get(current.val)
            temp.append(n.val)
            if n not in seen:
                seen.add(n)
                q.append(n)
    return g


def build_other_graph(node):
    seen = set()
    nodes_map = {}
    def dfs(node):
        if node not in nodes_map:
            nodes_map[node] = Node(node.val)
        for n in node.neighbours:
            new_node = nodes_map.get(n, Node(n.val))
            if nodes_map[node] not in new_node.neighbours:
                new_node.neighbours.append(nodes_map[node])
                nodes_map[n] = new_node
            if n not in seen:
                seen.add(n)
                dfs(n)    
    dfs(node)
    return nodes_map[node]

# 4 4
# 1 2
# 2 3
# 3 4
# 4 1
# one = Node(1)
# two = Node(2)
# three = Node(3)
# four = Node(4)
# one.neighbours = [two]
# two.neighbours = [three]
# three.neighbours = [four, one]
# four.neighbours = [one]
g = build_other_graph(three)
# print(g.val)
print("original graph " + str(recreate_graph(three)))
print('transposed graph ' + str(recreate_graph(g)))

# for k in g:
#     print(g[k])
# print(g.val)
# print(g.neighbours[0].val)
# print(g.neighbours[0].neighbours[0].val)
# print(g.neighbours[0].neighbours[0].neighbours[0].val)
# print(g.neighbours[0].neighbours[0].neighbours[0].neighbours[0].val)


# print(g.neighbours[0].neighbours)