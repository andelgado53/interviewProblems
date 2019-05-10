input = ['a', 'b', 'c', 'd', 'e', 'f']

def reverse_in_place(input):
    start = 0
    end = len(input) - 1

    while start < end:
        new = input[start]
        input[start] = input[end]
        input[end] = new
        start +=1 
        end -=1
    return input

# print(reverse_in_place([ 'c', 'a', 'k', 'e', ' ','p', 'o', 'u', 'n', 'd', ' ','s', 't', 'e', 'a', 'l' ])) 


