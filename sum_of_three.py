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


class ThreeSum:

    def __init__(self):
        self.sets = list()
        self.seen = set()

    def three_sum(self, nums):
        # this solution uses backtracking to find all possible sets,
        # pruning anything greater then 3 and avoiding duplicates.
        self.three_sum_helper(nums, [])
        results = [list(r) for r in self.sets]
        return sorted([sorted(x) for x in results])

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

    @staticmethod
    def three_sum2(data):
        # This solution is n^3
        index1 = 0
        index2 = 1
        index3 = 2
        output = []
        seen = set()
        while index1 < len(data):
            while index2 < len(data):
                while index3 < len(data):
                    if data[index1] + data[index2] + data[index3] == 0:
                        s = sorted([data[index1], data[index2], data[index3]])
                        if tuple(s) not in seen:
                            seen.add(tuple(s))
                            output.append([data[index1], data[index2], data[index3]])
                    index3 += 1
                index2 += 1
                index3 = index2 + 1
            index1 += 1
            index2 = index1 + 1
            index3 = index2 + 1
        return sorted([sorted(s) for s in output])

    @staticmethod
    def three_sum3(data):
        pos_map = {}
        index = 0
        seen = set()
        results = []
        while index < len(data):
            pos_map[data[index]] = index
            index += 1
        index1 = 0
        index2 = 1
        while index1 < len(data):
            while index2 < len(data):
                needed = - data[index1] - data[index2]
                need_pos = pos_map.get(needed, None)
                if need_pos is not None and need_pos > index2:
                    sorted_trio = sorted([data[index1], data[index2], data[need_pos]])
                    tuple_trio = tuple(sorted_trio)
                    if tuple_trio not in seen:
                        results.append([data[index1], data[index2], data[need_pos]])
                        seen.add(tuple_trio)
                index2 += 1
            index1 += 1
            index2 = index1 + 1
        return sorted([sorted(s) for s in results])


