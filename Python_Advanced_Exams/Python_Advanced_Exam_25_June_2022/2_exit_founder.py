# size of the matrix
from collections import deque

MAZE_SIZE = 6

# possible characters in the matrix
EXIT = 'E'
TRAP = 'T'
WALL = 'W'


def filling_matrix(size):
    matrix = []
    for row in range(size):
        matrix.append(list(input().split()))

    return matrix


players = deque({'player_name': name, 'rest': False} for name in input().split(', '))

maze_board = filling_matrix(MAZE_SIZE)

while True:
    current_player = players[0]

    # the given coordinates will always be valid
    given_row, given_col = [int(x) for x in input().strip('()').split(', ')]
    given_pos = maze_board[given_row][given_col]

    # checking if player is resting
    if current_player['rest']:
        current_player['rest'] = False
        players.rotate(-1)
        continue

    elif given_pos == EXIT:
        print(f'{current_player["player_name"]} found the Exit and wins the game!')
        break

    elif given_pos == TRAP:
        print(f'{current_player["player_name"]} is out of the game! The winner is {players[1]["player_name"]}.')
        break

    elif given_pos == WALL:
        print(f'{current_player["player_name"]} hits a wall and needs to rest.')
        current_player['rest'] = True

    players.rotate(-1)