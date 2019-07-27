import heapq
# This is a popular facebook problem.
# Given K sorted arrays arr, of size N each, merge them into a new array res, such that res is a sorted array.
# Assume N is very large compared to K. N may not even be known. The arrays could be just sorted streams,
# for instance, timestamp streams.
# All arrays might be sorted in increasing manner or decreasing manner.
# Sort all of them in the manner they appear in input.
# Note:
# Repeats are allowed.
# Negative numbers and zeros are allowed.
# Assume all arrays are sorted in the same order. Preserve that sort order in output.
# It is possible to find out the sort order from at least one of the arrays.


class MaxHeap:
    def __init__(self):
        self.values = []

    def pop(self):
        result = self.values.pop(1)
        new_head = self.values.pop()
        self.values.insert(1, new_head)
        if new_head:
            self.heapify(1)
        return result

    def push(self, value):
        self.values.append(value)
        self.bubble_up(len(self.values) - 1)

    def heapify(self, index):
        if len(self.values) == 3:
            max_val = max(self.values[1], self.values[2])
            min_val = min(self.values[1], self.values[2])
            self.values[1] = max_val
            self.values[2] = min_val
            return
        parent = self.values[index]
        left_child = index * 2
        right_child = (index * 2) + 1
        if left_child >= len(self.values) or right_child >= len(self.values):
            return
        if parent > self.values[left_child] and self.values[parent] > self.values[right_child]:
            return
        elif self.values[left_child] > self.values[right_child]:
            self.values[index] = self.values[left_child]
            self.values[left_child] = parent
            self.heapify(left_child)
        else:
            self.values[index] = self.values[right_child]
            self.values[right_child] = parent
            self.heapify(right_child)

    def bubble_up(self, index):
        parent = self.values[index // 2]
        while parent is not None and parent < self.values[index]:
            self.values[index // 2] = self.values[index]
            self.values[index] = parent
            self.bubble_up(index // 2)


# m = MaxHeap()
# m.values = [None, 7, 5, 6, 4, 3, 2, 1]
# print(m.values)
# m.push(8)
# print(m.values)
# m.push(10)
# print(m.values)
# while len(m.values) > 1:
#     print(m.pop())
#     print(m.values)

def get_direction(array):
    i = 0
    while i < len(array) - 2:
        if array[i] <= array[i + 1]:
            i += 1
        else:
            return -1
    return 1


def merge_k_sorted_arrays(arrays):
    heap = []
    heapq.heapify(heap)
    array_len = len(arrays[0])
    out_put = []
    array_index = 0
    # heap items = value, index in arra, array index
    ordering = get_direction(arrays[0])
    for array in arrays:
        heapq.heappush(heap, (ordering * array[0], 0, array_index))
        array_index += 1
    while len(heap) > 0:
        value, index, index_arr = heapq.heappop(heap)
        out_put.append(ordering * value)
        if index == array_len - 1:
            continue
        new_value = arrays[index_arr][index + 1]
        heapq.heappush(heap, (ordering * new_value, index + 1, index_arr))
    return out_put


input1 = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11], [-1, 0, 12, 13]]
input2 = [[34, 26, 20, 13, 11, 7, 4, 4], [41, 34, 27, 23, 19, 10, 8, 0], [26, 25, 19, 12, 7, 7, 7, 5]]

print(merge_k_sorted_arrays(input2))
print(merge_k_sorted_arrays(input1))
