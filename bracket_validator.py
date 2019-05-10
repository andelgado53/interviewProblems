
def validate_brackets(string):
    openers = set(['(', '{', '['])
    closers = { ')': '(', '}': '{', ']': '['}
    stack = []

    for letter in string:
        if letter in openers:
            stack.append(letter)
        elif letter in closers:
            opener = stack.pop()
            if closers[letter] != opener:
                return False
    
    if len(stack) > 0:
        return False
    return True

print(validate_brackets("{ [ ] ( ) }"))

print(validate_brackets("{ [ ( ] ) }"))

print(validate_brackets("{ [ }"))