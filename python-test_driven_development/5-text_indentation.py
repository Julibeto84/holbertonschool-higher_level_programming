#!/usr/bin/python3
"""
    Text indentation:
    Module that idents a text
"""


def text_indentation(text):
    """ text_identation - Idents a text by adding 2 new lines after chars (.?:)

        Arguments:
            text (str): text to ident
    """
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    i = 0
    chars = ".?:"
    while (i < len(text)):
        if text[i] in chars:
            print(text[i], end="\n\n")
            if i < (len(text) - 1) and text[i + 1] == " ":
                i += 2
            else:
                i += 1
        else:
            print(text[i], end="")
            i += 1
