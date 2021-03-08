class Dog:
    #class attribute
    species = 'Canis familiaris'

    def __init__(self, name, age):
        self.name = name
        self.age = age

"""
Use class attributes to define properties that should have the same value for every class instance. Use instance attributes for properties that vary from one
instance to another.
"""
