"""EX03 - Wordle - A fun word guessing game to play."""

__author__ = "730523706"


# Create a function that checks to see if each individule character of the user's guess is in any index of the secret word
# In funtion: Make sure that the character being searched for is a single character
# In funtion: Make a counting variable that keeps track of the indecies of the secret work being searched
# In funtion: Create a while loop that repeats for as long as the secret word it
# In the loop return true if the character is in the secret at any index and false if it did not appear in the word
def contains_char(searched_string: str, searching_character: str) -> bool:
    """Checks to see if a certain character in the user's guess is in the secret word."""
    assert len(searching_character) == 1
    counting_variable: int = 0
    while counting_variable < len(searched_string):
        if searched_string[counting_variable] == searching_character:
            return True
        counting_variable += 1
    return False


# Create a function that makes a string of emojis based off of if the characters of the user's guess are in the secret word and if they are in the right position(index)
# In funtion: Set an assertion to make sure the user's guess is the same length as the secret word
# In funtion: Create variables for the emojis of the boxes, counting variable, and the initial empty emoji string
# In funtion: Make a while loop that repeats for as long as the secret word is
# In funtion: Nest an if-elif-else statement within the while loop
# if the character of the indecies are equal add a green box to the string
# elif call to the contains_char funtion, if it comes back true add a yellow box
# else (the character isn't in the secret word) add a white box
# In funtion: once the loop is complete return the string of emojis
def emojified(user_guess: str, secret_word: str) -> str:
    """Generates a string of emojis that gives information about how well the guess matches the secret word based on each character of the guess."""
    assert len(user_guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    emoji_string: str = ""
    while i < len(secret_word):
        if user_guess[i] == secret_word[i]:
            emoji_string += GREEN_BOX
        elif contains_char(secret_word, user_guess[i]) is True:
            emoji_string += YELLOW_BOX
        else:
            emoji_string += WHITE_BOX
        i += 1
    return emoji_string


# Create a funtion that makes sure the user's guess is the same length of the secret word(an expected length)
# In funtion: Ask the user to enter a guess that is the length of the secret word
# In funtion: Make an if-else-statement
# If the guess is the right length reutrn the guess
# If the guess wasn't the right length make a while loop that asks for another guess until the guess is the correct length, then return the guess
def input_guess(expected_length: int) -> str:
    """Checks to make sure that the users guess is the same length as the secret word."""
    user_guess: str = input(f"Enter a {expected_length} character word: ")
    if expected_length == len(user_guess):
        return user_guess
    else:
        while expected_length != len(user_guess):
            user_guess = input(f"That wasn't {expected_length} chars! Try again: ")
        return user_guess


# Create a funtion that is the main funtion for the game
# In funtion: Create a variable that holds your secret word and a variable to keep track of the turns
# In funtion: The game goes on for 6 turns so create a while loop that repeats for the 6 turns
# In funtion: If the game gets to turn 7 tell the user they lost
# In while loop: Print the turn
# In while loop: Create a user guess variable and call to input_guess funtion with the len of the secret word
# In while loop: Print out the emoji string that is gotten from calling to the emojified funtion with (user_guess, secret_word)
# In while loop: Nest an If-Statement: If the user's guess is right then tell them they won and end the loop, if the user was wrong go onto the next turn
def main() -> None:
    """The enrtypoint of the program and main game loop."""
    secret_word: str = "codes"
    turn: int = 1
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        user_guess: str = input_guess(len(secret_word))
        print(emojified(user_guess, secret_word))
        if user_guess == secret_word:
            print(f"You won in {turn}/6 turns!")
            turn += 7
        else:
            turn += 1
    if turn == 7:
        print("X/6 - Sorry, try again tomorrow!")


# Create a way to run the game as a module
if __name__ == "__main__":
    main()