# Q3 — Longest Consecutive Increasing Run
#
# You are given a list of integers.
#
# Return the length of the longest consecutive increasing run.
#
# A consecutive increasing run means:
#
# numbers[i] + 1 == numbers[i+1]
# Example 1
numbers = [10, 11, 12, 13, 50, 51, 52]
#
# Output:
#
# 3
#
# because:
#
# 1,2,3
#
# is a run of length 3.
#
# and:
#
# 7,8
#
# is a run of length 2.
def solution(numbers):
    count = 1 # because the lowest count of 1 number is 1 basically 
    sequences = [] # we will add here later the results of the count of each continuous loop.
    for i in range(len(numbers)-1):
        if numbers[i] + 1 == numbers[i+1]:
            count += 1
        else:
            sequences.append(count)
            count = 1 # need this to always start the count when we loop again to 1
    sequences.append(count)
    return max(sequences)

print(solution(numbers))

