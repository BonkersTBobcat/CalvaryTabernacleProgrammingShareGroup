# Imports
from random import choice as random_word

# Get a list of all the words
def load_words(filename):
    # Create an empty list
    words = []
    # Open the file for reading
    with open(filename, "r") as file:
        # Read each line in the file
        for line in file:
            # Remove whitespace and newline characters
            cleaned_line = line.strip()
            # Skip empty lines
            if cleaned_line != "":
                words.append(cleaned_line)
    # Return whatever words were read
    return words

# Return what has been guessed and what is blank as a string
def display_word(secret_word, guessed_letters):
    # Create an empty string
    display = ""
    # Check each letter in our secret word
    for letter in secret_word:
        # If the letter is in our list of guessed letters
        if letter.lower() in guessed_letters:
            # Add the letter to our display string, along with an empty space
            display += letter + " "
        # Otherwise
        else:
            # add an Underscore and an empty space to our display string
            display += "_ "
    # Return the complete display string
    return display

# Check if the player won
def player_won(secret_word, guessed_letters):
    # For each letter in the secret word
    for letter in secret_word:
        # If that letter is not in the list of guessed letters
        if letter not in guessed_letters:
            # Return false
            return False
    # If we didn't return false already, then return true
    return True


# Load the words from a file
words = load_words("Program7_words.txt")
# Select one of these words at random
secret_word = random_word(words)
# Create a new empty set
guessed_letters = set()
# Track how many times the player has guessed wrong
wrong_guesses = 0
# Create a limit to how many times they can guess wrong
max_wrong = 6

# Introduce the game to the player
print("Welcome to Hangman!")

# GAME LOOP
# While the player has guesses left
while wrong_guesses < max_wrong:
    # Print the solved portion of the secret word
    print("\nWord:", display_word(secret_word, guessed_letters))
    # Print the letters that have been guessed, both right and wrong
    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    # Print out how many lives they have left
    print("Remaining lives:", max_wrong - wrong_guesses)
    # Prompt the player to make a guess
    guess = input("Guess a letter: ").lower()

    # If the player tried to enter more than one character or a non-letter character
    if len(guess) != 1 or not guess.isalpha():
        # Tell them to please enter a single character
        print("Please enter a single letter.")
        # Go back to the beginning of the loop
        continue

    # If the player entered a letter they already guessed
    if guess in guessed_letters:
        # Tell them they already guessed that
        print("You already guessed that.")
        # Go back to the beginning of the loop
        continue

    # Add this guess to the list of guessed letters
    guessed_letters.add(guess)

    # If the guess is not part of the secret word
    if guess not in secret_word:
        # Add 1 to the number of wrong guesses
        wrong_guesses += 1
        # Tell them they were wrong
        print("Wrong guess!")

    # If the player won
    if player_won(secret_word, guessed_letters):
        # Tell them they won
        print("\nYou win! The word was:", secret_word)
        # Exit the GAME LOOP
        break

# If they guessed wrong too many times
if wrong_guesses >= max_wrong:
    # Tell the player they lose
    print("\nYou lose! The word was:", secret_word)