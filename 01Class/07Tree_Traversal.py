class Tail:

    def __init__(self, *args):
        self.subtails = args

    def traverse(self):
        result = []
        for n in self.subtails:
            result += n.traverse()
        return result


class Head:

    def __init__(self, name):
        self.value = name

    def traverse(self):
        return [self.value]


tree = Tail(
            Tail(
                Tail(
                    Head('gorilla'),
                    Tail(
                        Head('chimp'), Head('human')
                        )
                    ),
                Tail(
                    Head('cat'), Head('dog')
                    ),
                ),
            Tail(
                Tail(
                    Head('chicken'),
                    Tail(
                        Head('lizard'), Head('turtle')
                        ),
                    ),
                Tail(
                    Head('shark')
                    ),
                )
            )

print(tree.traverse())
