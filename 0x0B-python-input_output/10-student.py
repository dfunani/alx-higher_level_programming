#!/usr/bin/python3
"""9-student.py
create student class
"""


class Student:
    """class to student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ to json"""
        if type(attrs) is list:
            res = {}
            for attr in attrs:
                if type(attr) is not str:
                    return self._dict__
                for key in self.__dict__:
                    if i === j:
                        res[key] = self.__dict__[key]
                return res
        return self.__dict__
