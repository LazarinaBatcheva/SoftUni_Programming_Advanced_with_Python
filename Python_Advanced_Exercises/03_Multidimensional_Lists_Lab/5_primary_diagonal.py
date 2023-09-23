rows = int(input())

matrix = []

for _ in range(rows):
    numbers = [int(x) for x in input().split()]
    matrix.append(numbers)

sum_diagonal = 0

for row_index in range(rows):
    sum_diagonal += matrix[row_index][row_index]

print(sum_diagonal)