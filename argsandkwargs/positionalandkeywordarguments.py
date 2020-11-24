"""
    Positional arguments are declared by a name only.
    Keyword arguments are declared by a name and a default value.

When a function is called, values for positional arguments must be given. Otherwise, we will get an error.

If we do not specify the value for a keyword argument, it takes the default value.
"""
def addition(a, b=2): #a is positional, b is keyword argument
	return a + b

print(addition(1))

def addition(a,b): #a and b are positional arguments
	return a + b

print(addition(1, 3))
print(addition(2))
