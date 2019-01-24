from random import randint


num = [randint(1, 10) for x in range(12)]


odd = lambda x: x % 2
even = lambda x: not odd(x)


print([x for x in num if odd(x)])
print([x for x in num if even(x)])
