"""EX02 - One Shot Wordle - Try to guess the secret word."""

__author__ = "730523706"

# Set a variable to be the secret word
# Set a variable to user's guess by getting the input from the user
secret_word: str = "python"
user_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
# Set variables to strings of the given emojis
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
# Create a while loop that corrects the user if their guess is the wrong length
while len(user_guess) != len(secret_word):
    user_guess = input(f"That was not {len(secret_word)} letters! Try again: ")
# Set your initial counting variable for the following while loop and empty string for the emojis
index_variable: int = 0
emojis_of_guess: str = ""
# Create a while loop that cycles through each index of the user's guess to check to see if the characters are the same as the secret word, resulting in the correct emoji for each index
# Nest an if-statement in the while loop to add a green box to the emoji string if the two indecies were the same or a yellow/white box if they weren't
# Nest a while loop in the else block to check if that character is located in a different index in the secret word
# Create a new counting variable for this while loop
# If the character is located in a different index add a yellow box to the emoji string, if it's not in the idex at all add a white block to the emoji string
while index_variable < len(secret_word):
    if user_guess[index_variable] == secret_word[index_variable]:
        emojis_of_guess += GREEN_BOX
    else:
        yellow_box_variable: int = 0
        while yellow_box_variable < len(secret_word):
            if user_guess[index_variable] == secret_word[yellow_box_variable]:
                emojis_of_guess += YELLOW_BOX
                yellow_box_variable += (len(secret_word) + 1)
            else:
                yellow_box_variable += 1
        if yellow_box_variable == len(secret_word):
            emojis_of_guess += WHITE_BOX
    index_variable += 1
# Print out the results of the guess, colored boxes and if it is correct or not, using a conditional if-statement
if user_guess == secret_word:
    print(emojis_of_guess)
    print("Woo! You got it!")
else:
    print(emojis_of_guess)
    print("Not quite. Play again soon!")