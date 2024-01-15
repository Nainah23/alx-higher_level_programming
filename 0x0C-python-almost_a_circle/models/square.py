#!/usr/bin/python3
"""Represents a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """New Square initialization.

        Args:
            size (int): New Square initialization.
            x (int): New Square x coordinate.
            y (int): New Square y coordinate.
            id (int): New Square identity.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get Square size."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Square update.

        Args:
            *args (ints): New attribute values.
              arg1  - id attribute
               arg2 - attribute size
               arg3 - x attribute
               arg4 - y attribute
            **kwargs (dict): New key/value attributes pairs.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return Square dict representation."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the Square str() & print() representation."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
