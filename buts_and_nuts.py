NUTS = [4, 32, 5, 7]

BOLTS = [32, 7, 5, 4]


    
def helper(pivot, bolts, start, end):
    if start > end:
        return
    left = start
    right = len(bolts) - 1
    i = start
    while i < len(bolts):
        if bolts[i] == pivot:
            break
        i += 1
    temp = bolts[start]
    bolts[start] = bolts[i]
    bolts[i] = temp
    while left <= right:
        while left <= end and bolts[left] <= pivot:
            left += 1
        while right > end and bolts[right] >= pivot:
            right -= 1
        if left < right:
            temp = bolts[left]
            bolts[left] = bolts[right]
            bolts[right] = temp
            left += 1
            right -= 1
    temp = bolts[right]
    bolts[right] = bolts[start]
    bolts[start] = temp
    print("bolts " + str(bolts))
    return right


nuts = [38, 32, 35, 9, 19, 21, 6]
bolts = [6, 32, 35, 21, 38, 19, 9]

NUTS = [4, 32, 5, 7] 
BOLTS = [32, 7, 5, 4]

p = helper(38, bolts, 0, 6)
for n in nuts[1:]:
    if n > bolts[p]:
        p = helper(n, bolts, p + 1, 6)
        print(p)
    elif n < bolts[p]:
        p = helper(n, bolts, 0,  p -1)
        print(p)
    else:
        break
    # helper(n, bolts, 0, 6)

    

# n = helper(38, bolts, 0, 6)  
# print(n)
# n = helper(32, bolts, 0, 5)
# print(n)
# n = helper(32, bolts, 0, 5)
# print(BOLTS)
# print(solve(nuts, bolts)) 
# helper(6, [6, 32, 35, 9, 19, 21, 38], 0, len([6, 32, 35, 9, 19, 21, 38])-1)



