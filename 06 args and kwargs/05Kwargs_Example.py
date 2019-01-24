def threearg(a, b, c):
    print(a, b, c)


a = {'a': "one", 'b': "two", 'c': "three"}
threearg(**a)