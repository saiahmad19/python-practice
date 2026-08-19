def get_column(matrix, col_index):
    column = []
    for row in matrix:
        column.append(row[col_index])
    return column

def dot_product(v1, v2):
    total = 0
    for i in range(len(v1)):
        total = total + v1[i] * v2[i]
    return total

def matrix_multiply(a, b):
    if len(a[0]) != len(b):
        print("invalid")
        return

    result = []
    for row in a:
        new_row = []
        for col_index in range(len(b[0])):
            col = get_column(b, col_index)
            new_row.append(dot_product(row, col))
        result.append(new_row)
    return result

a = [[1, 2], [3, 4], [5, 6]]
b = [[1, 4], [6, 8]]

result = matrix_multiply(a, b)
print(result)