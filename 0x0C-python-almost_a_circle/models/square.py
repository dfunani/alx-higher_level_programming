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

    def update(self, *args, **kwargs):
        """ updates the instance attrs """
        if args:
            for arg in range(len(args)):
                if arg == 0:
                    if not args[arg]:
                        self.__init__(self.size, self.size, self.x, self.y)
                    else:
                        self.id = args[arg]
                if arg == 1:
                    self.width = args[arg]
                    self.height = args[arg]
                if arg == 2:
                    self.x = args[arg]
                if arg == 3:
                    self.y = args[arg]

        elif kwargs:
            for key in kwargs:
                if key == "id":
                    if not kwargs[key]:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = kwargs[key]
                if key == "size":
                    self.width = kwargs[key]
                    self.height = kwargs[key]
                if key == "x":
                    self.x = kwargs[key]
                if key == "y":
                    self.y = kwargs[key]

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        if Rectangle.c_type(val, "w") and Rectangle.c_val(val, "w"):
            self.width = val
            self.height = val
