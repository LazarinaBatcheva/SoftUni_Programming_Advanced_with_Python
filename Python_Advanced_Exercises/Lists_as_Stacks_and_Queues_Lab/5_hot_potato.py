from collections import deque

children_names = deque(input().split())
number = int(input()) - 1

while len(children_names) > 1:
    children_names.rotate(-number)
    print(f"Removed {children_names.popleft()}")

print(f"Last is {children_names.pop()}")