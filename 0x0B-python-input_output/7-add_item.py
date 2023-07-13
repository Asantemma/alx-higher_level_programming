#!/usr/bin/python3
"""
script that adds all args to a python list and saves to a file
"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = 'add_item.json'
my_list = []
try:
    my_list = load_from_json_file(filename)
except Exception:
    save_to_json_file(my_list, filename)

arg_len = len(argv)

if arg_len > 1:
    for x in range(1, arg_len):
        my_list.append(argv[x])

    save_to_json_file(my_list, filename)
