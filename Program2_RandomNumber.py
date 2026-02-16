import random

running = True

while running:
    userInput = input("Hit enter to generate a random number.")
    randomNumber = random.randint(1,100)
    print(randomNumber)
    if userInput == "Q" or userInput == "q":
        running = False