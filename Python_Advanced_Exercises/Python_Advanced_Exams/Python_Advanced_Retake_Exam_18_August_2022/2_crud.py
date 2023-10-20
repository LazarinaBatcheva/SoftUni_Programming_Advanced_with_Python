MATRIX_SIZE = 6

EMPTY = '.'

DIRECTIONS_MAPPER = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

# Possible commands
CREATE = 'Create'
UPDATE = 'Update'
DELETE = 'Delete'
READ = 'Read'
STOP = 'Stop'


def filling_matrix(size):
    matrix_ = []
    for row_index in range(size):
        matrix_.append(list(input().split()))
        
    return matrix_


def create_value_on_position(matrix_, row, col, given_value):
    if matrix_[row][col] == EMPTY:
        matrix_[row][col] = given_value

    return matrix_


def update_value_on_position(matrix_, row, col, given_value):
    if matrix_[row][col] != EMPTY:
        matrix_[row][col] = given_value

    return matrix_


def delete_value_of_position(matrix_, row, col):
    if matrix_[row][col] != EMPTY:
        matrix_[row][col] = EMPTY

    return matrix_


def read_and_print_value_of_position(matrix_, row, col):
    if matrix_[row][col] != EMPTY:
        print(matrix_[row][col])


matrix = filling_matrix(MATRIX_SIZE)

start_row, start_col = [int(x) for x in input().strip('()').split(', ')]
command = input()

while command != STOP:
    current_command, direction, *values = command.split(', ')
    value = values[0] if values else None

    # the directions will always be within the scope of the matrix
    current_row = start_row + DIRECTIONS_MAPPER[direction][0]
    current_col = start_col + DIRECTIONS_MAPPER[direction][1]

    if current_command == CREATE:
        create_value_on_position(matrix, current_row, current_col, value)

    elif current_command == UPDATE:
        update_value_on_position(matrix, current_row, current_col, value)

    elif current_command == DELETE:
        delete_value_of_position(matrix, current_row, current_col)

    elif current_command == READ:
        read_and_print_value_of_position(matrix, current_row, current_col)

    start_row, start_col = current_row, current_col

    command = input()

[print(*row) for row in matrix]
