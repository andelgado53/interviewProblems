# https://leetcode.com/problems/binary-tree-preorder-traversal
# Given a binary tree, return the preorder traversal of its nodes' values.
#
# Example:
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,2,3]
# Follow up: Recursive solution is trivial, could you do it iteratively?


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


twelve = Node(12)
twelve.left = Node(10)
twelve.right = Node(14)
twelve.left.left = Node(8)
twelve.left.right = Node(11)
twelve.left.right.right = Node(9)
twelve.right.left = Node(13)
twelve.right.left.left = Node(7)
twelve.right.right = Node(15)
twelve.right.right.left = Node(16)
twelve.right.right.right = Node(17)
twelve.right.right.right.right = Node(25)
twelve.right.right.right.right.right = Node(30)
twelve.right.right.right.right.right.right = Node(35)
twelve.right.right.right.right.right.right.right = Node(45)
twelve.right.right.right.right.right.right.right.right = Node(55)


def pre_order_rec(node):
    output = []

    def helper(node, output):
        if node is not None:
            output.append(node.value)
            helper(node.left, output)
            helper(node.right, output)
    helper(node, output)
    return output


def pre_order_iter(head):
    stack = []
    current = head
    output = []

    while True:
        if current is not None:
            output.append(current.value)
            stack.append(current)
            current = current.left
        elif len(stack) > 0:
            current = stack.pop().right
        else:
            break
    return output


assert pre_order_iter(twelve) == pre_order_rec(twelve)




