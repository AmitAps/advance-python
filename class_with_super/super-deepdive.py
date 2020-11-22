#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 05:20:39 2020

@author: aps
"""

"""
super() can also take two parameters: the first is the subclass, and the second parameter is 
an object that is an instance of that subclass.
"""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)

"""
In Python 3, the super(Square, self) call is equivalent to the parameterless super() call.
The first parameter refers to the subclass Square, while the second parameter refers to a Square object which, 
in this case, is self.
"""

class Cube(Square):
    def surface_area(self):
        face_area = super(Square, self).area()
        return face_area * 6

    def volume(self):
        face_area = super(Square, self).area()
        return face_area * self.length

"""
In this example, you are setting Square as the subclass argument to super(), instead of Cube. This causes super() 
to start searching for a matching method (in this case, .area()) at one level above Square in the instance hierarchy, in this case Rectangle.

In this specific example, the behavior doesn’t change. But imagine that Square also implemented an .area() 
function that you wanted to make sure Cube did not use. Calling super() in this way allows you to do that.
"""

"""
Technically, super() doesn’t return a method. It returns a proxy object. This is an object that delegates calls to the correct class methods without making an additional object in order to do so. 
"""
