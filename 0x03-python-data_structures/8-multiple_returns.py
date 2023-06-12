#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        first_ch = None
    else:
        first_ch = sentence[0]

    len_str = len(sentence)
    new_tuple = (len_str, first_ch)

    return new_tuple
