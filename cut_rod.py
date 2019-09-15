
n = 20
prices = {
    1: 3,
    2: 5,
    3 : 9,
    20: 11
}

def max_profit_rec(n, prices):
    def helper(n, prices, out):
        if n == 0:
            return out
        else:
            max_profit = 0
            for s in prices:
                if s <= n:
                    max_profit = max(max_profit, helper(n - s , prices, out + prices[s]))
        return max_profit
    return helper(n, prices, 0)

def max_profit(n, prices):
    sizes = [0] * (n+1)
    for l in prices:
        for s in range(len(sizes)):
            if s >= l:
                sizes[s] = max(sizes[s - l] + prices[l], sizes[s])
    return sizes[-1]

print(max_profit_rec(n, prices))

max_profit(n, prices)
                