name = 'amitpratapsingh fbsehfbahhbfaiu'
vol = 'aeiou'
vowels = [vl for vl in name if vl in vol]
print(set(vowels))

# sentence = 'the rocket came back from mars'
# vowels = [i for i in sentence if i in 'aeiou']
# print(vowels)

"""
new_list = [expression for member in iterable (if conditional)]

Here, your conditional statement comes just before the closing bracket.

Conditionals are important because they allow list comprehensions to filter out unwanted values, which would normally require a call to filter():
"""
