import pprint
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
#
#
# Above is a 7 x 3 grid. How many possible unique paths are there?
#
# Note: m and n will be at most 100.
#
# Example 1:
#
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# Example 2:
#
# Input: m = 7, n = 3
# Output: 28


def create_matrix(columns, rows):
    matrix = [[0] * columns for i in range(rows)]
    return matrix


def is_valid_move(matrix, row, col):
    return row <= len(matrix) - 1 and col <= len(matrix[0]) - 1


# this solution is slow and works for s small size matrix
def unique_paths_helper(matrix, row, col, paths, goal_row, goal_col):
    if row == goal_row and col == goal_col:
        paths.append(1)
        pprint.pprint(len(paths))
        return
    if is_valid_move(matrix, row, col + 1):
        matrix[row][col + 1] = '*'
        unique_paths_helper(matrix, row, col + 1, paths, goal_row, goal_col)
    if is_valid_move(matrix, row + 1, col):
        matrix[row + 1][col] = '*'
        unique_paths_helper(matrix, row + 1, col, paths, goal_row, goal_col)


def unique_paths(columns, rows) -> int:
    matrix = create_matrix(columns, rows)
    matrix[0][0] = '*'
    out = list()
    unique_paths_helper(matrix, 0, 0, out, rows - 1, columns - 1)
    return len(out)


m = create_matrix(7, 3)
pprint.pprint(unique_paths(5, 5))


# fast solution and works for any size matrix
def unique_paths_v2(columns, rows):
    matrix = create_matrix(columns, rows)

    last_col = columns - 1
    last_row = rows - 1

    for col in range(columns):
        matrix[last_row][col] = 1

    for row in range(rows):
        matrix[row][last_col] = 1

    start_row = rows - 2
    while start_row >= 0:
        start_col = columns - 2
        while start_col >= 0:
            matrix[start_row][start_col] = matrix[start_row][start_col + 1] + matrix[start_row + 1][start_col]
            start_col -= 1
        start_row -= 1
    return matrix[0][0]


print(unique_paths_v2(23, 12))