"""
Inheritance is the process by which one class takes on the attributes and methods of another. Newly formed classes are called child classes, and the classes that child classes
are derived from are called parent classes.


Child classes can override or extend the attributes and methods of parent classes. In other words, child classes inherit all of the parent’s attributes and methods but can also specify attributes and methods
that are unique to themselves.
"""

class Dog:
    species = 'Canis familiaris'

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{ self.name } is { self.age } years old"

    #another instance method
    def speak(self,sound):
        return f"{ self.name } say { sound }"
