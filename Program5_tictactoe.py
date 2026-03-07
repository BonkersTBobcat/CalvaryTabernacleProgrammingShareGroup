from Program5_tictactoe_libary import print_board,player_move,is_game_over,bot_move

gameOver = False
board = ['1','2','3','4','5','6','7','8','9']

while not gameOver:
    print_board(board)
    player_move(board)
    print_board(board)
    if is_game_over(board,"X"):
        break
    bot_move(board)
    print_board(board)
    if is_game_over(board,"O"):
        break
