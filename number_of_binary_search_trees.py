# How Many Binary Search Trees With n Nodes?
# Problem Statement:
# Write a function that will return the number of binary search trees that can be constructed with n nodes.
# There may be other iterative solutions, but for the purpose of this exercise, please use recursive solution.
# The purpose of this problem is to learn recursion and not DP. So, you must write at least one recursive solution. 
# After that, you can write a DP solution if you want.

def num_of_bst_dynamic(n):
    memo = [0] * n
    memo[0] = 1
    memo[1] = 1
    for x in range(2, n):
        for i in range(x):
            memo[x] = memo[x] + (memo[i] * memo[x - i - 1])
    print(memo)

num_of_bst_dynamic(11)

def num_of_bst_rec(n):
    def helper(n):
        if n == 0 or n == 1:
            return 1
        else:
            result = 0 
            for i in range(n):
                left = num_of_bst_rec(i) 
                right = num_of_bst_rec(n- i - 1)
                result += (left * right)
        return result
    return helper(n)
    

print(num_of_bst_rec(100))