import contextlib
@contextlib.contextmanager
def my_context():
    print('Welcome!')
    yield
    print('Bye!')

"""
We created a very simple context manager that prints Welcome whenever we open the context and as soon as we are outside the context, prints Bye.
"""

with my_context():
    print('I am always excuted before the yield keyword!')
print('I am always excuted after the yield keyword!')
