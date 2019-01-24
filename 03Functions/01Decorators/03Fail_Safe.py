

class File:
    def __init__(self, func):
        self.function = func

    def __call__(self, *args):
        try:
            self.function(*args)
        except IOError:
            print('An I/O caught when opening file "{}"'.format(args[0]))


@File
def risky_fileopen(filename):
    open(filename)
    print('SUCCESS:', filename)


risky_fileopen('3Fail_Safe.py')
risky_fileopen('doesnotexist')

