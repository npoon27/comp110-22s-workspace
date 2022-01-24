"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730523706"

user_word: str = input("Enter a 5-character word: ")
if len(user_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
user_character: str = input("Enter a single character: ")
if len(user_character) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + user_character + " in " + user_word)

if user_character == user_word[0]:
    print(user_character + " found at index 0")
if user_character == user_word[1]:
    print(user_character + " found at index 1")
if user_character == user_word[2]:
    print(user_character + " found at index 2")
if user_character == user_word[3]:
    print(user_character + " found at index 3")
if user_character == user_word[4]:
    print(user_character + " found at index 4")

matching_characters: int = 0
if user_character == user_word[0]:
    matching_characters = matching_characters + 1
if user_character == user_word[1]:
    matching_characters = matching_characters + 1
if user_character == user_word[2]:
    matching_characters = matching_characters + 1
if user_character == user_word[3]:
    matching_characters = matching_characters + 1
if user_character == user_word[4]:
    matching_characters = matching_characters + 1

if matching_characters == 1:
    print(str(matching_characters) + " instance of " + user_character + " found in " + user_word)
elif matching_characters >= 1:
    print(str(matching_characters) + " instances of " + user_character + " found in " + user_word)
else:
    print("No instances of " + user_character + " found in " + user_word)