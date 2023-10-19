from collections import deque


seats = list(input().split(', '))
first_nums_sequence = deque(int(x) for x in input().split(', '))
second_nums_sequence = deque(int(x) for x in input().split(', '))

seats_matches = []
total_rotations_made = 0

while len(seats_matches) < 3 and total_rotations_made < 10:
    first_number = first_nums_sequence[0]
    second_number = second_nums_sequence[-1]
    sum_numbers = first_number + second_number
    sum_nums_ascii_chr = chr(sum_numbers)

    first_possible_seat = str(first_number) + sum_nums_ascii_chr
    second_possible_seat = str(second_number) + sum_nums_ascii_chr

    if first_possible_seat not in seats and second_possible_seat not in seats:
        first_nums_sequence.rotate(-1)
        second_nums_sequence.rotate(1)

    elif first_possible_seat in seats:
        if first_possible_seat not in seats_matches:
            seats_matches.append(first_possible_seat)
        first_nums_sequence.popleft()
        second_nums_sequence.pop()

    if second_possible_seat in seats:
        if second_possible_seat not in seats_matches:
            seats_matches.append(second_possible_seat)
        first_nums_sequence.popleft()
        second_nums_sequence.pop()

    total_rotations_made += 1

print(f'Seat matches: {", ".join(seats_matches)}')

print(f'Rotations count: {total_rotations_made}')