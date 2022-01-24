"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730523706"

user_word: str = input("Enter a 5-character word: ")
user_character: str = input("Enter a single character: ")
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

