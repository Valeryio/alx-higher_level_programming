#!/usr/bin/python3

"""This module has the only one function text indentation
    :param text: A text
"""

def text_indentation(text):
    """
        This function returns prints a text with new line characters
        :return nothing
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < (len(text)):
        if text[i] in ['.', '?', ':']:
            print("{}\n\n".format(text[i]), end="")
            i += 1
        else:
            print("{}".format(text[i]), end="", sep="")
        i+= 1
