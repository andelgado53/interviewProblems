
data = [ 1, 2, 1, 3, 4, 8]
data1 = [1,2,3,4,5]

def find_cycle(array):
    p = 0
    q = 0
    while True:
        if p >= len(array) or q >= len(array):
            return False
        p = array[p]
        if p == q:
            return True
        if p >= len(array)-1:
            return False
        p = array[p]
        if p == q:
            return True
        if p >= len(array)-1:
            return False
        q = array[q]
        if p == q:
            return True

    return False

print(find_cycle(data))