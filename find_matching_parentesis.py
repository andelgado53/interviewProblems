
sentence = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."

def find_macthing_parentesis(sentence, start):
    open_stack = []
    opens = '('
    closes = ')'
    index = 0
    indeces = {}
    for letter in sentence:
        if letter == opens:
            open_stack.append(index)
        elif letter == closes:
            temp = open_stack.pop()
            # if temp == start:
                # return index   
            indeces[temp] = index
        index += 1
    return indeces

print(find_macthing_parentesis(sentence, 10))

def find_macthing_parentesis_1(sentence, start):
    cnt = 0
    opens = '('
    closes = ')'
    index = start + 1
    for letter in sentence[start+1:]:
        if letter == opens:
            cnt +=1
        elif letter == closes:
            cnt -=1
        if cnt < 0:
            return index
        index +=1

print(find_macthing_parentesis_1(sentence, 68))



