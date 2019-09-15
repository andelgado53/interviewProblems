# String Transformation Using Given Dictionary Of Words
# Problem Statement:
# You are given a dictionary of words named words, and two strings named start and stop. All given strings have equal length. 
# Dictionary words are not in any particular order, there may be duplicates, too.
# You need to transform string start to string stop using given dictionary words. 
# In each transformation, you can only change one character of the current string. e.g. "abc" -> "abd" is a valid transformation, 
# because only one character 'c' is changed to 'd', but, "abc" -> "axy" is not a valid transformation, 
# because two characters are changed, character 'b' is changed to 'x' and character 'c' is changed to 'y'.
# In other words, you need to find out the least amount of transformations between two words start and stop, 
# given a specific set of allowed transformations words. In other words, you need to find 
# the shortest possible sequence of strings (two or more strings) such that:

# First string is start.
# Last string is stop.
# Every  string (except the first one) differs from the previous one by exactly one character.
# Every string (except, possibly, first and last ones) are in the dictionary of words.
# If two or more such sequences exist, any one of them is a correct answer.

# If no such sequence is there to be found, [“-1”] (a sequence of one string, “-1”) is the correct answer.
# Constraints:

# All input strings consist of lowercase Latin characters only.
# 0 <=  total number of characters in all dictionary words combined <= 10^5.

# Example
# For input n = 4, words = ["cat", "hat", "bad", "had"], start = “bat” and stop = “had”, output will be:
# bat
# hat
# had

def is_valid_transformation(word1, word2):
    cnt += 1
    index = 0 
    diff = 0
    while index < len(word1):
        if word1[index] != word2[index]:
            diff += 1
        if diff > 1:
            return False
        index += 1
    return diff == 1

def find_valind_transformation(start_word, words, seen):
    result = []
    for word in words:
        if word not in seen and is_valid_transformation(start_word, word):
            result.append(word)
    return result

def back_track(parents, start, end):
    if len(parents) == 0:
        return ['-1']
    current = end
    out = []
    while True:
        out.insert(0, current)
        current = parents.get(current)
        if current == start or current is None:
            break
    if len(out) >= 1:  
        out.insert(0, start)
        return out
    return ['-1']


def string_transformation(words, start, stop):
    if is_valid_transformation(start, stop):
        return [start, stop]
    unique_words = set(words)
    sorted_words = list(unique_words)
    seen = set()
    seen.add(start)
    q = []
    q.append(start)
    parents = {}
    while len(q) > 0:
        current = q.pop(0)
        for word in find_valind_transformation(current, sorted_words, seen):
            if is_valid_transformation(word, stop):
                parents[word] = current
                parents[stop] = word
                return back_track(parents, start, stop)
            if word not in seen:
                parents[word] = current
                q.append(word)
                seen.add(word)
    return ["-1"]

# print(cnt)
# print(sum(t))
# print(t)
# print(string_transformation(["cat", "hat", "bad", "had"], "bat", "hat"))
# words = []

# start = "zzzzzz"

# stop = "zzzzzz"
# print(is_valid_transformation(start, stop))
# print(string_transformation([], start, stop))


# w = ['aaa']
# s = 'baa'
# e = 'aab'
# print(string_transformation(w, s, e))
# # # print(is_valid_transformation('aaa', 'aab'))


# w = ['cat', 'hat', 'bad', 'had']
# s = 'bat'
# e = 'had'

# print(string_transformation(w, s, e))
# print(is_valid_transformation('zzzzz', 'zzzzz'))

# w = ['ggggnn', 'gggnnn', 'gggggn', 'ggnnnn', 'gnnnnn']

# s = 'gggggg'
# e = 'nnnnnn'
# print(string_transformation(w, s, e))


# w = ['cccw', 'accc', 'accw']
# s = 'cccc'
# e = 'cccc'

# print(string_transformation(w, s, e))

# print(is_valid_transformation('jh', 'oh'))

# print(find_valind_transformation('eaba', words))

# w = ['cccw', 'accc', 'accw']
# s = 'cccc'
# e = 'cccc'

# print(string_transformation(w, s, e))

# print(string_transformation(words, s, e))
