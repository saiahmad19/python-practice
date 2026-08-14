class bankaccount:
    def __init__(self, owner, starting_balance):
            self.owner = owner
            self.balance = starting_balance

    def deposit(self, amount):
          self.balance = self.balance + amount

    def withdraw(self, amount):

        if amount > self.balance:
          print("not enough funds")
        else:
          self.balance = self.balance - amount

    def show_balance(self):
        return f"{self.owner}'s balance : {self.balance}"

acc1 = bankaccount("sai", 100)
acc1.deposit(300)
acc1.withdraw(200)
print(acc1.show_balance())
acc1.withdraw(500)
print(acc1.show_balance())

acc2 = bankaccount("ali", 1000)
acc2.deposit(500)
print(acc2.show_balance())
acc2.withdraw(500)
print(acc2.show_balance())
acc2.withdraw(300)
print(acc2.show_balance())

