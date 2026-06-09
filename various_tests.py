# Question: revisting Two Sum

# numbers = [2,7,11,15]
# target = 9
#
# def solution(numbers, target):
#     hashmap = {}
#     for i, number in enumerate(numbers):
#         difference = target - number
#         if difference in hashmap:
#             return [hashmap[difference],i]
#         hashmap[number] = i
#     return None

#-----------------------------------------------------------------------------------------------------------------------------
# Q1 Array Analysis

# from list of integers , return True if the list contains three consecutive identical number

# numbers = [1,2,2,1,3]
#
# def solution(numbers):
#     for i in range(len(numbers)-2):
#         if numbers[i] == numbers[i+1] == numbers[i+2]:
#             return True
#     return False
# print(solution(numbers))
#----------------------------------------------------------------------------------------------------------------------------
# Q1 — Consecutive Increasing Numbers
#
# You are given a list of integers.
#
# Return True if there exist three consecutive elements such that:
#
# a[i] + 1 = a[i+1]
# a[i+1] + 1 = a[i+2]
#
# Otherwise return False.
#
# Example 1
# numbers = [5, 7, 8, 9, 3]
#
# Output:
#
# True
#
# because:
#
# 7, 8, 9
#
# are consecutive increasing numbers.

# def solution(numbers):
#     for i in range(len(numbers)-2):
#         if numbers[i] + 1 == numbers[i+1] and numbers[i] +2 == numbers[i+2]:
#             return True
#     return False
#--------------------------------------------------------------------------------------------------------------------------------
# Q1 — Adjacent Difference
#
# You are given a list of integers.
#
# Return True if there exist two adjacent elements whose difference is exactly 1.
#
# Otherwise return False.
#
# Example 1
# numbers = [5, 8, 2, 4]
#
# Output:
#
# True
#
# because:
#
# 3 and 4
#
# differ by exactly 1.
#
# def solution(numbers):
#     for i in range(len(numbers)-1):
#         if numbers[i+1] - numbers[i] == 1 or numbers[i] - numbers[i+1] ==1:
#             return True
#     return False
#-----------------------------------------------------------------------------------------------------------------------------------
# Q2 — First Repeated Number
#
# You are given a list of integers numbers.
#
# Return the first number that appears twice.
#
# If no number appears twice, return:
#
# -1
# Example 1
# numbers = [2, 1, 3, 5, 3, 2]
# #
# # Output:
# #
# # 3
# #
# # because 3 is the first value that appears again.
# def solution(numbers):
#     list_to_test = []
#     for n in numbers:
#         if n in list_to_test:
#             return n
#         else:
#             list_to_test.append(n)
#     return -1
# print (solution(numbers))
#-----------------------------------------------------------------------------------------------------------------------------------
# Q2 Return the first number that appears exactly once 
#Example:
#
# numbers = [2,3,2,4,3,5]
#
# #Output:
#
# #4
#
# def solution(numbers):
#     seen =[]
#     for n in numbers:
#         if n not in seen and numbers.count(n) == 1:
#             return n
#         else:
#             seen.append(n)
#-------------------------------------------------------------------------------------------------------------------------------------
# Q2 — Anagram Check
#
# Given two strings:
#
# s1
# s2
#
# Return:
#
# True
#
# if they are anagrams of each other.
#
# Otherwise return:
#
# False
#
# Two strings are anagrams if they contain exactly the same characters with the same frequencies.
#
# Example
# s1 = "gello"
# s2 = "silent"
# #
# # Output:
# #
# # True
# # Example
# # s1 = "hello"
# # s2 = "world"
# #
# # Output:
# #
# # False
#
# def solution(s1,s2):
#     if sorted(s1) == sorted(s2):
#         return True
#     return False
#-------------------------------------------------------------------------------------------------------------------------------------
# Q2 — Common Characters Count
#
# You are given two strings s1 and s2.
#
# Return the number of characters they have in common.
#
# Each character should only be counted as many times as it appears in both strings.
#
# Example 1
# s1 = "zzzz"
# s2 = "zz"
#
# Output:
#
# 3
# def solution(s1,s2):
#     common = []
#     for i in range(len(s1)):
#         for j in range(len(s2)):
#             if s1[i] == s2[j] and s1[i] not in common:
#                 common.append(s1[i])
#             else:
#                 if s2[j] == s2[i] and s2[j] not in common:
#                     common.append(s2[j])
#     return common
# print (solution(s1,s2))
#
# def solution_2(s1,s2):
#     seen_s1 = []
#     count = 0
#     for c in s1:
#         if c not in seen_s1 and c in s2:
#             seen_s1.append(c)
#     for c in seen_s1:
#         if s1.count(c) < s2.count(c):
#             count += s1.count(c)
#         else:
#             count += s2.count(c)
#     return count
#-------------------------------------------------------------------------------------------------------------------------------------------------
# Q2+ — Longest Consecutive Run
#
# You are given a list of integers.
#
# Return the length of the longest sequence of identical consecutive numbers.
#
# Example 1
# numbers = [1,1,7,7]
#
# Output:
#
# 3
#
# because:
#
# 1,1,1
#
# is the longest run.
# def solution(numbers):
#     current_count = 1
#     max_count = 1
#     for i in range (len(numbers)-1):
#         if numbers[i] == numbers[i+1]:
#             current_count += 1
#         else:
#             current_count = 1
#         if current_count > max_count:
#             max_count = current_count
#
#     return max_count
#
