def count():
    n = 1
    while n < 1000:
        yield n
        n *= 2


gen = count()

for num in gen:
    print(num)
