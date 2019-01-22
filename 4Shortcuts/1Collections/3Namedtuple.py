from collections import namedtuple


Animalia = namedtuple('Animal', ('title', 'legs', 'eggs', 'extinction'))


Species = [
    Animalia('xyz', 0, 'no info', False),
    Animalia('Chicken', 2, True, False),
    Animalia('Cow', 4, True, False),
    Animalia('Monkey', 2, False, False),
    Animalia('T-Rex', 2, True, True),
    Animalia('Shark', 0, False, False),
]


print('Animalia with 2 legs:')
for animals in Species:
    if animals.legs == 2:
        eggs = "lays eggs" if animals.eggs else "gives live birth"
        extinct = " and is extinct" if animals.extinction else ""
        print("{:>20s} {}{}.".format(animals.title, eggs, extinct))
