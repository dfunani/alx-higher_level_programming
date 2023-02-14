#!/usr/bin/python3
"""
Square module
creates a square of type rect class from Base class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ rect class """

    def __init__(self, size, x=0, y=0, id=None):
        """ constr class and inherit from base """
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        """ str rep of the rect """
        a = f"{self.x}/{self.y}"
        return f"[Square] ({self.id}) {a} - {self.size}"
