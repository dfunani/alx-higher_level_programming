#!/usr/bin/python3
"""1-write_file.py
creates ile readers and writers
"""


def write_file(filename="", text=""):
    """ File Reader """
    with open(filename, "w") as file:
        return file.write(text)
