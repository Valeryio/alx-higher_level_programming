#!/usr/bin/python3

def multiple_returns(sentence):
    """
        This function returns multiple elements

    Args:
        sentence: the string to analyse

    Returns:
        Length, and first character
    """

    if len(sentence) == 0:
        return 0, None

    return len(sentence), sentence[0]
