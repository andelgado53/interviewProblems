from random import shuffle
deck = [1,2,3,4,5,6,7,8,9,10,11,  12,13,14,15,16,17,18,19, 20]


shuffled_deck = [1,2,3,4,5, 12,13,14,   15, 6,7,8,9,10,11,  16,17,18,19,20]


def is_single_riffle2(shuffled_deck):
    half1 = [1,2,3,4,5,6,7,8,9,10,11]
    half2 = [12,13,14,15,16,17,18,19, 20]

    index1 = 0
    index2 = 0

    start_index = 0

    while start_index < len(shuffled_deck):
        if index1 < len(half1) and shuffled_deck[start_index] == half1[index1]:
            print("processing: " + str(shuffled_deck[start_index]))
            start_index +=1
            index1 += 1
        elif index2 < len(half2) and shuffled_deck[start_index] == half2[index2]:
            print("processing: " + str(shuffled_deck[start_index]))
            start_index +=1
            index2 += 1
        else:
            return False
    return True

def flip_halves(current_half, half1, half2):
    if current_half == half1:
        return half2
    return half1

def is_sorted(array):
    next_index = 1
    start = 0
    while next_index <= len(array)- 1:
        if array[next_index] < array[start]:
            return False
        else:
            next_index +=1
            start +=1
    return True

def is_single_riffle(shuffled_deck):
    half1 = []
    half2 = []
    current_half = half1
    start_index = 0
    next_index = 1
    while next_index <= len(shuffled_deck):
        if next_index == len(shuffled_deck)  or shuffled_deck[start_index] - shuffled_deck[next_index] == - 1:
            current_half.append(shuffled_deck[start_index])
        else:
            current_half.append(shuffled_deck[start_index])
            current_half = flip_halves(current_half, half1, half2)
        start_index +=1
        next_index +=1
    return is_sorted(half1) and is_sorted(half2)
    


# print(is_single_riffle(shuffled_deck))
shuffle(deck)
print(deck)
print(is_single_riffle2(deck))