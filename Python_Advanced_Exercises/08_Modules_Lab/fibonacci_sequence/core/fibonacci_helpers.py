def create_sequence(number):
    sequence = [0, 1]
    for _ in range(number - 2):
        current_num = sequence[-1]
        previous_num = sequence[-2]
        next_num = current_num + previous_num
        sequence.append(next_num)
    return sequence


def locate_num(number, sequence):
    try:
        return f'The number - {number} is at index {sequence.index(number)}'
    except ValueError:
        return f'The number {number} is not in the sequence'