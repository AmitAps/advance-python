#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 09:25:55 2020

@author: aps
"""

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        
 # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
"""
Remember, to create a child class, you create new class with its own name and then put the name of the parent 
class in parentheses. 
"""

class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass
