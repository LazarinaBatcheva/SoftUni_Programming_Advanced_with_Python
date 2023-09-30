def is_valid_index(r, c):
    return 0 <= r < size_matrix and 0 <= c < size_matrix


size_matrix = int(input())

matrix = []
alice_pos = []

for row in range(size_matrix):
    matrix.append(list(input().split()))
    for col in range(size_matrix):
        if matrix[row][col] == "A":
            matrix[row][col] = "*"
            alice_pos = [row, col]

moves_direction = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
bags_of_tea = 0

while bags_of_tea < 10:
    command = input()
    move = moves_direction[command]
    new_row = alice_pos[0] + move[0]
    new_col = alice_pos[1] + move[1]

    if not is_valid_index(new_row, new_col):
        break
    elif matrix[new_row][new_col] == "R":
        matrix[new_row][new_col] = "*"
        break
    elif matrix[new_row][new_col] not in ".*":
        bags_of_tea += int(matrix[new_row][new_col])

    matrix[new_row][new_col] = "*"
    alice_pos = [new_row, new_col]

if bags_of_tea >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
[print(*row) for row in matrix]
