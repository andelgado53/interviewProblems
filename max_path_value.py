
matrix = [
    [2, 5, 1],
    [3, 6, 7],
    [5,                                                                                               9, 10]
]

def max_paths_rec(m):
    out = []
    memo = {}
    def helper(m, r, c, memo):
        if r == len(m) -1 and c == len(m[0]) -1:
            return m[r][c]
        if r == len(m) or c == len(m[0]):
            return 0
        if (r+1, c) in memo:
            l = memo[(r+1, c)]
        else:
            l = helper(m, r + 1, c, memo)
            memo[(+ m[r][c])] = l 
        if (r, c+1) in memo: 
            ri = memo[(r, c+1)] 
        else:
            ri = helper(m, r, c+1, memo) 
            memo[(r, c+1)] = ri
        return max(ri, l) + m[r][c]
        
    m = helper(m, 0, 0, memo)
    print(m)
    return out

print(max_paths_rec(matrix))

