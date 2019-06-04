# Implement atoi which converts a string to an integer.
#
# The function first discards as many whitespace characters as necessary until
# the first non-whitespace character is found. Then, starting from this character,
# takes an optional initial plus or minus sign followed by as many numerical digits as possible,
# and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the integral number,
# which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number,
# or if no such sequence exists because either str is empty or it contains only whitespace characters,
# no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
#
# Note:
#
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store
# integers within the 32-bit signed integer range: [−231,  231 − 1].
# If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
# Example 1:
#
# Input: "42"
# Output: 42
# Example 2:
#
# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sign.
#              Then take as many numerical digits as possible, which gets 42.
# Example 3:
#
# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
# Example 4:
#
# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numerical
#              digit or a +/- sign. Therefore no valid conversion could be performed.
# Example 5:
#
# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
#              Therefore INT_MIN (−231) is returned.


def strip_leading_chars_from_word(word, char_to_strip):
    index = 0
    while index < len(word):
        if word[index] == char_to_strip:
            index += 1
        else:
            return word[index:]
    return word[index:]


def find_digits(word):
    output = ''
    for char in word:
        if char.isdigit():
            output += char
        else:
            break
    return output


def check_for_int_overflow(digits):
    # -2147483648' to 2147483647'
    max_val = '2147483647'
    max_num_of_digits = 10
    start_digit = 2
    end_digit = 8
    if (len(digits) > max_num_of_digits) \
            or (len(digits) == max_num_of_digits and (int(digits[0]) == start_digit and int(digits[-1]) >= end_digit)
                or (len(digits) == max_num_of_digits and int(digits[0]) > 2)):
        return max_val
    return digits


def get_int_with_overflow(digits):
    max_num_of_digits = 10
    sign = digits[0]
    digits_only = digits[1:]
    if len(digits_only) < max_num_of_digits:
        return digits
    elif sign == '+':
        if len(digits_only) > max_num_of_digits:
            return '+2147483647'
        elif int(digits_only[0]) == 2 and int(digits_only[1:]) > 147483647:
            return '+2147483647'
        elif int(digits_only[0]) > 2:
            return '+2147483647'
        else:
            return digits

    elif sign == '-':
        if len(digits_only) > max_num_of_digits:
            return '-2147483648'
        elif int(digits_only[0]) == 2 and int(digits_only[1:]) > 147483648:
            return '-2147483648'
        elif int(digits_only[0]) > 2:
            return '-2147483648'
        else:
            return digits
    else:
        return digits


def atoi(word):
    output = ''
    plus = '+'
    minus = '-'
    plus_or_minus = {plus, minus}
    clean_word = strip_leading_chars_from_word(word, ' ')

    if len(clean_word) == 0:
        return 0

    if clean_word[0] in plus_or_minus and len(clean_word) >= 2 and clean_word[1].isdigit():
        sign = clean_word[0]
        digits = find_digits(clean_word[1:])
        clean_word_digits = strip_leading_chars_from_word(digits, '0') if len(digits) > 1 else digits
        output = get_int_with_overflow(sign + clean_word_digits)
    elif clean_word[0].isdigit():
        digits = find_digits(clean_word)
        clean_word_digits = strip_leading_chars_from_word(digits, '0') if len(digits) > 1 else digits
        output = get_int_with_overflow('+' + clean_word_digits)

    if len(output) > 1:
        return int(output)

    return 0


def test_atoi():
    input1 = '42'
    assert atoi(input1) == 42
    input2 = "   -42"
    assert atoi(input2) == -42
    input3 = '4193 with words'
    assert atoi(input3) == 4193
    input4 = 'words and 987'
    assert atoi(input4) == 0
    input5 = '-91283472332'
    assert atoi(input5) == -2147483648
    input6 = '456 letters and then another number 2345'
    assert atoi(input6) == 456
    input7 = 'letter then +more letters'
    assert atoi(input7) == 0
    input8 = '+'
    assert atoi(input8) == 0
    input9 = "  0000000000012345678"
    assert atoi(input9)
    input10 = '    0000000000000   '
    assert atoi(input10) == 0
    input11 = ''
    assert atoi(input11) == 0
    input12 = ' '
    assert atoi(input12) == 0
    input13 = '+'
    assert atoi(input13) == 0
    input14 ='     +0a32'
    assert atoi(input14) == 0
    input15 = '2147483648'
    assert atoi(input15) == 2147483647
    input16 = '2147483800'
    assert atoi(input16) == 2147483647
    input17 = '-2147483649'
    assert atoi(input17) == -2147483648


def test_get_int_with_overflow():
    input1 = '+2147483648'
    assert get_int_with_overflow(input1) == '+2147483647'
    input2 = '+2147483649'
    assert get_int_with_overflow(input2) == '+2147483647'
    input3 = '+999999999999'
    assert get_int_with_overflow(input3) == '+2147483647'
    input4 = '+1147483648'
    assert get_int_with_overflow(input4) == '+1147483648'
    input5 = '+2147483800'
    assert get_int_with_overflow(input5) == '+2147483647'


def test_strip_leading_chars_from_word():
    space = ' '
    input1 = ' hello'
    assert strip_leading_chars_from_word(input1, space) == 'hello'
    input2 = '    world'
    assert strip_leading_chars_from_word(input2, space) == 'world'
    input3 = ' abc '
    assert strip_leading_chars_from_word(input3, space) == 'abc '
    input4 = '42'
    assert strip_leading_chars_from_word(input4, space) == '42'
    input5 = '0000000000012345678'
    assert strip_leading_chars_from_word(input5, '0') == '12345678'


test_strip_leading_chars_from_word()
test_get_int_with_overflow()
test_atoi()