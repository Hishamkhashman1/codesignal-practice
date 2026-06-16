# 334. Increasing Triplet Subsequence
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# Example 2:
#
# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# Example 3:
#
# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: One of the valid triplet is (1, 4, 5), because nums[1] == 1 < nums[4] == 4 < nums[5] == 6.
#
#
# Constraints:
#
# 1 <= nums.length <= 5 * 105
# -231 <= nums[i] <= 231 - 1
nums =[20,100,10,12,5,13]

# def solution(nums):
#     check = 0   
#     for i in range (len(nums)-2):
#             for j in range (i +1, len(nums)-1):
#                 for k in range (j +1, len(nums)):
#                     if nums[i] < nums[j] < nums[k]:
#                          check +=1
#                          print (nums[i],nums[j], nums[k])
#
#     if check > 0:
#         return True
#     else:
#         return False
#
# print (solution(nums))

# def solution_on2(nums):
#     for j in range(1, len(nums) -1):
#         left_smaller = False
#         right_bigger = False
#
#         for i in range(0, j):
#             if nums[i] < nums [j] :
#                 left_smaller = True
#
#         for k in range (j +1, len(nums)):
#             if nums [j] < nums [k] :
#                 right_bigger = True
#
#         if left_smaller and right_bigger:
#             return True
#
#     return False
#
# print (solution_on2(nums))

def solution_On0(nums):
    first_seen = float("inf")
    second_seen = float("inf")

    for n in nums:
        if n <= first_seen:
            first_seen = n

        elif n <= second_seen:
            second_seen = n

        else:
            return True
    return False

print (solution_On0(nums))


