#!/usr/bin/python3
"""The append text function"""


def append_write(filename="", text=""):
    """appends a string at end of and returns the number of characters added"""
    with open(filename, "a", encoding="utf-8") as file:
        str_a = file.write(text)
        return str_a
