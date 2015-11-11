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
        pokechoice = str(input('B, C, or S. Make your choice. ')).upper()

        if pokechoice == "B":
            return balbasaur   
        if pokechoice == "C":
            return charmander
        if pokechoice == "S":
            return squirtle
        elif pokechoice != "B" or "C" or "S":
            print("Please try again, B, C, or S. ")
            print("")
            return self.oaklabchoice()

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


def showpokemonascii():
    print(" ____       _                              ")
    print("|  _ \ ___ | | _____ _ __ ___   ___  _ __  ")
    print("| |_) / _ \| |/ / _ \ '_ ` _ \ / _ \| '_ \ ")
    print("|  __/ (_) |   <  __/ | | | | | (_) | | | |")
    print("|_|   \___/|_|\_\___|_| |_| |_|\___/|_| |_|")
    print("")

def intro():
    print("Welcome to the pokemon world.")
    print("There are 3 difficulty levels.")
    print("You can face the computer or a friend.")
    print("You take turns with your opponent.")
    print("You have 3 different moves you can choose from.")
    print("")
    print("")

def main():
    os.system("cls")
    print(" ____       _                              ")
    print("|  _ \ ___ | | _____ _ __ ___   ___  _ __  ")
    print("| |_) / _ \| |/ / _ \ '_ ` _ \ / _ \| '_ \ ",star.name)
    print("|  __/ (_) |   <  __/ | | | | | (_) | | | |",star.pokemon)
    print("|_|   \___/|_|\_\___|_| |_| |_|\___/|_| |_|",star.health)
    print("")
    print("Move 1:",star.move1,"- Move 2:",star.move2,"- Move 3:",star.move3)
    print("")


os.system("cls")
showpokemonascii()
intro()
star = Pokemon()
main()





