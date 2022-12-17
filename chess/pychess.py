import chess
board = chess.Board()
def checking():
    board.is_checkmate()
    #check if there is al checkmate
    board.is_fivefold_repetition()
    #check if the same moves have been done 5 times, (this makes the game a draw)
    board.is_check()
    #check if there is a check
    board.is_stalemate()
    #check if there is a stalemate
    if board.is_checkmate == True:
        print("L")
    if board.is_stalemate == True:
        print("Stalemate")
    if board.is_fivefold_repetition == True:
        print("Stalemate!")
    if board.is_check == True:
        print("check!")

def main():
    print(board)
    #show the board
    checking()
    #check if there are any special events
    move = input("\nwhat move would you like to do: ")
    if move == "legal":
        print(board.legal_moves)
        main()
    elif move == "quit" or move == "exit":
        exit()
    else:
        if move == board.legal_moves:
            board.push_san(move)
            main()
        else:
            print("invalid move, please check by typing: legal")
            main()
main()