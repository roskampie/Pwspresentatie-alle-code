from Board import initialize_board, display_board
from minesweeper_logic import player_move, game_status, map_reveal


def print_board(board):
    board_as_str = display_board(board)
    print(board_as_str)


def display_win(board):
    print_board(board)
    print("U WIN!")


def display_lost(board, row, col):
    map_reveal(board, row, col)
    print_board(board)
    print("U LOST...")


def play():
    board, bombs = initialize_board()

    while True:
        print(f'\nBombs remaining: {bombs}')
        print_board(board)

        move = -1
        while move == -1:
            row = int(input("Enter a row: "))
            col = int(input("Enter a column: "))
            action = input("R/r to reveal, F/f to flag: ")

            # modifies the board
            move = player_move(board, action, row, col)

            # invalid move = -1, valid move = 0, unflagged = 1
            if move == -1:
                print("Invalid move, please try again.")
            elif move == 1:
                bombs += 1
            elif action.lower() == 'f':
                bombs -= 1

        # 1 - win, 0 ongoing, -1, lost
        status = game_status(board)

        if status == 1:
            display_win(board)
            break
        elif status == -1:
            display_lost(board, row, col)
            break

    print("Thanks for playing!")


play()
