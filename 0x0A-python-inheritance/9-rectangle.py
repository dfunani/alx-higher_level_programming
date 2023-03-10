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

    def area(self):
        """ Extends area method"""
        return self.__height * self.__width

    def __str__(self):
        """ prints rect"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        """ prints rect"""
        return f"[Rectangle] {self.__width}/{self.__height}"
