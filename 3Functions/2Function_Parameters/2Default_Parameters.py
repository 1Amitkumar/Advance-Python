from functools import partial


def add(a=2, b=2, c=2):
    return a + b + c


print(add(3, 3, 3))
print(add(3, 3))
print(add(3))
print(add())
print(add(b=4))
print(add(b=4, c=5))


x = partial(add, c=7, a=2)         # partial parameter
print(x(b=5))