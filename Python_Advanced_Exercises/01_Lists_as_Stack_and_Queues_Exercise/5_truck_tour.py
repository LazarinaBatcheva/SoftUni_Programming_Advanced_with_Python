from collections import deque

number_of_lines = int(input())
petrol_pumps = deque()
start_position = 0
stops = 0

for _ in range(number_of_lines):
    info = input().split()
    petrol, kilometers = int(info[0]), int(info[1])
    petrol_pumps.append([petrol, kilometers])

while stops < number_of_lines:
    fuel = 0
    for index in range(number_of_lines):
        fuel += petrol_pumps[index][0]
        distance = petrol_pumps[index][1]
        if fuel < distance:
            petrol_pumps.rotate(-1)
            start_position += 1
            stops = 0
            break
        fuel -= distance
        stops += 1

print(start_position)