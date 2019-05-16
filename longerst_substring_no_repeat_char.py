# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


def lengthOfLongestSubstring(s: str):
    longest = {}
    longest_s = set()
    index = 0
    longest_word = ''
    current_word = ''
    while index < len(s):
        if s[index] not in longest_s:
            longest_s.add(s[index])
            longest[s[index]] = index
            current_word = current_word + s[index]
            index += 1
        else:
            print(current_word)
            new_index = longest[s[index]] + 1
            longest.clear()
            longest_s.clear()
            if len(current_word) > len(longest_word):
                longest_word = current_word
            current_word = ''
            index = new_index
    if len(current_word) > len(longest_word):
        return current_word
    return longest_word


print(lengthOfLongestSubstring("au"))