from random import choice as random_word

def print_file(filename):
    with open(filename) as file:
        for line in file:
            print(line.strip())

def load_word(filename):
    words = []
    with open(filename) as f:
        for line in f:
            if line.strip():
                words.append(line.strip().lower())
    return random_word(words)

def player_won(secret, guesses):
    for character in secret:
        if character not in guesses:
            return False
    return True

def display(secret, guesses):
    display = ""
    for character in secret:
        if character in guesses:
            display += character + " "
        else:
            display += "_ "
    return display

def print_game(secret, guesses, lives):
    print()
    print()
    print()
    print("WORD: " + display(secret_word, guesses))
    print("GUESSES: " + str(guesses))
    print("LIVES: " + str(lives))

while input("Would you like to play a game? (y/n): ").lower() == "y":
    secret_word = load_word("words_2.txt")
    guesses = []
    lives = 6

    while lives > 0 and not player_won(secret_word, guesses):
        print_game(secret_word, guesses, lives)

        guess = input("Guess a letter: ")

        while guess.lower() in guesses or not guess.isalpha() or len(guess) != 1:
            guess = input("Sorry, not a valid guess. Try again: ")

        guesses.append(guess.lower())

        if guess.lower() not in secret_word.lower():
            print("Sorry, try again!")
            lives -= 1
        else:
            print("You got one!")

    print("THE WORD IS: " + secret_word)

    if player_won(secret_word, guesses):
        print("You won!")
    else:
        print("You lost!")