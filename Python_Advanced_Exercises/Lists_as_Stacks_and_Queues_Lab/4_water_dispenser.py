from collections import deque

quantity_of_water = int(input())
name = input()

people_queue = deque()

while name != "Start":
    people_queue.append(name)
    name = input()

command = input()

while command != "End":
    current_command = command.split()
    if len(current_command) == 1:
        water_to_give = int(current_command[0])
        if water_to_give <= quantity_of_water:
            print(f"{people_queue.popleft()} got water")
            quantity_of_water -= water_to_give
        else:
            print(f"{people_queue.popleft()} must wait" )
    else:
        water_to_add = int(current_command[1])
        quantity_of_water += water_to_add
    command = input()

print(f"{quantity_of_water} liters left")