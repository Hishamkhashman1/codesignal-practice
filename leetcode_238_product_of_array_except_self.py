# 238. Product of Array Except Self
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
#
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#
#
# Constraints:
#
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
# import math
nums = [1,2,3,4]

# def solution(nums):
#     products = []
#
#     for i in range (len(nums)):
#         # if i == 0:
#         #     product = math.prod(nums[i+1 : len(nums)])
#         #     products.append(product)
#         # elif i == -1:
#         #     product = math.prod(nums[0 : -2])
#         #     products.append(product)
#         #
#         # else:
#         product = math.prod(nums[:i] + nums[i+1 :len(nums)])
#         products.append(product)
#
#
#     return products

# print (solution(nums))


