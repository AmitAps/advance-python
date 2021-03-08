"""
Creating a new object from a class is called instantiating an object. You can instantiate a new Dog object by typing the name of the class,
 followed by opening and closing parentheses:
"""



class Dog:
    pass

Dog()
<__main__.Dog object at 0x7f15b6f26cd0>

>>> Dog()
<__main__.Dog object at 0x7f8bf1ac6cd0>
>>> Dog()
<__main__.Dog object at 0x7f8bf1917eb0>


"""
The new Dog instance is located at a different memory address. That’s because it’s an entirely new instance and is completely unique from the
first Dog object that you instantiated
"""
