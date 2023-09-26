from collections import deque


def is_inside(matrix_, row, col):
    return 0 <= row < len(matrix_) and 0 <= col < len(matrix_[row])


rows = int(input())

matrix = [[int(x) for x in input().split()]for _ in range(rows)]

bombs_coordinates = deque([int(x) for x in coordinates.split(",")] for coordinates in input().split())
explosion_direction = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

while bombs_coordinates:
    current_bomb = bombs_coordinates.popleft()
    bomb_row_index, bomb_col_index = current_bomb
    bomb_value = matrix[bomb_row_index][bomb_col_index]

    if bomb_value <= 0:
        continue

    for dir_row, dir_col in explosion_direction:
        next_row, next_col = bomb_row_index + dir_row, bomb_col_index + dir_col
        if is_inside(matrix, next_row, next_col) and matrix[next_row][next_col] > 0:
            matrix[next_row][next_col] -= bomb_value

    matrix[bomb_row_index][bomb_col_index] = 0

alive_cells = 0
alive_cells_sum = 0

for row_ in matrix:
    for value in row_:
        if value > 0:
            alive_cells += 1
            alive_cells_sum += value

print(f"Alive cells: {alive_cells}")
print(f"Sum: {alive_cells_sum}")
[print(*row) for row in matrix]
