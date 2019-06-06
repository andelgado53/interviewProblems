# https://leetcode.com/problems/3sum/
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


import time


class ThreeSum:

    def __init__(self):
        self.sets = list()
        self.seen = set()

    def three_sum(self, nums):
        start_time = time.time()
        self.three_sum_helper(nums, [])
        results = [list(r) for r in self.sets]
        end_time = time.time()
        print(end_time - start_time)
        return results

    def three_sum_helper(self, nums, output):
        if len(nums) == 0:
            if len(output) == 3 and sum(output) == 0:
                s = sorted(output)
                if tuple(s) not in self.seen:
                    self.seen.add(tuple(s))
                    self.sets.append(tuple(output))
            else:
                return
        else:
            current = nums.pop(0)
            self.three_sum_helper(nums, output)
            output.append(current)
            t = sorted(output)
            if len(output) <= 3 and tuple(t) not in self.seen:
                self.three_sum_helper(nums, output)
            nums.insert(0, current)
            output.pop()


input1 = [-13,5,13,12,-2,-11,-1,12,-3,0,-3,-7,-7,-5,-3,-15,-2,14,14,13,6,-11,-11,5,-15,-14,5,-5,-2,0,3,-8,-10,-7,11,-5,-10,-5,-7,-6,2,5,3,2,7,7,3,-10,-2,2,-12,-11,-1,14,10,-9,-15,-8,-7,-9,7,3,-2,5,11,-13,-15,8,-3,-7,-12,7,5,-2,-6,-3,-10,4,2,-5,14,-3,-1,-10,-3,-14,-4,-3,-7,-4,3,8,14,9,-2,10,11,-10,-4,-15,-9,-1,-1,3,4,1,8,1]
t = ThreeSum()

input2 = [-1, -2, -3, 4, 1, 3, 0, 3, -2, 1, -2, 2, -1, 1, -5, 4, -3]
r = t.three_sum(input1)
print(r)
print(len(r))
print(len(input1))
# 8.426038026809692, 7.463499069213867






