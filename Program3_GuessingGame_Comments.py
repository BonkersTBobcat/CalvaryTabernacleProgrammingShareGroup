# First thing we are doing is importing any libraries we need.
# In this case, we are importing the random library. That's the only
# library we'll need for this program.
import random

# We create our running variable, which we will use
# to control if the program keeps running or not.
running = True

# We create a while loop, which will keep running while
# the running variable is true.
while running:
    # Next we create a randomNumber variable, and store in it whatever value comes from
    # the randint() function, giving the parameters 1 and 6 so that we only get numbers
    # between 1 and 6.
    randomNumber = random.randint(1,6)
    # Next we create a variable called correct, which we will use to keep track of if the
    # player has gotten the correct answer yet. Since the game just started, they have made
    # no guesses, so correct is False right now.
    correct = False
    # Then we have another while loop inside our first while loop. This one will keep running
    # while the player's answer is not correct. In programming, when you type in the word not.
    # that means something special. It means take whatever the following value is, and make it
    # the opposide. So if correct is False, then not correct would be True, which means that the
    # while loop will keep running. When correct becomes True, then not correct is false, and the
    # while loop will stop running.
    while not correct:
        # Now inside this second loop create another variable called guess, in which we store the
        # player's input. The player must type something, then hit the enter key. We ask the player
        # to type a number between 1 and 6, but there is nothing stopping the player from entering
        # something completely different.
        guess = input("Guess a number between 1 and 6: ")
        # Next we ask the computer, is player's input, the guess variable, equal to either Q or q.
        if guess == 'Q' or guess == 'q':
            # If the player's input was equal to Q or q, then we set running to false.
            running = False
            # break is a special control statement. It means to break out of the loop.
            # Right now we are inside the while not correct loop, but as soon as we say break,
            # The computer leaves this loop. Because there is no more code in the while running
            # loop after this, we go back to the beginning of the while running loop.
            break
        # elif is a special controller statement. It means, if the previous controller statement
        # was not true, then check if this one is true. In this case, we are checking if the
        # randomNumber variable is equal to the guess variable.
        #
        # Remember though that the input() function returns a string, and the randint() function returns
        # and integer. A String "6" and an integer 6 are not considered equal. So we use the int() function,
        # which converts a string into an integer. Then we check if the two values are equal.
        #
        # Notice also, that just like the while loop and the if, the elif line must end with a colon.
        elif randomNumber == int(guess):
            # If the player's guess was correct, we want to tell them. So we use the print() function to tell
            # them that they were "Correct".
            print("Correct")
            # We then set the correct variable to true, because the player got the correct answer
            correct = True
        # else is special. Think of it as a catch-all. If all the previous conditions were false,
        # then the code under the else will be used. But ONLY of the previous are false.
        # So you start with if, you can have as many elif as you want, and then you can end with an else.
        #
        # Notice that just like the while-loop, if, and elif lines, the else line must end with a colon.
        else:
            # if the player did not guess correctly, then we simply tell them "Incorrect".
            print("Incorrect")