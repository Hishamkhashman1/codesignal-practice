# You are given an integer array nums consisting of n elements, and an integer k.
#
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
#
#
#
# Example 1:
#
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

nums = [1,12,-5,-6,50,3]
k = 4

def solution(nums,k):
    max_sums = []

    if k == 1:
        return max(nums)

    for i in range (len(nums)-3):
        sums = sum(nums[i:(i + k)])

        if sums not in max_sums:
            max_sums.append(sums)

    return max(max_sums, default=0) / 4





print (solution(nums,k))
