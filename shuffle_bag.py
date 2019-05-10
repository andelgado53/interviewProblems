

# , (3, 90), (2, 15)
cake_tuples = [(7, 160), (3,90), (2,15)]
capacity    = 20

def shuffle_bag(capacity, cakes):
    capacities = [0] * len(range(capacity + 1))
    
    for cake in cake_tuples:
        weight = cake[0]
        value = cake[1]
        index = 1
        while index < len(capacities):
            if weight <= index and (capacities[index - weight] + value) > capacities[index]:
                capacities[index] = capacities[index - weight] + value
            index +=1
    return capacities[capacity]
            





print(shuffle_bag(capacity, cake_tuples))