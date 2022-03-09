class BankAccount:
    def __init__(self, int_rate =.02, balance=200): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance:$ {self.balance}")
        return self

    def yield_interest(self):
        interest = (self.balance * self.int_rate)
        self.balance += interest
        return self

amanda = BankAccount(.02, 500)
teola = BankAccount(.03, 500)
max = BankAccount(.01, 500)


amanda.deposit(50).deposit(50).deposit(50).withdraw(50).yield_interest().display_account_info()
teola.deposit(50).deposit(50).deposit(50).withdraw(50).yield_interest().display_account_info()
max.deposit(50).deposit(50).deposit(50).withdraw(50).yield_interest().display_account_info()

