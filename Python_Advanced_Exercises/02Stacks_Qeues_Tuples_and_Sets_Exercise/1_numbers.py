first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())
number_of_lines = int(input())

for _ in range(number_of_lines):
    command, first_second, *nums = input().split()
    numbers = [int(x) for x in nums]

    if command == "Add":
        if first_second == "First":
            for number in numbers:
                first_sequence.add(number)
        else:
            for number in numbers:
                second_sequence.add(number)

    elif command == "Remove":
        if first_second == "First":
            for number in numbers:
                if number in first_sequence:
                    first_sequence.remove(number)
        else:
            for number in numbers:
                if number in second_sequence:
                    second_sequence.remove(number)

    elif command == "Check":
        print(first_sequence.issuperset(second_sequence))

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")