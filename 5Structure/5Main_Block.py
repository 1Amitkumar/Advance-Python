def input_name():
    title = input('enter your name: ')
    return title


def addmsg(title):
    msg = "Good morning, %s! Nice to see you."%title
    return msg


def showmsg(msg):
    print(msg)

####################################
# main program:


if __name__ == '__main__':
    name = input_name()
    msg = addmsg(name)
    showmsg(msg)
