def is_valid_index(r, c, v):
    return 0 <= r < size_matrix and 0 <= c < size_matrix


size_matrix = int(input())
matrix = [[int(x) for x in input().split()]for _ in range(size_matrix)]

while True:
    command = input().split()
    if command[0] == "END":
        break

    row, col, value = int(command[1]), int(command[2]), int(command[3])

    if command[0] == "Add":
        if is_valid_index(row, col, value):
            matrix[row][col] += value
        else:
            print("Invalid coordinates")
    elif command[0] == "Subtract":
        if is_valid_index(row, col, value):
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")

[print(*row) for row in matrix]