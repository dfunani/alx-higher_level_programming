#!/usr/bin/python3
"""2-is_same_class module
creates class
"""


def is_same_class(obj, a_class):
    """checks class"""
    if not obj or not a_class:
        return False
    return a_class is type(obj)
