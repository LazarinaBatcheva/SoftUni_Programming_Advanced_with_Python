clothes_in_the_box = [int(num) for num in input().split()]
capacity_of_rack = int(input())

racks_counter = 0

while clothes_in_the_box:
    racks_counter += 1
    current_rack_capacity = capacity_of_rack
    while clothes_in_the_box and clothes_in_the_box[-1] <= current_rack_capacity:
        current_rack_capacity -= clothes_in_the_box.pop()

print(racks_counter)