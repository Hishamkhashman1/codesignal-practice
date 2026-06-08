matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

def solution_sum(matrix):
    matrix_sums = sum([sum(row) for row in matrix])
    return (matrix_sums)

def solution_even_count(matrix):
    count = 0
    joined_list = sum(matrix, [])
    for n in joined_list:
        if n % 2 == 0:
            count += 1
    return count

def solution_largest_value(matrix):
    all_matrix = sum(matrix, [])
    return max(all_matrix)

def solution_column_sum(matrix):
    sum_list = []
    for row in matrix:
        sum_list.append(row[0])
    return sum(sum_list)
