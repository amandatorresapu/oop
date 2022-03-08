# class User:		# here's what we have so far
#     def __init__(self, name, last):
#         self.name = name
#         self.last = last

        
#     # adding the deposit method
#     def greeting(self):	# takes an argument that is the amount of the deposit
#     	print(f"hello my name is {self.name}!")
        
# amanda = User("Amanda", "torres")
# amanda.greeting()	# the specific user's account increases by the amount of the value received




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
        return self
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount
        return self
    def display_user_balance(self): 
        print(f"user {self.name}{self.last} {self.account_balance}")
        return self

guido = User("guido","smith")
monty = User("monty", "python")
amanda = User("Amanda", "Torres")

amanda.make_withdrawal(100).make_deposit(50)
# guido.make_withdrawal(100)
# guido.make_deposit(100)
# guido.make_deposit(100)
# guido.make_deposit(50)
# monty.make_withdrawal(50)
# monty.make_deposit(50)
# monty.make_deposit(50)
# amanda.make_deposit(150)
# amanda.make_deposit(150)
# amanda.make_deposit(150)
# amanda.make_withdrawal(10)
amanda.display_user_balance()

# print(guido.account_balance)	
# print(monty.account_balance)
# print(amanda.account_balance)	

# base cass

# class Animal:
#     def __init__(self, name, color, age, size = "large",  ):
#         self.name = name 
#         self.color = color
#         self.size = size 
#         self.age = age
#     # methods (actions that the instances of the class can take)
#     def sleep(self):
#         print(f"{self.name} is sleeping")
#     def eat(self):
#         print(f"{self.name} is eating its favorite color: {self.color}")
    
#     @classmethod
#     def age_from_birth_year(cls, color, name, birth_year, size = "small"):
#         return cls(color, name, date.today().year - birth.year, small)

# # always check for the name (self) order or do what is outlined in the second cat example
# my_cat = Animal("kiwi", "grey & white", "1", "small")
# # (if you are getting them out of order, this is anoter way to do it)--> second_cat = Animal(name = "bootsie", color = "black and white", size = "small")

# # print(my_cat.size)
# # # this is how you would access all of the selfs...values from a give 
# # print(f"my cats name is {my_cat.name}, it is a {my_cat.size} cat, and the colors are {my_cat.color}")

# my_cat.sleep()
# my_cat.eat()

# mr_cat = Animal.age_from_birth_year("brown & grey", "Mister", 2019,)

# print(mr_cat.age)