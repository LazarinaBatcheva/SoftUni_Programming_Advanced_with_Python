from core.fibonacci_helpers import create_sequence, locate_num


def play_fibonacci():
    command = input()
    sequence = []

    while command != 'Stop':
        if command.startswith('Create'):
            number = int(command.split()[-1])
            sequence = create_sequence(number)
            print(*sequence)

        elif command.startswith('Locate'):
            number = int(command.split()[-1])
            print(locate_num(number, sequence))

        command = input()
