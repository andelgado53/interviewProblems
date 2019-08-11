# Kth Smallest Element Of BST
# Problem Statement:
# Given a BST (binary search tree), of size N, containing integer elements, and an integer k, 
# you have to find kth smallest element of given BST.

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

def find_k_smallest(root, k):
    out = []
    def helper(root):
        if root is not None:
            helper(root.left)
            out.append(root.val)
            helper(root.right)
    helper(root)
    print(out[k-1])
find_k_smallest(ten, 3)

def find_k_smallest_v2(node, k):
    stack = []
    current = node
    cnt = 0
    while True:
        if current is None:
            if len(stack) > 0:
                c = stack.pop()
                cnt +=1
                if cnt == k:
                    print(c.val)
                    break
                print(c.val)
                current = c.right
            else:
                break
        else:
            stack.append(current)
            current = current.left
find_k_smallest_v2(ten, 3)
