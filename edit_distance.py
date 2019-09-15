# Levenshtein Distance
# Problem Statement:
# Given two words word1 and word2, find the minimum number of steps required to 
# convert word1 to word2. (each operation is counted as 1 step.)
# You have the following 3 operations permitted on a word:
# a) Insert a character
# b) Delete a character
# c) Replace a character
# The minimum no of steps required to convert word1 to word2 with the given 
# set of allowed operations is called edit distance.

# e.g. Minimum edit distance between the words 'kitten' and 'sitting', is 3.
# kitten → sitten (substitution of "s" for "k")

# sitten → sittin (substitution of "i" for "e")

# sittin → sitting (insertion of "g" at the end)
import pprint 

def edit_distance(word1, word2):
    w1 = word1
    w2 = word2
    def helper(i1, i2):
        if i1 >= len(w1) and i2 >= len(w2):
            return 0
        if i1 >= len(w1):
            return 1 + helper(i1, i2+1)
        if i2 >= len(w2):
            return 1 + helper(i1+1, i2)
        if w1[i1] == w2[i2]:
            return helper(i1+ 1, i2+1)
        else:
            return 1 + min(helper(i1, i2+1), helper(i1+1, i2+1))
    return helper(0, 0)

def edit_distance_dp(word1, word2):
    matrix = [ [ 0 for i in range(len(word2) +1) ] for j in range(len(word1) +1)]
    r = len(word1)
    v = 0
    while r >= 0:
        matrix[r][len(word2)] = v
        r -= 1
        v += 1
    c = len(word2)
    v = 0
    while c >= 0:
        matrix[len(word1)][c] = v
        c -= 1
        v += 1
    row  = len(word1) - 1
    col = len(word2) - 1
    while row >= 0:
        while col >= 0:
            if word1[row] == word2[col]:
                matrix[row][col] = matrix[row+1][col+1]
            else:
                matrix[row][col] = 1 + min(matrix[row][col+1], matrix[row+1][col+1], matrix[row+1][col])
            col -= 1
        row -= 1
        col = len(word2) - 1
    pprint.pprint(matrix)
    return matrix[0][0]


    
        



w1 = 'a'
w2 = 'bc'
edit_distance_dp(w1, w2)
print(edit_distance(w1, w2))