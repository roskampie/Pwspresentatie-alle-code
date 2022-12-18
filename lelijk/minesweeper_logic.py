from Board import in_bounds


def reveal_cells(board, row, col):
    # reveal the cell and any adjacent cells until reaches cell next to bomb or edge of board
    cell_stack = [row, col]

    while cell_stack:
        col = cell_stack.pop()
        row = cell_stack.pop()
        if not board[row][col].get_flagged():
            board[row][col].reveal()
        if board[row][col].get_adjacent_bombs() == 0:
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, -1), (-1, -1), (1, 1)]:
                new_row = row + dr
                new_col = col + dc

                if in_bounds(new_row, new_col, len(board), len(board[0])) and board[new_row][new_col].is_hidden() and not board[new_row][new_col].get_flagged():
                    cell_stack.append(new_row)
                    cell_stack.append(new_col)


def player_move(board, action, row, col):
    if not in_bounds(row, col, len(board), len(board[row])):
        return -1

    cell = board[row][col]
    if action.lower() == 'f':
        # invalid if flag a revealed cell
        if cell.get_revealed():
            return -1
        # if already flagged, remove flag
        if cell.get_flagged():
            cell.remove_flag()
            return 1
        else:
            cell.flag()
    elif action.lower() == 'r':
        # invalid if revealing already revealed cell
        if cell.get_revealed():
            return -1

        reveal_cells(board, row, col)
        if cell.get_flagged():
            cell.remove_flag()
            cell.reveal()
            return 1
    else:
        return -1

    return 0


def game_status(board):
    all_and_only_bombs_flagged = True
    for row in range(len(board)):
        for col in range(len(board[row])):
            cell = board[row][col]

            if cell.get_bomb():
                # if cell with bomb revealed, game lost
                if cell.get_revealed():
                    return -1
                # if bomb not flagged, cannot win
                if not cell.get_flagged():
                    all_and_only_bombs_flagged = False
            else:
                # if no bomb but cell is flagged, cannot win
                if cell.get_flagged():
                    all_and_only_bombs_flagged = False

    if all_and_only_bombs_flagged:
        # won game
        return 1
    else:
        # game ongoing
        return 0


def map_reveal(board, row, col):
    # reveal all cells in board
    for r in range(len(board)):
        for c in range(len(board[row])):
            cell = board[r][c]
            cell.reveal()

            if r == row and c == col:
                # set exploding bomb at row, col
                cell.set_exploding_bomb()
