#!/usr/bin/python3
"""
Rectangle module
creates a rect class from Base class
"""
from models.base import Base


class Rectangle(Base):
    """ rect class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ constr class and inherit from base """
        super().__init__(id)
        if Rectangle.c_type(width, "w") and Rectangle.c_val(width, "w"):
            self.__width = width
        if Rectangle.c_type(height, "h") and Rectangle.c_val(height, "h"):
            self.__height = height
        if Rectangle.c_type(x, "x") and Rectangle.c_val(x, "x"):
            self.__x = x
        if Rectangle.c_type(y, "y") and Rectangle.c_val(y, "y"):
            self.__y = y

    def display(self):
        """ print the rect """
        for i in range(self.height):
            print("#" * self.width)
        return None
            
    def area(self):
        """ area function """
        return self.width * self.height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, val):
        if Rectangle.c_type(val, "w") and Rectangle.c_val(val, "w"):
            self.__width = val

    @height.setter
    def height(self, val):
        if Rectangle.c_type(val, "h") and Rectangle.c_val(val, "h"):
            self.__height = val

    @x.setter
    def x(self, val):
        if Rectangle.c_type(val, "x") and Rectangle.c_val(val, "x"):
            self.__x = val

    @y.setter
    def y(self, val):
        if Rectangle.c_type(val, "y") and Rectangle.c_val(val, "y"):
            self.__y = val

    @staticmethod
    def c_type(val, attr):
        if attr == "h":
            attr = "height"
        if attr == "w":
            attr = "width"
        if type(val) is int:
            return True
        raise TypeError(f"{attr} must be an integer")

    @staticmethod
    def c_val(val, attr):
        if attr == "w":
            attr = "width"
        if attr == "h":
            attr = "height"
        if val <= 0 and (attr == "width" or attr == "height"):
            raise ValueError(f"{attr} must be > 0")
        if val < 0 and (attr == "x" or attr == "y"):
            raise ValueError(f"{attr} must be >= 0")
        return True
