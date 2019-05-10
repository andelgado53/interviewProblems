words = 'After beating the eggs, Dana read the next step: Add milk and eggs, then add flour and sugar.'

def word_cloud(words):
    punctuation = set([',', '.', ':', ';', '!', '@', '#', '%', '(', ')', '[', ']'])
    words_counter = {}
    list_of_words = words.split(' ')
    for word in list_of_words:
        if word[-1] in punctuation:
            words_counter[word[:-1].lower()] = words_counter.get(word[:-1].lower(), 0) + 1
        else:
            words_counter[word.lower()] = words_counter.get(word.lower(), 0) + 1
    print(words_counter)

word_cloud(words)