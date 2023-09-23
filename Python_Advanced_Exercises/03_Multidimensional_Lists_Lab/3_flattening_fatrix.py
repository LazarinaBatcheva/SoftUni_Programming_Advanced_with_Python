rows = int(input())

matrix = []

for row_index in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

flattening_matrix = [el for row in matrix for el in row]

print(flattening_matrix)