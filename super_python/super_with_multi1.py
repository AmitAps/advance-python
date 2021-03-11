"""
Python supports multiple inheritance, in which a subclass can inherit from multiple superclasses
that don’t necessarily inherit from each other (also known as sibling classes).
"""
from super3 import *

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height



class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(self.base)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

"""
Method Resolution Order

The method resolution order (or MRO) tells Python how to search for inherited methods.
This comes in handy when you’re using super() because the MRO tells you exactly where Python will look for a method you’re calling with super() and in what order.
"""

"""
Every class has an .__mro__ attribute that allows us to inspect the order, so let’s do that:

>>> RightPyramid.__mro__
(<class 'super_with_multi0.RightPyramid'>, <class 'super_with_multi0.Triangle'>, <class 'super3.Square'>, <class 'super3.Rectangle'>, <class 'object'>)

This tells us that methods will be searched first in Rightpyramid, then in Triangle, then in Square,
then Rectangle, and then, if nothing is found, in object, from which all classes originate.
"""
