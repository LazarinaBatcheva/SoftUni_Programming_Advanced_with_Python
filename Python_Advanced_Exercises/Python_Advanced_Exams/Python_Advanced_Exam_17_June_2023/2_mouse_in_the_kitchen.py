ROWS_COUNT, COLS_COUNT = [int(x) for x in input().split(',')]

MOUSE = 'M'
CHEESE = 'C'
EMPTY = '*'
WALL = '@'
TRAP = 'T'

DIRECTIONS_MAPPER = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}


def is_in_area(desired_row_, desired_col_):
    return 0 <= desired_row_ < ROWS_COUNT and 0 <= desired_col_ < COLS_COUNT


matrix = []
mouse_pos = None
total_cheese_count = 0

for row_index in range(ROWS_COUNT):
    row_data = list(input())
    if MOUSE in row_data:
        mouse_pos = [row_index, row_data.index(MOUSE)]
    total_cheese_count += row_data.count(CHEESE)
    matrix.append(row_data)

direction = input()

while direction != 'danger':
    current_mouse_pos_row, current_mouse_pos_col = mouse_pos
    desired_row = current_mouse_pos_row + DIRECTIONS_MAPPER[direction][0]
    desired_col = current_mouse_pos_col + DIRECTIONS_MAPPER[direction][1]

    if not is_in_area(desired_row, desired_col):
        print('No more cheese for tonight!')
        break

    elif matrix[desired_row][desired_col] == CHEESE:
        matrix[desired_row][desired_col] = MOUSE
        matrix[current_mouse_pos_row][current_mouse_pos_col] = EMPTY
        total_cheese_count -= 1
        mouse_pos = [desired_row, desired_col]

        if total_cheese_count == 0:
            print('Happy mouse! All the cheese is eaten, good night!')
            break

    elif matrix[desired_row][desired_col] == TRAP:
        matrix[desired_row][desired_col] = MOUSE
        matrix[current_mouse_pos_row][current_mouse_pos_col] = EMPTY
        print('Mouse is trapped!')
        break

    elif matrix[desired_row][desired_col] == WALL:
        direction = input()
        continue

    mouse_pos = [desired_row, desired_col]
    matrix[desired_row][desired_col] = MOUSE
    matrix[current_mouse_pos_row][current_mouse_pos_col] = EMPTY

    direction = input()

if direction == 'danger':
    print('Mouse will come back later!')

[print(*row, sep='') for row in matrix]
