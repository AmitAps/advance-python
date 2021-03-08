"""
Parent Classes vs Child Classes
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

"""
Remember, to create a child class, you create new class with its own name and then put the name of the parent class in parentheses.
"""
class JackRussellTerrier(Dog):
    pass
class Dachshund(Dog):
    pass
class Bulldog(Dog):
    pass

"""
To determine which class a given object belongs to, you can use the built-in type():

>>> type(miles)
<class 'class_inheritance1.JackRussellTerrier'>

"""
"""
What if you want to determine if miles is also an instance of the Dog class? You can do this with the built-in isinstance():

>>> isinstance(miles, Dog)
True

Notice that isinstance() takes two arguments, an object and a class.

More generally, all objects created from a child class are instances of the parent class, although they may not be instances of other child classes.
"""
