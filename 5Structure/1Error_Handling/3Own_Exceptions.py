class NumberError(Exception):
    pass


VALIDINPUT = ["1", "2", "3", "4"]


def gettxt():
    txt = input("input number between 1-4: ")
    if not txt in VALIDINPUT:
        raise NumberError("{} is not a number between 1-4.".format(txt))
    return txt


gettxt()
