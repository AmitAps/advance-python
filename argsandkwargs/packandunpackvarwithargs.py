def arg_printer(*args):
   print(args)


lst = [1, 4, 5]
"""
If we pass a list to the function above, it will stored in args tuple as one single element.
"""
arg_printer(lst)

"""
If we put an asterisk before lst, the values in the list will be unpacked and stored in args tuple separately.
"""
arg_printer(*lst)

"""
We can pass multiple iterables to be unpacked together with single elements. All values will be stored in the args tuple.
"""

tpl = ('a','b',4)
arg_printer(*lst, *tpl, 5, 6)

