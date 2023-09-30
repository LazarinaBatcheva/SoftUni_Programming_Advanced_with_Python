def is_valid_index(r, c):
    return 0 <= r < size_matrix and 0 <= c < size_matrix


presents_count = int(input())
size_matrix = int(input())

matrix = []
santa_pos = []
nice_kids_left = 0

for row in range(size_matrix):
    matrix.append(list(input().split()))
    for col in range(size_matrix):
        if matrix[row][col] == "S":
            santa_pos = [row, col]
            matrix[row][col] = "-"
        elif matrix[row][col] == "V":
            nice_kids_left += 1

move_directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
happy_nice_kids = 0

while True:
    command = input()
    if command == "Christmas morning":
        matrix[santa_pos[0]][santa_pos[1]] = "S"
        break

    new_row = santa_pos[0] + move_directions[command][0]
    new_col = santa_pos[1] + move_directions[command][1]

    if is_valid_index(new_row, new_col):
        santa_pos = [new_row, new_col]

        if matrix[new_row][new_col] == "V":
            presents_count -= 1
            nice_kids_left -= 1
            happy_nice_kids += 1

        elif matrix[new_row][new_col] == "C":
            for course, move in move_directions.items():
                next_row = santa_pos[0] + move[0]
                next_col = santa_pos[1] + move[1]
                if is_valid_index(next_row, next_col) and matrix[next_row][next_col] in ["V", "X"]:
                    presents_count -= 1
                    if presents_count < 0:
                        break
                    if matrix[next_row][next_col] == "V":
                        nice_kids_left -= 1
                        happy_nice_kids += 1
                    matrix[next_row][next_col] = "-"

        matrix[new_row][new_col] = "-"

    if presents_count == 0:
        break

matrix[santa_pos[0]][santa_pos[1]] = "S"
if presents_count == 0 and nice_kids_left > 0:
    print("Santa ran out of presents!")

[print(*row) for row in matrix]

if nice_kids_left == 0:
    print(f"Good job, Santa! {happy_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_left} nice kid/s.")