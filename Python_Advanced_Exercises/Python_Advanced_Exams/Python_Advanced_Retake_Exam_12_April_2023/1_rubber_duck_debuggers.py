from collections import deque


DUCKY_RANGES = {
    "Darth Vader Ducky": range(0, 61),
    "Thor Ducky": range(61, 121),
    "Big Blue Rubber Ducky": range(121, 181),
    "Small Yellow Rubber Ducky": range(181, 241)
}


programmer_time = deque((int(x) for x in input().split()))
tasks_count = [int(x) for x in input().split()]

rubber_ducks = {
    'Darth Vader Ducky': 0,
    'Thor Ducky': 0,
    'Big Blue Rubber Ducky': 0,
    'Small Yellow Rubber Ducky': 0,
}

while programmer_time and tasks_count:
    current_programmer_time = programmer_time.popleft()
    current_task = tasks_count.pop()

    total_time_for_task = current_programmer_time * current_task

    # check if total task`s time in ducky`s ranges
    for ducky_name, ducky_range in DUCKY_RANGES.items():
        if total_time_for_task in ducky_range:
            rubber_ducks[ducky_name] += 1
            break
    else:
        tasks_count.append(current_task - 2)
        programmer_time.append(current_programmer_time)

print('Congratulations, all tasks have been completed! Rubber ducks rewarded:')
for name, count in rubber_ducks.items():
    print(f'{name}: {count}')