# Count the frequency of elements in an array in place
# input [2, 3, 1, 2, 3]
# output [0, -1, -2, -2, 0]


def count_frequency(data):
    index = 0
    while index < len(data):
        key = data[index]
        if key < 0:
            index += 1
        elif data[key] > 0:
            temp = data[key]
            data[index] = temp
            data[key] = - 1
        else:
            data[index] = 0
            data[key] = data[key] - 1
            index += 1
    return data


def test():
    assert count_frequency([1, 1]) == [0, -2]
    assert count_frequency([1, 1, 2]) == [0, -2, -1]
    assert count_frequency([2, 3, 1, 2, 3]) == [0, -1, -2, -2, 0]


test()

