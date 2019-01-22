def sqr(x, y):
    return "#" if (x+y) % 2 == 0 else "_"


check = '\n'.join([''.join([sqr(x, y) for x in range(8)]) for y in range(8)])
print(check)
