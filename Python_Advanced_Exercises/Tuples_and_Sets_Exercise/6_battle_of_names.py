number_of_lines = int(input())

odd_set = set()
even_set = set()

for number in range(1, number_of_lines + 1):
    name_sum = sum(ord(ch) for ch in (input())) // number

    if name_sum % 2 == 0:
        even_set.add(name_sum)
    else:
        odd_set.add(name_sum)

if sum(odd_set) > sum(even_set):
    result = odd_set - even_set     # odd_set.difference(even_set)

elif sum(odd_set) < sum(even_set):
    result = odd_set ^ even_set     # odd_set.symmetric_difference(even_set)

else:
    result = odd_set | even_set     # odd_set.union(even_set)

print(*result, sep=", ")