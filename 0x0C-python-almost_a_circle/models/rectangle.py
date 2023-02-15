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

    def to_dictionary(self):
        """ dictionary rep of the class """
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}

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
        return f"[Rectangle] ({self.id}) {a} - {self.width}/{self.height}"

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
