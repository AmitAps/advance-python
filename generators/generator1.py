"""
Building Generators With Generator Expressions
"""
nums_squared_lc = [num ** 2 for num in range(5)] #list comprehension
nums_squared_gc = (num ** 2 for num in range(5)) #generator expression

print(nums_squared_lc)
print(nums_squared_gc)
