# possible characters in the playground
SUBMARINE = 'S'
CRUISER = 'C'
MINE = '*'
EMPTY = '-'

DIRECTIONS_MAPPER = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

SIZE_OF_THE_BATTLEFIELD = int(input())

MAX_MINES_HITS = 2
CRUISER_COUNT = 3

battlefield = []
submarine_pos = None
mines_hits = 0
destroyed_cruisers = 0

# creating a square shape matrix and finding submarine`s position
for row_index in range(SIZE_OF_THE_BATTLEFIELD):
    row_data = list(input())
    if SUBMARINE in row_data:
        submarine_pos = [row_index, row_data.index(SUBMARINE)]
    battlefield.append(row_data)


while True:
    direction = input()

    current_row, current_col = submarine_pos
    row_to_go, col_to_go = DIRECTIONS_MAPPER[direction]
    desired_row = current_row + row_to_go
    desired_col = current_col + col_to_go

    if battlefield[desired_row][desired_col] == MINE:
        mines_hits += 1
        battlefield[desired_row][desired_col] = SUBMARINE
        battlefield[current_row][current_col] = EMPTY
        submarine_pos = [desired_row, desired_col]

        if mines_hits > MAX_MINES_HITS:
            print(f'Mission failed, U-9 disappeared! Last known coordinates {submarine_pos}!')
            break

    elif battlefield[desired_row][desired_col] == CRUISER:
        destroyed_cruisers += 1
        battlefield[desired_row][desired_col] = SUBMARINE
        battlefield[current_row][current_col] = EMPTY
        submarine_pos = [desired_row, desired_col]

        if destroyed_cruisers == CRUISER_COUNT:
            print('Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
            break

    elif battlefield[desired_row][desired_col] == EMPTY:
        battlefield[desired_row][desired_col] = SUBMARINE
        battlefield[current_row][current_col] = EMPTY
        submarine_pos = [desired_row, desired_col]

[print(*row, sep='') for row in battlefield]