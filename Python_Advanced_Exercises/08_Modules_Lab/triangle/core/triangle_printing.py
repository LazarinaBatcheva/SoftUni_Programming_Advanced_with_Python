def print_nums(i):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()


def print_upper_part(size):
    for i in range(1, size + 1):
        print_nums(i)


def print_down_part(size):
    for i in range(size - 1, 0, -1):
        print_nums(i)


def print_triangle(size):
    print_upper_part(size)
    print_down_part(size)
