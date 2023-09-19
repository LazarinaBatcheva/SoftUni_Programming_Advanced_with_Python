number_of_lines = int(input())

elements = []

for _ in range(number_of_lines):
    elements += [el for el in input().split()]

elements = set(elements)

for element in elements:
    print(element)