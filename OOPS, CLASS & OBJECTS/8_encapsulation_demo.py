# Demonstrating encapsulation and controlled access to object data

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Deposited {amount}. New balance: {self.__balance}')

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f'Withdrew {amount}. Remaining balance: {self.__balance}')
        else:
            print('Withdrawal failed: invalid amount or insufficient funds')

    def get_balance(self):
        return self.__balance

account = BankAccount('Riya', 1000)
account.deposit(500)
account.withdraw(300)
print('Balance:', account.get_balance())
