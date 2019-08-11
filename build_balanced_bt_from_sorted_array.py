# Balanced BST From A Sorted Array
# Problem Statement:
# Given a sorted array a of size N containing distinct integers, y
# ou have to build a balanced binary search tree of a.  
# A binary search tree is balanced if, for each node, a condition holds 
# that the number of nodes in the left subtree and the number of nodes 
# in the right subtree differ by at most 1.

# Sample Test Case:
# Sample Input:
# a = [8 10 12 15 16 20 25]
# Sample Output:
# Root of the Balanced BST where:
# 15 is the root node.
# 10 is 15's left child.
# 20 is 15's right child.
# 8 is 10's left child.
# 12 is 10's right child.
# 16 is 20's left child.
# 25 is 20's right child.

class TreeNode:
    def __init__(self, node_value):
        self.val = node_value
        self.left_ptr = None
        self.right_ptr = None

ten = TreeNode(10)
fifteen = TreeNode(15)
eight = TreeNode(8)
thirdteen  = TreeNode(13)
five = TreeNode(5)
nine = TreeNode(9)
twenty = TreeNode(20)
ten.left_ptr = eight
ten.right_ptr = fifteen
fifteen.left_ptr = thirdteen
fifteen.right_ptr = twenty
eight.left_ptr = five
eight.right_ptr = nine


def trav(node):
    if node is not None:
        trav(node.left_ptr)
        print(node.val)
        trav(node.right_ptr)


data = [5, 8, 9, 10, 13, 15, 20]
def build_balanced_bst(a):
    def helper(a, start, end):
        if end < start:
            return
        mid = (start + end) // 2
        n = TreeNode(a[mid])
        n.left_ptr = helper(a, start, mid-1)
        n.right_ptr = helper(a, mid+1, end)
        return n
    n = helper(a, 0, len(a)-1)
    return n
h = build_balanced_bst(data)
trav(h)


