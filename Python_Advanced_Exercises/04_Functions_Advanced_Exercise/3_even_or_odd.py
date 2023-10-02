def even_odd(*args):
        if args[-1] == "even":
        return list(filter(lambda x: x % 2 == 0, args[:-1]))
    elif args[-1] == "odd":
        return list(filter(lambda x: x % 2 != 0, args[:-1]))

    # even = [int(x) for x in args[:-1] if int(x) % 2 == 0]
    # odd = [int(x) for x in args[:-1] if int(x) % 2 != 0]

    # if args[-1] == "even":
    #     return even
    # else:
    #     return odd


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print()
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
