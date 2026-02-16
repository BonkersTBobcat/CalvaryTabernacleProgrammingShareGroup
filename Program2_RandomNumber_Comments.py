# In programming, we don't like to rewrite the same code over and over.
# We reuse code, so that we can save time. The import below is importing
# what is called a library. A library is just a collection of functions
# and other stuff that was written by somebody, and which you can use.
# In this case, we are importing a library called random,
# which will have some functions we need.
import random

# running below is what is known as a variable. You can think of a variable as
# a box, in which you can place a single value.
# Variables also tend to be specific Types of values.
#
# Here is a list of some of the major types of variables:
# integer - Stores whole numbers like 1, 2, 3, 4, etc...
# float - Stores decimal numbers, like 0.5, 0.75, 5.3, etc...
# string - Stores text, similar to what we did with the hello world
# boolean - only has 2 possible values, either True or False. Used to make decisions in code.
#
# In case you couldn't already tell, the variable running here is a boolean variable.
# We are setting it to True to start off, and we are going to use it tell the program it
# should keep running.
running = True

# This is a while loop. There are different kinds of loops in programming, but a while loop
# simply means while something is true, keep doing whatever code follows.
# In this case, while running is true. Note that you also type this
# while True:
# and it would function the same way as long as running is true.
# The difference is, by using a variable, we can actually change running to be false.
# When running becomes false, the while loop will stop running.
while running:
    # You'll notice that the following code is indented. That means it is inside the while loop.
    # Any code indented under the while loop is considered a part of the while loop's block of code.
    # Also note that when putting code under a loop, you must end the loop line with a colon.

    # The first thing we are doing here is creating a variable called userInput, and storing something
    # inside it. We are then calling the function input(). The function input() is a little special,
    # because it can be called with both 0 parameters and 1 parameter. In this case we are giving it 1
    # parameter.
    #
    # The print() function does a few things:
    # 1. If it has a string parameter, then it will print that string out, just like the print() function.
    # 2. It will freeze the program, and wait for you to hit the enter key.
    # 3. If you type in anything before you hit the enter key, what you typed in is returned by the function.
    #
    # In this case, we are taking whatever is returned by the input() function, and storing it inside the
    # userInput variable as a string. This will allow us to do things based on whatever the user entered.
    #
    # Note that if you didn't have this input() function, the program would just keep running, non-stop,
    # and it would go so fast you wouldn't have time to read it.
    userInput = input("Hit enter to generate a random number.")

    # Again, we are creating a variable called randomNumber, and storing inside this variable some value
    # returned from a function. The function we are calling is coming from the library random, which we
    # imported at the top. The dot here seperates the function from the library name. So we are calling
    # the function randint() from the library random. What this function randint does is give us a random
    # integer between 2 values. We are passing in 1 and 100, so it will give us a number between 1 and 100.
    randomNumber = random.randint(1,100)

    # Now we are calling our old friend print(), which prints whatever string you give it as a parameter.
    # Notice here though, we are not giving print() a string parameter. We are also not giving it a
    # string variable. We are giving it an integer variable. If you pass in just a single variable to print,
    # it will work with any variable type.
    # There are more complicated scenarios, but you don't need to worry about those yet.
    print(randomNumber)

    # Now we are going to learn about control statements. The simplest is an if statement. Think of this
    # as if this thing is true, then run the following code. In this case, we are asking if the userInput
    # variable is equal to a capital "Q" string, or a lowercase "q" string. Note that capital and lowercase
    # are different values when programming.
    #
    # You'll notice also that the equals sign is shown twice. In programming, a single equals sign is used
    # to STORE values. A double equals sign is used to CHECK if 2 values are equal to each other.
    #
    # The or in-between is means that either statement can be true. You can also put and in-between, but that
    # would change the meaning of the line. If you put and in-between, then both statements would have to be true.
    # In this case, that is impossible, because a single variable cannot have 2 different values.
    #
    # Together this is what is known as a boolean expression. A boolean expression is just a bunch of stuff put
    # together that is either True or false. So in this case, if you typed a q into the program, then this
    # boolean expression would be true. If you typed Q it would also be True. If you typed in Z, then it would
    # false.
    #
    # Notice also that the if line must end with a colon, just like the while loop line.
    if userInput == "Q" or userInput == "q":
        # You'll notice this line is indented yet again.
        # That's because this line not only belongs to the while loop, but it also belongs to this control statement.
        # Any code that belongs to a control statement will only be run if that control statement is True.
        #
        # What this line does is change the value of the running variable to False.
        # After this, the code goes back to the beginning of the loop. You'll notice that now the value for the while
        # loop is False. So that the while loop will stop running.
        # Because there is no more code after the while loops code, the program will stop running.
        #
        # But remember, we are only setting running to false if the user enters Q or q. This is the user's option to
        # quit the program.
        running = False