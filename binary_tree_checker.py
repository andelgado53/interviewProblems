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

def is_binary_tree(node, min_value, max_value):
    if node == None:
        return True
    if node.value > max_value or node.value < min_value:
        return False
    return is_binary_tree(node.left, min_value, node.value) and is_binary_tree(node.right, node.value, max_value)
    



print(is_binary_tree(one, -100, 100))

def is_binary_search_tree(node):
    stack = [node]
    out = set()
    n = node
    while n.left != None:
        stack.append(n.left)
        n = n.left.left
    while len(stack) > 0:
        n = stack.pop()
        out.add(n.left.value)
        out.add(n.value)
        out.add(n.right.value)
    n = node
    while n.right != None:
        stack.append(n.right)
        n = n.right.right
    while len(stack) > 0:
        n = stack.pop()
        out.add(n.left.value)
        out.add(n.value)
        out.add(n.right.value)
    return out
    

print(is_binary_search_tree(one))
