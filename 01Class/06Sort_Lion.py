from pprint import pprint


class Lion:

    def __init__(self, name, paw_size):
        self.name = name
        self.paw_size = paw_size

    def __str__(self):
        return "This is lion {} with a paw of size {})".format(self.name, self.paw_size)

    def __repr__(self):
        return "{:10s} (paw: {})".format(self.name, self.paw_size)

    def __gt__(self, other):
        return self.paw_size < other.paw_size


lions = [
    Lion('mama', 5),
    Lion('baby', 1),
    Lion('grandma', 6),
    Lion('daughter', 4),
    Lion('papa', 7),
    Lion('son', 2),
    Lion('uncle', 5)
]

pprint(lions)

print("\nBiggest lions go first:")
lions.sort()

pprint(lions)

