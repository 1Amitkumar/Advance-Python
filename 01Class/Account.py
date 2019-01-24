
class BankAccount:

    prefix = 'SBI'

    def __init__(self, newname, balance=0):
        self.name = newname
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        self.balance -= amt

    def __str__(self):
        return "{} | {:10s}:{:10.2f}".format(self.prefix, self.name, self.balance)

    @staticmethod
    def info_text():

        return """Bank account keeps your money safe."""

    @classmethod
    def prefix_text(cls):

        return """Bank account has the prefix: {}.""".format(cls.prefix)


if __name__ == '__main__':
    a = BankAccount('Ram', 1000)
    print(a)

    a.deposit(500)
    print(a)

    a.withdraw(100)
    print(a)

    print(a.info_text())
    print(a.prefix_text())

    print(BankAccount.info_text())
    print(BankAccount.prefix_text())
