def check_for_valid_coordinates(r1, c1, r2, c2, rows_num, cols_num):
    return 0 <= r1 <= rows_num and 0 <= c1 <= cols_num and 0 <= r2 <= rows_num and 0 <= c2 <= cols_num


rows, cols = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for _ in range(rows)]

while True:
    command = input()
    if command == "END":
        break

    current_command = command.split()

    if current_command[0] != "swap" or len(current_command) != 5:
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in current_command[1:]]

    if check_for_valid_coordinates(row1, row2, col1, col2, rows, cols):
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*row) for row in matrix]
    else:
        print("Invalid input!")
