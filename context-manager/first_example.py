with open('sample.txt', 'w') as file:
    file.write("Hello World!\n")

"""
How To Create a Custom Context Manager

There are two ways to build user-defined context-managers:

    class-based
    function-based



    In this method, there are 5 steps to implement your own context-managers:

    Define a function.
    (optional) Write any setup code your context needs.
    Use the yield keyword.
    (optional) Write any teardown code your context needs.
    Add the @contextlib.contextmanager decorator.
"""
