from collections import deque

parentheses = deque(input())

opened_parentheses = "({["
closed_parentheses = ")}]"
counter = 0

while parentheses and counter < len(parentheses) / 2:
    if parentheses[0] in closed_parentheses:
        break
    index = opened_parentheses.index(parentheses[0])
    if parentheses[1] == closed_parentheses[index]:
        parentheses.popleft()
        parentheses.popleft()
        parentheses.rotate(counter)
        counter = 0
    else:
        parentheses.rotate(-1)
        counter += 1

if parentheses:
    print("NO")
else:
    print("YES")