word = [(45, 'mango'),
         (33, 'apple'),
         (81, 'orange'),
         (126, 'pineapple'),
         (29, 'grapes'),
         (50, 'banana')]


def bars(data):

    g = iter(data)
    while 1:
        yield next(g)
        yield next(g)
        print('-' * 16)
        

for x in bars(word):
    print("%-10s:%5i" % (x[1], x[0]))

