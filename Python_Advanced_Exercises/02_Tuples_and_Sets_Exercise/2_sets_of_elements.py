first_num, second_num = input().split()

a = set()
b = set()

for _ in range(int(first_num)):
    current_number = int(input())
    a.add(current_number)

for _ in range(int(second_num)):
    current_num = int(input())
    b.add(current_num)

repeat_nums = a & b     # repeat_nums = a.intersection(b)

if repeat_nums:
    for number in repeat_nums:
        print(number)