#!/usr/bin/env python3
def no_c(my_string):
    no_c_string = ""

    for char in enumerate(my_string):
        if char != 'c' and char != 'C':
            no_c_string += char

    return no_c_string
