def is_valid_index(r, c, matrix_size):
    return 0 <= r < matrix_size and 0 <= c < matrix_size


size = int(input())
move_commands = input().split()

matrix = []
current_row, current_col = 0, 0
coal = 0
is_the_end = False

for row_index in range(size):
    matrix.append(list(input().split()))

    for col_index in range(size):
        if matrix[row_index][col_index] == "s":
            current_row, current_col = row_index, col_index

        elif matrix[row_index][col_index] == "c":
            coal += 1

for command in move_commands:
    if command == "left":
        if is_valid_index(current_row, current_col - 1, size):
            current_col -= 1
    elif command == "right":
        if is_valid_index(current_row, current_col + 1, size):
            current_col += 1
    elif command == "up":
        if is_valid_index(current_row - 1, current_col, size):
            current_row -= 1
    elif command == "down":
        if is_valid_index(current_row + 1, current_col, size):
            current_row += 1

    if matrix[current_row][current_col] == "e":
        print(f"Game over! ({current_row}, {current_col})")
        is_the_end = True
        break
    elif matrix[current_row][current_col] == "c":
        coal -= 1
        matrix[current_row][current_col] = "*"
        if coal == 0:
            print(f"You collected all coal! ({current_row}, {current_col})")
            is_the_end = True
            break

if not is_the_end:
    print(f"{coal} pieces of coal left. ({current_row}, {current_col})")