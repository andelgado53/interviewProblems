# https://leetcode.com/problems/4sum/
# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums
# such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
#
# Note:
#
# The solution set must not contain duplicate quadruplets.
#
# Example:
#
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]


def four_sum(nums, target):
    index1 = 0
    index2 = index1 + 1
    nums.sort()
    solutions = []
    seen = set()
    while index1 < len(nums) - 3:
        while index2 < len(nums) - 2:
            index3 = index2 + 1
            index4 = len(nums) - 1
            while index3 < index4:
                sum_value = nums[index1] + nums[index2] + nums[index3] + nums[index4]
                if sum_value == target:
                    solution = sorted([nums[index1], nums[index2], nums[index3], nums[index4]])
                    if tuple(solution) not in seen:
                        solutions.append(solution)
                        seen.add(tuple(solution))
                if sum_value < target:
                    index3 += 1
                    if nums[index3] == nums[index3 - 1]:
                        index3 += 1
                elif sum_value >= target:
                    index4 -= 1
                    if nums[index4] == nums[index4 + 1]:
                        index4 -= 1
            index2 += 1
            if nums[index2] == nums[index2 - 1]:
                index2 += 1
        index1 += 1
        index2 = index1 + 1
        if nums[index1] == nums[index1 - 1]:
            index1 += 1
            index2 = index1 + 1
    return solutions


def test():
    input1 = [1, 0, -1, 0, -2, 2]
    target1 = 0
    assert four_sum(input1, target1) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

    input2 = [-3, -2, -1, 0, 0, 1, 2, 3]
    target2 = 0
    assert four_sum(input2, target2) == [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-2, -1, 0, 3],
                                         [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

    input3 = [5, 5, 3, 5, 1, -5, 1, -2]
    target3 = 4
    assert four_sum(input3, target3) == [[-5, 1, 3, 5]]

    input4 = [-1, 2, 2, -5, 0, -1, 4]
    target4 = 3
    assert four_sum(input4, target4) == [[-5, 2, 2, 4], [-1, 0, 2, 2]]


test()
