

data = [1, 3, 1, 3, 5, 6, 7, 5, 7, 6, 9, 9, 4]


def find_unique_id(data):
    unique_id  = 0
    for number in data:
        unique_id = number ^ unique_id
    return int(unique_id)


print(find_unique_id(data))