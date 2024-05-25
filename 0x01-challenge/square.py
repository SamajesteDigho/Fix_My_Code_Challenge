#!/usr/bin/python3
"""
In this module, we typically manage Squares
"""


class square():
    """ Here the class for Squares """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Square initialissation procedure """
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    @property
    def width(self):
        """ Return width value """
        return self.width
    
    @width.setter
    def width(self, value):
        """ Set the width value """
        self.width = value
    
    @property
    def height(self):
        """ Return height value """
        return self.height
    
    @height.setter
    def height(self, value):
        """ Set the height value """
        self.height = value

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Here for sure we manage the square perimeter """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Getting the str representation of a square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
