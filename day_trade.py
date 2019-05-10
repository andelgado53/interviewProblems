stock_prices = [10, 7, 5, 8, 11, 9]

def get_max_profit(stock_prices):
    max_profit = -10000
    already_seen = set()

    for index, purchased_value in enumerate(stock_prices):
        for sell_value in stock_prices[index+1: ]:
            if (sell_value, purchased_value) not in already_seen:
                    profit = sell_value - purchased_value
                    if profit > max_profit:
                        max_profit = profit
            else:
                already_seen.add((sell_value, purchased_value))
    
    return max_profit

# print(get_max_profit(stock_prices))



def get_max_profit_2(stock_prices):
    last_index = len(stock_prices) - 1
    max_profit = -10000
    while last_index > 0:
        profit = stock_prices[last_index] - min(stock_prices[:last_index])
        last_index -=1
        if profit > max_profit:
            max_profit = profit
    return max_profit
# print(get_max_profit_2(stock_prices))

def proper_get_max_profit(prices):
    min_price = prices[0]
    max_profit = prices[1] - min_price

    x = 1
    while x < len(prices):
        potential_profit = prices[x] - min_price
        max_profit = max(max_profit, potential_profit)
        min_price = min(min_price, prices[x])
        x +=1
    return max_profit

print(proper_get_max_profit(stock_prices))