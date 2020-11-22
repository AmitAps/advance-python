#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 07:36:41 2020

@author: aps
"""

"""
A mixin works as a kind of inheritance, but instead of defining an “is-a” relationship it may be more accurate 
to say that it defines an “includes-a” relationship. With a mix-in you can write a behavior that can be directly included in any number of other classes.
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

class VolumeMixin:
    def volume(self):
        return self.area() * self.height

class Cube(VolumeMixin, Square):
    """
    In this example, the code was reworked to include a mixin called VolumeMixin. The mixin is then used by Cube and gives Cube the ability to calculate its volume, 
    """
    def __init__(self, length):
        super().__init__(length)
        self.height = length

    def face_area(self):
        return super().area()

    def surface_area(self):
        return super().area() * 6


"""
>>> cube = Cube(2)
>>> cube.surface_area()
24
>>> cube.volume()
8

"""

"""
This mixin can be used the same way in any other class that has an area defined for it and for which the formula area * height returns the correct volume.
"""
"""
 RightPyramid.__mro__
 to analyze and correct MRO
 """