def minimum(array):
    min_row = 0
    min_col = 0
    row_sum = 0
    col_sum = 0
    min_row_sum = sum(array[0])
    row_n = 0
    for col in array:
        row_sum = sum(col)
        if row_sum < min_row_sum:
            min_row_sum = row_sum
            min_row = row_n
        row_n += 1
        row_sum = 0
    col_n = 1
    i = 1
    min_col_sum = array[0][0] + array[0][1] + array[0][2]
    while col_n < len(array):
        while i < len(array):
            col_sum += array[i][col_n]
            i += 1
            if col_sum < min_col_sum:
                min_col_sum = col_sum
                min_col = col_n
        col_sum = 0
        i = 0
        col_n += 1

    return min_col + 1, min_row + 1


print(minimum([[7, 2, 7, 2, 0], [2, 9, 4, 1, 7], [3, 8, 6, 2, 4], [2, 5, 2, 9, 1], [6, 6, 5, 4, 5]]))
