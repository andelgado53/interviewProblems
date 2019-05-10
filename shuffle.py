import random 

numbers = [0,1,2,3,4,5,6,7,8,9]

def shuffle(numbers):
    celining = len(numbers) - 1
    for x in range(len(numbers) - 1):
        new_index = random.randint(x, celining)
        if new_index != x:
            temp = numbers[x]
            numbers[x] = numbers[new_index]
            numbers[new_index] = temp
    return numbers

# shuffle(numbers)

def test_probabilities(tries, number_to_test):
    dists = {}
    
    for x in range(tries):
        numbers = [0,1,2,3,4,5,6,7,8,9]
        n = shuffle(numbers)
        for index in range(len(numbers) -1):
            if n[index] == number_to_test:
                dists[index] = (dists.get(index, 0) + 1)
            index =+1
    for key in dists:
        dists[key] = (dists[key] / (tries*1.0)) *100
    print('probability of number ' + str(number_to_test) + ': ' + str(dists))

for num in numbers:
    test_probabilities(100000, num)

    
