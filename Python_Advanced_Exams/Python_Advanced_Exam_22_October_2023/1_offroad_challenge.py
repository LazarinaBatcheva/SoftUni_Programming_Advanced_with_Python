from collections import deque

initial_fuel = [int(x) for x in input().split()]
consumptions = deque(int(x) for x in input().split())
needed_quantities = deque(int(x) for x in input().split())

altitude = 0
altitudes_list = deque()

is_failed = False

while initial_fuel:
    current_fuel = initial_fuel.pop()
    current_consumption = consumptions.popleft()
    current_needed_quantity = needed_quantities.popleft()

    fuel_result = current_fuel - current_consumption

    if fuel_result >= current_needed_quantity:
        altitude += 1
        altitudes_list.append(altitude)
        print(f'John has reached: Altitude {altitude}')

    else:
        is_failed = True
        print(f'John did not reach: Altitude {altitude + 1}')
        break

if is_failed:
    print('John failed to reach the top.')

    if altitudes_list:
        print('Reached altitudes: ', end='')
        while altitudes_list:
            current_altitude = altitudes_list.popleft()
            end_char = ', ' if altitudes_list else ''
            print(f'Altitude {current_altitude}', end=end_char)

    else:
        print("John didn't reach any altitude.")

else:
    print('John has reached all the altitudes and managed to reach the top!')