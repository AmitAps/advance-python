"""
**kwargs allow a function to take any number of keyword arguments.

By default, **kwargs is an empty dictionary. Each undefined keyword argument is stored as a key-value pair in the **kwargs dictionary.
"""
def arg_printer(a, b, option=True, **kwargs):
	print(a, b)
	print(option)
	print(kwargs)

arg_printer(3, 4, param1=5, param2=6)
