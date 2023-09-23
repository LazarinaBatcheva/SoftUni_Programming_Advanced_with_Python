first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())
number_of_lines = int(input())

for _ in range(number_of_lines):
    command, first_second, *nums = input().split()
    numbers = [int(x) for x in nums]

    if command == "Add":
        if first_second == "First":
            first_sequence.update(numbers)
            
        else:
            second_sequence.update(numbers)

    elif command == "Remove":
        if first_second == "First":
            first_sequence.difference_update(numbers)
            
        else:
            for number in numbers:
                second_sequence.difference_update(numbers)

    elif command == "Check":
        print(first_sequence.issuperset(second_sequence))

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")
