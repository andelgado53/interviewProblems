# Single Value Tree
# Problem Statement:
# Given a binary tree, find the number of unival subtrees 
# (the unival tree is a tree which has the same value for every node in it). 

class Node:
    def __init__(self, val):
        self.val = val
        self.left_ptr = None
        self.right_ptr = None

def num_of_single_value_trees(root):
    def helper(root):
        if root is None:
            return (0, True)
        if root.left_ptr is None and root.right_ptr is None:
            return (1, True)
        left_unival_tree_count, is_left_unival = helper(root.left_ptr)
        right_unival_tree_count, is_right_unival = helper(root.right_ptr)
        if (root.left_ptr is None or root.left_ptr.val == root.val) and (root.right_ptr is None or root.right_ptr.val == root.val):
            if is_left_unival and is_right_unival:
                return (1 + left_unival_tree_count + right_unival_tree_count, True)
        return (0 + left_unival_tree_count + right_unival_tree_count, False)
       
    return helper(root)[0]

one = Node(1)
one_ = Node(1)
one__ = Node(1)
tw0 = Node(2)
one.left = one_
one.right = one__
one__.right = tw0
# c, v = num_of_unique_trees(one)
# print(c)

five0 = Node(5)
five1 = Node(5)
five2 = Node(5)
five3 = Node(5)
five4 = Node(5)
five5 = Node(5)
# five6 = Node(5)

five0.left_ptr = five1
five0.right_ptr = five2
five1.left_ptr = five3
five1.right_ptr = five4
# five2.left_ptr = five5
five2.right_ptr = five5

print(num_of_unique_trees(five0))

# 7
# 5 5 5 5 5 4 5
# 0
# 6
# 0 1 L
# 0 2 R
# 1 3 L
# 1 4 R
# 2 5 L
# 2 6 R