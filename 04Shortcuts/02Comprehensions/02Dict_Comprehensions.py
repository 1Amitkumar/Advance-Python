from pprint import pprint
from random import randint


sqr = {x: x**2 for x in range(16)}
pprint(sqr)

print('\n', '-' * 38, '\n')

asc_val = {char: ord(char) for char in "Hello"}
pprint(asc_val)
