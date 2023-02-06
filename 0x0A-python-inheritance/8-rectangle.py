#!/usr/bin/python3
"""5-base_geometry module
create class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Creates a rect class"""
    def __init__(self, width, height):
        """ Init vclass"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width
