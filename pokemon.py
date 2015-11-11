import time, os, random
from pokedex import * 


class Character:
    def __init__(self, health):
        self.health = health

    def attack(self, other):
        raise NotImplementedError


class Player1(Character):
    def __init__(self, health=100):
        super().__init__(health)


class Player2(Character):
    def __init__(self, health=100):
        super().__init__(health)




class Pokemon(object):
    def __init__(self):
        name = str(input("What is your name? "))
        self.name = name
        self.pokedict = self.oaklabchoice()
        self.pokemon = self.getname()
        self.health = self.gethealth()
        self.move1 = self.getmove1()
        self.move2 = self.getmove2()
        self.move3 = self.getmove3()


    def oaklabchoice(self):
        print("B for Balbasaur, Grass-Type")
        print("C for Charmander, Fire-Type")
        print("S for Squirtle, Water-Type")
        pokechoice = str(input('"B," "C," or "S." Make your choice. ')).upper()

        if pokechoice == "B":
            return balbasaur   
        if pokechoice == "C":
            return charmander
        if pokechoice == "S":
            return squirtle
        else:
            print("Please try again, B, C, or S. ")
            self.oaklabchoice()

    def getname(self):
        pokemon = self.pokedict
        return pokemon['Pokemon']

    def gethealth(self):
        pokemon = self.pokedict
        return pokemon['health']

    def getmove1(self):
        pokemon = self.pokedict
        return pokemon['move1']

    def getmove2(self):
        pokemon = self.pokedict
        return pokemon['move2']

    def getmove3(self):
        pokemon = self.pokedict
        return pokemon['move3']





"""

class Status():
    def __init__(self, name, health, oaklabchoice):
        self.name = name
        self.health = health
        self.pokemon = oaklabchoice
    def __str__(self):
        return "{} - {} \nHealth: {}\n".format(self.name, self.pokemon, self.health)

class Enemy(Status):
    def __init__(self):
        self.name = "Will"
        self.health = "100"
        self.pokemon = "Blastoise"
        #super().__init__(name = "Hydrogen", health = "H", pokemon = "1")
"""




def main():
    print("")
    print("Your name is:",star.name)
    print("You chose:",star.pokemon)
    print("It's health:",star.health)
    print("Move 1:",star.move1)
    print("Move 2:",star.move2)
    print("Move 3:",star.move3)



star = Pokemon()
main()





