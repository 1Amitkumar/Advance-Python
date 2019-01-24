from functools import reduce

num = [1, 2, 3, 4, 5, 6, 7, 8]


def sqr(x):
    return x ** 2                         # mapping


sqrs = map(sqr, num)
print(sqrs)
print(list(sqrs))


def multi_four(x):
    return x % 4 == 0                        # filtering


multi_four = filter(multi_four, map(sqr, num))
print(multi_four)
print(list(multi_four))


def add(x, y):                            # reducing
    return x + y


print(reduce(add, num))
print(reduce(add, [[1, 2, 3], [4, 5, 6]]))
