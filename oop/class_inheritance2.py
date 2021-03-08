"""
Extend the Functionality of a Parent Class
"""

class Dog:
    #Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    #instance method
    def __str__(self):
        return f"{ self.name } is { self.age } years old"

    #another instance method
    # Change the string returned by .speak()
    def speak(self,sound):
        return f"{ self.name } barks: { sound }"


class JackRussellTerrier(Dog):
    """
    Now .speak() is defined on the JackRussellTerrier class with the default argument for sound set to "Arf".
    """
    def speak(self, sound='Arf'):
        return f'{self.name} says {sound}'

class Dachshund(Dog):
    pass
class Bulldog(Dog):
    pass


"""
One thing to keep in mind about class inheritance is that changes to the parent class automatically propagate to child classes.
This occurs as long as the attribute or method being changed isn’t overridden in the child class.
"""
