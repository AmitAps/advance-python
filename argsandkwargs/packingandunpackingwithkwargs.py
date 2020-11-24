"""
We can do the packing and unpacking with keyword arguments as well.

But the iterable that is passed as keyword arguments must be a mapping such as a dictionary.
"""

def arg_printer(**kwargs):
	print(kwargs)

dct = {'param1': 5, 'param2':8}
arg_printer(**dct)


"""
If we also pass additional keyword arguments together with a dictionary, they will combined and stored in the kwargs dictionary.
"""
arg_printer(param3=9, **dct)
