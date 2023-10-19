# possible characters in matrix
TUNNEL = 'T'
FINISH = 'F'
EMPTY = '.'
RACE_CAR = 'C'

# passed kilometers
EMPTY_POS_KM = 10
TUNNEL_POS_KM = 30

DIRECTIONS_MAPPER = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0),
}


# filling the matrix and finding start position and end position of tunel
def create_route_and_find_tunnel_entries(size):
    route, tunel = [], []
    for row_index in range(size):
        row_data = list(input().split())
        if TUNNEL in row_data:
            tunel.append([row_index, row_data.index(TUNNEL)])
        route.append(row_data)

    return route, tunel


matrix_size = int(input())
racing_num = input()

race_field, sides_of_tunel = create_route_and_find_tunnel_entries(matrix_size)

command = input()

total_km_passed = 0
car_row, car_col = 0, 0
is_finished = False

while command != 'End':

    # The directions will always lead to coordinates in the matrix.
    car_row = car_row + DIRECTIONS_MAPPER[command][0]
    car_col = car_col + DIRECTIONS_MAPPER[command][1]

    if race_field[car_row][car_col] == EMPTY:
        total_km_passed += EMPTY_POS_KM

    elif race_field[car_row][car_col] == FINISH:
        total_km_passed += EMPTY_POS_KM
        is_finished = True
        break

    elif race_field[car_row][car_col] == TUNNEL:
        sides_of_tunel.remove([car_row, car_col])
        race_field[car_row][car_col] = EMPTY
        car_row, car_col = sides_of_tunel[0]
        race_field[car_row][car_col] = EMPTY
        total_km_passed += TUNNEL_POS_KM

    command = input()

race_field[car_row][car_col] = RACE_CAR

if is_finished:
    print(f'Racing car {racing_num} finished the stage!')
else:
    print(f'Racing car {racing_num} DNF.')

print(f'Distance covered {total_km_passed} km.')
[print(*row, sep='') for row in race_field]
