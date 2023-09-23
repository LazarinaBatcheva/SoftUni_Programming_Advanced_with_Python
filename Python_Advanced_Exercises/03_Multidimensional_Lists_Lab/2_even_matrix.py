rows = int(input())

matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

even_numbers = [[x for x in row if x % 2 == 0] for row in matrix]

print(even_numbers)