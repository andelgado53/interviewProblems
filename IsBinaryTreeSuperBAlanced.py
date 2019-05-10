
class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

one = BinaryTreeNode(1)
one.insert_left(2)
one.insert_right(3)
one.left.insert_left(4)
one.left.insert_right(5)
one.right.insert_left(6)
one.right.insert_right(7)
# one.right.right.insert_right(8)
# one.right.right.right.insert_right(9)

def count_steps_from_root_to_leaf(leafs, parents):
    depths = []
    for leaf in leafs:
        d = 0
        p = parents[leaf]
        while p != -1:
            d +=1
            p = parents[p]
        depths.append(d)
    print(depths)



def is_binary_tree_super_balanced(tree):
    q = []
    parents = {}
    leafs  = []
    if tree == None:
        return True
    q.append(tree)
    parents[1] = -1
    while len(q) > 0:
        t = q.pop()
        if t.left:
            parents[t.left.value] = t.value
            q.append(t.left)
        if t.right:
            parents[t.right.value] = t.value
            q.append(t.right)
        if t.left is None and t.right is None:
            leafs.append(t.value)
    print(leafs)
    print(parents)
    count_steps_from_root_to_leaf(leafs, parents)

def is_balanced(root):
    if root == None:
        return True
    nodes = []
    nodes.append((root, 0))
    depths = []
    while len(nodes) > 0:
        node, depth = nodes.pop()
        if not node.left and not node.right:
            if depth not in depths and len(depths) > 1:
                return False
            elif len(depths) == 1 and abs(depth[0] - depth) > 1:
                return False
            else:
                depths.append(depth)
            depths.append(depth)
        if node.left:
            nodes.append((node.left, depth + 1))
        if node.right:
            nodes.append((node.right, depth + 1))
    print(depths)

print(is_balanced(one))
is_binary_tree_super_balanced(one)