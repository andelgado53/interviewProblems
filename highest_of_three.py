numbers = [5, 6, 2, 3, 4, 1]
expected_value = 120
numbers1 = [10, 11, 9, 15, 20, 21]
negative_numbers = [-10, -10, 1, 3, 2]
other_example = [1, 10, -5, 1, -100, -12, 30, -8]




def get_highest_producr_of_three_3(numbers):
    highest = max(numbers[0], numbers[1])
    lowest = min(numbers[0], numbers[1])
    highest_prod_of_two = numbers[0] * numbers[1]
    lowest_prod_of_two = numbers[0] * numbers[1]
    highest_prod_of_3 = numbers[0] * numbers[1] * numbers[2]
    for x in range(2, len(numbers)):
        current = numbers[x]
        highest_prod_of_3 = max(current * highest_prod_of_two, current * lowest_prod_of_two, highest_prod_of_3)

        highest_prod_of_two = max(highest_prod_of_two, highest * current, lowest * current)
        lowest_prod_of_two = min(lowest_prod_of_two, highest * current, lowest * current)

        highest = max(highest, current)
        lowest = min(lowest, current)
    return highest_prod_of_3




print(get_highest_producr_of_three_3(numbers))
print(get_highest_producr_of_three_3(numbers1))
print(get_highest_producr_of_three_3(negative_numbers))
print(get_highest_producr_of_three_3(other_example))