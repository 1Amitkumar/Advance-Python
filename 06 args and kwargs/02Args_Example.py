def sum(*args):
    s = 0
    for i in args:
        s += i
    print("sum is", s)


sum(1, 2, 3)

sum(1, 2, 3, 4, 5, 7)

sum(1, 2, 3, 4, 5, 7, 8, 9, 10)

sum()