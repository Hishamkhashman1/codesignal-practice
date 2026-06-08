matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
]


def solution_border_sum(matrix):
    border_nums_rows = []
    border_nums_columns = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == 0 or i == len(matrix)-1:
                border_nums_rows.append(matrix[i][j])
            if j == 0 or j == len(matrix[i])-1:
                border_nums_columns.append(matrix[i][j])
    
    dup_nums_sum = matrix[0][0] + matrix[0][len(matrix[i])-1] + matrix[len(matrix)-1][0] + matrix[len(matrix)-1][len(matrix[i])-1]
    sum_borders = sum(border_nums_rows) + sum(border_nums_columns) - dup_nums_sum
    
    return sum_borders
print(solution_border_sum(matrix))
