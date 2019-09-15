# If n = 7 and steps = [2, 3], then input should be: 3

def countWaysToClimb(steps, n):
    def helper(steps, out):
        if out == 0:
            return 1
        elif out < 0:
            return 0
        else:
            ways = 0
            for s in steps:
                 ways += helper(steps, out - s)
            return ways
    return helper(steps, n)
            
print(countWaysToClimb([2,3], 7))

def countWaysToClimb_dp(steps, n):
    dp = [0] * (n+1)
    dp[0] = 1
    for step in steps:
        for i in range(n + 1):
            if i >= step:
                dp[i] +=  dp[i - step]
    print(dp)
countWaysToClimb_dp([2,3], 7)