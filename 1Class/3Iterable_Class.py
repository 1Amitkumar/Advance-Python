class Series:

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib_series = self.a
        if fib_series > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib_series


for i in Series(10):
    print(i)