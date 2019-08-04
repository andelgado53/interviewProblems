# Given an array of sorted numbers some of which are duplicates, 
# move all unique numbers to the start of the array in place and return the number of unique numbers.

data = [1, 2, 2, 2, 3, 4, 4, 5, 5,6,8,8,8,9,9,9,9]

def count_unique(data):
    unique = 0
    current = 0
    while current < len(data) - 1:
        if data[current] != data[current + 1]:
            data[unique]  = data[current] 
            unique += 1
        current += 1
    data[unique]  = data[current]
    unique += 1
    print(unique)
    print(data)

count_unique(data)
    