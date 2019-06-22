# Given a node in a binary tree find the next node that would occur if you were to traverse the tree in order
# This is an actual interview question from Discovery.
# Note that the tree has no value and it contains a pointer to it parent


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None


_20 = Node(20)
_35 = Node(35)
_30 = Node(30)
_45 = Node(45)
_12 = Node(12)
_7 = Node(7)
_19 = Node(19)
_17 = Node(17)
_18 = Node(18)
_17_5 = Node(17.5)
_19_5 = Node(19.5)


_20.right = _35
_20.left = _12
_20.parent = None

_35.left = _30
_35.right = _45
_35.parent = _20

_30.parent = _35
_45.parent = _35

_12.left = _7
_12.right = _19
_12.parent = _20

_7.parent = _12

_19.parent = _12
_19.left = _17
_19.right = _19_5

_17.parent = _19
_17.right = _18

_19_5.parent = _19

_18.parent = _17
_18.left = _17_5

_17_5.parent = _18


def traverse_tree(head):
    out = []

    def helper(head, output):
        current = head
        if current is not None:
            helper(current.left, output)
            output.append(current.value)
            helper(current.right, output)
    helper(head, out)
    return out


def find_most_left(node):
    current = node

    while current is not None:
        if current.left is None:
            return current
        current = current.left


def backtrack_to_first_parent_of_left_ancestry(node):
    current_child = node
    current_parent = node.parent

    while current_parent is not None:
        if current_parent.left == current_child:
            return current_parent
        else:
            current_child = current_parent
            current_parent = current_parent.parent
    return None


def find_next_node_in_order(node):
    if node.right is not None:
        return find_most_left(node.right)
    else:
        return backtrack_to_first_parent_of_left_ancestry(node)


def test():
    assert find_next_node_in_order(_7).value == 12
    assert find_next_node_in_order(_12).value == 17
    assert find_next_node_in_order(_17_5).value == 18
    assert find_next_node_in_order(_18).value == 19
    assert find_next_node_in_order(_19).value == 19.5
    assert find_next_node_in_order(_19_5).value == 20
    assert find_next_node_in_order(_20).value == 30
    assert find_next_node_in_order(_30).value == 35
    assert find_next_node_in_order(_35).value == 45
    assert find_next_node_in_order(_45) is None


print(find_next_node_in_order(_18).value)
test()
