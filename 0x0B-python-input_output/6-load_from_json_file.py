#!/usr/bin/python3
"""load_from_json_file
creates ile readers and writers
"""
import json


def load_from_json_file(filename):
    """ File Reader """
    with open(filename, "r") as file:
        return json.load(file)
