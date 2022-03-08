from ast import alias


class Superhero:
    def __init__(self, name, alias, ability, species, weakness, origin):
        self.name = name
        self.alias = alias
        self.ability = ability
        self.species = species
        self.weakness = weakness
        self.origin = origin


#METHODS
    def power(self):
        print(f"{self.name} AKA {self.alias}  uses {self.ability}")
    
    def attacked(self):
        print(f"{self.name} AKA {self.alias} is hit by {self.weakness}")

    def win(self):
        print(f"{self.alias} has saved {self.origin} once again!")




#instance
superhero1 = Superhero("ethan","ETREE", "super omega farm", "flora", "fire", " the redwoods")
superhero2 = Superhero("chad", "Whey-Boy", "superego", "a bro", "Intelligence", "the gym")
superhero3 = Superhero("Janice", "Moxie", "mind control", "human", "O intelligence people", "Alabama")


#actions
superhero1.power()

superhero2.attacked()

superhero3.win()
