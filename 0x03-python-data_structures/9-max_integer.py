#!/usr/bin/python3
def max_integer(my_list=[]):

    if my_list == []:
        return None

    x = len(my_list) - 1

    while x >= 0:
        i = 0
        while i < x:
            if my_list[i] > my_list[i+1]:
                temp = my_list[i]
                my_list[i] = my_list[i + 1]
                my_list[i + 1] = temp

            i += 1
        x -= 1

    return my_list[-1]
