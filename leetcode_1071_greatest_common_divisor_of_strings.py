# 1071. Greatest Common Divisor of Strings
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
#
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
#
#
#
# Example 1:
#
# Input: str1 = "ABCABC", str2 = "ABC"
#
# Output: "ABC"
#
# Example 2:
#
# Input: str1 = "ABABAB", str2 = "ABAB"
#
# Output: "AB"
#
# Example 3:
#
# Input: str1 = "LEET", str2 = "CODE"
#
# Output: ""
#
# Example 4:
#
# Input: str1 = "AAAAAB", str2 = "AAA"
#
# Output: ""​​​​​​​
#
#
#
# Constraints:
#
# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.
from math import gcd
str1 = "ABABAB"
str2 = "AB"





# loop into slices of the gcd and if match return the match
def solution(str1, str2):
    minimum_pattern = gcd(len(str1),len(str2))
    print (minimum_pattern)
    if minimum_pattern < 1:
        return ""
    else:
        for i in range(min(len(str1),len(str2))):
            if str1[i : minimum_pattern] == str2[i :minimum_pattern] and str2[i : minimum_pattern] * ( len (str1) // len(str2[i : minimum_pattern])) == str1 and str2[i : minimum_pattern] * ( len (str2) // len(str2[i : minimum_pattern])) == str2:
                return str2[i : minimum_pattern]
            return ""


print (solution(str1, str2))


# def solution(str1, str2):
#     for s in str2:
#         if s in str1:
#             return str2
# print (solution(str1, str2))
