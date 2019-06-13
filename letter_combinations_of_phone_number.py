# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Given a string containing digits from 2-9 inclusive, return all possible letter
# combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does
# not map to any letters.
#
# Example:
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
#
# Although the above answer is in lexicographical order, your answer could be in any order you want.


def find_combination_of_two(digit_one_values, digit_two_values):
    output = []
    for digit_one in digit_one_values:
        for digit_two in digit_two_values:
            output.append(digit_one + digit_two)
    return output


def letter_combinations(digits):
    mappings = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']}

    if len(digits) == 0:
        return []
    if len(digits) < 2:
        return mappings[digits]

    current = find_combination_of_two(mappings[digits[0]], mappings[digits[1]])
    current_index = 2
    while current_index < len(digits):
        current = find_combination_of_two(current, mappings[digits[current_index]])
        current_index += 1
    return current


def test():
    input1 = '23'
    assert letter_combinations(input1) == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']


test()