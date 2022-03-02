"""EX06 - Dictionary Functions - Creating basic dictionary fuctions to practice using dictionaries."""

__author__ = "730523706"


def invert(given_dict: dict[str, str]) -> dict[str, str]:
    """Given a dictionary invert it so that the new keys are the given values and the new values are the given keys."""
    inverted_dict: dict[str, str] = {}
    for key in given_dict:
        inverted_dict[given_dict[key]] = key
    return inverted_dict


def favorite_color(group: dict[str, str]) -> str:
    """Takes a group of people and their favorite colors and returns the most common favorite color of the group of people."""
    common_color: str = ""
    color_frequency: dict[str, int] = {}
    for name in group:
        if group[name] in color_frequency:
            color_frequency[group[name]] += 1
        else:
            color_frequency[group[name]] = 1
    for color in color_frequency:
        if common_color == "":
            common_color = color
        if color_frequency[color] > color_frequency[common_color]:
            common_color = color
    return common_color


def count(given_list: list[str]) -> dict[str, int]:
    """Create a dictionary that shows(counts) the amount of times each word in the given list shows up."""
    word_frequency: dict[str, int] = {}
    for word in given_list:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency