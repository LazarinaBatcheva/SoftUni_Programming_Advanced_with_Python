rows, cols = [int(x) for x in input().split()]

matrix = [[int(el) for el in input().split()]for _ in range(rows)]

max_sum = float("-inf")
submatrix = None

for row_index in range(rows - 2):
    for col_index in range(cols - 2):
        current_sum = 0
        for row in range(row_index, row_index + 3):
            for col in range(col_index, col_index + 3):
                current_sum += matrix[row][col]
        if max_sum < current_sum:
            max_sum = current_sum
            submatrix = [matrix[row][col_index:col_index + 3] for row in range(row_index, row_index + 3)]

print(f"Sum = {max_sum}")
[print(*r) for r in submatrix]