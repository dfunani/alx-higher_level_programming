#!/usr/bin/python3
"""9-student.py
create student class
"""


class Student:
    """class to student"""
    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def to_json(self):
        """ to json"""
        return self.__dict__
