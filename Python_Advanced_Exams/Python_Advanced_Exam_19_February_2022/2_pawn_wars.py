MATRIX_SIZE = 8

# possible characters in matrix
WHITE_PAWN = 'w'
BLACK_PAWN = 'b'


def find_pawn_positions(matrix):
    w_row, w_col = 0, 0
    b_row, b_col = 0, 0

    for row_index in range(MATRIX_SIZE):
        for col_index in range(MATRIX_SIZE):
            if matrix[row_index][col_index] == WHITE_PAWN:
                w_row, w_col = row_index, col_index
            elif matrix[row_index][col_index] == BLACK_PAWN:
                b_row, b_col = row_index, col_index

    return w_row, w_col, b_row, b_col


def is_diagonal_capture(color, w_row, w_col, b_row, b_col):
    if color == WHITE_PAWN:
        return (w_row - 1, w_col - 1) == (b_row, b_col) or (w_row - 1, w_col + 1) == (b_row, b_col)
    else:
        return (b_row + 1, b_col - 1) == (w_row, w_col) or (b_row + 1, b_col + 1) == (w_row, w_col)


def move_pawn(row, color):
    if color == WHITE_PAWN:
        return row - 1
    else:
        return row + 1


def play_game(matrix):
    w_row, w_col, b_row, b_col = find_pawn_positions(matrix)

    while True:
        if is_diagonal_capture(WHITE_PAWN, w_row, w_col, b_row, b_col):
            return f"Game over! White win, capture on {chr(97 + b_col)}{abs(b_row - 8)}."

        w_row = move_pawn(w_row, WHITE_PAWN)
        if w_row == 0:
            return f"Game over! White pawn is promoted to a queen at {chr(97 + w_col)}8."

        if is_diagonal_capture(BLACK_PAWN, w_row, w_col, b_row, b_col):
            return f"Game over! Black win, capture on {chr(97 + w_col)}{abs(w_row - 8)}."

        b_row = move_pawn(b_row, BLACK_PAWN)
        if b_row == 7:
            return f"Game over! Black pawn is promoted to a queen at {chr(97 + b_col)}1."


board = [input().split() for _ in range(MATRIX_SIZE)]

print(play_game(board))
