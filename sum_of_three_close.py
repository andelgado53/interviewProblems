# https://leetcode.com/problems/3sum-closest/
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three integers. Y
# ou may assume that each input would have exactly one solution.
#
# Example:
#
# Given array nums = [-1, 2, 1, -4], and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


def three_sum_close(nums, target):
    # This solution is n^3
    index1 = 0
    index2 = 1
    index3 = 2
    closest_diff = nums[index1] + nums[index2] + nums[index3]
    close_target = nums[index1] + nums[index2] + nums[index3]
    h1 = set()
    while index1 < len(nums):
        if nums[index1] in h1:
            index1 += 1
            index2 = index1 + 1
            index3 = index2 + 1
            continue
        h1.add(nums[index1])
        h2 = set()
        while index2 < len(nums):
            if nums[index2] in h2:
                index2 += 1
                index3 = index2 + 1
                continue
            h2.add(nums[index2])
            h3 = set()
            while index3 < len(nums):
                if nums[index3] in h3:
                    index3 += 1
                    continue
                h3.add(nums[index3])
                value = nums[index1] + nums[index2] + nums[index3]
                if abs(value - target) < closest_diff:
                    closest_diff = abs(target - value)
                    close_target = value
                    if close_target == target:
                        return close_target
                index3 += 1
            index2 += 1
            index3 = index2 + 1
        index1 += 1
        index2 = index1 + 1
        index3 = index2 + 1
    return close_target


input1 = [-1, 2, 1, -4]
target1 = 1
print(three_sum_close(input1, target1))
input2 = [1, 1, 1, 0]
target2 = -100
print(three_sum_close(input2, target2))
input3 = [-49, -84, 68, -30, 30, -77, -15, -39, -98, -78, -96, 13, 10, 14, -55, 48, -13, -61, 81, -77, 9, 85, -88, -86,
          -96, 49, 4, -34, 83, 67, 85, -7, 12, 10, 92, 71, 5, 57, -11, -10, -72, 65, -54, 58, 79, -6, -5, -93, 14, 44,
          56, -72, 35, -87, 4, -20, 89, -85, 15, -45, 33, 89, 31, -89, 15, -17, -12, 31, -17, 61, 47, -29, 98, -10, 22,
          38, 73, 60, -39, 82, -47, -58, -21, 73, -72, 25, -46, 88, 34, 54, -19, -78, -84, -94, -18, -9, -7, -56, 88,
          99, 61, -10, -43, -83, 62, -67, 95, -4, -14, 100, 5, 29, 7, 73, -46, 20, 60, 81, 95, -13, -32, 69, 56, -4, -2,
          68, 79, -53, -14, 81, -63, 100, -97, -59, -9, 12, 84, 0, 19, 76, 8, 63, -39, -38, -7, 45, -51, -60, 91, 4, 22,
          -74, -64, 77, 45, 38, -95, -72, 82, -52, -27, 26, -74, -92, -70, 97, 13, -96, -77, -26, 57, 6, 30, 50, -19,
          68]
target3 = 30
input4 = [-16, -2, 17, -16, 3, -7, -13, 20, -4, 12, 5, 13, -7, 0, 5, 4, -17, -16, 9, 1, 8, -6, 0, -8, 16, 10, -6, 9, -4,
          12, 16, 5, 19, 2, -9, -17, -8, -17, 7, -10, 2, 20, -18, -20, -14, -6, 6, 17, -10, -8, 18, -15, 7, -9, 13, 13,
          -13, 3, 18, 10, 12, 16, -6, -19, -6, -13, 8, -5, 16, 5, 8, -3, -9, -9, -5, 14, 14, -13, -18, 13, 15, -3, 9,
          14, 18, -14, -14, 1, 20, -4, -6, 0, 3, 15, 20, 20, 9, 13, -8, -1, -2, 6]
target4 = -58
print(sorted(input4))
print(three_sum_close(input4, target4))
input5 = [-26, 84, -85, 2, 99, 42, -28, 16, -97, -59, 64, -67, -30, 18, -15, -11, -60, -79, 41, -29, 49, -33, 21, -8,
          -73, 6, -31, 31, -23, 82, -34, 12, 86, 38, -4, 99, 4, 63, -13, -42, -4, 89, 88, -30, 0, 15, 37, -95, -85, 15,
          66, 8, 43, 95, -76, 75, -16, 48, 15, -82, 56, 83, 91, 81, -76, -29, 7, -77, -42, 39, -73, 29, 43, -60, 21, -5,
          -3, 1, 32, 34, -77, 49, 68, -1, -63, 93, -20, -57, -65, 53, 23, 96, 79, 87, -12, -18, 51, 39, -24, 27, 13,
          -55, -6, 28, 95, 91, -71, 77, 49, -26, -17, -83, 43, -86, 28, 20, 64, -6, 53, 40, 81, -30, -83, 67, -3, 25,
          37, 54, 95, 14, 84, -96, 76, 15, 35, 41, -86, 33, 10, -32, 59, 100, 30, -9, 58, -80, 23, 20, 43, 93, 58, -26,
          37, 44, -24, 27, 99, -46, -80, -85, -44, -45, -72, -32, 33, -24, 91, -67, 75, -40, 52, 49, 94, -10, 82, -76,
          -92, 58, 18, -43, 47, -75, -17, -30, -17, -57, 37, 51, -32, 69, 54, -71, -98, -74, -17, 99, 84, -67, 80, -24,
          -100, 98, 19, 99, -7, -98, -43, 73, -97, -21, 96, -44, 59]
target5 = -186
print(sorted(input5))
print(three_sum_close(input5, target5))
