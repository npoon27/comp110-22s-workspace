"""EX03 - Wordle - A fun word guessing game to play."""

__author__ = "730523706"


def contains_char(searched_string: str, searching_character: str) -> bool:
    """Checks to see if a certain character in the user's guess is in the secret word."""
    assert len(searching_character) == 1
    counting_variable: int = 0
    while counting_variable < len(searched_string):
        if searched_string[counting_variable] == searching_character:
            return True
        counting_variable += 1
    return False


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


def input_guess(expected_length: int) -> str:
    """Checks to make sure that the users guess is the same length as the secret word."""
    user_guess: str = input(f"Enter a {expected_length} character word: ")
    if expected_length == len(user_guess):
        return user_guess
    else:
        while expected_length != len(user_guess):
            user_guess = input(f"That wasn't {expected_length} chars! Try again: ")
        return user_guess


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
            exit()
        turn += 1
    print("X/6 - Sorry, try again tomorrow!")
    exit()


if __name__ == "__main__":
    main()