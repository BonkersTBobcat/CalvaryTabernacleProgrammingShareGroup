import os
import random

def game_over(board, print_message):
    if ((board[0]==board[1]==board[2]=="X")
    or (board[3]==board[4]==board[5]=="X")
    or (board[6]==board[7]==board[8]=="X")
    or (board[0]==board[3]==board[6]=="X")
    or (board[1]==board[4]==board[7]=="X")
    or (board[2]==board[5]==board[8]=="X")
    or (board[0]==board[4]==board[8]=="X")
    or (board[2]==board[4]==board[6]=="X")):
        if print_message:
            input("Congratulations, YOU WON!!!")
        return True
    elif ((board[0]==board[1]==board[2]=="O")
    or (board[3]==board[4]==board[5]=="O")
    or (board[6]==board[7]==board[8]=="O")
    or (board[0]==board[3]==board[6]=="O")
    or (board[1]==board[4]==board[7]=="O")
    or (board[2]==board[5]==board[8]=="O")
    or (board[0]==board[4]==board[8]=="O")
    or (board[2]==board[4]==board[6]=="O")):
        if print_message:
            input("Sorry, better luck next time")
        return True
    elif not any(item in board for item in ['1','2','3','4','5','6','7','8','9']):
        if print_message:
            input("Huh, looks like a tie")
        return True
    return False

def print_board(board):
    for i in range(20):
        print()
    if 'TERM' in os.environ:
        os.system('cls' if os.name == 'nt' else 'clear')
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

def player_move(board):
    # exit immediately if the game is over
    if game_over(board, False):
        return
    # let the player select a space
    choice = ""
    # keep asking the player until they select an unselected space
    while choice not in ['1','2','3','4','5','6','7','8','9'] or choice not in board:
        choice = input("Please select one of the available spaces: ")
    # set the player selected space to X
    board[int(choice)-1] = "X"

def bot_move(board):
    # exit immediately if the game is over
    if game_over(board, False):
        return
    # choose a random spot
    bot = random.randint(0,8)
    # if that random spot is already selected
    while board[bot] == "X" or board[bot]=="O":
        # choose another random spot until a spot that occupied is selected
        bot =random.randint(0,8)
    # set the random spot to O
    board[bot] = "O"