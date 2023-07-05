#!/usr/bin/python3
"""This module defines a function called text_indentation

See function docs for more details
"""


def text_indentation(text=None):
    """This function adds 2 new lines after every '.', '?' and ':'

    Args:
        text (str): The text to be printed
    Returns:
        None
    Raises
        ValueError: When text is not a string
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    text = text.replace('.', '.\n\n').replace('?', '?\n\n').replace(':',
                                                                    ':\n\n')
    lines = text.split('\n\n')
    print('\n\n'.join([line.strip() for line in lines]), end='')
