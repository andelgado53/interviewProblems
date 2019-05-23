import pprint
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
# Example 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I


def pad(letter, num_rows, offset):
    column = [None] * num_rows
    column[offset] = letter
    return column


def get_columns(word, rows, offset):
    off = offset
    output = []
    start_index = 0
    column = []
    r = 0
    while start_index < len(word):
        while r < rows and start_index < len(word):
            column.append(word[start_index])
            r += 1
            start_index += 1
        if len(column) > 0:
            output.append(column)
            column = []
        r = 0
        while off >= 1 and start_index < len(word):
            output.append(pad(word[start_index], rows, off))
            off -= 1
            start_index += 1
        off = offset
    return output


def convert(word, row_nums):
    if len(word) <= 1 or row_nums == 0:
        return word
    rows = get_columns(word, row_nums, row_nums - 2)
    col = 0
    row = 0
    new_word = ''
    while col < len(rows[0]):
        while row < len(rows):
            if col < len(rows[row]) and rows[row][col] is not None:
                new_word = new_word + rows[row][col]
            row += 1
        col += 1
        row = 0
    return new_word


def test():
    test_word = "PAYPALISHIRING"
    assert convert(test_word, 5) == "PHASIYIRPLIGAN"

    assert convert(test_word, 4) == "PINALSIGYAHRPI"

    assert convert(test_word, 3) == "PAHNAPLSIIGYIR"

    assert convert(test_word, 2) == "PYAIHRNAPLSIIG"

    assert convert(test_word, 1) == "PAYPALISHIRING"


test()

