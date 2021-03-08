class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

"""
Attributes created in .__init__() are called instance attributes. An instance attribute’s value is specific to a particular instance of the class. All Dog objects have a name and an age,
but the values for the name and age attributes will vary depending on the Dog instance.

On the other hand, class attributes are attributes that have the same value
for all class instances. You can define a class attribute by assigning a value to a variable name outside of .__init__().
"""
