from random import randint

num = [randint(1, 1000) for i in range(100000)]


sqr = []
for x in num:
    sqr.append(x ** 2)
print(sqr)