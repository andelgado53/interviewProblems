# print all nodes in the kth level of a binary tree

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

def print_k_level(node, k):
    if node is None:
        return 
    elif k == 0:
        print(node.val)
    else:
        print_k_level(node.left, k -1)
        print_k_level(node.right, k -1)

print_k_level(ten, 0)
