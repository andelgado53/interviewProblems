v = [8, 15, 3, 7]
# v = [149, 154, 63, 242, 12, 72, 65]
expected = 22

def maxWin(v):
    memo = {}
    def helper(i1, i2):
        if (i1, i2) in memo:
            return memo[(i1, i2)]
        if i1 == i2:
            return v[i1]
        if i1+1 == i2:
            return max(v[i1], v[i2])    
        val = max(v[i1] + min(helper(i1+2, i2), helper(i1+1, i2-1)), v[i2] + min(helper(i1+1, i2-1), helper(i1, i2-2)))
        memo[(i1, i2)] = val
        return val
    return helper(0, len(v)-1)

print(maxWin(v))  