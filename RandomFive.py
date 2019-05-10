import random
from pprint import pprint

# numbers = {}

# tries = 100000
# for n in range(tries):
#     number = random.randint(1, 7)
#     numbers[number] = numbers.get(number, 0) + 1

# for key in numbers:
#     numbers[key] = (numbers[key] * 1.0) / tries
# pprint(numbers)

def random5():
    while True:
        number = random.randint(1, 7)
        if number <= 5:
            break
    return number

# numbers = {}

# tries = 1000000
# for n in range(tries):
#     number = random5()
#     numbers[number] = numbers.get(number, 0) + 1

# for key in numbers:
#     numbers[key] = (numbers[key] * 1.0) / tries
# pprint(numbers)


def rand7() :
    buckets = {'11': -1,
                '12': 1,
                '13': 1,
                '14': 1,
                '15': 2,
                '21': 2,
                '22': 2,
                '23': 3,
                '24': 3,
                '25': 3,
                '31': 4,
                '32': 4,
                '33': 4,
                '34': 5,
                '35': 5,
                '41': 5,
                '42': 6,
                '43': 6,
                '44': 6,
                '45': 7,
                '51': 7,
                '52': 7,
                '53': -1,
                '54': -1,
                '55': -1}
    
    while True:
        dice1 = random.randint(1, 5)
        dice2 = random.randint(1, 5)
        key = str(dice1) + str(dice2)
        if buckets[key] != -1:
            return buckets[key]

  

numbers = {}
tries = 1000000
for n in range(tries):
    number = rand7()
    numbers[number] = numbers.get(number, 0) + 1

for key in numbers:
    numbers[key] = (numbers[key] * 1.0) / tries
# pprint(len(numbers.keys()))
pprint(numbers)