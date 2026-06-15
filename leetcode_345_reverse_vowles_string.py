# 345. Reverse Vowels of a String
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
#
#
#
# Example 1:
#
# Input: s = "IceCreAm"
#
# Output: "AceCreIm"
#
# Explanation:
#
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
#
# Example 2:
#
# Input: s = "leetcode"
#
# Output: "leotcede"
#
#
#
# Constraints:
#
# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.

s = "leetcode"

def solution (s):
    vowels = "aeiouy"
    result = []
    s = list(s)

# loop through charecters in s, if charecter is not vowel keep same index and append to result, if charecter is vowel append to result with index[::-1]

    for i in range (len(s)):
        if s[i] not in vowels:
            result.append(s[i])
            print (result)
        else:
            result.append(s[i::-1])
            print (result)
    print (result)

print (solution(s))

