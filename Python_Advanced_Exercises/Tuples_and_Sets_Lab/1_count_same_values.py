numbers = tuple(float(num) for num in input().split())

numbers_counter = {}

for number in numbers:
    numbers_counter[number] = numbers.count(number)

for key, value in numbers_counter.items():
    print(f"{key} - {value} times")