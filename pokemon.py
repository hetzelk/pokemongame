import time, os, random
from pokedex import * 




def multiplayer():
    print("Would you like to play against the computer or a friend?")
    print("[1] - Vs. Computer")
    print("[2] - Vs. Friend")
    multiplayerchoice = int(input("Select: "))
    if multiplayerchoice == 1:
        return 1
    elif multiplayerchoice ==2:
        return 2
    else:
        print("Please enter the right option. 1 or 2? ")
        print("")
        return difficulty()

def difficulty():
    print("Please select a difficulty.")
    print("[1]00, Health")
    print("[2]00, Health")
    print("[3]00, Health")
    difchoice = int(input("Level 1, 2, or 3? "))

    if difchoice == 1:
        return difficulty1   
    elif difchoice == 2:
        return difficulty2
    elif difchoice == 3:
        return difficulty3
        """
    elif difchoice == 4:
        return difficulty2
    elif difchoice == 5:
        return difficulty3
    elif difchoice == 10:
        return difficulty2
    elif difchoice == 100:
        return difficulty3"""

    else:
        print("Please enter the right option. 1, 2, or 3? ")
        print("")
        return difficulty()

multiplayer = multiplayer()
difficulty = difficulty()

class Player1():
    def __init__(self, multiplayer, difficulty):
        self.playername = 0
        self.multiplayer = multiplayer
        self.difficulty = difficulty #difficulty1, 2, 3
        self.pokemon = 0
        self.name1 = 0
        self.name2 = 0
        self.name3 = 0
        self.pokedict = 0
        self.pokechoice = 0
        self.health = 0
        self.battlehealth = 0
        self.move1 = 0
        self.move2 = 0
        self.move3 = 0

    def getplayername(self):
        self.playername = input("Please enter your name. ")

    def getnamechoices(self):
        chardict = self.difficulty
        pokemon1 = chardict[1]
        pokemon2 = chardict[2]
        pokemon3 = chardict[3]

        self.name1 = pokemon1['Pokemon']
        self.name2 = pokemon2['Pokemon']
        self.name3 = pokemon3['Pokemon']

    def pokemonchoice(self):
        chardict = self.difficulty
        pokechoice = 0
        print(self.playername,"make your choice of Pokemon. ")
        print("[1]", self.name1, "- Leaf-Type")
        print("[2]", self.name2, "- Fire-Type")
        print("[3]", self.name3, "- Water-Type")
        pokechoice = str(input("Pokemon 1, 2 or 3. "))

        if pokechoice == "1":
            print("")
            print(self.playername, "picked", self.name1)
            self.pokedict = chardict[1]
            self.pokemon = self.name1
        elif pokechoice == "2":
            print("")
            print(self.playername, "picked", self.name2)
            self.pokedict = chardict[2]
            self.pokemon = self.name2
        elif pokechoice == "3":
            print("")
            print(self.playername, "picked", self.name3)
            self.pokedict = chardict[3]
            self.pokemon = self.name3
        elif pokechoice != "1" or "2" or "3":
            print("Please enter the right option. 1, 2, or 3? ")
            print("")
            return self.pokemonchoice()


    def gethealth(self):
        pokemon = self.pokedict
        self.health = pokemon['health']

    def getmove1(self):
        pokemon = self.pokedict
        self.move1 = pokemon['move1']

    def getmove2(self):
        pokemon = self.pokedict
        self.move2 = pokemon['move2']

    def getmove3(self):
        pokemon = self.pokedict
        self.move3 = pokemon['move3']


    def attack(self):
        moves = {'move1':random.randint(15,25),'move2':random.randint(5,35),'move3':random.randint(10,20)}
        

        print("Your current health is:", self.health)
        print("[1]", self.move1)
        print("[2]", self.move2)
        print("[3]", self.move3)
        attacks = int(input("Select a move: "))

        if attacks == 1:
            print(self.playername, "used", self.move1)
            self.move = self.move1
        elif attacks == 2:
            print(self.playername, "used", self.move2)
            self.move = self.move2
        elif attacks == 3:
            print(self.playername, "used", self.move3)
            self.move = self.move3
        else:
            print("Please enter a correct choice.")
            return self.attack()


