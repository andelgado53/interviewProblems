# https://leetcode.com/problems/palindrome-partitioning/
# Palindromic Decomposition Of A String
# Problem Statement:
# A palindromic decomposition of string is a decomposition of the string into substrings, 
# such that all those substrings are valid palindromes.
# Given a string s, you have to find ALL possible palindromic decompositions of it.
# Note that string s itself is also a substring of s.
# Sample Input:
# "abracadabra"
# Sample Output:
# [
#    "a|b|r|a|c|a|d|a|b|r|a",
#    "a|b|r|a|c|ada|b|r|a",
#    "a|b|r|aca|d|a|b|r|a"
# ]

def is_pal(s):
    if len(s) == 1 or len(s) == 0:
        return True
    else:
        if s[0] == s[-1]:
            return is_pal(s[1: -1])
        else:
            return False

            

def generate_palindromic_decompositions(s):
    output = []
    def helper(s, out):
        if len(s) == 0:
            output.append("|".join(out))
        else:
            for i in range(1, len(s)+1):
                if is_pal(s[:i]):
                    helper(s[i:], out + [s[:i]])
    helper(s, [])
    print(output)

# print(is_pal("ababa"))
generate_palindromic_decompositions("xxy")

print(is_pal())
