data = [1,2,3,4,5,6,7,7]
#  sum of all numbers in a sequence n + (n+1) + ((n+1)+1) = (n^2 + n) /2

def find_duplicate_number(data):
    actual_sum = 0
    for num in data:
        actual_sum += num
    
    expected_sum = (len(data)**2 + len(data)) // 2
    assert expected_sum > actual_sum
    duplicate = len(data) - (expected_sum - actual_sum)
    print(duplicate)

find_duplicate_number(data)