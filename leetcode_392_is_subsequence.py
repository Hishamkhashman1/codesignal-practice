# 392. Is Subsequence
# Easy
# Topics
# premium lock icon
# Companies
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
#
#
#
# Example 1:
#
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
#
# Input: s = "axc", t = "ahbgdc"
# Output: false
#
#
# Constraints:
#
# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.
#
#
# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
s = "aaaaaa"
t = "bbaaaa"

# my solution which works for the example cases 

# def solution(s,t):
#     s_pass = []
#     t_pass = []
#
#     if s == "":
#         return True
#
#
#     for c in s:
#         if c in t:
#             s_pass.append(c)
#
#     for i in range (len(s)):
#         target_char = s[i]
#
#         for j in range (len(t)):
#             if t[j] == target_char:
#                 t_pass.append((target_char,j))
#
#
#     t_indexed = []
#
#     for item in t_pass:
#         index = item[1]
#         t_indexed.append(index)
#
    # for i in range (len(t_indexed)-2):
    #     if t_indexed[i] < t_indexed[i+1] < t_indexed[i+2]:
    #         return True
    # return False


#
#
#     print (s_pass)
#     print (t_pass)
#     print (t_indexed)
# print (solution(s,t))

# classic two pointer solution

def solution(s,t):
    i = 0

    for c in t:
        if i < len(s) and c == s[i]:
            i += 1
    return i == len(s)

print (solution(s,t))
