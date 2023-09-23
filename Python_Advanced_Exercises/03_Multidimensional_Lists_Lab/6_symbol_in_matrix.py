rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([x for x in input()])

symbol = input()

for row_index in range(rows):
    for col_index in range(len(matrix[row_index])):
        current_symbol = matrix[row_index][col_index]
        if current_symbol == symbol:
            print((row_index, col_index))
            exit()

print(f"{symbol} does not occur in the matrix")