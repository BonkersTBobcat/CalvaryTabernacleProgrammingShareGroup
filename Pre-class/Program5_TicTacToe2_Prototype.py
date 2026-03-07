from Program5_TacTacToe2_Library_Prototype import print_board, player_move, bot_move, game_over

board = ['1','2','3','4','5','6','7','8','9']

while not game_over(board, True):
    print_board(board)
    player_move(board)
    print_board(board)
    bot_move(board)
    print_board(board)