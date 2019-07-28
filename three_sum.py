# 3 Sum
# Problem Statement:
# Given an integer array arr of size N, find all magical triplets in it.
# Magical triplet is the group of 3 integers, whose sum is zero.
# Note that magical triplets may or may not be made of consecutive numbers in arr.
# Input/Output Format For The Function:
# Input Format:
# There is only one argument: integer array arr.
# Sample Input 1:
# arr = [10, 3, -4, 1, -6, 9];
# Sample Output 1:
# 10,-4,-6
# 3,-4,1
# Sample Test Case 2:
# Sample Input 2:
# arr = [12, 34, -46];
# Sample Output 2:
# 12,-46,34
# Sample Test Case 3:
# Sample Input 3:
# arr = [0, 0, 0];
# Sample Output 3:
# 0,0,0

def findZeroSum(arr):
    i = 0
    out = []
    arr.sort()
    while i < len(arr) - 2:
        k = len(arr) - 1
        j = i + 1
        while j < len(arr) - 1 and k > j:
            if arr[i] + arr[j] + arr[k] == 0:
                out.append(str(arr[i]) + ',' + str(arr[j]) + ',' + str(arr[k]))
                j += 1
                while j < len(arr) - 1 and arr[j] == arr[j-1]:
                    j += 1
            elif arr[i] + arr[j] + arr[k] > 0:
                k -= 1
            else:
                j += 1
        i += 1
        while i < len(arr) - 2 and arr[i] == arr[i-1]:
            i += 1
    return out

print(findZeroSum([12, 34, -46]))
print(findZeroSum([10, 3, -4, 1, -6, 9]))
print(findZeroSum([0, 0, 0]))
print(findZeroSum([0, 0, 0, 0, 0, 0]))
            
