squares = [i * i for i in range(10) if i%2 ==0]
print(squares)

name = ['amit','singh','aps', 'apssingh']
names = [name[n] for n in range(len(name)) if len(name[n]) > 3 ]
# for i in range(len(name)):
#     if len(name[i]) > 4:
#         print(name[i])
print(names)

"""
new_list = [expression for member in iterable]

Every list comprehension in Python includes three elements:

    expression is the member itself, a call to a method, or any other valid expression that returns a value. In the example above, the expression i * i is the square of the member value.

    member is the object or value in the list or iterable. In the example above, the member value is i.

    iterable is a list, set, sequence, generator, or any other object that can return its elements one at a time. In the example above, the iterable is range(10).

"""
