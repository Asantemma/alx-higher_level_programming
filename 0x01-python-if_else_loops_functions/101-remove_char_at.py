#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    count = 0
    str_copy = ""
    for character in str:
        if count == n:
            count = count + 1
            continue
        str_copy += str[count]
        count = count + 1
    return str_copy
