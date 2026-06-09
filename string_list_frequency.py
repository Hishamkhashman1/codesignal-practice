# You are given a string text.
#
# Return the character that appears most frequently.
#
# If multiple characters have the same highest frequency, return the one that appears first in the string.
#
# Example 1
#
text = "banana"
#
# Output:
#
# "a"
#
# because:
#
# a -> 3
# n -> 2
# b -> 1

def solution(text):
    list_letters = list(text)
    dict_with_count = {}

    for letter in list_letters:
        dict_with_count[letter] = dict_with_count.get(letter, 0) +1
    return max(dict_with_count, key=dict_with_count.get)
print (solution(text))
