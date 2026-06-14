# 1431. Kids With the Greatest Number of Candies
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
#
# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
#
# Note that multiple kids can have the greatest number of candies.
#
#
#
# Example 1:
#
# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true] 
# Explanation: If you give all extraCandies to:
# - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
# - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
# - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
# - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
# - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
# Example 2:
#
# Input: candies = [4,2,1,1,2], extraCandies = 1
# Output: [true,false,false,false,false] 
# Explanation: There is only 1 extra candy.
# Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.
# Example 3:
#
# Input: candies = [12,1,12], extraCandies = 10
# Output: [true,false,true]
#
#
# Constraints:
#
# n == candies.length
# 2 <= n <= 100
# 1 <= candies[i] <= 100
# 1 <= extraCandies <= 50

candies = [2,3,5,1,3]


extracandies = 3




def solution(candies, extracandies):
    with_extra = []
    result = []
    max_candies = max(candies)
    print (max_candies)

    for c in candies:
        with_extra.append(c + extracandies)

    for c in with_extra:
        if c >= max_candies:
            result.append(True)

        else:
            if c < max_candies:
                result.append(False)

    print (with_extra)
    print (result)

    return result



print (solution(candies, extracandies))
