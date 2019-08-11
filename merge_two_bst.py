# Merge Two BSTs
# Problem Statement:
# Given two BSTs (Binary Search Trees), one with N1 number of nodes and other one with N2 number of nodes.
# Your task is to merge them such that:
#    - Resultant tree is height balanced.
#    - Resultant tree is a BST.
#    - Resultant tree contains all values from given BST-1.
#    - Resultant tree contains all values from given BST-2.
#    - Size of the resultant tree is N1 + N2.
#    - For any value, no of occurrences in resultant tree = no of occurrences in BST-1 + no of occurrences in BST-2.
#  (If BST-1 contains 3 nodes with value 50 and BST-2 contains 4 nodes with value 50, 
# then resultant tree should contain exactly 7 nodes with value 50.)

# Any resultant tree, satisfying all the above conditions will be considered as valid answer.

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
fourty = Node(40)
seven = Node(7)
twentyFive = Node(25)
twenty.right =  twentyFive
twentyFive.right = fourty
ten.left = eight
ten.right = fifteen
fifteen.left = thirdteen
fifteen.right = twenty
eight.left = five
eight.right = nine
five.right = seven


dos = Node(2)
uno = Node(1)
tres = Node(3)
dos.left = uno
dos.right = tres

siete = Node(7)
seis = Node(6)
ocho = Node(8)
siete.left = seis
siete.right = ocho

def trav(node):
    out = []
    def helper(node):
        if node is not None:
            helper(node.left)
            out.append(node.val)
            helper(node.right)
    helper(node)
    return out


def mergeTwoBSTs(root1, root2):
    nodes_tree1 = trav(root1)
    nodes_tree2 = trav(root2)
    all_nodes = sorted(nodes_tree1 + nodes_tree2)
    def create_bst_from_array(arr, start, end):
        if end < start:
            return 
        mid = (start + end) // 2
        n = Node(arr[mid])
        n.left = create_bst_from_array(arr, start, mid -1)
        n.right = create_bst_from_array(arr, mid+1, end)
        return n
    
    return create_bst_from_array(all_nodes, 0, len(all_nodes) - 1)

h = mergeTwoBSTs(dos, siete)
print(trav(h))