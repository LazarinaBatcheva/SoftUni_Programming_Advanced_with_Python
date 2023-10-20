ROWS_COUNT, COLS_COUNT = [int(x) for x in input().split()]

# possible characters in the playground
PLAYER_POSITION = 'B'
OBSTACLE = 'O'
OPPONENT = 'P'
EMPTY = '-'

MAX_OPPONENTS = 3

DIRECTIONS_MAPPER = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}


# checking if desired move goes outside of playground
def is_in_area(row, col):
    return 0 <= row < ROWS_COUNT and 0 <= col < COLS_COUNT


playground = []
player_pos = None

for row_index in range(ROWS_COUNT):
    row_data = list(input().split())
    playground.append(row_data)
    if PLAYER_POSITION in row_data:
        player_pos = [row_index, row_data.index(PLAYER_POSITION)]
        playground[row_index][row_data.index(PLAYER_POSITION)] = EMPTY

command = input()

touched_opponents = 0
moves_count = 0

while command != "Finish":
    current_row, current_col = player_pos
    row_to_go, col_to_go = DIRECTIONS_MAPPER[command]
    desired_row = current_row + row_to_go
    desired_col = current_col + col_to_go

    if not is_in_area(desired_row, desired_col) or playground[desired_row][desired_col] == OBSTACLE:
        command = input()
        continue

    elif playground[desired_row][desired_col] == EMPTY:
        moves_count += 1
        player_pos = [desired_row, desired_col]

    elif playground[desired_row][desired_col] == OPPONENT:
        touched_opponents += 1
        moves_count += 1
        player_pos = [desired_row, desired_col]
        playground[current_row][current_col] = EMPTY

        if touched_opponents == MAX_OPPONENTS:
            break

    command = input()

print('Game over!')
print(f'Touched opponents: {touched_opponents} Moves made: {moves_count}')