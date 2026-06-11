# Missing Number
#
# You are given:
#
# numbers
# N
#
# The array numbers contains distinct integers from:
#
# 1 ... N
#
# Exactly one number is missing.
#
# Return the missing number.
#
# The array is not guaranteed to be sorted.
#
# Example 1
numbers = [1,2,3,4]
N = 5
#
# Output:
#
# 3

def solution(numbers, N):
    numbers = sorted(numbers)
    for i in range (len(numbers)):
        if numbers[i] +1 != numbers[i+1]:
            return numbers[i]+1
        if numbers[0] != 1:
            return 1
        if numbers[len(numbers)-1] != N:
            return N
print (solution(numbers, N))
