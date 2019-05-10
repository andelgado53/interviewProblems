
# letters = ['a', 'b']

def get_permutations(letters):
    output = []
    get_permutations_helper(letters, output)

def get_permutations_helper(letters, output):
    if len(letters) == 0:
        print(output)
        return 
    
    index = 0
    for letter in letters:
        current_letter = letters[index]
        letters.remove(letter)
        output.append(current_letter)
        get_permutations_helper(letters, output)
        letters.insert(index, current_letter)
        output.pop()
        index +=1

get_permutations(['1'])

# l = [1,2,3,4]
# print(l.pop())