from pprint import pprint
class Trie(object):

    def __init__(self):
        self.root_node = {}

    def add_word(self, word):
        current_node = self.root_node
        is_new_word = False

        for char in word:
            if char not in current_node:
                is_new_word = True
                current_node[char] = {}
            current_node = current_node[char]

        if "End Of Word" not in current_node:
            is_new_word = True
            current_node["End Of Word"] = {}

        return is_new_word

t = Trie()
print(t.add_word('andres'))
print(t.add_word('alfonso'))
print(t.add_word('alfredo'))
t.add_word('alfron')
t.add_word('alfrod')
t.add_word('alfro')
t.add_word('alfrin')
pprint(t.root_node)