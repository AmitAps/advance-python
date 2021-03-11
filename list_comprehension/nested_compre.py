cities = ['Austin', 'Tacoma', 'Topeka', 'Sacramento', 'Charlotte']
temps = {city: [0 for _ in range(7)] for city in cities}
print(temps)

"""
You create the outer collection temps with a dictionary comprehension. The expression is a key-value pair, which contains yet another comprehension. This code will quickly generate a list of data for each city in cities.
"""
matrix = [[i for i in range(5)] for _ in range(6)]
print(matrix)
"""
The outer list comprehension [... for _ in range(6)] creates six rows, while the inner list comprehension [i for i in range(5)] fills each of these rows with values.
"""

##################################################
matrix = [
    [0, 0, 0],
    [1, 1, 1],
    [2, 2, 2],
]

flat = [num for row in matrix for num in row]
print(flat)