def test():
    t = ThreeSum()
    input1 = [-13, 5, 13, 12, -2, -11, -1, 12, -3, 0, -3, -7, -7, -5, -3, -15, -2, 14, 14, 13, 6, -11, -11, 5, -15, -14, 5,
              -5, -2, 0, 3, -8, -10, -7, 11, -5, -10, -5, -7, -6, 2, 5, 3, 2, 7, 7, 3, -10, -2, 2, -12, -11, -1, 14, 10, -9,
              -15, -8, -7, -9, 7, 3, -2, 5, 11, -13, -15, 8, -3, -7, -12, 7, 5, -2, -6, -3, -10, 4, 2, -5, 14, -3, -1, -10,
              -3, -14, -4, -3, -7, -4, 3, 8, 14, 9, -2, 10, 11, -10, -4, -15, -9, -1, -1, 3, 4, 1, 8, 1]
    assert ThreeSum().three_sum(input1) == t.three_sum2(input1) == t.three_sum3(input1)
    input2 = [-1, -2, -3, 4, 1, 3, 0, 3, -2, 1, -2, 2, -1, 1, -5, 4, -3]
    assert ThreeSum().three_sum(input2) == t.three_sum2(input2) == t.three_sum3(input2)
    input3 = [3, 0, -2, -1, 1, 2]
    assert ThreeSum().three_sum(input3) == t.three_sum2(input3) == t.three_sum3(input3)
    input4 = [14, -11, -2, -3, 4, -3, -3, -8, -15, 11, 11, -6, -14, -13, 5, -10, -13, 0, -12, -8, 14, -12, -10, 2, -4, 9,
              13, 10, 2, 7, -2, -7, 4, 11, 5, -7, -15, 10, -7, -14, 6, 11, -5, 7, 6, 8, 5, 8, -7, 8, -15, 14, 11, 13, 1,
              -15, 7, 0, 10, -14, 14, -15, -14, 3, 4, 6, 4, 4, -7, 12, 5, 14, 0, 8, 7, 13, 1, -11, -2, 9, 12, -1, 8, 0, -11,
              -5, 0, 11, 2, -13, 4, 1, -12, 5, -10, -1, -12, 9, -12, -11, -2, 9, -12, 5, -6, 2, 4, 10, 6, -13, 4, 3, -7,
              -11, 11, -3, -9, -4, -15, 8, -9, -4, -13, -14, 8, 14]
    assert ThreeSum().three_sum(input4) == t.three_sum2(input4) == t.three_sum3(input4)
    input5 = [-3, 14, -10, -1, 12, 13, -3, 2, -6, 4, 13, 7, -8, 4, 0, -13, 11, -4, 7, 0, 4, -3, 12, 11, 5, -14, -8, 8, 3,
              -1, -8, -15, -2, -11, -9, -12, 9, 3, 5, -11, -8, 3, 3, -9, -15, -12, -15, 3, -9, 0, -12, 3, 12, -14, -1, -6,
              -13, -2, -13, -3, 12, -14, -3, -13, -9, 3, -10, -15, 13, 2, 11, 13, -9, -1, 11, 13, -6, 4, 1, 1, -11, 5, -11,
              8, -2, -5, -12, -8, 8, -10, 4, -3, -8, -14, -1, -10, -4, -3, 12, -14, 14, 9, 6, 12, -15, 3, 10, -13, -8, -11,
              3, -4, 1, -1]
    assert ThreeSum().three_sum(input5) == t.three_sum2(input5) == t.three_sum3(input5)
    input6 = [12, 0, 3, -14, 5, -11, 11, -5, -2, -1, 6, -7, -10, 1, 4, 1, 1, 9, -3, 6, -15, 0, 6, 1, 6, -12, 3, 7, 11, -6,
              -8, 0, 9, 3, -7, -1, 7, -10, 1, 13, -4, -7, -9, -7, 9, 3, 1, -13, -3, 13, 8, -11, -9, -8, -3, 4, -13, 7, -11,
              5, -14, -4, -9, 10, 6, -9, -6, -9, -12, 11, -11, -9, 11, -5, 0, -3, 13, -14, -1, -13, 7, -7, 14, 5, 0, -4, -6,
              -6, -11, -2, 14, -10, 2, 12, 8, -7, -11, -13, -9, 14, 5, -5, -9, 1, -2, 6, 5, -12, -1, -10, -9, -9, -10, 12,
              11]
    assert ThreeSum().three_sum(input6) == t.three_sum2(input6) == t.three_sum3(input6)
    input7 = [-12, -1, 4, -14, 0, 10, 7, -7, -6, 9, 6, -2, 7, 13, 9, -1, 4, 12, 9, 4, 14, 0, -4, 0, 0, 10, 2, -7, 7, -4,
              -11, 10, 2, 8, 4, -12, -4, -12, -4, -3, 12, 9, 11, 4, -1, -3, 10, -12, -6, -4, -1, -14, 3, 2, -7, -11, -3, 10,
              -11, -10, 13, -15, 7, 0, 0, -4, -5, 11, 0, -2, -14, -11, -8, 12, 1, -1, -14, -12, -6, -5, 0, 9, -4, -12, -4,
              4, 14, 9, -9, 10, 14, -11, 10, 6, -3, -4, 10, -1, 14, -13, 13, 7, -9, 12, 4, -1, -4, 5, 3, 6, 8, 10, 0, 11,
              13, 11, -7, 5, -3, -1, 0, -4, -4, -4, 10, 0]
    assert ThreeSum().three_sum(input7) == t.three_sum2(input7) == t.three_sum3(input7)
    input8 = [-1, -2, -3, 4, 1, 3, 0, 3, -2, 1, -2, 2, -1, 1, -5, 4, -3]
    assert ThreeSum().three_sum(input8) == t.three_sum2(input8) == t.three_sum3(input8)
    input9 = [-1, 0, 1, 2, -1, -4]
    assert ThreeSum().three_sum(input9) == t.three_sum2(input9) == t.three_sum3(input9)


test()





