# Problem from Cracking the Coding Interview.
# Chapter 1 Strings and Arrays.
# Given an image represented by an NxN matrix, Write a method to rotate the image by 90 degress.
#  Do it in place
import pprint

data = [
    [1,    2,    3,     4],
    [5,    6,    7,     8],
    [9,   10,   11,    12],
    [13,  14,   15,    16]
]
data1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
data2 = [
    [1, 2],
    [3, 4]
]


def rotate_matrix(matrix):
    layers = len(matrix) // 2
    for layer in range(layers):
        start = layer
        end = len(matrix[0]) - 1 - layer
        offset = 0
        while start < end:
            temp = matrix[layer][start]
            matrix[layer][start] = matrix[end - offset][start - offset]
            matrix[end - offset][start - offset] = matrix[end][end - offset]
            matrix[end][end - offset] = matrix[layer + offset][end]
            matrix[layer + offset][end] = temp
            start += 1
            offset += 1
    return matrix


pprint.pprint(data)
pprint.pprint(rotate_matrix(data))
print('******************')
pprint.pprint(data1)
pprint.pprint(rotate_matrix(data1))
print('******************')
pprint.pprint(data2)
pprint.pprint(rotate_matrix(data2))