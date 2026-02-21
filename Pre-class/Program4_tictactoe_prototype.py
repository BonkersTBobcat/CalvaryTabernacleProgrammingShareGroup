import os
import random

while True:
    # set game variables
    gameOver = False
    player = ""
    board = ['1','2','3','4','5','6','7','8','9']
    # let the player choose what piece to play
    while player != "X" and player != "O" and player != "Q":
        player = input("Choose either X or O: ")
    if player == "Q":
        break
    # begin the main game loop
    while True:
        print()
        print()
        print()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(" " + board[0] + " | " + board[1] + " | " + board[2])
        print("---|---|---")
        print(" " + board[3] + " | " + board[4] + " | " + board[5])
        print("---|---|---")
        print(" " + board[6] + " | " + board[7] + " | " + board[8])
        if player == "X":
            # let the player choose a space
            choice = ""
            while choice == "X" or choice == "O" or choice not in board:
                choice = input("Please select one of the available spaces: ")
            board[int(choice)-1] = "X"
            # check if X won horizontally
            if ((board[0] == board[1] == board[2] == "X")
                    or (board[3] == board[4] == board[5] == "X")
                    or (board[6] == board[7] == board[8] == "X")
                    or (board[0] == board[3] == board[6] == "X")
                    or (board[1] == board[4] == board[7] == "X")
                    or (board[2] == board[5] == board[8] == "X")
                    or (board[0] == board[4] == board[8] == "X")
                    or (board[2] == board[4] == board[6] == "X")):
                # print the board
                print()
                print()
                print()
                os.system('cls' if os.name == 'nt' else 'clear')
                print(" " + board[0] + " | " + board[1] + " | " + board[2])
                print("---|---|---")
                print(" " + board[3] + " | " + board[4] + " | " + board[5])
                print("---|---|---")
                print(" " + board[6] + " | " + board[7] + " | " + board[8])
                input("You won!")
                break
            # print the board
            print()
            print()
            print()
            os.system('cls' if os.name == 'nt' else 'clear')
            print(" " + board[0] + " | " + board[1] + " | " + board[2])
            print("---|---|---")
            print(" " + board[3] + " | " + board[4] + " | " + board[5])
            print("---|---|---")
            print(" " + board[6] + " | " + board[7] + " | " + board[8])
            # randomly select a place for the bot's piece
            bot = random.randint(1,9)
            while board[bot-1] == "X" or board[bot-1] == "O":
                bot = random.randint(1,9)
            board[bot-1] = "O"
            # check if O won
            if ((board[0] == board[1] == board[2] == "O")
                    or (board[3] == board[4] == board[5] == "O")
                    or (board[6] == board[7] == board[8] == "O")
                    or (board[0] == board[3] == board[6] == "O")
                    or (board[1] == board[4] == board[7] == "O")
                    or (board[2] == board[5] == board[8] == "O")
                    or (board[0] == board[4] == board[8] == "O")
                    or (board[2] == board[4] == board[6] == "O")):
                # print the board
                print()
                print()
                print()
                os.system('cls' if os.name == 'nt' else 'clear')
                print(" " + board[0] + " | " + board[1] + " | " + board[2])
                print("---|---|---")
                print(" " + board[3] + " | " + board[4] + " | " + board[5])
                print("---|---|---")
                print(" " + board[6] + " | " + board[7] + " | " + board[8])
                input("Sorry, better luck next time!")
                break
        else:
            # randomly select a place for the bot's piece
            bot = random.randint(1,9)
            while board[bot-1] == "X" or board[bot-1] == "O":
                bot = random.randint(1,9)
            board[bot-1] = "X"
            # check if O won
            if ((board[0] == board[1] == board[2] == "X")
                    or (board[3] == board[4] == board[5] == "X")
                    or (board[6] == board[7] == board[8] == "X")
                    or (board[0] == board[3] == board[6] == "X")
                    or (board[1] == board[4] == board[7] == "X")
                    or (board[2] == board[5] == board[8] == "X")
                    or (board[0] == board[4] == board[8] == "X")
                    or (board[2] == board[4] == board[6] == "X")):
                # print the board
                print()
                print()
                print()
                os.system('cls' if os.name == 'nt' else 'clear')
                print(" " + board[0] + " | " + board[1] + " | " + board[2])
                print("---|---|---")
                print(" " + board[3] + " | " + board[4] + " | " + board[5])
                print("---|---|---")
                print(" " + board[6] + " | " + board[7] + " | " + board[8])
                input("Sorry, better luck next time!")
                break
            # print the board
            print()
            print()
            print()
            os.system('cls' if os.name == 'nt' else 'clear')
            print(" " + board[0] + " | " + board[1] + " | " + board[2])
            print("---|---|---")
            print(" " + board[3] + " | " + board[4] + " | " + board[5])
            print("---|---|---")
            print(" " + board[6] + " | " + board[7] + " | " + board[8])
            # let the player choose a space
            choice = ""
            while choice == "X" or choice == "O" or choice not in board:
                choice = input("Please select one of the available spaces: ")
            board[int(choice)-1] = "O"
            # check if X won horizontally
            if ((board[0] == board[1] == board[2] == "O")
                    or (board[3] == board[4] == board[5] == "O")
                    or (board[6] == board[7] == board[8] == "O")
                    or (board[0] == board[3] == board[6] == "O")
                    or (board[1] == board[4] == board[7] == "O")
                    or (board[2] == board[5] == board[8] == "O")
                    or (board[0] == board[4] == board[8] == "O")
                    or (board[2] == board[4] == board[6] == "O")):
                # print the board
                print()
                print()
                print()
                os.system('cls' if os.name == 'nt' else 'clear')
                print(" " + board[0] + " | " + board[1] + " | " + board[2])
                print("---|---|---")
                print(" " + board[3] + " | " + board[4] + " | " + board[5])
                print("---|---|---")
                print(" " + board[6] + " | " + board[7] + " | " + board[8])
                input("You won!")
                break


