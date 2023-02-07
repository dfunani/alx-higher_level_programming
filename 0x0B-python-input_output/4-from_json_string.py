#!/usr/bin/python3
"""4-from_json_string.py
creates ile readers and writers
"""
import json


def from_json_string(my_str):
    """ File Reader """
    return json.loads(my_str)
