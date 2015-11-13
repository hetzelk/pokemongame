difficulty1 = {1:{'Pokemon': 'Balbasaur', 'move1': 'Tackle', 'move2': 'Razor', 'move3': 'Heal', 'health':100},2:{'Pokemon': 'Charmander', 'move1': 'Scratch', 'move2': 'Ember', 'move3': 'Heal', 'health':100},3:{'Pokemon': 'Squirtle', 'move1': 'Tackle', 'move2': 'Bubble', 'move3': 'Heal', 'health':100}}
difficulty2 = {1:{'Pokemon': 'Ivysaur', 'move1': 'Tackle', 'move2': 'Razor', 'move3': 'Heal', 'health':200},2:{'Pokemon': 'Charmeleon', 'move1': 'Scratch', 'move2': 'Ember', 'move3': 'Heal', 'health':200},3:{'Pokemon': 'Wartortle', 'move1': 'Tackle', 'move2': 'Bubble', 'move3': 'Heal', 'health':200}}
difficulty3 = {1:{'Pokemon': 'Venusaur', 'move1': 'Tackle', 'move2': 'Razor', 'move3': 'Heal', 'health':300},2:{'Pokemon': 'Charizard', 'move1': 'Scratch', 'move2': 'Ember', 'move3': 'Heal', 'health':300},3:{'Pokemon': 'Blastoise', 'move1': 'Tackle', 'move2': 'Bubble', 'move3': 'Heal', 'health':300}}



"""
balbasaur = {'Pokemon': 'Balbasaur', 'move1': 'Tackle', 'move2': 'Razor', 'move3': 'Heal', 'health':100}
ivysaur =   {'Pokemon': 'Ivysaur', 'move1': 'Tackle', 'move2': 'Razor', 'move3': 'Heal', 'health':200}
venusaur =  {'Pokemon': 'Venusaur', 'move1': 'Tackle', 'move2': 'Razor', 'move3': 'Heal', 'health':300}

charmander = {'Pokemon': 'Charmander', 'move1': 'Scratch', 'move2': 'Ember', 'move3': 'Heal', 'health':100}
charmeleon = {'Pokemon': 'Charmeleon', 'move1': 'Scratch', 'move2': 'Ember', 'move3': 'Heal', 'health':200}
charizard =  {'Pokemon': 'Charizard', 'move1': 'Scratch', 'move2': 'Ember', 'move3': 'Heal', 'health':300}

squirtle =  {'Pokemon': 'Squirtle', 'move1': 'Tackle', 'move2': 'Bubble', 'move3': 'Heal', 'health':100}
wartortle = {'Pokemon': 'Wartortle', 'move1': 'Tackle', 'move2': 'Bubble', 'move3': 'Heal', 'health':200}
blastoise = {'Pokemon': 'Blastoise', 'move1': 'Tackle', 'move2': 'Bubble', 'move3': 'Heal', 'health':300}







import time, os, random
from pokedex import * 




class Player1():
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
        print("[B]albasaur, Grass-Type")
        print("[C]harmander, Fire-Type")
        print("[S]quirtle, Water-Type")
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


    def attack(self):
        attacks = input("Select a move")



class Player2():
    def __init__(self):
        name = ("CPU")
        self.name = name
        self.pokedict = self.oaklabchoice()
        self.pokemon = self.getname()
        self.health = self.gethealth()
        self.move1 = self.getmove1()
        self.move2 = self.getmove2()
        self.move3 = self.getmove3()

    def oaklabchoice(self):
        cpuchoices = ['B', 'C', 'S']
        pokechoice = random.choice(cpuchoices)

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









def battle(Player1, Player2):
    print("Opponent wants to battle!")
    print("Opponent sent", player2.pokemon, "!")
    while player1.health > 0 and player2.health > 0:
        
        player1.attack() ##############################################this is where I left off, the next thing to do was select a move out of a list.
        if player2.health <= 0:
            break
        print(player2, "2You have 0 health!")

        player2.attack()
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
    print("| |_) / _ \| |/ / _ \ '_ ` _ \ / _ \| '_ \ ")
    print("|  __/ (_) |   <  __/ | | | | | (_) | | | |")
    print("|_|   \___/|_|\_\___|_| |_| |_|\___/|_| |_|")
    print("")
    print("Name:",player1.name)
    print("Pokemon:",player1.pokemon)
    print("Health:",player1.health)
    print("Name:",player2.name)
    print("Pokemon:",player2.pokemon)
    print("Health:",player2.health)
    #print("Move 1:",player1.move1,"- Move 2:",player1.move2,"- Move 3:",player1.move3)
    print("")

    battle(Player1(), Player2())


os.system("cls")
showpokemonascii()
intro()
player1 = Player1()
player2 = Player2()
main()




"""
