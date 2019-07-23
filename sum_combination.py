# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
# find all unique combinations in candidates where the candidate numbers sums to target.

# The same repeated number may be chosen from candidates unlimited number of times.

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# Example 2:

# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
import pprint

class Solution:
    def combinationSum(self, candidates, target):
        ways_to_make = {0: [[0]]}
        for candidate in candidates:
            for target in range(target + 1):
                if candidate <= target:
                    if target - candidate in ways_to_make:
                        ways = ways_to_make.get(target, [])
                        if target - candidate == 0:
                            ways.append([candidate])
                        else:
                            for left_over in ways_to_make[target - candidate]:
                                c = left_over + [candidate]
                                ways.append(c)
                        ways_to_make[target] = ways
        return ways_to_make.get(target, [])

def test():
    s = Solution()
    candidates = [2,3,6,7]
    target = 7
    pprint.pprint(s.combinationSum(candidates, target))
    candidates1 = [2,3,5]
    target1 = 8
    pprint.pprint(s.combinationSum(candidates1, target1))
    target2 = 10
    candidates2 = [2, 4, 6, 8]
    pprint.pprint(s.combinationSum(candidates2, target2))


test()