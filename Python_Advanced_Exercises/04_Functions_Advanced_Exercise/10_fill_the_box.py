def fill_the_box(height, length, width, *args):
    box_size = height * length * width
    no_box_space = 0
    for el in args:
        if el == "Finish":
            break
        elif el <= box_size:
            box_size -= el
        else:
            el -= box_size
            box_size = 0
            no_box_space += el
    if box_size > 0:
        result = f"There is free space in the box. You could put {box_size} more cubes."
    else:
        result = f"No more free space! You have {no_box_space} more cubes."
    return result


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print()
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print()
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
