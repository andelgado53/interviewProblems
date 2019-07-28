
# Dutch National Flag
# Problem Statement:
# You are given n balls. Each of these balls are of one the three colors: Red, Green and Blue. 
# They are arranged randomly in a line. Your task is to rearrange them such that all balls of the 
# same color are together and their collective color groups are in this order: Red balls first, 
# Green balls next and Blue balls last
# This combination of colors is similar to the Dutch National Flag, hence the problem name.

# This is a popular sorting problem.
# Constraints:
# 1 <= n <= 100000
# Do this in ONE pass over the array - NOT TWO passes, just one pass.
# Your solution can only use O(1) extra memory i.e. you have to do this in-place. 
# Don't use any other memory for processing.

# Sample Test Case:
# Sample Input:
# balls = [G, B, G, G, R, B, R, G]
# Sample Output:
# [R, R, G, G, G, G, B, B]

def dutch_flag_sort(balls):
    r = 0
    g = 0
    b = len(balls) - 1
    while g <= b:
        if balls[g] == 'R':
            temp = balls[r]
            balls[r] = balls[g]
            balls[g] = temp
            r += 1
            g += 1
        elif balls[g] == 'B':
            temp = balls[b]
            balls[b] = balls[g]
            balls[g] = temp
            b -= 1
        else:
            g += 1
    return balls

balls = ['G', 'B', 'G', 'G', 'R', 'B', 'R', 'G']
print(dutch_flag_sort(balls))
