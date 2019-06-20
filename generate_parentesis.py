# https://leetcode.com/problems/generate-parentheses/
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


def is_valid_parenthesis(parethesis):
    stack = []
    for p in parethesis:
        if p == '(':
            stack.append(p)
        elif len(stack) > 0:
            stack.pop()
        else:
            return False
    if len(stack) == 0:
        return True
    else:
        return False


def generate_all_combinations(pairs):
    results = []

    def combinations(output, seen, pairs):
        if len(output) == pairs:
            if is_valid_parenthesis(output) and output not in seen:
                results.append(output)
                seen.add(output)
            return
        else:
            combinations(output + '(', seen, pairs)
            combinations(output + ')', seen, pairs)

    combinations('', set(), pairs * 2)
    return results


def test():
    assert generate_all_combinations(3) == ['((()))', '(()())', '(())()', '()(())', '()()()']


test()
