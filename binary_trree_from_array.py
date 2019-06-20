# Convert a binary list to a binary tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def traverse_tree(head):
    current = head
    if current is not None:
        traverse_tree(current.left)
        print(current.value)
        traverse_tree(current.right)

def convert_list_to_binary_tree(data):
    index = 0
    data_node = [Node(v) for v in data]
    head = data_node[0]
    while index < len(data_node):
        if 1 + index + index < len(data_node):
            left_child = data_node[1 + index + index]
            data_node[index].left = left_child
        if 2 + index + index < len(data_node):
            right_child = data_node[2 + index + index]
            data_node[index].right = right_child
        index += 1
    return head

data = [12, 10, 15, 8, 11, 13, 16]
h = convert_list_to_binary_tree(data)
traverse_tree(h)


