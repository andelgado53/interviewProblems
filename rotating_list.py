data = [5,6,7,8,9,10,11,13,14,15,16,0,1,2,3,4]


# def find_rotation_point(data, start, end):
#     most_right = data[0]
#     first_rotation_point_found = -1
#     end = len(data) -1
#     while start < end:
#         mid = (start + end) / 2
#         if data[mid] < most_right:
#             first_rotation_point_found = mid
#             break
#         elif data[start] <= data[mid]:
#             start = mid + 1
#     # print(first_rotation_point_found)
#     if first_rotation_point_found:
#         while first_rotation_point_found >= 1:
#             if data[first_rotation_point_found] < data[first_rotation_point_found - 1]:
#                 return first_rotation_point_found
#             first_rotation_point_found -=1
#     return -1


data = [5,6,7,8,9,10,11,13,14,15,16,17,18,0,1,2,3,4]


def find_rotation_point1(data):
    first_value = data[0]
    start = 0
    end = len(data) - 1
    while start < end:
        mid = (start + end) / 2
        print('start ' + str(start) + ' mid ' + str(mid) + ' end ' + str(end))
        if data[mid] >= first_value:
            start = mid
        else:
            end = mid
        if start + 1  ==   end:
            print('==================')
            return end
    return -1

print(find_rotation_point1(data))
# print(find_rotation_point(data, 0, len(data)-1))
def find_rotation_point(words):
    first_word = words[0]
    floor_index = 0
    ceiling_index = len(words) - 1
    while floor_index < ceiling_index:
        guess_index = floor_index + ((ceiling_index - floor_index) / 2)
        print('start ' + str(floor_index) + ' mid ' + str(guess_index) + ' end ' + str(ceiling_index))
        if words[guess_index] >= first_word:
            floor_index = guess_index
        else:
            ceiling_index = guess_index
        if floor_index + 1 == ceiling_index:
            return ceiling_index

print(find_rotation_point(data))