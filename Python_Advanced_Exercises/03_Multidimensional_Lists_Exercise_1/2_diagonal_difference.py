rows = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(rows)]

primary_diagonal_sum = [matrix[row][row] for row in range(rows)]
secondary_diagonal_sum = [matrix[row][rows - row - 1] for row in range(rows)]
difference = abs(sum(primary_diagonal_sum) - sum(secondary_diagonal_sum))

print(difference)