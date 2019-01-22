
import time


def timestmp(func):
    def wrapper(*args):
        result = func(*args)
        print(time.asctime(),'   ', str(result))
        return result

    return wrapper


@timestmp
def add(a, b):
    time.sleep(0.5)
    return a + b


@timestmp
def multi(a, b):
    time.sleep(1)
    return a * b


add(1, 1)
add(3, 4)
multi(3, 4)
add(10, 10)
multi(10, 10)
