"""
Introduced with PEP 255, generator functions are a special kind of function that return a lazy iterator.
These are objects that you can loop over like a list. However, unlike lists, lazy iterators do not store their contents in memory.
"""
"""
Generator functions look and act just like regular functions, but with one defining characteristic.
Generator functions use the Python yield keyword instead of return.
"""
def infinite_sequence():
    num = 0
    while True:
        yield num
        num +=1

print(infinite_sequence())

"""
You can also define a generator expression (also called a generator comprehension), which has a
very similar syntax to list comprehensions. In this way, you can use the generator without calling a function:
"""
csv_gen = (row for row in (file_name))
