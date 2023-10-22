from collections import deque

MATRIX_SIZE = 6

# possible characters in the matrix
ROVER = 'E'             # it will be only one
WATER_DEPOSIT = 'W'     # one or more
METAL_DEPOSIT = 'M'     # one or more
CONCRETE_DEPOSIT = 'C'  # one or more
ROCK = 'R'              # one or more
EMPTY_POS = '-'

WATER = 'Water'
METAL = 'Metal'
CONCRETE = 'Concrete'

DIRECTIONS_MAPPER = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


def filling_area_and_finding_rover_position(size):
    matrix, rover_start_pos = [], None
    for row_index in range(size):
        row_data = list(input().split())
        if ROVER in row_data:
            rover_start_pos = row_index, row_data.index(ROVER)
        matrix.append(row_data)

    return matrix, rover_start_pos


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


area, rover_pos = filling_area_and_finding_rover_position(MATRIX_SIZE)

directions = deque(input().split(', '))

water_deposit_count, metal_deposit_count, concrete_deposit_count = 0, 0, 0

while directions:
    direction = directions.popleft()
    current_row, current_col = rover_pos
    row_to_go = current_row + DIRECTIONS_MAPPER[direction][0]
    col_to_go = current_col + DIRECTIONS_MAPPER[direction][1]

    next_row, next_col = finding_next_position(MATRIX_SIZE, row_to_go, col_to_go)

    if area[next_row][next_col] == EMPTY_POS:
        rover_pos = next_row, next_col
        continue

    if area[next_row][next_col] == ROCK:
        print(f'Rover got broken at ({next_row}, {next_col})')
        break

    elif area[next_row][next_col] == WATER_DEPOSIT:
        print(f'{WATER} deposit found at ({next_row}, {next_col})')
        water_deposit_count += 1

    elif area[next_row][next_col] == METAL_DEPOSIT:
        print(f'{METAL} deposit found at ({next_row}, {next_col})')
        metal_deposit_count += 1

    elif area[next_row][next_col] == CONCRETE_DEPOSIT:
        print(f'{CONCRETE} deposit found at ({next_row}, {next_col})')
        concrete_deposit_count += 1

    rover_pos = next_row, next_col

if water_deposit_count and metal_deposit_count and concrete_deposit_count:
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')