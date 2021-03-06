"""
Calling the previously built methods with super() saves you from needing to rewrite those
methods in your subclass, and allows you to swap out superclasses with minimal code changes.


Inheritance is a concept in object-oriented programming in which a class derives (or inherits)
attributes and behaviors from another class without needing to implement them again.
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length
