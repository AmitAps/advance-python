def addition(a, b, *args, option=True):
	result = 0
	if option:
		for i in args:
			result += i
		return a + b + result
	else:
		return result

print(addition(1,4,5,6,7))
print(addition(1,4,5,6,7, option=False))
