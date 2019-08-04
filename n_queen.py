# n Queen Problem
# Problem Statement:
# The n-queen problem is the problem of placing n chess queens on an n * n chessboard, so that no two queens attack each other.
# Your task is to find ALL possible arrangements for the n-queen problem.
# You have to solve this problem using recursion. 
# (There may be other ways of solving this problem, but for the purpose of this exercise, please use recursion only).
# A queen can move horizontally, vertically, or diagonally.
# Sample Test Case:
# Sample Input:
# 4
# Sample Output:
# Suppose name of the returned array is ret.

# ret [0] =
# [
# "--q-",

# "q---",

# "---q",

# "-q--"
# ]

# ret [1] =
# [
# "-q--",

# "---q",

# "q---",

# "--q-"
# ]

import pprint
import time

def can_place(new_pos, postions, placed_cols):
    new_r, new_col = new_pos
    if new_col in placed_cols:
        return False
    for r, c in postions:
        if c == new_col or abs(r - new_r) == abs(c - new_col):
            return False
    return True

def print_row(col, cols):
    s = ""
    for c in range(cols):
        if c == col:
            s += "q"
        else:
            s += "-"
    return s

def find_all_arrangements(n):
    t1 = time.time()
    solutions = []
    def helper(n, row, out, placed_cols):
        if row == n:
            sp = []
            for p in out:
                s = print_row(p[1], n)
                sp.append(s)
            solutions.append(sp)
        else:
            for col in range(n):
                if can_place((row, col), out, placed_cols):
                    placed_cols.add(col)
                    helper(n , row+1, out + [(row, col)], placed_cols)
                    placed_cols.remove(col)
    helper(n, 0, [], set())
    print(time.time() - t1)
    return solutions


s = find_all_arrangements(11)
print(len(s))
# pprint.pprint(s)
