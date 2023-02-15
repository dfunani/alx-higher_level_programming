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

    @classmethod
    def load_from_file(cls):
        """ load instances """
        try:
            with open(f"{cls.__name__}.json", "r") as file:
                json_string = file.read()
                list_dicts = Base.from_json_string(json_string)
                return [cls.create(**item) for item in list_dicts]
        except:
            return []

    @staticmethod
    def to_json_string(list_dictionaries):
        """ serializes a list of dicts """
        if not list_dictionaries:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        if not list_objs:
            list_objs = []
        with open(f"{cls.__name__}.json", "w") as file:
            file.write(Base.to_json_string(
                [objs.to_dictionary() for objs in list_objs]))

    @classmethod
    def create(cls, **dictionary):
        """ create instance """
        res = cls(1, 1)
        res.x = 0
        res.y = 0
        res.update(**dictionary)
        return res
