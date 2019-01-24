from pprint import pprint
from collections import OrderedDict

title = [
         "Ravi", "Anupam", "Radha", "Mark",
         "Krish", "Aabha", "Seema", "Ricky"
        ]

od = OrderedDict()

for i, name in enumerate(title):
    od[i] = name

pprint(od)
od.move_to_end(2)
pprint(od)
