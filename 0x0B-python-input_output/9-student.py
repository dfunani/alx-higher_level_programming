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

    def __dict__():
        return json.dumps{f"'first_name': '{first_name}', 'last_name': '{last_name}', 'age': '{age}'"}
