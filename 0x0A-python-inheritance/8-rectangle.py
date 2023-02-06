#!/usr/bin/python3
"""5-base_geometry module
create class
"""


class BaseGeometry:
    """ Creates a base class"""

    def area(self):
        """ raises Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return value


class Rectangle(BaseGeometry):
    """ Creates a rect class"""
    def __init__(self, width, height):
        """ Init vclass"""
        if integer_validator("width", width):
            self.width = width
        if integer_validator("height", height):
            self.height = height
