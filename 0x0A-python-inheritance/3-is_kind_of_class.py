#!/usr/bin/python3
"""3-is_kind_of_class module
creates a check
"""


def is_kind_of_class(obj, a_class):
    """
    checks kind
    """
    try:
        if not obj or not a_class:
            return False
        return isinstance(obj, a_class)
    except TypeError:
        return False
