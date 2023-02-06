#!/usr/bin/python3
"""2-is_same_class module
creates class
"""


def is_same_class(obj, a_class):
    """checks class"""
    if not obj:
        return False
    if not a_class:
        return False
    return obj is a_class
