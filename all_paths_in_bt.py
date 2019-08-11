# Print All Paths of a Tree
# Problem Statement:
# Given a binary tree, print out all of its root-to-leaf paths one per line.


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

def printAllPaths(root):
    def helper(root):
        if root is None:
            return []
        elif root.left is None and root.right is None:
            return [[str(root.val)]]
        else:
            left_path = helper(root.left)            
            for path in left_path:
                path.insert(0, str(root.val))
            right_path = helper(root.right)
            for p in right_path:
                p.insert(0, str(root.val))
            return left_path + right_path
    results = helper(root)
    print(results)
    for path in results:
        print(" ".join(path))

print(printAllPaths(ten))