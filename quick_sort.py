from random import shuffle
import unittest

data = [5, 3, 1, 6, 2, 4, 9, 8, 7]
shuffle(data)
def quick_sort(data, start, end):
    pivot = get_pivot(data, start, end)
    if (start < end):
        quick_sort(data, start, pivot-1)
        quick_sort(data, pivot+1, end)




    

def get_pivot(data, start, end):
    done = False
    left = start
    right = end
    while left < right and not done:
        pivot = data[start]
        while data[right] > pivot and right > start:
            right -=1
        while data[left] <= pivot and left < end:
            left +=1
        if (right <= left):
            done = True
            temp = data[right]
            data[start] = temp
            data[right] = pivot
        else:
            temp = data[right]
            data[right] = data[left]
            data[left] = temp
    return right

def test():
    data = [5, 3, 1, 6, 2, 4, 9, 8, 7]
    
    for x in range(1000):
        shuffle(data)
        quick_sort(data, 0, len(data) -1)
        assert data == [1, 2, 3, 4, 5, 6, 7, 8, 9]

test()
