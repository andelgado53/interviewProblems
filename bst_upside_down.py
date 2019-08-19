# Upside Down
# Problem Statement:
# Given a binary tree where every node has either 0 or 2 children 
# and every right node is a leaf node, flip it upside down turning 
# it into a binary tree where all left nodes are leafs.

class TreeNode():
   def __init__(self, val=None):
       self.val = val
       self.left_ptr = None
       self.right_ptr = None

# complete the function below
one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)
six = TreeNode(6)
seven = TreeNode(7)

one.left_ptr = two
one.right_ptr = three
two.left_ptr = four
two.right_ptr = five
four.left_ptr = six
four.right_ptr = seven

def travers(root):
    if root is not None:
        print(root.val)
        travers(root.left_ptr)
        
        travers(root.right_ptr)

#  travers(one)

def flipUpsideDown(root):
    new_head = []
    def helper(root):
        if root.left_ptr is None:
            new_head.append(root)
            return root
        elif root.left_ptr is not None:
            new_root = helper(root.left_ptr)
            new_root.right_ptr = root
            new_root.left_ptr = root.right_ptr
            root.right_ptr = None
            root.left_ptr = None
            return new_root.right_ptr
    helper(root)
    return new_head[0]

r = flipUpsideDown(one) 
travers(r)