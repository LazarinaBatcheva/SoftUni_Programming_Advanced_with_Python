def is_valid_sign(player_one_sign_):
    return player_one_sign_ in ['X', 'O']


def is_valid_choice(board_, board_mapper_, choice_, current_player_, size_):
    if not choice_.isdigit():
        print('Incorrect choice')
        print(f'{current_player_} you need to choose a number between 1-{size_ ** 2}')
        return False

    choice_ = int(choice_)

    if choice_ not in board_mapper_:
        print(f'{current_player_} you need to choose a number between 1-{size_ ** 2}')
        return False

    if board_[board_mapper_[choice_][0]][board_mapper_[choice_][1]]:
        print('The position is already taken! Please choose another one: ')
        return False

    return True


def render_board(board_):
    [print(f'| {" | ".join([sign if sign else " " for sign in row_])} |') for row_ in board_]


def is_row_win(board_):
    for row_ in board_:
        if len(set(row_)) == 1 and set(row_) != {None}:
            return True

    return False


def is_col_win(board_, current_sign_):
    for col_ in range(len(board_)):
        current_col = []
        for row_ in range(len(board_)):
            current_col.append(board_[row_][col_] == current_sign_)

        if all(current_col):
            return True

    return False


def is_diagonal_win(board_, current_sign_):
    diagonal_1, diagonal_2 = [], []
    for index in range(len(board_)):
        diagonal_1.append(board_[index][index] == current_sign_)
        diagonal_2.append(board_[index][len(board_) - 1 - index] == current_sign_)

    return all(diagonal_1) or all(diagonal_2)


def is_win(board_, current_sign_):
    return any([is_row_win(board_),
                is_col_win(board_, current_sign_),
                is_diagonal_win(board_, current_sign_)])


def is_row_win_possible(board_):
    if all(['X' in row_ and 'O' in row_ for row_ in board_]):
        return False
    return True


def is_col_win_possible(board_):
    columns = []
    for col_ in range(len(board_)):
        current_col = []
        for row_ in range(len(board_)):
            current_col.append(board_[row_][col_])
        columns.append(current_col)

    if all(['X' in col_ and 'O' in col_ for col_ in columns]):
        return False
    return True


def is_diagonal_win_possible(board_):
    diagonal_1, diagonal_2 = [], []
    for index in range(len(board_)):
        diagonal_1.append(board_[index][index])
        diagonal_2.append(board_[index][len(board_) - 1 - index])

    if 'X' in diagonal_1 and 'O' in diagonal_1 and 'X' in diagonal_2 and 'O' in diagonal_2:
        return False
    return True


def is_draw(board_):
    if any([is_row_win_possible(board_),
            is_col_win_possible(board_),
            is_diagonal_win_possible(board_)]):
        return False
    return True


player_one = input('Player one name: ')
player_two = input('Player two name: ')

while True:
    player_one_sign = input(f'{player_one} would you like to play with "X" or "O"? ').upper()

    if is_valid_sign(player_one_sign):
        break

    print(f'{player_one} please, enter a one of "X" or "O"!')

player_two_sign = 'O' if player_one_sign == 'X' else 'X'

size = 3
board = [[None] * size for _ in range(size)]
board_mapper = {i + 1: (i // size, i % size) for i in range(size ** 2)}

print('This is the numeration of the board:')
[print(f'| {" | ".join([str(i + 1 + row * size) for i in range(size)])} |') for row in range(size)]
print(f'{player_one} starts first!')

turn = 1

while True:
    current_player = player_one if turn % 2 else player_two
    current_sign = player_one_sign if turn % 2 else player_two_sign

    while True:
        choice = input(f'{current_player} choose a free position [1-{size ** 2}]: ')

        if is_valid_choice(board, board_mapper, choice, current_player, size):
            break

    row, col = board_mapper[int(choice)]
    board[row][col] = current_sign

    render_board(board)

    if is_win(board, current_sign):
        print(f'{current_player} won!')
        break

    if is_draw(board):
        print('Draw!')
        break

    turn += 1