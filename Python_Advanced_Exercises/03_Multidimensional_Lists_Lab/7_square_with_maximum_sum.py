rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

max_sum = float("-inf")
max_sum_indexes = None

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        first_num = matrix[row_index][col_index]
        right_num = matrix[row_index][col_index + 1]
        down_num = matrix[row_index + 1][col_index]
        down_right_num = matrix[row_index + 1][col_index + 1]
        current_sum = first_num + right_num + down_num + down_right_num

        if max_sum < current_sum:
            max_sum = current_sum
            max_sum_indexes = [[first_num, right_num], [down_num, down_right_num]]

print(*max_sum_indexes[0])
print(*max_sum_indexes[1])
print(max_sum)
