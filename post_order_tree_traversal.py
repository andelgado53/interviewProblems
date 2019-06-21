# https://leetcode.com/problems/binary-tree-postorder-traversal/
# Given a binary tree, return the postorder traversal of its nodes' values.
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
# Output: [3,2,1]
# Follow up: Recursive solution is trivial, could you do it iteratively?


def traverse_in_post_order_iter_recur(node):
    output = []

    def helper(node, output):
        if node is not None:
            helper(node.left, output)
            helper(node.right, output)
            output.append(node.value)
    helper(node, output)
    return output


def traverse_in_post_order_iter(node):
    stack = []
    current = node
    seen = set()
    output = []
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif len(stack) > 0:
            if stack[-1].right is None:
                c = stack.pop()
                seen.add(c)
                output.append(c.value)
            while len(stack) > 0 and stack[-1].right in seen:
                c = stack.pop()
                seen.add(c)
                output.append(c.value)
            if len(stack) == 0:
                break
            else:
                current = stack[-1].right
        else:
            break
    return output


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


def test():
    assert traverse_in_post_order_iter(twelve) == traverse_in_post_order_iter_recur(twelve)


test()

