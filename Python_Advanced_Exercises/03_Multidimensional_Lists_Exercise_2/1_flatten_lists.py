matrix = [[int(x) for x in row.split()]for row in input().split("|")]
flatten_lst = [num for row in matrix[::-1] for num in row]

print(" ".join(str(num) for num in flatten_lst))
