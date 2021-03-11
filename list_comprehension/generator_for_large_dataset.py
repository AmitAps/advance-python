"""
When the size of a list becomes problematic, it’s often helpful to use a generator instead of a
list comprehension in Python. A generator doesn’t create a single, large data structure in memory,
but instead returns an iterable. Your code can ask for the next value from the iterable as many times as necessary or until you’ve reached the end of your sequence, while only storing a single value at a time.
"""

print(sum([i * i for i in range(1000)]))
##########################################
print(sum(map(lambda i: i*i, range(1000000000))))
"""
map() also operates lazily, meaning memory won’t be an issue if you choose to use it in this case:
"""
#################################################
