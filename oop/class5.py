"""
Instance Methods

Instance methods are functions that are defined inside a class and can only be called from an instance of that class. Just like .__init__(), an instance method’s first
 parameter is always self.
"""

class Dog:
    #Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{ self.name } is { self.age } years old"

    #another instance method
    def speak(self,sound):
        return f"{ self.name } say { sound }"


"""
Methods like .__init__() and .__str__() are called dunder methods because they begin and end with double underscores. There are many dunder methods that you can use to customize classes in Python. 
"""
