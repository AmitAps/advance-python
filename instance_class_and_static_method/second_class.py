class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    # def __repr__(self):
    #     return f'Pizza({self.ingredients!r})'

    def __repr__(self):
    return 'Pizza(%r)' % self.ingredients


"""
>>> Pizza(['cheese','tomotoes'])
Pizza(['cheese', 'tomotoes'])

"""
