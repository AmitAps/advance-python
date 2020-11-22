#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 05:48:57 2020

@author: aps
"""

"""
 In addition to single inheritance, Python supports multiple inheritance, in which a subclass can inherit 
 from multiple superclasses that don’t necessarily inherit from each other (also known as sibling classes). 
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
        
        
        
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# class RightPyramid(Triangle, Square):
#     def __init__(self, base, slant_height):
#         self.base = base
#         self.slant_height = slant_height

#     def area(self):
#         base_area = super().area()
#         perimeter = super().perimeter()
#         return 0.5 * perimeter * self.slant_height + base_area



"""
Method Resolution Order

The method resolution order (or MRO) tells Python how to search for inherited methods. This comes in handy when
you’re using super() because the MRO tells you exactly where Python will look for a method you’re calling with super() and in what order.

Every class has an .__mro__ attribute that allows us to inspect the order, so let’s do that:
    
    >>> RightPyramid.__mro__
(<class '__main__.RightPyramid'>, <class '__main__.Triangle'>, 
 <class '__main__.Square'>, <class '__main__.Rectangle'>, 
 <class 'object'>)


This tells us that methods will be searched first in Rightpyramid, then in Triangle, then in Square, then Rectangle, 
and then, if nothing is found, in object, from which all classes originate.

Luckily, you have some control over how the MRO is constructed. Just by changing the signature of the RightPyramid class, you can search in the order you want, and the methods will resolve correctly:
"""

class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(self.base)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area
