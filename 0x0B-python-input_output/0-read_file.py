#!/usr/bin/python3
"""The read_file function"""


def read_file(filename=""):
    """""reads a text file(UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as file:
        file_r = file.read()
        print(file_r, end="")
