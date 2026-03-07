import random

def print_board(board):
    print()
    print()
    print()
    print(board[0] + board[1] + board[2])
    print(board[3] + board[4] + board[5])
    print(board[6] + board[7] + board[8])

def is_game_over(board, piece):
    if ((board[0]==board[1]==board[2]==piece)
    or (board[3]==board[4]==board[5]==piece)
    or (board[6]==board[7]==board[8]==piece)
    or (board[0]==board[3]==board[6]==piece)
    or (board[1]==board[4]==board[7]==piece)
    or (board[2]==board[5]==board[8]==piece)
    or (board[0]==board[4]==board[8]==piece)
    or (board[2]==board[4]==board[6]==piece)):
        if (piece=="X"):
            input("Congratulations, you won!")
            return True
        elif (piece== "O"):
            input("Sorry, better luck next time.")
            return True
    if not any(item in board for item in ['1','2','3','4','5','6','7','8','9']):
        input("Huh, looks like a tie")
        return True
    return False

def player_move(board):
    choice = input("Please select one of the available spaces: ")
    while choice not in board or choice not in ['1','2','3','4','5','6','7','8','9']:
        choice = input("Please select one of the available spaces: ")
    board[int(choice)-1] = "X"

def bot_move(board):
    bot = random.randint(0, 8)
    while board[bot] == "X" or board[bot] == "O":
        bot = random.randint(0, 8)
    board[bot] = "O"