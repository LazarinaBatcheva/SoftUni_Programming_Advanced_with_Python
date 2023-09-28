def is_valid_index(row, col):
    return 0 <= row < rows and 0 <= col < cols


rows, cols = [int(x) for x in input().split()]

matrix = []
player_row, player_col = 0, 0
bunnies = []

for row_index in range(rows):
    matrix.append(list(input()))
    for col_index in range(cols):
        if matrix[row_index][col_index] == "P":
            player_row, player_col = row_index, col_index
        elif matrix[row_index][col_index] == "B":
            bunnies.append([row_index, col_index])

commands = input()

directions = {
    "L": (0, -1),
    "R": (0, +1),
    "U": (-1, 0),
    "D": (+1, 0)
}
winner = False
dead = False
matrix[player_row][player_col] = "."

for command in commands:
    player_move_row = player_row + directions[command][0]
    player_move_col = player_col + directions[command][1]

    if not is_valid_index(player_move_row, player_move_col):
        winner = True
    else:
        if matrix[player_row][player_col] == "B":
            dead = True
        else:
            player_row, player_col = player_move_row, player_move_col

    new_bunnies = []
    for bunny_row, bunny_col in bunnies:
        matrix[bunny_row][bunny_col] = "B"
        for move in directions.values():
            new_bunny_row = bunny_row + move[0]
            new_bunny_col = bunny_col + move[1]
            if is_valid_index(new_bunny_row, new_bunny_col):
                new_bunnies.append([new_bunny_row, new_bunny_col])
                if new_bunny_row == player_row and new_bunny_col == player_col:
                    dead = True
    for new_bunny in new_bunnies:
        matrix[new_bunny[0]][new_bunny[1]] = "B"
    bunnies.extend(new_bunnies)

    if winner or dead:
        break

[print(*row, sep="") for row in matrix]
if winner:
    print(f"won: {player_row} {player_col}")
else:
    print(f"dead: {player_row} {player_col}")