
def is_palindrome(word):
    start = 0
    end = len(word) - 1
    is_palindrome = True
    while start < end:
        if word[start] != word[end]:
            return False
        start +=1
        end -=1
    return is_palindrome

def get_letter_frequencies(word):
    letter_freq = {}
    for letter in word:
        letter_freq[letter] = letter_freq.get(letter, 0) + 1
    
    evens = 0
    odds = 0
    for key in letter_freq:
        if letter_freq[key] % 2 == 0:
            evens +=1
        else:
            odds +=1
    if len(word) % 2 == 0 and odds == 0:
        return True
    elif len(word) % 2 != 0 and odds == 1:
        return True
    else:
        return False

print(get_letter_frequencies('civic'))
