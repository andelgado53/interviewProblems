# You are given an integer array arr, of size n. Group and rearrange them (in-place) into evens and odds in
# such a way that group of all even integers appears on the left side
# and group of all odd integers appears on the right side.


def group_numbers(data):
    left = 0
    right = len(data) - 1

    while left < right:
        while data[left] % 2 == 0 and left < len(data) - 1:
            left += 1
        while data[right] % 2 > 0 and right >= 0:
            right -= 1
        if left < right:
            temp = data[left]
            data[left] = data[right]
            data[right] = temp
            left += 1
            right -= 1

    return data


test1 = [3, 5]
print(group_numbers(test1))
test2 = [3]
print(group_numbers(test2))
test3 = [10, 90]
print(group_numbers(test3))
test4 = [4, 2, 1, 3]
print(group_numbers(test4))
test5 = [2, 4, 5, 7]
print(group_numbers(test5))
test6 = [1, 3, 5]
print(group_numbers(test6))