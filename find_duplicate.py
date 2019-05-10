numbers = [2,3,1,5,4,5]

numbers1 = [1,2,3,1,1,4,6,4,2]

def find_duplicate(data):
    start = 1
    end = len(data)
    while start < end:
        mid = (start + end) / 2
        cnt = 0
        for number in data:
            if number <= mid and number >= start:
                cnt +=1
        expected_numbers_in_range = (mid - start + 1)

        if cnt > expected_numbers_in_range:
            end = mid 
        else:
            start = mid + 1
    return end



print(find_duplicate(numbers1))