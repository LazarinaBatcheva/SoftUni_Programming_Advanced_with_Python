rows, cols = [int(x) for x in input().split(", ")]

matrix = []
sum_numbers = 0

for row in range(rows):
    numbers = [int(x) for x in input().split(", ")]
    sum_numbers += sum(numbers)
    matrix.append(numbers)

print(sum_numbers)
print(matrix)