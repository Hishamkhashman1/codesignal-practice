# You are given a list of integers numbers and an integer k.
#
# Return the maximum sum of any k consecutive elements.

numbers = [2, 1, 5, 1, 3, 2]
k = 3

def solution(numbers, k):
    total = []
    
    for i in range (len(numbers)):
        if i + 2 < len(numbers):
            sum_slice = sum(numbers[i : i+k])
            total.append(sum_slice)
    return max(total)
print (solution(numbers,k))


