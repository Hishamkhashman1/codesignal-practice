# You are given a matrix of integers.
#
# Return its transpose.
#
# The transpose of a matrix is obtained by swapping rows and columns.
#
# Example
#
# For
#
matrix = [
    [1,2,3],
    [4,5,6]
]
#
# the output should be
#
# [
#     [1,4],
#     [2,5],
#     [3,6]
# ]

# matrix [r0][c0] and [r1][c1] diagonal stays the same. so whenever i == j then they keep their position of course DUH 0,0 is 0,0 and n, n is n, n

# everything else shifts. number 3 for example. has initial Matrix [0][2] and should become matrix [2][1]
#                         number 4 for example. has intitial matrix [1][0] and bshould become matrix [0][1]
#                         number 6 for example. has initial matrix [1][2] and should become matrix [2][1]
#                         number 2 for example. has initial matrix [0][1] and should become matrix [1][0]

# we just need to swap indices and append in new table
# 
def solution_transpose(matrix):
    transposed_matrix = [list(row) for row in zip(*matrix)]
    return transposed_matrix
print (solution_transpose(matrix))

def solution_transpose_manually(matrix):
    for j in range(len(matrix[0])):


