#Errors and Exceptions
# x = 5
# assert (x>=0), 'x is not positive'

# a = 5 / 0o7
# print(a)

# try:
#     a = 5/0
# except Exception as e:
#     print(f'{e} is not allowed')

try:
    a = 5 / 1
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
