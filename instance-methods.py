#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 08:59:58 2020

@author: aps
"""

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # # Instance method
    # def description(self):
    #     return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

    def __str__(self):
        return f"{self.name} is {self.age} years old"

"""
Methods like .__init__() and .__str__() are called dunder methods because they begin and end with double underscores.
There are many dunder methods that you can use to customize classes in Python.
"""