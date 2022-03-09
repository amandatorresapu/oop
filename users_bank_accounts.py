class User:		# here's what we have so far
    def __init__(self, name, last):
        self.name = name
        self.last = last
        self.account = 300
        
    # adding the deposit method
    def make_withdrawal(self, amount):	# takes an argument that is the amount of the deposit
        self.account -= amount
        return self
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account += amount
        return self
    def display_user_balance(self): 
        print(f"user {self.name}{self.last} {self.account}")
        return self

    def transfer_money(self, amount, user):
        self.account -= amount
        user.account += amount
        self.display_user_balance()
        user.display_user_balance()


guido = User("guido","smith")
monty = User("monty", "python")
amanda = User("Amanda", "Torres")


amanda.make_withdrawal(100).make_deposit(200).display_user_balance()


