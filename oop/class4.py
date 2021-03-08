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

    #instance method
    def description(self):
        return f"{ self.name } is { self.age } years old"

    #another instance method
    def speak(self,sound):
        return f"{ self.name } say { sound }"
