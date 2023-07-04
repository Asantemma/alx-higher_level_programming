#!/usr/bin/python3
"""
    5-text_indentation Module
"""


def text_indentation(text):
    """
        Prints a text with 2 new lines after each of this characters
        '.', '?', and ':'

        Args:
            text: text to print
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':']
    new_text = []
    current_line = ""

    for character in text:
        if character in punctuation:
            new_text.append(current_line.strip())
            new_text.append("")
            new_text.append("")
            current_line = ""
        else:
            current_line += character

    new_text.append(current_line.strip())

    for line in new_text:
        print(line)
