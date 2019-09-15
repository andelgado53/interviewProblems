# Find Order Of Characters From Alien Dictionary
# Problem Statement:
# Given a sorted dictionary of an alien language, you have to find the order of characters in that language.
# (This is a popular interview problem.)
# Generally, dictionary does not contain duplicate values, but for the sake of this problem, 
# assume that dictionary might have duplicate values. (Sometimes interviewer tricks the question, 
# to see, how you will handle it.)
# Sample Input 1:
# words = ["baa", "abcd", "abca", "cab", "cad"]
# Sample Output 1:
# "bdac"

def compare_words(word1, word2):
    index1 = 0
    index2 = 0
    print(word1)
    print(word2)
    while index1 < len(word1) and index2 < len(word2) and word1[index1] == word2[index2]:
        index1 +=1
        index2 += 1
    if index1 < len(word1) and index2 < len(word2):
        return (word1[index1], word2[index2])
    return None

def build_graph(words):
    index = 1
    graph = {}
    graph[words[0][0]] = []
    while index < len(words):
        pair = compare_words(words[index - 1], words[index])
        if pair is not None:
            first, second = pair
            graph[second] = graph.get(second, [])
            temp_list = graph.get(first, list())
            temp_list.append(second)
            graph[first] = temp_list
        index += 1
    return graph


def find_order(words):
    graph = build_graph(words)
    seen = set()
    time = [0]
    top_order = []
    def dfs(node, graph):
        time[0] += 1
        seen.add(node)
        for letter in graph[node]:
            if letter not in seen:
                seen.add(letter)
                dfs(letter, graph)
        time[0] += 1
        end_time = time[0]
        top_order.append((end_time, node))
    for k in graph:
        if k not in seen:
            dfs(k, graph)
    print(top_order)
    print(graph)
    top_order = sorted(top_order, reverse=True)
    result  = [letter for rank, letter in top_order]
    return "".join(result)


# words = ["baa", "abcd", "abca", "cab", "cad"]
words = ["vvvv", "vvvc", "hhhhvv", "hhhcv", "ccc", "ccc"]
# print(compare_words("cab", "cad"))
# print(build_graph(words))
print(find_order(words))