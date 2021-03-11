"""
A set comprehension is almost exactly the same as a list comprehension in Python.
The difference is that set comprehensions make sure the output contains no duplicates. You can create a set comprehension by using curly braces instead of brackets:
"""
quote = "life, uh, finds a way"
unique_vowels = {i for i in quote if i in 'aeiou'}
print(unique_vowels)

"""
Your set comprehension outputs all the unique vowels it found in quote. Unlike lists, sets don’t guarantee that items will be saved in any particular order
"""
