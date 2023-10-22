MATRIX_SIZE = int(input())

NEEDED_FISH_QUANTITY = 20

# possible characters in fishing area
SHIP = 'S'
WHIRLPOOL = 'W'
EMPTY_POS = '-'

DIRECTIONS_MAPPER = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


def filling_matrix_and_finding_ship_position(size):
    matrix, ship_pos_row, ship_pos_col = [], None, None

    for row_index in range(size):
        row_data = list(input())
        matrix.append(row_data)
        if SHIP in row_data:
            ship_pos_row = row_index
            ship_pos_col = row_data.index(SHIP)
    matrix[ship_pos_row][ship_pos_col] = EMPTY_POS

    return matrix, ship_pos_row, ship_pos_col


def finding_next_position(size, desired_row, desired_col):
    if desired_row == size:
        desired_row = 0
    elif desired_row < 0:
        desired_row = size - 1
    elif desired_col == size:
        desired_col = 0
    elif desired_col < 0:
        desired_col = size - 1

    return desired_row, desired_col


fishing_area, ship_row, ship_col = filling_matrix_and_finding_ship_position(MATRIX_SIZE)

command = input()

collected_fish = 0
is_enough_fish = False

while command != 'collect the nets':
    row_to_go = ship_row + DIRECTIONS_MAPPER[command][0]
    col_to_go = ship_col + DIRECTIONS_MAPPER[command][1]

    next_row, next_col = finding_next_position(MATRIX_SIZE, row_to_go, col_to_go)

    if fishing_area[next_row][next_col].isdigit():
        collected_fish += int(fishing_area[next_row][next_col])
        fishing_area[next_row][next_col] = EMPTY_POS

        if collected_fish >= NEEDED_FISH_QUANTITY and not is_enough_fish:
            is_enough_fish = True

    elif fishing_area[next_row][next_col] == WHIRLPOOL:
        collected_fish = 0
        print(f'You fell into a whirlpool! The ship sank and you lost the fish you caught. '
              f'Last coordinates of the ship: [{next_row},{next_col}]')
        exit()

    ship_row, ship_col = next_row, next_col

    command = input()

fishing_area[ship_row][ship_col] = SHIP

if is_enough_fish:
    print('Success! You managed to reach the quota!')
else:
    print(f"You didn't catch enough fish and didn't reach the quota! "
          f"You need {NEEDED_FISH_QUANTITY - collected_fish} tons of fish more.")

if collected_fish:
    print(f'Amount of fish caught: {collected_fish} tons.')

[print(*row, sep='') for row in fishing_area]
