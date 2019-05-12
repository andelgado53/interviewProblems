# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.
#
# Example 1:
#
# Input: [2, 3, 1, 1, 4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:
#
# Input: [3, 2, 1, 0, 4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
# jump length is 0, which makes it impossible to reach the last index.

data = [2, 3, 1, 1, 4]


def can_jump_helper_dynamic(data, index):
    if index == len(data) - 1:
        return True
    else:
        for j in range(1, data[index] + 1):
            result = can_jump_helper_dynamic(data, j + index)
            if result:
                return result
    return False


def can_jump_dynamic(data):
    return can_jump_helper_dynamic(data, 0)


def can_jump_linear(data):
    last_good_index = len(data) - 1
    index = last_good_index

    while index >= 0:
        if data[index] + index >= last_good_index:
            last_good_index = index
        index -= 1
    if last_good_index == 0:
        return True
    else:
        return False


print(can_jump_linear(data))
print(can_jump_dynamic(data))
