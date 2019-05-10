
goal = 5
coins = [1,3,5]
def number_of_ways_to_make_change(goal, coins):
    ways = [0] * len(range(goal + 1))
    ways[0] = 1

    for coin in coins:
        index = 1
        while index < len(ways):
            if coin <= index:
                ways[index] = ways[index] + ways[index - coin]
            index += 1
    print(ways)
    return ways[goal]

print(number_of_ways_to_make_change(goal, coins))