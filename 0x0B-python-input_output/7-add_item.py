#!/usr/bin/python3
"""7-add_item.py
creates a storage of args
"""
import sys
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
try:
    my_list = load_from_json_file(filename)
except Exception:
    my_list = []
[my_list.append(i) for i in sys.argv[1:]]
save_to_json_file(my_list, filename)
