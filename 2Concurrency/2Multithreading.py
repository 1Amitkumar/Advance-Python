import threading
import time
import random


num = 1


class ThreadOne (threading.Thread):

    def run(self):
        global num
        print('thread ' + str(num) + ' speaking.')
        n = num
        num += 1
        for i in range(20):
            print('thread', n, 'counts', i)
            time.sleep(0.1 * random.randint(1, 10))


for x in range(10):
    ThreadOne().start()

