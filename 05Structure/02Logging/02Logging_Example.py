import logging
import sys

logging.basicConfig(filename='debug.log', level=logging.CRITICAL)  # change the value of 'level' to
                                                               # DEBUG, ERROR, WARNING, INFO and CRITICAL
                                                               # and check the debug.log file


def factorial(n=10):

    i = 1
    factorial = 1
    while i < n:
        logging.info('starting iteration {}'.format(i))
        factorial *= i
        logging.debug('new factorial: {}'.format(factorial))
        i += 1

    logging.warning('Final result: {}'.format(factorial))
        

if __name__ == '__main__':
    logging.warning('warning message')
    logging.info('info message')
    factorial(10)
    logging.critical('Factorial ended')


l1 = logging.getLogger('ex1')
l1.addHandler(logging.FileHandler('debug2.log', mode='w'))
l1.setLevel(logging.DEBUG)
l1.info('got spam')

l2 = logging.getLogger('ex2')
handler = logging.StreamHandler(sys.stderr)
l2.addHandler(handler)
fmt='%(asctime)s %(message)s'
handler.setFormatter(logging.Formatter(fmt, datefmt='%m/%d/%Y %I:%M:%S %p'))
l2.setLevel(logging.WARNING)
l2.warning('got spam spam spam')
