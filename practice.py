# class User:		# here's what we have so far
#     def __init__(self, name, last):
#         self.name = name
#         self.last = last

        
#     # adding the deposit method
#     def greeting(self):	# takes an argument that is the amount of the deposit
#     	print(f"hello my name is {self.name}!")
        
# amanda = User("Amanda", "torres")
# amanda.greeting()	# the specific user's account increases by the amount of the value received

from unicodedata import name


# class User:		# here's what we have so far
#     def __init__(self, name, last):
#         self.name = name
#         self.last = last
#         self.account_balance = 0
        
#     # adding the deposit method
#     def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
#         self.account_balance += amount
# guido = User("guido","smith")
# monty = User("monty", "python")

# guido.make_deposit(100)
# guido.make_deposit(200)
# monty.make_deposit(50)
# print(guido.account_balance)	# output: 300
# print(monty.account_balance)	# output: 50

class User:		# here's what we have so far
    def __init__(self, name, last):
        self.name = name
        self.last = last
        self.account_balance = 300
        
    # adding the deposit method
    def make_withdrawal(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance -= amount
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount
    def display_user_balance(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance = amount

guido = User("guido","smith")
monty = User("monty", "python")
amanda = User("Amanda", "Torres")

guido.make_withdrawal(100)
guido.make_deposit(100)
guido.make_deposit(100)
guido.make_deposit(50)
monty.make_withdrawal(50)
monty.make_deposit(50)
monty.make_deposit(50)
amanda.make_deposit(150)
amanda.make_deposit(150)
amanda.make_deposit(150)
amanda.make_withdrawal(10)
print(guido.account_balance)	
print(monty.account_balance)
print(amanda.account_balance)	

