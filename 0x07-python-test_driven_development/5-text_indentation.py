#!/usr/bin/python3
"""
Prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :
            text (str): text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for ch in text:
        if ch == "." or ch == "," or ch == "?" or ch == ":":
            print("\n")
        else:
            print(ch, end="")
