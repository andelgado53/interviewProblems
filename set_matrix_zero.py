# https://leetcode.com/problems/set-matrix-zeroes/
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
#
# Example 1:
#
# Input:
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output:
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# Example 2:
#
# Input:
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output:
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
import pprint


def set_zeroes(matrix):
    zero_cols = []
    zero_rows = []

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 0:
                zero_cols.append(c)
                zero_rows.append(r)
    for col in zero_cols:
        for r in range(len(matrix)):
            matrix[r][col] = 0

    for row in zero_rows:
        for c in range(len(matrix[row])):
            matrix[row][c] = 0
    return matrix


def set_zeros_no_space(matrix):
    is_first_col_zero = False
    ROWS = len(matrix)
    COLS = len(matrix[0])

    for row in range(ROWS):
        if matrix[row][0] == 0:
            is_first_col_zero = True
        for col in range(1, COLS):
            if matrix[row][col] == 0:
                matrix[0][col] = 0
                matrix[row][0] = 0

    for row in range(1, ROWS):
        for col in range(1, COLS):
            if matrix[row][0] == 0 or matrix[0][col] == 0:
                matrix[row][col] = 0

    if is_first_col_zero:
        for row in range(1, ROWS):
            matrix[row][0] = 0

    if matrix[0][0] == 0:
        for col in range(COLS):
            matrix[0][col] = 0

    pprint.pprint(matrix)


input1 = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
# pprint.pprint(set_zeroes(input1))
set_zeros_no_space(input1)

# assert set_zeroes(input1) == set_zeros_no_space(input1)

input2 = [
    [1,1,1],
    [1,0,1],
    [1,1,1]]
# pprint.pprint(set_zeroes(input2))
set_zeros_no_space(input2)
# assert set_zeroes(input2) == set_zeros_no_space(input2)