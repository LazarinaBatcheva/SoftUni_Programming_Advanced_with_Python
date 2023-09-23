rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for row in range(rows):
    numbers = [int(x) for x in input().split()]
    matrix.append(numbers)

for col_index in range(cols):
    sum_cols = 0
    for row_index in range(rows):
        sum_cols += matrix[row_index][col_index]
    print(sum_cols)