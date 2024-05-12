#!/usr/bin/python3
"""A function that prints a text and 2 new lines
after every . ? or :"""


def text_indentation(text):
    """Prints the text until it encounters . ? : and allow 2 new lines"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for idx, w in enumerate(text):
        if (w == "." or w == "?" or w == ":"):
            print()
        elif text[idx] == " " and (text[idx - 1] == "." or text[idx - 1] == "?"\
                or text[idx - 1] == ":"):
            print()
        else:
            print(text[idx], end="")
