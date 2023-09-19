from collections import deque

green_light_sec = int(input())
free_window = int(input())

total_cars = 0
cars = deque()
command = input()

while command != "END":
    if command != "green":
        cars.append(command)
    else:
        current_green_light = green_light_sec
        while current_green_light > 0 and cars:
            current_car = cars.popleft()
            time_to_cross = current_green_light + free_window

            if time_to_cross >= len(current_car):
                current_green_light -= len(current_car)
                total_cars += 1
            else:
                print(f"A crash happened!\n{current_car} was hit at {current_car[time_to_cross]}.")
                exit()  # raise SystemExit
    command = input()

print(f"Everyone is safe.\n{total_cars} total cars passed the crossroads.")
