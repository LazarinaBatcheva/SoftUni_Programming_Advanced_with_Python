from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

operators = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: abs(a - b),
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b
}

collected_nectar = deque()
total_honey = 0

while bees and nectar:
    if nectar[-1] >= bees[0]:
        collected_nectar.append(bees.popleft())
        collected_nectar.append(nectar.pop())
    else:
        nectar.pop()

while collected_nectar and symbols:
    current_bee = collected_nectar.popleft()
    current_nectar = collected_nectar.popleft()
    sym = symbols.popleft()

    if sym == "/" and current_nectar == 0:
        continue
    else:
        total_honey += operators[sym](current_bee, current_nectar)

print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")