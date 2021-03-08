import contextlib
@contextlib.contextmanager

def read_only(path_to_file):
    file = open(path_to_file,'r')
    yield file
    file.close()

with read_only('sample.txt') as file:
    print('Printing the contents of the file\n')
    print(file.read())
