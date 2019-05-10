from reverse_string_in_place import reverse_in_place
message = [ 'c', 'a', 'k', 'e', ' ','p', 'o', 'u', 'n', 'd', ' ','s', 't', 'e', 'a', 'l' ]

def reverse_slice_array(array, start, end):
    while start < end:
        new = array[start]
        array[start] = array[end]
        array[end] = new
        start +=1
        end -=1


# n + n


def reverse_words(input):
    reverse_in_place(input)
    start = 0
    end = 0
    while end < len(input):
        if input[end] == ' ':
            reverse_slice_array(input, start, end - 1)
            start = end + 1
            end = start
        elif end == len(input) - 1:
            reverse_slice_array(input, start, end)
            end +=1
        else:
            end +=1

print(message)
