
memo = {}
memo[0] = 0
memo[1] = 1

def fib(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]

print(fib(100))

def fib_non_recursive(n):
    one_before = 1
    two_before = 0

    for x in range(n - 1):
        current = one_before + two_before
        one_before = current
        two_before = one_before
    return current

print(fib_non_recursive(3))