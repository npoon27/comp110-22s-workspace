"""EX02 - One Shot Wordle - Try to guess the secret word."""

__author__ = "730523706"

secret_word: str = "python"
user_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(user_guess) != len(secret_word):
    user_guess = input(f"That was not {len(secret_word)} letters! Try again: ")

index_variable: int = 0
emojis_of_guess: str = ""
while index_variable < len(secret_word):
    if user_guess[index_variable] == secret_word[index_variable]:
        emojis_of_guess = emojis_of_guess + GREEN_BOX
    else:
        yellow_box_variable: int = 0
        while yellow_box_variable < len(secret_word):
            if user_guess[index_variable] == secret_word[yellow_box_variable]:
                emojis_of_guess = emojis_of_guess + YELLOW_BOX
                yellow_box_variable = yellow_box_variable + len(secret_word) + 1
            else:
                yellow_box_variable = yellow_box_variable + 1
        if yellow_box_variable == len(secret_word):
            emojis_of_guess = emojis_of_guess + WHITE_BOX
    index_variable = index_variable + 1

if user_guess == secret_word:
    print(emojis_of_guess)
    print("Woo! You got it!")
else:
    print(emojis_of_guess)
    print("Not quite. Play again soon!")