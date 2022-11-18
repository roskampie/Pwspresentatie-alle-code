import random
from Cell import Cell


def in_bounds(row, col, rows, cols):
    return 0 <= row < rows and 0 <= col < cols


def randomize_bombs(board):
    # generate random rows and cols for bombs
    random_rows = []
    random_cols = []

    bomb_locations = set()
    num_bombs = 0

    for i in range(10):
        rand_row = random.randint(0, 9)
        rand_col = random.randint(0, 9)

        random_rows.append(rand_row)
        random_cols.append(rand_col)

    for idx in range(10):
        row = random_rows[idx]
        col = random_cols[idx]

        if (row, col) not in bomb_locations:
            bomb_locations.add((row, col))
            num_bombs += 1

            cell = board[row][col]
            cell.put_bomb()

            # add 1 bomb for each of 8 adjacent cells
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
                adj_row = dr + row
                adj_col = dc + col

                # modify board to increment num adjacent bombs
                if in_bounds(adj_row, adj_col, len(board), len(board[0])):
                    adj_cell = board[adj_row][adj_col]
                    adj_cell.add_adjacent_bomb()
    return num_bombs


def initialize_board():
    board = []

    for _ in range(10):
        cell_row = []
        for _ in range(10):
            cell_row.append(Cell())
        board.append(cell_row)

    bombs = randomize_bombs(board)
    return board, bombs


def display_board(board):
    board_as_str = ''

    for row in range(len(board)):
        temp_str = '|'
        for col in range(len(board[row])):
            cell = board[row][col]
            if not cell.get_revealed():
                if cell.get_flagged():
                    temp_str += 'F'
                else:
                    temp_str += '.'
            else:
                if cell.get_exploding_bomb():
                    temp_str += 'B'
                elif cell.get_bomb():
                    temp_str += 'b'
                elif cell.get_adjacent_bombs() > 0:
                    temp_str += str(cell.get_adjacent_bombs())
                else:
                    temp_str += ' '
            temp_str += '|'
        temp_str += '\n'
        board_as_str += temp_str

    return board_as_str
