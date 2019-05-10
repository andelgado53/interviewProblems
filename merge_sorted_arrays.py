my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14]

third_list = [16, 17, 18, 19]

def merge_sorted_lists(array1, array2):

    index1 = 0
    index2 = 0
    merged_results = []

    while index1 < len(array1) and index2 < len(array2):
        if array1[index1] < array2[index2]:
            merged_results.append(array1[index1])
            index1 +=1
        
        else:
            merged_results.append(array2[index2])
            index2 +=1
    
    while index1 <  len(array1):
        merged_results.append(array1[index1])
        index1 +=1
    
    while index2 <  len(array2):
        merged_results.append(array2[index2])
        index2 +=1

    return merged_results

# print(merge_sorted_lists(my_list, alices_list))

input = [my_list, alices_list, third_list]

def merge_sorted_list_of_arrays(array_of_arrays):
    current = array_of_arrays[0]
    next_array = 1
    while next_array < len(array_of_arrays):
        current = merge_sorted_lists(current, array_of_arrays[next_array])
        next_array +=1
    return current

print(merge_sorted_list_of_arrays(input))

