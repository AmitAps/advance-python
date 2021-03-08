class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    # def __repr__(self):
    #     return f'Pizza({self.ingredients!r})'

    def __repr__(self):
        return 'Pizza(%r)' % self.ingredients

    @classmethod
    def margherita(cls):
        return cls(['mozzarella','tomotoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella','tomotoes','ham'])

"""
>>> from third_class import *
>>> Pizza.margherita()
Pizza(['mozzarella', 'tomotoes'])
>>> Pizza.prosciutto()
Pizza(['mozzarella', 'tomotoes', 'ham'])

"""

"""
Python only allows one __init__ method per class. Using class methods it’s possible to add as many alternative constructors as necessary.
"""
