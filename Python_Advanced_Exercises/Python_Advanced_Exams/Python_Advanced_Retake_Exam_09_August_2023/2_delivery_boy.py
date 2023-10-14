DELIVERY_BOY = 'B'
PIZZA = 'P'
RESTAURANT = 'R'
DELIVERY_ADDRESS = 'A'
EMPTY = '-'
OBSTACLE = '*'
PATH = '.'

DIRECTIONS_MAPPER = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}

ROWS_COUNT, COLS_COUNT = map(int, input().split())


# Checking if the desired move is within the matrix
def is_in_area(row, col):
    return 0 <= row < ROWS_COUNT and 0 <= col < COLS_COUNT


neighborhood = []
delivery_boy_start_pos = None

# finding delivery boy start position
for row_index in range(ROWS_COUNT):
    row_data = list(input())
    if DELIVERY_BOY in row_data:
        delivery_boy_start_pos = [row_index, row_data.index(DELIVERY_BOY)]
    neighborhood.append(row_data)

delivery_boy_pos = delivery_boy_start_pos
is_finished = False

while not is_finished:
    direction = input()
    if direction not in DIRECTIONS_MAPPER:
        continue

    current_row, current_col = delivery_boy_pos
    row_to_go, col_to_go = DIRECTIONS_MAPPER[direction]
    desired_row = current_row + row_to_go
    desired_col = current_col + col_to_go

    if not is_in_area(desired_row, desired_col):  # if pizza is not delivered
        neighborhood[delivery_boy_start_pos[0]][delivery_boy_start_pos[1]] = ' '
        print('The delivery is late. Order is canceled.')
        is_finished = True

    elif neighborhood[desired_row][desired_col] == OBSTACLE:
        continue

    # finding restaurant and collecting pizza
    elif neighborhood[desired_row][desired_col] == PIZZA:
        neighborhood[desired_row][desired_col] = RESTAURANT
        print('Pizza is collected. 10 minutes for delivery.')

    # delivering pizza
    elif neighborhood[desired_row][desired_col] == DELIVERY_ADDRESS:
        neighborhood[desired_row][desired_col] = PIZZA
        print('Pizza is delivered on time! Next order...')
        is_finished = True

    # indicating delivery boy path
    if neighborhood[current_row][current_col] == EMPTY:
        neighborhood[current_row][current_col] = PATH

    delivery_boy_pos = [desired_row, desired_col]

# printing neighborhood
[print(*row, sep='') for row in neighborhood]