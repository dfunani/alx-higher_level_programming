#!/usr/bin/python3
"""5-save_to_json_file.py
creates ile readers and writers
"""
import json


def save_to_json_file(my_obj, filename):
    """ File Reader """
    with open(filename, "w") as file:
        return json.dump(my_obj, file)
