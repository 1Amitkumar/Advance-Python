class File:

    def __init__(self, func):
        self.function = func

    def __call__(self, *args):
        try:
            self.function(*args)
        except IOError:
            print('I/O error caught')
            print(args)


@File
def risky_fileopen(filename):
    open(filename)
    print('SUCCESS:', filename)


risky_fileopen('2Decorator_Class.py')
risky_fileopen('not exist')

