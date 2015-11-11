import time, os, random
from pokedex import * 




class Pokemon:
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
class Character:
    def __init__(self, health):
        self.health = health

    def attack(self, other):
        raise NotImplementedError
"""

class Player1(Pokemon):
    def __init__(self, health=100):
        super().__init__(health)


class Player2(Pokemon):
    def __init__(self, health=100):
        super().__init__(health)









def battle(Player1, Player2):
    print("Opponent wants to battle!")
    print("Opponent sent", pokemon)
    while player1.health > 0 and player2.health > 0:
        
        player1.attack(player2)
        if player2.health <= 0:
            break
        print(player2, "2You have 0 health!")

        player2.attack(player1)
        if player1.health <= 0:
            break
        print(player1, "1You have 0 health!")



    if player1.health > 0:
        print(player1,", you defeated",player2,"!")
    if player2.health > 0:
        print(player2,", you were defeated",player1,"!")





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
    battle(Player1(), Player2())


os.system("cls")
showpokemonascii()
intro()
star = Pokemon()
main()





