
coins = [1,3,5]
goal = 5

def get_minimum_number_of_coins(goal, coins):
    amounts = [100000] * len(range(goal + 1))
    amounts[0] = 0
    index = 1
    while index < len(amounts):
        for coin in coins:
            if coin <= index and amounts[index - coin] + 1 < amounts[index]:
                amounts[index] = amounts[index - coin] + 1
        index += 1
    print(amounts)
    return amounts[goal]

print(get_minimum_number_of_coins(goal, coins))

def get_minimum_number_of_coins_one(goal, coins):
    amounts = [100000] * len(range(goal + 1))
    amounts[0] = 0
    
    for coin in coins:
        index = 1
        while index < len(amounts):
            if coin <= index and amounts[index - coin] + 1 < amounts[index]:
                amounts[index] = amounts[index - coin] + 1
            index +=1
    print(amounts)
    return amounts[goal]

print(get_minimum_number_of_coins_one(goal, coins))

