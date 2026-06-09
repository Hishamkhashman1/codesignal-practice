# You are given a string.
#
# Return the first character that appears exactly once.
#
# If no such character exists, return:
#
# "_"
# Example 1
text = "abacabad"
#
# Output:
#
# "c"
#
# because:
#
# a -> 4
# b -> 2
# c -> 1
# d -> 1
#
# and "c" is the first unique character encountered.

def solution(text):
    chars = list(text)
    for c in chars:
        if chars.count(c) == 1:
            return c
    return "_"
print(solution(text))
