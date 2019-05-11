data = [5, 3, 4, 1, 9, 7, 8, 2, 6]

def merge_sort(data, start, end):
    mid = (start + end) // 2
    if len(data[start:end]) > 1:
        merge_sort(data, start, mid)
        merge_sort(data, mid, end)
        left = data[start: mid]
        right = data[mid: end]
        left_index = 0
        right_index = 0
        data_index = start

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                data[data_index] = left[left_index]
                left_index +=1
            else:
                data[data_index] = right[right_index]
                right_index +=1
            data_index +=1
        
        while left_index < len(left) and data_index < len(data):
            data[data_index] = left[left_index]
            left_index +=1
            data_index +=1
        
        while right_index < len(right) and data_index < len(data):
            data[data_index] = right[right_index]
            right_index +=1 
            data_index += 1

print('unsorted data ' + str(data))
merge_sort(data, 0 , len(data))
print(data)

