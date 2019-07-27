# Top K
# Problem Statement:

# You are given an array of integers arr, of size n, which is analogous to a continuous stream of integers input. 
# Your task is to find K largest elements from a given stream of numbers.

# By definition, we don't know the size of the input stream. Hence, 
# produce K largest elements seen so far, at any given time. For repeated numbers, return them only once.

# If there are less than K distinct elements in arr, return all of them.
# Note:
# Don't rely on size of input array arr.
# Feel free to use built-in functions if you need a specific data-structure.

# Sample Input 1:
# arr = [1, 5, 4, 4, 2]; K = 2
# Sample Output 1:
# [4, 5]

# Sample Test Case 2:
# Sample Input 2:
# arr = [1, 5, 1, 5, 1]; K = 3
# Sample Output 2:
# [5, 1]
import heapq

def topK(arr, k):
    heap = []
    seen = set()
    heapq.heapify(heap)
    cnt = 0 
    for element in arr:
        if cnt < k and element not in seen:
            cnt += 1
            seen.add(element)
            heapq.heappush(heap, element)
        else:
            if element > heap[0] and element not in seen:
                heapq.heappop(heap)
                heapq.heappush(heap, element)
                seen.add(element)
    return heap

print(topK([1, 5, 4, 4, 2], 2))
print(topK([1, 5, 1, 5, 1], 3))