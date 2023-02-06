#!/usr/bin/python3
"""4-inherits_from module
creates a check
"""


def is_kind_of_class(obj, a_class):
    """
    checks kind
    """
    try:
        return isinstance(obj, a_class) and type(obj) != a_class
    except TypeError:
        return False
