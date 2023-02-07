#!/usr/bin/python3
"""2-append_write.py
creates ile readers and writers
"""


def append_write(filename="", text=""):
    """ File Reader """
    with open(filename, "a") as file:
        return file.write(text)
