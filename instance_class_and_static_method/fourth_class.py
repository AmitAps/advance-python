import math

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi


"""
Flagging a method as a static method is not just a hint that a method won’t modify class or instance state — this restriction is also enforced by the Python runtime.



    Instance methods need a class instance and can access the instance through self.
    Class methods don’t need a class instance. They can’t access the instance (self) but they have access to the class itself via cls.
    Static methods don’t have access to cls or self. They work like regular functions but belong to the class’s namespace.
    Static and class methods communicate and (to a certain degree) enforce developer intent about class design. This can have maintenance benefits.

"""
