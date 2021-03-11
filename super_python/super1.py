
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
    Here, you’ve used super() to call the __init__() of the Rectangle class,
    allowing you to use it in the Square class without repeating code.
    """
    def __init__(self, length):
        super().__init__(length, length)
"""
In this example, Rectangle is the superclass, and Square is the subclass.

Because the Square and Rectangle .__init__() methods are so similar, you can simply call the superclass’s .__init__() method (Rectangle.__init__()) from that of Square by using super(). This sets the .length and .width attributes even though you just had to supply a single length parameter to the Square constructor.

When you run this, even though your Square class doesn’t explicitly implement it, the call to .area() will use the .area() method in the superclass and print 16. The Square class inherited .area() from the Rectangle class.

>>> from super1 import *
>>> square = Square(4)
>>> square.area()
16

"""
