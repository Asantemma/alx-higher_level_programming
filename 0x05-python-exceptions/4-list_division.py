#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for a in range(list_length):
        try:
            div = my_list_1[a] / my_list_2[a]
        except (ValueError, TypeError):
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            result_list.append(div)
    return result_list
