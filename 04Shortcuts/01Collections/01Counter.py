from random import choice
from pprint import pprint
from collections import Counter


title = [
         "Ravi", "Anupam", "Radha", "Mark",
         "Krish", "Aabha", "Seema", "Ricky"
        ]


data = [choice(title) for i in range(100)]     # it generates 100 random title


cnt = Counter(data)

pprint(cnt)                            # print stands for pretty printer
pprint(cnt.most_common(3))
print(cnt['Aabha'])