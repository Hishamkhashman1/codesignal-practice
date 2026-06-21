# 283. Move Zeroes
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
#
#
#
# Example 1:
#
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
#
# Input: nums = [0]
# Output: [0]
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1

nums = [0,1,0,3,12]


def solution (nums):
    nums_not_0 = []
    for n in nums:
        if n != 0:
            nums_not_0.append(n)

    for i in range (len(nums_not_0),len(nums)):
        nums_not_0.append(0)

    nums[:] = nums_not_0

    return nums
    

print (solution(nums))

