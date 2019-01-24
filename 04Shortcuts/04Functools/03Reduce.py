
from functools import reduce

word = [(45, 'mango'),
         (33, 'apple'),
         (81, 'orange'),
         (126, 'pineapple'),
         (29, 'grapes'),
         (50, 'banana')]


def newline(a, b):
    return a + '\n' + b


def wordformatting(x):
    return "{:>10s}:{:5d}".format(x[1], x[0])


print(reduce(newline, map(wordformatting, word)))