class Player2():
    def __init__(self, multiplayer, difficulty):
        self.playername = 0
        self.multiplayer = multiplayer
        self.difficulty = difficulty #difficulty1, 2, 3
        self.pokemon = 0
        self.name1 = 0
        self.name2 = 0
        self.name3 = 0
        self.pokedict = 0
        self.pokechoice = 0
        self.health = 0
        self.battlehealth = 0
        self.move1 = 0
        self.move2 = 0
        self.move3 = 0

    def getplayername(self):
        if multiplayer == 1:
            self.playername = "Computer"
        else:
            self.playername = input("Please enter your name. ")

    def getnamechoices(self):
        chardict = self.difficulty
        pokemon1 = chardict[1]
        pokemon2 = chardict[2]
        pokemon3 = chardict[3]

        self.name1 = pokemon1['Pokemon']
        self.name2 = pokemon2['Pokemon']
        self.name3 = pokemon3['Pokemon']

    def pokemonchoice(self):
        chardict = self.difficulty

        pokechoice = random.randint(1,3)

        if pokechoice == 1:
            print("")
            print(self.playername, "picked", self.name1)
            self.pokedict = chardict[1]   
            self.pokemon = self.name1
        elif pokechoice == 2:
            print("")
            print(self.playername, "picked", self.name2)
            self.pokedict = chardict[2]
            self.pokemon = self.name2
        elif pokechoice == 3:
            print("")
            print(self.playername, "picked", self.name3)
            self.pokedict = chardict[3]
            self.pokemon = self.name3


    def gethealth(self):
        pokemon = self.pokedict
        self.health = pokemon['health']
        self.battlehealth = pokemon['health']
    def getmove1(self):
        pokemon = self.pokedict
        self.move1 = pokemon['move1']
    def getmove2(self):
        pokemon = self.pokedict
        self.move2 = pokemon['move2']
    def getmove3(self):
        pokemon = self.pokedict
        self.move3 = pokemon['move3']

    def attack(self):
        moves = {'move1':random.randint(15,25),'move2':random.randint(5,35),'move3':random.randint(10,20)}
        

        print(self.playername, "current health is:", self.health)

        attacks = random.randint(1,100)

        healpercent = self.health * .20

        if self.battlehealth <= healpercent:
            print(self.playername, "used", self.move3)
            self.move = self.move3
        else:
            if attacks >= 85:
                print(self.playername, "used", self.move3)
                self.move = self.move3
            elif attacks >= 50:
                print(self.playername, "used", self.move2)
                self.move = self.move2
            elif attacks >= 1:
                print(self.playername, "used", self.move1)
                self.move = self.move1









def battle(Player1, Player2):
    print("Opponent wants to battle!")
    print("Opponent sent", comp.pokemon, "!")
    while player.battlehealth > 0 and comp.battlehealth > 0:
        
        print("")
        player.attack() ##############################################this is where I left off, the next thing to do was select a move out of a list.
        if comp.battlehealth <= 0:
            print(comp.playername, "2You have 0 health!")
            break

        print("")
        comp.attack()
        if player.battlehealth <= 0:
            print(player.playername, "1You have 0 health!")
            break


    if player.battlehealth > 0:
        print(player.playername,", you were defeated by",comp.playername,"!")
    if comp.battlehealth > 0:
        print(comp.playername,", you were defeated by",player.playername,"!")





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



def run():
    os.system("cls")
    print(" ____       _                              ")
    print("|  _ \ ___ | | _____ _ __ ___   ___  _ __  ")
    print("| |_) / _ \| |/ / _ \ '_ ` _ \ / _ \| '_ \ ")
    print("|  __/ (_) |   <  __/ | | | | | (_) | | | |")
    print("|_|   \___/|_|\_\___|_| |_| |_|\___/|_| |_|")
    print("")
    print("")
    player.getplayername()
    print("")
    #print("player # choice",player.multiplayer, "this is the dict for difficulty",player.difficulty)
    print("")
    player.getnamechoices()
    player.pokemonchoice()
    player.gethealth()
    player.getmove1()
    player.getmove2()
    player.getmove3()
    print("Starting Health: ",player.health)
    print("Move 1:",player.move1,"- Move 2:",player.move2,"- Move 3:",player.move3)
    print("")

    comp.getplayername()
    comp.getnamechoices()
    comp.pokemonchoice()
    comp.gethealth()
    comp.getmove1()
    comp.getmove2()
    comp.getmove3()
    print("Computer starting Health: ",comp.health)
    print("Com Move 1:",comp.move1,"- Com Move 2:",comp.move2,"- Com Move 3:",comp.move3)
    print("")
    print("")
    print("")
    #player.attack()
    #comp.attack()



os.system("cls")
showpokemonascii()

#intro()
player = Player1(multiplayer, difficulty)
#player2 =Player()
comp = Player2(multiplayer, difficulty)
run()

battle(Player1, Player2)


