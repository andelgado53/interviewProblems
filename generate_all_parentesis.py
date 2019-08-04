
# Given a positive integer n, find ALL well formed round brackets string of length 2*n.

# The purpose of this problem is to learn recursion and not DP. 
# So, you must write at least one recursive solution. After that, you can write a DP solution if you want.

def is_well_formed(s):
    stack = []
    open_p = "("
    close_p = ")"
    for p in s:
        if p == open_p:
            stack.append(p)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    return len(stack) == 0


def find_all_well_formed_brackets(n):
    output = []
    def helper(n, out):
        if n == 0:
            if is_well_formed(out):
                output.append(out)
        else:
            helper(n-1, out + "(")
            helper(n-1, out + ")")
    helper(n*2, "")
    return output


def find_all_well_formed_brackets_v2(n):
    results = []
    def helper(o, c, out):
        if o == 0 and c == 0:
            results.append(out)
        elif o == c:
            helper(o - 1, c, out + "(")
        else:
            if o > 0:
                helper(o - 1, c, out + "(")
            if c > 0:
                helper(o, c - 1, out + ")")
    helper(n, n, "")
    return results

n = 12
a = find_all_well_formed_brackets(n)
# print(a)
print("******")
find_all_well_formed_brackets_v2(n)