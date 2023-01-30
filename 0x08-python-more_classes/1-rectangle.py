#!/usr/bin/python3
"""
Rectangle class to serve as an abstraction of a Rectangle
"""


class Rectangle:
    """
    New rectangle can be created
    """
    def __init__(self, height=0, width=0):
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @height.setter
    def height(self, value):
        self.__height = value

    @width.setter
    def width(self, value):
        self.__width = value
