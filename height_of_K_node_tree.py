# Height Of K-Ary Tree
# Problem Statement:
# Given a k-ary tree T, containing N nodes. You have to find height of the tree. 
# (Length of the longest path from root to any node.)
# (We are looking for number of edges on longest path from root to any node, 
# not number of nodes on longest path from root to any node.)
# Definition from Wikipedia: A k-ary tree is a rooted tree in which each node has no more than k children. 
# A binary tree is the special case where k=2.

class TreeNode:
    def __init__(self):
        self.children = []

one  = TreeNode()
two = TreeNode()
three = TreeNode()
four = TreeNode()
five = TreeNode()
one.children = [two, three, five]
five.children = [four]

def find_height(root):
    max_h = []
    def helper(root, level):
        if root == None:
            return
        max_h.append(level)
        for c in root.children:
            helper(c, level+1)
    helper(root, 0)
    return sorted(max_h)[-1]

print(find_height(one))