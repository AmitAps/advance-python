#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 04:56:12 2020

@author: aps
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    """
    Here, you’ve used super() to call the __init__() of the Rectangle class, allowing you to use it in the Square class without repeating code. 
   
   Because the Square and Rectangle .__init__() methods are so similar, you can simply call the superclass’s .__init__() method (Rectangle.__init__()) from that of Square by using super(). 
   """
    def __init__(self, length):
        super().__init__(length, length)

class Cube(Square):
    """
    Note that in our example above, super() alone won’t make the method calls for you: you have to call the method on the proxy object itself.
    """
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length
    
"""
Here you have implemented two methods for the Cube class: .surface_area() and .volume(). Both of these calculations rely on calculating the area of a single face,
so rather than reimplementing the area calculation, you use super() to extend the area calculation.

Also notice that the Cube class definition does not have an .__init__(). Because Cube inherits from Square and .__init__() doesn’t really do anything differently for Cube than it already does for Square, you can skip defining it, and the .__init__() of the superclass (Square) will be called automatically.

super() returns a delegate object to a parent class, so you call the method you want directly on it: super().area(). 
"""

