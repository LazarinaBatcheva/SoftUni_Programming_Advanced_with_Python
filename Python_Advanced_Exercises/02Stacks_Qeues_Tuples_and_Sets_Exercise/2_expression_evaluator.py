from collections import deque

string_expression = input().split()

operators = "*+-/"
numbers = deque()

for element in string_expression:
    if element in operators:
        while len(numbers) > 1:
            first_number = numbers.popleft()
            second_number = numbers.popleft()

            result = 0

            if element == "*":
                result += first_number * second_number
            elif element == "+":
                result += first_number + second_number
            elif element == "/":
                result += first_number // second_number
            elif element == "-":
                result += first_number - second_number

            numbers.appendleft(result)

    else:
        numbers.append(int(element))

print(numbers.pop())