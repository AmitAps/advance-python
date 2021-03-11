"""
Understanding the Python Yield Statement.
"""

def multi_yield():
    yield_str = "This will print the first string"
    yield yield_str
    yield_str = "This will print the second string"
    yield yield_str

multi_obj = iter(multi_yield())
while True:
    try:
        prt = next(multi_obj)
        print(prt)
    except StopIteration:
        break

# print(next(multi_obj))
#
# print(next(multi_obj))
# print(next(multi_obj))

"""
Take a closer look at that last call to next(). You can see that execution has blown up with a
traceback. This is because generators, like all iterators, can be exhausted. Unless your
generator is infinite, you can iterate through it one time only. Once all values have been
evaluated, iteration will stop and the for loop will exit. If you used next(),
then instead you’ll get an explicit StopIteration exception.
"""
