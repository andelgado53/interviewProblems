# https://leetcode.com/problems/maximum-binary-tree/
# Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
#
# The root is the maximum number in the array.
# The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
# Construct the maximum tree by the given array and output the root node of this tree.
#
# Example 1:
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:
#
#       6
#     /   \
#    3     5
#     \    /
#      2  0
#        \
#         1


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def find_max(data):
    if len(data) == 0:
        return None
    elif len(data) == 1:
        return 0
    else:
        start = 0
        highest = data[start]
        max_index = 0
        while start < len(data):
            if data[start] > highest:
                highest = data[start]
                max_index = start
            start += 1
    return max_index


def max_binary_tree(nums):

    def helper(nums):

        if len(nums) == 0:
            return None

        max_index = find_max(nums)
        max_val = nums[max_index]
        node = TreeNode(max_val)
        node.left = helper(nums[: max_index])
        node.right = helper(nums[max_index+1:])
        return node

    max_index = find_max(nums)
    max_val = nums[max_index]
    head = TreeNode(max_val)
    head.left = helper(nums[:max_index])
    head.right = helper(nums[max_index+1:])
    return head


def in_order_traverse(node):
    current = node

    if current is not None:
        in_order_traverse(node.left)
        print(node.val)
        in_order_traverse(node.right)


data = [3, 2, 1, 6, 0, 5]
# print(find_max(data))

c = max_binary_tree(data)

in_order_traverse(c)
