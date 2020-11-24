def arg_printer(a, b, *args):
"""
The first two values are given to a and b. The remaining values are stored in the args tuple.
"""
	print(f'a is {a}')
	print(f'b is {b}')
	print(f'args are{args}')

arg_printer(3, 4, 5, 8, 3)
