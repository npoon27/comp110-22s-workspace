"""EX02 - One Shot Wordle - Try to guess the secret word."""

__author__ = "730523706"

secret_word: str = "python"
user_guess: str = input("What is your 6-letter guess? ")

while len(user_guess) != 6:
    user_guess: str = input("That was not 6 letters! Try again: ")

if user_guess == "python":
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")