class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


ten = Node(12)
ten.left = Node(10)
ten.right = Node(14)
ten.left.left = Node(8)
ten.left.right = Node(11)
ten.right.left = Node(13)
ten.right.right = Node(15)


def in_order_traverse_rec(node):
    if node is not None:
        in_order_traverse_rec(node.left)

        in_order_traverse_rec(node.right)
        print(node.value)


def in_order_traverse_non_rec(node):
    stack = []
    current = node
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif len(stack) > 0:
            current = stack.pop()
            print(current.value)
            current = current.right
        else:
            break


# in_order_traverse_non_rec(ten)
in_order_traverse_rec(ten)
