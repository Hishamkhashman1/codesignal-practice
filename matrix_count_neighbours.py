matrix = [
    [1,1,1],
    [1,1,1],
    [1,1,0]
]

row_index = 2
col_index = 2
def count_neigbours_1(matrix, row_index, col_index):
    count = 0
    if 0<= row_index-1 < len(matrix) and matrix[(row_index-1)][col_index] == 1:
        count += 1
    if  row_index+1 < len(matrix) and matrix[(row_index+1)][col_index] == 1:
        count += 1
    if col_index+1 < len(matrix[0]) and matrix[row_index][col_index+1] == 1: 
        count += 1
    if 0<= col_index-1 < len(matrix[0]) and matrix[row_index][col_index-1] == 1:
        count += 1
    return count

print(count_neigbours_1(matrix, row_index,col_index))
