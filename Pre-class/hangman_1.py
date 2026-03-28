from random import choice as random_word

def load_word(filename):
    words = []
    with open(filename, "r") as words_file:
        for line in words_file:
            if line.strip():
                words.append(line.strip().lower())
    return random_word(words)

def player_won(secret, guesses):
    for character in secret:
        if character.lower() not in guesses:
            return False
    return True

def display(secret, guesses):
    display = ""
    for character in secret:
        if character.lower() in guesses:
            display += character + " "
        else:
            display += "_ "
    return display

def print_game(secret, guesses, lives):
    print()
    print()
    print()
    print("WORD: " + display(secret, guesses))
    print("GUESSES: " + str(guesses))
    print("LIVES: " + str(lives))


secret = load_word("words_1.txt")
guesses = []
lives = 6

while lives > 0 and not player_won(secret, guesses):
    print_game(secret, guesses, lives)

    guess = input("Guess a letter: ")
    if guess.lower() in guesses:
        print("You guessed that letter already")
        continue
    if len(guess) != 1 or not guess.isalpha():
        print("Sorry, please enter a single letter")
        continue
    guesses.append(guess)
    if guess.lower() not in secret.lower():
        print("Incorrect guess, please try again")
        lives -= 1
    else:
        print("You got one!")

if player_won(secret, guesses):
    print("You won!")
else:
    print("You lost!")