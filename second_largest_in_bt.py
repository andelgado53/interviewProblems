class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = value
        return self.left

    def insert_right(self, value):
        self.right = value
        return self.right

one = BinaryTreeNode(15)
one.insert_left(BinaryTreeNode(12))
one.insert_right(BinaryTreeNode(17))
one.left.insert_left(BinaryTreeNode(11))
one.left.insert_right(BinaryTreeNode(13))
one.right.insert_left(BinaryTreeNode(16))
one.right.insert_right(BinaryTreeNode(18))
one.right.right.insert_right(BinaryTreeNode(19))

def find_largest(node):
    if node.right == None:
        return node.value
    return find_largest(node.right)

def second_largest_2(node):
    if node.right == None or node == None:
        return
    if node.right.right == None and node.right.left == None:
        return node.value
    elif node.right.right == None and node.right.left:
        return find_largest(node.right.left)
    else:
        return second_largest_2(node.right)


def second_largest(node):
    parents = {}
    queue = []
    queue.insert(0, node)
    while len(queue) > 0:
        n = queue.pop()
        if n.right != None:
            parents[n.right.value] = n.value
            queue.insert(0, n.right)
    parent = node
    right_child = parent.right
    print(parents)
    while True:
        if right_child == None:
            return parents[parent.value]
        parent = right_child
        right_child = right_child.right

items = []
def second_largest_1(node):
    if node != None:
        second_largest_1(node.left)
        items.append(node.value)
        second_largest_1(node.right)

# print(second_largest_1(one))
# print(items)
# print(items[-2])

# print(second_largest(one))

# print(second_largest_2(one))

# print(find_largest(one))

two = BinaryTreeNode(5)
two.insert_left(BinaryTreeNode(3))
two.insert_right(BinaryTreeNode(8))
two.left.insert_left(BinaryTreeNode(1))
two.left.insert_right(BinaryTreeNode(4))

two.right.insert_left(BinaryTreeNode(7))
two.right.insert_right(BinaryTreeNode(12))
two.right.right.insert_left(BinaryTreeNode(10))
two.right.right.left.insert_left(BinaryTreeNode(9))
two.right.right.left.insert_right(BinaryTreeNode(11))


# second_largest_1(one)
# print(items[-2])
print(second_largest_2(one))
print(second_largest_2(two))

