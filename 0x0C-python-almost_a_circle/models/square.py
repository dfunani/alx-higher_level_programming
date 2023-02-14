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

    def __str__(self):
        """ str rep of the rect """
        a = f"{self.x}/{self.y}"
        return f"[Square] ({self.id}) {a} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        if check_t(val, "size") and check_v(val, "size"):
            self.width = val
            self.height = val

    @staticmethod
    def check_t(val, attr):
        if type(val) is int:
            return True
        raise TypeError(f"{attr} must be an integer")

    @staticmethod
    def check_v(val, attr):
        if val <= 0 and attr == "size":
            raise ValueError(f"{attr} must be > 0")
        return True
