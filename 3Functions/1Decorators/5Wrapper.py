import time
from functools import wraps


def timestmp(func):

    def wrapper(*args):
        result = func(*args)
        print(time.asctime(), '   ', str(result))
        return result

    return wrapper


@timestmp
def add(a, b):

    return a + b


add(1, 1)
add(3, 4)

print("name of the function:", add.__name__)
print("documentation string:", add.__doc__)
