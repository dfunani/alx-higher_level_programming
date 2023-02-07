#!/usr/bin/python3
"""to_json_string
creates ile readers and writers
"""
import json


def to_json_string(my_obj):
    """ File Reader """
    return json.dumps(my_obj)
