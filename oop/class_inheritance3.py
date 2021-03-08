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
    You can access the parent class from inside a method of a child class by using super():
    """
    def speak(self, sound='Arf'):
        return super().speak(sound)

class Dachshund(Dog):
    pass
class Bulldog(Dog):
    pass


"""
When you call super().speak(sound) inside JackRussellTerrier, Python searches the parent class,
Dog, for a .speak() method and calls it with the variable sound.
"""
