#!/usr/bin/python3
"""This module  has a class for rectangule instances.
The module has the class Rectangle.
"""


class Rectangle:
    """class rectangle.
    the class defines the height and width prived
    instance attributes, getter and setter method for each
    area and permiter methods,  __str__ implementation.
    """

    def __init__(self, width=0, height=0):
        if (type(height) != int):
            raise TypeError("height must be an integer")
        elif (height < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
        if (type(width) != int):
            raise TypeError("width must be an integer")
        elif (width < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if (self.height == 0 or self.width == 0):
            return 0
        else:
            return 2 * self.height + 2 * self.width

    def __str__(self):
        if (self.height != 0 and self.width != 0):
            res = ""
            for i in range(self.height):
                for j in range(self.width):
                    res += "#"
                if i == self.height - 1:
                    break
                res += "\n"
            return (res)
        else:
            return ("")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
