n = int(input())
stack = []

for _ in range(n):
    command = input().split()
    action = command[0]
    if action == "1":
        number = int(command[1])
        stack.append(number)
    else:
        if len(stack) > 0:
            if action == "2":
                stack.pop()
            elif action == "3":
                print(max(stack))
            else:
                print(min(stack))

while len(stack) > 1:
    print(stack.pop(), end=", ")
print(stack.pop())