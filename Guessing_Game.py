import random

running = True

while running:
    randomNumber = random.randint(1, 6)
    correct = False
    while not correct:
        guess = input("Guess a number between 1 and 6: ")
        if guess == "Q" or guess == "q":
            running = False
            break
        elif randomNumber == int(guess):
            print("Correct")
            correct = True
        else:
            print("Incorrect")