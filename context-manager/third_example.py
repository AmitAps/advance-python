import time
import contextlib
@contextlib.contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print(f'This code block executed in { end - start } seconds.')

with timer():
    for i in range(10):
        time.sleep(0.1)
print('Done!')

"""
Python starts the timer whenever the interprets sees with timer(): and ends it (executes yield and what comes after) as soon as a new unindented statement is written (print('Done!'))
"""
