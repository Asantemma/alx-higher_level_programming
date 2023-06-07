#!/usr/bin/python3
x = 122
while x >= 97:
    if x % 2 == 0:
        print("{}".format(chr(x)), end="")
    else:
        print("{}".format(chr(x - 32)), end="")
    x = x - 1
