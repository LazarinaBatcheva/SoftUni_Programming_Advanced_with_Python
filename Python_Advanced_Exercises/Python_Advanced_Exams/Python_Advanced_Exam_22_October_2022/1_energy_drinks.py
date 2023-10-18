from collections import deque

MAX_CAFFEINE = 300
CAFFEINE_TO_DECREASE = 30

milligrams_of_caffeine = [int(x) for x in input().split(', ')]
energy_drinks = deque(int(x) for x in input().split(', '))

consumed_caffeine = 0

while milligrams_of_caffeine and energy_drinks:
    current_caffeine = milligrams_of_caffeine.pop()
    current_energy_drink = energy_drinks.popleft()
    total_caffeine = current_caffeine * current_energy_drink

    if consumed_caffeine + total_caffeine <= MAX_CAFFEINE:
        consumed_caffeine += total_caffeine

    else:
        if consumed_caffeine >= CAFFEINE_TO_DECREASE = 30:
            consumed_caffeine -= CAFFEINE_TO_DECREASE = 30
        energy_drinks.append(current_energy_drink)

if energy_drinks:
    print(f'Drinks left: {", ".join(map(str, energy_drinks))}')
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f'Stamat is going to sleep with {consumed_caffeine} mg caffeine.')
