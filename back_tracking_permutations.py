
def get_permutations_helper(data, choosen):
    
    if len(data) == 0:
        print(choosen)
    
    else:
        for i in range(len(data)):
            value = data[i]
            choosen.append(value)
            data.pop(i)
            get_permutations_helper(data, choosen)

            data.insert(i, value)
            choosen.pop()


def get_permutations(data):
    choosen = []
    get_permutations_helper(data, choosen)


get_permutations(['a', 'b', 'c'])