# Given a binary tree, find out if there is a path (root to leave) where the sum of all values across the path sum up to K

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

ten = Node(10)
fifteen = Node(15)
eight = Node(8)
thirdteen  = Node(13)
five = Node(5)
nine = Node(9)
twenty = Node(20)
ten.left = eight
ten.right = fifteen
fifteen.left = thirdteen
fifteen.right = twenty
eight.left = five
eight.right = nine

def sum_path(node, k, out):
    if node == None:
        return []
    elif node.left is None and node.right is None and k - node.val == 0:
        out.append(node.val)
        return out
    else:
        left_path = sum_path(node.left, k - node.val, out)
        right_path = sum_path(node.right, k - node.val, out)
        if len(left_path) > 0:
            left_path.append(node.val)
            return left_path
        elif len(right_path) > 0:
            right_path.append(node.val)
            return right_path
        else:
            return []

print(sum_path(ten, 23, []))
