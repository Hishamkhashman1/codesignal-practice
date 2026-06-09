# Find the Largest Element Position

# You are given a matrix of integers.
#
# Return the coordinates of the largest element as:
#
# [row_index, column_index]
#
# If there are multiple largest elements, return the coordinates of the first one encountered when traversing:
#
# left to right
# top to bottom
# Example
matrix = [
    [1, 7, 3],
    [4, 5, 6],
    [2, 8, 1]
]
#
# Output:
#
# [2, 1]
#
# because:
#
# matrix[2][1] = 8
#
# and 8 is the largest value.
#
#
# loop through items in row and getting max
# 

def solution(matrix):
    transform_matrix = {(r,c): value for r, row in enumerate(matrix) for c, value in enumerate(row)}
    return max(transform_matrix, key=transform_matrix.get)
print (solution(matrix))
