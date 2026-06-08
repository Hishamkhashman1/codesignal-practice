matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
]

def solution_secondary_diag_sum(matrix):
    rev_matrix = []
    diag_num = []
    for row in matrix:
        rev_matrix.append(row[::-1])
        print (rev_matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
                       if i == j:
                           diag_num.append(matrix[i][j])
    return sum(diag_num)

print (solution_secondary_diag_sum(matrix))

