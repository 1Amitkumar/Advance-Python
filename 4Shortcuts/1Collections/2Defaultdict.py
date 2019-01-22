from random import choice, randint
from pprint import pprint
from collections import defaultdict


title = [
         "Ravi", "Anupam", "Radha", "Mark",
         "Krish", "Aabha", "Seema", "Ricky"
        ]


d = defaultdict(int)          # dict initialization

for i in range(100):
    key = choice(title)
    d[key] += 1

pprint(d)


d = defaultdict(list)    # dict initialization with empty list

for key in title:
    for i in range(3):
        d[key].append(randint(1, 10))

pprint(d)
