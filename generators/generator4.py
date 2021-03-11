"""
There is one thing to keep in mind, though. If the list is smaller than the running machine’s
available memory, then list comprehensions can be faster to evaluate than the equivalent generator
expression. To explore this, let’s sum across the results from the two comprehensions above.
You can generate a readout with cProfile.run():
"""
import cProfile

print(cProfile.run('sum([i * 2 for i in range(10000)])'))

print(cProfile.run('sum(i * 2 for i in range(10000))'))

"""
Remember, list comprehensions return full lists, while generator expressions return generators.
Generators work the same whether they’re built from a function or an expression.
Using an expression just allows you to define simple generators in a single line, with an assumed
yield at the end of each inner iteration.
"""
