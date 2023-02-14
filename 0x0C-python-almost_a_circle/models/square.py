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

    def update(self, *args, **kwargs):
        """ updates the instance attrs """
        if args:
            for arg in range(len(args)):
                if arg == 0:
                    if not args[arg]:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = args[arg]
                if arg == 1:
                    self.width = args[arg]
                if arg == 2:
                    self.height = args[arg]
                if arg == 3:
                    self.x = args[arg]
                if arg == 4:
                    self.y = args[arg]

        elif kwargs:
            for key in kwargs:
                if key == "id":
                    if not kwargs[key]:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = kwargs[key]
                if key == "width":
                    self.width = kwargs[key]
                if key == "height":
                    self.height = kwargs[key]
                if key == "x":
                    self.x = kwargs[key]
                if key == "y":
                    self.y = kwargs[key]

    def __str__(self):
        """ str rep of the rect """
        a = f"{self.x}/{self.y}"
        return f"[Square] ({self.id}) {a} - {self.size}"

    def display(self):
        """ print the rect """
        for i in range(self.height + self.y):
            if i < self.y:
                print()
            else:
                print(" " * self.x, end="")
                print("#" * self.width)
        return None

    def area(self):
        """ area function """
        return self.width * self.height

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
