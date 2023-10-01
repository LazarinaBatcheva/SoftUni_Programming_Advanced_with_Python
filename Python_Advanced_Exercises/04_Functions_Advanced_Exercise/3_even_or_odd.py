def even_odd(*args):
    even = []
    odd = []

    for number in args[:-1]:
        if int(number) % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    if args[-1] == "even":
        return even
    else:
        return odd


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print()
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))