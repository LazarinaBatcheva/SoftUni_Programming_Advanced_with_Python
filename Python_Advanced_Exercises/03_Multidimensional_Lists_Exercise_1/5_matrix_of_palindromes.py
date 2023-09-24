rows, cols = [int(x) for x in input().split()]

first_letter = ord("a")

for row_index in range(rows):
    for col_index in range(cols):
        print(f"{chr(first_letter + row_index)}{chr(first_letter + row_index + col_index)}"
              f"{chr(first_letter + row_index)}", end=" ")
    print()