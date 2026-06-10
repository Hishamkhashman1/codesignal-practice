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
#is the longest run.
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
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Q3 — Replace Each Element With Neighbor Sum
#
# You are given a list of integers numbers.
#
# Return a new list result where each element is replaced by the sum of itself and its immediate neighbors.
#
# If a neighbor does not exist, ignore it.
#
# Example 1
# numbers = [4, 0, 1, -2, 3]
#
# Output:
#
# [4, 5, -1, 2, 1]
#
# Explanation:
#
# result[0] = 4 + 0 = 4
# result[1] = 4 + 0 + 1 = 5
# result[2] = 0 + 1 + (-2) = -1
# result[3] = 1 + (-2) + 3 = 2
# result[4] = -2 + 3 = 1
# Example 2
# numbers = [10]
#
# Output:
#
# [10]
#
# def solution(numbers):
#     result =[]
#     for i in range(len(numbers)):
#         if 0 <= i-1 and i+1 < len(numbers):
#             total = numbers[i] + numbers[i-1] + numbers[i+1]
#             result.append(total)
#         else:
#             if i == 0:
#                 total = numbers[i] + numbers[i+1]
#                 result.append(total)
#         if i == (len(numbers)-1):
#             total = numbers[len(numbers)-1] + numbers [len(numbers)-2]
#             result.append(total)
#     return result
#---------------------------------------------------------------------------------------------------------------------------------------------
# Dictionary Frequency count


# # Given:
#
# numbers = [1,2,2,3,3,3,4]
#
# #Return a dictionary with key= numbers and values = count:
#
# # {
# #  1:1,
# #  2:2,
# #  3:3,
# #  4:1
# # }
# dictionary_numbers = dict(enumerate(numbers))
#
# # print (dictionary_numbers)
# #
# # result_dict = {}
# #
# # for n in numbers:
# #     if n in result_dict:
# #         result_dict[n] += 1
# #     else:
# #         result_dict[n] = 1
# # print (result_dict)
#
# def solution(numbers):
#     count_dict = {}
#     for n in numbers:
#         if n in count_dict:
#             count_dict[n] +=1
#         else:
#             count_dict[n] = 1
#     return count_dict
# print(solution(numbers))
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#Exercise 2 — Most Frequent Character
#
# Given:
#
# text = "banana"
#
# Return:
#
# "a"
#
# because:
#
# a -> 3
# n -> 2
# b -> 1
#
# Target:
#
# 5 minutes
#
# Hint:
#
# max(dictionary, key=dictionary.get)
# def solution(text):
#     result_dict = {}
#     for c in text:
#         if c in result_dict:
#             result_dict[c] += 1
#         else:
#             result_dict[c] = 1
#     return max(result_dict, key=result_dict.get)
# print (solution(text))
#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 3 — First Character Appearing Twice
# text = "abccba"

# return the first character appearing twice

# def solution(text):
#     seen = []
#     for c in text:
#         if c in seen:
#             return c
#         else:
#             seen.append(c)
#------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 4 — Count Distinct Values
# Given:
#
# numbers = [1,2,2,3,3,3,4]
# #
# # Return:
# #
# # 3
# def solution(numbers):
#     seen = []
#     count = 0
#     for n in numbers:
#         if n not in seen:
#             seen.append(n)
#             count += 1
#     return count
# print (solution(numbers))
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 5 — Dictionary Warm-up

# Given:
#
# numbers = [5,5,5,2,2,7]
#
# Return:
#
# 2
#
# because:
#
# 7 -> 1 occurrence
# 2 -> 2 occurrences
# 5 -> 3 occurrences
#
# and we want the number with the lowest frequency.
#
# def solution(numbers):
#     dict = {}
#     for n in numbers:    
#         if n in dict:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return min(dict, key=dict.get)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
# First Non-Repeating Character (try dictionary)
# Given:
#
# text
#
# Return the first character that appears exactly once.
#
# If none exist, return:
#
# "_"
# Example
# text = "abacaad"
# #
# # Output:
# #
# # "c"
#
# def solution(text):
#     for c in text:
#         if text.count(c) == 1:
#             return c
#
# def solution_dict(text):
#     counts = {}
#     for c in text:
#         counts[c] = counts.get(c,0) +1
#     for c in text:
#         if counts[c] == 1:
#             return c
#     return "_"
# print(solution_dict(text))
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Q2 — Character Frequencies Match

# Given two strings:
#
# s1
# s2
#
# Return:
#
# True
#
# if every character appears the same number of times in both strings.
#
# Otherwise return:
#
# False
# Example 1
# s1 = "aabbcc"
# s2 = "ccbbaa"
#
# Output:
#
# True
#
# because:
#
# a -> 2
# b -> 2
# c -> 2
#
# in both strings.

# array solution
#
# def solution_array(s1,s2):
#     if sorted(s1) == sorted(s2):
#         return True
#     return False
#
# def solution_dict(s1,s2):
#     counts_s1 = {}
#     counts_s2 = {}
#     for c in s1:
#         counts_s1[c] = counts_s1.get(c,0) +1
#     for c in s2:
#         counts_s2[c] = counts_s2.get(c,0) +1
#     return True if counts_s1 == counts_s2 else False 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Realistic Q3-lite (Hashmap + Arrays)
#
# Given a list of integers:
#
# numbers
#
# Return:
#
# True
#
# if there exist two different elements whose sum equals 10.
#
# Otherwise return:
#
# False
# Example 1
# numbers = [1,4,3,1]
# #i
# Output:
#
# True
#
# because:
#
# 1 + 9 = 10
# target = 10
# def solution(numbers, target):
#     sums = {}
#     for i, n in enumerate(numbers):
#         difference = target - n
#         if difference in sums:
#             return True
#         sums[n] = i
#     return False
#



# def solution(numbers, target):
#     hashmap = {}
#     for i, number in enumerate(numbers):
#         difference = target - number
#         if difference in hashmap:
#             return [hashmap[difference],i]
#         hashmap[number] = i
#     return None
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Q2/Q3 — Count Pairs Equal to Target
#
# Given:
#
# numbers = [1, 4, 6, 9]
# target = 10
# #
# # Return the number of pairs whose sum equals the target.
# #
# # Example 1
# # numbers = [1,4,6,9]
# # target = 10
# #
# # Pairs:
# #
# # 1 + 9
# # 4 + 6
# #
# # Output:
# #
# # 2
# #
# def solution(numbers, target):
#     count = 0
#     seen = {}
#     for i, n in enumerate(numbers):
#         difference = target - n
#         if difference in seen:
#             count += 1
#         seen[n] = i
#     return count
# print (solution(numbers,target))
#---------------------------------------------------------------------------------------------------------------------------------------------------------
# Q4 — Lookup Table
#
# Given an array of unique integers numbers, return the number of pairs of indices (i, j) such that:
#
# i <= j
#
# and:
#
# numbers[i] + numbers[j]
#
# is a power of 2.
#
# Powers of 2 include:
#
# 1, 2, 4, 8, 16, 32, ...
# Example 1
# numbers = [1, -1, 2, 3]
#
# Output:
#
# 5
#
# Valid pairs:
#
# (-1, 2) = 1
# (1, 1) = 2
# (-1, 3) = 2
# (1, 3) = 4
# (2, 2) = 4
#
# def solution(numbers):
#     totals = 0
#     for i, n in enumerate(numbers):
#         for j, n in enumerate(numbers):
#             if i <= j:
#                 sum = numbers[j] + numbers[i]
#                 if sum >0 and bin(sum).count("1") == 1:
#                     totals += 1
#     return totals
# print (solution(numbers))
