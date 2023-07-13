#!/usr/bin/python3
"""The write_file function"""


def write_file(filename="", text=""):
    """writes a string to a text file.
        Args:
            filename (str): name of file.
            text (str): text to be written.
            Return: the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as file:
        file_w = file.write(text)
        return (file_w)
