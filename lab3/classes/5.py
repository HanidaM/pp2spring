
class account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        deposit = int(input())
        return self.balance + deposit

    def withdraw(self):
        withdraw = int(input())
        if withdraw > self.balance:
            return 'Your balance is low'
        else:
            return self.balance - withdraw

name = input("Type your name: ")
user = account(name, 25000)

print(user.withdraw())