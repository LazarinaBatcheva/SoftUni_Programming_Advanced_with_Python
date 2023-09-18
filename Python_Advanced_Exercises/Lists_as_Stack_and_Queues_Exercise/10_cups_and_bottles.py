from collections import deque

cups = deque(int(x) for x in input().split())
bottles = list(int(x) for x in input().split())

wasted_water = 0

while cups and bottles:
    current_bottle = bottles.pop()
    if cups[0] <= current_bottle:
        wasted_water += (current_bottle - cups.popleft())
    else:
        cups[0] -= current_bottle

if not cups:
    print(f"Bottles: {' '.join(map(str, bottles))}")
else:
    print(f"Cups: {' '.join(map(str, cups))}")

print(f"Wasted litters of water: {wasted_water}")