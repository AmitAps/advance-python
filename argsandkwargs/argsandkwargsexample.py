def arg_printer(a, b, *args, option=True, **kwargs):
	"""
	We can use both *args and **kwargs in a function but *args must be put before **kwargs.
	"""
	print(a, b)
	print(args)
	print(option)
	print(kwargs)

arg_printer(1, 4, 6, 5, param1=5, param2=6)
