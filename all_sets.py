# Problem Statement:
# Given a set (in form of string s containing only distinct lowercase letters ('a' - 'z')), 
# you have to generate ALL possible subsets of it .

# Note that:

# empty set is always a subset of any set.
# whole set s should also be considered as its subset here.

# Sample Test Cases:
# Sample Input:
# "xy"
# Sample Output:
# ["", "x", "y", "xy"]

def generate_all_subsets(s):
    output = []
    def helper(s, out):
        if len(s) == 0:
            output.append(out)
            print(out)
        else:
            helper(s[1:], out)
            helper(s[1:], out + s[0])
    helper(s, "")
    return output

print(generate_all_subsets("xy"))