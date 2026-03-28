from random import choice as random_word
from random import randint as random_number

def load_word(filename):
    # count words in file
    count = 0
    with open(filename, "r") as words_file:
        for line in words_file:
            if line.strip():
                count += 1
    # get random word number
    line_number = random_number(1, count)
    # retrieve that word
    currentline = 0;
    with open(filename, "r") as words_file:
        for line in words_file:
            if line.strip():
                currentline += 1
                if currentline == line_number:
                    return line.strip().lower()

def player_won(secret, guesses):
    for character in secret:
        if character.lower() not in guesses:
            return False
    return True

def display(secret, guesses):
    display = ""
    for character in secret:
        if character.lower() in guesses:
            display += character.lower() + " "
        else:
            display += "_ "
    return display

def print_game(secret, guesses, lives):
    print()
    print()
    print()
    print_hangman(lives)
    print("WORD: " + display(secret, guesses))
    print("GUESSES: " + str(guesses))

def print_hangman(lives):
    if lives == 6:
        print(" ___  ")
        print("|   | ")
        print("|     ")
        print("|     ")
        print("|     ")
        print("|_____")
    elif lives == 5:
        print(" ___  ")
        print("|   | ")
        print("|   O ")
        print("|     ")
        print("|     ")
        print("|_____")
    elif lives == 4:
        print(" ___  ")
        print("|   | ")
        print("|   O ")
        print("|   | ")
        print("|     ")
        print("|_____")
    elif lives == 3:
        print(" ___  ")
        print("|   | ")
        print("|   O ")
        print("|  /| ")
        print("|     ")
        print("|_____")
    elif lives == 2:
        print(" ___  ")
        print("|   | ")
        print("|   O ")
        print("|  /|\\")
        print("|     ")
        print("|_____")
    elif lives == 1:
        print(" ___  ")
        print("|   | ")
        print("|   O ")
        print("|  /|\\")
        print("|  /  ")
        print("|_____")
    elif lives == 0:
        print(" ___  ")
        print("|   | ")
        print("|   O ")
        print("|  /|\\")
        print("|  / \\")
        print("|_____")

secret = load_word("Program7_words.txt")
guesses = []
lives = 6

while lives > 0 and not player_won(secret, guesses):
    print_game(secret, guesses, lives)

    guess = input("Guess a letter: ")
    if guess.lower() in guesses:
        print("You guessed that letter already")
        continue
    if not len(guess) == 1 or not guess.isalpha():
        print("Sorry, please enter a single letter")
        continue
    guesses.append(guess)
    if guess.lower() not in secret.lower():
        print("Incorrect guess, please try again")
        lives -= 1
    else:
        print("You got one!")

print()
print()
print()

if player_won(secret,guesses):
    print("You won!")
else:
    print_hangman(lives)
    print("You lost!")

print("WORD: " + secret)