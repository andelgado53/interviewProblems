# Problem Statement:
# You are given n balls. Each of these balls are of one the three colors: Red, Green and Blue. 
# They are arranged randomly in a line. Your task is to rearrange them such that all 
# balls of the same color are together and their collective color groups are in this order: 
# Red balls first, Green balls next and Blue balls last.

# This combination of colors is similar to the Dutch National Flag, hence the problem name.

# This is a popular sorting problem.

# Sample Input:
# balls = [G, B, G, G, R, B, R, G]
# Sample Output:
# [R, R, G, G, G, G, B, B]

#  RGB

def order(arr):
    r = 0
    g = 0
    b = len(arr) - 1

    while g <= b:
        if arr[g] == "G":
            g += 1
        elif arr[g] == "B":
            arr[g], arr[b] = arr[b], arr[g]
            b -= 1
        else:
            arr[r], arr[g] = arr[g], arr[r]
            r += 1
            g += 1
    return arr

print(order(["G", "B", "G", "G", "R", "B", "R", "G"]))



