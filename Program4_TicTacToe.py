import os
import random

gameOver = False
board = ['1','2','3','4','5','6','7','8','9']

while not gameOver:
    print(board[0] + board[1] + board[2])
    print(board[3] + board[4] + board[5])
    print(board[6] + board[7] + board[8])
    choice = input("Please select one of the available spaces: ")
    board[int(choice)-1] = "X"
    print()
    print()
    print()
    print(board[0] + board[1] + board[2])
    print(board[3] + board[4] + board[5])
    print(board[6] + board[7] + board[8])
    if ((board[0]=="X" and board[1]=="X" and board[2]=="X")
    or (board[3]=="X" and board[4]=="X" and board[5]=="X")
    or (board[6]=="X" and board[7]=="X" and board[8]=="X")
    or (board[0]=="X" and board[3]=="X" and board[6]=="X")
    or (board[1]=="X" and board[4]=="X" and board[7]=="X")
    or (board[2]=="X" and board[5]=="X" and board[8]=="X")
    or (board[0]=="X" and board[4]=="X" and board[8]=="X")
    or (board[2]=="X" and board[4]=="X" and board[6]=="X")):
        input("Congratulations, You Won!")
        break

    bot = random.randint(0,8)
    while board[bot] == "X" or board[bot]=="O":
        bot =random.randint(0,8)
    board[bot] = "O"
    print()
    print()
    print()
    print(board[0] + board[1] + board[2])
    print(board[3] + board[4] + board[5])
    print(board[6] + board[7] + board[8])
    if ((board[0]=="O" and board[1]=="O" and board[2]=="O")
    or (board[3]=="O" and board[4]=="O" and board[5]=="O")
    or (board[6]=="O" and board[7]=="O" and board[8]=="O")
    or (board[0]=="O" and board[3]=="O" and board[6]=="O")
    or (board[1]=="O" and board[4]=="O" and board[7]=="O")
    or (board[2]=="O" and board[5]=="O" and board[8]=="O")
    or (board[0]=="O" and board[4]=="O" and board[8]=="O")
    or (board[2]=="O" and board[4]=="O" and board[6]=="O")):
        input("Sorry, better luck next time")
        break