def is_valid_index(r, c):
    return 0 <= r < size_matrix and 0 <= c < size_matrix


size_matrix = 5
matrix = []
player_pos = []
targets_left = 0

for row in range(size_matrix):
    matrix.append(list(input().split()))
    for col in range(size_matrix):
        if matrix[row][col] == "A":
            player_pos = [row, col]
            matrix[row][col] = "."
        elif matrix[row][col] == "x":
            targets_left += 1

num_of_commands = int(input())

targets_pos = []
move_directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

for _ in range(num_of_commands):
    command = input().split()

    current_command = command[0]
    direction = command[1]
    new_row = player_pos[0] + move_directions[direction][0]
    new_col = player_pos[1] + move_directions[direction][1]

    if current_command == "move":
        new_row = player_pos[0] + move_directions[direction][0] * int(command[2])
        new_col = player_pos[1] + move_directions[direction][1] * int(command[2])
        if is_valid_index(new_row, new_col) and matrix[new_row][new_col] == ".":
            player_pos = [new_row, new_col]

    elif current_command == "shoot":
        while is_valid_index(new_row, new_col):
            if matrix[new_row][new_col] == "x":
                matrix[new_row][new_col] = "."
                targets_left -= 1
                targets_pos.append([new_row, new_col])
                break
            new_row += move_directions[direction][0]
            new_col += move_directions[direction][1]

        if targets_left == 0:
            print(f"Training completed! All {len(targets_pos)} targets hit.")
            break

if targets_left > 0:
    print(f"Training not completed! {targets_left} targets left.")
[print(row) for row in targets_pos]
