from collections import deque

# possible characters in the field
SQUIRREL = 's'
HAZELNUT = 'h'
EMPTY = '*'
TRAP = 't'


DIRECTIONS_MAPPER = {
    'left': (0, -1),
    'right': (0, 1),
    'down': (1, 0),
    'up': (-1, 0)
}

# size of square shape matrix
SIZE_FIELD = int(input())

MAX_HAZELNUT_COUNT = 3


def is_in_area(row, col):
    return 0 <= row < SIZE_FIELD and 0 <= col < SIZE_FIELD


directions = deque(el for el in input().split(', '))

matrix = []
squirrel_pos = None
hazelnut_count = 0

# filling the matrix
for row_index in range(SIZE_FIELD):
    row_data = list(input())
    matrix.append(row_data)
    if SQUIRREL in row_data:
        squirrel_pos = [row_index, row_data.index(SQUIRREL)]
        matrix[row_index][row_data.index(SQUIRREL)] = EMPTY

while directions:
    current_direction = directions.popleft()
    current_row, current_col = squirrel_pos
    row_to_go, col_to_go = DIRECTIONS_MAPPER[current_direction]
    desired_row = current_row + row_to_go
    desired_col = current_col + col_to_go

    # checking if squirrel goes out of the field
    if not is_in_area(desired_row, desired_col):
        print('The squirrel is out of the field.')
        print(f'Hazelnuts collected: {hazelnut_count}')
        exit()

    elif matrix[desired_row][desired_col] == TRAP:
        print('Unfortunately, the squirrel stepped on a trap...')
        print(f'Hazelnuts collected: {hazelnut_count}')
        exit()

    elif matrix[desired_row][desired_col] == HAZELNUT:
        hazelnut_count += 1
        matrix[desired_row][desired_col] = EMPTY
        squirrel_pos = [desired_row, desired_col]

        if hazelnut_count == MAX_HAZELNUT_COUNT:
            print('Good job! You have collected all hazelnuts!')
            print(f'Hazelnuts collected: {hazelnut_count}')
            exit()

    # if squirrel steps on empty position
    else:
        squirrel_pos = [desired_row, desired_col]


# if no more directions and squirrel has`n enough hazelnuts
print('There are more hazelnuts to collect.')
print(f'Hazelnuts collected: {hazelnut_count}')
