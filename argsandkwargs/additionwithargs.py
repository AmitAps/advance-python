def addition(*args):
	"""
	*args allow a function to take any number of positional arguments.
	"""
	result = 0
	for i in args:
		result = result + i
	return result

print(addition())
print(addition(1,4))
print(addition(1,7,3))

