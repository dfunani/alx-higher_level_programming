#!/usr/bin/python3
"""base
create a base class for inheritence by higher order classes
"""
import json


class Base:
    """
    Base class: Parent Class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor: creates the instance
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ serializes a list of dicts """
        if not list_dictionaries:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if not list_objs:
            list_objs = []
        with open(f"{cls.__name__}.json", "w") as file:
            file.write(Base.to_json_string(
                [objs.to_dictionary() for objs in list_objs]))
