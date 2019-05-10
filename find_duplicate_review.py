data = [1,2,1,3,4,5]

def find_duplicate(data):
    start = 1
    end = len(data) - 1
    while start < end:
        mid = (end + start) / 2
        lows = 0
        for e in data:
            if e >= start and e <= mid:
                lows +=1
        if lows > (mid - start) + 1:
            end = mid
        else:
            start = mid + 1
    return end


print(find_duplicate(data))