# write your code here
from itertools import count

game = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]


def print_board(board):
    print("---------")
    for row in board:
        print("| " + " ".join(row) + " |")
    print("---------")


def valid_play(cells):
    if len(cells) != 9:
        print("There must be 9 plays")
        return False
    for letter in cells:
        if letter != 'X' and letter != 'O' and letter != '_':
            print("Wrong move " + str(letter))
            return False
    return True


def update_board(row, row_number):
    game[row_number] = row


def play(cells):
    update_board(list(cells[:3]), 0)
    update_board(list(cells[3:6]), 1)
    update_board(list(cells[6:]), 2)


def game_status(game):
    # if not valid_game(game):
    #    return "Impossible"
    winner = get_winner(game)
    if winner:
        return winner + " wins"
    if "_" in game[0] or "_" in game[1] or "_" in game[2]:
        return "Game not finished"
    else:
        return "Draw"


def valid_game(game, cells):
    diff = cells.count('X') - cells.count('O')
    if -1 <= diff <= 1:
        wins = ""
        # Check 3 equals in a row
        for row in range(0, 3):
            if game[row][0] == game[row][1] == game[row][2]:
                winner = game[row][0]
                if not wins or wins == winner:
                    wins = winner
                else:
                    return False

        # Check 3 equals in a column
        for column in range(0, 3):
            if game[0][column] == game[1][column] == game[2][column]:
                winner = game[0][column]
                if not wins or wins == winner:
                    wins = winner
                else:
                    return False
        return True
    return False


def get_winner(game):
    # Check 3 equals in a row
    for row in range(0, 3):
        if game[row][0] == game[row][1] == game[row][2] != '_':
            return game[row][0]

    # Check 3 equals in a column
    for column in range(0, 3):
        if game[0][column] == game[1][column] == game[2][column] != '_':
            return game[0][column]

    # Check diagonals
    if game[0][0] == game[1][1] == game[2][2] != '_':
        return game[0][0]

    if game[0][2] == game[1][1] == game[2][0] != '_':
        return game[0][2]


def valid_coord(game, inp):
    try:
        c_x, c_y = get_coords(inp)
    except Exception:
        print("You should enter numbers!")
        return False

    if not (1 <= c_x <= 3 and 1 <= c_y <= 3):
        print("Coordinates should be from 1 to 3!")
        return False

    row, col = coords_to_row_col(c_x, c_y)
    if game[row][col] != '_':
        print("This cell is occupied! Choose another one!")
        return False
    return True


def coords_to_row_col(x, y):
    col = int(x) - 1
    row = 3 - int(y)
    return row, col


def get_coords(inp):
    x, y = inp.strip().split(" ")
    return int(x), int(y)


def make_move(game, x, y, symb):
    row, col = coords_to_row_col(x, y)
    game[row][col] = symb


# cells = input("Enter cells: > ")
# while not valid_play(cells):
#    cells = input("Enter cells: > ")

# play(cells)

status = "playing"
play_round = 0
symbols = ["X", "O"]
final_status = ["Draw", "X wins", "O wins"]
print_board(game)

while status not in final_status:
    play_round = play_round + 1
    symbol = symbols[play_round % 2]
    inp = input("Enter the coordinates: > ")

    while not valid_coord(game, inp):
            inp = input("Enter the coordinates: > ")

    coord_x, coord_y = get_coords(inp)
    make_move(game, coord_x, coord_y, symbol)

    print_board(game)
    status = game_status(game)

print(status)
