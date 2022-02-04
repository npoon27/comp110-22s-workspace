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
    """Generates a string emojis that gives information about how well the guess matches the secret word."""
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
