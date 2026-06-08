# Matrix Exercise 5: Main Diagonal Sum
#
# You are given a square matrix.
#
# Return the sum of the main diagonal.
#
# The main diagonal consists of:
#
# matrix[0][0]
# matrix[1][1]
# matrix[2][2]
# ...
# Example
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# print (matrix[0][0])
# print (len(matrix))
# print (len(matrix[0]))
#
# Output:
#
# 15
#
# because:
#
# 1 + 5 + 9 = 15
# count = 0
# for row in matrix:
#     for item in row:
#         count += 1
# if count / len(matrix) == len(matrix):
#     print ("square matrix, OK")
#     x = len(matrix)
#     y = len(matrix)
#     diag_nums = []
#     for row in matrix:
#         for item in row:
#             if row[0]:
#                 diag_num.append(row[0][0])
#
#
# else:
#     print ("not square matrix, sorry")

def solution_main_diag_sum(matrix):
    diag_nums = []
    for i in range(len(matrix)):
            for j in range(len(matrix[i])):
    # when row[index] in matrix == column[index] in row
                if i == j:
    # append row[index] in daig_nums[]
                    diag_nums.append(matrix[i][j])
    return sum(diag_nums)
    # return sum diag_nums
print (solution_main_diag_sum(matrix))
