size = int(input())

matrix = []
bunny_pos = []

for row in range(size):
    matrix.append(list(input().split()))
    for col in range(size):
        if matrix[row][col] == "B":
            bunny_pos = [row, col]

directions = {"up": (-1, 0), "down": (1, 0), "right": (0, 1), "left": (0, -1)}
max_eggs = float("-inf")
best_direction = ""
max_eggs_pos = []

for direction, move in directions.items():
    eggs = 0
    eggs_pos = []
    new_row = bunny_pos[0] + move[0]
    new_col = bunny_pos[1] + move[1]

    while 0 <= new_row < size and 0 <= new_col < size:
        if matrix[new_row][new_col] == "X":
            break
        eggs += int(matrix[new_row][new_col])
        eggs_pos.append([new_row, new_col])
        new_row += move[0]
        new_col += move[1]

    if eggs > max_eggs and eggs_pos:
        max_eggs = eggs
        best_direction = direction
        max_eggs_pos = eggs_pos

print(best_direction)
[print(row) for row in max_eggs_pos]
print(max_eggs)
