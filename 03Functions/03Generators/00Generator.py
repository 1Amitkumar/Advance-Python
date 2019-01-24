def range(start, stop, step=1):
    if stop <= start:
        raise RuntimeError("start must be smaller than stop")
    i = start
    while i < stop:
        yield i
        i += step


try:
    for k in range(100, 500, 30):
        print(k)
except RuntimeError as ex:
    print(ex)
except:
    print("Unknown error occurred")