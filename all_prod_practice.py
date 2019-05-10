data = [1, 7, 3, 4]
expected = [84, 12, 28, 21]

def prod_all_except_index(data):
    prods = [1] * len(data)
    index = 1
    prod = data[0]
    while index < len(data):
        prods[index] = prod
        prod = prod * data[index]
        index +=1
    index = len(data) - 2
    prod = data[-1]
    while index >= 0:
        prods[index] = prods[index] * prod
        prod = prod * data[index]
        index -=1
    print(prods)

prod_all_except_index(data)