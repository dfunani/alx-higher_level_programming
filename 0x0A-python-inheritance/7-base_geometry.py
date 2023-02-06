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
            raise ValueError("{name} must be greater than 0")
