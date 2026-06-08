# Question 3: Matrix Maximum Row

# You are given a rectangular matrix of integers matrix.

# Your task is to find the row whose elements have the greatest sum.

# Return the index of that row.

# If multiple rows have the same maximum sum, return the smallest such index.

# Example matrix = [
#               [1,2,3],
#               [4,0,1],
#               [2,2,2]
# ]

# the solution(matrix) should be = 0 (index 0)

matrix = [
        [1,2,3],
        [4,0,1],
        [2,2,2]
]

row_sums = [sum(row) for row in matrix]

print (row_sums)
