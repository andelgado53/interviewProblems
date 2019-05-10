a = [1, 12, 15, 15, 19, 20, 21]
b = [2, 15, 17, 19, 21, 21, 21, 21]
expected = [ 15, 19, 21]
def find_intersect(array1, array2):
    x = 0
    y = 0
    inter = []
    while x < len(array1) and y < len(array2):
        if array1[x] == array2[y]:
            inter.append(array1[x])
            x += 1
            y += 1
        elif array2[y] > array1[x]:
            x += 1
        elif array1[x] > array2[y]:
            y += 1
    return inter

print(find_intersect(a, b))