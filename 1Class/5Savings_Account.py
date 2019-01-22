from Account import BankAccount


class SavingAccount(BankAccount):

    prefix = 'SAVING:'

    def __init__(self, newname, interest):
        super().__init__(newname, 0)
        self.__interest = interest

    @property
    def interest_rate(self):
        return self.__interest

    @interest_rate.setter
    def interest_rate(self, interest):
        self.__interest = interest

    def add_interest(self):
        self.balance *= self.interest_rate

    def withdraw(self, amount):
        print('**extra identification step approved**')
        super().withdraw(amount)


if __name__ == '__main__':
    b = SavingAccount('Ram', interest=1.03)
    print(b)

    b.deposit(1000)
    print(b)

    b.withdraw(500)
    print(b)

    b.add_interest()
    print(b)

    b.interest_rate = 1.06    
    b.add_interest()
    print(b)


